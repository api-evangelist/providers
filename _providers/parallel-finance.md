---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Substrate/Polkadot JSON-RPC interface to the Parallel Finance parachain, accessed over WebSocket with the polkadot.js API and Parallel's @parallel-finance/api SDK. Exposes chain state, extrinsics (len
  name: Parallel Finance JSON-RPC (polkadot.js)
  slug: parallel-finance-json-rpc-polkadotjs
artifact_total: 2
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/parallel-finance/parallel-js/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/parallel-finance/parallel-js/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parallel-finance-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parallel-finance
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/parallel-finance/parallel
- group: build
  title: ''
  type: Packages
  url: packages/parallel-finance-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/parallel-finance-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/parallel-finance-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parallel-finance-llms.txt
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ParallelFi
created: '2026-07-17'
description: Parallel Finance is a decentralized money-market protocol built on the Polkadot ecosystem, offering lending, staking, and borrowing where depositors can lend and stake simultaneously to earn combined yield and borrowers can post collateral to borrow. It runs as a Substrate/Polkadot parachain (Parallel mainnet and the Heiko canary network on Kusama). Rather than a REST API, developers integrate through a JSON-RPC node over WebSocket (wss://rpc.parallel.fi) using polkadot.js, aided by Parallel's first-party @parallel-finance TypeScript SDK packages on npm that supply the chain types, RPC definitions, and connection options. Source, chain specs, and the auction toolkit are published under the parallel-finance GitHub organization.
image: https://avatars.githubusercontent.com/u/79623569?v=4
layout: provider
modified: '2026-07-20'
name: Parallel Finance
nav: Providers
network: true
overview: Parallel Finance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DeFi, Blockchain, Polkadot, and Lending.
random_paper: 18
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  open_source:
    applies: true
    score: 0.0
  previous_composite: 8.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parallel-finance/refs/heads/main/screenshots/parallel-finance-2026-08-07T191423.png
security:
- kind: domain-security
  name: Parallel Finance Domain Security
  slug: parallel-finance-domain-security
  summary_line: DNSSEC · DMARC
slug: parallel-finance
tags:
- Company
- DeFi
- Blockchain
- Polkadot
- Lending
- Staking
- Money Market
- Substrate
- Web3
- Cryptocurrency
---
