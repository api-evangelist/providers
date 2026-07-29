---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: CEHRT-certified API (§ 170.315(g)(7)) for patient data selection, enabling authorized access to patient records within the Axxess EHR platform using FHIR standards.
  name: Axxess Patient Selection API
  slug: axxess-patient-selection-api
- description: CEHRT-certified API (§ 170.315(g)(8)) for categorical patient data retrieval, supporting structured data access by category within the Axxess certified EHR solution.
  name: Axxess Data Category Request API
  slug: axxess-data-category-request-api
- description: CEHRT-certified API (§ 170.315(g)(9)) supporting CCDS C-CDA comprehensive data requests, allowing full patient data export in compliance with federal interoperability requirements.
  name: Axxess All Data Request API
  slug: axxess-all-data-request-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axxess-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/axxess/refs/heads/main/plans/axxess-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/axxess/refs/heads/main/rate-limits/axxess-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/axxess/refs/heads/main/finops/axxess-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://engage.axxess.com/api.html
- group: other
  title: ''
  type: UsagePolicy
  url: https://engage.axxess.com/AxxessAPI_UsagePolicy.html
- group: company
  title: ''
  type: Website
  url: https://www.axxess.com
- group: company
  title: ''
  type: Blog
  url: https://www.axxess.com/blog/
- group: company
  title: ''
  type: News
  url: https://www.axxess.com/media/
- group: company
  title: ''
  type: InteroperabilityPartners
  url: https://www.axxess.com/interoperability-partners/
- group: other
  title: ''
  type: AxxessExchange
  url: https://www.axxess.com/axxess-exchange/
- group: other
  title: ''
  type: AxxessConnect
  url: https://www.axxess.com/axxess-connect/
created: '2026-06-13'
description: Home health, hospice, and private duty software with REST APIs for managing patient plans of care, visit documentation, billing, scheduling, and OASIS assessments. Axxess provides certified EHR technology with FHIR-compliant interoperability, supporting data exchange across care settings via HL7, TEFCA, FHIR, HITRUST, and HIPAA standards.
finops:
- name: Axxess Finops
  service_category: ''
  slug: axxess-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/axxess.png
jsonld:
- class_count: 0
  name: Axxess Context
  property_count: 49
  slug: axxess-context
layout: provider
modified: '2026-06-13'
name: Axxess
nav: Providers
network: true
overview: 'Axxess publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Home Health, Hospice, Private Duty, EHR, and Healthcare.


  The Axxess catalog on APIs.io includes 1 JSON-LD context.


  Axxess'' developer surface includes documentation, engineering blog, product news, and 9 more developer resources.'
plans:
- name: Axxess Plans Pricing
  plan_count: 3
  slug: axxess-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 0
  name: Axxess Rate Limits
  slug: axxess-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: -4.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 23.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/axxess/refs/heads/main/screenshots/axxess-2026-06-20T172828.png
security:
- kind: domain-security
  name: Axxess Domain Security
  slug: axxess-domain-security
  summary_line: TLSv1.2 · DMARC
slug: axxess
tags:
- Home Health
- Hospice
- Private Duty
- EHR
- Healthcare
- FHIR
- OASIS
- Billing
- Scheduling
- Visit Documentation
website: https://www.axxess.com
---
