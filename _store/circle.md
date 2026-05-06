---
aid: circle
name: Circle
url: https://raw.githubusercontent.com/api-evangelist/circle/refs/heads/main/apis.yml
tags:
  - Blockchain
  - Compliance
  - Cross-Chain
  - Currency
  - Money
  - Payments
  - Stablecoin
  - Transfers
  - USDC
  - Wallets
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-07'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: Circle Internet Financial is the issuer of USDC and EURC and operates a developer platform for moving regulated stablecoin money across the internet. Their APIs cover programmable wallets (developer- and user-controlled), gas sponsorship, the Cross-Chain Transfer Protocol (CCTP), Gateway unified balances, the Smart Contract Platform, the Circle Payments Network (CPN) for cross-border payments, compliance, StableFX trading on Arc, and xReserve for issuing USDC-backed stablecoins.
apis:
  - aid: circle:developer-controlled-wallets
    name: Developer-Controlled Wallets
    tags:
      - Custody
      - USDC
      - Wallets
    humanURL: https://developers.circle.com/w3s/programmable-wallets
    baseURL: https://api.circle.com/v1/w3s
    properties:
      - url: https://developers.circle.com/w3s/programmable-wallets
        type: Documentation
      - url: https://developers.circle.com/openapi/developer-controlled-wallets.yaml
        type: OpenAPI
    description: Create and manage server-side wallets where the application controls private keys via Circle's secure key management. Supports balances, transfers, signing, and webhook notifications.
  - aid: circle:user-controlled-wallets
    name: User-Controlled Wallets
    tags:
      - Custody
      - End-User
      - USDC
      - Wallets
    humanURL: https://developers.circle.com/w3s/user-controlled-wallets
    baseURL: https://api.circle.com/v1/w3s
    properties:
      - url: https://developers.circle.com/w3s/user-controlled-wallets
        type: Documentation
      - url: https://developers.circle.com/openapi/user-controlled-wallets.yaml
        type: OpenAPI
    description: Create wallets that end users control via PIN, biometrics, or social recovery while Circle handles the cryptography. Used to embed non-custodial USDC wallets directly inside consumer apps.
  - aid: circle:gas-station
    name: Gas Station and Paymaster
    tags:
      - Gas Sponsorship
      - Paymaster
      - USDC
    humanURL: https://developers.circle.com/w3s/gas-station
    baseURL: https://api.circle.com/v1/w3s
    properties:
      - url: https://developers.circle.com/w3s/gas-station
        type: Documentation
    description: Sponsor gas fees on behalf of users or let users pay gas in USDC via Circle Paymaster, removing native-token friction from onboarding.
  - aid: circle:cctp
    name: Cross-Chain Transfer Protocol (CCTP)
    tags:
      - Bridging
      - Cross-Chain
      - USDC
    humanURL: https://developers.circle.com/cctp
    properties:
      - url: https://developers.circle.com/cctp
        type: Documentation
      - url: https://developers.circle.com/openapi/cctp.yaml
        type: OpenAPI
    description: Burn-and-mint protocol for moving native USDC between supported blockchains without wrapped assets. Provides REST endpoints for attestations and a Bridge Kit SDK for frontend integration.
  - aid: circle:gateway
    name: Circle Gateway
    tags:
      - Cross-Chain
      - Liquidity
      - USDC
    humanURL: https://developers.circle.com/gateway
    properties:
      - url: https://developers.circle.com/gateway
        type: Documentation
      - url: https://developers.circle.com/openapi/gateway.yaml
        type: OpenAPI
    description: Unified USDC balance across multiple EVM chains and support for nanopayments down to $0.000001 of USDC.
  - aid: circle:smart-contract-platform
    name: Smart Contract Platform
    tags:
      - Contracts
      - EVM
      - Web3
    humanURL: https://developers.circle.com/w3s/smart-contract-platform
    baseURL: https://api.circle.com/v1/w3s
    properties:
      - url: https://developers.circle.com/w3s/smart-contract-platform
        type: Documentation
      - url: https://developers.circle.com/openapi/smart-contract-platform.yaml
        type: OpenAPI
    description: Deploy, query, and interact with smart contracts across supported blockchains, including ERC-20 and ERC-721 templates and arbitrary contract calls.
  - aid: circle:cpn
    name: Circle Payments Network (CPN)
    tags:
      - Cross-Border
      - Payments
      - Settlement
    humanURL: https://developers.circle.com/cpn
    properties:
      - url: https://developers.circle.com/cpn
        type: Documentation
      - url: https://developers.circle.com/openapi/cpn-ofi.yaml
        type: OpenAPI
    description: A network for regulated financial institutions to settle cross-border payments using USDC, with originating and beneficiary financial institution (OFI/BFI) APIs.
  - aid: circle:compliance-engine
    name: Compliance Engine
    tags:
      - AML
      - Compliance
      - Risk
    humanURL: https://developers.circle.com/w3s/compliance-engine
    properties:
      - url: https://developers.circle.com/w3s/compliance-engine
        type: Documentation
      - url: https://developers.circle.com/openapi/compliance.yaml
        type: OpenAPI
    description: Screen wallet addresses and transactions against sanctions lists and risk signals; configure rule sets and review queues for AML programs.
  - aid: circle:stablefx
    name: StableFX
    tags:
      - Arc
      - FX
      - Trading
    humanURL: https://developers.circle.com/stablefx
    properties:
      - url: https://developers.circle.com/stablefx
        type: Documentation
      - url: https://developers.circle.com/openapi/stablefx.yaml
        type: OpenAPI
    description: Stablecoin foreign-exchange trading API on the Arc blockchain for converting between USDC, EURC, and other regulated stablecoins.
  - aid: circle:xreserve
    name: xReserve
    tags:
      - Issuance
      - Reserves
      - Stablecoin
    humanURL: https://developers.circle.com/xreserve
    properties:
      - url: https://developers.circle.com/xreserve
        type: Documentation
      - url: https://developers.circle.com/openapi/xreserve.yaml
        type: OpenAPI
    description: Issue and redeem regulated stablecoins backed by USDC reserves; manage minting, burning, and reserve attestations.
common:
  - type: Website
    url: https://www.circle.com/
  - type: Portal
    url: https://developers.circle.com/
  - type: Console
    url: https://console.circle.com/
  - type: Authentication
    url: https://developers.circle.com/w3s/authentication
  - type: Getting Started
    url: https://developers.circle.com/w3s/getting-started
  - type: Status
    url: https://status.circle.com/
  - type: Support
    url: https://support.usdc.circle.com/
  - type: Blog
    url: https://www.circle.com/blog
  - type: Community
    url: https://discord.com/invite/buildoncircle
  - type: GitHub Organization
    url: https://github.com/circlefin
  - type: Privacy Policy
    url: https://www.circle.com/legal/privacy-policy
  - type: Terms of Service
    url: https://www.circle.com/legal/terms-of-service
  - type: JSON-LD
    url: json-ld/circle-context.jsonld
  - type: JSONSchema
    url: json-schema/circle-wallet-schema.json
  - type: JSONSchema
    url: json-schema/circle-transaction-schema.json
  - type: Spectral
    url: rules/circle-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/circle-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
