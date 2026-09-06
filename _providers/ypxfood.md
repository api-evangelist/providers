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
  url: security/ypxfood-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ypxfood.com
created: '2026-07-17'
description: ypxfood (YPX Cayman) is a Taiwanese quick-service restaurant company specializing in Taiwanese food and snacks, backed by Qiming Venture Partners, LionRock Capital, and Ignition Capital. It is a consumer restaurant and food business with no public developer or API surface; enrichment probes found the corporate website (Cloudflare-fronted, returning 403 to automated clients) and no documentation, OpenAPI, SDKs, or well-known discovery endpoints. This profile is retained as a network company record.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ypxfood.png
layout: provider
modified: '2026-07-21'
name: ypxfood
nav: Providers
network: true
overview: ypxfood is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Restaurant, Quick Service Restaurant, and Taiwan.
random_paper: 0
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
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
    - taiwan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Ypxfood Domain Security
  slug: ypxfood-domain-security
  summary_line: TLSv1.3
slug: ypxfood
tags:
- Company
- Food
- Restaurant
- Quick Service Restaurant
- Taiwan
website: https://ypxfood.com
---
