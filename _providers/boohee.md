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
  url: security/boohee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.boohee.com/
created: '2026-07-17'
description: Boohee (薄荷健康) is a Chinese consumer health-technology company focused on scientific weight management, serving a cumulative 180 million users over its ~17-year history. Its portfolio spans the Boohee Health mobile app (calorie and food tracking, diet and exercise logging, AI weight-management coaching, meal plans, smart body scales, community), Boohee Life nutritional foods and subscription services, the Boohee Life Internet Hospital (Tianjin-based telemedicine for internal and traditional Chinese medicine), and a Boohee weight-loss SaaS platform that helps hospitals stand up weight-management clinics. The company operates as a consumer mobile and content platform and does not publish a public developer API or open platform; this profile is maintained in the API Evangelist network as a portfolio lead of DCM Ventures.
image: https://www.boohee.com/favicon.png
layout: provider
modified: '2026-07-18'
name: Boohee
nav: Providers
network: true
overview: Boohee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Health, Nutrition, and Weight Management.
random_paper: 17
score:
  band: minimal
  composite: 3.3
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
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boohee/refs/heads/main/screenshots/boohee-2026-07-25T203611.png
security:
- kind: domain-security
  name: Boohee Domain Security
  slug: boohee-domain-security
  summary_line: TLSv1.2
slug: boohee
tags:
- Company
- Consumer
- Health
- Nutrition
- Weight Management
- Telemedicine
- Mobile App
- China
website: http://www.boohee.com/
---
