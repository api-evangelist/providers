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
  scored_at: '2026-09-01'
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
random_paper: 17
rate_limits:
- limit_count: 5
  name: National Health Service Rate Limits
  slug: national-health-service-rate-limits
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
