---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
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
  score: 30.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Hiro Agentic Access
  operation_count: 154
  slug: hiro-agentic-access
  summary_line: 154 operations · 14 acting
api_count: 4
apis:
- description: REST API for Chainhook predicate registration and event streaming for Bitcoin and Stacks.
  name: Hiro Chainhooks API
  slug: chainhooks-api
- description: REST API to programmatically manage Hiro Platform devnets and chainhooks.
  name: Hiro Platform API
  slug: platform-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Read-only endpoints to obtain Stacks account details
  name: Hiro Accounts API
  slug: hiro-accounts-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Operations related to the Atlas global namespace.
  name: Hiro Atlas API
  slug: hiro-atlas-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: The Blocks API from Hiro — 37 operation(s) for blocks.
  name: Hiro Blocks API
  slug: hiro-blocks-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: The Blocks Proposals API from Hiro — 2 operation(s) for blocks proposals.
  name: Hiro Blocks Proposals API
  slug: hiro-blocks-proposals-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Read-only endpoints to obtain burn block details
  name: Hiro Burn Blocks API
  slug: hiro-burn-blocks-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Endpoints to request STX or BTC tokens (not possible on Mainnet)
  name: Hiro Faucets API
  slug: hiro-faucets-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Read-only endpoints to obtain fee details
  name: Hiro Fees API
  slug: hiro-fees-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: The Fungible Tokens API from Hiro — 1 operation(s) for fungible tokens.
  name: Hiro Fungible Tokens API
  slug: hiro-fungible-tokens-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Read-only endpoints to obtain network, Proof-of-Transfer, Stacking, STX token, and node information
  name: Hiro Info API
  slug: hiro-info-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Endpoints to obtain Mempool information
  name: Hiro Mempool API
  slug: hiro-mempool-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Read-only endpoints to obtain microblocks details
  name: Hiro Microblocks API
  slug: hiro-microblocks-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Endpoints related to Stacks block production and mining.
  name: Hiro Mining API
  slug: hiro-mining-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Read-only endpoints realted to the Blockchain Naming System on Stacks
  name: Hiro Names API
  slug: hiro-names-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Read-only endpoints to obtain non-fungible token details
  name: Hiro Non-Fungible Tokens API
  slug: hiro-non-fungible-tokens-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Endpoints to get information about the Proof of Transfer consensus mechanism
  name: Hiro Proof of Transfer API
  slug: hiro-proof-of-transfer-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Read-only endpoints to search for accounts, blocks, smart contracts, and transactions
  name: Hiro Search API
  slug: hiro-search-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: The Signers API from Hiro — 4 operation(s) for signers.
  name: Hiro Signers API
  slug: hiro-signers-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Read-only endpoints to obtain Clarity smart contract details
  name: Hiro Smart Contracts API
  slug: hiro-smart-contracts-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Endpoints for interacting with StackerDB instances.
  name: Hiro StackerDB API
  slug: hiro-stackerdb-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: The Stacking API from Hiro — 4 operation(s) for stacking.
  name: Hiro Stacking API
  slug: hiro-stacking-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Read-only endpoints to obtain Stacking reward details
  name: Hiro Stacking Rewards API
  slug: hiro-stacking-rewards-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Service status endpoints
  name: Hiro Status API
  slug: hiro-status-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Token metadata endpoints
  name: Hiro Tokens API
  slug: hiro-tokens-api
- baseURL: https://api.mainnet.hiro.so
  baseurl_source: declared
  description: Endpoints to obtain transaction details and to broadcast transactions to the network
  name: Hiro Transactions API
  slug: hiro-transactions-api
artifact_total: 57
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Signer Metrics Accounts API
  slug: open-hiro-accounts-api
- collection_type: open
  name: Signer Metrics Accounts Atlas API
  slug: open-hiro-atlas-api
- collection_type: open
  name: Signer Metrics Accounts Blocks API
  slug: open-hiro-blocks-api
- collection_type: open
  name: Signer Metrics Accounts Blocks Proposals API
  slug: open-hiro-blocks-proposals-api
- collection_type: open
  name: Signer Metrics Accounts Burn Blocks API
  slug: open-hiro-burn-blocks-api
- collection_type: open
  name: Signer Metrics Accounts Faucets API
  slug: open-hiro-faucets-api
- collection_type: open
  name: Signer Metrics Accounts Fees API
  slug: open-hiro-fees-api
- collection_type: open
  name: Signer Metrics Accounts Fungible Tokens API
  slug: open-hiro-fungible-tokens-api
- collection_type: open
  name: Signer Metrics Accounts Info API
  slug: open-hiro-info-api
- collection_type: open
  name: Signer Metrics Accounts Mempool API
  slug: open-hiro-mempool-api
- collection_type: open
  name: Signer Metrics Accounts Microblocks API
  slug: open-hiro-microblocks-api
- collection_type: open
  name: Signer Metrics Accounts Mining API
  slug: open-hiro-mining-api
- collection_type: open
  name: Signer Metrics Accounts Names API
  slug: open-hiro-names-api
- collection_type: open
  name: Signer Metrics Accounts Non-Fungible Tokens API
  slug: open-hiro-non-fungible-tokens-api
- collection_type: open
  name: Signer Metrics Accounts Proof of Transfer API
  slug: open-hiro-proof-of-transfer-api
- collection_type: open
  name: Signer Metrics Accounts Search API
  slug: open-hiro-search-api
- collection_type: open
  name: Signer Metrics Accounts Signers API
  slug: open-hiro-signers-api
- collection_type: open
  name: Signer Metrics Accounts Smart Contracts API
  slug: open-hiro-smart-contracts-api
- collection_type: open
  name: Signer Metrics Accounts StackerDB API
  slug: open-hiro-stackerdb-api
- collection_type: open
  name: Signer Metrics Accounts Stacking API
  slug: open-hiro-stacking-api
- collection_type: open
  name: Signer Metrics Accounts Stacking Rewards API
  slug: open-hiro-stacking-rewards-api
- collection_type: open
  name: Signer Metrics Accounts Status API
  slug: open-hiro-status-api
- collection_type: open
  name: Signer Metrics Accounts Tokens API
  slug: open-hiro-tokens-api
- collection_type: open
  name: Signer Metrics Accounts Transactions API
  slug: open-hiro-transactions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hiro-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hiro-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hiro-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hiro.so/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hirosystems
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hiro-systems
- group: company
  title: ''
  type: Website
  url: https://www.hiro.so/
- group: commercial
  title: ''
  type: Plans
  url: plans/hiro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hiro-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hiro-finops.yml
created: '2026-05-08'
description: Hiro builds developer tooling for Bitcoin and the Stacks layer. Provides REST APIs (Stacks Blockchain API, Token Metadata API, Signer Metrics API, Chainhooks API, Platform API), Stacks Node JSON-RPC, plus the Hiro Platform for managing devnets and chainhooks.
finops:
- name: Hiro Finops
  service_category: Web3
  slug: hiro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hiro.png
layout: provider
modified: '2026-05-08'
name: Hiro
nav: Providers
network: true
overview: 'Hiro publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Atlas API, Blocks API, and 21 more. Tagged areas include Web3, Blockchain, Bitcoin, Stacks, and sBTC.


  Hiro''s developer surface includes authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Hiro Plans Pricing
  plan_count: 3
  slug: hiro-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Hiro Rate Limits
  slug: hiro-rate-limits
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 48.0
    catalog_earned_first_party: 0.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 53.4
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hiro/refs/heads/main/screenshots/hiro-2026-06-20T182757.png
security:
- kind: authentication
  name: Hiro Authentication
  slug: hiro-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hiro Domain Security
  slug: hiro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hiro
tags:
- Web3
- Blockchain
- Bitcoin
- Stacks
- sBTC
- Indexing
website: https://www.hiro.so/
---
