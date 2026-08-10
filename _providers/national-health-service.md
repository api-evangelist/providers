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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Use this API to submit ambulance data to the NHS Data Processing Service (DPS) so that it can be made available for analysis and review by NHS England and ambulance trusts.
  name: NHS Ambulance Data Submission FHIR API
  slug: ambulance-data-submission-fhir
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/national-health-service-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-health-service-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nhs
- group: company
  title: ''
  type: Website
  url: https://www.nhs.uk/
- group: start
  title: ''
  type: Portal
  url: https://digital.nhs.uk/developer
- group: other
  title: ''
  type: ApiCatalog
  url: https://digital.nhs.uk/developer/api-catalogue
created: '2025-01-07'
description: The National Health Service (NHS) of England publishes a catalogue of APIs for health and care providers, including the Ambulance Data Submission FHIR API used to submit ambulance data to the NHS Data Processing Service (DPS) for analysis and review by NHS England and ambulance trusts.
finops:
- name: National Health Service Finops
  service_category: API
  slug: national-health-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-health-service.png
layout: provider
modified: '2026-04-28'
name: National Health Service
nav: Providers
network: true
overview: 'National Health Service publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Ambulance, Health, Healthcare, and National Health Service.


  National Health Service''s developer surface includes developer portal and 5 more developer resources.'
plans:
- name: National Health Service Plans Pricing
  plan_count: 3
  slug: national-health-service-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: National Health Service Rate Limits
  slug: national-health-service-rate-limits
score:
  band: emerging
  composite: 19.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 19.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-health-service/refs/heads/main/screenshots/national-health-service-2026-06-20T190024.png
security:
- kind: domain-security
  name: National Health Service Domain Security
  slug: national-health-service-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: National Health Service Vulnerability Disclosure
  slug: national-health-service-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: national-health-service
tags:
- Ambulance
- Health
- Healthcare
- National Health Service
website: https://www.nhs.uk/
---
