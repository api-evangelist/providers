---
aid: ethereum
name: Ethereum
description: Ethereum is a decentralized, open-source blockchain platform that supports smart contracts - self-executing programs that run on its distributed network. It is the foundation for a vast ecosystem of decentralized applications (dApps), tokens, DeFi protocols, and NFTs, and uses a proof-of-stake consensus mechanism.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Blockchain
  - DeFi
  - Ethereum
  - JSON-RPC
  - Smart Contracts
  - Web3
url: https://ethereum.org
created: '2025-01-01'
modified: '2026-04-28'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
apis:
  - aid: ethereum:ethereum-json-rpc-api
    name: Ethereum JSON-RPC API
    description: The standard JSON-RPC interface for interacting with Ethereum nodes, providing methods for querying blockchain state, sending transactions, managing accounts, and interacting with smart contracts.
    humanURL: https://ethereum.org/en/developers/docs/apis/json-rpc/
    tags:
      - Blockchain
      - JSON-RPC
      - Smart Contracts
    properties:
      - type: Documentation
        url: https://ethereum.org/en/developers/docs/apis/json-rpc/
      - type: OpenAPI
        url: openapi/ethereum-json-rpc-openapi.yml
common:
  - type: JSONSchema
    url: json-schema/ethereum-json-rpc-schema.json
  - type: JSON-LD
    url: json-ld/ethereum-json-rpc-context.jsonld
  - type: Website
    url: https://ethereum.org
  - type: Documentation
    url: https://ethereum.org/en/developers/docs/
  - type: GettingStarted
    url: https://ethereum.org/en/developers/
  - type: GitHubOrganization
    url: https://github.com/ethereum
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
