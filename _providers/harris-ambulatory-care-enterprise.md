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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: The Pulse §170.315(g)(10) ONC Certified FHIR API enables third-party application developers to register, authenticate, and integrate with providers using Harris Pulse EHR software. The documentation d
  name: Pulse FHIR API
  slug: pulse-fhir-api
- description: Amazing Charts is an EHR product within Harris Ambulatory Care Enterprise that exposes a §170.315(g)(10) ONC Certified FHIR API for third-party application developers.
  name: Amazing Charts API
  slug: amazing-charts-api
- description: CareTracker is a Harris Ambulatory Care Enterprise EHR product that provides a §170.315(g)(10) ONC Certified FHIR API for third-party developers.
  name: CareTracker API
  slug: caretracker-api
- description: Picasso is an ambulatory practice management product within Harris Ambulatory Care Enterprise that provides API documentation for third-party integrators.
  name: Picasso API
  slug: picasso-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harris-ambulatory-care-enterprise-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/harrisambulatorygroup
- group: company
  title: ''
  type: Website
  url: https://harrisambulatory.com
- group: docs
  title: ''
  type: Pulse Documentation
  url: https://harrisambulatory.com/pulse-api-documentation/
- group: docs
  title: ''
  type: Amazing Charts Documentation
  url: https://harrisambulatory.com/ac-api-documentation/
- group: docs
  title: ''
  type: CareTracker Documentation
  url: https://harrisambulatory.com/caretracker-api-documentation/
- group: docs
  title: ''
  type: Picasso Documentation
  url: https://harrisambulatory.com/picasso-api-documentation/
- group: other
  title: ''
  type: Parent Company
  url: https://www.harriscomputer.com
created: '2025-02-24'
description: Harris Ambulatory Care Enterprise (part of Harris Healthcare, a Harris Computer company) provides ambulatory healthcare software solutions including the Pulse electronic health record system. The platform supports a §170.315(g)(10) ONC certified FHIR API for third-party application developers to access patient data, provider information, and clinical resources. Pulse is deployed on-premises, so each provider hosts a separate API instance with its own base URL. Third-party developers must obtain an ONC 2015 Edition Certified API License and register with each provider organization.
finops:
- name: Harris Ambulatory Care Enterprise Finops
  service_category: API
  slug: harris-ambulatory-care-enterprise-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/harris-ambulatory-care-enterprise.png
layout: provider
modified: '2026-04-28'
name: Harris Ambulatory Care Enterprise
nav: Providers
network: true
overview: Harris Ambulatory Care Enterprise publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Ambulatory Care, Electronic Health Records, FHIR, Health IT, and Healthcare.
plans:
- name: Harris Ambulatory Care Enterprise Plans Pricing
  plan_count: 3
  slug: harris-ambulatory-care-enterprise-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Harris Ambulatory Care Enterprise Rate Limits
  slug: harris-ambulatory-care-enterprise-rate-limits
score:
  band: emerging
  composite: 11.8
  delta: 1.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harris-ambulatory-care-enterprise/refs/heads/main/screenshots/harris-ambulatory-care-enterprise-2026-06-20T182518.png
security:
- kind: domain-security
  name: Harris Ambulatory Care Enterprise Domain Security
  slug: harris-ambulatory-care-enterprise-domain-security
  summary_line: TLSv1.3 · DMARC
slug: harris-ambulatory-care-enterprise
tags:
- Ambulatory Care
- Electronic Health Records
- FHIR
- Health IT
- Healthcare
- ONC Certified
- Pulse
website: https://harrisambulatory.com
---
