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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Credit balance, usage, and transaction history.
  name: Orthogonal Account API
  slug: orthogonal-account-api
- description: Find APIs and endpoints, inspect parameters, and get code snippets.
  name: Orthogonal Discovery API
  slug: orthogonal-discovery-api
- description: Execute a call against any catalog API through Orthogonal.
  name: Orthogonal Run API
  slug: orthogonal-run-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.orthogonal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.orthogonal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.orthogonal.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.orthogonal.com/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://www.orthogonal.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://orthogonal.com/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orthogonal.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orthogonal.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orthogonal-sh
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/orthogonal-openapi.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/orthogonal-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/orthogonal-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/orthogonal-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/orthogonal-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/orthogonal-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orthogonal-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/orthogonal-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orthogonal-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/orthogonal-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/orthogonal-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/orthogonal-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/orthogonal-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/orthogonal-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/orthogonal-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/orthogonal-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orthogonal-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/orthogonal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/orthogonal-vulnerability-disclosure.yml
created: '2026-07-17'
description: Orthogonal is a unified API and payment layer for AI agents, backed by Pantera Capital and Y Combinator. An agent describes what it needs in natural language and Orthogonal returns the right service from a catalog of 40+ third-party APIs (web search, data enrichment, scraping, email finding/verification, identity), then proxies the call and meters a per-call price. Access is available through a REST API (api.orthogonal.com), a TypeScript SDK (@orth/sdk), a Python SDK (orth), a CLI (@orth/cli), and an official hosted MCP server (mcp.orthogonal.com) for Claude, Cursor, and other agents. Billing is prepaid credits or pay-per-call stablecoin micropayments over x402 (USDC on Base) and MPP (USDC.e on Tempo). Orthogonal also publishes an open library of 88 installable Agent Skills.
image: https://orthogonal.sh/logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: orthogonal-mcp.yml
  slug: orthogonal-mcpyml
modified: '2026-07-20'
name: Orthogonal
nav: Providers
network: true
overview: 'Orthogonal publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Discovery API, and Run API. Tagged areas include Company, AI Agents, API Discovery, API Marketplace, and Agent Payments.


  Orthogonal''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, CLI, authentication, and 22 more developer resources.'
random_paper: 19
scopes:
- name: Orthogonal Scopes
  scope_count: 0
  slug: orthogonal-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.0
  delta: -2.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 44.1
    developer_ergonomics: 71.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 49.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Orthogonal Authentication
  slug: orthogonal-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Orthogonal Domain Security
  slug: orthogonal-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Orthogonal Vulnerability Disclosure
  slug: orthogonal-vulnerability-disclosure
  summary_line: disclosure policy published
slug: orthogonal
tags:
- Company
- AI Agents
- API Discovery
- API Marketplace
- Agent Payments
- MCP
- Data Enrichment
- Crypto
- Stablecoins
website: https://www.orthogonal.com/
---
