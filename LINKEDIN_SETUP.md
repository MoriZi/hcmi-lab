# LinkedIn homepage feed

The homepage reads the four latest posts from the HCMI Lab company page during each site build. The fetch script keeps the LinkedIn access token on the build machine and writes only the post text and public post links into an ignored Hugo data file. If LinkedIn is unavailable, a previous snapshot in the same working copy is retained; a clean build with no snapshot uses the bundled fallback post.

## LinkedIn access needed

LinkedIn does not expose organization posts to an unauthenticated public feed. This integration uses the official [Posts API](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api) and requires:

- A LinkedIn developer app approved for Community Management API access with the `r_organization_social` permission.
- An OAuth token authorized by a member who has an administrator, content administrator, or direct sponsored content poster role on the HCMI Lab page.
- The numeric HCMI Lab company page ID. A page administrator can find it in the company page's admin view.

## Configure build credentials

For regular automatic token renewal, enable LinkedIn programmatic refresh tokens for the app and set these environment variables in the build environment:

```text
LINKEDIN_CLIENT_ID
LINKEDIN_CLIENT_SECRET
LINKEDIN_REFRESH_TOKEN
LINKEDIN_ORGANIZATION_ID
```

The refresh token lasts one year and needs to be reauthorized when it expires. If the app does not have refresh-token access, set `LINKEDIN_ACCESS_TOKEN` instead; LinkedIn access tokens last 60 days and must be renewed manually. Never put these values in the repository or in a file under `static/`.

`LINKEDIN_API_VERSION` is optional. The integration currently defaults to `202608` and can be set to another supported version if LinkedIn retires that version.

The fetch runs from `deploy.sh`, Netlify builds, and the GitHub build workflow. Without credentials, the bundled post remains visible and the section still links to the HCMI Lab LinkedIn page. A failed API request leaves the last fetched snapshot in place.
