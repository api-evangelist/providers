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
- acting_count: 14
  human_in_the_loop: 0
  name: Hiro Agentic Access
  operation_count: 154
  slug: hiro-agentic-access
  summary_line: 154 operations · 14 acting
api_count: 26
apis:
- description: REST API for Chainhook predicate registration and event streaming for Bitcoin and Stacks.
  name: Hiro Chainhooks API
  slug: chainhooks-api
- description: REST API to programmatically manage Hiro Platform devnets and chainhooks.
  name: Hiro Platform API
  slug: platform-api
- description: Read-only endpoints to obtain Stacks account details
  name: Hiro Accounts API
  slug: hiro-accounts-api
- description: Operations related to the Atlas global namespace.
  name: Hiro Atlas API
  slug: hiro-atlas-api
- description: The Blocks API from Hiro — 37 operation(s) for blocks.
  name: Hiro Blocks API
  slug: hiro-blocks-api
- description: The Blocks Proposals API from Hiro — 2 operation(s) for blocks proposals.
  name: Hiro Blocks Proposals API
  slug: hiro-blocks-proposals-api
- description: Read-only endpoints to obtain burn block details
  name: Hiro Burn Blocks API
  slug: hiro-burn-blocks-api
- description: Endpoints to request STX or BTC tokens (not possible on Mainnet)
  name: Hiro Faucets API
  slug: hiro-faucets-api
- description: Read-only endpoints to obtain fee details
  name: Hiro Fees API
  slug: hiro-fees-api
- description: The Fungible Tokens API from Hiro — 1 operation(s) for fungible tokens.
  name: Hiro Fungible Tokens API
  slug: hiro-fungible-tokens-api
- description: Read-only endpoints to obtain network, Proof-of-Transfer, Stacking, STX token, and node information
  name: Hiro Info API
  slug: hiro-info-api
- description: Endpoints to obtain Mempool information
  name: Hiro Mempool API
  slug: hiro-mempool-api
- description: Read-only endpoints to obtain microblocks details
  name: Hiro Microblocks API
  slug: hiro-microblocks-api
- description: Endpoints related to Stacks block production and mining.
  name: Hiro Mining API
  slug: hiro-mining-api
- description: Read-only endpoints realted to the Blockchain Naming System on Stacks
  name: Hiro Names API
  slug: hiro-names-api
- description: Read-only endpoints to obtain non-fungible token details
  name: Hiro Non-Fungible Tokens API
  slug: hiro-non-fungible-tokens-api
- description: Endpoints to get information about the Proof of Transfer consensus mechanism
  name: Hiro Proof of Transfer API
  slug: hiro-proof-of-transfer-api
- description: Read-only endpoints to search for accounts, blocks, smart contracts, and transactions
  name: Hiro Search API
  slug: hiro-search-api
- description: The Signers API from Hiro — 4 operation(s) for signers.
  name: Hiro Signers API
  slug: hiro-signers-api
- description: Read-only endpoints to obtain Clarity smart contract details
  name: Hiro Smart Contracts API
  slug: hiro-smart-contracts-api
- description: Endpoints for interacting with StackerDB instances.
  name: Hiro StackerDB API
  slug: hiro-stackerdb-api
- description: The Stacking API from Hiro — 4 operation(s) for stacking.
  name: Hiro Stacking API
  slug: hiro-stacking-api
- description: Read-only endpoints to obtain Stacking reward details
  name: Hiro Stacking Rewards API
  slug: hiro-stacking-rewards-api
- description: Service status endpoints
  name: Hiro Status API
  slug: hiro-status-api
- description: Token metadata endpoints
  name: Hiro Tokens API
  slug: hiro-tokens-api
- description: Endpoints to obtain transaction details and to broadcast transactions to the network
  name: Hiro Transactions API
  slug: hiro-transactions-api
artifact_total: 32
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
random_paper: 26
rate_limits:
- limit_count: 2
  name: Hiro Rate Limits
  slug: hiro-rate-limits
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.4
    developer_ergonomics: 13.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.5
  schema_version: 0.5
  scored_at: '2026-07-27'
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
