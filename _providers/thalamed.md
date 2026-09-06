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
  url: security/thalamed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.thalamed.com
created: '2026-07-17'
description: Thalamed is a Berlin-based medical device procurement marketplace, founded in 2014, that connects healthcare providers such as clinics, private practices, and outpatient care facilities with suppliers of medical equipment including ultrasound and x-ray devices, sterilization and disinfection systems, and medical lasers. Customers describe the device they need and Thalamed's team evaluates the request and contacts the most suitable providers to deliver matching quotes, simplifying comparison and purchasing. The company is a Point Nine and RTAventures portfolio company. No public developer API, documentation, or integration surface is published as of this enrichment pass.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thalamed.png
layout: provider
modified: '2026-07-21'
name: Thalamed
nav: Providers
network: true
overview: Thalamed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Devices, Marketplace, and Procurement.
random_paper: 13
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
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
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
screenshot: https://raw.githubusercontent.com/api-evangelist/thalamed/refs/heads/main/screenshots/thalamed-2026-09-02T163313.png
security:
- kind: domain-security
  name: Thalamed Domain Security
  slug: thalamed-domain-security
  summary_line: TLSv1.2
slug: thalamed
tags:
- Company
- Healthcare
- Medical Devices
- Marketplace
- Procurement
- Germany
website: http://www.thalamed.com
---
