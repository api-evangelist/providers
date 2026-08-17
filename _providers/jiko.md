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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: The Customer API is for Jiko customers integrating Jiko directly into their own internal systems. It uses OAuth 2.0 (authorization code and client credentials flows) with Private Key JWT client authen
  name: Jiko Customer API
  slug: jiko-customer-api
- description: The Partner API is for applications that embed Jiko's services and offer Jiko products to their own customers. It authenticates with a bearer token obtained via Login, and requires an x-jiko-idempoten
  name: Jiko Partner API
  slug: jiko-partner-api
artifact_total: 9
asyncapis:
- description: ''
  name: Jiko Webhooks
  slug: jiko-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://jiko.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.jiko.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jiko.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.jiko.io/products/customer-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jiko.io/products/customer-api/guides/oauth/getting-started
- group: company
  title: ''
  type: Blog
  url: https://jiko.com/blog
- group: operate
  title: ''
  type: Support
  url: https://jiko.com
- group: start
  title: ''
  type: SignUp
  url: https://authentication-portal.sandbox-api.jikoservices.com/sign-up
- group: start
  title: ''
  type: Portal
  url: https://business.jiko.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jiko.com/agreements-disclosures
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jiko.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://jiko.com/trust-and-safety
- group: auth
  title: ''
  type: Compliance
  url: https://jiko.com/trust-and-safety
- group: auth
  title: ''
  type: Authentication
  url: authentication/jiko-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jiko-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jiko-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/jiko-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jiko-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/jiko-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/jiko-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jiko-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/jiko-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jiko-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jiko-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jiko-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/jiko-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/jiko-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jiko-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jiko-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Jiko is a fintech infrastructure company that turns idle cash into US Treasury bills held in the customer's own name, combining a nationally chartered bank, a registered broker-dealer, and a real-time settlement network (JikoNet) behind a single API. Its "Jiko as a Service" platform lets partners embed T-bill-backed accounts, virtual and physical debit cards, pockets (paired bank + brokerage accounts), and multi-rail money movement (ACH, wire, SWIFT, cards, and 24/7 on-us JikoNet transfers) into their own applications. Jiko exposes two OAuth 2.0 / HMAC-secured REST APIs — a Customer API for direct integrators and a Partner API for embedding Jiko products on behalf of end customers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jiko.png
layout: provider
mcp_servers:
- description: ''
  name: Jiko MCP Server (candidate)
  slug: jiko-mcp-server-candidate
modified: '2026-07-19'
name: Jiko
nav: Providers
network: true
overview: 'Jiko publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Payments, Treasury, and Embedded Finance.


  The Jiko catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Jiko''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, developer portal, and 23 more developer resources.'
random_paper: 131
rate_limits:
- limit_count: 16
  name: Jiko Rate Limits
  slug: jiko-rate-limits
scopes:
- name: Jiko Scopes
  scope_count: 25
  slug: jiko-scopes
  summary_line: 25 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 54.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 55.3
  previous_composite: 54.2
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jiko/refs/heads/main/screenshots/jiko-2026-07-25T223151.png
security:
- kind: authentication
  name: Jiko Authentication
  slug: jiko-authentication
  summary_line: oauth2/openIdConnect/http · 2 schemes
- kind: domain-security
  name: Jiko Domain Security
  slug: jiko-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Jiko Trust Center
  slug: jiko-trust-center
  summary_line: SOC 2, PCI DSS
slug: jiko
tags:
- Company
- Banking
- Payments
- Treasury
- Embedded Finance
- Fintech
- Cards
- Settlement
- Broker-Dealer
- Banking as a Service
website: https://jiko.com
---
