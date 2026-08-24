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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/id-planet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://idplanet.io/
- group: docs
  title: ''
  type: Documentation
  url: https://idplanet.gitbook.io/whitepaper
- group: company
  title: ''
  type: Blog
  url: https://idplanet.io/blog/
- group: operate
  title: ''
  type: Support
  url: https://idplanet.io/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://idplanet.io/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/id-planet-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/id-planet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/id-planet-rate-limits.yml
- group: company
  title: ''
  type: Twitter
  url: https://x.com/idplanet_world
- group: other
  title: ''
  type: Telegram
  url: https://t.me/idplanet
- group: learn
  title: ''
  type: YouTube
  url: https://youtube.com/@idplanet
coverage:
  checked: '2026-08-22'
  detail: ID Planet's GitBook whitepaper advertises an EVM-compatible "ID Planet Chain", an "ID Explorer" block explorer and asset APIs "easily accessible to third-party developers", but names no RPC URL, chain ID, explorer host, SDK or specification anywhere across its sixteen published pages, and idplanet.io returns a hard 404 for /llms.txt, /openapi.json and every /.well-known/ path -- the only machine-readable document on any ID Planet host is the llms.txt GitBook emits automatically for the whitepaper space.
  evidence:
  - status: 200
    url: https://idplanet.gitbook.io/whitepaper/id-planet-ecosystem/id-planet-chain.md
  - status: 200
    url: https://idplanet.gitbook.io/whitepaper/llms.txt
  - status: 404
    url: https://idplanet.io/openapi.json
  - status: 404
    url: https://idplanet.io/.well-known/api-catalog
  - status: 404
    url: https://idplanet.io/.well-known/agent-card.json
  - status: 404
    url: https://idplanet.io/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: ID Planet is a Web3 GameFi company building an EVM-compatible blockchain ecosystem for blockchain gaming. Its published ecosystem spans ID Planet Chain, the ID Explorer block explorer, the ID Wallet multi-chain wallet, ID SWAP (a decentralized exchange), ID PLANETXC (a centralized exchange) and an NFT marketplace, alongside first-party game titles Infinitar (5v5 MOBA), Runesoul (ARPG) and CoolGods (MOBA). The $ID governance token is issued as a BEP20 asset on BNB Chain with a total supply of 7,800,000,000 and a mining/burn distribution model. Company material is published as a GitBook whitepaper in eight languages. As of 2026-08-22 ID Planet publishes no developer portal, API reference, RPC endpoint, chain ID or machine-readable specification on any host it controls, so this profile is identity and documentation only.
image: https://idplanet.io/wp-content/uploads/2025/03/cropped-20250328_225855_0000-192x192.png
layout: provider
modified: '2026-08-22'
name: ID Planet
nav: Providers
network: true
overview: 'ID Planet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Web3, Blockchain, Gaming, and GameFi.


  ID Planet''s developer surface includes documentation, engineering blog, support, YouTube channel, and 8 more developer resources.'
plans:
- name: Id Planet Plans Pricing
  plan_count: 0
  slug: id-planet-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Id Planet Rate Limits
  slug: id-planet-rate-limits
score:
  band: emerging
  composite: 11.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 26.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: domain-security
  name: Id Planet Domain Security
  slug: id-planet-domain-security
  summary_line: TLSv1.2 · DMARC
slug: id-planet
tags:
- Company
- Web3
- Blockchain
- Gaming
- GameFi
- Cryptocurrency
- NFT
- Digital Wallet
- Cryptocurrency Exchange
website: https://idplanet.io/
---
