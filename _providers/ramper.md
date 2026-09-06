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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://ramper.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ramper.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ramper.xyz/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ramper.xyz/embedded-wallet-sdk/quickstart
- group: company
  title: ''
  type: Blog
  url: https://blog.ramper.xyz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ramper-xyz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.ramper.xyz/embedded-wallet-sdk/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.ramper.xyz/embedded-wallet-sdk/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/ramper-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ramper-packages.yml
- group: design
  title: ''
  type: Components
  url: components/ramper-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ramper-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ramper-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ramper-llms.txt
created: '2026-07-17'
description: Ramper is a Web3 embedded-wallet and social-login platform that lets DApps onboard users with familiar Web2 credentials (Email, Google, Facebook, Apple, Twitter) and instantly create non-custodial, self-custody wallets with no seed phrases, browser extensions, or downloads. Its Embedded Wallet SDK ships as first-party npm packages for web (@ramper-v2/core, @ramper-v2/multi, @ramper/ethereum, @ramper/near, @ramper/terra, @ramper/chiliz, @ramper/viction), React Native mobile, Unity, and Telegram Mini Apps, and is compatible with ethers.js across EVM chains plus NEAR, Solana, BNB Chain, Sei, and Viction. Ramper also provides an embeddable WalletView (balances, transfers, transaction signing, fiat on-ramp) and a fiat NFT Checkout SDK. Developers integrate via an App ID / App Secret issued from the Developer Dashboard.
image: https://ramper.xyz/thumbnail.png
layout: provider
modified: '2026-07-20'
name: Ramper
nav: Providers
network: true
overview: 'Ramper is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Web3, Wallets, Embedded Wallet, and Blockchain.


  Ramper''s developer surface includes documentation, getting-started guide, engineering blog, authentication, and 10 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 20.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ramper/refs/heads/main/screenshots/ramper-2026-09-02T152843.png
security:
- kind: authentication
  name: Ramper Authentication
  slug: ramper-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Ramper Domain Security
  slug: ramper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ramper
tags:
- Company
- Web3
- Wallets
- Embedded Wallet
- Blockchain
- Social Login
- Authentication
- SDK
- NFT
- Cryptocurrency
- DeFi
website: https://ramper.xyz
---
