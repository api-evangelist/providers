---
aid: chainlens
url: https://raw.githubusercontent.com/api-evangelist/chainlens/refs/heads/main/apis.yml
name: Chainlens
x-type: company
tags:
  - Analytics
  - Blockchain
  - Block Explorer
  - Cryptocurrencies
  - DeFi
  - Ethereum
  - EVM
  - NFTs
  - Smart Contracts
  - Web3
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-07'
modified: '2026-05-04'
position: Consumer
description: Chainlens, built by Web3 Labs, is a blockchain explorer and analytics platform for EVM-compatible public and private chains (Ethereum, Hyperledger Besu, Quorum, Polygon, Avalanche, BNB Chain, etc.) as well as Substrate-based chains. It combines a user-friendly block explorer with powerful REST APIs for real-time transaction monitoring, smart contract verification, token and NFT tracking (ERC-20, ERC-721, ERC-1155), and integration of on-chain data with existing analytics and reporting pipelines. The API follows the EIP-3091 block explorer route conventions and is offered both as SaaS and self-hosted.
apis:
  - aid: chainlens:chainlens-api
    name: Chainlens Blockchain Explorer API
    tags:
      - Blockchain
      - Block Explorer
      - EIP-3091
      - Events
      - NFTs
      - Smart Contracts
      - Tokens
      - Transactions
    humanURL: https://www.chainlens.com/
    baseURL: https://api.chainlens.com
    properties:
      - url: https://docs.chainlens.com/
        type: Documentation
      - url: https://www.chainlens.com/features/blockchain-api
        type: Overview
      - url: openapi/chainlens-openapi.yml
        type: OpenAPI
      - url: https://eips.ethereum.org/EIPS/eip-3091
        type: Specification
    description: The Chainlens REST API exposes block explorer data for EVM chains including transactions, internal transactions, events, blocks, addresses, tokens, NFTs, and smart contract metadata. Endpoints follow OpenAPI 3 conventions and the EIP-3091 block explorer route standard, supporting real-time on-chain analytics, wallet inspection, contract verification look-up, and reporting pipelines.
common:
  - type: Website
    url: https://www.chainlens.com/
  - type: Documentation
    url: https://docs.chainlens.com/
  - type: GettingStarted
    url: https://www.chainlens.com/documentation-categories/getting-started
  - type: SignUp
    url: https://www.chainlens.com/free-sign-up
  - type: Pricing
    url: https://www.chainlens.com/plans
  - type: Blog
    url: https://www.chainlens.com/blog
  - type: GitHub
    url: https://github.com/web3labs/chainlens-free
  - type: ParentCompany
    url: https://www.web3labs.com/
  - type: Contact
    url: https://www.chainlens.com/contact
  - type: TermsOfService
    url: https://www.chainlens.com/terms
  - type: PrivacyPolicy
    url: https://www.chainlens.com/privacy-policy
  - type: LinkedIn
    url: https://www.linkedin.com/company/web3labs/
  - type: X
    url: https://x.com/web3labs
  - name: Features
    type: Features
    data:
      - 'Chainlens: free public API'
      - Free tier available; commercial use requires Web3 enterprise contracts.
      - 'Public URL: https://chainlens.com/'
    sources:
      - https://chainlens.com/
    updated: '2026-05-04'
  - name: UseCases
    type: UseCases
    data:
      - name: Real-Time Transaction Monitoring
      - name: Smart Contract Event Monitoring
      - name: On-Chain Asset Tracking
      - name: Wallet Portfolio Analytics
      - name: Regulatory Reporting
      - name: Compliance Monitoring
      - name: DeFi Analytics
      - name: NFT Collection Analytics
      - name: Enterprise Blockchain Visibility
      - name: Custom Analytics Integration
  - name: Integrations
    type: Integrations
    data:
      - name: Ethereum
      - name: Hyperledger Besu
      - name: Quorum
      - name: Polygon
      - name: Avalanche
      - name: BNB Chain
      - name: Arbitrum
      - name: Optimism
      - name: Base
      - name: Substrate
      - name: Ink! Smart Contracts
      - name: Web3j
      - name: MetaMask
      - name: Grafana
      - name: Elasticsearch
      - name: Kafka
  - name: Plans
    type: Plans
    data:
      - name: Free
      - name: Developer
      - name: Team
      - name: Enterprise
      - name: Self-Hosted
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
