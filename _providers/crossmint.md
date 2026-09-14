---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Crossmint Agentic Access
  operation_count: 18
  slug: crossmint-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 1
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
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Balances API from Crossmint — 1 operation(s) for balances.
  name: Crossmint Balances API
  slug: crossmint-balances-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The NFTs API from Crossmint — 1 operation(s) for nfts.
  name: Crossmint NFTs API
  slug: crossmint-nfts-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Signatures API from Crossmint — 3 operation(s) for signatures.
  name: Crossmint Signatures API
  slug: crossmint-signatures-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Signers API from Crossmint — 2 operation(s) for signers.
  name: Crossmint Signers API
  slug: crossmint-signers-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Transactions API from Crossmint — 3 operation(s) for transactions.
  name: Crossmint Transactions API
  slug: crossmint-transactions-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Transfers API from Crossmint — 2 operation(s) for transfers.
  name: Crossmint Transfers API
  slug: crossmint-transfers-api
- baseURL: https://staging.crossmint.com/api/2022-06-09 (staging) | https://www.crossmint.com/api/2022-06-09 (prod)
  baseurl_source: declared
  description: The Wallets API from Crossmint — 2 operation(s) for wallets.
  name: Crossmint Wallets API
  slug: crossmint-wallets-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Crossmint Wallets Balances API
  slug: open-crossmint-balances-api
- collection_type: open
  name: Crossmint Wallets Balances NFTs API
  slug: open-crossmint-nfts-api
- collection_type: open
  name: Crossmint Wallets Balances Signatures API
  slug: open-crossmint-signatures-api
- collection_type: open
  name: Crossmint Wallets Balances Signers API
  slug: open-crossmint-signers-api
- collection_type: open
  name: Crossmint Wallets Balances Transactions API
  slug: open-crossmint-transactions-api
- collection_type: open
  name: Crossmint Wallets Balances Transfers API
  slug: open-crossmint-transfers-api
- collection_type: open
  name: Crossmint Balances Wallets API
  slug: open-crossmint-wallets-api
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
random_paper: 7
rate_limits:
- limit_count: 1
  name: Crossmint Rate Limits
  slug: crossmint-rate-limits
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
