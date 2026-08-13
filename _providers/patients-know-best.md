---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: HL7 FHIR STU3 (3.0.2) "Facade" server exposing Patients Know Best personal health record data — Patient, Appointment, Communication, Consent, DiagnosticReport, DocumentReference, Encounter, Observatio
  name: PKB Facade FHIR API
  slug: pkb-facade-fhir-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/patients-know-best-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://patientsknowbest.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wiki.patientsknowbest.com/space/api
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.patientsknowbest.com/space/api/3363602489/FHIR%C2%AE+APIs
- group: docs
  title: ''
  type: APIReference
  url: https://pkbdev.atlassian.net/wiki/spaces/api/pages/3363602541/FHIR+Conformance
- group: operate
  title: ''
  type: Roadmap
  url: https://wiki.patientsknowbest.com/space/api
- group: operate
  title: ''
  type: Support
  url: https://manual.patientsknowbest.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.patientsknowbest.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://patientsknowbest.com/privacy-statement/
- group: start
  title: ''
  type: SignUp
  url: https://patientsknowbest.com/register/
- group: start
  title: ''
  type: Login
  url: https://my.patientsknowbest.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.pkbstatus.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://wiki.patientsknowbest.com/space/REL
- group: company
  title: ''
  type: Partners
  url: https://patientsknowbest.com/partners/
- group: auth
  title: ''
  type: Authentication
  url: authentication/patients-know-best-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/patients-know-best-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/patients-know-best-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://patientsknowbest.com
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/patients-know-best-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/patients-know-best-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/patients-know-best-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/patients-know-best-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/patients-know-best-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/patients-know-best-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/patients-know-best-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/patients-know-best-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://my.patientsknowbest.com/.well-known/security.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/patients-know-best-sandbox.yml
created: '2026-07-17'
description: Patients Know Best (PKB) is a UK health-technology company operating what it describes as the world's largest personal health record, with more than seven million registered patients across the NHS and other health systems. The platform lets patients hold, view and share their medical records, messages, test results, care plans and questionnaires with clinicians and carers across web, mobile and the NHS App. For integrators, PKB publishes a HL7 FHIR STU3 (3.0.2) API — the "Facade" FHIR server at my.patientsknowbest.com/fhir — that conforms to the NHS CareConnect profiles and exposes patient demographics, documents, observations, appointments, consent, questionnaires and read receipts, secured with OAuth 2.0 client-credentials. PKB was surfaced as a Seedcamp portfolio company and enriched into the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/patients-know-best.png
layout: provider
mcp_servers:
- description: ''
  name: patients-know-best-mcp.yml
  slug: patients-know-best-mcpyml
modified: '2026-08-08'
name: Patients Know Best
nav: Providers
network: true
overview: 'Patients Know Best publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Electronic Health Records, and Personal Health Record.


  Patients Know Best''s developer surface includes documentation, API reference, support, engineering blog, signup flow, changelog, authentication, and 22 more developer resources.'
random_paper: 39
score:
  band: developing
  composite: 42.6
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 40.0
    developer_ergonomics: 51.6
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 47.4
  previous_composite: 42.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 40.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/patients-know-best/refs/heads/main/screenshots/patients-know-best-2026-08-07T191555.png
security:
- kind: authentication
  name: Patients Know Best Authentication
  slug: patients-know-best-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Patients Know Best Domain Security
  slug: patients-know-best-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Patients Know Best Vulnerability Disclosure
  slug: patients-know-best-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: patients-know-best
tags:
- Company
- Health
- Healthcare
- Electronic Health Records
- Personal Health Record
- FHIR
- Interoperability
- NHS
- Patient Data
- Medical Records
website: https://patientsknowbest.com
---
