---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Optimism Agentic Access
  operation_count: 1
  slug: optimism-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Public Ethereum JSON-RPC endpoint for OP Mainnet (chain ID 10). Supports standard eth_* methods plus Optimism extensions for L1 fee estimation, deposit tracking, and withdrawal proving. Public endpoin
  name: OP Mainnet JSON-RPC
  slug: mainnet-rpc
- description: Public Ethereum JSON-RPC endpoint for the OP Sepolia testnet (chain ID 11155420) used for development and integration testing.
  name: OP Sepolia JSON-RPC
  slug: sepolia-rpc
- description: Canonical cross-chain bridge for depositing and withdrawing ETH and ERC-20 tokens between Ethereum L1 and OP Mainnet, secured by the OP Stack StandardBridge contracts. Available as a hosted app and vi
  name: Optimism Bridge (Standard Bridge)
  slug: bridge
- description: Open-source, modular Ethereum L2 rollup stack. The monorepo at github.com/ethereum-optimism/optimism contains op-geth (execution), op-node (consensus), op-batcher, op-proposer, op-challenger, op-deplo
  name: OP Stack
  slug: op-stack
- description: Source-of-truth index of chains that are part of the Optimism Superchain — genesis files, deployment addresses, RPC endpoints, explorers, and chain metadata in machine-readable form.
  name: Superchain Registry
  slug: superchain-registry
- description: Modern Optimism SDK exposed as a Viem extension (viem/op-stack) for L1<->L2 message tracking, deposit and withdrawal flows, fee estimation, and Superchain multi-chain helpers.
  name: Optimism SDK (Viem extension)
  slug: viem-sdk
- description: Local Superchain simulator that spins up multiple OP Stack chains for developing and testing cross-chain interop messages (CrossL2Inbox / L2ToL2CrossDomainMessenger) before mainnet rollout.
  name: Supersim
  slug: supersim
- description: Etherscan-family block explorer for OP Mainnet and OP Sepolia with REST API access for contracts, transactions, and addresses.
  name: Optimism Etherscan
  slug: etherscan-explorer
- description: Open-source Blockscout block explorer for OP Mainnet with REST and GraphQL APIs.
  name: Optimism Blockscout
  slug: blockscout-explorer
- baseURL: https://mainnet.optimism.io
  baseurl_source: declared
  description: Standard Ethereum JSON-RPC method invocation.
  name: Optimism JSON-RPC API
  slug: optimism-json-rpc-api
artifact_total: 21
asyncapis:
- description: 'AsyncAPI 2.6 description of the WebSocket JSON-RPC subscription surface exposed by op-geth — the OP Stack execution client used by OP Mainnet (chain ID 10) and OP Sepolia (chain ID 11155420). ## Publi'
  name: Optimism (OP Stack) WebSocket JSON-RPC API
  slug: optimism-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OP Mainnet JSON-RPC API
  slug: open-optimism-json-rpc-api
- collection_type: open
  name: OP Mainnet JSON-RPC
  slug: open-optimism
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ethereum-optimism/optimism/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/ethereum-optimism/optimism/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/ethereum-optimism/optimism/blob/develop/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/ethereum-optimism/.github/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/ethereum-optimism/optimism/blob/develop/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/ethereum-optimism/optimism/blob/develop/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/optimism-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optimism-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.optimism.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.optimism.io
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ethereum-optimism
- group: other
  title: ''
  type: Specs
  url: https://specs.optimism.io
- group: start
  title: ''
  type: SuperchainRegistry
  url: https://github.com/ethereum-optimism/superchain-registry
- group: other
  title: ''
  type: Governance
  url: https://gov.optimism.io
- group: operate
  title: ''
  type: Status
  url: https://status.optimism.io
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Optimism
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/optimism
- group: company
  title: ''
  type: Blog
  url: https://blog.oplabs.co
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.optimism.io/llms.txt
created: '2026-05-23'
description: Optimism is an Ethereum Layer 2 scaling network and the originator of the OP Stack — an open-source, modular rollup framework that powers OP Mainnet and a growing Superchain of interoperable chains (Base, Mode, Zora, Worldchain, and others). Developers interact via standard Ethereum JSON-RPC, the Optimism (Viem-based) SDK, the canonical Optimism Bridge, OP Stack operator tooling (op-geth, op-node, op-deployer, op-batcher, op-proposer, op-challenger), and the Superchain Registry.
finops:
- name: Optimism Finops
  service_category: API
  slug: optimism-finops
graphqls:
- description: ''
  name: Optimism GraphQL API
  slug: optimism-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optimism.png
layout: provider
modified: '2026-05-29'
name: Optimism
nav: Providers
network: true
overview: 'Optimism publishes 3 APIs on the [APIs.io](https://apis.io/) network: OP Mainnet JSON-RPC, OP Sepolia JSON-RPC, and JSON-RPC API. Tagged areas include Layer 2, Ethereum, OP Stack, Superchain, and JSON-RPC.


  The Optimism catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Optimism''s developer surface includes documentation, GitHub presence, status page, engineering blog, and 15 more developer resources.'
plans:
- name: Optimism Plans Pricing
  plan_count: 1
  slug: optimism-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Optimism Rate Limits
  slug: optimism-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Optimism API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: optimism-asyncapi-spectral-rules
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 54.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 60.7
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 100.0
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optimism/refs/heads/main/screenshots/optimism-2026-06-20T191109.png
security:
- kind: domain-security
  name: Optimism Domain Security
  slug: optimism-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: optimism
tags:
- Layer 2
- Ethereum
- OP Stack
- Superchain
- JSON-RPC
- Rollup
- Bridge
website: https://www.optimism.io
---
