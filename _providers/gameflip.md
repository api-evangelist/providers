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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.0
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: Account and wallet service.
  name: Gameflip Account API
  slug: gameflip-account-api
- description: Create and manage sell/buy records (exchanges).
  name: Gameflip Exchange API
  slug: gameflip-exchange-api
- description: Create and manipulate listings of items for sale.
  name: Gameflip Listing API
  slug: gameflip-listing-api
- description: Account profile service.
  name: Gameflip Profile API
  slug: gameflip-profile-api
- description: Create listings/escrow for multiple Steam items with one trade offer.
  name: Gameflip Steam Bulk API
  slug: gameflip-steam-bulk-api
- description: Escrow Steam items.
  name: Gameflip Steam Escrow API
  slug: gameflip-steam-escrow-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gameflip API (GFAPI) Account API
  slug: open-gameflip-account-api
- collection_type: open
  name: Gameflip API (GFAPI) Account Exchange API
  slug: open-gameflip-exchange-api
- collection_type: open
  name: Gameflip API (GFAPI) Account Listing API
  slug: open-gameflip-listing-api
- collection_type: open
  name: Gameflip API (GFAPI) Account Profile API
  slug: open-gameflip-profile-api
- collection_type: open
  name: Gameflip API (GFAPI) Account Steam Bulk API
  slug: open-gameflip-steam-bulk-api
- collection_type: open
  name: Gameflip API (GFAPI) Account Steam Escrow API
  slug: open-gameflip-steam-escrow-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/gameflip-create-and-sell.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gameflip-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gameflip-gfapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://gameflip.com
- group: start
  title: ''
  type: GettingStarted
  url: https://gameflip.github.io/gfapi/
- group: docs
  title: ''
  type: Documentation
  url: https://gameflip.github.io/gfapi/
- group: docs
  title: ''
  type: APIReference
  url: https://gameflip.github.io/gfapi/
- group: build
  title: ''
  type: SDKs
  url: packages/gameflip-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/gameflip-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gameflip
- group: operate
  title: ''
  type: Support
  url: https://support.gameflip.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://gameflip.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://gameflip.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gameflip.com/about/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gameflip.com/about/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/gameflip-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gameflip-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gameflip-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gameflip-llms.txt
created: '2026-07-17'
description: 'Gameflip is a digital marketplace where gamers buy and sell games, in-game items, gift cards, game accounts, boosting/coaching gigs, and other digital goods, backed by an escrow-style buyer guarantee and a built-in wallet. For developers and power sellers, Gameflip publishes the GFAPI — a JSON REST API (base path /api/v1) for creating and managing listings, searching the marketplace, running exchanges (sell/buy records), reading account profiles and wallet history, and handling Steam item escrow and bulk trade-offer listings. Requests are authenticated with an API key plus a rotating TOTP one-time password sent in the Authorization header (`GFAPI <apikey>:<totp>`). Access is Beta and gated: API keys and TOTP secrets are issued to selected developers through Gameflip support / account settings. An official Node.js client library (gfapi) with sample code is published by Gameflip.'
image: https://gameflip.com/img/app/gf_logo_280x150.jpg
layout: provider
mcp_servers:
- description: ''
  name: gameflip-mcp.yml
  slug: gameflip-mcpyml
modified: '2026-07-19'
name: Gameflip
nav: Providers
network: true
overview: 'Gameflip publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Exchange API, Listing API, and 3 more. Tagged areas include Company, Gaming, Marketplace, Digital Goods, and E-Commerce.


  Gameflip''s developer surface includes getting-started guide, documentation, API reference, support, engineering blog, signup flow, authentication, and 12 more developer resources.'
random_paper: 92
rate_limits:
- limit_count: 1
  name: Gameflip Rate Limits
  slug: gameflip-rate-limits
score:
  band: developing
  composite: 45.7
  delta: 2.7
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 58.0
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 23.7
  previous_composite: 43.0
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
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gameflip/refs/heads/main/screenshots/gameflip-2026-07-25T215417.png
security:
- kind: authentication
  name: Gameflip Authentication
  slug: gameflip-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gameflip Domain Security
  slug: gameflip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gameflip
tags:
- Company
- Gaming
- Marketplace
- Digital Goods
- E-Commerce
- Payments
- Wallet
- Listings
- Steam
- Gift Cards
website: https://gameflip.com
---
