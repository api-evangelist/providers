---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 23
  human_in_the_loop: 4
  name: Graphadvocate Com Agentic Access
  operation_count: 23
  slug: graphadvocate-com-agentic-access
  summary_line: 23 operations · 23 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: Hosted MCP server at https://graphadvocate.com/mcp (Streamable HTTP for one-shot JSON-RPC initialize and tools/list; SSE session at /mcp/sse). tools/list answers anonymously with three tools — route_d
  name: Graph Advocate MCP Server
  slug: graph-advocate-mcp-server
- baseURL: https://graphadvocate.com/mcp
  baseurl_source: declared
  description: The Agent API from PaulieB14 — 1 operation(s) for agent.
  name: PaulieB14 Agent API
  slug: graphadvocate-com-agent-api
- baseURL: https://graphadvocate.com/mcp
  baseurl_source: declared
  description: The Ask API from PaulieB14 — 1 operation(s) for ask.
  name: PaulieB14 Ask API
  slug: graphadvocate-com-ask-api
- baseURL: https://graphadvocate.com/mcp
  baseurl_source: declared
  description: The Hyperliquid API from PaulieB14 — 6 operation(s) for hyperliquid.
  name: PaulieB14 Hyperliquid API
  slug: graphadvocate-com-hyperliquid-api
- baseURL: https://graphadvocate.com/mcp
  baseurl_source: declared
  description: The Kalshi API from PaulieB14 — 2 operation(s) for kalshi.
  name: PaulieB14 Kalshi API
  slug: graphadvocate-com-kalshi-api
- baseURL: https://graphadvocate.com/mcp
  baseurl_source: declared
  description: The Kalshi Polymarket API from PaulieB14 — 1 operation(s) for kalshi polymarket.
  name: PaulieB14 Kalshi Polymarket API
  slug: graphadvocate-com-kalshi-polymarket-api
- baseURL: https://graphadvocate.com/mcp
  baseurl_source: declared
  description: The Narrative API from PaulieB14 — 1 operation(s) for narrative.
  name: PaulieB14 Narrative API
  slug: graphadvocate-com-narrative-api
- baseURL: https://graphadvocate.com/mcp
  baseurl_source: declared
  description: The Onchain X402 API from PaulieB14 — 1 operation(s) for onchain x402.
  name: PaulieB14 Onchain X402 API
  slug: graphadvocate-com-onchain-x402-api
- baseURL: https://graphadvocate.com/mcp
  baseurl_source: declared
  description: The Polymarket API from PaulieB14 — 5 operation(s) for polymarket.
  name: PaulieB14 Polymarket API
  slug: graphadvocate-com-polymarket-api
- baseURL: https://graphadvocate.com/mcp
  baseurl_source: declared
  description: The Predmarket API from PaulieB14 — 1 operation(s) for predmarket.
  name: PaulieB14 Predmarket API
  slug: graphadvocate-com-predmarket-api
- baseURL: https://graphadvocate.com/mcp
  baseurl_source: declared
  description: The Route API from PaulieB14 — 1 operation(s) for route.
  name: PaulieB14 Route API
  slug: graphadvocate-com-route-api
- baseURL: https://graphadvocate.com/mcp
  baseurl_source: declared
  description: The Uniswap API from PaulieB14 — 3 operation(s) for uniswap.
  name: PaulieB14 Uniswap API
  slug: graphadvocate-com-uniswap-api
artifact_total: 23
common:
- group: company
  title: ''
  type: Website
  url: https://graphadvocate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.graphadvocate.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.graphadvocate.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.graphadvocate.com/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://graphadvocate.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.graphadvocate.com/route
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PaulieB14
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/PaulieB14/graph-advocate
- group: company
  title: ''
  type: Twitter
  url: https://x.com/graphtronauts_c
- group: agent
  href: https://artifacts.apis.io/graphadvocate-com/llms/graphadvocate-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/graphadvocate-com-llms.txt
- group: other
  href: https://artifacts.apis.io/graphadvocate-com/a2a/graphadvocate-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/graphadvocate-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/graphadvocate-com/mcp/graphadvocate-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/graphadvocate-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/graphadvocate-com/mcp/graphadvocate-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/graphadvocate-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/graphadvocate-com/well-known/graphadvocate-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/graphadvocate-com-well-known.yml
- group: build
  href: https://artifacts.apis.io/graphadvocate-com/packages/graphadvocate-com-packages.yml
  title: ''
  type: Packages
  url: packages/graphadvocate-com-packages.yml
- group: build
  href: https://artifacts.apis.io/graphadvocate-com/packages/graphadvocate-com-packages.yml
  title: ''
  type: SDKs
  url: packages/graphadvocate-com-packages.yml
- group: agent
  href: https://artifacts.apis.io/graphadvocate-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/graphadvocate-com/conformance/graphadvocate-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/graphadvocate-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/graphadvocate-com/errors/graphadvocate-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/graphadvocate-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/graphadvocate-com/lifecycle/graphadvocate-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/graphadvocate-com-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/graphadvocate-com/lifecycle/graphadvocate-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/graphadvocate-com-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/graphadvocate-com/authentication/graphadvocate-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/graphadvocate-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/graphadvocate-com/conventions/graphadvocate-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/graphadvocate-com-conventions.yml
- group: commercial
  href: https://artifacts.apis.io/graphadvocate-com/plans/graphadvocate-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/graphadvocate-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/graphadvocate-com/rate-limits/graphadvocate-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/graphadvocate-com-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/graphadvocate-com/overlays/graphadvocate-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/graphadvocate-com-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/graphadvocate-com/regulatory/graphadvocate-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/graphadvocate-com-regulatory-posture.yml
- group: auth
  href: https://artifacts.apis.io/graphadvocate-com/security/graphadvocate-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/graphadvocate-com-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/graphadvocate-com/agentic-access/graphadvocate-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/graphadvocate-com-agentic-access.yml
created: '2026-09-19'
description: 'PaulieB14 (GitHub handle of the Graph Advocate author; provider.organization in the published A2A agent card) operates Graph Advocate, an onchain-data routing agent for The Graph Protocol at graphadvocate.com. Agents send a plain-English blockchain data question over A2A JSON-RPC 2.0, REST or MCP and receive the best subgraph among 15,500+ indexed on The Graph, a ready-to-run GraphQL query and, on paid calls, the executed rows. Twenty-two paid endpoints add derived trader intelligence for Hyperliquid perps, Polymarket, Kalshi, Limitless and Uniswap plus natural-language SQL over x402 settlements on Base. There are no API keys or signups: paid calls settle in USDC on Base via x402 (HTTP 402 + PAYMENT-REQUIRED header), and the agent is registered as ERC-8004 agent #734 (Arbitrum) and #41034 (Base) under the ENS name graphadvocate.eth. The author also publishes six npx-installable MCP servers (Aave, Uniswap, Polymarket, lending, Limitless) that read The Graph directly.'
finops:
- has_sources: true
  method: derived
  name: Graphadvocate Com Finops
  primary_unit: query
  service_category: ''
  slug: graphadvocate-com-finops
  template: false
image: https://graphadvocate.com/graphadvocate.png
layout: provider
mcp_servers:
- description: Remote MCP server at graphadvocate.com over HTTP; 3 tools listed.
  name: PaulieB14 MCP Server
  slug: graph-advocate-mcp
modified: '2026-09-19'
name: PaulieB14
nav: Providers
network: true
overview: 'PaulieB14 publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Ask API, Hyperliquid API, and 9 more. Tagged areas include Blockchain, On-Chain Data, The Graph, Subgraph, and GraphQL.


  The PaulieB14 catalog on APIs.io includes 1 Spectral governance ruleset.


  PaulieB14''s developer surface includes documentation, getting-started guide, API reference, pricing, authentication, and 24 more developer resources.'
plans:
- name: Graphadvocate Com Plans Pricing
  plan_count: 3
  slug: graphadvocate-com-plans-pricing
- name: Graphadvocate Com Price Estimates
  plan_count: 0
  slug: graphadvocate-com-price-estimates
random_paper: 5
rate_limits:
- limit_count: 0
  name: Graphadvocate Com Rate Limits
  slug: graphadvocate-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: PaulieB14 API Rules
  rule_count: 48
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 2
  slug: graphadvocate-com-rules
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 44.7
    contract_governance: 31.8
    contract_quality: 52.4
    developer_ergonomics: 45.2
    discoverability: 75.0
    operational_transparency: 10.5
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/graphadvocate-com/graphadvocate-com-2026-10-11T105014.png
security:
- kind: authentication
  name: Graphadvocate Com Authentication
  slug: graphadvocate-com-authentication
  summary_line: none/x402-payment · 4 schemes
- kind: domain-security
  name: Graphadvocate Com Domain Security
  slug: graphadvocate-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: graph-advocate
  slug: graphadvocate-com-graph-advocate
- name: Graphadvocate
  slug: graphadvocate-com-graphadvocate
slug: graphadvocate-com
tags:
- Blockchain
- On-Chain Data
- The Graph
- Subgraph
- GraphQL
- MCP
- A2A
- x402
- Agentic Commerce
- AI Agents
- DeFi
- Prediction Markets
- Trader Intelligence
- Web3
website: https://graphadvocate.com/
---
