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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Sadq Holding Limited Agentic Access
  operation_count: 65
  slug: sadq-holding-limited-agentic-access
  summary_line: 65 operations · 43 acting
api_count: 1
apis:
- baseURL: https://api.sadq.sa
  baseurl_source: declared
  description: File archiving categories and delegation management
  name: Sadq Holding Limited Archiving & Delegations API
  slug: sadq-holding-limited-archiving-delegations-api
- baseURL: https://api.sadq.sa
  baseurl_source: declared
  description: Obtain and manage API access tokens
  name: Sadq Holding Limited Authentication API
  slug: sadq-holding-limited-authentication-api
- baseURL: https://api.sadq.sa
  baseurl_source: declared
  description: Update tenant SMS provider and system configuration
  name: Sadq Holding Limited Configuration API
  slug: sadq-holding-limited-configuration-api
- baseURL: https://api.sadq.sa
  baseurl_source: declared
  description: Download and manage signed document files
  name: Sadq Holding Limited Documents API
  slug: sadq-holding-limited-documents-api
- baseURL: https://api.sadq.sa
  baseurl_source: declared
  description: Initiate and manage signing envelopes and document packages
  name: Sadq Holding Limited Envelopes API
  slug: sadq-holding-limited-envelopes-api
- baseURL: https://api.sadq.sa
  baseurl_source: declared
  description: Electronic and digital signature operations via Nafath/PKI
  name: Sadq Holding Limited eSign API
  slug: sadq-holding-limited-esign-api
- baseURL: https://api.sadq.sa
  baseurl_source: declared
  description: Send, extend, and remind signing invitations
  name: Sadq Holding Limited Invitations API
  slug: sadq-holding-limited-invitations-api
- baseURL: https://api.sadq.sa
  baseurl_source: declared
  description: Know Your Business — CR checks, Absher OTP, delegacy lookups
  name: Sadq Holding Limited KYB API
  slug: sadq-holding-limited-kyb-api
- baseURL: https://api.sadq.sa
  baseurl_source: declared
  description: Consumption reports, request listings and bulk signature jobs
  name: Sadq Holding Limited Reports & Requests API
  slug: sadq-holding-limited-reports-requests-api
- baseURL: https://api.sadq.sa
  baseurl_source: declared
  description: Direct signing operations including multi-file and templates
  name: Sadq Holding Limited Sign API
  slug: sadq-holding-limited-sign-api
- baseURL: https://api.sadq.sa
  baseurl_source: declared
  description: List and retrieve reusable signing templates
  name: Sadq Holding Limited Templates API
  slug: sadq-holding-limited-templates-api
- baseURL: https://api.sadq.sa
  baseurl_source: declared
  description: User management, permissions and signature uploads
  name: Sadq Holding Limited Users API
  slug: sadq-holding-limited-users-api
- baseURL: https://api.sadq.sa
  baseurl_source: declared
  description: Configure and manage webhook subscriptions and logs
  name: Sadq Holding Limited Webhooks API
  slug: sadq-holding-limited-webhooks-api
- baseURL: https://api.sadq.sa
  baseurl_source: declared
  description: Create and manage document signing workflows
  name: Sadq Holding Limited Workflows API
  slug: sadq-holding-limited-workflows-api
artifact_total: 35
asyncapis:
- description: ''
  name: Sadq Holding Limited Webhooks
  slug: sadq-holding-limited-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sadq Integration Archiving & Delegations API
  slug: open-sadq-holding-limited-archiving-delegations-api
- collection_type: open
  name: Sadq Integration Archiving & Delegations Authentication API
  slug: open-sadq-holding-limited-authentication-api
- collection_type: open
  name: Sadq Integration Archiving & Delegations Configuration API
  slug: open-sadq-holding-limited-configuration-api
- collection_type: open
  name: Sadq Integration Archiving & Delegations Documents API
  slug: open-sadq-holding-limited-documents-api
- collection_type: open
  name: Sadq Integration Archiving & Delegations Envelopes API
  slug: open-sadq-holding-limited-envelopes-api
- collection_type: open
  name: Sadq Integration Archiving & Delegations eSign API
  slug: open-sadq-holding-limited-esign-api
- collection_type: open
  name: Sadq Integration Archiving & Delegations Invitations API
  slug: open-sadq-holding-limited-invitations-api
- collection_type: open
  name: Sadq Integration Archiving & Delegations KYB API
  slug: open-sadq-holding-limited-kyb-api
- collection_type: open
  name: Sadq Integration Archiving & Delegations Reports & Requests API
  slug: open-sadq-holding-limited-reports-requests-api
- collection_type: open
  name: Sadq Integration Archiving & Delegations Sign API
  slug: open-sadq-holding-limited-sign-api
- collection_type: open
  name: Sadq Integration Archiving & Delegations Templates API
  slug: open-sadq-holding-limited-templates-api
- collection_type: open
  name: Sadq Integration Archiving & Delegations Users API
  slug: open-sadq-holding-limited-users-api
- collection_type: open
  name: Sadq Integration Archiving & Delegations Webhooks API
  slug: open-sadq-holding-limited-webhooks-api
- collection_type: open
  name: Sadq Integration Archiving & Delegations Workflows API
  slug: open-sadq-holding-limited-workflows-api
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
  url: openapi/_original/sadq-holding-limited-openapi-original.json
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
- description: MCP server exposing the Sadq e-signature platform API. Supports creating envelopes, managing signatories, sending documents for signature, querying webhook logs, and more.
  name: Sadq Holding Limited MCP Server
  slug: sadq-holding-limited-mcp-server
modified: '2026-07-21'
name: Sadq Holding Limited
nav: Providers
network: true
overview: 'Sadq Holding Limited publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Archiving & Delegations API, Authentication API, Configuration API, and 11 more. Tagged areas include Company, E-Signature, Digital Signature, Identity, and KYB.


  The Sadq Holding Limited catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sadq Holding Limited''s developer surface includes documentation, API reference, quickstart, signup flow, support, authentication, sandbox, and 20 more developer resources.'
random_paper: 5
scopes:
- name: Sadq Holding Limited Scopes
  scope_count: 4
  slug: sadq-holding-limited-scopes
  summary_line: 4 scopes
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 58.3
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 36.5
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sadq-holding-limited/refs/heads/main/screenshots/sadq-holding-limited-2026-08-17T081705.png
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
- Document-Management
- Saudi Arabia
- Nafath
- Webhook
- Agent Ready
website: https://sadq.sa
---
