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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/ctpparking/hosts/ctpparking-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ctpparking-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ctpparking/security/ctpparking-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ctpparking-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://icnctp.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://icnctp.com
  - status: 403
    url: https://equityzen.com/company/ctpparking
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Ctpparking, operating under Shanghai CTP Information Technology Co., Ltd., provides a smart, all‑in‑one parking solution platform. It offers real‑time parking space discovery, reservation, cashless payment, and electric‑vehicle charging integration for governments, enterprises, and private users across multiple cities. The service includes on‑street and off‑street parking management, data analytics, and city‑wide charging network operations, aiming to improve urban mobility and reduce congestion.
layout: provider
modified: '2026-10-11'
name: Ctpparking
nav: Providers
network: true
overview: Ctpparking is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Parking, Smart City, IoT, and China.
random_paper: 19
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
  delta: 0.0
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
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 3.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ctpparking Domain Security
  slug: ctpparking-domain-security
  summary_line: no transport/DNS hardening detected
slug: ctpparking
tags:
- Company
- Parking
- Smart City
- IoT
- China
website: https://icnctp.com
---
