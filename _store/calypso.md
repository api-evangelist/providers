---
aid: calypso
name: Calypso
description: APIs and developer resources for Nasdaq Calypso (formerly Adenza / Calypso Technology), a cross-asset front-to-back capital markets technology platform for trading, risk management, collateral, treasury, processing, and accounting used by banks, asset managers, central banks, and clearing houses worldwide.
image: https://www.calypso.com/favicon.ico
url: https://raw.githubusercontent.com/api-evangelist/calypso/refs/heads/main/apis.yml
type: Index
created: '2024-01-01'
modified: '2026-04-23'
specificationVersion: '0.19'
tags:
  - Capital Markets
  - Collateral Management
  - Enterprise Software
  - Financial Technology
  - Post-Trade Processing
  - Risk Management
  - Trading
  - Treasury
apis:
  - aid: calypso:calypso-core-api
    name: Calypso Core API
    description: Main REST API for the Nasdaq Calypso platform. Provides programmatic access to remotely control calls to the Calypso platform from other software, enabling regulatory analytics, current limits usage queries, and pre-deal limit checks for enhanced operating flexibility across capital markets operations.
    image: https://www.calypso.com/favicon.ico
    humanURL: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso
    baseURL: https://api.calypso.example.com/v1
    tags:
      - Capital Markets
      - REST API
      - Risk Management
      - Trading
    properties:
      - type: Documentation
        url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso
  - aid: calypso:calypso-front-office-api
    name: Calypso Front Office API
    description: Provides programmatic access to Calypso front office capabilities including real-time portfolio insights, instant order generation, pricing, live risk and P&L monitoring, trade entry, and scenario analysis across multiple asset classes for trading desks and portfolio managers.
    image: https://www.calypso.com/favicon.ico
    humanURL: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/front-office
    baseURL: https://api.calypso.example.com/v1
    tags:
      - Front Office
      - Portfolio Management
      - Pricing
      - Trading
    properties:
      - type: Documentation
        url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/front-office
  - aid: calypso:calypso-middle-office-trading-risk-api
    name: Calypso Middle Office and Trading Risk API
    description: Enables integration with Calypso middle office and trading risk capabilities including market risk, credit risk, clearing risk, and liquidity risk metrics. Supports VaR calculations, stress testing, back testing, and compliance management based on internal and regulatory mandates.
    image: https://www.calypso.com/favicon.ico
    humanURL: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/middle-office-trading-risk
    baseURL: https://api.calypso.example.com/v1
    tags:
      - Compliance
      - Credit Risk
      - Market Risk
      - Risk Management
    properties:
      - type: Documentation
        url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/middle-office-trading-risk
  - aid: calypso:calypso-treasury-api
    name: Calypso Treasury API
    description: Provides access to Calypso treasury management capabilities for front-to-back treasury operations including cross-asset trading decisions, analytics, risk tools, real-time monitoring, and management of treasury positions across cash and derivatives products.
    image: https://www.calypso.com/favicon.ico
    humanURL: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/treasury
    baseURL: https://api.calypso.example.com/v1
    tags:
      - Asset Management
      - Cash Management
      - Liquidity
      - Treasury
    properties:
      - type: Documentation
        url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/treasury
  - aid: calypso:calypso-collateral-margin-securities-finance-api
    name: Calypso Collateral, Margin and Securities Finance API
    description: Provides integration with Calypso collateral management, margin calculation, and securities financing capabilities. Supports management of exposures for cleared and uncleared trades, real-time collateral transfers, intraday margining, and automated margin call processing.
    image: https://www.calypso.com/favicon.ico
    humanURL: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/collateral-margin-securities-finance
    baseURL: https://api.calypso.example.com/v1
    tags:
      - Collateral Management
      - Margin
      - Risk
      - Securities Finance
    properties:
      - type: Documentation
        url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/collateral-margin-securities-finance
  - aid: calypso:calypso-clearing-api
    name: Calypso Clearing API
    description: Provides access to Calypso integrated cross-asset OTC and exchange-traded derivatives clearing capabilities including trade connectivity, processing, collateral management and optimization, margin calculation, and reconciliation for clearing houses and clearing members.
    image: https://www.calypso.com/favicon.ico
    humanURL: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/clearing
    baseURL: https://api.calypso.example.com/v1
    tags:
      - Clearing
      - Derivatives
      - Exchange Traded
      - OTC
    properties:
      - type: Documentation
        url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/clearing
  - aid: calypso:calypso-post-trade-processing-api
    name: Calypso Post-Trade Processing API
    description: Enables integration with Calypso back-office processing capabilities including trade comparison, netting, settlement, profitability analysis, corporate actions, accounting, and regulatory reporting. Supports full straight-through processing with exception-based user interaction.
    image: https://www.calypso.com/favicon.ico
    humanURL: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/post-trade-processing
    baseURL: https://api.calypso.example.com/v1
    tags:
      - Accounting
      - Back Office
      - Post-Trade
      - Settlement
    properties:
      - type: Documentation
        url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/post-trade-processing
  - aid: calypso:calypso-reserve-monetary-policy-api
    name: Calypso Reserve and Monetary Policy Management API
    description: Provides integration capabilities for central bank reserve management and monetary policy operations on the Calypso platform. Supports monitoring and managing debt and liquidity, regulating financial system liquidity, and responding to market fluctuations for central banks.
    image: https://www.calypso.com/favicon.ico
    humanURL: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/reserve-and-monetary-policy-management
    baseURL: https://api.calypso.example.com/v1
    tags:
      - Central Banking
      - Liquidity
      - Monetary Policy
      - Reserve Management
    properties:
      - type: Documentation
        url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/reserve-and-monetary-policy-management
common:
  - type: Portal
    url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso
  - type: Documentation
    url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso
  - type: Website
    url: https://www.calypso.com/
  - type: Support
    url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/resources
  - type: Learning
    url: https://learncalypso.nasdaq.com/
  - type: Certification
    url: https://www.nasdaq.com/solutions/fintech/services/education-learning/nasdaq-calypso/certification
  - type: Training
    url: https://www.nasdaq.com/solutions/fintech/services/education-learning/nasdaq-calypso
  - type: Privacy Policy
    url: https://www.calypso.com/Privacy
  - type: Terms of Service
    url: https://km.calypso.com/pages/terms
  - type: LinkedIn
    url: https://www.linkedin.com/company/calypso-technology
  - type: Wikipedia
    url: https://en.wikipedia.org/wiki/Adenza
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
include: []
---
