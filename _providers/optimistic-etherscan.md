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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Optimistic Etherscan Agentic Access
  operation_count: 1
  slug: optimistic-etherscan-agentic-access
  summary_line: 1 operation
api_count: 7
apis:
- description: Address balances, transaction lists, and token holdings on OP Mainnet
  name: Optimism Etherscan Accounts API
  slug: optimistic-etherscan-accounts-api
- description: Block rewards, countdowns, and block-to-timestamp lookups
  name: Optimism Etherscan Blocks API
  slug: optimistic-etherscan-blocks-api
- description: Smart contract source code, ABI, creation info, and verification
  name: Optimism Etherscan Contracts API
  slug: optimistic-etherscan-contracts-api
- description: Ethereum JSON-RPC proxy for direct node-level queries
  name: Optimism Etherscan Geth Proxy API
  slug: optimistic-etherscan-geth-proxy-api
- description: OP Mainnet network statistics, OP token supply, and gas oracle
  name: Optimism Etherscan Stats API
  slug: optimistic-etherscan-stats-api
- description: ERC-20 and ERC-721 token balances, supply, and holder lists
  name: Optimism Etherscan Tokens API
  slug: optimistic-etherscan-tokens-api
- description: Transaction execution status, receipts, and internal transactions
  name: Optimism Etherscan Transactions API
  slug: optimistic-etherscan-transactions-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/optimistic-etherscan-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/optimistic-etherscan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optimistic-etherscan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/optimistic-etherscan-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://optimistic.etherscan.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.optimism.etherscan.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://etherscan.io/apis
- group: commercial
  title: ''
  type: TermsOfService
  url: https://etherscan.io/apiterms
- group: start
  title: ''
  type: Signup
  url: https://optimistic.etherscan.io/myapikey
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.optimism.etherscan.io/support/rate-limits
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.etherscan.io/llms.txt
- group: start
  title: ''
  type: Sandbox
  url: https://docs.optimism.etherscan.io/optimism-sepolia-etherscan
created: '2026-06-13'
description: Optimism Etherscan is the official blockchain explorer and API platform for the Optimism L2 network (OP Mainnet, chain ID 10). It provides REST APIs for querying Optimism transactions, token events, smart contract source code, account balances, block data, and OP Mainnet statistics. API subscriptions have migrated to Etherscan API V2, enabling a single API key to access Optimism alongside 60+ EVM chains. The free tier covers select chains with 3 calls/second and 100,000 calls/day; paid plans start at $49/month for full multichain access.
finops:
- name: Optimistic Etherscan Finops
  service_category: API
  slug: optimistic-etherscan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optimistic-etherscan.png
jsonld:
- class_count: 0
  name: Optimistic Etherscan Context
  property_count: 39
  slug: optimistic-etherscan-context
layout: provider
modified: '2026-06-13'
name: Optimism Etherscan
nav: Providers
network: true
overview: 'Optimism Etherscan publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Blocks API, Contracts API, and 4 more. Tagged areas include Blockchain, Optimism, Layer 2, Ethereum, and EVM.


  The Optimism Etherscan catalog on APIs.io includes 1 JSON-LD context.


  Optimism Etherscan''s developer surface includes authentication, developer portal, documentation, pricing, signup flow, sandbox, and 6 more developer resources.'
plans:
- name: Optimistic Etherscan Plans Pricing
  plan_count: 7
  slug: optimistic-etherscan-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 13
  name: Optimistic Etherscan Rate Limits
  slug: optimistic-etherscan-rate-limits
score:
  band: developing
  composite: 50.9
  delta: 2.7
  facets:
    commercial_clarity: 73.7
    contract_quality: 67.9
    developer_ergonomics: 34.8
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Optimistic Etherscan Authentication
  slug: optimistic-etherscan-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Optimistic Etherscan Domain Security
  slug: optimistic-etherscan-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Optimistic Etherscan Vulnerability Disclosure
  slug: optimistic-etherscan-vulnerability-disclosure
  summary_line: disclosure policy published
slug: optimistic-etherscan
tags:
- Blockchain
- Optimism
- Layer 2
- Ethereum
- EVM
- Web3
- Cryptocurrency
website: https://optimistic.etherscan.io/
---
