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
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.9
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Low-latency Solana trading API (gRPC, HTTP/REST with per-region Swagger UI, WebSocket, and QUIC) for transaction submission, batching, sniping, bundle execution, DEX quoting/swaps (Jupiter, Raydium, P
  name: bloXroute Solana Trader API
  slug: bloxroute-solana-trader-api
artifact_total: 6
asyncapis:
- description: Event surface for the bloXroute Blockchain Distribution Network and Solana Trader API. Captured by the API Evangelist enrichment pipeline from the provider's published stream documentation and protobu
  name: bloXroute Streams (BDN + Solana Trader API)
  slug: bloxroute-streams-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloxroute-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bloxroute.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bloxroute.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bloxroute.com/
- group: docs
  title: ''
  type: APIReference
  url: https://uk.solana.dex.blxrbdn.com/swagger/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bloxroute.com/getting-started/register-an-account
- group: start
  title: ''
  type: SignUp
  url: https://portal.bloxroute.com/
- group: operate
  title: ''
  type: Support
  url: https://docs.bloxroute.com/getting-started/technical-support
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.bloxroute.com/getting-started/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.bloxroute.com/getting-started/technical-support/cloud-api-health
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloXroute-Labs
- group: auth
  title: ''
  type: Authentication
  url: authentication/bloxroute-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bloxroute-mcp.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/bloxroute-solana-trader.proto
- group: build
  title: ''
  type: Packages
  url: packages/bloxroute-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bloxroute-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/bloxroute-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bloxroute-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bloxroute-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bloxroute-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bloxroute-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bloxroute-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bloxroute-rate-limits.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/bloxroute-streams-asyncapi.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bloxroute-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: bloXroute operates the Blockchain Distribution Network (BDN), a high-capacity, low-latency global relay network that speeds up transaction and block propagation for blockchain traders, builders, and validators. Its developer surface spans the BDN Gateway and Cloud API, the Solana Trader API (gRPC/HTTP/WebSocket/QUIC) for low-latency transaction submission, bundles, sniping, and DEX routing across Pump.fun, Jupiter, and Raydium, real-time mempool/block/event streams (newTxs, pendingTxs, txReceipts, newBlocks), the Optimized Feed Relay (OFR) shred stream, MEV relay and BackRunMe programs, and Protect/Fast RPC services. Supported chains include Solana, BNB Chain, Base, Ethereum, Polygon, Hyperliquid, Robinhood, Monad, and X Layer. Added to the API Evangelist network as a crypto-infrastructure provider.
image: https://avatars.githubusercontent.com/u/36855910?v=4
layout: provider
mcp_servers:
- description: Official bloXroute hosted MCP server. Provides read-only access to bloXroute's public documentation and integration knowledge so agents can find endpoints, understand services, and generate integratio
  name: bloXroute MCP Server
  slug: bloxroute-mcp-server
modified: '2026-07-18'
name: bloXroute
nav: Providers
network: true
overview: 'bloXroute publishes 1 API on the [APIs.io](https://apis.io/) network: Solana Trader API. Tagged areas include Company, Crypto, Blockchain, Trading, and MEV.


  The bloXroute catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  bloXroute''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, pricing, authentication, and 19 more developer resources.'
random_paper: 9
rate_limits:
- limit_count: 0
  name: Bloxroute Rate Limits
  slug: bloxroute-rate-limits
score:
  band: developing
  composite: 40.9
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 47.8
    developer_ergonomics: 70.8
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 40.9
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloxroute/refs/heads/main/screenshots/bloxroute-2026-07-25T203421.png
security:
- kind: authentication
  name: Bloxroute Authentication
  slug: bloxroute-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bloxroute Domain Security
  slug: bloxroute-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloxroute
tags:
- Company
- Crypto
- Blockchain
- Trading
- MEV
- Solana
- Ethereum
- Low Latency
- Streaming
- Infrastructure
website: https://bloxroute.com/
---
