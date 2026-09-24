---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-09-24'
api_count: 1
apis:
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Hyperliquid account state and risk management
  name: FarmDash Agent Hub Account API
  slug: farmdash-account-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Policy-bounded loop configuration and execution
  name: FarmDash Agent Hub Autopilot API
  slug: farmdash-autopilot-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Hyperliquid wallet delegation
  name: FarmDash Agent Hub Delegation API
  slug: farmdash-delegation-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Futures order execution and cancellation
  name: FarmDash Agent Hub Execution API
  slug: farmdash-execution-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Fee event history and revenue metrics
  name: FarmDash Agent Hub History API
  slug: farmdash-history-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Trail Heat protocol data and chain analytics
  name: FarmDash Agent Hub Intelligence API
  slug: farmdash-intelligence-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Futures market research — funding rates, technical indicators
  name: FarmDash Agent Hub Research API
  slug: farmdash-research-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Pre-trade risk analysis, alerts, and execution guardrails
  name: FarmDash Agent Hub Risk API
  slug: farmdash-risk-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Bounded session management
  name: FarmDash Agent Hub Session API
  slug: farmdash-session-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Strategy analysis and position sizing
  name: FarmDash Agent Hub Strategy API
  slug: farmdash-strategy-api
- baseURL: https://www.farmdash.one/api
  baseurl_source: declared
  description: Token swap quotes, execution, and confirmation
  name: FarmDash Agent Hub Swap API
  slug: farmdash-swap-api
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://www.farmdash.one/
- group: other
  title: ''
  type: APIsJSON
  url: https://www.farmdash.one/apis.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/mcp/farmdash-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/farmdash-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/overlays/farmdash-agent-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/farmdash-agent-api-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://www.farmdash.one/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.farmdash.one/agents
- group: docs
  title: ''
  type: APIReference
  url: https://www.farmdash.one/agents/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.farmdash.one/agents
- group: commercial
  title: ''
  type: Pricing
  url: https://www.farmdash.one/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.farmdash.one/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.farmdash.one/privacy
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/AR6hVaDj
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.farmdash.one/updates
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/plans/farmdash-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/farmdash-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/rate-limits/farmdash-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/farmdash-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/packages/farmdash-packages.yml
  title: ''
  type: Packages
  url: packages/farmdash-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/well-known/farmdash-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/farmdash-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/conformance/farmdash-conformance.yml
  title: ''
  type: Conformance
  url: conformance/farmdash-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/lifecycle/farmdash-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/farmdash-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/conventions/farmdash-conventions.yml
  title: ''
  type: Conventions
  url: conventions/farmdash-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/errors/farmdash-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/farmdash-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/data-model/farmdash-data-model.yml
  title: ''
  type: DataModel
  url: data-model/farmdash-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/sandbox/farmdash-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/farmdash-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/authentication/farmdash-authentication.yml
  title: ''
  type: Authentication
  url: authentication/farmdash-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/security/farmdash-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/farmdash-domain-security.yml
created: '2026-08-26'
description: 'FarmDash is a zero-custody intelligence and control layer for DeFi agents and airdrop farmers, combining Trail Heat opportunity scoring, Signal Architect swap routing, wallet and Sybil-risk intelligence, and Hyperliquid futures research across EVM, Solana, HyperEVM and StarkNet. It is one of the most thoroughly agent-instrumented providers in the catalog: a live OpenAPI 3.1.0 with 27 operations, an 84-tool MCP manifest carrying full input schemas, an A2A-flavored agent card, an ai-plugin manifest, llms.txt, ai.txt, a machine-readable agent report, and a runtime capability contract that the provider declares authoritative over tool discovery. Auth is tiered API keys (Scout free / Pioneer $39.99 / Syndicate $199, all USDC) with a verified live x402 machine-payment fallback settling on Base. Writes are gated by mandatory pre-execution simulation and user-held EIP-191/EIP-712 signatures — FarmDash never broadcasts and never holds keys.'
image: https://www.farmdash.one/og-wagon-preview.png?v=20260425
layout: provider
mcp_servers:
- description: 'FarmDash MCP server for zero-custody DeFi agent intelligence and control: Trail Heat discovery, wallet intelligence, typed adapter validation, policy checks, simulations, EIP-712 approval queues and x'
  name: FarmDash Agent Hub MCP Server
  slug: farmdash-agent-hub-mcp-server
modified: '2026-08-26'
name: FarmDash Agent Hub
nav: Providers
network: true
overview: 'FarmDash Agent Hub publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Account API, Autopilot API, Delegation API, and 8 more. Tagged areas include DeFi, DeFAI, AI Agents, MCP, and OpenAPI.


  FarmDash Agent Hub''s developer surface includes documentation, API reference, getting-started guide, pricing, support, changelog, sandbox, and 19 more developer resources.'
plans:
- name: Farmdash Plans Pricing
  plan_count: 3
  slug: farmdash-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Farmdash Rate Limits
  slug: farmdash-rate-limits
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 57.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    operational_transparency: 47.4
  previous_composite: 53.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/farmdash/refs/heads/main/screenshots/farmdash-2026-09-02T145504.png
security:
- kind: authentication
  name: Farmdash Authentication
  slug: farmdash-authentication
  summary_line: http/apiKey-literal/wallet-signature/http-payment · 7 schemes
- kind: domain-security
  name: Farmdash Domain Security
  slug: farmdash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: farmdash
tags:
- DeFi
- DeFAI
- AI Agents
- MCP
- OpenAPI
- x402
- Blockchain
- Crypto
- airdrop tracking
- Developer Tools
- Agent Readiness
- Machine Payments
- Hyperliquid
- Wallet Intelligence
- zero custody
- A2A
website: https://www.farmdash.one/
---
