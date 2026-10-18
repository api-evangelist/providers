---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Cookies.com provides an e‑commerce storefront but does not expose a public developer API.
  name: Cookies API
  slug: cookies-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cookies/refs/heads/main/well-known/cookies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cookies-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cookies/refs/heads/main/hosts/cookies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cookies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cookies/refs/heads/main/vendors/cookies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cookies-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cookies/refs/heads/main/security/cookies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cookies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/cookies
coverage:
  checked: '2026-10-11'
  detail: The only discovered site https://cookies.com/password is a Shopify password page with no public API documentation.
  evidence:
  - status: 200
    url: https://cookies.com/password
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-10'
description: Cookies is a stub company listed in the API Evangelist secondary-market harvest. It currently lacks a public-facing website or documented APIs. The profile aims to gather identity information, potential documentation links, and future API specifications as they become available. No concrete product details are present at this time, and the company appears to be a placeholder for further enrichment.
layout: provider
modified: '2026-10-10'
name: Cookies
nav: Providers
network: true
overview: Cookies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Placeholder, and Data.
random_paper: 1
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cookies Domain Security
  slug: cookies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cookies
tags:
- Company
- Placeholder
- Data
website: https://equityzen.com/company/cookies
---
