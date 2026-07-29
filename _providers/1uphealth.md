---
access_model:
  confidence: high
  label: Enterprise · Gated developer console (public docs)
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - documentation
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-07-28'
api_count: 10
apis:
- description: 1upHealth's managed HL7 FHIR R4 (4.0.1) REST API cloud server, exposing 144 FHIR resource types with SMART-on-FHIR OAuth 2.0 security. Publishes a live CapabilityStatement at /fhir/r4/metadata.
  name: 1up FHIR API (R4)
  slug: 1uphealth-fhir-r4-api
- description: 1upHealth's managed HL7 FHIR STU3 (3.0.2) REST API cloud server, exposing 117 FHIR resource types. Publishes a live CapabilityStatement at /fhir/stu3/metadata.
  name: 1up FHIR API (STU3)
  slug: 1uphealth-fhir-stu3-api
- description: 1upHealth's managed HL7 FHIR DSTU2 (1.0.2) REST API cloud server, exposing 94 FHIR resource types. Publishes a live Conformance statement at /fhir/dstu2/metadata.
  name: 1up FHIR API (DSTU2)
  slug: 1uphealth-fhir-dstu2-api
- description: CMS Patient Access solution delivering member clinical and claims data to patient-authorized third-party apps over FHIR, aligned to the CARIN Blue Button and US Core implementation guides.
  name: 1up Patient Access API
  slug: 1uphealth-patient-access-api
- description: CMS Provider Access solution enabling payers to share member data with in-network providers over FHIR, aligned to the Da Vinci implementation guides.
  name: 1up Provider Access API
  slug: 1uphealth-provider-access-api
- description: CMS Payer-to-Payer Data Exchange solution for sharing a member's historical clinical and claims data between health plans over FHIR when a member changes payers.
  name: 1up Payer-to-Payer Data Exchange API
  slug: 1uphealth-payer-to-payer-api
- description: Publicly accessible FHIR Provider Directory publishing accurate provider and network listings, aligned to the Da Vinci PDEX Plan-Net implementation guide.
  name: 1up Provider Directory API
  slug: 1uphealth-provider-directory-api
- description: CMS-0057-F Electronic Prior Authorization solution automating prior authorization submission and decisioning over FHIR, aligned to the Da Vinci PAS / DTR / CRD implementation guides.
  name: 1up Electronic Prior Authorization API
  slug: 1uphealth-epa-api
- description: Connectivity solution that acquires patient-authorized clinical records from a national network of EHR/provider and payer connections and normalizes them into the 1up FHIR data store.
  name: 1up Patient Connect
  slug: 1uphealth-patient-connect-api
- description: Population-scale connectivity and Bulk Data (Flat FHIR) export solution for acquiring and computing over large member/patient populations as FHIR.
  name: 1up Population Connect (Bulk FHIR)
  slug: 1uphealth-population-connect-api
artifact_total: 16
asyncapis:
- description: ''
  name: 1Uphealth Subscription Webhooks
  slug: 1uphealth-subscription-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/1uphealth-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1uphealth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1up.health/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.1up.health/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.1up.health/
- group: start
  title: ''
  type: DeveloperConsole
  url: https://developer.1up.health/
- group: company
  title: ''
  type: Blog
  url: https://1up.health/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.1up.health/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.1up.health/
- group: auth
  title: ''
  type: Security
  url: https://trust.1up.health/
- group: operate
  title: ''
  type: Support
  url: https://1uphealth.my.site.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.1up.health/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/1uphealth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1up.health/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://1up.health/privacy-policy/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.1up.health/help-center/Content/en-US/api-references/rest-api-reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.1up.health/docs/get-started/faq
- group: build
  title: ''
  type: Postman
  url: https://docs.1up.health/help-center/Content/en-US/get-started/quick-start/postman.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/1uphealth-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/1uphealth-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/1uphealth-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/1uphealth-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/1uphealth-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.1up.health/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/1uphealth-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/1uphealth-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/1uphealth-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1uphealth-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/1uphealth-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/1uphealth-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/1uphealth-subscription-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/1uphealth-well-known.yml
created: '2026-07-24'
description: 1upHealth is a US healthcare data interoperability company, founded in 2017 and headquartered in Boston, Massachusetts, that operates an HL7 FHIR-first health data platform for claims and clinical data acquisition, exchange, and compute. Built on a lakehouse architecture, the platform lets health plans, providers, and digital health developers ingest, normalize, store, and query patient and member data as FHIR, and ships modular solutions aligned to US federal interoperability mandates - Patient Access, Provider Access, Payer-to-Payer Data Exchange, Provider Directory, Formulary, and Electronic Prior Authorization (CMS Interoperability & Prior Authorization, CMS-0057-F). 1upHealth runs a managed, HIPAA-compliant FHIR REST API cloud server exposing FHIR R4 (4.0.1), STU3 (3.0.2), and DSTU2 (1.0.2) endpoints, each publishing a live CapabilityStatement, secured with SMART-on-FHIR OAuth 2.0. The company is HITRUST, SOC 2, and HIPAA aligned. Home market is the United States. Developer
  documentation is public at docs.1up.health, while provisioning API credentials and the developer console require an account (gated self-serve / partner onboarding).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: 1uphealth-mcp.yml
  slug: 1uphealth-mcpyml
modified: '2026-07-24'
name: 1upHealth
nav: Providers
network: true
overview: '1upHealth publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, FHIR, HL7, and Interoperability.


  The 1upHealth catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  1upHealth''s developer surface includes documentation, engineering blog, support, signup flow, API reference, getting-started guide, authentication, and 26 more developer resources.'
random_paper: 17
scopes:
- name: 1Uphealth Scopes
  scope_count: 1
  slug: 1uphealth-scopes
  summary_line: 1 scope · clientCredentials/authorizationCode
score:
  band: strong
  composite: 58.2
  delta: 3.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 55.0
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 55.3
  previous_composite: 54.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 76.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/1uphealth/refs/heads/main/screenshots/1uphealth-2026-07-25T181115.png
security:
- kind: authentication
  name: 1Uphealth Authentication
  slug: 1uphealth-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: 1Uphealth Domain Security
  slug: 1uphealth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: 1Uphealth Trust Center
  slug: 1uphealth-trust-center
  summary_line: SOC 2, HIPAA, CSA STAR
slug: 1uphealth
tags:
- Healthcare
- United States
- FHIR
- HL7
- Interoperability
- SMART on FHIR
- Payer
- Claims
- Patient Access
- Health Data
website: https://1up.health/
---
