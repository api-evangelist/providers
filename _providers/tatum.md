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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tatum Agentic Access
  operation_count: 5
  slug: tatum-agentic-access
  summary_line: 5 operations
api_count: 9
apis:
- description: JSON-RPC over HTTPS to 130+ blockchain networks (Ethereum, Bitcoin, Solana, Polygon, BNB, Avalanche, Algorand, Tron, etc.).
  name: Tatum RPC Gateway
  slug: rpc-gateway
- description: REST API for indexed multi-chain blockchain data (balances, NFTs, tokens, transactions, blocks).
  name: Tatum Data API
  slug: data-api
- description: REST API for managing webhook subscriptions for blockchain events.
  name: Tatum Notifications API
  slug: notifications
- description: REST API for NFT minting, transfers, metadata, and ownership queries on multiple chains.
  name: Tatum NFT API
  slug: nft-api
- description: REST API to generate wallets, derive addresses, build/sign transactions across many chains.
  name: Tatum Wallet API
  slug: wallet-api
- description: REST API to deploy, invoke, and read smart contracts on EVM and other chains.
  name: Tatum Smart Contract API
  slug: smart-contract-api
- description: REST API for off-chain virtual account ledger with deposit address allocation, transfers, and reconciliation.
  name: Tatum Virtual Accounts (Ledger)
  slug: virtual-accounts
- description: The Data API from Tatum — 4 operation(s) for data.
  name: Tatum Data API
  slug: tatum-data-api
- description: The Rates API from Tatum — 1 operation(s) for rates.
  name: Tatum Rates API
  slug: tatum-rates-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tatum Data API
  slug: open-tatum-data-api
- collection_type: open
  name: Tatum Data Rates API
  slug: open-tatum-rates-api
- collection_type: open
  name: Tatum Data API
  slug: open-tatum
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tatum-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tatum-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tatum-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tatum-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://tatum.io/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tatumio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tatumio
- group: company
  title: ''
  type: Website
  url: https://tatum.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/tatum-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tatum-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tatum-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.tatum.io/llms.txt
created: '2026-05-08'
description: Tatum is a multi-chain Web3 platform offering an RPC Gateway across 130+ blockchains, indexed Data APIs, Notifications/Webhooks, NFT/Wallet APIs, Smart Contract APIs, Virtual Accounts, and a Key Management System (KMS). Both REST and JSON-RPC interfaces are available.
finops:
- name: Tatum Finops
  service_category: Web3
  slug: tatum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tatum.png
layout: provider
modified: '2026-05-08'
name: Tatum
nav: Providers
network: true
overview: 'Tatum publishes 2 APIs on the [APIs.io](https://apis.io/) network: Data API and Rates API. Tagged areas include Web3, Blockchain, RPC, Multi-Chain, and Wallets.


  Tatum''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Tatum Plans Pricing
  plan_count: 5
  slug: tatum-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Tatum Rate Limits
  slug: tatum-rate-limits
score:
  band: thin
  composite: 30.2
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 55.9
    developer_ergonomics: 14.3
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tatum/refs/heads/main/screenshots/tatum-2026-06-20T194929.png
security:
- kind: authentication
  name: Tatum Authentication
  slug: tatum-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tatum Domain Security
  slug: tatum-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Tatum Trust Center
  slug: tatum-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: tatum
tags:
- Web3
- Blockchain
- RPC
- Multi-Chain
- Wallets
- NFT
website: https://tatum.io/
---
