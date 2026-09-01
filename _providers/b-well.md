---
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: B Well Agentic Access
  operation_count: 3
  slug: b-well-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 2
apis:
- description: 'Federated GraphQL gateway plus REST endpoints that let end-user applications read and write a person''s health data, manage data-source connections, handle consent, and coordinate care workflows in an '
  name: b.well Application APIs
  slug: application-apis
- description: System-level FHIR R4 API over b.well's normalized clinical data store, built on the open-source Helix FHIR Server. Supports standard FHIR REST search, $everything bulk patient retrieval, International
  name: b.well FHIR Server
  slug: fhir-server
- description: A b.well-hosted Model Context Protocol server that exposes a catalog of healthcare agents/tools — insurance coverage validation, FHIR record and lab retrieval, patient summaries, provider search, appo
  name: b.well Health SDK for AI (MCP Server)
  slug: health-sdk-for-ai-mcp
- description: The Users API from b.well — 2 operation(s) for users.
  name: b.well Users API
  slug: b-well-users-api
- description: The Webhook API from b.well — 1 operation(s) for webhook.
  name: b.well Webhook API
  slug: b-well-webhook-api
artifact_total: 20
asyncapis:
- description: ''
  name: B Well Webhooks
  slug: b-well-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Client Webhook API
  slug: open-b-well-client-webhook-api
- collection_type: open
  name: bwell User Data Operations
  slug: open-b-well-user-data-operations
- collection_type: open
  name: bwell User Data Operations Users API
  slug: open-b-well-users-api
- collection_type: open
  name: Client Webhook API
  slug: open-b-well-webhook-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/b-well-client-webhook-api-overlay.yaml
- group: operate
  title: ''
  type: Releases
  url: https://github.com/icanbwell/fhir-server/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/icanbwell/fhir-server/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/icanbwell/fhir-server/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/b-well-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.icanbwell.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bwell.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bwell.com/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bwell.com/reference/ts-sdk-apireference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.bwell.com/docs/welcome
- group: auth
  title: ''
  type: Authentication
  url: authentication/b-well-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/b-well-scopes.yml
- group: operate
  title: ''
  type: Support
  url: mailto:support@icanbwell.com
- group: company
  title: ''
  type: Blog
  url: https://resources.icanbwell.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/icanbwell
- group: start
  title: ''
  type: Login
  url: https://developer.bwell.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.icanbwell.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.icanbwell.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bwell.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/b-well-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/b-well-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/b-well-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/b-well-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/b-well-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/b-well-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.icanbwell.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/b-well-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/b-well-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/b-well-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/b-well-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/b-well-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/b-well-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/b-well-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/b-well-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/b-well-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/b-well-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/b-well-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/b-well-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/b-well-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/b-well-rate-limits.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/b-well-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/b-well-trust-center.yml
created: '2026-08-06'
description: b.well Connected Health is a Baltimore-based digital health platform that unifies a person's fragmented medical, pharmacy, claims, wearable and lab data into a single FHIR-native longitudinal health record, then exposes that record to partner applications through a developer platform. The company operates a consumer-mediated health data network spanning millions of providers, health plans, HIEs/HINs, TEFCA QHINs and CMS-aligned networks, and licenses it to health systems, payers, employers and retail health brands who embed it in their own apps. Its developer surface is built around four Health SDKs (Web/TypeScript, Android/Kotlin, iOS/Swift and an AI SDK that speaks Model Context Protocol), a federated GraphQL gateway, REST endpoints for user data operations and webhooks, and a FHIR R4 server (the open-source Helix FHIR Server) supporting $everything and International Patient Summary retrieval. Authentication is OAuth 2.0 throughout — token exchange with OIDC for end-user context,
  client credentials for system-to-system access, and HMAC-SHA512 request signing on the user data operations API.
image: https://www.icanbwell.com/wp-content/uploads/2023/01/bwell-logo.png
layout: provider
mcp_servers:
- description: ''
  name: b.well MCP Server
  slug: bwell-mcp-server
modified: '2026-08-15'
name: b.well
nav: Providers
network: true
overview: 'b.well publishes 2 APIs on the [APIs.io](https://apis.io/) network: Users API and Webhook API. Tagged areas include Company, Health, Healthcare, Digital Health, and FHIR.


  The b.well catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  b.well''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, changelog, and 36 more developer resources.'
plans:
- name: B Well Plans Pricing
  plan_count: 0
  slug: b-well-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: B Well Rate Limits
  slug: b-well-rate-limits
scopes:
- name: B Well Scopes
  scope_count: 4
  slug: b-well-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 56.5
  coverage:
    artifact_dirs: 24
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 59.4
    developer_ergonomics: 53.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  open_source:
    applies: true
    score: 50.0
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 75.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 73.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/b-well/refs/heads/main/screenshots/b-well-2026-08-07T162052.png
security:
- kind: authentication
  name: B Well Authentication
  slug: b-well-authentication
  summary_line: oauth2/apiKey · 7 schemes
- kind: domain-security
  name: B Well Domain Security
  slug: b-well-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: B Well Vulnerability Disclosure
  slug: b-well-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: B Well Trust Center
  slug: b-well-trust-center
  summary_line: HITRUST, NIST Cybersecurity Framework (CSF), HIPAA
slug: b-well
tags:
- Company
- Health
- Healthcare
- Digital Health
- FHIR
- Health Data
- Interoperability
- Patient Access
- Health Records
- MCP
website: https://www.icanbwell.com/
---
