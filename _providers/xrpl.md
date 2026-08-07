---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 4
apis:
- description: JSON-RPC interface to the XRP Ledger mainnet for querying accounts, transactions, ledgers, order books, AMM pools, NFTs, and server info. Served by community-run public rippled and Clio nodes.
  name: XRPL JSON-RPC API (Mainnet)
  slug: xrpl-json-rpc-api-mainnet
- description: WebSocket interface to the XRP Ledger mainnet supporting all JSON-RPC methods plus real-time subscriptions for ledger closes, transactions, account activity, order book updates, and payment path findi
  name: XRPL WebSocket API (Mainnet)
  slug: xrpl-websocket-api-mainnet
- description: JSON-RPC interface to the XRP Ledger Altnet testnet for development and testing. Supports the same method set as mainnet. Testnet XRP has no monetary value and can be obtained via the XRPL faucet.
  name: XRPL JSON-RPC API (Testnet)
  slug: xrpl-json-rpc-api-testnet
- description: WebSocket interface to the XRP Ledger Altnet testnet for development and testing. Supports real-time subscriptions identical to mainnet WebSocket API.
  name: XRPL WebSocket API (Testnet)
  slug: xrpl-websocket-api-testnet
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xrpl-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/XRPLF
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/XRPLF/rippled
- group: docs
  title: ''
  type: Documentation
  url: https://xrpl.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://xrpl.org/docs/tutorials/get-started/
- group: operate
  title: ''
  type: ChangeLog
  url: https://xrpl.org/blog/
- group: company
  title: ''
  type: Blog
  url: https://xrpl.org/blog/
- group: operate
  title: ''
  type: Community
  url: https://xrpl.org/community
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/sfX3ERAMjH
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ripple.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ripple.com/terms-of-use/
- group: operate
  title: ''
  type: StatusPage
  url: https://livenet.xrpl.org/
- group: other
  title: ''
  type: Explorer
  url: https://livenet.xrpl.org/
- group: other
  title: ''
  type: Faucet
  url: https://faucet.altnet.rippletest.net/accounts
- group: build
  title: ''
  type: SDKs
  url: https://xrpl.org/docs/references/client-libraries
created: '2026-06-14'
description: The XRP Ledger (XRPL) is a decentralized, public blockchain with fast settlement and low transaction costs. It provides HTTP/WebSocket JSON-RPC APIs for querying accounts, transactions, ledgers, order books, payment channels, and network statistics. Developers can connect to community-run public servers on mainnet, testnet, and devnet without authentication for most operations.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://xrpl.org/img/xrp-ledger-logo.svg
layout: provider
modified: '2026-06-14'
name: XRP Ledger
nav: Providers
network: true
overview: 'XRP Ledger publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, XRP, Cryptocurrency, DeFi, and Ledger.


  XRP Ledger''s developer surface includes documentation, getting-started guide, changelog, engineering blog, and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 2
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 29.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 29.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xrpl/refs/heads/main/screenshots/xrpl-2026-06-20T201721.png
security:
- kind: domain-security
  name: Xrpl Domain Security
  slug: xrpl-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: xrpl
tags:
- Blockchain
- XRP
- Cryptocurrency
- DeFi
- Ledger
- Web3
website: https://xrpl.org/
---
