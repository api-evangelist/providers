---
aid: quicknode
name: QuickNode
description: QuickNode is a blockchain infrastructure platform offering RPC, REST, and gRPC APIs across 77+ blockchains, plus services for IPFS pinning, streams of real-time blockchain data, webhooks, and a managed key-value store. The platform is positioned at developers building Web3 and onchain applications who need low-latency, reliable infrastructure without operating their own nodes.
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Blockchain
  - Web3
  - Infrastructure
  - RPC
  - IPFS
  - Streaming Data
  - Webhooks
  - Key-Value Store
created: '2025-02-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/quicknode/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: quicknode:core
    name: QuickNode Core API
    description: The QuickNode Core API exposes JSON-RPC, REST, and gRPC endpoints for 77+ blockchains including Ethereum, Solana, Base, Bitcoin, and more. Each customer endpoint is provisioned at a unique URL of the form https://{endpoint}.quiknode.pro/{token}/ and authenticated by the embedded token.
    humanURL: https://www.quicknode.com/
    baseURL: https://{endpoint}.quiknode.pro/{token}/
    tags:
      - Blockchain
      - RPC
      - JSON-RPC
      - Web3
    properties:
      - type: Documentation
        url: https://www.quicknode.com/docs/welcome
      - type: Ethereum
        url: https://www.quicknode.com/docs/ethereum
      - type: Solana
        url: https://www.quicknode.com/docs/solana
      - type: Bitcoin
        url: https://www.quicknode.com/docs/bitcoin
  - aid: quicknode:ipfs
    name: QuickNode IPFS API
    description: The QuickNode IPFS REST API provides managed IPFS pinning, gateway management, and account usage information so developers can keep content persistently available on the IPFS network.
    humanURL: https://www.quicknode.com/docs/ipfs
    baseURL: https://api.quicknode.com/ipfs/rest
    tags:
      - IPFS
      - Storage
      - Pinning
    properties:
      - type: Documentation
        url: https://www.quicknode.com/docs/ipfs
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/quicknode/refs/heads/main/openapi/quicknode-ipfs-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/quicknode/refs/heads/main/json-schema/quicknode-pin-schema.json
  - aid: quicknode:streams
    name: QuickNode Streams API
    description: QuickNode Streams provides customizable real-time blockchain data feeds with event-driven logic and destination integrations. The REST API supports creating, pausing, resuming, deleting, and inspecting Streams.
    humanURL: https://www.quicknode.com/docs/streams
    baseURL: https://api.quicknode.com/streams/rest/v1
    tags:
      - Streaming Data
      - Blockchain
      - Webhooks
    properties:
      - type: Documentation
        url: https://www.quicknode.com/docs/streams
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/quicknode/refs/heads/main/openapi/quicknode-streams-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/quicknode/refs/heads/main/json-schema/quicknode-stream-schema.json
  - aid: quicknode:key-value-store
    name: QuickNode Key-Value Store API
    description: QuickNode Key-Value Store is a managed key-value storage service accessible via REST, designed for storing onchain-related metadata and large datasets alongside QuickNode infrastructure.
    humanURL: https://www.quicknode.com/docs/key-value-store
    baseURL: https://api.quicknode.com/kv/rest/v1
    tags:
      - Key-Value Store
      - Storage
      - Database
    properties:
      - type: Documentation
        url: https://www.quicknode.com/docs/key-value-store
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/quicknode/refs/heads/main/openapi/quicknode-key-value-store-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/quicknode/refs/heads/main/json-schema/quicknode-kv-schema.json
  - aid: quicknode:webhooks
    name: QuickNode Webhooks
    description: QuickNode Webhooks provide real-time customizable blockchain data notifications with advanced alerting capabilities, allowing applications to react to onchain events without polling.
    humanURL: https://www.quicknode.com/docs/webhooks
    tags:
      - Webhooks
      - Real-time
      - Blockchain
    properties:
      - type: Documentation
        url: https://www.quicknode.com/docs/webhooks
  - aid: quicknode:marketplace
    name: QuickNode Marketplace Add-ons
    description: The QuickNode Marketplace lists add-ons that extend QuickNode endpoints with additional APIs (NFT, token, analytics, MEV, and more) developed by QuickNode and ecosystem partners.
    humanURL: https://www.quicknode.com/docs/marketplace-addons
    tags:
      - Marketplace
      - Add-ons
      - NFT
      - Analytics
    properties:
      - type: Documentation
        url: https://www.quicknode.com/docs/marketplace-addons
common:
  - type: Website
    url: https://www.quicknode.com/
  - type: Documentation
    url: https://www.quicknode.com/docs/welcome
  - type: Pricing
    url: https://www.quicknode.com/pricing
  - type: Sign Up
    url: https://dashboard.quicknode.com/signup
  - type: Login
    url: https://dashboard.quicknode.com/
  - type: Status
    url: https://www.quicknodestatus.com/
  - type: Blog
    url: https://www.quicknode.com/blog
  - type: GitHub
    url: https://github.com/quiknode-labs
  - type: Terms of Service
    url: https://www.quicknode.com/terms-of-service
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/quicknode/refs/heads/main/json-ld/quicknode-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
