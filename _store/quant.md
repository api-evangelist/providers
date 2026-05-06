---
aid: quant
name: Quant Network
description: Quant Network is a blockchain interoperability company whose Overledger platform provides APIs to issue, connect, and monitor digital assets, smart contracts, transactions, and accounts across multiple distributed ledger technologies without requiring blockchain expertise.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Blockchain
  - Distributed Ledger
  - Interoperability
  - Overledger
  - Smart Contracts
  - Digital Assets
  - Web3
created: '2025-02-12'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: quant:overledger
    name: Quant Overledger API
    description: Overledger APIs provide a single unified interface for building cross-ledger applications, including endpoints for accounts, addresses, keys, balances, transactions, smart contracts (deploy, read, write, NFT, events), webhooks, asset transfers, bridges, and a digital currency sandbox spanning multiple supported blockchains.
    humanURL: https://docs.overledger.dev/
    tags:
      - Blockchain
      - Interoperability
      - Smart Contracts
      - Digital Assets
      - Webhooks
    properties:
      - type: Documentation
        url: https://docs.overledger.dev/
      - type: API Documentation
        url: https://docs.overledger.dev/reference/how-to-access-overledger-apis
      - type: Getting Started
        url: https://docs.overledger.dev/docs/getting-started
      - type: Authentication
        url: https://docs.overledger.dev/reference/getaccesstoken
      - type: Changelog
        url: https://docs.overledger.dev/changelog
      - type: SDK
        url: https://github.com/quantnetwork/overledger-sdk-javascript-v2
common:
  - type: Website
    url: https://www.quant.network/
  - type: Developer Portal
    url: https://docs.overledger.dev/
  - type: GitHub Organization
    url: https://github.com/quantnetwork
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
