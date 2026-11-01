---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Stan platform
  name: Stan API
  slug: stan-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/getstan-app/hosts/getstan-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getstan-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/getstan-app/vendors/getstan-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getstan-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/getstan-app/security/getstan-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getstan-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getstan.app/
coverage:
  checked: '2026-10-29'
  detail: Main site returns a JavaScript shell with no machine‑readable API spec
  evidence:
  - status: 200
    url: https://getstan.app/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Stan (STAN) is India’s leading social app for gamers and creators, connecting communities through interactive clubs, esports tournaments, brand deals, ads, gifting, and Web3 rewards. It empowers creators to monetize and engage fans, offering events like STANfest and integrating NFT and blockchain features for unique experiences.
layout: provider
modified: '2026-10-29'
name: Stan
nav: Providers
network: true
overview: Stan is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Social, CreatorEconomy, and Web3.
random_paper: 20
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 6
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
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getstan App Domain Security
  slug: getstan-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: getstan-app
tags:
- Company
- Gaming
- Social
- CreatorEconomy
- Web3
website: https://getstan.app/
---
