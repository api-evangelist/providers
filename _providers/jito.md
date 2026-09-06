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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Jito Agentic Access
  operation_count: 3
  slug: jito-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 2
apis:
- description: Real-time streaming surfaces from Jito infrastructure — the wss tip_stream for continuous bundle-tip percentile updates, the ShredstreamProxy SubscribeEntries gRPC method for sub-slot Solana shred del
  name: Jito Streaming Surfaces
  slug: jito-streaming
- description: gRPC SearcherService exposing SubscribeBundleResults, SendBundle, GetNextScheduledLeader, GetConnectedLeaders, GetConnectedLeadersRegioned, GetTipAccounts, and GetRegions. Authenticated via the AuthSe
  name: Jito Searcher gRPC Service
  slug: jito-searcher-grpc
- description: gRPC interface between Jito-Solana validators / relayers and the Block Engine — BlockEngineValidator with SubscribePackets, SubscribeBundles, GetBlockBuilderFeeInfo, GetBlockEngineEndpoints, and Block
  name: Jito Block Engine Validator gRPC
  slug: jito-block-engine-validator-grpc
- description: Relayer gRPC service that sits in front of a Jito-Solana validator, exposing GetTpuConfigs and SubscribePackets so the validator can receive deduplicated packets from the Block Engine and the public T
  name: Jito Relayer gRPC
  slug: jito-relayer-grpc
- description: JitoSOL — Solana's MEV-aware liquid staking token, backed by an instance of the SPL Stake Pool program. Deposit SOL or an existing stake account to receive JitoSOL whose exchange rate accrues both sta
  name: JitoSOL Stake Pool
  slug: jitosol-stake-pool
- description: Jito Restaking — the on-chain program suite (Restaking + Vault) that lets SPL tokens be restaked into Vaults whose security is rented to NCNs (Node Consensus Networks). Includes the tip router, the re
  name: Jito Restaking And Vaults
  slug: jito-restaking
- description: Jito-Solana — the Jito Foundation MEV-enabled fork of the Solana validator client. Adds the Block Engine / Relayer integration that makes the bundle auction possible at the validator layer. Ships alon
  name: Jito-Solana Validator Client
  slug: jito-solana
- baseURL: https://mainnet.block-engine.jito.wtf/api/v1/bundles
  baseurl_source: declared
  description: Submit and inspect atomic Solana transaction bundles.
  name: Jito Labs Bundles API
  slug: jito-bundles-api
- baseURL: https://mainnet.block-engine.jito.wtf/api/v1/bundles
  baseurl_source: declared
  description: Bundle tip pricing data.
  name: Jito Labs Tips API
  slug: jito-tips-api
- baseURL: https://mainnet.block-engine.jito.wtf/api/v1/bundles
  baseurl_source: declared
  description: Direct sendTransaction proxy to validator leaders.
  name: Jito Labs Transactions API
  slug: jito-transactions-api
artifact_total: 80
asyncapis:
- description: 'Real-time streaming endpoints exposed by Jito infrastructure: the WebSocket bundle tip stream and the gRPC ShredStream for low-latency Solana shred delivery. These are the canonical out-of-band feeds '
  name: Jito Streaming Surfaces
  slug: jito-streaming-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jito Block Engine JSON-RPC API
  slug: open-jito-block-engine
- collection_type: open
  name: Jito Block Engine JSON-RPC Bundles API
  slug: open-jito-bundles-api
- collection_type: open
  name: Jito Bundles Tip Floor API
  slug: open-jito-bundles-tip-floor
- collection_type: open
  name: Jito Block Engine JSON-RPC Bundles Tips API
  slug: open-jito-tips-api
- collection_type: open
  name: Jito Block Engine JSON-RPC Bundles Transactions API
  slug: open-jito-transactions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jito-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jito-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.jito.network
- group: start
  title: ''
  type: Portal
  url: https://www.jito.network/stakers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jito.wtf
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jito.wtf/lowlatencytxnsend
- group: other
  title: ''
  type: Repository
  url: https://github.com/jito-labs/jito-docs
- group: docs
  title: ''
  type: Documentation
  url: https://jito-labs.gitbook.io/mev/
- group: docs
  title: ''
  type: Documentation
  url: https://jito-foundation.gitbook.io/mev/
- group: start
  title: ''
  type: Console
  url: https://explorer.jito.wtf/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jito-labs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jito-foundation
- group: other
  title: ''
  type: Repository
  url: https://github.com/jito-labs/mev-protos
- group: build
  title: ''
  type: SDKs
  url: https://github.com/jito-labs/jito-ts
- group: build
  title: ''
  type: SDKs
  url: https://github.com/jito-labs/jito-rs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/jito-labs/jito-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/jito-labs/jito-js-rpc
- group: build
  title: ''
  type: SDKs
  url: https://github.com/jito-labs/jito-py-rpc
- group: build
  title: ''
  type: SDKs
  url: https://github.com/jito-labs/jito-rust-rpc
- group: build
  title: ''
  type: SDKs
  url: https://github.com/jito-labs/jito-go-rpc
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/jito-labs/searcher-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/jito-labs/mev-bot
- group: build
  title: ''
  type: Tools
  url: https://github.com/jito-labs/shredstream-proxy
- group: build
  title: ''
  type: Tools
  url: https://github.com/jito-labs/block_engine_simple
- group: other
  title: ''
  type: Repository
  url: https://github.com/jito-foundation/jito-solana
- group: other
  title: ''
  type: Repository
  url: https://github.com/jito-foundation/jito-relayer
- group: other
  title: ''
  type: Repository
  url: https://github.com/jito-foundation/restaking
- group: other
  title: ''
  type: Repository
  url: https://github.com/jito-foundation/stakenet
- group: other
  title: ''
  type: Repository
  url: https://github.com/jito-foundation/jito-programs
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/jito-foundation/jito-omnidocs
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/jito_sol
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/jito_labs
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/jito
- group: design
  title: ''
  type: SpectralRules
  url: rules/jito-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/jito-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/jito-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/jito-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jito-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/jito-finops.yml
- group: company
  title: ''
  type: About
  url: https://gov.jito.network
created: '2026-05-24T00:00:00.000Z'
description: Jito Labs is the Solana MEV infrastructure company behind Jito-Solana, the MEV-enabled validator client that runs on the majority of Solana mainnet stake, and the Jito Block Engine, an off-chain auction service that accepts bundles and transactions from searchers and forwards them to the next leader. Together with the Jito Foundation it stewards JitoSOL — Solana's largest MEV-aware liquid staking token — the StakeNet validator scoring system, the Jito Restaking and Vault programs that power Node Consensus Networks, the merkle-based token distributor used for airdrops, and the JTO governance token. Developer surfaces include a JSON-RPC API for bundle and transaction submission, a public REST tip floor and WebSocket tip stream for pricing, the ShredStream gRPC service for sub-slot Solana shreds, and the open mev-protos repository that defines the canonical Auth, Block Engine, Bundle, Packet, Relayer, Searcher, Shared, and ShredStream gRPC interfaces — with official SDKs in TypeScript,
  Python, Rust, and Go.
examples:
- key_count: 4
  name: Jito Getbundlestatuses Example
  slug: jito-getBundleStatuses-example
- key_count: 4
  name: Jito Gettipaccounts Example
  slug: jito-getTipAccounts-example
- key_count: 4
  name: Jito Sendbundle Example
  slug: jito-sendBundle-example
- key_count: 3
  name: Jito Sendbundle Response Example
  slug: jito-sendBundle-response-example
features:
- Jito-Solana — MEV-enabled fork of the Solana validator client run by the majority of mainnet stake
- Block Engine — off-chain bundle and transaction auction with regional clusters in Amsterdam, Dublin, Frankfurt, London, New York, Salt Lake City, Singapore, and Tokyo plus testnet endpoints in Dallas and New York
- Bundles — atomic, ordered groups of up to five Solana transactions priced by SOL tip
- sendBundle, getBundleStatuses, getInflightBundleStatuses, getTipAccounts, and getRandomTipAccount JSON-RPC methods
- sendTransaction proxy with optional bundleOnly mode for single-tx bundles
- Tip Floor REST endpoint and tip_stream WebSocket for live tip percentile pricing
- ShredStream gRPC service for sub-slot Solana shred delivery to bots, dApps, and validators
- Jito Relayer with GetTpuConfigs and SubscribePackets gRPC interface
- SearcherService gRPC with SubscribeBundleResults, GetNextScheduledLeader, GetConnectedLeaders, and GetRegions
- BlockEngineValidator and BlockEngineRelayer gRPC integrations consumed by Jito-Solana
- AuthService challenge / token-refresh flow for all gRPC surfaces
- Official SDKs in TypeScript (jito-ts, jito-js-rpc), Python (jito-python, jito-py-rpc), Rust (jito-rs, jito-rust-rpc), and Go (jito-go-rpc)
- JitoSOL — MEV-aware liquid staking token built on the SPL Stake Pool with on-chain StakeNet validator scoring
- Jito Restaking and Vault programs enabling SPL token restaking into NCN-secured workloads
- Tip Router NCN, Rewards NCN, and BLS NCN reference implementations
- JTO governance through Jito Realms (forked Solana governance UI)
- Merkle-based token distributor program for airdrops and reward distribution
- Geyser gRPC plugin and accountsdb connector for account and slot streaming
- Local block engine for testing bundles against jito-solana
- block_engine_simple, mev-bot, searcher-examples, and stakenet-simulator reference codebases
- Open mev-protos repository defining the canonical Auth, Block Engine, Bundle, Packet, Relayer, Searcher, Shared, and ShredStream gRPC services
finops:
- name: Jito Finops
  service_category: ''
  slug: jito-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jito.png
integrations:
- description: All Jito services are native to Solana; Jito-Solana is the dominant validator client on mainnet.
  name: Solana
- description: Reference Jupiter integration via jupiter-api-rust-example used in mev-bot.
  name: Jupiter
- description: Reference Drift Protocol v2 bot via jito-drift-bots-v2.
  name: Drift
- description: Reference Mango v3 smart contract integration via mango-v3.
  name: Mango Markets
- description: Reference Solend SDK integration via solend-sdk.
  name: Solend
- description: JitoSOL is bridged across chains via the jitosol-wormhole-updater and jitosol-evm-token-contract.
  name: Wormhole
- description: Jito governance runs on the Solana Realms governance UI, forked into governance-ui.
  name: Realms
- description: Squads V4 multisig integration ships in the Jito Foundation org.
  name: Squads
- description: Major Solana RPC providers expose Jito bundle submission and ShredStream alongside their own infrastructure.
  name: Helius / Triton / QuickNode
json_schemas:
- name: Jito Bundle
  property_count: 4
  slug: jito-bundle
- name: Jito Bundle Status
  property_count: 5
  slug: jito-bundle-status
- name: JitoSOL Stake Position
  property_count: 7
  slug: jito-jitosol-stake
- name: Jito NCN (Node Consensus Network)
  property_count: 6
  slug: jito-ncn
- name: Jito Bundle Tip Floor
  property_count: 7
  slug: jito-tip-floor
json_structures:
- name: Jito Bundle Status Structure
  property_count: 5
  slug: jito-bundle-status-structure
- name: Jito Bundle Structure
  property_count: 4
  slug: jito-bundle-structure
jsonld:
- class_count: 26
  name: Jito Context
  property_count: 0
  slug: jito-context
layout: provider
modified: '2026-07-25'
name: Jito Labs
nav: Providers
network: true
overview: 'Jito Labs publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Jito Streaming Surfaces, Bundles API, Tips API, and 1 more. Tagged areas include Solana, MEV, Block Engine, Bundles, and Liquid Staking.


  The Jito Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Jito Labs'' developer surface includes developer portal, documentation, developer console, code examples, tooling, and 35 more developer resources.'
plans:
- name: Jito Plans Pricing
  plan_count: 3
  slug: jito-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Jito Rate Limits
  slug: jito-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Jito Labs API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: jito-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Jito Labs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: jito-jsonschema-spectral-rules
- effective_rule_count: 45
  extends:
  - spectral:oas
  name: Jito Labs API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: jito-rules
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 74.5
    catalog_earned_first_party: 0.0
    catalog_gap: 40.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 71.2
    developer_ergonomics: 54.8
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jito/refs/heads/main/screenshots/jito-2026-06-20T183736.png
security:
- kind: domain-security
  name: Jito Domain Security
  slug: jito-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: jito
solutions:
- description: Bundle-based MEV capture with auction-priced inclusion and gRPC streaming results.
  name: Searchers
- description: Run Jito-Solana + jito-relayer to receive bundles and share in MEV revenue.
  name: Validators
- description: Stake SOL into JitoSOL for MEV-aware liquid staking with no lockup.
  name: Stakers
- description: Run new Node Consensus Network workloads secured by restaked SPL collateral.
  name: NCN Operators
- description: Consume ShredStream and the Block Engine for low-latency Solana access.
  name: dApps And Bots
tags:
- Solana
- MEV
- Block Engine
- Bundles
- Liquid Staking
- JitoSOL
- Restaking
- JTO
- DAO
- Validator
- Searcher
- ShredStream
- Crypto
- DeFi
use_cases:
- description: Searchers submit bundles capturing cross-AMM arbitrage opportunities on Solana DEXs.
  name: MEV Arbitrage
- description: Lending protocol liquidations submitted as atomic bundles so a liquidation either lands fully or not at all.
  name: Liquidation Bots
- description: Consumer trading bots use ShredStream and sendBundle for low-latency token sniping.
  name: Telegram Trading Bots
- description: Market makers consume ShredStream for the lowest-latency view of block state and use sendTransaction with bundleOnly for priority routing.
  name: High-Frequency Trading
- description: Bundles guarantee atomic mint + transfer flows that revert cleanly if the mint slot is missed.
  name: NFT Mint Sniping
- description: Users hold JitoSOL to earn staking and MEV rewards while keeping liquidity for DeFi.
  name: Liquid Staking
- description: New NCN workloads (oracles, bridges, DA, coprocessors) bootstrap economic security by renting restaked SPL collateral from Jito Vaults.
  name: Restaked Security
- description: Solana validators run Jito-Solana plus jito-relayer to participate in the bundle auction and capture MEV rewards.
  name: Validator Operations
website: https://www.jito.network
---
