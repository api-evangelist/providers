# API Evangelist Companies (api-evangelist-companies)
An alphabetical listing of every company tracked across the API Evangelist network.

**URL:** [Visit APIs.json URL](https://github.com/api-evangelist/companies/blob/main/apis.yml)

## Scope

- **Type:** Companies
- **Position:** Consuming
- **Access:** 3rd-Party

## Tags

- Companies

## Timestamps

- **Created:** 2024-10-14
- **Modified:** 2026-06-03

## Listing

The site is a static, alphabetically-grouped index (A–Z plus 0-9) of all company
repositories under `all/*`. There are no detail pages — each company links out to:

- its **APIs.io provider page** (`https://providers.apis.io/providers/<slug>/`) when the
  company has an API listed (i.e. it appears in `api-search/providers/_providers/`), or
- its **GitHub repository** (`https://github.com/api-evangelist/<slug>`) otherwise.

The listing data is generated into `_data/companies.json` by `scripts/build-listing.py`,
which scans `all/*` (company repos) and `api-search/providers/_providers/*` (provider
listings). Re-run it to refresh the index:

```
python3 scripts/build-listing.py
```

This site is static — there is no API backend. The listing is generated at build
time from local repositories and deployed as plain HTML + a static `apis.json` feed.

## Properties

- [GitHubRepository](https://github.com/api-evangelist/companies)
- [Documentation](https://developer.apievangelist.com/documentation/)

## Common Properties

- [GitHubOrganization](https://github.com/api-evangelist/)

## Maintainers

**FN:** Kin Lane

**Email:** info@apievangelist.com
