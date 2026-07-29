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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bscscan Agentic Access
  operation_count: 71
  slug: bscscan-agentic-access
  summary_line: 71 operations · 1 acting
api_count: 10
apis:
- description: The Accounts API from BscScan — 12 operation(s) for accounts.
  name: BscScan Accounts API
  slug: bscscan-accounts-api
- description: The API PRO Endpoints API from BscScan — 20 operation(s) for api pro endpoints.
  name: BscScan API PRO Endpoints API
  slug: bscscan-api-pro-endpoints-api
- description: The Blocks API from BscScan — 8 operation(s) for blocks.
  name: BscScan Blocks API
  slug: bscscan-blocks-api
- description: The Contracts API from BscScan — 5 operation(s) for contracts.
  name: BscScan Contracts API
  slug: bscscan-contracts-api
- description: The Gas Tracker API from BscScan — 5 operation(s) for gas tracker.
  name: BscScan Gas Tracker API
  slug: bscscan-gas-tracker-api
- description: The Geth/Parity Proxy API from BscScan — 14 operation(s) for geth/parity proxy.
  name: BscScan Geth/Parity Proxy API
  slug: bscscan-geth-parity-proxy-api
- description: The Logs API from BscScan — 3 operation(s) for logs.
  name: BscScan Logs API
  slug: bscscan-logs-api
- description: The Stats API from BscScan — 13 operation(s) for stats.
  name: BscScan Stats API
  slug: bscscan-stats-api
- description: The Tokens API from BscScan — 9 operation(s) for tokens.
  name: BscScan Tokens API
  slug: bscscan-tokens-api
- description: The Transactions API from BscScan — 2 operation(s) for transactions.
  name: BscScan Transactions API
  slug: bscscan-transactions-api
artifact_total: 26
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bscscan-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bscscan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bscscan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bscscan-authentication.yml
created: '2026-06-13'
description: BscScan is the leading block explorer and analytics platform for BNB Smart Chain (BSC), providing a REST API for querying transactions, token transfers, smart contract ABIs, gas prices, BEP-20 token information, and on-chain statistics. API subscriptions are now unified under the Etherscan V2 platform, enabling access to 60+ EVM chains via a single API key using the chainid parameter (BSC chainid=56).
examples:
- key_count: 3
  name: Account Balance
  slug: account-balance
- key_count: 3
  name: Gas Oracle
  slug: gas-oracle
- key_count: 3
  name: Token Transfer
  slug: token-transfer
- key_count: 3
  name: Transaction List
  slug: transaction-list
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://bscscan.com/images/svg/brands/bscscan-logo-circle.svg
json_schemas:
- name: BscScan Account Balance Response
  property_count: 3
  slug: account-balance
- name: BscScan BEP-20 Token Transfer Event
  property_count: 18
  slug: token-transfer
- name: BscScan Transaction
  property_count: 20
  slug: transaction
jsonld:
- class_count: 0
  name: context Context
  property_count: 36
  slug: context
layout: provider
modified: '2026-06-13'
name: BscScan
nav: Providers
network: true
overview: 'BscScan publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, API PRO Endpoints API, Blocks API, and 7 more. Tagged areas include blockchain, block-explorer, BNB Smart Chain, BSC, and BEP-20.


  The BscScan catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BscScan''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Plans
  plan_count: 7
  slug: plans
random_paper: 4
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: BscScan API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bscscan-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.5
  delta: -4.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.9
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Bscscan Authentication
  slug: bscscan-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bscscan Domain Security
  slug: bscscan-domain-security
  summary_line: TLSv1.3 · DNSSEC
- kind: vulnerability-disclosure
  name: Bscscan Vulnerability Disclosure
  slug: bscscan-vulnerability-disclosure
  summary_line: disclosure policy published
slug: bscscan
tags:
- blockchain
- block-explorer
- BNB Smart Chain
- BSC
- BEP-20
- transactions
- smart-contracts
- DeFi
- EVM
---
