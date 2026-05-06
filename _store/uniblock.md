---
aid: uniblock
url: https://raw.githubusercontent.com/api-evangelist/uniblock/refs/heads/main/apis.yml
name: Uniblock
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Blockchain
  - Web3
description: Uniblock is a Web3 infrastructure platform that provides a standardized API aggregating data from hundreds of DEXs and cross-chain bridges, abstracting the complexity of multi-chain development into a single endpoint. The platform completed $5.2 million in financing with $7.5 million in total funding.
created: '2025-02-08'
modified: '2026-03-24'
specificationVersion: '0.19'
apis:
  - aid: uniblock:unified-api
    name: Uniblock Unified API
    tags:
      - Blockchain
      - Market Data
      - NFTs
      - Tokens
      - Transactions
      - Web3
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.uniblock.dev
    humanURL: https://docs.uniblock.dev/docs/unified-api-overview
    properties:
      - url: https://docs.uniblock.dev/docs/unified-api-overview
        type: Documentation
      - url: openapi/uniblock-unified-api-openapi.yml
        type: OpenAPI
      - url: asyncapi/uniblock-webhooks-asyncapi.yml
        type: AsyncAPI
    description: The Uniblock Unified API provides a single standardized interface for interacting with multiple blockchain networks and data providers. It offers higher-level endpoints for common data needs including token metadata and balances, NFT collections and assets, transaction lookups, and market data for pricing and analytics.
  - aid: uniblock:direct-api
    name: Uniblock Direct API
    tags:
      - Blockchain
      - Pass-Through
      - Providers
      - Web3
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.uniblock.dev/direct/v1
    humanURL: https://docs.uniblock.dev/docs/direct-api-overview
    properties:
      - url: https://docs.uniblock.dev/docs/direct-api-overview
        type: Documentation
      - url: openapi/uniblock-direct-api-openapi.yml
        type: OpenAPI
    description: The Uniblock Direct API gives developers access to provider-specific endpoints exactly as offered by upstream blockchain data providers. This is intended for use cases where a specific method is not yet abstracted into the Unified API, allowing direct pass-through access to providers like Alchemy, SimpleHash, TonAPI, and others. Requests follow the pattern of specifying the provider and endpoint path, while still benefiting from Uniblock's routing, retry, and failover infrastructure.
  - aid: uniblock:json-rpc-api
    name: Uniblock JSON-RPC API
    tags:
      - Blockchain
      - EVM
      - JSON-RPC
      - Nodes
      - Web3
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.uniblock.dev
    humanURL: https://docs.uniblock.dev/reference/unified-api-reference-overview
    properties:
      - url: https://docs.uniblock.dev/reference/unified-api-reference-overview
        type: Documentation
      - url: openapi/uniblock-json-rpc-api-openapi.yml
        type: OpenAPI
    description: The Uniblock JSON-RPC API provides a single endpoint for standard JSON-RPC calls across hundreds of blockchain networks. Rather than managing individual node provider connections for each chain, developers can send JSON-RPC requests through Uniblock which automatically selects the best upstream node provider. This supports standard Ethereum and EVM-compatible JSON-RPC methods, as well as Solana and other chain-specific RPC interfaces, with built-in failover and automatic retries.
common:
  - type: JSON-LD
    url: json-ld/uniblock-context.jsonld
  - type: JSONSchema
    url: json-schema/uniblock-token-schema.json
  - type: JSONSchema
    url: json-schema/uniblock-nft-schema.json
  - type: JSONSchema
    url: json-schema/uniblock-transaction-schema.json
  - type: JSONSchema
    url: json-schema/uniblock-webhook-event-schema.json
  - type: Website
    url: https://uniblock.dev/
  - type: Portal
    url: https://docs.uniblock.dev/
  - type: Documentation
    url: https://docs.uniblock.dev/docs/welcome-to-uniblock
  - type: Getting Started
    url: https://docs.uniblock.dev/docs/uniblock-quickstart-guide
  - type: Blog
    url: https://www.uniblock.dev/blog
  - type: Features
    url: https://www.uniblock.dev/features
  - type: Integrations
    url: https://www.uniblock.dev/integrations
  - type: Chains
    url: https://www.uniblock.dev/chains
  - type: Login
    url: https://app.uniblock.dev/
  - type: Spectral Rules
    url: rules/uniblock-rules.yml
  - type: Vocabulary
    url: vocabulary/uniblock-vocabulary.yml
  - type: Capabilities
    url: capabilities/blockchain-data.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
