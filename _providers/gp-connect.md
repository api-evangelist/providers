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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Gp Connect Agentic Access
  operation_count: 14
  slug: gp-connect-agentic-access
  summary_line: 14 operations · 5 acting
api_count: 5
apis:
- description: Retrieve unstructured documents (e.g. scanned letters, attachments) from a patient's GP practice record. Complements the structured access API for cases where clinical information is held as binary do
  name: GP Connect Access Document FHIR API
  slug: access-document-fhir
- description: Send a PDF consultation summary or clinical document to a patient's registered GP practice. Used when a patient is seen in a non-GP setting (out-of-hours, community pharmacy, urgent care centre) and t
  name: GP Connect Send Document FHIR API
  slug: send-document-fhir
- description: The Appointment API from GP Connect — 2 operation(s) for appointment.
  name: GP Connect Appointment API
  slug: gp-connect-appointment-api
- description: The Documents API from GP Connect — 2 operation(s) for documents.
  name: GP Connect Documents API
  slug: gp-connect-documents-api
- description: The FHIR API from GP Connect — 1 operation(s) for fhir.
  name: GP Connect FHIR API
  slug: gp-connect-fhir-api
- description: The Meta API from GP Connect — 1 operation(s) for meta.
  name: GP Connect Meta API
  slug: gp-connect-meta-api
- description: The Patient API from GP Connect — 4 operation(s) for patient.
  name: GP Connect Patient API
  slug: gp-connect-patient-api
- description: The Slot API from GP Connect — 1 operation(s) for slot.
  name: GP Connect Slot API
  slug: gp-connect-slot-api
- description: The Task API from GP Connect — 1 operation(s) for task.
  name: GP Connect Task API
  slug: gp-connect-task-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: gp-connect-access-record-structured-fhir Appointment API
  slug: open-gp-connect-appointment-api
- collection_type: open
  name: gp-connect-access-record-structured-fhir Appointment Documents API
  slug: open-gp-connect-documents-api
- collection_type: open
  name: gp-connect-access-record-structured- Appointment FHIR API
  slug: open-gp-connect-fhir-api
- collection_type: open
  name: gp-connect-access-record-structured-fhir Appointment Meta API
  slug: open-gp-connect-meta-api
- collection_type: open
  name: gp-connect-access-record-structured-fhir Appointment Patient API
  slug: open-gp-connect-patient-api
- collection_type: open
  name: gp-connect-access-record-structured-fhir Appointment Slot API
  slug: open-gp-connect-slot-api
- collection_type: open
  name: gp-connect-access-record-structured-fhir Appointment Task API
  slug: open-gp-connect-task-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/gp-connect-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gp-connect-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gp-connect-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gp-connect-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://digital.nhs.uk/services/gp-connect
- group: docs
  title: ''
  type: Documentation
  url: https://digital.nhs.uk/developer/api-catalogue
- group: operate
  title: ''
  type: HelpAndSupport
  url: https://digital.nhs.uk/developer/help-and-support
- group: start
  title: ''
  type: Signup
  url: https://digital.nhs.uk/services/gp-connect/develop-gp-connect-services/specifications-for-developers
- group: auth
  title: ''
  type: Authentication
  url: https://digital.nhs.uk/developer/guides-and-documentation/security-and-authorisation/user-restricted-restful-apis-nhs-login-separate-authentication-and-authorisation
- group: start
  title: ''
  type: GettingStarted
  url: https://digital.nhs.uk/services/gp-connect/develop-gp-connect-services/specifications-for-developers
- group: build
  title: ''
  type: GitHub
  url: https://github.com/NHSDigital
- group: other
  title: ''
  type: Standards
  url: https://standards.nhs.uk/published-standards/gp-connect-access-record-structured-fhir-api
- group: start
  title: ''
  type: Sandbox
  url: https://orange.testlab.nhs.uk/
- group: other
  title: ''
  type: ServiceLevel
  url: https://digital.nhs.uk/developer/guides-and-documentation/reference-guide#service-levels
- group: other
  title: ''
  type: NetworkAccess
  url: https://digital.nhs.uk/developer/guides-and-documentation/network-access-for-apis
- group: build
  title: ''
  type: ClinicalSafety
  url: https://digital.nhs.uk/services/clinical-safety
- group: commercial
  title: ''
  type: Plans
  url: plans/gp-connect-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gp-connect-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gp-connect-finops.yml
created: '2026-06-13'
description: GP Connect is a national NHS England interoperability programme that enables authorised clinical and patient-facing systems to securely access and update patient records held in GP principal clinical systems (EMIS Web, SystmOne, Vision). The programme exposes a suite of FHIR-based REST APIs spanning structured clinical record access (medications, allergies, immunisations, consultations, problems, investigations), unstructured document retrieval, appointment management, document sending, record updating, and patient-facing services for patients to view their own records, manage repeat prescriptions, and book appointments via the NHS App. Clinical system APIs are mediated through the Spine Security Proxy (SSP) over HSCN; patient-facing APIs use NHS login OpenID Connect at P9 identity verification. Access requires NHS England onboarding, an approved clinical use case, information governance compliance, and a clinical safety officer holding DCB0129 and DCB0160 certification. The
  service is funded by NHS England at no direct API cost to consuming organisations.
finops:
- name: Gp Connect Finops
  service_category: Healthcare Interoperability
  slug: gp-connect-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gp-connect.png
jsonld:
- class_count: 0
  name: Gp Connect Context
  property_count: 0
  slug: gp-connect
layout: provider
modified: '2026-06-13'
name: GP Connect
nav: Providers
network: true
overview: 'GP Connect publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Appointment API, Documents API, FHIR API, and 4 more. Tagged areas include NHS, FHIR, Healthcare, GP Records, and Appointments.


  The GP Connect catalog on APIs.io includes 1 JSON-LD context.


  GP Connect''s developer surface includes developer portal, documentation, signup flow, authentication, getting-started guide, GitHub presence, sandbox, and 12 more developer resources.'
plans:
- name: Gp Connect Plans
  plan_count: 3
  slug: gp-connect-plans
random_paper: 19
rate_limits:
- limit_count: 3
  name: Gp Connect Rate Limits
  slug: gp-connect-rate-limits
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 43.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 54.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gp-connect/refs/heads/main/screenshots/gp-connect-2026-07-25T220156.png
security:
- kind: domain-security
  name: Gp Connect Domain Security
  slug: gp-connect-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gp Connect Vulnerability Disclosure
  slug: gp-connect-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: gp-connect
tags:
- NHS
- FHIR
- Healthcare
- GP Records
- Appointments
- Prescriptions
- Interoperability
- UK
- Patient Records
- Electronic Health Records
- FHIR STU3
- FHIR R4
website: https://digital.nhs.uk/services/gp-connect
---
