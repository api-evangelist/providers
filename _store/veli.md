---
aid: veli
name: Veli
description: Veli provides crypto investment strategies via API, enabling platforms to offer smart investment solutions while handling running investment strategies, buying, selling, rebalancing, and fee collection behind the scenes. Partners retain custody and execution while Veli manages the strategy logic.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Crypto
  - DeFi
  - Finance
  - Investment
  - Portfolio Management
url: https://raw.githubusercontent.com/api-evangelist/veli/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: veli:veli
    name: Veli API
    description: 'The Veli API enables financial platforms and crypto exchanges to integrate automated investment strategies for their users. Partners keep custody and execution while Veli handles the strategy engine: portfolio creation, automated rebalancing, buy/sell execution signals, fee collection, and performance reporting. Supports index-based, theme-based, and custom strategy portfolios.'
    humanURL: https://veli.io/
    tags:
      - Crypto
      - DeFi
      - Finance
      - Investment
      - Portfolio Management
    properties:
      - type: Documentation
        url: https://veli.io/
      - type: Portal
        url: https://veli.io/
      - type: OpenAPI
        url: openapi/veli-openapi.yml
      - type: JSONSchema
        url: json-schema/veli-portfolio-schema.json
        title: Portfolio Schema
      - type: JSONSchema
        url: json-schema/veli-strategy-schema.json
        title: Strategy Schema
      - type: JSONSchema
        url: json-schema/veli-position-schema.json
        title: Position Schema
      - type: JSONSchema
        url: json-schema/veli-order-schema.json
        title: Order Schema
      - type: JSONSchema
        url: json-schema/veli-asset-allocation-schema.json
        title: Asset Allocation Schema
      - type: JSONSchema
        url: json-schema/veli-performance-response-schema.json
        title: Performance Response Schema
      - type: JSONSchema
        url: json-schema/veli-create-portfolio-request-schema.json
        title: Create Portfolio Request Schema
      - type: JSONStructure
        url: json-structure/veli-portfolio-structure.json
        title: Portfolio Structure
      - type: JSONStructure
        url: json-structure/veli-strategy-structure.json
        title: Strategy Structure
      - type: JSONStructure
        url: json-structure/veli-position-structure.json
        title: Position Structure
      - type: JSONStructure
        url: json-structure/veli-order-structure.json
        title: Order Structure
      - type: JSONStructure
        url: json-structure/veli-asset-allocation-structure.json
        title: Asset Allocation Structure
      - type: JSONStructure
        url: json-structure/veli-performance-response-structure.json
        title: Performance Response Structure
      - type: JSONStructure
        url: json-structure/veli-create-portfolio-request-structure.json
        title: Create Portfolio Request Structure
      - type: Example
        url: examples/veli-portfolio-example.json
        title: Portfolio Example
      - type: Example
        url: examples/veli-strategy-example.json
        title: Strategy Example
      - type: Example
        url: examples/veli-position-example.json
        title: Position Example
      - type: Example
        url: examples/veli-order-example.json
        title: Order Example
      - type: Example
        url: examples/veli-asset-allocation-example.json
        title: Asset Allocation Example
      - type: Example
        url: examples/veli-performance-response-example.json
        title: Performance Response Example
      - type: Example
        url: examples/veli-create-portfolio-request-example.json
        title: Create Portfolio Request Example
common:
  - type: Website
    url: https://veli.io/
  - type: Portal
    url: https://veli.io/
  - type: Documentation
    url: https://veli.io/
  - type: SpectralRules
    url: rules/veli-spectral-rules.yml
    title: Veli API Spectral Rules
  - type: Vocabulary
    url: vocabulary/veli-vocabulary.yml
    title: Veli Vocabulary
  - type: NaftikoCapability
    url: capabilities/crypto-investment.yaml
    title: Crypto Investment
  - type: Features
    data:
      - name: Automated Investment Strategies
        description: Deploy pre-built or custom crypto investment strategies including index tracking, theme portfolios, and algorithmic rebalancing.
      - name: Portfolio Rebalancing
        description: Automatic portfolio rebalancing to maintain target allocations as market prices shift, with configurable rebalancing thresholds.
      - name: Partner Custody
        description: Partners retain full custody and execution of assets while Veli provides the strategy logic, signals, and portfolio management.
      - name: Fee Collection
        description: Built-in fee management for partner platforms to charge management fees on invested assets with automated collection workflows.
      - name: Performance Reporting
        description: Portfolio performance metrics, returns, allocation breakdowns, and transaction history for investor reporting and dashboards.
  - type: UseCases
    data:
      - name: Crypto Exchange Investment Products
        description: Exchanges integrate Veli to offer automated investment portfolios (crypto index funds, theme portfolios) to their retail user base.
      - name: Neobank Wealth Features
        description: Neobanks and fintech apps add crypto investment strategy features powered by Veli while maintaining regulatory compliance and custody.
      - name: Robo-Advisor for Crypto
        description: Build automated crypto wealth management products with goal-based portfolio construction, risk profiling, and rebalancing automation.
      - name: White-Label Investment Platform
        description: Launch branded crypto investment products using Veli's strategy engine without building portfolio management infrastructure.
  - type: Integrations
    data:
      - name: Crypto Exchanges
        description: Integrate with major crypto exchanges for execution of buy/sell orders triggered by Veli strategy signals.
      - name: Portfolio Trackers
        description: Connect portfolio data to tracking apps and dashboards via Veli performance and allocation APIs.
      - name: KYC/AML Providers
        description: Integrate identity verification and compliance checks with Veli user management for regulated investment products.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
