---
aid: uniswap
url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/apis.yml
apis:
  - aid: uniswap:uniswap-trading-api
    name: Uniswap Trading API
    tags:
      - Blockchain
      - Cryptocurrency
      - DeFi
      - Liquidity
      - Swaps
    humanURL: https://developers.uniswap.org/
    properties:
      - url: https://developers.uniswap.org/
        type: Documentation
      - url: https://developers.uniswap.org/dashboard
        type: SignUp
      - url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/openapi/uniswap-trading-openapi.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/json-schema/uniswap-quote-request-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/json-schema/uniswap-quote-response-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/json-schema/uniswap-create-swap-request-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/json-schema/uniswap-create-swap-response-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/json-schema/uniswap-order-request-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/json-schema/uniswap-order-response-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/examples/uniswap-get-swap-quote-example.json
        type: Example
      - url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/examples/uniswap-create-swap-transaction-example.json
        type: Example
      - url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/examples/uniswap-create-gasless-order-example.json
        type: Example
      - url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/examples/uniswap-create-lp-position-example.json
        type: Example
    description: The Uniswap Trading API provides REST endpoints for token swaps, bridges, liquidity management, and execution planning across 25+ blockchain networks. It supports swap quoting, gasless UniswapX orders, LP position management, wallet operations (EIP-7702, ERC-4337), and multi-step execution plans. Authentication requires an API key passed in the x-api-key header.
  - aid: uniswap:uniswap-subgraph-api
    name: Uniswap Subgraph API
    tags:
      - Blockchain
      - DeFi
      - GraphQL
      - On-Chain Data
    humanURL: https://developers.uniswap.org/api/overview
    properties:
      - url: https://developers.uniswap.org/api/overview
        type: Documentation
    description: The Uniswap Subgraph API provides GraphQL endpoints for querying on-chain data across Uniswap protocol versions v1, v2, v3, and v4. Powered by The Graph Protocol decentralized network, it supports queries for pools, positions, swaps, ticks, and historical data. Requires an API key from The Graph Studio.
  - aid: uniswap:uniswap-x-api
    name: UniswapX API
    tags:
      - Blockchain
      - DeFi
      - Gasless
      - Intent Orders
    humanURL: https://docs.uniswap.org/
    properties:
      - url: https://docs.uniswap.org/
        type: Documentation
    description: UniswapX is a gasless, auction-based ERC20 swap settlement protocol that routes orders through a competitive filler network. Swappers sign off-chain orders which are filled by fillers who compete to provide the best execution. The API supports order creation, retrieval, and status tracking.
name: Uniswap
tags:
  - Blockchain
  - Cryptocurrency
  - DeFi
  - Decentralized Exchange
  - Liquidity
  - Swaps
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-16'
modified: '2026-05-03'
position: Consuming
segments:
  - DeFi
  - Cryptocurrency
description: Uniswap is the world's leading decentralized exchange (DEX) protocol, enabling permissionless token swaps on Ethereum and 25+ EVM-compatible blockchains through automated market making (AMM). The Uniswap Labs Trading API provides REST endpoints for quotes, swap execution, gasless UniswapX orders, liquidity provider (LP) position management, and wallet operations. Developers can build trading bots, portfolio managers, DeFi aggregators, and embedded swap UIs on top of the protocol.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: Uniswap Developer Portal
    url: https://developers.uniswap.org/
    type: Portal
  - name: Uniswap Documentation
    url: https://docs.uniswap.org/
    type: Documentation
  - name: Uniswap API Dashboard
    url: https://developers.uniswap.org/dashboard
    type: Login
  - name: Uniswap GitHub Organization
    url: https://github.com/Uniswap
    type: GitHubOrganization
  - name: Uniswap Blog
    url: https://blog.uniswap.org/
    type: Blog
  - name: Uniswap Discord
    url: https://discord.gg/FCfyBSbCU5
    type: Discord
  - name: Uniswap Twitter/X
    url: https://twitter.com/uniswap
    type: X
  - name: Uniswap Core TypeScript SDK
    url: https://www.npmjs.com/package/@uniswap/sdk-core
    type: SDK
  - name: Uniswap v3 TypeScript SDK
    url: https://www.npmjs.com/package/@uniswap/v3-sdk
    type: SDK
  - name: Uniswap v4 TypeScript SDK
    url: https://developers.uniswap.org/docs/sdks/v4/overview
    type: SDK
  - name: Uniswap Spectral Rules
    url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/rules/uniswap-spectral-rules.yml
    type: SpectralRules
  - name: Uniswap Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/vocabulary/uniswap-vocabulary.yaml
    type: Vocabulary
  - name: Uniswap DeFi Trading Capability
    url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/capabilities/defi-trading.yaml
    type: NaftikoCapability
  - name: Uniswap JSON-LD Context
    url: https://raw.githubusercontent.com/api-evangelist/uniswap/refs/heads/main/json-ld/uniswap-context.jsonld
    type: JSON-LD
  - name: Uniswap Features
    type: Features
    data:
      - name: Token Swaps
        description: Swap any ERC-20 token on 25+ EVM chains with optimal routing across Uniswap v2, v3, and v4 liquidity pools.
      - name: Gasless UniswapX Orders
        description: Sign off-chain intent-based orders that are filled by competing fillers without requiring the swapper to pay gas fees directly.
      - name: Liquidity Provider Management
        description: Create, increase, decrease, and manage concentrated liquidity positions on Uniswap v3 and v4 with fee tier and tick range control.
      - name: Cross-Chain Bridging
        description: Bridge tokens across EVM networks using the unified quote and swap APIs with automatic routing to the best bridge provider.
      - name: Limit Orders
        description: Submit limit orders that execute automatically when market conditions meet the specified price target.
      - name: Smart Wallet Support
        description: Native support for EIP-7702 delegated accounts, ERC-4337 account abstraction, and EIP-5792 wallet capabilities.
      - name: Execution Plans
        description: Create multi-step execution plans for complex DeFi workflows with step proofs for verification and tracking.
      - name: On-Chain Data via Subgraphs
        description: Query historical and real-time on-chain data for pools, positions, swaps, and ticks via GraphQL subgraph endpoints.
  - name: Uniswap Use Cases
    type: UseCases
    data:
      - name: Token Swap Integration
        description: Embed token swap functionality in wallets, DApps, and portfolio managers using the Trading API's quote and swap endpoints.
      - name: DeFi Aggregator
        description: Build a DEX aggregator that routes through Uniswap's liquidity alongside other protocols for best execution.
      - name: Liquidity Mining Bot
        description: Automate LP position management — create, rebalance, and close positions based on market conditions using LP management endpoints.
      - name: On-Chain Analytics
        description: Power analytics dashboards with historical pool, swap, and liquidity data from the Subgraph GraphQL API.
      - name: Cross-Chain Bridge UI
        description: Build a bridge interface that quotes and executes cross-chain token transfers using the swap/bridge endpoints.
  - name: Uniswap Integrations
    type: Integrations
    data:
      - name: The Graph Protocol
        description: Uniswap subgraphs are indexed and served by The Graph Protocol's decentralized network.
      - name: Ethereum
        description: Primary deployment network for Uniswap v2, v3, and v4 smart contracts.
      - name: Polygon
        description: Uniswap v3 deployed on Polygon PoS and zkEVM networks.
      - name: Arbitrum
        description: Uniswap v3 deployed on Arbitrum One for low-cost swaps.
      - name: Optimism
        description: Uniswap v3 deployed on Optimism for low-cost swaps.
      - name: Base
        description: Uniswap v3 and v4 deployed on Base (Coinbase's L2 network).
      - name: UniswapX Fillers
        description: Third-party filler bots compete to fill UniswapX gasless orders for best execution.
---
