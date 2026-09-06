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
  url: security/rvds-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rvds.kr
created: '2026-07-17'
description: RVDS Inc. is a South Korean food and beverage company that describes itself as growing into Korea's representative Multi-K-Food Brand Operator, building and operating a portfolio of consumer dining brands including Dodo Korea, Butai, and Salad Monster. Based in Cheongju-si, Chungcheongbuk-do, the company is backed by 500 Global. As a consumer food-brand operator it publishes no public API, developer portal, SDKs, or technical documentation, so this profile carries only identity and probed domain-security signals rather than API artifacts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rvds-inc.png
layout: provider
modified: '2026-07-21'
name: RVDS Inc.
nav: Providers
network: true
overview: RVDS Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Consumer Brands, Restaurant, and Korea.
random_paper: 8
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
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rvds-inc/refs/heads/main/screenshots/rvds-inc-2026-09-02T154221.png
security:
- kind: domain-security
  name: Rvds Inc Domain Security
  slug: rvds-inc-domain-security
  summary_line: TLSv1.3 · HSTS
slug: rvds-inc
tags:
- Company
- Food and Beverage
- Consumer Brands
- Restaurant
- Korea
- Food Service
website: https://rvds.kr
---
