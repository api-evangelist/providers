---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: Integration hub API for WellSky's CareTend home infusion and specialty pharmacy platform, providing programmatic access to patient management, billing authorizations, clinical visits, inventory, purch
  name: WellSky CareTend API
  slug: caretend-api
- description: FHIR R4-compliant API built on the US Core Implementation Guide, providing read access to patient health data including demographics, conditions, medications, lab results, care plans, and clinical doc
  name: WellSky FHIR API
  slug: fhir-api
- description: FHIR R4 interoperability API for EHR partners integrating with WellSky's Consolo hospice and palliative care platform, supporting patient demographics, care plans, medication requests, observations, e
  name: WellSky Hospice and Palliative API
  slug: hospice-palliative-api
- description: FHIR-compliant API for WellSky Personal Care software platform enabling data integration and interoperability for home care agencies, built on OAuth 2.0 client credentials flow for scheduling, care wo
  name: WellSky Personal Care Connect API
  slug: personal-care-connect-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wellsky-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://wellsky.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://wellsky.com/support/
- group: commercial
  title: ''
  type: Plans
  url: plans/wellsky-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wellsky-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wellsky-finops.yml
created: '2026-06-13'
description: WellSky provides care coordination and home health software with REST APIs for managing patient referrals, authorizations, visit scheduling, clinical documentation, and billing workflows across home health, hospice, palliative care, personal care, and specialty pharmacy settings.
finops:
- name: Wellsky Finops
  service_category: ''
  slug: wellsky-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wellsky.png
jsonld:
- class_count: 39
  name: Wellsky Context
  property_count: 5
  slug: wellsky-context
layout: provider
modified: '2026-06-13'
name: WellSky
nav: Providers
network: true
overview: 'WellSky publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Home Health, Hospice, Care Coordination, and FHIR.


  The WellSky catalog on APIs.io includes 1 JSON-LD context.


  WellSky''s developer surface includes engineering blog, support, and 4 more developer resources.'
plans:
- name: Wellsky Plans Pricing
  plan_count: 4
  slug: wellsky-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Wellsky Rate Limits
  slug: wellsky-rate-limits
score:
  band: thin
  composite: 29.9
  delta: 7.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 22.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 22.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/wellsky/refs/heads/main/screenshots/wellsky-2026-06-20T201350.png
security:
- kind: domain-security
  name: Wellsky Domain Security
  slug: wellsky-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wellsky
tags:
- Healthcare
- Home Health
- Hospice
- Care Coordination
- FHIR
- Clinical Documentation
- Billing
- EHR
---
