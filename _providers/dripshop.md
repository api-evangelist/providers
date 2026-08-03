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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: First-party GraphQL API powering Drip Shop Live's livestream shopping clients — streams, auctions, box breaks, giveaways, catalog, carts, orders, payments and messaging. 268 queries, 283 mutations, 56
  name: Drip Shop Live GraphQL API
  slug: drip-shop-live-graphql-api
artifact_total: 5
common:
- group: docs
  title: ''
  type: GraphQL
  url: graphql/dripshop-schema.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/dripshop-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dripshop-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dripshop-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dripshop-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dripshop-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dripshop-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dripshop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dripshop.live/
- group: operate
  title: ''
  type: Support
  url: https://help.dripshop.live/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://host.dripshop.live/creator-program/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dripshop.live/tos
created: '2026-07-17'
description: Drip Shop Live (legal entity Flourish Cares, Inc. DBA Drip Shop Live) is a livestream shopping marketplace and community built for collectors. Sellers host live streams to run realtime auctions, box breaks, provably-fair pull games and giveaways across trading cards (Pokémon, Magic, Yu-Gi-Oh!, Digimon), sports cards and other collectibles, while buyers watch, bid, chat and check out in-stream and earn Drip Coin rewards. The platform is crypto-native — wallet sign-in, Solana, Base and a Farcaster mini-app — alongside Stripe and PayPal payments, and is backed by Kindred Ventures. It runs on a single first-party GraphQL API (introspection enabled) powering its iOS, Android and web clients.
graphqls:
- description: Drip Shop Live (legal entity **Flourish Cares, Inc.** DBA Drip Shop Live) operates a
  name: Drip Shop Live GraphQL API
  slug: dripshop-graphql
image: https://cdn.dripshop.live/images/mini_app_hero.jpg
layout: provider
mcp_servers:
- description: ''
  name: dripshop-mcp.yml
  slug: dripshop-mcpyml
modified: '2026-07-18'
name: Dripshop
nav: Providers
network: true
overview: 'Dripshop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Live Shopping, Collectibles, Trading Cards, and Marketplace.


  Dripshop''s developer surface includes authentication, support, getting-started guide, and 9 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 28.4
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 43.2
    developer_ergonomics: 28.3
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 28.4
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dripshop/refs/heads/main/screenshots/dripshop-2026-07-25T212415.png
security:
- kind: authentication
  name: Dripshop Authentication
  slug: dripshop-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Dripshop Domain Security
  slug: dripshop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dripshop
tags:
- Company
- Live Shopping
- Collectibles
- Trading Cards
- Marketplace
- Ecommerce
- Auctions
- Live Streaming
- Payments
- GraphQL
website: https://dripshop.live/
---
