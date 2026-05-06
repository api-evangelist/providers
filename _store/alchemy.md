---
aid: alchemy
url: https://raw.githubusercontent.com/api-evangelist/alchemy/refs/heads/main/apis.yml
name: Alchemy
tags:
  - Blockchain
  - Cryptocurrency
  - Web3
  - Account Abstraction
  - Ethereum
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-07T00:00:00.000Z'
modified: '2026-04-19'
position: Consuming
description: Alchemy is a Web3 developer platform providing powerful APIs, SDKs, and infrastructure tools to build and scale blockchain applications. Supporting Ethereum, Polygon, and other EVM-compatible networks, Alchemy powers production dApps with reliable node infrastructure, enhanced APIs for token data, asset transfers, NFTs, and ERC-4337 Account Abstraction tools including gas sponsorship (Gas Manager) and smart account bundling.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
apis:
  - aid: alchemy:alchemy-gas-manager-api
    name: Alchemy Gas Manager API
    tags:
      - Gas Manager
      - Account Abstraction
      - ERC-4337
    humanURL: https://www.alchemy.com/gas-manager
    description: The Alchemy Gas Manager API enables developers to sponsor gas fees for end users via the ERC-4337 Account Abstraction standard. Manage sponsorship policies with per-user spend limits, total caps, allowlisted contracts, and time-based expiry, enabling gasless transactions for dApp users.
    properties:
      - type: OpenAPI
        url: openapi/alchemy-gas-manager-api-openapi.yml
      - type: JSONSchema
        url: json-schema/alchemy-gas-manager-api-policy-schema.json
      - type: JSONSchema
        url: json-schema/alchemy-gas-manager-api-policy-list-response-schema.json
      - type: JSONSchema
        url: json-schema/alchemy-gas-manager-api-create-policy-request-schema.json
      - type: JSONSchema
        url: json-schema/alchemy-gas-manager-api-sponsor-user-operation-request-schema.json
      - type: JSONSchema
        url: json-schema/alchemy-gas-manager-api-sponsor-user-operation-result-schema.json
      - type: JSONSchema
        url: json-schema/alchemy-gas-manager-api-sponsor-user-operation-response-schema.json
      - type: JSONStructure
        url: json-structure/alchemy-gas-manager-api-policy-structure.json
      - type: JSONStructure
        url: json-structure/alchemy-gas-manager-api-policy-list-response-structure.json
      - type: JSONStructure
        url: json-structure/alchemy-gas-manager-api-create-policy-request-structure.json
      - type: JSONStructure
        url: json-structure/alchemy-gas-manager-api-sponsor-user-operation-request-structure.json
      - type: JSONStructure
        url: json-structure/alchemy-gas-manager-api-sponsor-user-operation-result-structure.json
      - type: JSONStructure
        url: json-structure/alchemy-gas-manager-api-sponsor-user-operation-response-structure.json
      - type: JSON-LD
        url: json-ld/alchemy-gas-manager-api-context.jsonld
      - type: Example
        url: examples/alchemy-gas-manager-api-policy-example.json
      - type: Example
        url: examples/alchemy-gas-manager-api-policy-list-response-example.json
      - type: Example
        url: examples/alchemy-gas-manager-api-create-policy-request-example.json
      - type: Example
        url: examples/alchemy-gas-manager-api-sponsor-user-operation-request-example.json
      - type: Example
        url: examples/alchemy-gas-manager-api-sponsor-user-operation-result-example.json
      - type: Example
        url: examples/alchemy-gas-manager-api-sponsor-user-operation-response-example.json
  - aid: alchemy:alchemy-token-api
    name: Alchemy Token API
    tags:
      - Tokens
      - ERC-20
      - DeFi
    humanURL: https://www.alchemy.com/token-api
    description: The Alchemy Token API provides comprehensive access to ERC-20 token data across EVM-compatible networks. Retrieve token balances by wallet address, token metadata (name, symbol, decimals, logo), and real-time pricing data. Supports multi-chain queries for wallets, portfolio trackers, and DeFi applications.
    properties:
      - type: OpenAPI
        url: openapi/alchemy-token-api-openapi.yml
      - type: JSONSchema
        url: json-schema/alchemy-token-api-token-balance-schema.json
      - type: JSONSchema
        url: json-schema/alchemy-token-api-token-balances-result-schema.json
      - type: JSONSchema
        url: json-schema/alchemy-token-api-token-balances-response-schema.json
      - type: JSONSchema
        url: json-schema/alchemy-token-api-token-metadata-schema.json
      - type: JSONSchema
        url: json-schema/alchemy-token-api-token-metadata-response-schema.json
      - type: JSONStructure
        url: json-structure/alchemy-token-api-token-balance-structure.json
      - type: JSONStructure
        url: json-structure/alchemy-token-api-token-balances-result-structure.json
      - type: JSONStructure
        url: json-structure/alchemy-token-api-token-balances-response-structure.json
      - type: JSONStructure
        url: json-structure/alchemy-token-api-token-metadata-structure.json
      - type: JSONStructure
        url: json-structure/alchemy-token-api-token-metadata-response-structure.json
      - type: JSON-LD
        url: json-ld/alchemy-token-api-context.jsonld
      - type: Example
        url: examples/alchemy-token-api-token-balance-example.json
      - type: Example
        url: examples/alchemy-token-api-token-balances-result-example.json
      - type: Example
        url: examples/alchemy-token-api-token-balances-response-example.json
      - type: Example
        url: examples/alchemy-token-api-token-metadata-example.json
      - type: Example
        url: examples/alchemy-token-api-token-metadata-response-example.json
  - aid: alchemy:alchemy-transfers-api
    name: Alchemy Transfers API
    tags:
      - Transfers
      - NFTs
      - Transaction History
    humanURL: https://www.alchemy.com/transfers-api
    description: The Alchemy Transfers API provides access to historical on-chain transfer data across EVM-compatible networks. Query asset transfers by address, block range, and transfer category (ETH, ERC-20, ERC-721, ERC-1155, and internal transfers), enabling wallet activity tracking, portfolio history, and transaction auditing.
    properties:
      - type: OpenAPI
        url: openapi/alchemy-transfers-api-openapi.yml
      - type: JSONSchema
        url: json-schema/alchemy-transfers-api-asset-transfer-schema.json
      - type: JSONSchema
        url: json-schema/alchemy-transfers-api-transfer-metadata-schema.json
      - type: JSONSchema
        url: json-schema/alchemy-transfers-api-asset-transfers-result-schema.json
      - type: JSONSchema
        url: json-schema/alchemy-transfers-api-asset-transfers-response-schema.json
      - type: JSONStructure
        url: json-structure/alchemy-transfers-api-asset-transfer-structure.json
      - type: JSONStructure
        url: json-structure/alchemy-transfers-api-transfer-metadata-structure.json
      - type: JSONStructure
        url: json-structure/alchemy-transfers-api-asset-transfers-result-structure.json
      - type: JSONStructure
        url: json-structure/alchemy-transfers-api-asset-transfers-response-structure.json
      - type: JSON-LD
        url: json-ld/alchemy-transfers-api-context.jsonld
      - type: Example
        url: examples/alchemy-transfers-api-asset-transfer-example.json
      - type: Example
        url: examples/alchemy-transfers-api-transfer-metadata-example.json
      - type: Example
        url: examples/alchemy-transfers-api-asset-transfers-result-example.json
      - type: Example
        url: examples/alchemy-transfers-api-asset-transfers-response-example.json
  - aid: alchemy:alchemy-bundler-api
    name: Alchemy Bundler API
    tags:
      - Bundler
      - Account Abstraction
      - ERC-4337
    humanURL: https://www.alchemy.com/bundler
    description: The Alchemy Bundler API implements the ERC-4337 Account Abstraction bundler standard, allowing UserOperations to be submitted to the blockchain. Developers can send, estimate, and track UserOperations using standard eth_sendUserOperation and related methods.
    properties: []
common:
  - url: https://www.alchemy.com/pricing
    name: Pricing
    type: Pricing
  - url: https://www.alchemy.com/sandbox
    name: Sandbox
    type: Sandbox
  - url: https://www.alchemy.com/webhooks
    name: Webhooks
    type: Webhooks
  - url: https://www.alchemy.com/sdk
    name: Alchemy SDK
    type: SDKs
  - url: https://www.alchemy.com/blog
    name: Blog
    type: Blog
  - url: https://www.postman.com/alchemyapi/alchemy-platforms/overview
    name: Postman Workspace
    type: PostmanWorkspace
  - url: https://docs.alchemy.com
    name: Documentation
    type: Documentation
  - url: https://www.alchemy.com/support
    name: Support
    type: Support
  - url: https://dashboard.alchemy.com/signup
    name: Sign Up
    type: SignUp
  - url: https://status.alchemy.com
    name: Status Page
    type: StatusPage
  - url: https://github.com/alchemyplatform
    name: GitHub Organization
    type: GitHubOrganization
  - url: rules/alchemy-spectral-rules.yml
    name: Alchemy Spectral Rules
    type: SpectralRules
  - url: vocabulary/alchemy-vocabulary.yaml
    name: Alchemy Vocabulary
    type: Vocabulary
  - url: capabilities/web3-wallet-portfolio.yaml
    name: Web3 Wallet Portfolio
    type: NaftikoCapability
  - url: capabilities/gasless-transaction-management.yaml
    name: Gasless Transaction Management
    type: NaftikoCapability
  - type: Features
    data:
      - name: Multi-Chain Support
        description: Query token data and transfers across Ethereum, Polygon, and other EVM-compatible networks.
      - name: ERC-4337 Account Abstraction
        description: Full support for ERC-4337 with bundler, paymaster (Gas Manager), and smart account APIs.
      - name: Gasless Transactions
        description: Sponsor gas fees for end users via Gas Manager policies with spend limits and network rules.
      - name: Token Data
        description: Real-time ERC-20 token balances and metadata including name, symbol, decimals, and logo.
      - name: Transfer History
        description: Historical on-chain transfer data for ETH, ERC-20, ERC-721, and ERC-1155 assets.
      - name: JSON-RPC Compatibility
        description: Standard Ethereum JSON-RPC interface with Alchemy-enhanced methods for additional data.
      - name: Webhook Notifications
        description: Real-time blockchain event notifications via webhooks for address activity and mined transactions.
  - type: UseCases
    data:
      - name: Wallet Application Development
        description: Build EVM wallets with real-time token balances, transaction history, and NFT support.
      - name: DeFi Portfolio Tracking
        description: Track multi-asset portfolios across EVM networks with accurate token pricing and balances.
      - name: Gasless dApp UX
        description: Abstract gas fees from end users so they can interact with dApps without holding ETH.
      - name: NFT Marketplace Integration
        description: Query ERC-721 and ERC-1155 transfer history for NFT ownership tracking and provenance.
      - name: Blockchain Analytics
        description: Analyze on-chain transfer patterns, wallet activity, and token flow across EVM networks.
  - type: Integrations
    data:
      - name: Ethereum
        description: Native support for Ethereum mainnet and testnets.
      - name: Polygon
        description: Full API support for Polygon (MATIC) mainnet and Mumbai testnet.
      - name: ERC-4337 Bundlers
        description: Works with any ERC-4337 compatible bundler for UserOperation submission.
      - name: MetaMask
        description: Integration with MetaMask wallet for Web3 connection management.
      - name: Hardhat and Foundry
        description: Developer toolchain integration for local testing and deployment.
---
