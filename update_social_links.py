#!/usr/bin/env python3
"""
Script to update Google Scholar and LinkedIn links for authors.
Uses a predefined mapping of names to URLs.
"""

import re
import yaml
from pathlib import Path

# Mapping of author names to their social links
# Format: (name_key, google_scholar_url, linkedin_url)
SOCIAL_LINKS = {
    "morteza-zihayat": (
        "https://scholar.google.com/citations?user=lZ8oEM8AAAAJ&hl=en",
        "https://ca.linkedin.com/in/morteza-zihayat"
    ),
    "ebrahim-bagheri": (
        "https://scholar.google.com/citations?user=mG0H8oYAAAAJ&hl=en",
        "https://ca.linkedin.com/in/ebrahim-bagheri-6330841"
    ),
    "mehdi-kargar": (
        "https://scholar.google.com/citations?user=aYRWbNsAAAAJ&hl=en",
        "https://ca.linkedin.com/in/mehdi-kargar"
    ),
    "nancy-yang": (
        "https://scholar.google.com/citations?user=KKqs9sUAAAAJ&hl=en",
        "https://ca.linkedin.com/in/xingweinancyyang"
    ),
    "shayan-alipour": (
        "https://scholar.google.com/citations?user=ex9m4ksAAAAJ&hl=en",
        "https://ca.linkedin.com/in/shayanalip"
    ),
    "mina-soltangheis": (
        "https://scholar.google.com/citations?user=RBE3ctMAAAAJ&hl=en",
        "https://www.linkedin.com/in/minasoltangheis/"
    ),
    "wendi-zhou": (
        None,  # No Google Scholar provided
        "https://www.linkedin.com/in/wendi-zhou-5b223b40"
    ),
    "hai-son-le": (
        "https://scholar.google.com/citations?user=JuJhGLMAAAAJ&hl=en",
        "https://www.linkedin.com/in/haisonle01/"
    ),
    "mohammad-hosseini": (
        "https://scholar.google.com/citations?user=hbgJnN0AAAAJ&hl=en",
        "https://www.linkedin.com/in/mhoseyny/"
    ),
    "niloufar-naeeni": (
        "https://scholar.google.com/citations?user=X4_logIAAAAJ&hl=en",
        "https://www.linkedin.com/in/niloufar-naeeni/"
    ),
}

def parse_markdown_frontmatter(file_path: Path):
    """Parse markdown file with YAML frontmatter."""
    content = file_path.read_text(encoding='utf-8')
    
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

def update_social_links(file_path: Path, google_scholar: str = None, linkedin: str = None) -> bool:
    """
    Update social links in the author file.
    Returns True if updated, False otherwise.
    """
    frontmatter, body = parse_markdown_frontmatter(file_path)
    
    if 'social' not in frontmatter:
        frontmatter['social'] = []
    
    updated = False
    
    # Update or add Google Scholar link
    if google_scholar:
        gs_found = False
        for item in frontmatter['social']:
            if isinstance(item, dict) and item.get('icon') == 'google-scholar':
                if item.get('link') != google_scholar:
                    item['link'] = google_scholar
                    updated = True
                gs_found = True
                break
        
        if not gs_found:
            frontmatter['social'].append({
                'icon': 'google-scholar',
                'icon_pack': 'ai',
                'link': f'"{google_scholar}"' if '?' in google_scholar or '&' in google_scholar else google_scholar
            })
            updated = True
    
    # Update or add LinkedIn link
    if linkedin:
        li_found = False
        for item in frontmatter['social']:
            if isinstance(item, dict) and item.get('icon') == 'linkedin':
                if item.get('link') != linkedin:
                    item['link'] = linkedin
                    updated = True
                li_found = True
                break
        
        if not li_found:
            frontmatter['social'].append({
                'icon': 'linkedin',
                'icon_pack': 'fab',
                'link': f'"{linkedin}"' if '?' in linkedin or '&' in linkedin else linkedin
            })
            updated = True
    
    if not updated:
        return False
    
    # Reconstruct file - ensure URLs are properly quoted
    # Convert link values to strings and quote if needed
    for item in frontmatter.get('social', []):
        if isinstance(item, dict) and 'link' in item:
            link = item['link']
            # Remove existing quotes if any, then add quotes for URLs with special chars
            if isinstance(link, str):
                link = link.strip('"\'')
                if '?' in link or '&' in link or link.startswith('http'):
                    item['link'] = f'"{link}"'
    
    frontmatter_yaml = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
    new_content = f"---\n{frontmatter_yaml}---\n{body}"
    
    file_path.write_text(new_content, encoding='utf-8')
    return True

def main():
    """Main function to update all author files."""
    authors_dir = Path("content/authors")
    
    if not authors_dir.exists():
        print(f"Error: {authors_dir} does not exist")
        return
    
    updated_count = 0
    skipped_count = 0
    
    print("Updating social links for authors...\n")
    
    for author_key, (google_scholar, linkedin) in SOCIAL_LINKS.items():
        author_dir = authors_dir / author_key
        index_file = author_dir / "_index.md"
        
        if not index_file.exists():
            print(f"⚠️  Skipping {author_key}: _index.md not found")
            skipped_count += 1
            continue
        
        print(f"Processing: {author_key}")
        
        if google_scholar:
            print(f"  Google Scholar: {google_scholar[:60]}...")
        if linkedin:
            print(f"  LinkedIn: {linkedin[:60]}...")
        
        try:
            if update_social_links(index_file, google_scholar, linkedin):
                print(f"  ✓ Updated {author_key}")
                updated_count += 1
            else:
                print(f"  - No changes needed for {author_key}")
                skipped_count += 1
        except Exception as e:
            print(f"  ✗ Error updating {author_key}: {e}")
            skipped_count += 1
        
        print()
    
    print(f"{'='*60}")
    print(f"Summary:")
    print(f"  Updated: {updated_count}")
    print(f"  Skipped/No changes: {skipped_count}")
    print(f"  Total processed: {len(SOCIAL_LINKS)}")

if __name__ == "__main__":
    main()

