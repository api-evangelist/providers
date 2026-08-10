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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Kareo Agentic Access
  operation_count: 32
  slug: kareo-agentic-access
  summary_line: 32 operations · 32 acting
api_count: 8
apis:
- description: The Kareo Integration SOAP API provides a web services interface for integrating third-party applications with practice management data. Supports read access to patients, providers, appointments, tran
  name: Kareo Integration SOAP API
  slug: kareo-soap-api
- description: The Kareo Clinical Open API provides REST-based access to EHR clinical data, exposing patient clinical records, MACRA/MIPS reporting data, and related healthcare information. The API is documented wit
  name: Kareo Clinical Open API
  slug: kareo-clinical-open-api
- description: Vendor registration, throttles, and configuration
  name: Kareo Administrative API
  slug: kareo-administrative-api
- description: Appointment scheduling and management
  name: Kareo Appointments API
  slug: kareo-appointments-api
- description: Charges, payments, and transactions
  name: Kareo Billing API
  slug: kareo-billing-api
- description: Clinical encounter and document management
  name: Kareo Encounters API
  slug: kareo-encounters-api
- description: Patient demographic and record management
  name: Kareo Patients API
  slug: kareo-patients-api
- description: Provider and practice administration
  name: Kareo Providers API
  slug: kareo-providers-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kareo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kareo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kareo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kareo.com
- group: docs
  title: ''
  type: Documentation
  url: https://helpme.tebra.com/01_Kareo_PM/12_API_and_Integration
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/kareo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kareo
- group: company
  title: ''
  type: Blog
  url: https://www.tebra.com/theintake
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tebra.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tebra.com
- group: other
  title: ''
  type: X
  url: https://x.com/kareo
- group: commercial
  title: ''
  type: Plans
  url: plans/kareo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kareo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kareo-finops.yml
created: '2026-06-13'
description: Kareo, now part of Tebra, provides cloud medical software for independent practices. The platform offers SOAP-based web service APIs for integrating with clinical data, patient management, appointment scheduling, billing, collections, and insurance eligibility verification. The Kareo Integration API enables developers to build programs that access practice management data and functionality through authenticated XML-based SOAP requests. The platform also exposes a Clinical Open API for EHR data access.
examples:
- key_count: 4
  name: Kareo Create Appointment Example
  slug: kareo-create-appointment-example
- key_count: 4
  name: Kareo Create Patient Example
  slug: kareo-create-patient-example
- key_count: 5
  name: Kareo Get Patients Example
  slug: kareo-get-patients-example
finops:
- name: Kareo Finops
  service_category: ''
  slug: kareo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kareo.png
json_schemas:
- name: KareoAppointment
  property_count: 9
  slug: kareo-appointment
- name: KareoEncounter
  property_count: 8
  slug: kareo-encounter
- name: KareoPatient
  property_count: 14
  slug: kareo-patient
jsonld:
- class_count: 21
  name: Kareo Context
  property_count: 43
  slug: kareo-context
layout: provider
modified: '2026-06-13'
name: Kareo
nav: Providers
network: true
overview: 'Kareo publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Administrative API, Appointments API, Billing API, and 3 more. Tagged areas include Healthcare, Medical Software, EHR, Practice Management, and Medical Billing.


  The Kareo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kareo''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Kareo Plans Pricing
  plan_count: 5
  slug: kareo-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 2
  name: Kareo Rate Limits
  slug: kareo-rate-limits
rules:
- name: Kareo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: kareo-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.8
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 66.7
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 20.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kareo/refs/heads/main/screenshots/kareo-2026-06-20T183920.png
security:
- kind: domain-security
  name: Kareo Domain Security
  slug: kareo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kareo Trust Center
  slug: kareo-trust-center
  summary_line: PCI DSS, HIPAA
slug: kareo
tags:
- Healthcare
- Medical Software
- EHR
- Practice Management
- Medical Billing
- Patient Scheduling
- Clinical Data
- Insurance Eligibility
- HIPAA
website: https://www.kareo.com
---
