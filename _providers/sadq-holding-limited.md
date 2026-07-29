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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 58.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Sadq Holding Limited Agentic Access
  operation_count: 65
  slug: sadq-holding-limited-agentic-access
  summary_line: 65 operations · 43 acting
api_count: 14
apis:
- description: File archiving categories and delegation management
  name: Sadq Holding Limited Archiving & Delegations API
  slug: sadq-holding-limited-archiving-delegations-api
- description: Obtain and manage API access tokens
  name: Sadq Holding Limited Authentication API
  slug: sadq-holding-limited-authentication-api
- description: Update tenant SMS provider and system configuration
  name: Sadq Holding Limited Configuration API
  slug: sadq-holding-limited-configuration-api
- description: Download and manage signed document files
  name: Sadq Holding Limited Documents API
  slug: sadq-holding-limited-documents-api
- description: Initiate and manage signing envelopes and document packages
  name: Sadq Holding Limited Envelopes API
  slug: sadq-holding-limited-envelopes-api
- description: Electronic and digital signature operations via Nafath/PKI
  name: Sadq Holding Limited eSign API
  slug: sadq-holding-limited-esign-api
- description: Send, extend, and remind signing invitations
  name: Sadq Holding Limited Invitations API
  slug: sadq-holding-limited-invitations-api
- description: Know Your Business — CR checks, Absher OTP, delegacy lookups
  name: Sadq Holding Limited KYB API
  slug: sadq-holding-limited-kyb-api
- description: Consumption reports, request listings and bulk signature jobs
  name: Sadq Holding Limited Reports & Requests API
  slug: sadq-holding-limited-reports-requests-api
- description: Direct signing operations including multi-file and templates
  name: Sadq Holding Limited Sign API
  slug: sadq-holding-limited-sign-api
- description: List and retrieve reusable signing templates
  name: Sadq Holding Limited Templates API
  slug: sadq-holding-limited-templates-api
- description: User management, permissions and signature uploads
  name: Sadq Holding Limited Users API
  slug: sadq-holding-limited-users-api
- description: Configure and manage webhook subscriptions and logs
  name: Sadq Holding Limited Webhooks API
  slug: sadq-holding-limited-webhooks-api
- description: Create and manage document signing workflows
  name: Sadq Holding Limited Workflows API
  slug: sadq-holding-limited-workflows-api
artifact_total: 20
asyncapis:
- description: ''
  name: Sadq Holding Limited Webhooks
  slug: sadq-holding-limited-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://sadq.sa
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sadq.sa/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sadq.sa/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sadq.sa/api/schema
- group: start
  title: ''
  type: Quickstart
  url: https://docs.sadq.sa/auth.md
- group: start
  title: ''
  type: SignUp
  url: https://sadq.sa/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sadq.sa/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sadq.sa/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@sadq.sa
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/sadq-holding-limited-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sadq-holding-limited-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sadq-holding-limited-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sadq-holding-limited-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/sadq-holding-limited-api-catalog.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/sadq-holding-limited-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sadq-holding-limited-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/sadq-holding-limited-openid-configuration.json
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sadq-holding-limited-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sadq-holding-limited-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sadq-holding-limited-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sadq-holding-limited-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sadq-holding-limited-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sadq-holding-limited-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sadq-holding-limited-openapi-original-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sadq-holding-limited-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sadq-holding-limited-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Sadq (صادق) is a Saudi Arabian electronic-signature and digital-trust platform that lets businesses send, sign, and manage legally binding documents online. Its Integration API covers signing envelopes and document packages, signing invitations (email/SMS/link), direct and template-based signing, PKI/e-signing via Saudi Arabia's Nafath national digital identity, document download, reusable templates, users and permissions, signing workflows, webhooks, KYB business verification (commercial-registration checks, Absher OTP, delegacy and national-address lookups), archiving, delegations, and consumption reporting. The platform is fully agent-native — it publishes an OpenAPI schema, an RFC 9727 API catalog, OAuth 2.0 / OIDC discovery metadata, an llms.txt, an auth.md agent-registration guide, and a hosted MCP server. Sadq is a 500 Global portfolio company.
image: https://sadq.sa/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: sadq-holding-limited-mcp.yml
  slug: sadq-holding-limited-mcpyml
modified: '2026-07-21'
name: Sadq Holding Limited
nav: Providers
network: true
overview: 'Sadq Holding Limited publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Archiving & Delegations API, Authentication API, Configuration API, and 11 more. Tagged areas include Company, E-Signature, Digital Signature, Identity, and KYB.


  The Sadq Holding Limited catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sadq Holding Limited''s developer surface includes documentation, API reference, quickstart, signup flow, support, authentication, sandbox, and 20 more developer resources.'
random_paper: 75
scopes:
- name: Sadq Holding Limited Scopes
  scope_count: 4
  slug: sadq-holding-limited-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 48.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 64.5
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sadq Holding Limited Authentication
  slug: sadq-holding-limited-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Sadq Holding Limited Domain Security
  slug: sadq-holding-limited-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: sadq-holding-limited
tags:
- Company
- E-Signature
- Digital Signature
- Identity
- KYB
- Document Management
- Saudi Arabia
- Nafath
- Webhooks
- Agent Ready
website: https://sadq.sa
---
