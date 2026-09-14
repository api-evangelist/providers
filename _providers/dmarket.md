---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://api.dmarket.com
  baseurl_source: declared
  description: User profile and balance.
  name: DMarket Account API
  slug: dmarket-account-api
- baseURL: https://api.dmarket.com
  baseurl_source: declared
  description: Aggregated market price data.
  name: DMarket Aggregator API
  slug: dmarket-aggregator-api
- baseURL: https://api.dmarket.com
  baseurl_source: declared
  description: Browse marketplace offers and buy orders (targets), and purchase items.
  name: DMarket Buy items API
  slug: dmarket-buy-items-api
- baseURL: https://api.dmarket.com
  baseurl_source: declared
  description: User inventory, deposits and withdrawals.
  name: DMarket Inventory/items API
  slug: dmarket-inventory-items-api
- baseURL: https://api.dmarket.com
  baseurl_source: declared
  description: Create, edit, delete and list your sell offers.
  name: DMarket Sell Items API
  slug: dmarket-sell-items-api
- baseURL: https://api.dmarket.com
  baseurl_source: declared
  description: History of your completed sales.
  name: DMarket Sold user items API
  slug: dmarket-sold-user-items-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DMarket trading Account API
  slug: open-dmarket-account-api
- collection_type: open
  name: DMarket trading Account Aggregator API
  slug: open-dmarket-aggregator-api
- collection_type: open
  name: DMarket trading Account Buy items API
  slug: open-dmarket-buy-items-api
- collection_type: open
  name: DMarket trading Account Inventory/items API
  slug: open-dmarket-inventory-items-api
- collection_type: open
  name: DMarket trading Account Sell Items API
  slug: open-dmarket-sell-items-api
- collection_type: open
  name: DMarket trading Account Sold user items API
  slug: open-dmarket-sold-user-items-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/dmarket-trading-overlay.yaml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-18'
name: DMarket
nav: Providers
network: true
overview: 'DMarket publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Aggregator API, Buy items API, and 3 more. Tagged areas include Company, Crypto, Gaming, Marketplace, and Trading.


  DMarket''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 13 more developer resources.'
random_paper: 9
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
