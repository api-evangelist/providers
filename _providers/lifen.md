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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: The CommunicationRequest API from Lifen — 3 operation(s) for communicationrequest.
  name: Lifen CommunicationRequest API
  slug: lifen-communicationrequest-api
- description: The Coverage API from Lifen — 1 operation(s) for coverage.
  name: Lifen Coverage API
  slug: lifen-coverage-api
- description: The Encounter API from Lifen — 2 operation(s) for encounter.
  name: Lifen Encounter API
  slug: lifen-encounter-api
- description: The Organization API from Lifen — 1 operation(s) for organization.
  name: Lifen Organization API
  slug: lifen-organization-api
- description: The Patient API from Lifen — 2 operation(s) for patient.
  name: Lifen Patient API
  slug: lifen-patient-api
- description: The Practitioner API from Lifen — 1 operation(s) for practitioner.
  name: Lifen Practitioner API
  slug: lifen-practitioner-api
- description: The Token API from Lifen — 1 operation(s) for token.
  name: Lifen Token API
  slug: lifen-token-api
artifact_total: 20
asyncapis:
- description: ''
  name: Lifen Platform Webhooks
  slug: lifen-platform-webhooks
collections:
- collection_type: postman
  name: lifen-authentication-api CommunicationRequest API
  slug: postman-lifen-communicationrequest-api
- collection_type: postman
  name: lifen-authentication-api CommunicationRequest Coverage API
  slug: postman-lifen-coverage-api
- collection_type: postman
  name: lifen-authentication-api CommunicationRequest Encounter API
  slug: postman-lifen-encounter-api
- collection_type: postman
  name: lifen-authentication-api CommunicationRequest Organization API
  slug: postman-lifen-organization-api
- collection_type: postman
  name: lifen-authentication-api CommunicationRequest Patient API
  slug: postman-lifen-patient-api
- collection_type: postman
  name: lifen-authentication-api CommunicationRequest Practitioner API
  slug: postman-lifen-practitioner-api
- collection_type: postman
  name: lifen-authentication-api CommunicationRequest Token API
  slug: postman-lifen-token-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/lifen/overview
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lifen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lifen.fr/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lifen.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lifen.fr/docs/platform-services-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://developer.lifen.fr/reference/patient
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.lifen.fr/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.lifen.fr/contact
- group: company
  title: ''
  type: Blog
  url: https://www.lifen.fr/ressources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/honestica
- group: start
  title: ''
  type: SignUp
  url: https://www.lifen.fr/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.lifen.fr/log-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lifen.fr/cgu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lifen.fr/donnees-personnelles
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.lifen.fr/mentions-legales
- group: build
  title: ''
  type: Postman
  url: https://developer.lifen.fr/docs/quickstart
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lifen.fr/793930656
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.lifen.fr/changelog
- group: auth
  title: ''
  type: Compliance
  url: https://www.lifen.fr/nos-expertises/securite-des-donnees-de-sante
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lifen-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lifen-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lifen-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lifen-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lifen-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lifen-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lifen-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lifen-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lifen-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lifen-platform-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lifen-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lifen-fhir-api-overlay.yaml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lifen-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lifen-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lifen-rate-limits.yml
created: '2026-07-17'
description: 'Lifen (Honestica SAS, Paris) is a French digital-health company whose Lifen Platform exposes FHIR R4 APIs that let e-health applications exchange health data with French hospital information systems and with healthcare professionals over the national MSSanté secure-messaging network. The platform is organised as API Services: Hospital API Services (an Identity & Encounter service giving secure access to patient administrative, coverage, encounter and appointment data inside a given hospital, and a Send-documents-to-EHR service that pushes medical documents into hospital Electronic Health Records), and National API Services (the MSS service for sending medical documents to healthcare professionals via MSSanté). Access is machine-to-machine over OAuth 2.0 client credentials, scoped by functional scopes and bound to a healthcare organisation through a database_reference. Lifen also ships an SSO/OIDC API and a signed webhook surface for patient and encounter events. The company
  is ISO 27001 certified and an HDS (Hebergeur de Donnees de Sante) certified health-data host.'
image: https://files.readme.io/ea56e58-small-Logo_couleur.png
layout: provider
mcp_servers:
- description: ''
  name: lifen-mcp.yml
  slug: lifen-mcpyml
modified: '2026-07-19'
name: Lifen
nav: Providers
network: true
overview: 'Lifen publishes 7 APIs on the [APIs.io](https://apis.io/) network, including CommunicationRequest API, Coverage API, Encounter API, and 4 more. Tagged areas include Company, Healthcare, FHIR, Interoperability, and Health Data.


  The Lifen catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lifen''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 28 more developer resources.'
random_paper: 34
rate_limits:
- limit_count: 0
  name: Lifen Rate Limits
  slug: lifen-rate-limits
scopes:
- name: Lifen Scopes
  scope_count: 0
  slug: lifen-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.9
  delta: -3.4
  facets:
    commercial_clarity: 42.1
    contract_quality: 64.3
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 44.7
  previous_composite: 60.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 65.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/screenshots/lifen-2026-07-25T225040.png
security:
- kind: authentication
  name: Lifen Authentication
  slug: lifen-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Lifen Domain Security
  slug: lifen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lifen
tags:
- Company
- Healthcare
- FHIR
- Interoperability
- Health Data
- Electronic Health Records
- Medical Documents
- Secure Messaging
- France
- HL7
website: https://www.lifen.fr/
---
