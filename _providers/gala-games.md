---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 63.5
  scored_at: '2026-08-17'
api_count: 8
apis:
- description: 'The GalaChain asset-channel token contract, exposed over REST by the GalaChain Gateway. Covers fungible and non-fungible token classes, balances, allowances, minting, burning, locking, transfers, NFT '
  name: GalaChain Token Contract API
  slug: galachain-token-contract
- description: The GalaChain asset-channel concentrated-liquidity DEX contract (dexv3), exposed over REST by the GalaChain Gateway. Covers pool data, positions, liquidity estimation, tick and bitmap data, swap allow
  name: GalaChain DEX v3 Contract API
  slug: galachain-dexv3-contract
- description: 'The GalaChain asset-channel launchpad contract, exposed over REST by the GalaChain Gateway. Covers bonding-curve token sales: buying and selling meme tokens against the native token, sale details and '
  name: GalaChain Launchpad Contract API
  slug: galachain-launchpad-contract
- description: The GalaChain asset-channel fee contract, exposed over REST by the GalaChain Gateway. Used to fetch fee authorizations that pay for cross-channel operations, and to dry-run fee transactions before sub
  name: GalaChain Fee Contract API
  slug: galachain-fee-contract
- description: 'The GalaChain asset-channel public key contract, exposed over REST by the GalaChain Gateway. Resolves on-chain identity: fetching registered public keys and chain objects by key, plus dry-run support '
  name: GalaChain Public Key Contract API
  slug: galachain-public-key-contract
- description: 'GalaConnect is Gala''s public programmatic surface for GalaSwap: fetching and filling token swaps, creating and terminating swaps, creating headless wallets, creating project tokens, authorizing cross-'
  name: GalaConnect API
  slug: galaconnect
- description: 'Near real-time GalaChain chain data: blocks and recent blocks by channel, transactions, block height, registered channels, token media, balances, allowances, bridge operations and a cross-entity searc'
  name: Gala Block Explorer API
  slug: block-explorer
- description: 'The backend behind GalaSwap: trade quotes, pools and composite pools, positions, add and remove liquidity, swaps, bundles, slot0 and transaction status, plus explore analytics, price oracle, CoinGecko'
  name: Gala DeFi Backend API
  slug: defi-backend
artifact_total: 14
asyncapis:
- description: ''
  name: Gala Games Event Surface
  slug: gala-games-event-surface
common:
- group: company
  title: ''
  type: Website
  url: https://gala.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://galachain.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.galachain.com/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://gateway-mainnet.galachain.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.galachain.com/latest/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://support.gala.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GalaChain
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/GalaChain/sdk
- group: start
  title: ''
  type: SignUp
  url: https://games.gala.com/account
- group: auth
  title: ''
  type: Authentication
  url: authentication/gala-games-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gala-games-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/gala-games-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gala-games-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/gala-games-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gala-games-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/gala-games-tool-crosswalk.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gala-games-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/gala-games-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gala-games-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gala-games-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gala-games-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gala-games-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gala-games-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gala-games-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gala-games-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gala-games-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-16'
description: Gala (formerly Gala Games) is a Web3 gaming and entertainment company that operates GalaChain, a Hyperledger Fabric based Layer 1 built for games, music and film. Its public API surface is REST-first rather than RPC. The GalaChain Gateway publishes an OpenAPI document per deployed chaincode contract (token, DEX v3, launchpad, fee and public key) across eighteen channel/contract pairs including per-game channels such as mirandus, championsarena and thewalkingdeadempires. GalaConnect exposes token swaps, headless wallet creation and cross-chain operations at api-galaswap.gala.com, a Block Explorer API serves blocks, transactions and balances, and the Gala DeFi backend serves pool, trading, liquidity and leaderboard data for GalaSwap. Write operations are authenticated by secp256k1 request signatures rather than bearer tokens, and every write carries a uniqueKey that GalaChain enforces as an idempotency key.
image: https://avatars.githubusercontent.com/u/135145372?v=4
layout: provider
mcp_servers:
- description: ''
  name: gala-games-mcp.yml
  slug: gala-games-mcpyml
modified: '2026-08-16'
name: Gala Games
nav: Providers
network: true
overview: 'Gala Games publishes 8 APIs on the [APIs.io](https://apis.io/) network, including GalaChain Token Contract API, GalaChain DEX v3 Contract API, GalaChain Launchpad Contract API, and 5 more. Tagged areas include Company, Blockchain, Web3, Gaming, and NFT.


  The Gala Games catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gala Games'' developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, CLI, and 20 more developer resources.'
plans:
- name: Gala Games Plans Pricing
  plan_count: 0
  slug: gala-games-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 1
  name: Gala Games Rate Limits
  slug: gala-games-rate-limits
score:
  band: developing
  composite: 46.3
  facets:
    commercial_clarity: 13.2
    contract_quality: 48.5
    developer_ergonomics: 78.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 42.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
security:
- kind: authentication
  name: Gala Games Authentication
  slug: gala-games-authentication
  summary_line: signature/apiKey · 4 schemes
- kind: domain-security
  name: Gala Games Domain Security
  slug: gala-games-domain-security
  summary_line: TLSv1.3
slug: gala-games
tags:
- Company
- Blockchain
- Web3
- Gaming
- NFT
- Tokens
- DeFi
- Cryptocurrency
- Distributed Ledger
- Smart Contracts
- Entertainment
- Decentralized Exchange
website: https://gala.com/
---
