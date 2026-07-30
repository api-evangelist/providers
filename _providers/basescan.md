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
  name: Basescan Agentic Access
  operation_count: 71
  slug: basescan-agentic-access
  summary_line: 71 operations · 1 acting
api_count: 10
apis:
- description: The Accounts API from Basescan — 12 operation(s) for accounts.
  name: Basescan Accounts API
  slug: basescan-accounts-api
- description: The API PRO Endpoints API from Basescan — 20 operation(s) for api pro endpoints.
  name: Basescan API PRO Endpoints API
  slug: basescan-api-pro-endpoints-api
- description: The Blocks API from Basescan — 8 operation(s) for blocks.
  name: Basescan Blocks API
  slug: basescan-blocks-api
- description: The Contracts API from Basescan — 5 operation(s) for contracts.
  name: Basescan Contracts API
  slug: basescan-contracts-api
- description: The Gas Tracker API from Basescan — 5 operation(s) for gas tracker.
  name: Basescan Gas Tracker API
  slug: basescan-gas-tracker-api
- description: The Geth/Parity Proxy API from Basescan — 14 operation(s) for geth/parity proxy.
  name: Basescan Geth/Parity Proxy API
  slug: basescan-geth-parity-proxy-api
- description: The Logs API from Basescan — 3 operation(s) for logs.
  name: Basescan Logs API
  slug: basescan-logs-api
- description: The Stats API from Basescan — 13 operation(s) for stats.
  name: Basescan Stats API
  slug: basescan-stats-api
- description: The Tokens API from Basescan — 9 operation(s) for tokens.
  name: Basescan Tokens API
  slug: basescan-tokens-api
- description: The Transactions API from Basescan — 2 operation(s) for transactions.
  name: Basescan Transactions API
  slug: basescan-transactions-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/basescan-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/basescan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/basescan-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://basescan.org/myapikey
- group: commercial
  title: ''
  type: Plans
  url: https://etherscan.io/apis?id=8453
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://etherscan.io/privacyPolicy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://etherscan.io/terms
- group: company
  title: ''
  type: Blog
  url: https://info.basescan.org
- group: operate
  title: ''
  type: Support
  url: https://info.basescan.org
created: '2026-06-13'
description: Base L2 blockchain explorer with a REST API for querying Base network transactions, token balances, smart contract ABIs, ERC-20 transfer events, gas prices, and block data. Powered by the Etherscan team and migrated to the unified Etherscan API V2 platform, enabling access to 50+ EVM chains with a single API key using chain ID 8453 for Base.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://basescan.org/images/brandassets/basescan-logo-circle.png
jsonld:
- class_count: 0
  name: Apis Io Context
  property_count: 0
  slug: apis-io
layout: provider
modified: '2026-06-13'
name: Basescan
nav: Providers
network: true
overview: 'Basescan publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, API PRO Endpoints API, Blocks API, and 7 more. Tagged areas include blockchain, Base, L2, explorer, and Ethereum.


  The Basescan catalog on APIs.io includes 1 JSON-LD context.


  Basescan''s developer surface includes authentication, engineering blog, support, and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 7
  slug: plans
random_paper: 12
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 38.7
  delta: -2.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 62.7
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 40.9
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
  name: Basescan Authentication
  slug: basescan-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Basescan Domain Security
  slug: basescan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: basescan
tags:
- blockchain
- Base
- L2
- explorer
- Ethereum
- EVM
- transactions
- tokens
- smart contracts
---
