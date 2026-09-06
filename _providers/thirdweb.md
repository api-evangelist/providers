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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Thirdweb Agentic Access
  operation_count: 42
  slug: thirdweb-agentic-access
  summary_line: 42 operations · 23 acting
api_count: 1
apis:
- baseURL: https://api.thirdweb.com
  baseurl_source: declared
  description: Wallet authentication flows.
  name: thirdweb Authentication API
  slug: thirdweb-authentication-api
- baseURL: https://api.thirdweb.com
  baseurl_source: declared
  description: Smart contract read, write, and deployment.
  name: thirdweb Contracts API
  slug: thirdweb-contracts-api
- baseURL: https://api.thirdweb.com
  baseurl_source: declared
  description: Backend transaction execution with server wallets.
  name: thirdweb Engine API
  slug: thirdweb-engine-api
- baseURL: https://api.thirdweb.com
  baseurl_source: declared
  description: Indexed on-chain events, transactions, tokens, and NFTs.
  name: thirdweb Insight API
  slug: thirdweb-insight-api
- baseURL: https://api.thirdweb.com
  baseurl_source: declared
  description: AI blockchain interface.
  name: thirdweb Nebula API
  slug: thirdweb-nebula-api
- baseURL: https://api.thirdweb.com
  baseurl_source: declared
  description: Bridge, swap, convert, onramp, and x402 payments.
  name: thirdweb Payments API
  slug: thirdweb-payments-api
- baseURL: https://api.thirdweb.com
  baseurl_source: declared
  description: Token creation, listing, and ownership.
  name: thirdweb Tokens API
  slug: thirdweb-tokens-api
- baseURL: https://api.thirdweb.com
  baseurl_source: declared
  description: Transaction submission and status.
  name: thirdweb Transactions API
  slug: thirdweb-transactions-api
- baseURL: https://api.thirdweb.com
  baseurl_source: declared
  description: User and server wallet management, signing, and transfers.
  name: thirdweb Wallets API
  slug: thirdweb-wallets-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: thirdweb Authentication API
  slug: open-thirdweb-authentication-api
- collection_type: open
  name: thirdweb Authentication Contracts API
  slug: open-thirdweb-contracts-api
- collection_type: open
  name: thirdweb Authentication Engine API
  slug: open-thirdweb-engine-api
- collection_type: open
  name: thirdweb Authentication Insight API
  slug: open-thirdweb-insight-api
- collection_type: open
  name: thirdweb Authentication Nebula API
  slug: open-thirdweb-nebula-api
- collection_type: open
  name: thirdweb Authentication Payments API
  slug: open-thirdweb-payments-api
- collection_type: open
  name: thirdweb Authentication Tokens API
  slug: open-thirdweb-tokens-api
- collection_type: open
  name: thirdweb Authentication Transactions API
  slug: open-thirdweb-transactions-api
- collection_type: open
  name: thirdweb Authentication Wallets API
  slug: open-thirdweb-wallets-api
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
random_paper: 17
rate_limits:
- limit_count: 6
  name: Thirdweb Rate Limits
  slug: thirdweb-rate-limits
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 49.4
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 35.9
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
