---
aid: bloomberg-valuation-service-bval
name: Bloomberg Valuation Service (BVAL)
description: Bloomberg Valuation Service (BVAL) is Bloomberg's evaluated pricing service providing independent fair value prices for over 2.5 million fixed income securities including corporate bonds, municipal bonds, government securities, structured products, and derivatives. BVAL prices are designed for portfolio valuation, NAV calculation, regulatory reporting, and risk management, with full transparency on pricing methodology and inputs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-valuation-service-bval/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - BVAL
  - Evaluated Pricing
  - Fixed Income
  - Fair Value
  - Bond Pricing
  - Municipal Bonds
  - Structured Products
  - Bloomberg
apis:
  - aid: bloomberg-valuation-service-bval:bval-api
    name: Bloomberg BVAL Pricing API
    description: Access BVAL evaluated prices, yield curves, spread data, and pricing transparency metadata for fixed income securities via BLPAPI and Data License. Supports corporate bonds, municipal bonds, government bonds, ABS, MBS, and other structured products.
    humanURL: https://www.bloomberg.com/professional/solution/bval/
    baseURL: blpapi://localhost:8194
    tags:
      - Evaluated Pricing
      - Fixed Income
      - BVAL
      - Bond Pricing
      - Fair Value
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/bval/
  - aid: bloomberg-valuation-service-bval:bval-muni
    name: Bloomberg BVAL Municipal Bond Pricing
    description: Evaluated pricing for US municipal bonds with BVAL's deep munis coverage providing independent prices for general obligation, revenue, and specialty municipal securities. Widely used for NAV calculation and portfolio valuation.
    humanURL: https://www.bloomberg.com/professional/solution/bval/
    baseURL: blpapi://localhost:8194
    tags:
      - Municipal Bonds
      - Munis
      - NAV
      - Portfolio Valuation
      - Tax-Exempt
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/bval/
  - aid: bloomberg-valuation-service-bval:bval-structured-products
    name: Bloomberg BVAL Structured Product Pricing
    description: Evaluated pricing for complex structured finance instruments including ABS, MBS, CMBS, CLOs, and other securitized products using market-consistent models and observable market data inputs.
    humanURL: https://www.bloomberg.com/professional/solution/bval/
    baseURL: blpapi://localhost:8194
    tags:
      - ABS
      - MBS
      - CMBS
      - CLO
      - Structured Products
      - Securitization
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/bval/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://www.bloomberg.com/professional/solution/bval/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Features
    data:
      - name: Independent Fair Value Prices
        description: Third-party evaluated prices for over 2.5 million fixed income securities.
      - name: Price Transparency
        description: Full transparency on pricing methodology, comparable securities, and model inputs.
      - name: Coverage Breadth
        description: Pricing coverage for corporate, government, municipal, and structured products globally.
      - name: Regulatory-Grade Prices
        description: BVAL prices designed to meet ASC 820/IFRS 13 fair value hierarchy requirements.
      - name: Yield Curve Data
        description: Bloomberg yield curves and spread surfaces used in BVAL pricing.
      - name: Audit Trail
        description: Full audit trail and pricing justification for regulatory and compliance review.
  - type: UseCases
    data:
      - name: NAV Calculation
        description: Use BVAL prices for end-of-day NAV calculation for fixed income funds.
      - name: Portfolio Valuation
        description: Value fixed income portfolios at fair value for reporting and analytics.
      - name: Regulatory Reporting
        description: Meet fair value measurement requirements for ASC 820 and IFRS 13 reporting.
      - name: Risk Management
        description: Use BVAL prices for mark-to-market and risk analytics.
      - name: Collateral Valuation
        description: Value fixed income collateral for repo, lending, and margin purposes.
      - name: Performance Attribution
        description: Calculate accurate returns and attribution using BVAL evaluated prices.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
