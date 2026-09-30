#!/usr/bin/env python3
"""Fetch the latest HCMI Lab company posts for the Hugo build."""

import json
import os
import re
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "linkedin_posts_generated.json"
DEFAULT_API_VERSION = "202608"
LINKEDIN_API = "https://api.linkedin.com/rest/posts"
LINKEDIN_TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"


def warn(message):
    print(f"LinkedIn feed: {message}", file=sys.stderr)


def request_json(request, timeout=20):
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def access_token():
    direct_token = os.environ.get("LINKEDIN_ACCESS_TOKEN", "").strip()
    refresh_token = os.environ.get("LINKEDIN_REFRESH_TOKEN", "").strip()
    client_id = os.environ.get("LINKEDIN_CLIENT_ID", "").strip()
    client_secret = os.environ.get("LINKEDIN_CLIENT_SECRET", "").strip()

    refresh_values = (refresh_token, client_id, client_secret)
    if any(refresh_values):
        if not all(refresh_values):
            warn("set LINKEDIN_REFRESH_TOKEN, LINKEDIN_CLIENT_ID, and LINKEDIN_CLIENT_SECRET together; keeping the last fetched feed.")
            return direct_token or None

        body = urlencode({
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": client_id,
            "client_secret": client_secret,
        }).encode("ascii")
        request = Request(
            LINKEDIN_TOKEN_URL,
            data=body,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            method="POST",
        )
        try:
            token_data = request_json(request)
            token = token_data.get("access_token")
            if token:
                return token
            warn("LinkedIn did not return an access token; keeping the last fetched feed.")
        except (HTTPError, URLError, TimeoutError, ValueError) as error:
            warn(f"could not refresh the access token ({error}); keeping the last fetched feed.")

    if direct_token:
        return direct_token

    warn("credentials are not configured; keeping the last fetched feed.")
    return None


def clean_text(value):
    value = re.sub(r"@\[([^\]]+)\]\(urn:li:[^)]+\)", r"\1", value or "")
    value = re.sub(r"\{hashtag\|\\?#\|([^}]+)\}", r"#\1", value)
    return "\n".join(line.strip() for line in value.splitlines() if line.strip()).strip()


def truncate(value, limit):
    value = " ".join((value or "").split())
    if len(value) <= limit:
        return value
    shortened = value[: limit - 1].rsplit(" ", 1)[0].rstrip(" ,;:-")
    return f"{shortened}…"


def card_for(post):
    content = post.get("content") or {}
    article = content.get("article") or {}
    media = content.get("media") or {}
    document = content.get("document") or {}
    commentary = clean_text(post.get("commentary", ""))
    attachment_title = article.get("title") or media.get("title") or document.get("title")
    title = attachment_title or ""

    if not title and commentary:
        first_line = commentary.splitlines()[0]
        title = re.split(r"(?<=[.!?])\s+", first_line, maxsplit=1)[0]
    if not title:
        title = "Latest update from HCMI Lab"

    title = truncate(title, 115)
    description = commentary
    if not attachment_title and description.startswith(title):
        description = description[len(title):].lstrip(" .,:;—–-\n")
    description = description or article.get("description") or "Read the full update on LinkedIn."

    post_id = post.get("id", "")
    if not post_id.startswith(("urn:li:share:", "urn:li:ugcPost:")):
        return None

    return {
        "title": title,
        "text": truncate(description, 210),
        "url": f"https://www.linkedin.com/feed/update/{post_id}/",
    }


def main():
    token = access_token()
    organization_id = os.environ.get("LINKEDIN_ORGANIZATION_ID", "").strip()
    if not organization_id:
        warn("LINKEDIN_ORGANIZATION_ID is not set; keeping the last fetched feed.")
        return
    if not token:
        return

    organization_urn = organization_id
    if organization_id.isdigit():
        organization_urn = f"urn:li:organization:{organization_id}"
    if not organization_urn.startswith("urn:li:organization:"):
        warn("LINKEDIN_ORGANIZATION_ID must be a numeric page ID or organization URN; keeping the last fetched feed.")
        return

    query = urlencode({
        "author": organization_urn,
        "q": "author",
        "count": "4",
        "sortBy": "CREATED",
        "viewContext": "READER",
    })
    api_version = os.environ.get("LINKEDIN_API_VERSION", DEFAULT_API_VERSION).strip() or DEFAULT_API_VERSION
    request = Request(
        f"{LINKEDIN_API}?{query}",
        headers={
            "Authorization": f"Bearer {token}",
            "LinkedIn-Version": api_version,
            "X-Restli-Protocol-Version": "2.0.0",
            "Accept": "application/json",
        },
    )

    try:
        response = request_json(request)
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")[:500]
        warn(f"LinkedIn API request failed ({error.code}): {detail}; keeping the last fetched feed.")
        return
    except (URLError, TimeoutError, ValueError) as error:
        warn(f"could not fetch posts ({error}); keeping the last fetched feed.")
        return

    elements = response.get("elements")
    if not isinstance(elements, list):
        warn("LinkedIn returned an unexpected response; keeping the last fetched feed.")
        return

    posts = []
    for item in elements:
        if item.get("lifecycleState") != "PUBLISHED":
            continue
        card = card_for(item)
        if card:
            posts.append(card)
        if len(posts) == 4:
            break

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps({"posts": posts}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"LinkedIn feed: fetched {len(posts)} post(s) for the homepage.")


if __name__ == "__main__":
    main()
