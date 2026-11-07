---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.0
  scored_at: '2026-11-06'
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
artifact_total: 20
asyncapis:
- description: 'AsyncAPI 2.6 description of the WebSocket JSON-RPC subscription surface exposed by op-geth — the OP Stack execution client used by OP Mainnet (chain ID 10) and OP Sepolia (chain ID 11155420). ## Publi'
  name: Optimism (OP Stack) WebSocket JSON-RPC API
  slug: optimism-asyncapi
collections:
- collection_type: open
  name: OP Mainnet JSON-RPC API
  slug: open-optimism-json-rpc-api
- collection_type: open
  name: OP Mainnet JSON-RPC
  slug: open-optimism
common:
- group: commercial
  href: https://artifacts.apis.io/optimism/plans/optimism-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/optimism-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/optimism/rate-limits/optimism-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/optimism-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/optimism/finops/optimism-finops.yml
  title: ''
  type: FinOps
  url: finops/optimism-finops.yml
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
  href: https://artifacts.apis.io/optimism/agentic-access/optimism-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/optimism-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/optimism/security/optimism-domain-security.yml
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
- has_sources: false
  method: generated
  name: Optimism Finops
  primary_unit: ''
  service_category: API
  slug: optimism-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optimism.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.optimism.io over HTTP; 3 tools listed.
  name: Optimism MCP Server
  slug: optimism
modified: '2026-05-29'
name: Optimism
nav: Providers
network: true
overview: 'Optimism publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including OP Mainnet JSON-RPC, OP Sepolia JSON-RPC, JSON-RPC API, and 7 more. Tagged areas include Layer 2, Ethereum, OP Stack, Superchain, and JSON-RPC.


  The Optimism catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Optimism''s developer surface includes documentation, GitHub presence, status page, engineering blog, and 18 more developer resources.'
plans:
- name: Optimism Plans Pricing
  plan_count: 1
  slug: optimism-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Optimism Rate Limits
  slug: optimism-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Optimism — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: optimism-asyncapi-spectral-rules
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 55.9
    developer_ergonomics: 16.7
    discoverability: 75.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/optimism/optimism-2026-06-20T191109.png
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
- Optimism
- Real-Time
website: https://www.optimism.io
---
