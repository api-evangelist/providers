---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arena-club-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arenaclub.com
- group: other
  title: ''
  type: Marketplace
  url: https://arenaclub.com/marketplace
- group: operate
  title: ''
  type: Support
  url: https://arenaclubsupport.zendesk.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://arenaclub.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://info.arenaclub.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://info.arenaclub.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arenaclub
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arena-club-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Arena Club ships a Next.js web app and native iOS/Android apps backed by an undocumented Express service at api.arenaclub.com, but publishes no developer portal, no API reference, no SDK and no machine-readable contract - every OpenAPI, GraphQL, MCP, agent-card and /.well-known probe against arenaclub.com, api.arenaclub.com and info.arenaclub.com returned 404.
  evidence:
  - status: 404
    url: https://api.arenaclub.com/openapi.json
  - status: 404
    url: https://api.arenaclub.com/graphql
  - status: 404
    url: https://api.arenaclub.com/.well-known/agent-card.json
  - status: 404
    url: https://arenaclub.com/.well-known/api-catalog
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Arena Club is a technology-first trading-card and collectibles platform founded in 2022 by entrepreneur Brian Lee and baseball Hall-of-Famer Derek Jeter, operating as Arenaclub.com, Inc. The company combines AI- and computer-vision-assisted card grading, an insured physical vault with 24/7 surveillance and climate control, a digital "Showroom" where collectors organize vaulted cards into collections, and an online marketplace for buying, selling and trading slabbed sports and trading-card-game cards. Members submit cards for grading and vaulting, browse and transact in the marketplace, open digital packs, and can retrieve physical cards from the vault on demand. Arena Club ships web and native iOS/Android apps but publishes no public developer program, API documentation, or machine-readable API contract.
image: https://assets.arenaclub.com/homepage_assets/social_img.png
layout: provider
modified: '2026-08-06'
name: Arena Club
nav: Providers
network: true
overview: 'Arena Club is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Collectibles, Trading Cards, Marketplace, and E-Commerce.


  Arena Club''s developer surface includes support, signup flow, and 7 more developer resources.'
random_paper: 58
score:
  band: emerging
  composite: 15.3
  delta: 0.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arena-club/refs/heads/main/screenshots/arena-club-2026-08-07T161644.png
security:
- kind: domain-security
  name: Arena Club Domain Security
  slug: arena-club-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arena-club
tags:
- Company
- Collectibles
- Trading Cards
- Marketplace
- E-Commerce
- Sports
- Grading
- Consumer
website: https://arenaclub.com
---
