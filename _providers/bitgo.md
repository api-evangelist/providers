---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Bitgo Agentic Access
  operation_count: 19
  slug: bitgo-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 11
apis:
- description: The Addresses API from BitGo — 1 operation(s) for addresses.
  name: BitGo Addresses API
  slug: bitgo-addresses-api
- description: The Enterprise API from BitGo — 1 operation(s) for enterprise.
  name: BitGo Enterprise API
  slug: bitgo-enterprise-api
- description: The Keychains API from BitGo — 1 operation(s) for keychains.
  name: BitGo Keychains API
  slug: bitgo-keychains-api
- description: The Policies API from BitGo — 1 operation(s) for policies.
  name: BitGo Policies API
  slug: bitgo-policies-api
- description: The Staking API from BitGo — 1 operation(s) for staking.
  name: BitGo Staking API
  slug: bitgo-staking-api
- description: The Trading API from BitGo — 1 operation(s) for trading.
  name: BitGo Trading API
  slug: bitgo-trading-api
- description: The Transactions API from BitGo — 2 operation(s) for transactions.
  name: BitGo Transactions API
  slug: bitgo-transactions-api
- description: The Transfers API from BitGo — 2 operation(s) for transfers.
  name: BitGo Transfers API
  slug: bitgo-transfers-api
- description: The User API from BitGo — 1 operation(s) for user.
  name: BitGo User API
  slug: bitgo-user-api
- description: The Wallets API from BitGo — 2 operation(s) for wallets.
  name: BitGo Wallets API
  slug: bitgo-wallets-api
- description: The Webhooks API from BitGo — 1 operation(s) for webhooks.
  name: BitGo Webhooks API
  slug: bitgo-webhooks-api
artifact_total: 19
collections:
- collection_type: open
  name: BitGo Platform API
  slug: open-bitgo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bitgo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitgo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitgo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitgo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BitGo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bitgo
- group: company
  title: ''
  type: Website
  url: https://www.bitgo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bitgo.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/bitgo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bitgo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bitgo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.bitgo.com/resources/blog/
created: '2026-07-01'
description: BitGo is an institutional digital-asset custody, wallet, staking, trading, and settlement infrastructure provider and qualified custodian. The BitGo Platform REST API v2 lets developers programmatically create and manage multi-signature and advanced-cryptography wallets, addresses, keychains, transactions and transfers, webhooks, spending policies, staking, and Go Network off-chain settlement across hundreds of coins and tokens, with an optional self-hosted Express signing proxy.
finops:
- name: Bitgo Finops
  service_category: Digital Asset Custody and Infrastructure
  slug: bitgo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitgo.png
layout: provider
modified: '2026-07-01'
name: BitGo
nav: Providers
network: true
overview: 'BitGo publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Enterprise API, Keychains API, and 8 more. Tagged areas include Digital Assets, Custody, Wallets, Blockchain, and Crypto.


  BitGo''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Bitgo Plans Pricing
  plan_count: 4
  slug: bitgo-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 2
  name: Bitgo Rate Limits
  slug: bitgo-rate-limits
score:
  band: thin
  composite: 39.4
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.8
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitgo/refs/heads/main/screenshots/bitgo-2026-07-25T203154.png
security:
- kind: authentication
  name: Bitgo Authentication
  slug: bitgo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bitgo Domain Security
  slug: bitgo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bitgo Vulnerability Disclosure
  slug: bitgo-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: bitgo
tags:
- Digital Assets
- Custody
- Wallets
- Blockchain
- Crypto
- Staking
- Settlement
website: https://www.bitgo.com/
---
