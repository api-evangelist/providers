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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: REST API for AI-agent identity and payments. Buyer agents create kya, pay, and kya-pay tokens; seller agents introspect and charge tokens and manage seller services; enterprises manage users. Authenti
  name: Skyfire API
  slug: skyfire-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://skyfire.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.skyfire.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skyfire.xyz/docs/developer-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://docs.skyfire.xyz/reference/skyfire-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.skyfire.xyz/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://skyfire.xyz/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.skyfire.xyz
- group: start
  title: ''
  type: Login
  url: https://app.skyfire.xyz
- group: operate
  title: ''
  type: Support
  url: mailto:support@skyfire.xyz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://skyfire.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skyfire.xyz/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skyfire-xyz
- group: auth
  title: ''
  type: Authentication
  url: authentication/skyfire-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/skyfire-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skyfire-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/skyfire-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/skyfire-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/skyfire-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/skyfire-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/skyfire-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/skyfire-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skyfire-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/skyfire-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/skyfire-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/skyfire-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skyfire-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/skyfire-skyfire.md
created: '2026-07-17'
description: Skyfire is the open identity and payments layer for AI agents. It lets AI agents securely create accounts, verify a real-world identity (Know Your Agent, KYA), and autonomously pay for digital services using token-based authentication and stablecoin settlement. Developers use Skyfire to monetize APIs, tools, MCP servers, and content directly to agents. The platform issues three signed, interoperable KYAPay token types — kya (identity), pay (payment), and kya-pay (combined) — that buyer agents present to seller services over a simple REST API and a hosted MCP server. Sellers validate and charge tokens, discover services, and manage seller-service lifecycles, while enterprises manage users and agents through admin APIs. Skyfire is backed by DCVC, Lightspeed Venture Partners, and Trinity Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skyfire.png
layout: provider
mcp_servers:
- description: ''
  name: skyfire-mcp.yml
  slug: skyfire-mcpyml
modified: '2026-07-21'
name: Skyfire
nav: Providers
network: true
overview: 'Skyfire publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Agent Payments, Identity, and Payments.


  Skyfire''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 20 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 34.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 80.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 34.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Skyfire Authentication
  slug: skyfire-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Skyfire Domain Security
  slug: skyfire-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: skyfire
tags:
- Company
- AI Agents
- Agent Payments
- Identity
- Payments
- Authentication
- Stablecoin
- MCP
- Agentic Commerce
- Know Your Agent
website: https://skyfire.xyz
---
