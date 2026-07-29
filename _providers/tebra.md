---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tebra Agentic Access
  operation_count: 14
  slug: tebra-agentic-access
  summary_line: 14 operations
api_count: 8
apis:
- description: SOAP operations for patient records - GetPatient, GetPatients, GetAllPatients, CreatePatient, UpdatePatient, UpdatePatientsExternalID, and UpdatePrimaryPatientCase. Part of the former Kareo Integratio
  name: Tebra Patients API
  slug: tebra-patients-api
- description: SOAP operations for scheduling - GetAppointment, GetAppointments, CreateAppointment, UpdateAppointment, UpdateAppointmentStatus, DeleteAppointment, plus GetAppointmentReasons and CreateAppointmentReas
  name: Tebra Appointments API
  slug: tebra-appointments-api
- description: SOAP reference-data operations - GetProviders, GetPractices, GetServiceLocations, and GetProcedureCodes - used to resolve the providers, practices, locations, and procedure codes referenced by patient
  name: Tebra Providers and Practices API
  slug: tebra-providers-practices-api
- description: SOAP revenue-cycle operations covering charges, encounters, payments, and transactions - GetCharges, GetEncounterDetails, CreateEncounter, UpdateEncounterStatus, GetPayments, CreatePayment, and GetTra
  name: Tebra Billing and Claims API
  slug: tebra-billing-claims-api
- description: SOAP operations for attaching and removing documents on practice records - CreateDocument and DeleteDocument - along with external-vendor utilities GetExternalVendors, RegisterExternalVendor, GetCusto
  name: Tebra Documents API
  slug: tebra-documents-api
- description: USCDI-aligned clinical data classes for the authenticated patient.
  name: Tebra Clinical API
  slug: tebra-clinical-api
- description: Binary clinical summary documents (e.g. C-CDA).
  name: Tebra Documents API
  slug: tebra-documents-api
- description: Core patient demographic record.
  name: Tebra Patient API
  slug: tebra-patient-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tebra-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tebra-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tebra-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tebra-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tebra
- group: company
  title: ''
  type: Website
  url: https://www.tebra.com
- group: docs
  title: ''
  type: Documentation
  url: https://helpme.tebra.com/Tebra_PM/12_API_and_Integration
- group: commercial
  title: ''
  type: Plans
  url: plans/tebra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tebra-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tebra-finops.yml
created: '2026-07-10'
description: Tebra is a healthcare technology company providing an all-in-one operating system for independent medical practices - EHR, practice management, medical billing, patient engagement, and practice growth. Tebra was formed from the 2021 merger of Kareo (practice management and billing) and PatientPop (practice growth), and its developer surface reflects that lineage. Two documented API surfaces exist. The Tebra SOAP Practice Management API - the former Kareo Integration API, still served at webservice.kareo.com - covers patients, appointments, providers, practices, charges, encounters, payments, and transactions, and is partner / administrator gated. The Tebra Clinical Data API is a REST patient-access API published under tebra.com/macra (ONC / 21st Century Cures Act), exposing USCDI clinical data with an API Key the patient generates from the Tebra Patient Portal.
finops:
- name: Tebra Finops
  service_category: Healthcare Practice Management and EHR
  slug: tebra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tebra.png
layout: provider
modified: '2026-07-10'
name: Tebra
nav: Providers
network: true
overview: 'Tebra publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Clinical API, and 2 more. Tagged areas include Healthcare, Practice Management, EHR, Medical Billing, and Patient Engagement.


  Tebra''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Tebra Plans Pricing
  plan_count: 3
  slug: tebra-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 3
  name: Tebra Rate Limits
  slug: tebra-rate-limits
score:
  band: thin
  composite: 37.2
  delta: -4.9
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Tebra Authentication
  slug: tebra-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tebra Domain Security
  slug: tebra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tebra Trust Center
  slug: tebra-trust-center
  summary_line: PCI DSS, HIPAA
slug: tebra
tags:
- Healthcare
- Practice Management
- EHR
- Medical Billing
- Patient Engagement
- Kareo
- PatientPop
website: https://www.tebra.com
---
