---
aid: argus-investor
name: Argus Investor
description: Argus Research Company is an independent equity research firm founded in 1934, providing institutional-quality investment research, stock ratings, and analyst recommendations for 500+ publicly traded companies. The firm publishes fundamental research, earnings estimates, target prices, and Buy/Hold/Sell ratings across all major sectors including healthcare, technology, financial services, and industrials. Research is distributed to institutional clients and through financial data platforms including Bloomberg, Fidelity, Schwab, and Interactive Brokers.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Equity Analysis
  - Financial Data
  - Financial Services
  - Investment Ratings
  - Stock Research
url: https://raw.githubusercontent.com/api-evangelist/argus-investor/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: argus-investor:argus-research-api
    name: Argus Research API
    description: The Argus Research API provides programmatic access to equity research reports, stock ratings, analyst recommendations, earnings estimates, target prices, and sector analysis. Used by institutional clients and financial platforms to integrate Argus Research data into investment workflows.
    humanURL: https://www.argusresearch.com/
    tags:
      - Equity Analysis
      - Financial Data
      - Investment Ratings
      - Research
      - Stock Ratings
    properties:
      - type: Documentation
        url: https://www.argusresearch.com/
      - type: Authentication
        url: https://www.argusresearch.com/
      - type: Pricing
        url: https://www.argusresearch.com/
common:
  - type: Website
    url: https://www.argusresearch.com/
  - type: Documentation
    url: https://www.argusresearch.com/
  - type: Portal
    url: https://www.argusresearch.com/
  - type: Support
    url: https://www.argusresearch.com/
  - type: Features
    data:
      - name: Fundamental Equity Research
        description: In-depth company analysis using a six-point system covering financials, management, competitive position, earnings quality, growth, and valuation.
      - name: Buy/Hold/Sell Ratings
        description: Clear investment recommendations with target prices and time horizon for 500+ publicly traded companies.
      - name: Earnings Estimates
        description: Quarterly and annual earnings per share estimates for covered securities with revision history.
      - name: Sector Analysis
        description: Regular sector-level commentary and relative weighting recommendations across major GICS sectors.
      - name: Economic Commentary
        description: Weekly macro-economic analysis covering interest rates, GDP, employment, and market conditions.
      - name: Model Portfolios
        description: Curated model portfolios across growth, income, and defensive strategies with performance tracking.
      - name: Institutional Independence
        description: No investment banking conflicts — Argus does not underwrite IPOs, broker trades, or manage money.
      - name: Market Commentary
        description: Daily and weekly market analysis including Daily Spotlight, Market Watch, and analyst quick notes.
  - type: UseCases
    data:
      - name: Portfolio Research Integration
        description: Integrate Argus ratings and estimates into portfolio management systems and research platforms.
      - name: Stock Screening
        description: Screen securities by Argus rating, sector, market cap, and analyst confidence level.
      - name: Earnings Estimate Consensus
        description: Access Argus estimates as an independent data point alongside consensus estimates.
      - name: Brokerage Research Distribution
        description: Distribute Argus research reports to brokerage clients via financial data platforms.
      - name: Compliance Monitoring
        description: Track rating changes and analyst recommendations for investment committee compliance.
  - type: Integrations
    data:
      - name: Bloomberg
        description: Argus research distributed through Bloomberg Terminal for institutional clients.
      - name: Fidelity
        description: Argus ratings and reports available on Fidelity research platform for retail and institutional investors.
      - name: Charles Schwab
        description: Argus content integrated into Schwab's research and planning tools.
      - name: Interactive Brokers
        description: Argus research available through Interactive Brokers research portal.
      - name: Reuters
        description: Argus analyst commentary and ratings cited in Reuters financial news coverage.
      - name: Yahoo Finance
        description: Argus ratings featured in Yahoo Finance analyst rating aggregations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
