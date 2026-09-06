---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stylesaint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stylesaint.com
created: '2026-07-17'
description: StyleSaint is a Los Angeles-based direct-to-consumer luxury women's fashion brand, originally an a16z-backed social-commerce startup and now an independent e-commerce label selling silk, lace, and other luxury-fabric apparel that is handmade in LA, ethically made, and sustainably sourced. The storefront runs on Shopify. As of this enrichment pass StyleSaint publishes no public developer program, API documentation, OpenAPI/AsyncAPI specification, SDKs, or agent-facing surface of its own; it is catalogued here as an a16z portfolio company. Any programmable commerce capability would be provided by the underlying Shopify platform rather than by a first-party StyleSaint API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stylesaint.png
layout: provider
modified: '2026-07-21'
name: StyleSaint
nav: Providers
network: true
overview: StyleSaint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, E-Commerce, Retail, and Apparel.
random_paper: 12
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stylesaint/refs/heads/main/screenshots/stylesaint-2026-09-02T161053.png
security:
- kind: domain-security
  name: Stylesaint Domain Security
  slug: stylesaint-domain-security
  summary_line: TLSv1.3 · HSTS
slug: stylesaint
tags:
- Company
- Fashion
- E-Commerce
- Retail
- Apparel
- Direct to Consumer
- Shopify
website: https://stylesaint.com
---
