---
aid: blockfrost
url: https://raw.githubusercontent.com/api-evangelist/blockfrost/refs/heads/main/apis.yml
name: Blockfrost
description: Blockfrost is a RESTful API service providing access to the Cardano blockchain and its ecosystem. It serves as an infrastructure layer for developers building dApps, wallets, NFT platforms, DeFi protocols, and analytics tools on Cardano. Blockfrost provides endpoints for querying blocks, transactions, accounts, addresses, native assets, epochs, governance data, and IPFS storage, supporting both mainnet and testnet networks.
tags:
  - Blockchain
  - Cardano
  - Cryptocurrency
  - DApps
  - NFT
  - Web3
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-09-27'
modified: '2026-04-19'
position: Consuming
specificationVersion: '0.19'
apis:
  - aid: blockfrost:blockfrost
    name: Blockfrost API
    description: RESTful API for interacting with the Cardano blockchain and parts of its ecosystem. Provides access to blocks, transactions, accounts, addresses, native assets, epochs, governance data, and IPFS. Requires a project_id obtained from blockfrost.io for authentication. Supports Cardano mainnet, preview testnet, preprod testnet, and Midnight mainnet networks.
    humanURL: https://blockfrost.io/
    tags:
      - Blockchain
      - Cardano
      - Cryptocurrency
      - Web3
    properties:
      - type: Documentation
        url: https://docs.blockfrost.io/
      - type: OpenAPI
        url: openapi/blockfrost-openapi.yaml
      - type: NaftikoCapability
        url: capabilities/blockfrost-cardano-explorer.yaml
      - type: SpectralRules
        url: rules/blockfrost-spectral-rules.yml
      - type: Vocabulary
        url: vocabulary/blockfrost-vocabulary.yaml
common:
  - type: Website
    url: https://blockfrost.io/
  - type: Documentation
    url: https://blockfrost.dev/
  - type: GettingStarted
    url: https://blockfrost.dev/overview/getting-started
  - type: Pricing
    url: https://blockfrost.io/#pricing
  - type: StatusPage
    url: https://status.blockfrost.io/
  - type: Support
    url: https://blockfrost.dev/support
  - type: GitHubOrganization
    url: https://github.com/blockfrost
  - type: Discord
    url: https://discord.gg/inputoutput
  - type: TermsOfService
    url: https://blockfrost.io/terms
  - type: PrivacyPolicy
    url: https://blockfrost.io/privacy
  - type: Login
    url: https://blockfrost.io/auth/signin
  - type: SDK
    url: https://blockfrost.dev/sdks
    title: Official SDKs
  - type: SpectralRules
    url: rules/blockfrost-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/blockfrost-cardano-explorer.yaml
  - type: Vocabulary
    url: vocabulary/blockfrost-vocabulary.yaml
  - type: Features
    data:
      - name: Cardano Blockchain Access
        description: Query blocks, transactions, slots, epochs, accounts, and addresses on the Cardano mainnet and testnet networks.
      - name: Native Asset Support
        description: Full support for Cardano native assets including fungible tokens, NFTs, and multi-asset UTXOs with on-chain metadata (CIP-25, CIP-68).
      - name: Stake Pool and Delegation Data
        description: Query stake pool information, delegation history, rewards, and account activity for Cardano staking workflows.
      - name: Governance Data
        description: Access Cardano governance data including proposals, DRep registrations, and voting activity introduced in the Conway era.
      - name: IPFS Integration
        description: Built-in IPFS API for storing and retrieving off-chain NFT metadata and other content via Blockfrost's IPFS gateway.
      - name: Multi-Network Support
        description: Single API surface covering Cardano mainnet, preview testnet, preprod testnet, and the Midnight blockchain.
      - name: Transaction Submission
        description: Submit signed transactions directly to the Cardano network via the Blockfrost API without running a local node.
  - type: UseCases
    data:
      - name: dApp Development
        description: Developers build Cardano dApps using Blockfrost to query blockchain state, submit transactions, and interact with smart contracts.
      - name: NFT Platform Integration
        description: NFT marketplaces and minting platforms use Blockfrost to track asset minting, transfers, and metadata across the Cardano network.
      - name: DeFi Protocol Building
        description: DeFi protocols integrate Blockfrost to monitor liquidity pool states, track DEX transactions, and manage smart contract interactions.
      - name: Wallet Development
        description: Cardano wallet applications use Blockfrost to fetch UTXOs, balances, transaction history, and submit transactions.
      - name: Blockchain Analytics
        description: Analytics platforms query Blockfrost for on-chain data including block history, epoch statistics, and network activity metrics.
  - type: Integrations
    data:
      - name: Mesh SDK
        description: The Mesh JavaScript/TypeScript SDK integrates with Blockfrost as a provider for Cardano dApp development.
      - name: Lucid Evolution
        description: Lucid Evolution (TypeScript library) supports Blockfrost as a blockchain provider for transaction building and submission.
      - name: PyCardano
        description: PyCardano Python library uses Blockfrost as a chain context provider for Cardano smart contract development.
      - name: Cardano Serialization Library
        description: The Cardano Serialization Library (CSL) pairs with Blockfrost for transaction construction and UTXO management.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
