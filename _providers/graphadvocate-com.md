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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.5
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 23
  human_in_the_loop: 4
  name: Graphadvocate Com Agentic Access
  operation_count: 23
  slug: graphadvocate-com-agentic-access
  summary_line: 23 operations · 23 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://graphadvocate.com
  baseurl_source: declared
  description: Routing and trader-intelligence API at graphadvocate.com. POST / speaks A2A JSON-RPC 2.0 (message/send) and is the free tier (3 routed queries/day per wallet-identified sender); POST /route and 22 fur
  name: Graph Advocate API
  slug: graph-advocate-api
- description: Hosted MCP server at https://graphadvocate.com/mcp (Streamable HTTP for one-shot JSON-RPC initialize and tools/list; SSE session at /mcp/sse). tools/list answers anonymously with three tools — route_d
  name: Graph Advocate MCP Server
  slug: graph-advocate-mcp-server
artifact_total: 8
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
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/llms/graphadvocate-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/graphadvocate-com-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/a2a/graphadvocate-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/graphadvocate-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/mcp/graphadvocate-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/graphadvocate-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/mcp/graphadvocate-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/graphadvocate-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/well-known/graphadvocate-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/graphadvocate-com-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/packages/graphadvocate-com-packages.yml
  title: ''
  type: Packages
  url: packages/graphadvocate-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/packages/graphadvocate-com-packages.yml
  title: ''
  type: SDKs
  url: packages/graphadvocate-com-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/conformance/graphadvocate-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/graphadvocate-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/errors/graphadvocate-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/graphadvocate-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/lifecycle/graphadvocate-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/graphadvocate-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/lifecycle/graphadvocate-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/graphadvocate-com-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/authentication/graphadvocate-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/graphadvocate-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/conventions/graphadvocate-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/graphadvocate-com-conventions.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/plans/graphadvocate-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/graphadvocate-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/rate-limits/graphadvocate-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/graphadvocate-com-rate-limits.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/overlays/graphadvocate-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/graphadvocate-com-openapi-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/regulatory/graphadvocate-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/graphadvocate-com-regulatory-posture.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/security/graphadvocate-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/graphadvocate-com-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/graphadvocate-com/refs/heads/main/agentic-access/graphadvocate-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/graphadvocate-com-agentic-access.yml
created: '2026-09-19'
description: 'PaulieB14 (GitHub handle of the Graph Advocate author; provider.organization in the published A2A agent card) operates Graph Advocate, an onchain-data routing agent for The Graph Protocol at graphadvocate.com. Agents send a plain-English blockchain data question over A2A JSON-RPC 2.0, REST or MCP and receive the best subgraph among 15,500+ indexed on The Graph, a ready-to-run GraphQL query and, on paid calls, the executed rows. Twenty-two paid endpoints add derived trader intelligence for Hyperliquid perps, Polymarket, Kalshi, Limitless and Uniswap plus natural-language SQL over x402 settlements on Base. There are no API keys or signups: paid calls settle in USDC on Base via x402 (HTTP 402 + PAYMENT-REQUIRED header), and the agent is registered as ERC-8004 agent #734 (Arbitrum) and #41034 (Base) under the ENS name graphadvocate.eth. The author also publishes six npx-installable MCP servers (Aave, Uniswap, Polymarket, lending, Limitless) that read The Graph directly.'
image: https://graphadvocate.com/graphadvocate.png
layout: provider
mcp_servers:
- description: ''
  name: PaulieB14 MCP Server
  slug: paulieb14-mcp-server
modified: '2026-09-19'
name: PaulieB14
nav: Providers
network: true
overview: 'PaulieB14 publishes 1 API on the [APIs.io](https://apis.io/) network: Graph Advocate API. Tagged areas include Blockchain, On-Chain Data, The Graph, Subgraph, and GraphQL.


  PaulieB14''s developer surface includes documentation, getting-started guide, API reference, pricing, authentication, and 24 more developer resources.'
plans:
- name: Graphadvocate Com Plans Pricing
  plan_count: 2
  slug: graphadvocate-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Graphadvocate Com Rate Limits
  slug: graphadvocate-com-rate-limits
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 64.3
    discoverability: 75.9
    operational_transparency: 13.2
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Graphadvocate Com Authentication
  slug: graphadvocate-com-authentication
  summary_line: none/x402-payment · 4 schemes
- kind: domain-security
  name: Graphadvocate Com Domain Security
  slug: graphadvocate-com-domain-security
  summary_line: TLSv1.3 · HSTS
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
