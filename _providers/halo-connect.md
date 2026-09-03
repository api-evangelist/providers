---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Halo Connect Agentic Access
  operation_count: 29
  slug: halo-connect-agentic-access
  summary_line: 29 operations · 14 acting
api_count: 2
apis:
- baseURL: https://api.haloconnect.io
  baseurl_source: declared
  description: Query practice data using FHIR resources.
  name: Halo Connect FHIR API
  slug: halo-connect-fhir-api
- baseURL: https://api.haloconnect.io
  baseurl_source: declared
  description: The Registered Queries API from Halo Connect — 6 operation(s) for registered queries.
  name: Halo Connect Registered Queries API
  slug: halo-connect-registered-queries-api
- baseURL: https://api.haloconnect.io
  baseurl_source: declared
  description: Endpoints for practice onboarding and site metadata.
  name: Halo Connect Sites API
  slug: halo-connect-sites-api
- baseURL: https://api.haloconnect.io
  baseurl_source: declared
  description: Send SQL queries to practices as immediate, async or registered queries. **Immediate queries** are small, time-sensitive queries that return a result in seconds. Response size is limited to 8MB. **Asy
  name: Halo Connect SQL Passthrough API
  slug: halo-connect-sql-passthrough-api
- baseURL: https://api.haloconnect.io
  baseurl_source: declared
  description: Obtain authorization tokens for desktop applications to authenticate API requests.
  name: Halo Connect Tokens API
  slug: halo-connect-tokens-api
artifact_total: 14
asyncapis:
- description: Halo Cloud delivers HTTPS POST webhook notifications when an async or a registered query completes. The payload does NOT include the query result; the integrator retrieves results via the REST API usi
  name: Halo Connect Webhooks
  slug: halo-connect-webhooks-asyncapi
collections:
- collection_type: open
  name: Halo Cloud API for Desktop Applications
  slug: open-halo-connect-desktop
- collection_type: open
  name: Halo Cloud API for Integrators
  slug: open-halo-connect-integrator
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/halo-connect-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/halo-connect-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/halo-connect-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/halo-connect-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://haloconnect.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.haloconnect.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.haloconnect.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.haloconnect.io/api-reference/integrator-openapi.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.haloconnect.io/halo-cloud/getting-started/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.haloconnect.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://haloconnect.io/trust
- group: company
  title: ''
  type: Blog
  url: https://haloconnect.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/halo-connect-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/halo-connect-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://haloconnect.io/sla
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/halo-connect-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/halo-connect-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/halo-connect-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/halo-connect-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://haloconnect.io/trust
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/halo-connect-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/halo-connect-webhooks-asyncapi.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/halo-connect-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.haloconnect.io/security/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/halo-connect-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/halo-connect-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/halo-connect-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/halo-connect-integrator-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/halo-connect-desktop-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/halo-connect-well-known.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://haloconnect.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://haloconnect.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://haloconnect.io/contact-us
created: '2026-07-24'
description: Halo Connect is an Australian healthcare interoperability platform, founded in 2021 and headquartered in Brisbane, Queensland, that makes primary-care data integration simple by exposing on-premise practice management system (PMS) databases through a modern cloud API. Its Halo Link agent and Halo Cloud service let approved software integrators query systems such as Best Practice, Zedmed, and Dental4Windows using either SQL passthrough or a standards-based FHIR R4 (4.0.1) API built toward the AU Base 4.1.0 implementation guide, without maintaining a separate database agent per integration. Halo Connect built the first FHIR API for the Best Practice Premier medical-practice industry. The platform runs on Microsoft Azure hosted in Australia, and access is gated behind a Halo Cloud subscription using Azure API Management subscription keys and, for desktop applications, bearer JWT tokens issued from a token endpoint; there is no self-serve public API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Halo Connect MCP Server
  slug: halo-connect-mcp-server
modified: '2026-07-24'
name: Halo Connect
nav: Providers
network: true
overview: 'Halo Connect publishes 5 APIs on the [APIs.io](https://apis.io/) network, including FHIR API, Registered Queries API, Sites API, and 2 more. Tagged areas include Healthcare, Australia, FHIR, HL7, and Interoperability.


  The Halo Connect catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Halo Connect''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, changelog, sandbox, and 27 more developer resources.'
random_paper: 14
score:
  band: strong
  composite: 56.7
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 63.9
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 56.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 51.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/halo-connect/refs/heads/main/screenshots/halo-connect-2026-07-25T220547.png
security:
- kind: authentication
  name: Halo Connect Authentication
  slug: halo-connect-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Halo Connect Domain Security
  slug: halo-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Halo Connect Vulnerability Disclosure
  slug: halo-connect-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Halo Connect Trust Center
  slug: halo-connect-trust-center
  summary_line: CyberCert SMB1001-2023 Level 3 (Gold), ISO 27001 (policies/procedures align to principles; not stated as certified)
slug: halo-connect
tags:
- Healthcare
- Australia
- FHIR
- HL7
- Interoperability
- EHR
- Practice Management
- Primary Care
- AU Base
- Health Data
website: https://haloconnect.io/
---
