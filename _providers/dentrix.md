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
  scored_at: '2026-08-06'
api_count: 7
apis:
- description: Retrieve and (with the Write API / Ascend scopes) manage patient demographics, contact details, household and responsible-party relationships, and patient status. On Dentrix Ascend this is a REST/JSON
  name: Dentrix Patients API
  slug: dentrix-patients-api
- description: Read the schedule and book, reschedule, or cancel appointments. In the Dentrix Developer Program this maps to the commercial-only Scheduling API; on Dentrix Ascend it is a REST scheduling resource. En
  name: Dentrix Appointments & Scheduling API
  slug: dentrix-appointments-api
- description: Look up providers, operatories, and practice/location metadata used to associate appointments, procedures, and production with the responsible dentist or hygienist. Read-oriented reference data expose
  name: Dentrix Providers API
  slug: dentrix-providers-api
- description: Access clinical and treatment data - procedure codes (CDT), completed and planned procedures, treatment plans, and clinical notes. Surfaced through clinical table views and stored procedures on the De
  name: Dentrix Procedures & Treatment API
  slug: dentrix-procedures-treatment-api
- description: Read insurance coverage and claim status and, on Ascend, submit claims. The Dentrix Developer Program exposes a dedicated Claims Summary API for practice-level claims reporting; Dentrix Ascend support
  name: Dentrix Insurance & Claims API
  slug: dentrix-insurance-claims-api
- description: Access account ledgers, charges, payments, adjustments, and balances for patient and insurance financial reconciliation. Read via financial table views and stored procedures (desktop) or REST ledger r
  name: Dentrix Ledger & Billing API
  slug: dentrix-ledger-billing-api
- description: 'Read prescription and medication history captured in the patient clinical record. Availability is subject to program category and partner agreement; exposed through clinical table views/DLL functions '
  name: Dentrix Prescriptions API
  slug: dentrix-prescriptions-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dentrix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dentrix.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/henry-schein-one
- group: docs
  title: ''
  type: Documentation
  url: https://ddp.dentrix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.henryscheinone.com/dental-solutions/api-exchange
- group: start
  title: ''
  type: SignUp
  url: https://ddp.dentrix.com/pages/faq
- group: commercial
  title: ''
  type: Plans
  url: plans/dentrix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dentrix-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.henryscheinone.com/insights/blogs/
created: '2026-07-03'
description: 'Dentrix is a dental practice management platform from Henry Schein One, used by dental offices to manage patients, scheduling, clinical charting, treatment planning, insurance, and billing. Dentrix exposes third-party integration APIs through two distinct channels. The original Dentrix Developer Program (DDP, launched 2012) targets the on-premise Dentrix desktop application: integrations run locally against the office''s Dentrix database over password-protected ODBC connections, stored procedures, table views, and DLL functions (authenticated via a RegisterUser call) - it is NOT a public REST/cloud API, and cloud integrations require a locally installed desktop agent. The newer Dentrix Ascend API Exchange (launched July 2023) is a cloud, REST/JSON API over HTTPS secured with OAuth 2.0 on the SOC 2 Type II Dentrix Ascend platform, exposing patient, scheduling, claims, and inventory data. Both channels are partner-gated: access requires an application, a signed agreement, and
  paid developer fees. There is no public self-serve API key or published OpenAPI, so the APIs below are modeled from Henry Schein One''s public developer materials rather than an official machine-readable specification.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dentrix.png
layout: provider
modified: '2026-07-03'
name: Dentrix
nav: Providers
network: true
overview: 'Dentrix publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Dental, Practice Management, Healthcare, Dentistry, and Patient Data.


  Dentrix''s developer surface includes documentation, signup flow, engineering blog, and 6 more developer resources.'
plans:
- name: Dentrix Plans Pricing
  plan_count: 3
  slug: dentrix-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 5
  name: Dentrix Rate Limits
  slug: dentrix-rate-limits
score:
  band: emerging
  composite: 19.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 19.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dentrix/refs/heads/main/screenshots/dentrix-2026-07-25T211726.png
security:
- kind: domain-security
  name: Dentrix Domain Security
  slug: dentrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dentrix
tags:
- Dental
- Practice Management
- Healthcare
- Dentistry
- Patient Data
- EHR
- Partner API
- Henry Schein One
website: https://www.dentrix.com/
---
