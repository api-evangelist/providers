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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Provides statistical data and APIs for interest rates, exchange rates, and financial market statistics.
  name: Riksbank API
  slug: riksbank-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/riksbank/refs/heads/main/hosts/riksbank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/riksbank-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/riksbank/refs/heads/main/vendors/riksbank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/riksbank-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/riksbank/refs/heads/main/packages/riksbank-packages.yml
  title: ''
  type: SDKs
  url: packages/riksbank-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/riksbank/refs/heads/main/packages/riksbank-packages.yml
  title: ''
  type: Packages
  url: packages/riksbank-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/riksbank/refs/heads/main/security/riksbank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/riksbank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.riksbank.se/
- group: docs
  title: ''
  type: Documentation
  url: https://www.riksbank.se/sv/statistik/
coverage:
  checked: '2026-10-15'
  detail: The API reference page returns 404 for OpenAPI JSON and no machine‑readable contract is published.
  evidence:
  - status: 404
    url: https://www.riksbank.se/sv/statistik/hamta-rantor-och-valutakurser-via-api/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Riksbank, Sveriges Riksbank, is Sweden's central bank responsible for monetary policy, financial stability, and issuing currency. It provides statistical data and APIs for interest rates, exchange rates, and financial market statistics, supporting developers and researchers with programmatic access to economic indicators.
image: https://www.riksbank.se/cdn-cgi/image/format=auto,width=1200,height=630,quality=85,fit=cover/contentassets/147e6b2ace2145218db03f2c9c11128d/riksbankshuset-open-graph.jpg
layout: provider
modified: '2026-10-15'
name: Riksbank
nav: Providers
network: true
overview: 'Riksbank is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, CentralBank, Sweden, and Economics.


  Riksbank''s developer surface includes documentation and 6 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
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
  name: Riksbank Domain Security
  slug: riksbank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: riksbank
tags:
- Company
- Finance
- CentralBank
- Sweden
- Economics
website: https://www.riksbank.se/
---
