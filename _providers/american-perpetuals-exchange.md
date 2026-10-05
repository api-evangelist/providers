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
  href: https://raw.githubusercontent.com/api-evangelist/american-perpetuals-exchange/refs/heads/main/hosts/american-perpetuals-exchange-hosts.yml
  title: ''
  type: Hosts
  url: hosts/american-perpetuals-exchange-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/american-perpetuals-exchange/refs/heads/main/vendors/american-perpetuals-exchange-vendors.yml
  title: ''
  type: Vendors
  url: vendors/american-perpetuals-exchange-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/american-perpetuals-exchange/refs/heads/main/security/american-perpetuals-exchange-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/american-perpetuals-exchange-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/american-perpetuals-exchange_stock/
created: '2026-09-24'
description: American Perpetuals Exchange (APEX) is a US‑based fintech company developing a digital asset trading platform that offers perpetual futures contracts and other derivative products. Founded in 2025, the firm raised $30 million in Series A funding to build a regulated exchange infrastructure, aiming for CFTC and SEC compliance. Operating in stealth mode, APEX targets institutional and retail traders seeking leveraged exposure to cryptocurrencies and synthetic assets, with plans to launch a web and API‑driven trading interface in 2027.
layout: provider
modified: '2026-09-24'
name: American Perpetuals Exchange
nav: Providers
network: true
overview: American Perpetuals Exchange is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Trading, Derivatives, and Cryptocurrency.
random_paper: 12
score:
  band: minimal
  composite: 2.2
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
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
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 5.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: American Perpetuals Exchange Domain Security
  slug: american-perpetuals-exchange-domain-security
  summary_line: TLSv1.3 · DMARC
slug: american-perpetuals-exchange
tags:
- Company
- Fintech
- Trading
- Derivatives
- Cryptocurrency
website: https://forgeglobal.com/american-perpetuals-exchange_stock/
---
