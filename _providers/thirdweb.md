---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Thirdweb Agentic Access
  operation_count: 42
  slug: thirdweb-agentic-access
  summary_line: 42 operations · 23 acting
api_count: 9
apis:
- description: Wallet authentication flows.
  name: thirdweb Authentication API
  slug: thirdweb-authentication-api
- description: Smart contract read, write, and deployment.
  name: thirdweb Contracts API
  slug: thirdweb-contracts-api
- description: Backend transaction execution with server wallets.
  name: thirdweb Engine API
  slug: thirdweb-engine-api
- description: Indexed on-chain events, transactions, tokens, and NFTs.
  name: thirdweb Insight API
  slug: thirdweb-insight-api
- description: AI blockchain interface.
  name: thirdweb Nebula API
  slug: thirdweb-nebula-api
- description: Bridge, swap, convert, onramp, and x402 payments.
  name: thirdweb Payments API
  slug: thirdweb-payments-api
- description: Token creation, listing, and ownership.
  name: thirdweb Tokens API
  slug: thirdweb-tokens-api
- description: Transaction submission and status.
  name: thirdweb Transactions API
  slug: thirdweb-transactions-api
- description: User and server wallet management, signing, and transfers.
  name: thirdweb Wallets API
  slug: thirdweb-wallets-api
artifact_total: 16
collections:
- collection_type: open
  name: thirdweb API
  slug: open-thirdweb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thirdweb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thirdweb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thirdweb-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.thirdweb.com/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thirdweb-dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/third-web
- group: company
  title: ''
  type: Website
  url: https://thirdweb.com
- group: docs
  title: ''
  type: Documentation
  url: https://portal.thirdweb.com
- group: commercial
  title: ''
  type: Plans
  url: plans/thirdweb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thirdweb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/thirdweb-finops.yml
created: '2026-06-20'
description: thirdweb is a full-stack web3 development platform. Its HTTP APIs unify wallet management, transaction execution, smart contract read/write, token and NFT operations, fiat-to-crypto payments and bridging, indexed on-chain data, and an AI blockchain interface across thousands of EVM chains and Solana, authenticated with a client ID or secret key.
finops:
- name: Thirdweb Finops
  service_category: Web3 and Blockchain Infrastructure
  slug: thirdweb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thirdweb.png
layout: provider
modified: '2026-06-20'
name: thirdweb
nav: Providers
network: true
overview: 'thirdweb publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Contracts API, Engine API, and 6 more. Tagged areas include Web3, Blockchain, Wallets, Smart Contracts, and Payments.


  thirdweb''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Thirdweb Plans Pricing
  plan_count: 5
  slug: thirdweb-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 6
  name: Thirdweb Rate Limits
  slug: thirdweb-rate-limits
score:
  band: thin
  composite: 35.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thirdweb/refs/heads/main/screenshots/thirdweb-2026-06-20T195307.png
security:
- kind: authentication
  name: Thirdweb Authentication
  slug: thirdweb-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Thirdweb Domain Security
  slug: thirdweb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: thirdweb
tags:
- Web3
- Blockchain
- Wallets
- Smart Contracts
- Payments
- Indexer
website: https://thirdweb.com
---
