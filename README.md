# API Evangelist Providers (api-evangelist-providers)
An alphabetical listing of every provider tracked across the API Evangelist network.

**URL:** [Visit APIs.json URL](https://github.com/api-evangelist/providers/blob/main/apis.yml)

## Scope

- **Type:** Providers
- **Position:** Consuming
- **Access:** 3rd-Party

## Tags

- Providers

## Timestamps

- **Created:** 2024-10-14
- **Modified:** 2026-06-03

## Listing

The site is a static, alphabetically-grouped index (A–Z plus 0-9) of all provider
repositories under `all/*`. There are no detail pages — each provider links out to:

- its **APIs.io provider page** (`https://providers.apis.io/providers/<slug>/`) when the
  provider has an API listed (i.e. it appears in `api-search/providers/_providers/`), or
- its **GitHub repository** (`https://github.com/api-evangelist/<slug>`) otherwise.

The listing data is generated into `_data/companies.json` by `scripts/build-listing.py`,
which scans `all/*` (provider repos) and `api-search/providers/_providers/*` (provider
listings). Re-run it to refresh the index:

```
python3 scripts/build-listing.py
```

This site is static — there is no API backend. The listing is generated at build
time from local repositories and deployed as plain HTML + a static `apis.json` feed.

## Editing `_data/` — read this first

Jekyll does **not** parse `_data/*.json` with a JSON parser. It hands them to
SafeYAML → Psych, and YAML is stricter than JSON: it accepts `\uXXXX` only for the
Basic Multilingual Plane and rejects the surrogate-pair escapes JSON uses for
anything above U+FFFF. A file can be perfectly valid JSON and still kill the entire
Pages build before one page renders — which is what a single emoji in one provider
description, written by a bare `json.dump`, did on 2026-08-11.

So: **anything that rewrites a file under `_data/` must go through `dump_json()` in
`scripts/build-listing.py`**, which desurrogates and writes `ensure_ascii=False`.
Never a bare `json.dump` (its default `ensure_ascii=True` is the trap).

Two guards enforce this:

```bash
ruby scripts/check-data.rb        # parse every data file the way Pages will
git config core.hooksPath .githooks   # run that check automatically pre-commit
```

The second line is **required once per clone** — `core.hooksPath` lives in
`.git/config` and is not versioned. `.github/workflows/validate-data.yml` is the
backstop if it was never run; it reports in ~1 minute instead of the ~25 the Pages
build takes to tell you.

## Properties

- [GitHubRepository](https://github.com/api-evangelist/providers)
- [Documentation](https://developer.apievangelist.com/documentation/)

## Common Properties

- [GitHubOrganization](https://github.com/api-evangelist/)

## Maintainers

**FN:** Kin Lane

**Email:** info@apievangelist.com
