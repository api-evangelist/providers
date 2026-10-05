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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Nasdaq Private Market platform offering liquidity solutions, investment platform, data & intelligence for private companies and investors.
  name: Beast Enterprises API
  slug: beast-enterprises-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beast-enterprises/refs/heads/main/vendors/beast-enterprises-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beast-enterprises-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beast-enterprises/refs/heads/main/hosts/beast-enterprises-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beast-enterprises-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beast-enterprises/refs/heads/main/security/beast-enterprises-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beast-enterprises-domain-security.yml
coverage:
  checked: '2026-09-27'
  detail: Main website renders content via JavaScript, preventing automated extraction of API specifications.
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Beast Enterprises appears in the API Evangelist harvest as a placeholder entry derived from secondary‑market sources. At present, no public website, corporate landing page, or API documentation can be located for this entity. The available data consists solely of minimal metadata such as the company name and a brief note that it is a stub awaiting further information. This entry is retained in the network to enable future enrichment should verifiable sources, official documentation, or a functional API become discoverable.
layout: provider
modified: '2026-09-27'
name: Beast Enterprises
nav: Providers
network: true
overview: Beast Enterprises publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Placeholder, Stub, API-Evangelist, and Harvest.
random_paper: 16
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
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
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beast Enterprises Domain Security
  slug: beast-enterprises-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beast-enterprises
tags:
- Company
- Placeholder
- Stub
- API-Evangelist
- Harvest
website: https://www.nasdaqprivatemarket.com/
---
