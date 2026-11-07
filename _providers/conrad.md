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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/conrad/security/conrad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conrad-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.conrad.com/
created: '2026-10-26'
description: Conrad Electronic is a German retailer specializing in electronics, tools, and components for hobbyists, professionals, and makers. It offers a wide range of products including computers, automation, robotics, and DIY supplies through its online store and physical locations across Europe. The company provides APIs for product catalogs, pricing, and order management, supporting integration with e‑commerce platforms and third‑party services.
layout: provider
modified: '2026-10-26'
name: Conrad Electronic
nav: Providers
network: true
overview: Conrad Electronic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electronics, Retail, E-Commerce, and DIY.
random_paper: 7
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 9
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
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 4.4
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/conrad/conrad-2026-11-03T125142.png
security:
- kind: domain-security
  name: Conrad Domain Security
  slug: conrad-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Conrad Vulnerability Disclosure
  slug: conrad-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: conrad
tags:
- Company
- Electronics
- Retail
- E-Commerce
- DIY
website: https://www.conrad.com/
---
