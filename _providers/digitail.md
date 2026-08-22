---
access_model:
  confidence: high
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Digitail Agentic Access
  operation_count: 21
  slug: digitail-agentic-access
  summary_line: 21 operations · 1 acting
api_count: 18
apis:
- description: The Appointments API from Digitail — 3 operation(s) for appointments.
  name: Digitail Appointments API
  slug: digitail-appointments-api
- description: The Breeds API from Digitail — 1 operation(s) for breeds.
  name: Digitail Breeds API
  slug: digitail-breeds-api
- description: The Charges API from Digitail — 1 operation(s) for charges.
  name: Digitail Charges API
  slug: digitail-charges-api
- description: The Clients API from Digitail — 1 operation(s) for clients.
  name: Digitail Clients API
  slug: digitail-clients-api
- description: The Clinics API from Digitail — 1 operation(s) for clinics.
  name: Digitail Clinics API
  slug: digitail-clinics-api
- description: The Files API from Digitail — 1 operation(s) for files.
  name: Digitail Files API
  slug: digitail-files-api
- description: The Invoices API from Digitail — 1 operation(s) for invoices.
  name: Digitail Invoices API
  slug: digitail-invoices-api
- description: The Labs API from Digitail — 1 operation(s) for labs.
  name: Digitail Labs API
  slug: digitail-labs-api
- description: The Medication API from Digitail — 1 operation(s) for medication.
  name: Digitail Medication API
  slug: digitail-medication-api
- description: The Pet Parents API from Digitail — 1 operation(s) for pet parents.
  name: Digitail Pet Parents API
  slug: digitail-pet-parents-api
- description: The Pets API from Digitail — 2 operation(s) for pets.
  name: Digitail Pets API
  slug: digitail-pets-api
- description: The Prescriptions API from Digitail — 1 operation(s) for prescriptions.
  name: Digitail Prescriptions API
  slug: digitail-prescriptions-api
- description: The Records API from Digitail — 1 operation(s) for records.
  name: Digitail Records API
  slug: digitail-records-api
- description: The Reports API from Digitail — 1 operation(s) for reports.
  name: Digitail Reports API
  slug: digitail-reports-api
- description: The Sales API from Digitail — 1 operation(s) for sales.
  name: Digitail Sales API
  slug: digitail-sales-api
- description: The Species API from Digitail — 1 operation(s) for species.
  name: Digitail Species API
  slug: digitail-species-api
- description: The Vets API from Digitail — 1 operation(s) for vets.
  name: Digitail Vets API
  slug: digitail-vets-api
- description: The Visit Types API from Digitail — 1 operation(s) for visit types.
  name: Digitail Visit Types API
  slug: digitail-visit-types-api
artifact_total: 44
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Digitail Open Appointments API
  slug: open-digitail-appointments-api
- collection_type: open
  name: Digitail Open Appointments Breeds API
  slug: open-digitail-breeds-api
- collection_type: open
  name: Digitail Open Appointments Charges API
  slug: open-digitail-charges-api
- collection_type: open
  name: Digitail Open Appointments Clients API
  slug: open-digitail-clients-api
- collection_type: open
  name: Digitail Open Appointments Clinics API
  slug: open-digitail-clinics-api
- collection_type: open
  name: Digitail Open Appointments Files API
  slug: open-digitail-files-api
- collection_type: open
  name: Digitail Open Appointments Invoices API
  slug: open-digitail-invoices-api
- collection_type: open
  name: Digitail Open Appointments Labs API
  slug: open-digitail-labs-api
- collection_type: open
  name: Digitail Open Appointments Medication API
  slug: open-digitail-medication-api
- collection_type: open
  name: Digitail Open Appointments Pet Parents API
  slug: open-digitail-pet-parents-api
- collection_type: open
  name: Digitail Open Appointments Pets API
  slug: open-digitail-pets-api
- collection_type: open
  name: Digitail Open Appointments Prescriptions API
  slug: open-digitail-prescriptions-api
- collection_type: open
  name: Digitail Open Appointments Records API
  slug: open-digitail-records-api
- collection_type: open
  name: Digitail Open Appointments Reports API
  slug: open-digitail-reports-api
- collection_type: open
  name: Digitail Open Appointments Sales API
  slug: open-digitail-sales-api
- collection_type: open
  name: Digitail Open Appointments Species API
  slug: open-digitail-species-api
- collection_type: open
  name: Digitail Open Appointments Vets API
  slug: open-digitail-vets-api
- collection_type: open
  name: Digitail Open Appointments Visit Types API
  slug: open-digitail-visit-types-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/digitail-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/digitail-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/digitail-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/digitail-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/digitail-veterinary-software/
- group: company
  title: ''
  type: Website
  url: https://digitail.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.digitail.io/
- group: start
  title: ''
  type: SignUp
  url: https://digitail.com/api/access
- group: commercial
  title: ''
  type: Plans
  url: plans/digitail-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/digitail-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/digitail-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://digitail.com/blog/
created: '2026-07-04'
description: Digitail is a cloud-based, AI-native veterinary practice management software (PIMS) that consolidates scheduling, electronic medical records, AI SOAP dictation, client communication, billing, inventory, and reporting into one platform, paired with a Pet Parent mobile app for booking, records access, and payments. The Digitail Open API is a documented REST API (base https://developer.digitail.io/api/v1) secured with OAuth 2.0 authorization-code grant with PKCE, giving clinics, technology partners, and ecosystem players (labs, insurers, pharmacies, telemedicine, analytics) programmatic, real-time access to clinic data. API credentials are provisioned via an access registration; Open API access is included across Digitail subscription plans.
finops:
- name: Digitail Finops
  service_category: ''
  slug: digitail-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digitail.png
layout: provider
modified: '2026-07-04'
name: Digitail
nav: Providers
network: true
overview: 'Digitail publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Breeds API, Charges API, and 15 more. Tagged areas include Veterinary, PIMS, Practice Management, Pets, and Healthcare.


  Digitail''s developer surface includes authentication, documentation, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: Digitail Plans Pricing
  plan_count: 4
  slug: digitail-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Digitail Rate Limits
  slug: digitail-rate-limits
scopes:
- name: Digitail Scopes
  scope_count: 0
  slug: digitail-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.6
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 36.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/digitail/refs/heads/main/screenshots/digitail-2026-07-25T212019.png
security:
- kind: authentication
  name: Digitail Authentication
  slug: digitail-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Digitail Domain Security
  slug: digitail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: digitail
tags:
- Veterinary
- PIMS
- Practice Management
- Pets
- Healthcare
- Scheduling
- Billing
- SaaS
website: https://digitail.com/
---
