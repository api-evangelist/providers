---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Elation Agentic Access
  operation_count: 67
  slug: elation-agentic-access
  summary_line: 67 operations · 43 acting
api_count: 13
apis:
- description: Allergy and drug intolerance tracking
  name: Elation Health Allergies API
  slug: elation-allergies-api
- description: Scheduling and appointment management
  name: Elation Health Appointments API
  slug: elation-appointments-api
- description: OAuth2 token management
  name: Elation Health Authentication API
  slug: elation-authentication-api
- description: Billing codes and bill management
  name: Elation Health Billing API
  slug: elation-billing-api
- description: Insurance company, plan, and policy management
  name: Elation Health Insurance API
  slug: elation-insurance-api
- description: Laboratory order management
  name: Elation Health Lab Orders API
  slug: elation-lab-orders-api
- description: Medication and prescription management
  name: Elation Health Medications API
  slug: elation-medications-api
- description: Secure direct messaging
  name: Elation Health Messaging API
  slug: elation-messaging-api
- description: Patient profile management
  name: Elation Health Patients API
  slug: elation-patients-api
- description: Provider and staff management
  name: Elation Health Physicians API
  slug: elation-physicians-api
- description: Practice administration
  name: Elation Health Practices API
  slug: elation-practices-api
- description: Patient problem list management
  name: Elation Health Problems API
  slug: elation-problems-api
- description: Clinical encounter documentation
  name: Elation Health Visit Notes API
  slug: elation-visit-notes-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elation-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/elation-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.elationhealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.elationhealth.com/reference/api-overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/elationemr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elationhealth
- group: company
  title: ''
  type: Blog
  url: https://www.elationhealth.com/resources/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elationhealth.com/contact-us/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://elationhealth.statuspage.io
- group: other
  title: ''
  type: X
  url: https://x.com/elationhealth
- group: commercial
  title: ''
  type: Plans
  url: plans/elation-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elation-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/elation-finops.yml
created: '2026-06-13'
description: Elation Health provides a primary care EHR platform with a REST API for managing patient profiles, clinical encounters, orders, results, prescriptions, and direct secure messaging in ambulatory settings. The API enables interoperability by integrating patient data from third-party sources, supporting patient engagement, clinical operations, scheduling, pharmacy management, and practice administration through OAuth2-secured REST endpoints.
examples:
- key_count: 18
  name: Elation Appointment Example
  slug: elation-appointment-example
- key_count: 25
  name: Elation Patient Example
  slug: elation-patient-example
finops:
- name: Elation Finops
  service_category: ''
  slug: elation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elation.png
json_schemas:
- name: Patient
  property_count: 43
  slug: elation-patient
jsonld:
- class_count: 28
  name: Elation Context
  property_count: 69
  slug: elation-context
layout: provider
modified: '2026-06-13'
name: Elation Health
nav: Providers
network: true
overview: 'Elation Health publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Allergies API, Appointments API, Authentication API, and 10 more. Tagged areas include EHR, Electronic Health Records, Primary Care, Healthcare, and FHIR.


  The Elation Health catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Elation Health''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Elation Plans Pricing
  plan_count: 3
  slug: elation-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 0
  name: Elation Rate Limits
  slug: elation-rate-limits
rules:
- name: Elation Health API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: elation-jsonschema-spectral-rules
scopes:
- name: Elation Scopes
  scope_count: 1
  slug: elation-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 47.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 42.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elation/refs/heads/main/screenshots/elation-2026-06-20T180646.png
security:
- kind: authentication
  name: Elation Authentication
  slug: elation-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Elation Domain Security
  slug: elation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elation
tags:
- EHR
- Electronic Health Records
- Primary Care
- Healthcare
- FHIR
- Clinical
- Patients
- Prescriptions
- Messaging
website: https://www.elationhealth.com/
---
