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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 72.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 43
  human_in_the_loop: 6
  name: Natural Ai Agentic Access
  operation_count: 76
  slug: natural-ai-agentic-access
  summary_line: 76 operations · 43 acting · 6 human-in-the-loop
api_count: 15
apis:
- description: Agent key management
  name: Natural AI Agent Keys API
  slug: natural-ai-agent-keys-api
- description: Agent management
  name: Natural AI Agents API
  slug: natural-ai-agents-api
- description: API key management
  name: Natural AI API Keys API
  slug: natural-ai-api-keys-api
- description: Approval review
  name: Natural AI Approvals API
  slug: natural-ai-approvals-api
- description: Customer management
  name: Natural AI Customers API
  slug: natural-ai-customers-api
- description: Webhook event log
  name: Natural AI Events API
  slug: natural-ai-events-api
- description: Linked external bank accounts
  name: Natural AI External Accounts API
  slug: natural-ai-external-accounts-api
- description: Party invitation management
  name: Natural AI Invitations API
  slug: natural-ai-invitations-api
- description: Party and organization management
  name: Natural AI Parties API
  slug: natural-ai-parties-api
- description: Payment request management
  name: Natural AI PaymentRequests API
  slug: natural-ai-paymentrequests-api
- description: Payment management
  name: Natural AI Payments API
  slug: natural-ai-payments-api
- description: Transaction activity and history
  name: Natural AI Transactions API
  slug: natural-ai-transactions-api
- description: Deposits and withdrawals
  name: Natural AI Transfers API
  slug: natural-ai-transfers-api
- description: Wallet management
  name: Natural AI Wallets API
  slug: natural-ai-wallets-api
- description: Webhook endpoint management
  name: Natural AI Webhooks API
  slug: natural-ai-webhooks-api
artifact_total: 37
asyncapis:
- description: ''
  name: Natural Ai Webhooks
  slug: natural-ai-webhooks
collections:
- collection_type: postman
  name: Natural Agent Keys API
  slug: postman-natural-ai-agent-keys-api
- collection_type: postman
  name: Natural Agent Keys Agents API
  slug: postman-natural-ai-agents-api
- collection_type: postman
  name: Natural Agent Keys API Keys API
  slug: postman-natural-ai-api-keys-api
- collection_type: postman
  name: Natural Agent Keys Approvals API
  slug: postman-natural-ai-approvals-api
- collection_type: postman
  name: Natural Agent Keys Customers API
  slug: postman-natural-ai-customers-api
- collection_type: postman
  name: Natural Agent Keys Events API
  slug: postman-natural-ai-events-api
- collection_type: postman
  name: Natural Agent Keys External Accounts API
  slug: postman-natural-ai-external-accounts-api
- collection_type: postman
  name: Natural Agent Keys Invitations API
  slug: postman-natural-ai-invitations-api
- collection_type: postman
  name: Natural Agent Keys Parties API
  slug: postman-natural-ai-parties-api
- collection_type: postman
  name: Natural Agent Keys PaymentRequests API
  slug: postman-natural-ai-paymentrequests-api
- collection_type: postman
  name: Natural Agent Keys Payments API
  slug: postman-natural-ai-payments-api
- collection_type: postman
  name: Natural Agent Keys Transactions API
  slug: postman-natural-ai-transactions-api
- collection_type: postman
  name: Natural Agent Keys Transfers API
  slug: postman-natural-ai-transfers-api
- collection_type: postman
  name: Natural Agent Keys Wallets API
  slug: postman-natural-ai-wallets-api
- collection_type: postman
  name: Natural Agent Keys Webhooks API
  slug: postman-natural-ai-webhooks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/natural-ai/overview
- group: company
  title: ''
  type: Website
  url: https://www.natural.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.natural.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.natural.com/guides/overview/start-here
- group: docs
  title: ''
  type: APIReference
  url: https://docs.natural.com/api-reference/about
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.natural.com/guides/overview/start-here
- group: start
  title: ''
  type: SignUp
  url: https://natural.com/signup
- group: start
  title: ''
  type: Login
  url: https://natural.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/naturalpay
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/natural-ai-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/natural-ai-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/natural-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/natural-ai-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/natural-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/natural-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/natural-ai-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/natural-ai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/natural-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/natural-ai-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/natural-ai-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/natural-ai-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/natural-ai-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/natural-ai-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/natural-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/natural-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.natural.com/guides/overview/security
- group: design
  title: ''
  type: DataModel
  url: data-model/natural-ai-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/natural-ai-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/natural-ai-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/natural-ai-agentic-access.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/natural-ai-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.natural.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.natural.com/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://natural.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.natural.com/nsa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.natural.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.natural.com/blog
created: '2026-07-17'
description: 'Natural (natural.com) is the agentic payments platform: one API for AI agents, apps, and businesses to send, receive, and manage money. Agents get FDIC-insured wallets, credit lines, and the ability to pay or request funds by email, phone, @handle, party, or agent ID, plus card issuing, merchant acceptance, and PCI-compliant voice payments. The REST API (api.natural.com, Bearer auth, JSON:API envelope) is complemented by first-party Python and TypeScript SDKs, a `natural` CLI, and a hosted Model Context Protocol server at mcp.natural.com exposing 24 intent-shaped tools with OAuth 2.1 + PKCE. Natural was surfaced as a portfolio company of Forerunner Ventures and enriched into the API Evangelist network.'
image: https://www.natural.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: natural-ai-mcp.yml
  slug: natural-ai-mcpyml
modified: '2026-07-20'
name: Natural AI
nav: Providers
network: true
overview: 'Natural AI publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Agent Keys API, Agents API, API Keys API, and 12 more. Tagged areas include Company, Ai, Payments, Agents, and Fintech.


  The Natural AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Natural AI''s developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, CLI, changelog, and 31 more developer resources.'
random_paper: 22
rate_limits:
- limit_count: 0
  name: Natural Ai Rate Limits
  slug: natural-ai-rate-limits
scopes:
- name: Natural Ai Scopes
  scope_count: 0
  slug: natural-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.7
  delta: 0.7
  facets:
    commercial_clarity: 52.6
    contract_quality: 66.1
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 63.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 75.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Natural Ai Authentication
  slug: natural-ai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Natural Ai Domain Security
  slug: natural-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: natural-ai
tags:
- Company
- Ai
- Payments
- Agents
- Fintech
- Money Movement
- Wallets
- Agentic Payments
- MCP
website: https://www.natural.com
---
