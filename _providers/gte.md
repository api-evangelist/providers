---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Gte Agentic Access
  operation_count: 18
  slug: gte-agentic-access
  summary_line: 18 operations · 1 acting
api_count: 6
apis:
- description: The Exchange API from GTE — 1 operation(s) for exchange.
  name: GTE Exchange API
  slug: gte-exchange-api
- description: The Health API from GTE — 1 operation(s) for health.
  name: GTE Health API
  slug: gte-health-api
- description: The Info API from GTE — 1 operation(s) for info.
  name: GTE Info API
  slug: gte-info-api
- description: The Markets API from GTE — 6 operation(s) for markets.
  name: GTE Markets API
  slug: gte-markets-api
- description: The Tokens API from GTE — 3 operation(s) for tokens.
  name: GTE Tokens API
  slug: gte-tokens-api
- description: The Users API from GTE — 6 operation(s) for users.
  name: GTE Users API
  slug: gte-users-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gte-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gte-agentic-access.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gte.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gte.xyz
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gte-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/gte-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gte-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gte-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gte-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gte-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gte-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gte-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gte-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gte-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gte-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gte-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gte-openapi-overlay.yaml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Liquid-Labs-Inc
- group: company
  title: ''
  type: Blog
  url: https://www.gte.xyz/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/gte-xyz
- group: start
  title: ''
  type: SignUp
  url: https://testnet.gte.xyz/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gte.xyz/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gte.xyz/privacy-policy
- group: other
  title: ''
  type: X
  url: https://x.com/GTE_XYZ
- group: company
  title: ''
  type: Website
  url: https://www.gte.xyz
created: '2026-07-17'
description: GTE (Global Token Exchange) is a non-custodial, permissionless decentralized exchange built on MegaETH, offering a central limit order book (CLOB) with CEX-level speed — advertised at 100,000 orders per second and ~1ms latency — combined with DeFi security properties. Users trade crypto and tokenized assets 24/7 from a self-custodied wallet, with spot and leveraged/perpetual markets, shortable positions, and on-chain settlement. GTE exposes a public HTTP + WebSocket API (GTE API v1) covering tokens, markets, candles, trades, order books, and per-wallet portfolio/order data, plus a signed POST /exchange endpoint for submitting orders and trades. An official Python SDK (gte-py) constructs the signed transaction bodies. GTE is developed by Liquid Labs and backed by Paradigm.
image: https://framerusercontent.com/images/dmNBRSvrpcZRlw2DSNsXF7eY0MA.png
layout: provider
mcp_servers:
- description: ''
  name: gte-mcp.yml
  slug: gte-mcpyml
modified: '2026-07-19'
name: GTE
nav: Providers
network: true
overview: 'GTE publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Exchange API, Health API, Info API, and 3 more. Tagged areas include Company, Crypto Defi, Decentralized Exchange, Trading, and Market Data.


  GTE''s developer surface includes documentation, authentication, sandbox, engineering blog, support, signup flow, and 20 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 40.0
  delta: -2.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 44.9
    developer_ergonomics: 51.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gte/refs/heads/main/screenshots/gte-2026-07-25T220408.png
security:
- kind: authentication
  name: Gte Authentication
  slug: gte-authentication
  summary_line: signature · 0 schemes
- kind: domain-security
  name: Gte Domain Security
  slug: gte-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gte
tags:
- Company
- Crypto Defi
- Decentralized Exchange
- Trading
- Market Data
- Order Book
- Perpetuals
- MegaETH
- Blockchain
website: https://www.gte.xyz
---
