---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides access to property listings, search and contact functionality as described on the developer portal.
  name: VRM Immo API
  slug: vrm-immo-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/vrm-immo/hosts/vrm-immo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vrm-immo-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://vrm-immo.de/s/login
- group: auth
  href: https://artifacts.apis.io/vrm-immo/security/vrm-immo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vrm-immo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vrm-immo.de/
coverage:
  checked: '2026-10-28'
  detail: The provider’s website offers a login page but no public API specification is available.
  evidence:
  - status: 404
    url: https://vrm-immo.de/openapi.json
  - status: 0
    url: https://api.vrm-immo.de/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: VRM Immo operates a regional real‑estate marketplace focused on the Rhein‑Main area in Germany. It connects buyers, renters, and sellers with property listings, offering search, detailed property information, and contact options. The platform is part of the Rhein Main Presse media group and serves as a local hub for residential and commercial real‑estate transactions, providing tools for agents and private users alike.
layout: provider
modified: '2026-10-28'
name: VRM Immo
nav: Providers
network: true
overview: VRM Immo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Marketplace, Germany, and Rhein-Main.
random_paper: 4
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 6.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vrm-immo/vrm-immo-2026-11-03T145929.png
security:
- kind: domain-security
  name: Vrm Immo Domain Security
  slug: vrm-immo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vrm-immo
tags:
- Company
- Real Estate
- Marketplace
- Germany
- Rhein-Main
website: https://vrm-immo.de/
---
