---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
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
  score: 27.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 52
  human_in_the_loop: 0
  name: Solana Agentic Access
  operation_count: 52
  slug: solana-agentic-access
  summary_line: 52 operations · 52 acting
api_count: 1
apis:
- description: SPL Token-oriented JSON-RPC methods for the Solana blockchain. Provides getTokenAccountBalance to return the token balance for an SPL Token account, getTokenAccountsByDelegate to find accounts with ma
  name: Solana RPC Tokens API
  slug: solana-rpc-tokens-api
- description: Transaction-oriented JSON-RPC methods for the Solana blockchain. Includes sendTransaction to submit a signed transaction to the network, simulateTransaction to test a transaction without broadcasting,
  name: Solana RPC Transactions API
  slug: solana-rpc-transactions-api
- description: Block and slot-oriented JSON-RPC methods for the Solana blockchain. Includes getBlock to retrieve a confirmed block at a given slot, getBlockCommitment for commitment level of a slot, getBlockHeight f
  name: Solana RPC Blocks API
  slug: solana-rpc-blocks-api
- description: Cluster and validator-oriented JSON-RPC methods for the Solana network. Includes getClusterNodes for the list of nodes in the cluster, getEpochInfo and getEpochSchedule for epoch data, getGenesisHash,
  name: Solana RPC Cluster API
  slug: solana-rpc-cluster-api
- description: Economics and staking-oriented JSON-RPC methods for the Solana blockchain. Includes getInflationGovernor to retrieve current inflation parameters, getInflationRate for the specific inflation values fo
  name: Solana RPC Economics API
  slug: solana-rpc-economics-api
- description: Real-time WebSocket subscription API for the Solana blockchain. Provides event-driven notifications for accounts (accountSubscribe, programSubscribe), transactions (logsSubscribe, signatureSubscribe),
  name: Solana RPC WebSocket Subscriptions API
  slug: solana-rpc-websocket-api
- description: Methods for querying account state, balances, and program ownership
  name: Solana Accounts API
  slug: solana-accounts-api
- description: Methods for querying blocks, slots, and ledger information
  name: Solana Blocks API
  slug: solana-blocks-api
- description: Methods for querying cluster nodes, validators, and network state
  name: Solana Cluster API
  slug: solana-cluster-api
- description: Methods for querying inflation, staking, and supply information
  name: Solana Economics API
  slug: solana-economics-api
- description: Methods for querying SPL Token accounts, balances, and supply
  name: Solana Tokens API
  slug: solana-tokens-api
- description: Methods for sending, simulating, and querying transactions
  name: Solana Transactions API
  slug: solana-transactions-api
arazzos:
- description: Read an account's size and lamports, then look up the rent-exempt minimum for that size.
  name: Solana Check Whether an Account Is Rent Exempt
  slug: solana-account-rent-exemption-workflow
- description: List an address's recent transaction signatures and expand the newest one into full detail.
  name: Solana Page an Address's Transaction History
  slug: solana-address-transaction-history-workflow
- description: Resolve the current slot, fetch its block, and read the block's timestamp and commitment.
  name: Solana Inspect a Confirmed Block at the Current Slot
  slug: solana-block-inspection-workflow
- description: Probe an RPC node's health, version, current slot, epoch position, and block height.
  name: Solana Run a Cluster Health and Readiness Check
  slug: solana-cluster-health-check-workflow
- description: Check node health, record a balance, request an airdrop, confirm it, and verify the balance moved.
  name: Solana Request a Devnet Airdrop and Confirm Funding
  slug: solana-devnet-airdrop-workflow
- description: Fetch a blockhash, price a message, sample recent priority fees, and re-check blockhash validity.
  name: Solana Estimate Transaction Fees and Priority Fees
  slug: solana-fee-estimation-workflow
- description: Read epoch position and schedule, fetch the leader schedule, and identify the current and upcoming leaders.
  name: Solana Resolve the Current Epoch's Leader Schedule
  slug: solana-leader-schedule-workflow
- description: Find the node's earliest available block and minimum retained slot, then walk a page of blocks.
  name: Solana Discover the Available Ledger Range and Backfill Blocks
  slug: solana-ledger-backfill-range-workflow
- description: Pull recent performance samples, the running transaction count, block production, and the node list.
  name: Solana Sample Network Performance and Block Production
  slug: solana-network-performance-workflow
- description: Read total and circulating supply, profile the largest accounts, and read inflation and staking floors.
  name: Solana Snapshot Network Supply and Staking Economics
  slug: solana-network-supply-economics-workflow
- description: Read a node's identity, genesis hash, version, snapshot slots, and shred-processing high-water marks.
  name: Solana Identify a Node and Its Cluster and Snapshot State
  slug: solana-node-identity-snapshot-workflow
- description: Verify an address is an executable program, list the accounts it owns, and batch-read the first of them.
  name: Solana Scan a Program's Owned Accounts
  slug: solana-program-accounts-scan-workflow
- description: Fetch a blockhash, simulate a signed transaction, send it, poll to finality, and read it back.
  name: Solana Submit a Transaction and Confirm It
  slug: solana-send-transaction-lifecycle-workflow
- description: List the token accounts a delegate can spend from, resolve one balance, and inspect the account.
  name: Solana Audit Token Accounts Delegated to an Address
  slug: solana-token-delegate-audit-workflow
- description: Read a mint's total supply, list its 20 largest token accounts, and inspect the top holder.
  name: Solana Analyze an SPL Token Mint and Its Largest Holders
  slug: solana-token-mint-analytics-workflow
- description: Read the current epoch, list current and delinquent vote accounts, and resolve inflation rewards.
  name: Solana Audit Validator Vote Accounts and Inflation Rewards
  slug: solana-validator-rewards-workflow
- description: Read a wallet's lamport balance, enumerate its SPL Token accounts, and price one token account.
  name: Solana Snapshot a Wallet's SOL and SPL Token Holdings
  slug: solana-wallet-portfolio-workflow
artifact_total: 67
collections:
- collection_type: postman
  name: Solana JSON-RPC Accounts API
  slug: postman-solana-accounts-api
- collection_type: postman
  name: Solana JSON-RPC Accounts Blocks API
  slug: postman-solana-blocks-api
- collection_type: postman
  name: Solana JSON-RPC Accounts Cluster API
  slug: postman-solana-cluster-api
- collection_type: postman
  name: Solana JSON-RPC Accounts Economics API
  slug: postman-solana-economics-api
- collection_type: postman
  name: Solana JSON-RPC Accounts Tokens API
  slug: postman-solana-tokens-api
- collection_type: postman
  name: Solana JSON-RPC Accounts Transactions API
  slug: postman-solana-transactions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Solana JSON-RPC Accounts API
  slug: open-solana-accounts-api
- collection_type: open
  name: Solana JSON-RPC Accounts Blocks API
  slug: open-solana-blocks-api
- collection_type: open
  name: Solana JSON-RPC Accounts Cluster API
  slug: open-solana-cluster-api
- collection_type: open
  name: Solana JSON-RPC Accounts Economics API
  slug: open-solana-economics-api
- collection_type: open
  name: Solana JSON-RPC Accounts Tokens API
  slug: open-solana-tokens-api
- collection_type: open
  name: Solana JSON-RPC Accounts Transactions API
  slug: open-solana-transactions-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/anza-xyz/kit/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/anza-xyz/kit/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/anza-xyz/kit/blob/main/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/anza-xyz/kit/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/anza-xyz/kit/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/solana/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/solana-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solana-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://solana.com/
- group: start
  title: ''
  type: Portal
  url: https://solana.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://solana.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://solana.com/docs/intro/quick-start
- group: other
  title: Solana RPC Overview
  type: RPC
  url: https://solana.com/docs/rpc
- group: auth
  title: Public endpoints require no API key; private RPC providers require API keys
  type: Authentication
  url: https://solana.com/docs/rpc
- group: auth
  title: ''
  type: Authentication
  url: authentication/solana-authentication.yml
- group: build
  title: Official JavaScript/TypeScript SDKs
  type: SDKs
  url: https://solana.com/docs/clients/official/javascript
- group: build
  title: '@solana/kit (Recommended TypeScript SDK)'
  type: SDKs
  url: https://www.npmjs.com/package/@solana/kit
- group: build
  title: '@solana/web3.js (Legacy TypeScript SDK)'
  type: SDKs
  url: https://www.npmjs.com/package/@solana/web3.js
- group: build
  title: '@solana/client (Headless Runtime)'
  type: SDKs
  url: https://www.npmjs.com/package/@solana/client
- group: build
  title: '@solana/react-hooks (React Integration)'
  type: SDKs
  url: https://www.npmjs.com/package/@solana/react-hooks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solana-labs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solana-foundation
- group: build
  title: '@solana/kit SDK Repository'
  type: GitHubRepository
  url: https://github.com/anza-xyz/kit
- group: build
  title: '@solana/web3.js SDK Repository'
  type: GitHubRepository
  url: https://github.com/solana-foundation/solana-web3.js
- group: operate
  title: ''
  type: StatusPage
  url: https://status.solana.com/
- group: operate
  title: Solana Changelog
  type: ChangeLog
  url: https://solanacompass.com/learn/Changelog
- group: company
  title: ''
  type: Blog
  url: https://solana.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://solana.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://solana.com/privacy-policy
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/solana-rpc-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/solana-plans.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/solana-finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/solana-rpc-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/solana-rpc-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/solana-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/solana-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/solana-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/solana-llms.txt
- group: agent
  title: llms-full.txt (inline docs corpus)
  type: LLMsTxt
  url: llms/solana-llms-full.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/solana-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/solana-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/solana-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/solana-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/solana-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/solana-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/solana-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/solana-cli.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/solana-rpc-schemas.json
- group: build
  title: ''
  type: Examples
  url: examples/solana-rpc-examples.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/solana-rpc-vocabulary.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/solana-rpc-context.jsonld
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-send-transaction-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-devnet-airdrop-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-wallet-portfolio-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-address-transaction-history-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-fee-estimation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-account-rent-exemption-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-token-mint-analytics-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-token-delegate-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-program-accounts-scan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-cluster-health-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-node-identity-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-block-inspection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-ledger-backfill-range-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-leader-schedule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-network-performance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-validator-rewards-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/solana-network-supply-economics-workflow.yml
created: '2026-06-13'
description: Solana is a high-performance blockchain platform designed for fast, secure, and scalable decentralized applications and marketplaces. It exposes a JSON-RPC 2.0 API over HTTP and WebSocket for querying accounts, transactions, programs, token balances, blocks, and cluster state, as well as submitting and simulating transactions. Three public clusters are available — Mainnet, Devnet, and Testnet — with dedicated API nodes for each environment.
examples:
- key_count: 5
  name: Solana Rpc Examples
  slug: solana-rpc-examples
features:
- description: Standard JSON-RPC 2.0 protocol over HTTP POST to cluster API nodes
  name: JSON-RPC 2.0 over HTTP
- description: Real-time push notifications for accounts, transactions, blocks, and cluster events
  name: WebSocket Subscriptions
- description: Mainnet (production), Devnet (development), and Testnet (validator testing) environments
  name: Three Network Clusters
- description: processed, confirmed, and finalized commitment levels for all applicable methods
  name: Commitment Levels
- description: Full support for querying SPL Token accounts, balances, delegates, and supply
  name: SPL Token Support
- description: Simulate transactions before broadcasting to catch errors without consuming fees
  name: Transaction Simulation
- description: Query recent prioritization fees to optimize transaction landing time
  name: Priority Fees
- description: Request free SOL airdrops on Devnet and Testnet for development and testing
  name: Airdrop (Devnet/Testnet)
finops:
- name: Solana Finops
  service_category: Blockchain Infrastructure
  slug: solana-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/solana.png
json_schemas:
- name: Solana JSON-RPC API Schemas
  property_count: 0
  slug: solana-rpc-schemas
jsonld:
- class_count: 17
  name: Solana Rpc Context
  property_count: 56
  slug: solana-rpc-context
layout: provider
mcp_servers:
- description: 'The Solana Foundation publishes solana-dev-mcp, an official reference/demo Model Context Protocol server (stdio transport) that exposes core Solana RPC methods as tools for LLM clients such as Claude '
  name: Solana MCP Server
  slug: solana-mcp-server
modified: '2026-06-20'
name: Solana
nav: Providers
network: true
overview: 'Solana publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Blocks API, Cluster API, and 3 more. Tagged areas include Blockchain, Cryptocurrency, Web3, DeFi, and Transaction.


  The Solana catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Solana''s developer surface includes developer portal, documentation, getting-started guide, authentication, changelog, engineering blog, sandbox, and 61 more developer resources.'
plans:
- name: Solana Plans
  plan_count: 3
  slug: solana-plans
random_paper: 8
rate_limits:
- limit_count: 5
  name: Solana Rpc Rate Limits
  slug: solana-rpc-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Solana API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: solana-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 68.4
  coverage:
    artifact_dirs: 30
    catalog_gap: 31.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 29.5
    contract_quality: 63.3
    developer_ergonomics: 88.1
    discoverability: 75.9
    governance: 29.5
    operational_transparency: 76.3
  open_source:
    applies: true
    score: 85.0
  previous_composite: 68.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/solana/refs/heads/main/screenshots/solana-2026-06-20T194144.png
security:
- kind: authentication
  name: Solana Authentication
  slug: solana-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Solana Domain Security
  slug: solana-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: solana
tags:
- Blockchain
- Cryptocurrency
- Web3
- DeFi
- Transaction
- Tokens
use_cases:
- description: Query token balances, account states, and submit transactions for decentralized finance apps
  name: DeFi Application Backend
- description: Retrieve program accounts and token account data to power NFT discovery and trading
  name: NFT Marketplace Integration
- description: Stream block and transaction data via subscriptions for real-time analytics pipelines
  name: Blockchain Analytics
- description: Check balances, fetch transaction history, sign and send transactions for wallet apps
  name: Wallet Development
- description: Monitor cluster health, epoch schedules, slot leaders, and vote accounts
  name: Validator Monitoring
- description: Interact with SPL Token program to create and manage fungible and non-fungible tokens
  name: Token Issuance
website: https://solana.com/
---
