---
aid: etherscan
name: Etherscan
description: Etherscan is the leading blockchain explorer, search, API, and analytics platform for Ethereum and other EVM-compatible chains. It allows users to easily access and explore blockchain data, including transaction histories, smart contracts, token balances, and network activity. Etherscan's unified V2 API covers 60+ chains under a single account and API key, with a free tier offering 100,000 daily calls and paid tiers up to enterprise.
url: https://raw.githubusercontent.com/api-evangelist/etherscan/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
position: Consumer
access: 3rd-Party
created: '2025-02-17'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Blockchain
  - Cryptocurrency
  - Ethereum
  - EVM
  - Web3
apis:
  - aid: etherscan:etherscan
    name: Etherscan API
    description: Etherscan API V2 provides unified access to blockchain data across Ethereum and 60+ EVM-compatible chains, including transactions, addresses, blocks, smart contracts, token transfers, and gas tracking. A single API key works across all supported networks.
    humanURL: https://docs.etherscan.io/
    baseURL: https://api.etherscan.io/v2/api
    tags:
      - Blockchain
      - Cryptocurrency
      - Ethereum
      - EVM
    properties:
      - url: https://docs.etherscan.io/
        type: Documentation
      - url: https://etherscan.io/apis
        type: Pricing
      - url: https://etherscan.io/myapikey
        type: SignUp
      - url: https://etherscan.io/apiterms
        type: Terms of Service
      - url: openapi/etherscan-openapi.yml
        type: OpenAPI
common:
  - url: https://etherscan.io/
    type: Portal
  - url: https://docs.etherscan.io/
    type: Documentation
  - url: https://etherscan.io/apis
    type: Pricing
  - url: https://etherscan.io/apiterms
    type: Terms of Service
  - url: https://etherscan.io/myapikey
    type: SignUp
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
