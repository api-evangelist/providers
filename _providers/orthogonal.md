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
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.6
  scored_at: '2026-08-19'
api_count: 4
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
- description: The resold catalog itself — 795 payable operations across 58 third-party provider families (scraping, enrichment, search, jobs, weather, agent infrastructure), each namespaced /{provider-slug}/{upstre
  name: Orthogonal API Marketplace
  slug: orthogonal-marketplace-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Orthogonal Account API
  slug: open-orthogonal-account-api
- collection_type: open
  name: Orthogonal Account Discovery API
  slug: open-orthogonal-discovery-api
- collection_type: open
  name: Orthogonal Account Run API
  slug: open-orthogonal-run-api
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
  url: openapi/_original/orthogonal-openapi.yaml
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
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/orthogonal-marketplace-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/orthogonal-marketplace-overlay.yaml
- group: other
  title: ''
  type: AgentCard
  url: a2a/orthogonal-a2a.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/orthogonal-tool-crosswalk.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/orthogonal-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/orthogonal-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/orthogonal-finops.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.orthogonal.com/
- group: company
  title: ''
  type: Blog
  url: https://www.orthogonal.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.orthogonal.com/
created: '2026-07-17'
description: Orthogonal is a unified API and payment layer for AI agents, backed by Pantera Capital and Y Combinator. An agent describes what it needs in natural language and Orthogonal returns the right service from a catalog of 40+ third-party APIs (web search, data enrichment, scraping, email finding/verification, identity), then proxies the call and meters a per-call price. Access is available through a REST API (api.orthogonal.com), a TypeScript SDK (@orth/sdk), a Python SDK (orth), a CLI (@orth/cli), and an official hosted MCP server (mcp.orthogonal.com) for Claude, Cursor, and other agents. Billing is prepaid credits or pay-per-call stablecoin micropayments over x402 (USDC on Base) and MPP (USDC.e on Tempo). Orthogonal also publishes an open library of 88 installable Agent Skills.
finops:
- name: Orthogonal Finops
  service_category: ''
  slug: orthogonal-finops
image: https://orthogonal.sh/logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: orthogonal-mcp.yml
  slug: orthogonal-mcpyml
modified: '2026-08-14'
name: Orthogonal
nav: Providers
network: true
overview: 'Orthogonal publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Discovery API, Run API, and 1 more. Tagged areas include Company, AI Agents, API Discovery, API Marketplace, and Agent Payments.


  Orthogonal''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, CLI, authentication, and 32 more developer resources.'
plans:
- name: Orthogonal Plans Pricing
  plan_count: 2
  slug: orthogonal-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Orthogonal Rate Limits
  slug: orthogonal-rate-limits
scopes:
- name: Orthogonal Scopes
  scope_count: 0
  slug: orthogonal-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.0
  delta: 0.1
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 16.7
    contract_quality: 13.6
    developer_ergonomics: 81.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 13.2
  previous_composite: 50.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 64.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orthogonal/refs/heads/main/screenshots/orthogonal-2026-08-07T190954.png
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
  summary_line: Hackerone · security.txt · contact published
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
