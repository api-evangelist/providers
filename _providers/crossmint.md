---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Crossmint Agentic Access
  operation_count: 18
  slug: crossmint-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 12
apis:
- description: REST API to create and manage server-side custodial and non-custodial smart wallets across EVM and Solana, sign transactions, manage delegated permissions.
  name: Crossmint Wallets API
  slug: wallets-api
- description: REST API to mint and manage NFTs on multiple chains, including collection creation, batch minting, and metadata management.
  name: Crossmint Minting API
  slug: minting-api
- description: REST API for hosted and headless checkout flows allowing credit-card and crypto purchases of NFTs.
  name: Crossmint Checkout API
  slug: checkout-api
- description: REST API to issue, manage, and verify verifiable credentials anchored on chain.
  name: Crossmint Verifiable Credentials API
  slug: credentials-api
- description: REST Order API for fully headless on-chain commerce flows including fiat and crypto payment intents.
  name: Crossmint Headless Checkout (Order API)
  slug: headless-checkout
- description: The Balances API from Crossmint — 1 operation(s) for balances.
  name: Crossmint Balances API
  slug: crossmint-balances-api
- description: The NFTs API from Crossmint — 1 operation(s) for nfts.
  name: Crossmint NFTs API
  slug: crossmint-nfts-api
- description: The Signatures API from Crossmint — 3 operation(s) for signatures.
  name: Crossmint Signatures API
  slug: crossmint-signatures-api
- description: The Signers API from Crossmint — 2 operation(s) for signers.
  name: Crossmint Signers API
  slug: crossmint-signers-api
- description: The Transactions API from Crossmint — 3 operation(s) for transactions.
  name: Crossmint Transactions API
  slug: crossmint-transactions-api
- description: The Transfers API from Crossmint — 2 operation(s) for transfers.
  name: Crossmint Transfers API
  slug: crossmint-transfers-api
- description: The Wallets API from Crossmint — 2 operation(s) for wallets.
  name: Crossmint Wallets API
  slug: crossmint-wallets-api
artifact_total: 20
collections:
- collection_type: open
  name: Crossmint Wallets API
  slug: open-crossmint
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crossmint-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crossmint-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crossmint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crossmint-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crossmint
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crossmint-io
- group: company
  title: ''
  type: Website
  url: https://www.crossmint.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/crossmint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crossmint-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/crossmint-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.crossmint.com/llms.txt
created: '2026-05-08'
description: Crossmint is a Web3 platform offering APIs for wallets, NFT minting, checkout, payments, embedded checkout, and verifiable credentials. Supports server-managed wallets across EVM and Solana, fiat-on-ramp checkout, and credit-card-funded NFT purchases.
finops:
- name: Crossmint Finops
  service_category: Web3
  slug: crossmint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crossmint.png
layout: provider
modified: '2026-05-08'
name: Crossmint
nav: Providers
network: true
overview: 'Crossmint publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Balances API, NFTs API, Signatures API, and 4 more. Tagged areas include Web3, Wallets, NFT, Payments, and Checkout.


  Crossmint''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Crossmint Plans Pricing
  plan_count: 3
  slug: crossmint-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 1
  name: Crossmint Rate Limits
  slug: crossmint-rate-limits
score:
  band: thin
  composite: 34.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.4
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crossmint/refs/heads/main/screenshots/crossmint-2026-06-20T175244.png
security:
- kind: authentication
  name: Crossmint Authentication
  slug: crossmint-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Crossmint Domain Security
  slug: crossmint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crossmint Vulnerability Disclosure
  slug: crossmint-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crossmint
tags:
- Web3
- Wallets
- NFT
- Payments
- Checkout
website: https://www.crossmint.com/
---
