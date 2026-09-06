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
  url: security/h2o-hospitality-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/h2o-hospitality-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://h2ohospitality.io/en/
- group: company
  title: ''
  type: Website
  url: https://h2ohospitality.io
created: '2026-07-17'
description: 'H2O Hospitality is a South Korea-based hospitality digital-transformation company that connects existing hotel and leisure systems rather than replacing them, streamlining operations from booking to checkout. Its products span three areas: Connect (cloud property-management tooling including Smart CRS, Smart RMS, and Smart FMS), Maximize (revenue and guest-engagement tools such as Smart D2C and AI-based CRM), and Transform (managed operations). It offers smart mobile check-in and automated inventory management, operates across nine countries in Korea, Japan, Southeast Asia, and the Middle East, and is ISO 27001 and ISO 27701 certified. As of this enrichment pass the company publishes no public API, OpenAPI, or developer portal.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/h2o-hospitality.png
layout: provider
modified: '2026-07-19'
name: H2O Hospitality
nav: Providers
network: true
overview: H2O Hospitality is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, Hotels, Property Management, and Travel.
random_paper: 8
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 8.8
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/h2o-hospitality/refs/heads/main/screenshots/h2o-hospitality-2026-07-25T220503.png
security:
- kind: domain-security
  name: H2O Hospitality Domain Security
  slug: h2o-hospitality-domain-security
  summary_line: TLSv1.2 · DMARC
slug: h2o-hospitality
tags:
- Company
- Hospitality
- Hotels
- Property Management
- Travel
- Revenue Management
- Digital Transformation
- South Korea
website: https://h2ohospitality.io
---
