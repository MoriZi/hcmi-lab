#!/usr/bin/env python3
"""
Script to fetch abstracts for all publications from multiple APIs
and update the markdown files.
"""

import os
import re
import time
import requests
from pathlib import Path
from typing import Optional, Dict, List
import yaml
from urllib.parse import quote
from difflib import SequenceMatcher

# API endpoints
SEMANTIC_SCHOLAR_SEARCH = "https://api.semanticscholar.org/graph/v1/paper/search"
SEMANTIC_SCHOLAR_PAPER = "https://api.semanticscholar.org/graph/v1/paper"
CROSSREF_API = "https://api.crossref.org/works"
ARXIV_API = "http://export.arxiv.org/api/query"

def similarity(a: str, b: str) -> float:
    """Calculate similarity ratio between two strings."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def normalize_title(title: str) -> str:
    """Normalize title for comparison."""
    # Remove special characters, extra spaces
    title = re.sub(r'[^\w\s]', '', title.lower())
    title = re.sub(r'\s+', ' ', title).strip()
    return title

def fetch_by_doi(doi: str) -> Optional[str]:
    """Fetch abstract using DOI from CrossRef or Semantic Scholar."""
    if not doi or doi.strip() == "":
        return None
    
    doi = doi.strip()
    
    # Try Semantic Scholar first (better for CS papers)
    try:
        url = f"{SEMANTIC_SCHOLAR_PAPER}/{quote(doi)}"
        params = {"fields": "title,authors,abstract"}
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            abstract = data.get("abstract")
            if abstract:
                return abstract
    except:
        pass
    
    # Try CrossRef
    try:
        url = f"{CROSSREF_API}/{quote(doi)}"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            message = data.get("message", {})
            abstract = message.get("abstract")
            if abstract:
                # CrossRef abstracts are often in HTML, extract text
                abstract_text = re.sub(r'<[^>]+>', '', abstract)
                if abstract_text.strip():
                    return abstract_text.strip()
    except:
        pass
    
    return None

def fetch_from_semantic_scholar(title: str, authors: List[str], doi: str = None) -> Optional[str]:
    """Fetch abstract from Semantic Scholar using multiple search strategies."""
    
    # Strategy 1: If we have DOI, use it directly
    if doi:
        result = fetch_by_doi(doi)
        if result:
            return result
    
    # Strategy 2: Search by exact title
    queries = [
        title,  # Full title
        title[:100],  # First 100 chars
    ]
    
    # Strategy 3: Add first author to query
    if authors:
        first_author_lastname = authors[0].split()[-1] if len(authors[0].split()) > 0 else authors[0]
        queries.append(f"{title[:80]} {first_author_lastname}")
    
    for query in queries:
        try:
            params = {
                "query": query[:200],
                "limit": 10,  # Get more results
                "fields": "title,authors,abstract,externalIds"
            }
            
            headers = {
                "User-Agent": "HCMI-Lab-Abstract-Fetcher (mailto:your-email@example.com)"
            }
            
            response = requests.get(SEMANTIC_SCHOLAR_SEARCH, params=params, headers=headers, timeout=10)
            
            if response.status_code != 200:
                continue
                
            data = response.json()
            papers = data.get("data", [])
            
            if not papers:
                continue
            
            # Normalize search title
            search_title_norm = normalize_title(title)
            search_authors_norm = [normalize_title(a) for a in authors[:3]]
            
            best_match = None
            best_score = 0.0
            
            for paper in papers:
                paper_title = paper.get("title", "")
                if not paper_title:
                    continue
                
                paper_title_norm = normalize_title(paper_title)
                
                # Calculate title similarity
                title_sim = similarity(search_title_norm, paper_title_norm)
                
                # Check author match
                paper_authors = [author.get("name", "").lower() for author in paper.get("authors", [])]
                author_match = False
                
                for search_author in search_authors_norm:
                    for paper_author in paper_authors:
                        # Check if last name matches or full name is similar
                        search_last = search_author.split()[-1] if search_author.split() else ""
                        paper_last = paper_author.split()[-1] if paper_author.split() else ""
                        
                        if (search_last and paper_last and search_last == paper_last) or \
                           similarity(search_author, paper_author) > 0.7:
                            author_match = True
                            break
                    if author_match:
                        break
                
                # Calculate combined score
                score = title_sim
                if author_match:
                    score += 0.2
                
                if score > best_score and score > 0.6:  # Lower threshold
                    best_score = score
                    best_match = paper
            
            if best_match:
                abstract = best_match.get("abstract")
                if abstract:
                    return abstract
                
                # Try to get by DOI if available
                external_ids = best_match.get("externalIds", {})
                if "DOI" in external_ids:
                    doi_result = fetch_by_doi(external_ids["DOI"])
                    if doi_result:
                        return doi_result
            
        except Exception as e:
            continue
    
    return None

def fetch_from_crossref(title: str, authors: List[str]) -> Optional[str]:
    """Try to fetch from CrossRef as fallback."""
    try:
        # Search by title
        params = {
            "query.title": title[:200],
            "rows": 5
        }
        
        headers = {"Accept": "application/json"}
        response = requests.get(CROSSREF_API, params=params, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return None
        
        data = response.json()
        items = data.get("message", {}).get("items", [])
        
        search_title_norm = normalize_title(title)
        
        for item in items:
            item_title = item.get("title", [""])[0] if item.get("title") else ""
            if not item_title:
                continue
            
            item_title_norm = normalize_title(item_title)
            title_sim = similarity(search_title_norm, item_title_norm)
            
            if title_sim > 0.7:
                abstract = item.get("abstract")
                if abstract:
                    abstract_text = re.sub(r'<[^>]+>', '', abstract)
                    if abstract_text.strip():
                        return abstract_text.strip()
        
        return None
    except:
        return None

def parse_markdown_frontmatter(file_path: Path):
    """
    Parse markdown file with YAML frontmatter.
    
    Returns:
        Tuple of (frontmatter dict, content after frontmatter)
    """
    content = file_path.read_text(encoding='utf-8')
    
    # Match YAML frontmatter
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if not match:
        return {}, content
    
    frontmatter_text = match.group(1)
    body = match.group(2)
    
    try:
        frontmatter = yaml.safe_load(frontmatter_text) or {}
        return frontmatter, body
    except yaml.YAMLError as e:
        print(f"  Error parsing YAML: {e}")
        return {}, content

def update_abstract_in_file(file_path: Path, new_abstract: str) -> bool:
    """
    Update the abstract field in a markdown file.
    
    Returns:
        True if updated, False otherwise
    """
    frontmatter, body = parse_markdown_frontmatter(file_path)
    
    # Check if abstract already exists and is not a placeholder
    current_abstract = frontmatter.get("abstract", "")
    
    # Skip if abstract is already substantial (more than 100 chars and not a placeholder)
    if current_abstract and len(current_abstract) > 100:
        # Check if it's not a generic placeholder
        placeholder_phrases = [
            "this paper presents",
            "this work introduces",
            "this paper introduces",
            "this work presents"
        ]
        if not any(phrase in current_abstract.lower()[:50] for phrase in placeholder_phrases):
            return False
    
    # Update abstract
    frontmatter["abstract"] = new_abstract
    
    # Reconstruct file
    frontmatter_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
    new_content = f"---\n{frontmatter_yaml}---\n{body}"
    
    file_path.write_text(new_content, encoding='utf-8')
    return True

def process_publication_file(file_path: Path) -> bool:
    """
    Process a single publication file to fetch and update abstract.
    
    Returns:
        True if abstract was updated, False otherwise
    """
    print(f"\nProcessing: {file_path.parent.name}")
    
    frontmatter, _ = parse_markdown_frontmatter(file_path)
    
    title = frontmatter.get("title", "")
    authors = frontmatter.get("authors", [])
    doi = frontmatter.get("doi", "").strip()
    
    if not title:
        print("  No title found, skipping")
        return False
    
    if not authors:
        print("  No authors found, skipping")
        return False
    
    print(f"  Title: {title[:70]}")
    if doi:
        print(f"  DOI: {doi}")
    print(f"  Authors: {', '.join(authors[:2])}")
    
    # Try multiple strategies
    abstract = None
    
    # Strategy 1: Try Semantic Scholar (best for CS/ML papers)
    print("  Trying Semantic Scholar...", end=" ")
    abstract = fetch_from_semantic_scholar(title, authors, doi)
    if abstract:
        print(f"✓ Found ({len(abstract)} chars)")
    else:
        print("not found")
    
    # Strategy 2: Try CrossRef as fallback
    if not abstract:
        print("  Trying CrossRef...", end=" ")
        abstract = fetch_from_crossref(title, authors)
        if abstract:
            print(f"✓ Found ({len(abstract)} chars)")
        else:
            print("not found")
    
    if not abstract:
        print("  ✗ No abstract found from any source")
        return False
    
    # Update file
    if update_abstract_in_file(file_path, abstract):
        print("  ✓ Abstract updated in file")
        return True
    else:
        print("  Abstract already exists or is substantial, skipping update")
        return False

def main():
    """Main function to process all publication files."""
    publications_dir = Path("content/publication")
    
    if not publications_dir.exists():
        print(f"Error: {publications_dir} does not exist")
        return
    
    # Get all publication directories
    pub_dirs = [d for d in publications_dir.iterdir() 
                if d.is_dir() and not d.name.startswith('_')]
    
    print(f"Found {len(pub_dirs)} publication directories")
    
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    for pub_dir in sorted(pub_dirs):
        index_file = pub_dir / "index.md"
        
        if not index_file.exists():
            print(f"\nSkipping {pub_dir.name}: no index.md")
            continue
        
        try:
            if process_publication_file(index_file):
                updated_count += 1
            else:
                skipped_count += 1
            
            # Be nice to the API - add delay between requests
            time.sleep(1)
            
        except Exception as e:
            print(f"\nError processing {pub_dir.name}: {e}")
            error_count += 1
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Updated: {updated_count}")
    print(f"  Skipped: {skipped_count}")
    print(f"  Errors: {error_count}")
    print(f"  Total: {len(pub_dirs)}")

if __name__ == "__main__":
    main()

