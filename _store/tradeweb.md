---
aid: tradeweb
name: Tradeweb
description: Tradeweb Markets is a leading global operator of electronic marketplaces for rates, credit, equities, and money markets. The platform provides APIs for electronic trading execution, straight-through processing, market data, trade reporting, and integration with order management and risk systems across more than 40 fixed income and derivatives products.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/tradeweb/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Electronic Trading
  - Financial Markets
  - Fixed Income
  - Market Data
  - OTC Trading
apis:
  - aid: tradeweb:trading-api
    name: Tradeweb Trading API
    description: Electronic trading API for executing trades across fixed income, derivatives, and ETF markets. Supports RFQ (Request for Quote), click-to-trade, and automated execution via AiEX (Automated Intelligent Execution) workflows.
    humanURL: https://www.tradeweb.com/our-markets/institutional/integration/
    baseURL: https://api.tradeweb.com
    tags:
      - Electronic Trading
      - Execution
      - Fixed Income
      - RFQ
    properties:
      - type: Documentation
        url: https://www.tradeweb.com/our-markets/institutional/integration/
  - aid: tradeweb:python-api
    name: Tradeweb Python API
    description: Python API enabling seamless integration between trading strategies and Tradeweb execution. Allows direct connection between Python-coded trading models and Tradeweb for solicited workflows and Automated Intelligent Execution (AiEX).
    humanURL: https://www.tradeweb.com/our-markets/institutional/integration/
    baseURL: https://api.tradeweb.com
    tags:
      - Automation
      - Python
      - Quantitative Trading
      - SDK
    properties:
      - type: Documentation
        url: https://www.tradeweb.com/our-markets/institutional/integration/
  - aid: tradeweb:fix-api
    name: Tradeweb FIX API
    description: FIX protocol connectivity for electronic trading integration with order management systems, risk systems, and third-party trading platforms. Industry-standard FIX messaging for trade execution and straight-through processing.
    humanURL: https://www.tradeweb.com/our-markets/institutional/integration/
    baseURL: fix://tradeweb.com
    tags:
      - FIX Protocol
      - Integration
      - OMS
      - STP
    properties:
      - type: Documentation
        url: https://www.tradeweb.com/our-markets/institutional/integration/
  - aid: tradeweb:market-data-api
    name: Tradeweb Market Data API
    description: Real-time and historical market data API providing independent pricing information and benchmark OTC pricing data across more than 20 asset classes including government bonds, credit, swaps, and ETFs.
    humanURL: https://www.lseg.com/en/data-analytics/financial-data/pricing-and-market-data/fixed-income-pricing-data/tradeweb-data
    baseURL: https://api.tradeweb.com/data
    tags:
      - Benchmark Data
      - Market Data
      - OTC Pricing
      - Real-Time Data
    properties:
      - type: Documentation
        url: https://www.lseg.com/en/data-analytics/financial-data/pricing-and-market-data/fixed-income-pricing-data/tradeweb-data
  - aid: tradeweb:apa-api
    name: Tradeweb APA Trade Reporting API
    description: Approved Publication Arrangement (APA) API enabling market participants to meet MiFID II post-trade transparency requirements. Supports real-time trade reporting across all mandated instrument classes.
    humanURL: https://www.tradeweb.com/our-markets/data-analytics/trade-reporting-services-apa/
    baseURL: https://apa.tradeweb.com/api
    tags:
      - APA
      - Compliance
      - MiFID II
      - Trade Reporting
      - Transparency
    properties:
      - type: Documentation
        url: https://www.tradeweb.com/our-markets/data-analytics/trade-reporting-services-apa/
common:
  - type: Portal
    url: https://www.tradeweb.com/
  - type: Documentation
    url: https://www.tradeweb.com/our-markets/institutional/integration/
  - type: Support
    url: https://www.tradeweb.com/contact/
  - type: Blog
    url: https://www.tradeweb.com/newsroom/media-center/insights/
  - type: TermsOfService
    url: https://www.tradeweb.com/terms-of-use/
  - type: PrivacyPolicy
    url: https://www.tradeweb.com/privacy-policy/
  - type: Features
    data:
      - name: Request for Quote (RFQ)
        description: Send RFQs to multiple dealers simultaneously for competitive pricing on fixed income and derivatives.
      - name: Automated Intelligent Execution (AiEX)
        description: Automated trade execution with pre-defined rules for straight-through processing.
      - name: Click-to-Trade
        description: One-click trade execution on streaming dealer prices.
      - name: Market Data
        description: Real-time and historical pricing data across 20+ asset classes as an independent benchmark source.
      - name: Trade Reporting (APA)
        description: MiFID II compliant post-trade transparency reporting via Approved Publication Arrangement.
      - name: Straight-Through Processing
        description: Automated post-trade processing from execution to settlement with STP vendor integration.
      - name: Python API
        description: Direct connection between Python trading models and Tradeweb execution.
      - name: FIX Connectivity
        description: Industry-standard FIX protocol integration with OMS, EMS, and risk systems.
      - name: Multi-Asset Coverage
        description: Trading across rates, credit, equities, ETFs, and money markets on a single platform.
      - name: Pre-Trade Analytics
        description: Transaction cost analysis and liquidity analytics before trade execution.
  - type: UseCases
    data:
      - name: Institutional Fixed Income Trading
        description: Execute government bond, corporate bond, and municipal bond trades electronically.
      - name: Derivatives Execution
        description: Trade interest rate swaps, credit default swaps, and other OTC derivatives.
      - name: ETF Trading
        description: Access institutional ETF liquidity with RFQ and portfolio trading workflows.
      - name: Algorithmic Trading
        description: Connect Python-based algo strategies directly to Tradeweb execution via API.
      - name: OMS Integration
        description: Integrate Tradeweb execution with order management and portfolio management systems.
      - name: Regulatory Reporting
        description: Meet MiFID II post-trade transparency requirements via APA trade reporting.
      - name: Market Data Analytics
        description: Access independent OTC pricing data for valuation, risk, and compliance.
      - name: Treasury Management
        description: Execute US Treasury and government bond trades across CLOB and RFQ protocols.
  - type: Solutions
    data:
      - name: Tradeweb Institutional
        description: Electronic marketplace for buy-side institutional trading across fixed income and derivatives.
      - name: Tradeweb Wholesale (Dealerweb)
        description: Inter-dealer marketplace for wholesale fixed income and derivatives trading.
      - name: Tradeweb Retail
        description: Electronic marketplace for retail-sized fixed income trading.
      - name: Tradeweb Data & Analytics
        description: Market data, pricing, and analytics services including APA trade reporting.
  - type: Spectral
    url: rules/tradeweb-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/tradeweb-vocabulary.yaml
  - type: JSONLd
    url: json-ld/tradeweb-context.jsonld
  - type: JSONSchema
    url: json-schema/tradeweb-trade-schema.json
  - type: JSONSchema
    url: json-schema/tradeweb-rfq-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
