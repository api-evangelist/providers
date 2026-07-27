---
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 75.0
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Halo Connect Agentic Access
  operation_count: 29
  slug: halo-connect-agentic-access
  summary_line: 29 operations · 14 acting
api_count: 3
apis:
- description: The Halo Cloud API for third-party software integrators to query on-premise practice management system databases over the cloud, covering site pairing, SQL passthrough (immediate and async queries), F
  name: Halo Cloud API for Integrators
  slug: halo-cloud-integrator-api
- description: The Halo Cloud API for desktop applications, exposing a token endpoint plus SQL passthrough, FHIR R4 resource search, and registered-query operations under the /desktop path. Authenticated with an Azu
  name: Halo Cloud API for Desktop Applications
  slug: halo-cloud-desktop-api
- description: Halo Connect's FHIR API for accessing primary-care data from on-premise practice management systems, based on FHIR Release 4 (R4) version 4.0.1 and built toward the AU Base 4.1.0 implementation guide.
  name: Halo Cloud FHIR API
  slug: halo-cloud-fhir-api
artifact_total: 10
asyncapis:
- description: Halo Cloud delivers HTTPS POST webhook notifications when an async or a registered query completes. The payload does NOT include the query result; the integrator retrieves results via the REST API usi
  name: Halo Connect Webhooks
  slug: halo-connect-webhooks-asyncapi
common:
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
  name: halo-connect-mcp.yml
  slug: halo-connect-mcpyml
modified: '2026-07-24'
name: Halo Connect
nav: Providers
network: true
overview: 'Halo Connect publishes 3 APIs on the [APIs.io](https://apis.io/) network: Halo Cloud API for Integrators, Halo Cloud API for Desktop Applications, and Halo Cloud FHIR API. Tagged areas include Healthcare, Australia, FHIR, HL7, and Interoperability.


  The Halo Connect catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Halo Connect''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, changelog, sandbox, and 26 more developer resources.'
random_paper: 55
score:
  band: developing
  composite: 58.3
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 60.4
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 58.3
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 78.3
  schema_version: 0.5
  scored_at: '2026-07-27'
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
