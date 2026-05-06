---
aid: bloomberg-product-suite
name: Bloomberg Product Suite
description: Bloomberg's Product Suite encompasses the complete portfolio of Bloomberg professional products including the Bloomberg Terminal, data products, analytics solutions, trading platforms, media, and technology infrastructure. The suite serves financial professionals across asset management, banking, insurance, government, and corporate sectors with integrated data, analytics, and workflow tools.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-product-suite/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Product Suite
  - Terminal
  - Data
  - Analytics
  - Trading
  - Financial Technology
  - Bloomberg
apis:
  - aid: bloomberg-product-suite:blpapi
    name: Bloomberg Open API (BLPAPI)
    description: The core API providing programmatic access to the Bloomberg data ecosystem including real-time prices, reference data, news, analytics, and Terminal functions.
    humanURL: https://bloomberg.github.io/blpapi-docs/
    baseURL: blpapi://localhost:8194
    tags:
      - Core API
      - Market Data
      - Reference Data
    properties:
      - type: Documentation
        url: https://bloomberg.github.io/blpapi-docs/
  - aid: bloomberg-product-suite:data-license
    name: Bloomberg Data License
    description: Enterprise bulk data delivery platform for acquiring Bloomberg reference data, pricing, corporate actions, and analytics at scale for data management and downstream applications.
    humanURL: https://www.bloomberg.com/professional/products/data/data-management/data-license/
    baseURL: https://dlws.bloomberg.com
    tags:
      - Data License
      - Bulk Data
      - Enterprise
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/products/data/data-management/data-license/
  - aid: bloomberg-product-suite:bloomberg-anywhere
    name: Bloomberg Anywhere
    description: Remote access service extending Bloomberg Terminal capabilities to any internet-connected device, enabling mobile and remote access to Bloomberg data, analytics, and messaging.
    humanURL: https://www.bloomberg.com/professional/solution/bloomberg-anywhere/
    baseURL: https://bba.bloomberg.net
    tags:
      - Remote Access
      - Mobile
      - Bloomberg Anywhere
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/bloomberg-anywhere/
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
      - name: Bloomberg Terminal
        description: Professional financial workstation with data, analytics, and messaging.
      - name: Enterprise Data
        description: B-PIPE and Data License for enterprise-wide data distribution.
      - name: Portfolio Analytics
        description: PORT and multi-asset analytics for portfolio management.
      - name: Trading Solutions
        description: EMSX and Tradebook for electronic order routing and execution.
      - name: Risk Solutions
        description: Credit and market risk analytics across asset classes.
      - name: Research Solutions
        description: Bloomberg Intelligence research and analytics.
  - type: UseCases
    data:
      - name: Investment Management
        description: Full-lifecycle investment data and analytics for portfolio managers.
      - name: Trading and Execution
        description: Order management and execution across equities, fixed income, FX, and derivatives.
      - name: Risk and Compliance
        description: Integrated risk analytics and regulatory compliance solutions.
      - name: Corporate Finance
        description: M&A, capital markets, and corporate treasury data and analytics.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
