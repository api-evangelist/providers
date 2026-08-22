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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tebra Agentic Access
  operation_count: 14
  slug: tebra-agentic-access
  summary_line: 14 operations
api_count: 9
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
- description: USCDI-aligned clinical data classes for the authenticated patient. Base host (api.tebra.com) is the host documented in Tebra's own "General API Documentation" (Oct 2023) PDF and matches this spec's se
  name: Tebra Clinical API
  slug: tebra-clinical-api
- description: Binary clinical summary documents (e.g. C-CDA). Base host (api.tebra.com) matches the Oct 2023 "General API Documentation" PDF and this spec's servers[], but as of 2026-08-14 it returns NXDOMAIN on pu
  name: Tebra Documents API
  slug: tebra-documents-api
- description: Core patient demographic record. Base host (api.tebra.com) matches the Oct 2023 "General API Documentation" PDF and this spec's servers[], but as of 2026-08-14 it returns NXDOMAIN on public DNS resolv
  name: Tebra Patient API
  slug: tebra-patient-api
- description: SMART on FHIR (HL7 FHIR R4) patient-access API built on US Core Implementation Guide STU3 Release 3.1.1, satisfying USCDI v1 / ONC 21st Century Cures Act information-blocking requirements. Hosted on t
  name: Tebra FHIR API
  slug: tebra-fhir-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tebra Data Clinical API
  slug: open-tebra-clinical-api
- collection_type: open
  name: Tebra Data Clinical Documents API
  slug: open-tebra-documents-api
- collection_type: open
  name: Tebra Data Clinical Patient API
  slug: open-tebra-patient-api
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tebra-scopes.yml
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
  type: Compliance
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
- group: operate
  title: ''
  type: Support
  url: https://helpme.tebra.com
- group: company
  title: ''
  type: Blog
  url: https://www.tebra.com/theintake
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tebra.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tebra.com/tebra-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tebra.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tebra.com
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
- group: design
  title: ''
  type: Conformance
  url: conformance/tebra-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tebra-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tebra-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tebra-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tebra-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tebra-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/tebra-packages.yml
created: '2026-07-10'
description: Tebra is a healthcare technology company providing an all-in-one operating system for independent medical practices - EHR, practice management, medical billing, patient engagement, and practice growth. Tebra was formed from the 2021 merger of Kareo (practice management and billing) and PatientPop (practice growth), and its developer surface reflects that lineage. Three documented API surfaces exist. The Tebra SOAP Practice Management API - the former Kareo Integration API, still served at webservice.kareo.com - covers patients, appointments, providers, practices, charges, encounters, payments, and transactions, and is partner / administrator gated. The Tebra Clinical Data API is a REST patient-access API documented under tebra.com/macra (ONC / 21st Century Cures Act) with an API Key the patient generates from the Tebra Patient Portal; its documented host (api.tebra.com) no longer resolves in DNS as of this review. Tebra has since published a SMART on FHIR API (R4, US Core STU3
  3.1.1, USCDI v1) at fhir.prd.cloud.tebra.com, built on the SmileCDR platform, offering no-charge patient read (GET) access to USCDI clinical resources over 2-legged or 3-legged OAuth 2.0.
finops:
- name: Tebra Finops
  service_category: Healthcare Practice Management and EHR
  slug: tebra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tebra.png
layout: provider
mcp_servers:
- description: ''
  name: tebra-mcp.yml
  slug: tebra-mcpyml
modified: '2026-08-14'
name: Tebra
nav: Providers
network: true
overview: 'Tebra publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Clinical API, and 3 more. Tagged areas include Healthcare, Practice Management, EHR, Medical Billing, and Patient Engagement.


  Tebra''s developer surface includes authentication, documentation, support, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Tebra Plans Pricing
  plan_count: 3
  slug: tebra-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Tebra Rate Limits
  slug: tebra-rate-limits
scopes:
- name: Tebra Scopes
  scope_count: 27
  slug: tebra-scopes
  summary_line: 27 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 63.3
  delta: 9.3
  facets:
    access_clarity: 86.8
    commercial_clarity: 86.8
    contract_governance: 12.1
    contract_quality: 57.3
    developer_ergonomics: 28.6
    discoverability: 81.5
    governance: 12.1
    operational_transparency: 47.4
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 86.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/tebra/refs/heads/main/screenshots/tebra-2026-08-17T082258.png
security:
- kind: authentication
  name: Tebra Authentication
  slug: tebra-authentication
  summary_line: apiKey/oauth2 · 3 schemes
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
