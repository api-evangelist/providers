---
aid: bloomberg-tradebook
name: Bloomberg Tradebook
description: Bloomberg Tradebook is an electronic brokerage and agency trading platform offering execution services across global equities, futures, options, and foreign exchange. Founded in 1996 as a Bloomberg LP subsidiary, Tradebook provides algorithmic trading, direct market access, and transaction cost analysis (TCA) via FIX protocol connectivity and integration with Bloomberg Terminal workflows.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-tradebook/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Tradebook
  - Electronic Trading
  - Equities
  - Futures
  - Options
  - FX
  - Agency Brokerage
  - Bloomberg
apis:
  - aid: bloomberg-tradebook:tradebook-fix-api
    name: Bloomberg Tradebook FIX API
    description: FIX protocol connectivity to Bloomberg Tradebook for electronic order routing, execution reporting, and position updates across equities, futures, options, and FX markets. Supports FIX 4.2, 4.4, and 5.0.
    humanURL: https://www.bloomberg.com/professional/product/tradebook/
    baseURL: fixs://tradebook.bloomberg.com:8194
    tags:
      - FIX Protocol
      - Order Routing
      - Electronic Trading
      - Equities
      - Futures
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/product/tradebook/
  - aid: bloomberg-tradebook:emsx-tradebook-integration
    name: Bloomberg EMSX-Tradebook Integration
    description: Integration between Bloomberg's Electronic Order Management System (EMSX) and Tradebook for seamless order routing from the Bloomberg Terminal to Tradebook execution desks and algorithms.
    humanURL: https://www.bloomberg.com/professional/solution/emsx/
    baseURL: blpapi://localhost:8194
    tags:
      - EMSX
      - Terminal Integration
      - Order Management
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/emsx/
  - aid: bloomberg-tradebook:tradebook-fx
    name: Bloomberg Tradebook FX Marketplace
    description: Bloomberg Tradebook's foreign exchange marketplace for electronic FX spot, forward, and swap execution. Launched in 2007, providing competitive FX pricing and execution from major liquidity providers.
    humanURL: https://www.bloomberg.com/professional/product/tradebook/
    baseURL: https://fx.tradebook.bloomberg.com
    tags:
      - FX
      - Foreign Exchange
      - Spot
      - Forward
      - Swap
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/product/tradebook/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://www.bloomberg.com/professional/product/tradebook/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Features
    data:
      - name: Algorithmic Trading
        description: Access to Tradebook's proprietary and third-party trading algorithms.
      - name: Direct Market Access
        description: DMA connectivity to global equity and futures exchanges.
      - name: Transaction Cost Analysis
        description: TCA reporting for evaluating execution quality and broker performance.
      - name: FIX Connectivity
        description: Standard FIX protocol integration for order routing and execution.
      - name: FX Execution
        description: Electronic FX marketplace for competitive spot and forward execution.
      - name: Global Execution
        description: Access to global equity, futures, options, and FX markets through one platform.
  - type: UseCases
    data:
      - name: Equity Execution
        description: Execute equity orders globally with algorithmic and DMA strategies.
      - name: Futures Trading
        description: Trade global futures contracts through Tradebook's electronic platform.
      - name: FX Execution
        description: Execute FX transactions competitively through Tradebook's FX marketplace.
      - name: Execution Quality Measurement
        description: Analyze execution quality and broker performance with TCA reporting.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
