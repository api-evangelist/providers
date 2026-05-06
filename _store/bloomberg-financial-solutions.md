---
aid: bloomberg-financial-solutions
name: Bloomberg Financial Solutions
description: Bloomberg Financial Solutions encompasses the full suite of Bloomberg financial data, analytics, and technology products designed to support front, middle, and back office workflows across asset management, banking, insurance, and corporate treasury. Solutions include market data, risk analytics, portfolio management, trading, compliance, and regulatory reporting capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-financial-solutions/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Financial Solutions
  - Market Data
  - Analytics
  - Trading
  - Risk Management
  - Bloomberg
apis:
  - aid: bloomberg-financial-solutions:blpapi
    name: Bloomberg Open API (BLPAPI)
    description: Core Bloomberg API providing real-time and reference data access for financial applications across trading, risk, analytics, and compliance workflows.
    humanURL: https://bloomberg.github.io/blpapi-docs/
    baseURL: blpapi://localhost:8194
    tags:
      - Core API
      - Market Data
      - Financial Data
    properties:
      - type: Documentation
        url: https://bloomberg.github.io/blpapi-docs/
  - aid: bloomberg-financial-solutions:port-api
    name: Bloomberg PORT (Portfolio Risk and Analytics)
    description: Bloomberg's portfolio risk and analytics solution providing attribution, risk factor analysis, stress testing, and regulatory reporting for asset managers and institutional investors.
    humanURL: https://www.bloomberg.com/professional/solution/portfolio-risk-analytics/
    baseURL: blpapi://localhost:8194
    tags:
      - Portfolio Analytics
      - Risk
      - Attribution
      - Regulatory
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/portfolio-risk-analytics/
  - aid: bloomberg-financial-solutions:aim-api
    name: Bloomberg AIM (Asset and Investment Manager)
    description: Bloomberg's order and portfolio management system for asset managers supporting the full investment lifecycle from order creation through compliance and settlement.
    humanURL: https://www.bloomberg.com/professional/solution/aim/
    baseURL: blpapi://localhost:8194
    tags:
      - Order Management
      - Portfolio Management
      - Compliance
      - OMS
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/aim/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://developer.bloomberg.com/
  - type: GitHubOrganization
    url: https://github.com/bloomberg
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Features
    data:
      - name: Market Data
        description: Real-time and historical market data across equities, fixed income, FX, and commodities.
      - name: Portfolio Analytics
        description: Portfolio risk, attribution, and performance analytics.
      - name: Order Management
        description: End-to-end order management and execution workflow.
      - name: Compliance
        description: Pre- and post-trade compliance monitoring and reporting.
      - name: Regulatory Reporting
        description: Regulatory data and reporting for MiFID II, EMIR, and other frameworks.
  - type: UseCases
    data:
      - name: Asset Management
        description: Full-service data and analytics for portfolio management and investment operations.
      - name: Investment Banking
        description: Market data and analytics for capital markets, M&A, and advisory.
      - name: Risk Management
        description: Cross-asset risk analytics for trading and investment portfolios.
      - name: Corporate Treasury
        description: FX, fixed income, and liquidity management solutions for corporates.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
