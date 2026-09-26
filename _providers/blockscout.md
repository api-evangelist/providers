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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-09-25'
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
artifact_total: 42
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
- group: company
  title: ''
  type: Website
  url: https://www.blockscout.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blockscout/refs/heads/main/agentic-access/blockscout-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blockscout-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.blockscout.com/mcp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blockscout/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blockscout/refs/heads/main/finops/blockscout-x402.yml
  title: ''
  type: x402
  url: finops/blockscout-x402.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blockscout/refs/heads/main/security/blockscout-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/blockscout/refs/heads/main/plans/blockscout-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blockscout-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/blockscout/refs/heads/main/rate-limits/blockscout-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/blockscout-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/blockscout/refs/heads/main/finops/blockscout-finops.yml
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
- name: Blockscout X402
  service_category: ''
  slug: blockscout-x402
graphqls:
- description: GraphQL API exposing blocks, transactions, addresses, and tokens.
  name: Blockscout GraphQL API
  slug: blockscout-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blockscout.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-08'
name: Blockscout
nav: Providers
network: true
overview: 'Blockscout publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Blocks API, CelestiaService API, and 15 more. Tagged areas include Blockscout, Web3, Explorer, Open Source, and EVM.


  Blockscout''s developer surface includes developer portal, documentation, GitHub presence, engineering blog, and 12 more developer resources.'
plans:
- name: Blockscout Plans Pricing
  plan_count: 4
  slug: blockscout-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Blockscout Rate Limits
  slug: blockscout-rate-limits
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 41.2
    developer_ergonomics: 28.6
    discoverability: 75.0
    operational_transparency: 13.2
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/blockscout/refs/heads/main/screenshots/blockscout-2026-06-20T173404.png
security:
- kind: domain-security
  name: Blockscout Domain Security
  slug: blockscout-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: blockscout
tags:
- Blockscout
- Web3
- Explorer
- Open Source
- EVM
- Multi-Chain
- GraphQL
- REST
- Etherscan-Compatible
- MCP
- Agent Skills
- x402
- Agent-Native
website: https://www.blockscout.com/
---
