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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Blockscout Agentic Access
  operation_count: 57
  slug: blockscout-agentic-access
  summary_line: 57 operations · 1 acting
api_count: 1
apis:
- description: Recommended REST API on each Blockscout instance. Endpoints cover blocks, transactions, addresses, tokens, smart-contract verification, and more. Path varies by chain (eth, optimism, base, etc.). Free
  name: Blockscout REST API v2
  slug: rest-api-v2
- description: GraphQL API exposing blocks, transactions, addresses, and tokens.
  name: Blockscout GraphQL API
  slug: graphql-api
- description: Drop-in Etherscan-style RPC API (action / module query parameters) for easy migration.
  name: Blockscout Etherscan-Compatible API
  slug: etherscan-compatible-api
- description: Hosted multi-chain Blockscout API with unified routes, plans, and credit-based metering. Replaces the older MyAccount API; old keys do not work on PRO routes.
  name: Blockscout PRO API
  slug: pro-api
- baseURL: https://eth.blockscout.com/api/v2
  baseurl_source: declared
  description: The Addresses API from Blockscout — 15 operation(s) for addresses.
  name: Blockscout Addresses API
  slug: blockscout-addresses-api
- baseURL: https://eth.blockscout.com/api/v2
  baseurl_source: declared
  description: The Blocks API from Blockscout — 4 operation(s) for blocks.
  name: Blockscout Blocks API
  slug: blockscout-blocks-api
- baseURL: https://eth.blockscout.com/api/v2
  baseurl_source: declared
  description: The CelestiaService API from Blockscout — 3 operation(s) for celestiaservice.
  name: Blockscout CelestiaService API
  slug: blockscout-celestiaservice-api
- baseURL: https://eth.blockscout.com/api/v2
  baseurl_source: declared
  description: The Config API from Blockscout — 1 operation(s) for config.
  name: Blockscout Config API
  slug: blockscout-config-api
- baseURL: https://eth.blockscout.com/api/v2
  baseurl_source: declared
  description: The Internal Transactions API from Blockscout — 1 operation(s) for internal transactions.
  name: Blockscout Internal Transactions API
  slug: blockscout-internal-transactions-api
- baseURL: https://eth.blockscout.com/api/v2
  baseurl_source: declared
  description: The Main Page API from Blockscout — 3 operation(s) for main page.
  name: Blockscout Main Page API
  slug: blockscout-main-page-api
- baseURL: https://eth.blockscout.com/api/v2
  baseurl_source: declared
  description: The Proxy API from Blockscout — 1 operation(s) for proxy.
  name: Blockscout Proxy API
  slug: blockscout-proxy-api
- baseURL: https://eth.blockscout.com/api/v2
  baseurl_source: declared
  description: The Search API from Blockscout — 2 operation(s) for search.
  name: Blockscout Search API
  slug: blockscout-search-api
- baseURL: https://eth.blockscout.com/api/v2
  baseurl_source: declared
  description: The Smart Contracts API from Blockscout — 3 operation(s) for smart contracts.
  name: Blockscout Smart Contracts API
  slug: blockscout-smart-contracts-api
- baseURL: https://eth.blockscout.com/api/v2
  baseurl_source: declared
  description: The Stats API from Blockscout — 3 operation(s) for stats.
  name: Blockscout Stats API
  slug: blockscout-stats-api
- baseURL: https://eth.blockscout.com/api/v2
  baseurl_source: declared
  description: The Token Transfers API from Blockscout — 1 operation(s) for token transfers.
  name: Blockscout Token Transfers API
  slug: blockscout-token-transfers-api
- baseURL: https://eth.blockscout.com/api/v2
  baseurl_source: declared
  description: The Tokens API from Blockscout — 11 operation(s) for tokens.
  name: Blockscout Tokens API
  slug: blockscout-tokens-api
- baseURL: https://eth.blockscout.com/api/v2
  baseurl_source: declared
  description: The Transactions API from Blockscout — 8 operation(s) for transactions.
  name: Blockscout Transactions API
  slug: blockscout-transactions-api
- baseURL: https://eth.blockscout.com/api/v2
  baseurl_source: declared
  description: The Withdrawals API from Blockscout — 1 operation(s) for withdrawals.
  name: Blockscout Withdrawals API
  slug: blockscout-withdrawals-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BlockScout Addresses API
  slug: open-blockscout-addresses-api
- collection_type: open
  name: BlockScout Addresses Blocks API
  slug: open-blockscout-blocks-api
- collection_type: open
  name: BlockScout Addresses CelestiaService API
  slug: open-blockscout-celestiaservice-api
- collection_type: open
  name: BlockScout Addresses Config API
  slug: open-blockscout-config-api
- collection_type: open
  name: BlockScout Addresses Internal Transactions API
  slug: open-blockscout-internal-transactions-api
- collection_type: open
  name: BlockScout Addresses Main Page API
  slug: open-blockscout-main-page-api
- collection_type: open
  name: BlockScout Addresses Proxy API
  slug: open-blockscout-proxy-api
- collection_type: open
  name: BlockScout Addresses Search API
  slug: open-blockscout-search-api
- collection_type: open
  name: BlockScout Addresses Smart Contracts API
  slug: open-blockscout-smart-contracts-api
- collection_type: open
  name: BlockScout Addresses Stats API
  slug: open-blockscout-stats-api
- collection_type: open
  name: BlockScout Addresses Token Transfers API
  slug: open-blockscout-token-transfers-api
- collection_type: open
  name: BlockScout Addresses Tokens API
  slug: open-blockscout-tokens-api
- collection_type: open
  name: BlockScout Addresses Transactions API
  slug: open-blockscout-transactions-api
- collection_type: open
  name: BlockScout Addresses Withdrawals API
  slug: open-blockscout-withdrawals-api
- collection_type: open
  name: BlockScout API
  slug: open-blockscout
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blockscout-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blockscout-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blockscout
- group: start
  title: ''
  type: Portal
  url: https://www.blockscout.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockscout.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.blockscout.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/blockscout
- group: commercial
  title: ''
  type: Plans
  url: plans/blockscout-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/blockscout-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/blockscout-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://dev.blockscout.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.blog.blockscout.com/rss/
created: '2026-05-08'
description: Blockscout is an open-source EVM blockchain explorer covering 1,000+ L1, L2, and L3 EVM chains. Each Blockscout instance exposes a REST v1 API (legacy), REST v2 API (recommended), GraphQL API, and an Etherscan-compatible API. The hosted Blockscout PRO API at dev.blockscout.com provides multi-chain access with unified routes, plans, and credit-based metering.
finops:
- name: Blockscout Finops
  service_category: Crypto Explorer
  slug: blockscout-finops
graphqls:
- description: GraphQL API exposing blocks, transactions, addresses, and tokens.
  name: Blockscout GraphQL API
  slug: blockscout-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blockscout.png
layout: provider
modified: '2026-05-08'
name: Blockscout
nav: Providers
network: true
overview: 'Blockscout publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Blocks API, CelestiaService API, and 11 more. Tagged areas include Web3, Explorer, Open-Source, EVM, and Multi-Chain.


  Blockscout''s developer surface includes developer portal, documentation, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Blockscout Plans Pricing
  plan_count: 4
  slug: blockscout-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Blockscout Rate Limits
  slug: blockscout-rate-limits
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 45.5
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 28.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blockscout/refs/heads/main/screenshots/blockscout-2026-06-20T173404.png
security:
- kind: domain-security
  name: Blockscout Domain Security
  slug: blockscout-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: blockscout
tags:
- Web3
- Explorer
- Open-Source
- EVM
- Multi-Chain
- GraphQL
- REST
- Etherscan-Compatible
website: https://dev.blockscout.com/
---
