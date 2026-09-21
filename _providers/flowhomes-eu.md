---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Flowhomes Eu Agentic Access
  operation_count: 34
  slug: flowhomes-eu-agentic-access
  summary_line: 34 operations · 14 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.flowhomes.eu
  baseurl_source: declared
  description: The x402 pay-per-call REST surface, published as OpenAPI 3.1.0 "Qorevia Market Intelligence" 2.0.0 at https://api.flowhomes.eu/openapi.json (servers https://api.flowhomes.eu; 34 paths). Thirteen price
  name: Qorevia Market Intelligence API
  slug: qorevia-market-intelligence-api
- description: 'The free discovery and routing layer in front of the paid tools, served from the same origin. MCP: https://api.flowhomes.eu/mcp is POST-only Streamable HTTP (GET 404), answers initialize with protocol'
  name: Qorevia Universal Agent Gateway (MCP + A2A)
  slug: qorevia-universal-agent-gateway
artifact_total: 9
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/agentic-access/flowhomes-eu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flowhomes-eu-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/security/flowhomes-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flowhomes-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.flowhomes.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://api.flowhomes.eu/skill.md
- group: docs
  title: ''
  type: APIReference
  url: https://api.flowhomes.eu/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.flowhomes.eu/api/try
- group: commercial
  title: ''
  type: Pricing
  url: https://api.flowhomes.eu/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/llms/flowhomes-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flowhomes-eu-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://api.flowhomes.eu/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/well-known/flowhomes-eu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flowhomes-eu-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/a2a/flowhomes-eu-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/flowhomes-eu-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/mcp/flowhomes-eu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/flowhomes-eu-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/mcp/flowhomes-eu-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/flowhomes-eu-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://api.flowhomes.eu/skill.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/authentication/flowhomes-eu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flowhomes-eu-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/conventions/flowhomes-eu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/flowhomes-eu-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/errors/flowhomes-eu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/flowhomes-eu-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/lifecycle/flowhomes-eu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/flowhomes-eu-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/changelog/flowhomes-eu-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/flowhomes-eu-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/conformance/flowhomes-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flowhomes-eu-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/plans/flowhomes-eu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flowhomes-eu-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/rate-limits/flowhomes-eu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/flowhomes-eu-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/packages/flowhomes-eu-packages.yml
  title: ''
  type: Packages
  url: packages/flowhomes-eu-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/data-model/flowhomes-eu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flowhomes-eu-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/regulatory/flowhomes-eu-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/flowhomes-eu-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/flowhomes-eu/refs/heads/main/well-known/flowhomes-eu-x402.json
  title: ''
  type: X-X402Discovery
  url: well-known/flowhomes-eu-x402.json
created: '2026-09-19'
description: 'Qorevia ("Qorevia Market Intelligence", operated from api.flowhomes.eu) is an agent-native, pay-per-call API seller: thirteen deterministic market-intelligence, data-profiling and developer utility tools — live XAUUSD (gold) quote, OHLCV bars and computed market state read from a read-only MetaTrader 5 terminal, trading-session state in Europe/Vienna time, stop/target risk levels, a strategy robustness grade, tick PnL, OHLCV state, CSV and JSON structural profiling, JWT decode, EVM address syntax and regex testing — each priced between $0.0025 and $0.05 and settled per call in USDC on Base Mainnet (eip155:8453) through the x402 v2 protocol (HTTP 402 -> pay -> retry with PAYMENT-SIGNATURE), with no accounts and no API keys. Discovery is free and unusually complete: an OpenAPI 3.1.0 contract at /openapi.json, an x402 manifest at /.well-known/x402, a remote MCP server at /mcp (four free finder/router/catalog tools, listed in the Official MCP Registry), an A2A 1.0 agent card at
  /.well-known/agent-card.json backed by a live JSON-RPC endpoint at /a2a, a skill.md, an llms.txt, a natural-language finder (/api/find) and a "Founders Network" whose tiers derive from verified x402 payment history. The registrable domain flowhomes.eu does not serve a website (TLS handshake fails; HTTP returns Cloudflare error 1001), so every surface lives on api.flowhomes.eu.'
layout: provider
mcp_servers:
- description: ''
  name: Qorevia MCP Server
  slug: qorevia-mcp-server
- description: ''
  name: Qorevia MCP endpoint (Streamable HTTP, POST-only)
  slug: qorevia-mcp-endpoint-streamable-http-post-only
modified: '2026-09-19'
name: Qorevia
nav: Providers
network: true
overview: 'Qorevia publishes 1 API on the [APIs.io](https://apis.io/) network: Market Intelligence API. Tagged areas include Market Data, Gold, XAUUSD, Trading, and Finance.


  Qorevia''s developer surface includes documentation, API reference, getting-started guide, pricing, authentication, changelog, and 21 more developer resources.'
plans:
- name: Flowhomes Eu Plans Pricing
  plan_count: 2
  slug: flowhomes-eu-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Flowhomes Eu Rate Limits
  slug: flowhomes-eu-rate-limits
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 33.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 35.1
    developer_ergonomics: 47.6
    discoverability: 72.2
    operational_transparency: 15.8
  previous_composite: 2.8
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Flowhomes Eu Authentication
  slug: flowhomes-eu-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Flowhomes Eu Domain Security
  slug: flowhomes-eu-domain-security
  summary_line: TLSv1.3
slug: flowhomes-eu
tags:
- Market Data
- Gold
- XAUUSD
- Trading
- Finance
- Quantitative Research
- Risk Management
- Data Profiling
- Developer Tools
- x402
- USDC
- Base L2
- Agentic Commerce
- pay-per-call
- MCP
- A2A
- Agents
- agent-native
website: https://api.flowhomes.eu/
---
