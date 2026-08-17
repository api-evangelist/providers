---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 37
  human_in_the_loop: 0
  name: Opendental Agentic Access
  operation_count: 68
  slug: opendental-agentic-access
  summary_line: 68 operations · 37 acting
api_count: 13
apis:
- description: MODELED. Adjustments and payment splits on the patient ledger.
  name: Open Dental Accounts & Ledger API
  slug: opendental-accounts-ledger-api
- description: CONFIRMED. Scheduling, slots, and WebSched.
  name: Open Dental Appointments API
  slug: opendental-appointments-api
- description: CONFIRMED. Insurance claims and claim workflow.
  name: Open Dental Claims API
  slug: opendental-claims-api
- description: MODELED. Files and images attached to a patient.
  name: Open Dental Documents API
  slug: opendental-documents-api
- description: MODELED. Procedure fees and fee schedules.
  name: Open Dental Fees & Fee Schedules API
  slug: opendental-fees-fee-schedules-api
- description: MODELED. Medication catalog, patient meds, and prescriptions.
  name: Open Dental Medications & Prescriptions API
  slug: opendental-medications-prescriptions-api
- description: CONFIRMED. Patient demographic records.
  name: Open Dental Patients API
  slug: opendental-patients-api
- description: CONFIRMED. Patient payments, refunds, and split reallocation.
  name: Open Dental Payments API
  slug: opendental-payments-api
- description: CONFIRMED. ProcedureLogs, insurance history, and group notes.
  name: Open Dental Procedures API
  slug: opendental-procedures-api
- description: CONFIRMED. Dentists, hygienists, and billing entities.
  name: Open Dental Providers API
  slug: opendental-providers-api
- description: MODELED. Hygiene / continuing-care recalls.
  name: Open Dental Recalls API
  slug: opendental-recalls-api
- description: MODELED. Referral sources and attachments.
  name: Open Dental Referrals API
  slug: opendental-referrals-api
- description: MODELED. Configurable clinical and administrative forms.
  name: Open Dental Sheets API
  slug: opendental-sheets-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Open Dental Accounts & Ledger API
  slug: open-opendental-accounts-ledger-api
- collection_type: open
  name: Open Dental Accounts & Ledger Appointments API
  slug: open-opendental-appointments-api
- collection_type: open
  name: Open Dental Accounts & Ledger Claims API
  slug: open-opendental-claims-api
- collection_type: open
  name: Open Dental Accounts & Ledger Documents API
  slug: open-opendental-documents-api
- collection_type: open
  name: Open Dental Accounts & Ledger Fees & Fee Schedules API
  slug: open-opendental-fees-fee-schedules-api
- collection_type: open
  name: Open Dental Accounts & Ledger Medications & Prescriptions API
  slug: open-opendental-medications-prescriptions-api
- collection_type: open
  name: Open Dental Accounts & Ledger Patients API
  slug: open-opendental-patients-api
- collection_type: open
  name: Open Dental Accounts & Ledger Payments API
  slug: open-opendental-payments-api
- collection_type: open
  name: Open Dental Accounts & Ledger Procedures API
  slug: open-opendental-procedures-api
- collection_type: open
  name: Open Dental Accounts & Ledger Providers API
  slug: open-opendental-providers-api
- collection_type: open
  name: Open Dental Accounts & Ledger Recalls API
  slug: open-opendental-recalls-api
- collection_type: open
  name: Open Dental Accounts & Ledger Referrals API
  slug: open-opendental-referrals-api
- collection_type: open
  name: Open Dental Accounts & Ledger Sheets API
  slug: open-opendental-sheets-api
- collection_type: open
  name: Open Dental API
  slug: open-opendental
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opendental-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendental-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opendental-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenDental
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/open-dental-software
- group: company
  title: ''
  type: Website
  url: https://www.opendental.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.opendental.com/site/apispecification.html
- group: commercial
  title: ''
  type: Plans
  url: plans/opendental-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendental-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendental-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://opendental.blog/feed/
created: '2026-07-03'
description: Open Dental is dental practice management software with an openly documented public REST API. The API is hosted at Open Dental headquarters (base https://api.opendental.com/api/v1) and lets approved third-party developers read and write practice data - patients, appointments, providers, procedures, insurance claims, payments, ledger adjustments, fee schedules, recalls, documents, medications and prescriptions, referrals, and clinical sheets - on behalf of Open Dental customers. Requests authenticate with a per-application Developer Key and a per-customer Customer Key sent together in an Authorization ODFHIR {DeveloperKey}/{CustomerKey} header. The public spec documents 130+ resource groups with GET/POST/PUT/DELETE operations. Open Dental also runs a local API Service option that talks to the on-premises Open Dental program without routing through Open Dental's servers, and a separate FHIR interface.
finops:
- name: Opendental Finops
  service_category: Healthcare and Practice Management
  slug: opendental-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendental.png
layout: provider
modified: '2026-07-03'
name: Open Dental
nav: Providers
network: true
overview: 'Open Dental publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Accounts & Ledger API, Appointments API, Claims API, and 10 more. Tagged areas include Dental, Practice Management, Healthcare, EHR, and Patient Records.


  Open Dental''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Opendental Plans Pricing
  plan_count: 3
  slug: opendental-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 4
  name: Opendental Rate Limits
  slug: opendental-rate-limits
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.9
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
    score: 15.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendental/refs/heads/main/screenshots/opendental-2026-08-07T190545.png
security:
- kind: authentication
  name: Opendental Authentication
  slug: opendental-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Opendental Domain Security
  slug: opendental-domain-security
  summary_line: TLSv1.3 · DMARC
slug: opendental
tags:
- Dental
- Practice Management
- Healthcare
- EHR
- Patient Records
- REST
website: https://www.opendental.com
---
