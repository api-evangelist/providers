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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Ezyvet Agentic Access
  operation_count: 47
  slug: ezyvet-agentic-access
  summary_line: 47 operations · 20 acting
api_count: 9
apis:
- description: Animal (patient) records and reference data. (Modeled.)
  name: ezyVet Animals API
  slug: ezyvet-animals-api
- description: Appointments, types, and statuses. (Modeled.)
  name: ezyVet Appointments API
  slug: ezyvet-appointments-api
- description: OAuth 2.0 Client Credentials token exchange. (Confirmed.)
  name: ezyVet Authentication API
  slug: ezyvet-authentication-api
- description: Clinical consultation records. (Modeled.)
  name: ezyVet Consultations API
  slug: ezyvet-consultations-api
- description: Contacts (clients / pet owners) and their details. (Confirmed CRUD.)
  name: ezyVet Contacts API
  slug: ezyvet-contacts-api
- description: Diagnostic requests and results (Standard Diagnostic Integration). (Confirmed integration.)
  name: ezyVet Diagnostics API
  slug: ezyvet-diagnostics-api
- description: Invoices, invoice lines, and payments. (Modeled.)
  name: ezyVet Invoices API
  slug: ezyvet-invoices-api
- description: Prescriptions and vaccinations. (Partially confirmed.)
  name: ezyVet Prescriptions API
  slug: ezyvet-prescriptions-api
- description: Product / inventory catalog. (Modeled.)
  name: ezyVet Products API
  slug: ezyvet-products-api
artifact_total: 17
collections:
- collection_type: open
  name: ezyVet API
  slug: open-ezyvet
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ezyvet-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ezyvet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ezyvet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ezyvet-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ezyvet
- group: company
  title: ''
  type: Website
  url: https://www.ezyvet.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.ezyvet.com/docs/v1/
- group: commercial
  title: ''
  type: Plans
  url: plans/ezyvet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ezyvet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ezyvet-finops.yml
created: '2026-07-04'
description: ezyVet is cloud-based veterinary practice information management software (PIMS) for clinics, specialty, and emergency hospitals, covering patient records, scheduling, clinical workflows, billing, inventory, and diagnostics. Founded in New Zealand in 2006, ezyVet was acquired by IDEXX Laboratories in June 2021 and sits alongside IDEXX's Cornerstone and Neo PIMS offerings (the acquisition also included Vet Radar). ezyVet exposes a documented RESTful API of roughly 216 endpoints over animals/patients, contacts/clients, appointments, consultations, invoices, products, and diagnostics. The API is partner-gated - developer access requires an approved integration application and issued client credentials - but the endpoint catalog, best-practice guides, and a full Postman collection are publicly documented at developers.ezyvet.com. Authentication is OAuth 2.0 Client Credentials with 12-hour bearer tokens.
finops:
- name: Ezyvet Finops
  service_category: Veterinary Practice Management Software
  slug: ezyvet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ezyvet.png
layout: provider
modified: '2026-07-04'
name: ezyVet
nav: Providers
network: true
overview: 'ezyVet publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Animals API, Appointments API, Authentication API, and 6 more. Tagged areas include Veterinary, Practice Management, PIMS, Healthcare, and Animal Health.


  ezyVet''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Ezyvet Plans Pricing
  plan_count: 3
  slug: ezyvet-plans-pricing
random_paper: 99
rate_limits:
- limit_count: 3
  name: Ezyvet Rate Limits
  slug: ezyvet-rate-limits
score:
  band: thin
  composite: 35.4
  delta: -0.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 22.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ezyvet/refs/heads/main/screenshots/ezyvet-2026-07-25T214103.png
security:
- kind: authentication
  name: Ezyvet Authentication
  slug: ezyvet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ezyvet Domain Security
  slug: ezyvet-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Ezyvet Vulnerability Disclosure
  slug: ezyvet-vulnerability-disclosure
  summary_line: disclosure policy published
slug: ezyvet
tags:
- Veterinary
- Practice Management
- PIMS
- Healthcare
- Animal Health
- IDEXX
- Partner Gated
website: https://www.ezyvet.com
---
