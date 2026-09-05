---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 7
apis:
- description: Access to the tab32 patient data object - demographics, contact and insurance details, and patient records - for integrating patient management into CRM, patient-facing apps, and enterprise systems. E
  name: tab32 Patients API
  slug: tab32-patients-api
- description: Access to the tab32 provider data object - dentists, hygienists, and other practitioners across a practice or DSO's locations. Endpoint paths are not published publicly; access is via the partner-gate
  name: tab32 Providers API
  slug: tab32-providers-api
- description: Access to the tab32 schedule data object - appointments, availability, and booking - supporting online booking, recall, and appointment-scheduling integrations. Endpoint paths are not published public
  name: tab32 Schedule API
  slug: tab32-schedule-api
- description: Access to the tab32 charts data object - clinical and periodontal charting and treatment planning data - for clinical workflow and analytics integrations. Endpoint paths are not published publicly; ac
  name: tab32 Charts API
  slug: tab32-charts-api
- description: Access to the tab32 notes data object - clinical and progress notes attached to patient and encounter records. Endpoint paths are not published publicly; access is via the partner-gated developer port
  name: tab32 Notes API
  slug: tab32-notes-api
- description: Access to the tab32 ledger data object - patient and practice financial ledger, charges, and insurance claim / revenue-cycle data. Endpoint paths are not published publicly; access is via the partner-
  name: tab32 Ledger API
  slug: tab32-ledger-api
- description: Access to the tab32 payments data object - patient payments and transaction records (tab32 integrates payment processing via Stripe). Endpoint paths are not published publicly; access is via the partn
  name: tab32 Payments API
  slug: tab32-payments-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tab32-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tab32
- group: company
  title: ''
  type: Website
  url: https://tab32.com
- group: docs
  title: ''
  type: Documentation
  url: https://tab32.com/application-programming-interface
- group: commercial
  title: ''
  type: Plans
  url: plans/tab32-plans-pricing.yml
created: '2026-07-04'
description: tab32 is a cloud-based dental practice management, imaging, and analytics platform for dental practices and dental service organizations (DSOs). tab32 offers a real, commercial API - powered by Google Apigee and HIPAA / SOC 2 Type II compliant - that exposes tab32's patient, provider, schedule, charts, notes, ledger, and payments data objects to DSOs and third-party developers. Access is partner-gated, not open self-service - developers reach the API through tab32's developer API portal after establishing a partnership or enterprise relationship, and full endpoint reference, authentication, and base URL details live behind that portal rather than on the public website. The API entries below are modeled from tab32's publicly documented data objects and API messaging; their endpoint paths are not published publicly and are therefore illustrative, not confirmed.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tab32.png
layout: provider
modified: '2026-07-04'
name: tab32
nav: Providers
network: true
overview: 'tab32 publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Dental, Practice Management, Healthcare, Cloud Dental Software, and DSO.


  tab32''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Tab32 Plans Pricing
  plan_count: 3
  slug: tab32-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 3
    catalog_earned: 47.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tab32/refs/heads/main/screenshots/tab32-2026-09-02T161700.png
security:
- kind: domain-security
  name: Tab32 Domain Security
  slug: tab32-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tab32
tags:
- Dental
- Practice Management
- Healthcare
- Cloud Dental Software
- DSO
- HIPAA
- Patient Data
- Partner API
website: https://tab32.com
---
