---
aid: cme-group
url: https://raw.githubusercontent.com/api-evangelist/cme-group/refs/heads/main/apis.yml
name: CME Group
x-type: company
tags:
  - Capital Markets
  - Derivatives
  - Exchange
  - Financial Markets
  - Futures
  - Market Data
  - Options
  - Reference Data
  - Trading
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-23'
modified: '2026-04-23'
specificationVersion: '0.19'
description: CME Group is the world's largest derivatives exchange and operator of the CME, CBOT, NYMEX, and COMEX markets, offering futures and options across interest rates, equity indexes, foreign exchange, energy, agricultural products, and metals. CME Group exposes a portfolio of REST and streaming APIs through its Data Services Portal - including CME Reference Data API, Real-Time Futures and Options Data API, CME Term SOFR API, FedWatch API, Greeks and Implied Volatility API, EUR/USD Cross Currency Basis Index API, the CME ClearPort API for OTC trade submission, and iLink/MDP 3.0 connectivity to CME Globex for execution and market data.
apis:
  - aid: cme-group:cme-reference-data-api
    name: CME Reference Data API
    tags:
      - Instruments
      - OAuth
      - Products
      - Reference Data
      - REST
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cmegroup.com/trading/market-tech-and-data-services/cme-reference-data-api.html
    properties:
      - url: https://www.cmegroup.com/trading/market-tech-and-data-services/cme-reference-data-api.html
        type: Documentation
      - url: https://cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX/CME+Reference+Data+API+Version+3
        type: Reference
      - url: https://www.cmegroup.com/market-data/market-data-api.html
        type: Portal
    description: A set of JSON RESTful web service APIs that provide access to product and instrument reference data for CME Group, BrokerTec, EBS, hosted partners, and CME Group-cleared markets. Supports OAuth-secured access to product definitions, instrument metadata, market segment information, and trading hours used to power trading automation and risk systems.
    x-features:
      - name: Product Reference
        description: Lookup of CME Group product definitions across asset classes.
      - name: Instrument Reference
        description: Detailed instrument-level data including expirations, contract specs, and tick sizes.
      - name: Trading Hours
        description: Authoritative trading hours and holiday calendars by venue.
      - name: OAuth Authentication
        description: OAuth 2.0 secured access to reference data endpoints.
    x-useCases:
      - name: Trading Automation
        description: Hydrate algorithmic trading systems with current product and instrument metadata.
      - name: Risk and Compliance
        description: Drive risk and surveillance systems with authoritative reference data.
      - name: Order Routing
        description: Validate and route orders against the latest CME instrument definitions.
  - aid: cme-group:real-time-futures-options-api
    name: Real-Time Futures and Options Data API
    tags:
      - Futures
      - Market Data
      - Options
      - Real-Time
      - REST
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cmegroup.com/market-data/real-time-futures-and-options-data-api.html
    properties:
      - url: https://www.cmegroup.com/market-data/real-time-futures-and-options-data-api.html
        type: Documentation
      - url: https://www.cmegroup.com/market-data/market-data-api.html
        type: Portal
    description: Real-time market data API delivering futures and options price, volume, and open-interest information across CME Group markets. Available via REST and WebSocket on a monthly subscription basis from the CME Data Services portal.
    x-features:
      - name: Real-Time Quotes
        description: Streaming real-time bid/ask, last trade, and volume.
      - name: Options Chains
        description: Full options chain data including strikes and expirations.
      - name: REST + WebSocket
        description: Choice of pull-based REST or push-based WebSocket delivery.
    x-useCases:
      - name: Trading Dashboards
        description: Power proprietary trader and investor dashboards with live CME pricing.
      - name: Algo Trading
        description: Drive systematic strategies with real-time CME futures and options data.
  - aid: cme-group:cme-term-sofr-api
    name: CME Term SOFR API
    tags:
      - Benchmarks
      - Interest Rates
      - REST
      - SOFR
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cmegroup.com/market-data/cme-group-benchmark-administration/term-sofr.html
    properties:
      - url: https://www.cmegroup.com/market-data/cme-group-benchmark-administration/term-sofr.html
        type: Documentation
      - url: https://www.cmegroup.com/market-data/market-data-api.html
        type: Portal
    description: JSON-over-REST API delivering CME Term SOFR Reference Rates - the IOSCO-compliant forward-looking term Secured Overnight Financing Rate at 1-month, 3-month, 6-month, and 12-month tenors - with real-time updates and full history.
    x-features:
      - name: Term SOFR Tenors
        description: 1M, 3M, 6M, and 12M Term SOFR reference rates.
      - name: Historical Series
        description: Full history of published Term SOFR fixings for backtesting and risk.
    x-useCases:
      - name: Loan Documentation
        description: Embed Term SOFR fixings into loan and credit-agreement systems.
      - name: Risk Management
        description: Drive interest-rate risk and valuation systems with the official benchmark.
  - aid: cme-group:fedwatch-api
    name: CME FedWatch API
    tags:
      - Fed Funds
      - Market-Implied Probabilities
      - Monetary Policy
      - REST
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html
    properties:
      - url: https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html
        type: Documentation
      - url: https://www.cmegroup.com/market-data/market-data-api.html
        type: Portal
    description: 'REST API exposing the data behind the CME FedWatch Tool: market-implied probabilities of FOMC rate-change decisions derived from 30-Day Fed Funds futures pricing.'
    x-features:
      - name: FOMC Probabilities
        description: Probabilities of rate moves at upcoming FOMC meetings.
      - name: Historical Probabilities
        description: Time series of market-implied probabilities across meeting dates.
    x-useCases:
      - name: Macro Research
        description: Embed Fed Funds expectations into research and macro newsletters.
      - name: Risk Hedging
        description: Inform interest-rate hedging programs with market-implied policy paths.
  - aid: cme-group:greeks-iv-api
    name: Greeks and Implied Volatility API
    tags:
      - Greeks
      - Implied Volatility
      - Options
      - REST
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cmegroup.com/market-data/market-data-api.html
    properties:
      - url: https://www.cmegroup.com/market-data/market-data-api.html
        type: Documentation
    description: REST API delivering CME-calculated option Greeks (delta, gamma, vega, theta, rho) and implied volatility surfaces for CME Group options markets. JSON payloads accessed via the Data Services self-service API portal.
    x-features:
      - name: Greeks
        description: Delta, gamma, vega, theta, and rho per option.
      - name: Implied Volatility
        description: Implied volatility per strike and expiry.
    x-useCases:
      - name: Option Pricing
        description: Power option pricing and risk systems with CME-calculated Greeks.
      - name: Risk Distribution
        description: Distribute volatility-surface data into trading and analytics systems.
  - aid: cme-group:eurusd-basis-api
    name: EUR/USD Cross Currency Basis Index API
    tags:
      - FX
      - Index
      - REST
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cmegroup.com/market-data/market-data-api.html
    properties:
      - url: https://www.cmegroup.com/market-data/market-data-api.html
        type: Documentation
    description: JSON-over-REST API delivering the CME-administered EUR/USD Cross Currency Basis Index with real-time updates and full history.
    x-features:
      - name: Real-Time Index
        description: Real-time EUR/USD cross-currency basis index values.
      - name: Historical Series
        description: Full history of index values for backtesting and benchmarking.
    x-useCases:
      - name: Cross-Currency Hedging
        description: Drive cross-currency basis hedging strategies with the official index.
  - aid: cme-group:cme-clearport-api
    name: CME ClearPort API
    tags:
      - Clearing
      - OTC
      - Trade Submission
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cmegroup.com/clearport/clearport-api.html
    properties:
      - url: https://www.cmegroup.com/clearport/clearport-api.html
        type: Documentation
    description: The CME ClearPort API enables electronic submission of bilaterally negotiated OTC trades for clearing through CME ClearPort. Used by brokers, exchanges, and trading systems to automate trade submission and clearing workflows.
    x-features:
      - name: Trade Submission
        description: Submit OTC trades for clearing programmatically.
      - name: Block Trades
        description: Submit block trades and EFRPs (Exchange For Related Position).
    x-useCases:
      - name: Broker Workflow Automation
        description: Automate trade-capture-to-clearing workflows for OTC products.
common:
  - url: https://www.cmegroup.com
    name: CME Group Website
    type: Website
  - url: https://www.cmegroup.com/market-data/market-data-api.html
    name: Market Data APIs
    type: Portal
  - url: https://dataservices.cmegroup.com/pages/CME-Data-Via-API
    name: CME Data Services Portal
    type: Portal
  - url: https://cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX
    name: CME Group Client Systems Wiki
    type: Documentation
  - url: https://www.cmegroup.com/tools-information/webhelp/data-services-portal/Content/Onboarding%20CME%20Group%20Cloud-Based%20Market%20Data%20APIs.html
    name: Onboarding CME Group Cloud-Based Market Data APIs
    type: GettingStarted
  - url: https://www.cmegroup.com/markets.html
    name: Markets
    type: About
  - url: https://www.cmegroup.com/company/about-us.html
    name: About CME Group
    type: About
  - url: https://www.cmegroup.com/contact-us.html
    name: Contact Us
    type: Support
  - url: https://www.cmegroup.com/disclaimer.html
    name: Disclaimer
    type: TermsOfService
  - url: https://www.cmegroup.com/privacy-policy.html
    name: Privacy Policy
    type: PrivacyPolicy
  - url: https://www.cmegroup.com/openmarkets.html
    name: OpenMarkets Blog
    type: Blog
  - url: https://twitter.com/CMEGroup
    name: CME Group on X
    type: X
  - url: https://www.linkedin.com/company/cme-group/
    name: CME Group on LinkedIn
    type: LinkedIn
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
