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
  href: https://raw.githubusercontent.com/api-evangelist/bet9ja/refs/heads/main/hosts/bet9ja-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bet9ja-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bet9ja/refs/heads/main/vendors/bet9ja-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bet9ja-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bet9ja/refs/heads/main/security/bet9ja-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bet9ja-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bet9ja.com
created: '2026-09-28'
description: Bet9ja is a Nigerian online sports betting and gaming platform founded in 2013. It offers a wide range of betting options on sports, casino games, and virtual events, catering to a large user base across Nigeria and other African markets. The company provides mobile and web interfaces, with a focus on secure transactions and user-friendly experience.
layout: provider
modified: '2026-09-28'
name: Bet9ja
nav: Providers
network: true
overview: Bet9ja is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports Betting, Gaming, Nigeria, and Online Platform.
random_paper: 3
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 6
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - nigeria
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
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
  name: Bet9Ja Domain Security
  slug: bet9ja-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bet9ja
tags:
- Company
- Sports Betting
- Gaming
- Nigeria
- Online Platform
website: https://bet9ja.com
---
