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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: User profile and balance.
  name: DMarket Account API
  slug: dmarket-account-api
- description: Aggregated market price data.
  name: DMarket Aggregator API
  slug: dmarket-aggregator-api
- description: Browse marketplace offers and buy orders (targets), and purchase items.
  name: DMarket Buy items API
  slug: dmarket-buy-items-api
- description: User inventory, deposits and withdrawals.
  name: DMarket Inventory/items API
  slug: dmarket-inventory-items-api
- description: Create, edit, delete and list your sell offers.
  name: DMarket Sell Items API
  slug: dmarket-sell-items-api
- description: History of your completed sales.
  name: DMarket Sold user items API
  slug: dmarket-sold-user-items-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dmarket-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dmarket-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/dmarket-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dmarket-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dmarket-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dmarket-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://dmarket.com/ingame-items/item-list/csgo-skins
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dmarket.com/trading-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dmarket.com/v1/swagger.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dmarket.com/v1/swagger.html
- group: start
  title: ''
  type: GettingStarted
  url: https://dmarket.com/faq#tradingAPI
- group: operate
  title: ''
  type: Support
  url: https://dmarket.com/faq
- group: company
  title: ''
  type: Blog
  url: https://dmarket.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dmarket
- group: commercial
  title: ''
  type: Pricing
  url: https://dmarket.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dmarket.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dmarket.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dmarket.com/privacy-policy
created: '2026-07-17'
description: 'DMarket is a marketplace for trading in-game items and skins across titles like CS2 (CS:GO), Dota 2, Team Fortress 2, and Rust. It offers a public JSON-based Trading API that lets developers programmatically manage their DMarket inventory: read account balance, sync and deposit items from linked game inventories, create and manage sell offers, place standing buy orders (targets), buy and withdraw assets, read aggregated market prices, and pull sales history. Requests authenticate with a public API key plus a per-request Ed25519 signature. DMarket was surfaced as a portfolio company of Pantera Capital. Sector: crypto / gaming.'
image: https://dmarket.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: dmarket-mcp.yml
  slug: dmarket-mcpyml
modified: '2026-07-18'
name: DMarket
nav: Providers
network: true
overview: 'DMarket publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Aggregator API, Buy items API, and 3 more. Tagged areas include Company, Crypto, Gaming, Marketplace, and Trading.


  DMarket''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 12 more developer resources.'
random_paper: 33
score:
  band: developing
  composite: 43.4
  delta: -3.8
  facets:
    commercial_clarity: 44.7
    contract_quality: 53.9
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 47.2
  provenance:
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
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dmarket/refs/heads/main/screenshots/dmarket-2026-07-25T212204.png
security:
- kind: authentication
  name: Dmarket Authentication
  slug: dmarket-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Dmarket Domain Security
  slug: dmarket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dmarket
tags:
- Company
- Crypto
- Gaming
- Marketplace
- Trading
- Skins
- In-Game Items
- Blockchain
website: https://dmarket.com/ingame-items/item-list/csgo-skins
---
