---
access_model:
  confidence: high
  label: Enterprise · Sandbox self-serve · Production partner-gated
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - well-known
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.6
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Epic's HL7 FHIR R4 (4.0.1) REST API, aligned to the US Core implementation guides and exposing 59 resource types (Patient, Encounter, Observation, Condition, MedicationRequest, DiagnosticReport, Docum
  name: Epic FHIR R4 API
  slug: epic-fhir-r4-api
- description: Epic's HL7 FHIR STU3 (3.0.1) REST API for clinical and administrative resources, authorized with SMART on FHIR / OAuth 2.0. A live public sandbox CapabilityStatement was harvested verbatim.
  name: Epic FHIR STU3 API
  slug: epic-fhir-stu3-api
- description: Epic's HL7 FHIR DSTU2 (1.0.2) REST API, published as a FHIR Conformance resource covering the legacy DSTU2 resource set. A live public sandbox Conformance statement was harvested verbatim.
  name: Epic FHIR DSTU2 API
  slug: epic-fhir-dstu2-api
- description: Epic's SMART on FHIR / OAuth 2.0 authorization surface backing the FHIR APIs. The live .well-known/smart-configuration advertises authorize/token endpoints, grant types (authorization_code, refresh_to
  name: Epic SMART on FHIR Authorization
  slug: epic-smart-on-fhir-authorization
- description: Epic's implementation of the HL7 FHIR Bulk Data Access (Flat FHIR) specification, providing backend system-level population export via the $export operation, authorized with OAuth 2.0 client-credentia
  name: Epic FHIR Bulk Data Access API
  slug: epic-fhir-bulk-data-api
- description: Epic's support for the CDS Hooks specification, letting external clinical decision support services return cards and SMART app launch links at documented workflow hook points inside the Epic EHR. Docu
  name: Epic CDS Hooks API
  slug: epic-cds-hooks-api
artifact_total: 11
asyncapis:
- description: ''
  name: Epic Systems Cds Hooks Webhooks
  slug: epic-systems-cds-hooks-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/epic-systems-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epic-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.epic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fhir.epic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fhir.epic.com/Documentation
- group: docs
  title: ''
  type: APIReference
  url: https://fhir.epic.com/Specifications
- group: start
  title: ''
  type: GettingStarted
  url: https://fhir.epic.com/Documentation?docId=fhirtutorial
- group: auth
  title: ''
  type: Authentication
  url: authentication/epic-systems-authentication.yml
- group: start
  title: ''
  type: SignUp
  url: https://fhir.epic.com/Developer/Index
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fhir.epic.com/Download/ApiLicenseAgreement
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/epic1979/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/epic-systems-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/epic-systems-security.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/epic-systems-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/epic-systems-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/epic-systems-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/epic-systems-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/epic-systems-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/epic-systems-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/epic-systems-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/epic-systems-cds-hooks-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/epic-systems-llms.txt
- group: auth
  title: ''
  type: Security
  url: https://www.epic.com/epic/page/reporting-potential-security-vulnerability/
created: '2026-07-24'
description: Epic Systems Corporation is a privately held electronic health record (EHR/EMR) software company founded in 1979 and headquartered in Verona, Wisconsin, United States. Epic's software supports the medical records of a large share of U.S. hospital systems and academic medical centers, and its "Epic on FHIR" developer program (fhir.epic.com / open.epic.com) exposes a standards-based HL7 FHIR interoperability surface for patient- and provider-facing apps. Epic serves live, public sandbox FHIR endpoints across three FHIR versions - R4 (4.0.1), STU3 (3.0.1), and DSTU2 (1.0.2) - aligned to the US Core implementation guides, with SMART on FHIR / OAuth 2.0 authorization, CDS Hooks, and FHIR Bulk Data ($export) access. Production access requires client registration and a health system's participation; the developer sandbox, specifications, and CapabilityStatements are openly published. Epic is a core node of the U.S. healthcare interoperability landscape shaped by the ONC/CMS 21st Century
  Cures Act information-blocking rules and TEFCA.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Epic Systems
nav: Providers
network: true
overview: 'Epic Systems publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, EHR, EMR, and FHIR.


  The Epic Systems catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Epic Systems'' developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, and 18 more developer resources.'
random_paper: 24
scopes:
- name: Epic Systems Scopes
  scope_count: 0
  slug: epic-systems-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.6
  delta: 5.4
  facets:
    commercial_clarity: 23.7
    contract_quality: 55.0
    developer_ergonomics: 45.7
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 18.4
  previous_composite: 39.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 72.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/epic-systems/refs/heads/main/screenshots/epic-systems-2026-07-25T213516.png
security:
- kind: authentication
  name: Epic Systems Authentication
  slug: epic-systems-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Epic Systems Domain Security
  slug: epic-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Epic Systems Vulnerability Disclosure
  slug: epic-systems-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: epic-systems
tags:
- Healthcare
- United States
- EHR
- EMR
- FHIR
- HL7
- Interoperability
- SMART on FHIR
- US Core
- Clinical Data
website: https://www.epic.com/
---
