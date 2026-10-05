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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitstar/refs/heads/main/hosts/bitstar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitstar-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitstar/refs/heads/main/vendors/bitstar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitstar-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitstar/refs/heads/main/security/bitstar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitstar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/bitstar
coverage:
  checked: '2026-09-28'
  detail: No public developer documentation or API endpoints were found on the company's website.
  evidence:
  - status: 200
    url: https://www.bitstar.co
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: BitStar is a Tokyo‑based influencer marketing platform that connects brands with video creators. The company offers a suite of tools including BitStar Agent, Studio, and a marketplace to manage campaigns, analytics, and payments. Founded in 2014, BitStar has raised multiple funding rounds and serves hundreds of creators across Asia, providing data‑driven solutions to accelerate growth in the creator economy.
layout: provider
modified: '2026-09-28'
name: Bitstar
nav: Providers
network: true
overview: Bitstar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Influencer Marketing, Video Creators, Tokyo, and Software-as-a-Service.
random_paper: 13
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 0
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
    discoverability: 51.8
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
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
  name: Bitstar Domain Security
  slug: bitstar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bitstar
tags:
- Company
- Influencer Marketing
- Video Creators
- Tokyo
- Software-as-a-Service
website: https://equityzen.com/company/bitstar
---
