---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Bitgo Agentic Access
  operation_count: 19
  slug: bitgo-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 1
apis:
- baseURL: https://app.bitgo.com/api/v2
  baseurl_source: declared
  description: The Addresses API from BitGo — 1 operation(s) for addresses.
  name: BitGo Addresses API
  slug: bitgo-addresses-api
- baseURL: https://app.bitgo.com/api/v2
  baseurl_source: declared
  description: The Enterprise API from BitGo — 1 operation(s) for enterprise.
  name: BitGo Enterprise API
  slug: bitgo-enterprise-api
- baseURL: https://app.bitgo.com/api/v2
  baseurl_source: declared
  description: The Keychains API from BitGo — 1 operation(s) for keychains.
  name: BitGo Keychains API
  slug: bitgo-keychains-api
- baseURL: https://app.bitgo.com/api/v2
  baseurl_source: declared
  description: The Policies API from BitGo — 1 operation(s) for policies.
  name: BitGo Policies API
  slug: bitgo-policies-api
- baseURL: https://app.bitgo.com/api/v2
  baseurl_source: declared
  description: The Staking API from BitGo — 1 operation(s) for staking.
  name: BitGo Staking API
  slug: bitgo-staking-api
- baseURL: https://app.bitgo.com/api/v2
  baseurl_source: declared
  description: The Trading API from BitGo — 1 operation(s) for trading.
  name: BitGo Trading API
  slug: bitgo-trading-api
- baseURL: https://app.bitgo.com/api/v2
  baseurl_source: declared
  description: The Transactions API from BitGo — 2 operation(s) for transactions.
  name: BitGo Transactions API
  slug: bitgo-transactions-api
- baseURL: https://app.bitgo.com/api/v2
  baseurl_source: declared
  description: The Transfers API from BitGo — 2 operation(s) for transfers.
  name: BitGo Transfers API
  slug: bitgo-transfers-api
- baseURL: https://app.bitgo.com/api/v2
  baseurl_source: declared
  description: The User API from BitGo — 1 operation(s) for user.
  name: BitGo User API
  slug: bitgo-user-api
- baseURL: https://app.bitgo.com/api/v2
  baseurl_source: declared
  description: The Wallets API from BitGo — 2 operation(s) for wallets.
  name: BitGo Wallets API
  slug: bitgo-wallets-api
- baseURL: https://app.bitgo.com/api/v2
  baseurl_source: declared
  description: The Webhooks API from BitGo — 1 operation(s) for webhooks.
  name: BitGo Webhooks API
  slug: bitgo-webhooks-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BitGo Platform Addresses API
  slug: open-bitgo-addresses-api
- collection_type: open
  name: BitGo Platform Addresses Enterprise API
  slug: open-bitgo-enterprise-api
- collection_type: open
  name: BitGo Platform Addresses Keychains API
  slug: open-bitgo-keychains-api
- collection_type: open
  name: BitGo Platform Addresses Policies API
  slug: open-bitgo-policies-api
- collection_type: open
  name: BitGo Platform Addresses Staking API
  slug: open-bitgo-staking-api
- collection_type: open
  name: BitGo Platform Addresses Trading API
  slug: open-bitgo-trading-api
- collection_type: open
  name: BitGo Platform Addresses Transactions API
  slug: open-bitgo-transactions-api
- collection_type: open
  name: BitGo Platform Addresses Transfers API
  slug: open-bitgo-transfers-api
- collection_type: open
  name: BitGo Platform Addresses User API
  slug: open-bitgo-user-api
- collection_type: open
  name: BitGo Platform Addresses Wallets API
  slug: open-bitgo-wallets-api
- collection_type: open
  name: BitGo Platform Addresses Webhooks API
  slug: open-bitgo-webhooks-api
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
random_paper: 8
rate_limits:
- limit_count: 2
  name: Bitgo Rate Limits
  slug: bitgo-rate-limits
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
