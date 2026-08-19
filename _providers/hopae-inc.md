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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 24
  human_in_the_loop: 21
  name: Hopae Inc Agentic Access
  operation_count: 42
  slug: hopae-inc-agentic-access
  summary_line: 42 operations · 24 acting · 21 human-in-the-loop
api_count: 9
apis:
- description: Workspace API key management (Console)
  name: Hopae, Inc. Console - API Keys API
  slug: hopae-inc-console-api-keys-api
- description: eID provider discovery
  name: Hopae, Inc. Providers API
  slug: hopae-inc-providers-api
- description: OAuth 2.0 token exchange
  name: Hopae, Inc. Token API
  slug: hopae-inc-token-api
- description: Identity verification sessions
  name: Hopae, Inc. Verifications API
  slug: hopae-inc-verifications-api
- description: Provider activation per app
  name: Hopae, Inc. Workspace API - Activation API
  slug: hopae-inc-workspace-api-activation-api
- description: App management
  name: Hopae, Inc. Workspace API - Apps API
  slug: hopae-inc-workspace-api-apps-api
- description: Production test challenges
  name: Hopae, Inc. Workspace API - Production Tests API
  slug: hopae-inc-workspace-api-production-tests-api
- description: Workflow configuration per app
  name: Hopae, Inc. Workspace API - Workflows API
  slug: hopae-inc-workspace-api-workflows-api
- description: Workspace information
  name: Hopae, Inc. Workspace API - Workspace API
  slug: hopae-inc-workspace-api-workspace-api
artifact_total: 26
asyncapis:
- description: Outgoing webhook deliveries from Hopae Connect for the identity verification lifecycle. Every delivery is signed with an HMAC-SHA256 signature in the X-Hopae-Signature header (format `t=<unix-ts>,v1=<
  name: Hopae hConnect Webhooks
  slug: hopae-inc-hconnect-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: hConnect Console - API Keys API
  slug: open-hopae-inc-console-api-keys-api
- collection_type: open
  name: hConnect Console - API Keys Providers API
  slug: open-hopae-inc-providers-api
- collection_type: open
  name: hConnect Console - API Keys Token API
  slug: open-hopae-inc-token-api
- collection_type: open
  name: hConnect Console - API Keys Verifications API
  slug: open-hopae-inc-verifications-api
- collection_type: open
  name: hConnect Console - API Keys Workspace API - Activation API
  slug: open-hopae-inc-workspace-api-activation-api
- collection_type: open
  name: hConnect Console - API Keys Workspace API - Apps API
  slug: open-hopae-inc-workspace-api-apps-api
- collection_type: open
  name: hConnect Console - API Keys Workspace API - Production Tests API
  slug: open-hopae-inc-workspace-api-production-tests-api
- collection_type: open
  name: hConnect Console - API Keys Workspace API - Workflows API
  slug: open-hopae-inc-workspace-api-workflows-api
- collection_type: open
  name: hConnect Console - API Keys Workspace API - Workspace API
  slug: open-hopae-inc-workspace-api-workspace-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/hopae-inc-hconnect-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hopae-inc-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hopae-inc-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.hopae.com
- group: auth
  title: ''
  type: Compliance
  url: https://trust.hopae.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/hopae-inc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hopae-inc-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/hopae-inc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hopae-inc-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hopae-inc-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hopae-inc-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hopae-inc-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hopae-inc-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/hopae-inc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hopae-inc-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hopae-inc-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hopae-inc-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hopae-inc-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hopae-inc-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.hopae.com/api-reference/workspace/rate-limit
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/hopae-inc-hconnect-webhooks.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hopae-inc-hconnect-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hopae-inc-changelog.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.hopae.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hopae.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hopae.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hopae.com/guides/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: mailto:dev@hopae.com
- group: company
  title: ''
  type: Blog
  url: https://www.hopae.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hopae-official
- group: start
  title: ''
  type: SignUp
  url: https://console.hopae.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hopae.com/legal/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://hopae.com
created: '2026-07-17'
description: Hopae, Inc. (Hopae S.A.) is a digital identity infrastructure company that connects verification providers, regulated businesses, and trust service providers to 65+ government-backed electronic IDs (eIDs) worldwide through a single, compliant API. Its flagship product, hConnect, is a unified global eID verification hub exposing an OIDC OpenID Provider surface plus a REST API for provider discovery and the verification lifecycle. Hopae also ships an accredited eIDAS 2.0 wallet SDK, authored the widely used SD-JWT / SD-JWT-VC reference implementation (donated to the OpenWallet Foundation), and builds around open standards including eIDAS 2.0, mDL, SD-JWT, and W3C Verifiable Credentials. The platform is developer-first with sandbox and production environments, HMAC-signed webhooks, and a published SOC 2 / ISO 27001 / GDPR compliance posture.
image: https://framerusercontent.com/assets/JDrpQK9QXlyYCuykjUrR228U2M.svg
layout: provider
mcp_servers:
- description: ''
  name: hopae-inc-mcp.yml
  slug: hopae-inc-mcpyml
modified: '2026-07-19'
name: Hopae, Inc.
nav: Providers
network: true
overview: 'Hopae, Inc. publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Console - API Keys API, Providers API, Token API, and 6 more. Tagged areas include Company, Identity, Identity Verification, Digital Identity, and eID.


  The Hopae, Inc. catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hopae, Inc.''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, support, and 27 more developer resources.'
random_paper: 139
scopes:
- name: Hopae Inc Scopes
  scope_count: 7
  slug: hopae-inc-scopes
  summary_line: 7 scopes
score:
  band: developing
  composite: 50.3
  delta: -3.4
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 30.3
    contract_quality: 68.2
    developer_ergonomics: 63.7
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 26.3
  previous_composite: 53.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hopae-inc/refs/heads/main/screenshots/hopae-inc-2026-07-25T221528.png
security:
- kind: authentication
  name: Hopae Inc Authentication
  slug: hopae-inc-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Hopae Inc Domain Security
  slug: hopae-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Hopae Inc Trust Center
  slug: hopae-inc-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, eIDAS 2.0
slug: hopae-inc
tags:
- Company
- Identity
- Identity Verification
- Digital Identity
- eID
- Verifiable Credentials
- Authentication
- OpenID Connect
- eIDAS
- KYC
website: https://hopae.com
---
