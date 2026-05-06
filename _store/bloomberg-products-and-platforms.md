---
aid: bloomberg-products-and-platforms
name: Bloomberg Products and Platforms
description: Bloomberg Products and Platforms covers the breadth of Bloomberg's integrated offerings spanning the Bloomberg Terminal, Enterprise data products, API platforms, trading systems, analytics, messaging, media, and government intelligence solutions. Bloomberg serves financial professionals with an interconnected ecosystem of products and platforms for data, analytics, and communication.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-products-and-platforms/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Products
  - Platforms
  - Terminal
  - Enterprise
  - Financial Data
  - Analytics
  - Bloomberg
apis:
  - aid: bloomberg-products-and-platforms:blpapi
    name: Bloomberg Open API (BLPAPI)
    description: Cross-platform API providing access to the full Bloomberg data ecosystem including real-time, reference, and historical data with SDKs for Python, Java, C++, and other languages.
    humanURL: https://bloomberg.github.io/blpapi-docs/
    baseURL: blpapi://localhost:8194
    tags:
      - Core API
      - Cross-Platform
      - Market Data
    properties:
      - type: Documentation
        url: https://bloomberg.github.io/blpapi-docs/
  - aid: bloomberg-products-and-platforms:bpipe
    name: Bloomberg B-PIPE
    description: Enterprise data distribution platform for delivering Bloomberg data at scale to multiple applications and users within an institution using a managed entitlement and authorization framework.
    humanURL: https://www.bloomberg.com/professional/support/api-library/
    baseURL: blpapi://bpipe-server:8194
    tags:
      - B-PIPE
      - Enterprise
      - Data Distribution
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/support/api-library/
  - aid: bloomberg-products-and-platforms:emsx
    name: Bloomberg EMSX (Electronic Order Management)
    description: Bloomberg's Electronic Order Management System (EMSX) enabling electronic order routing to brokers across equities, fixed income, FX, and derivatives. Provides FIX connectivity, algorithmic trading, and TCA.
    humanURL: https://www.bloomberg.com/professional/solution/emsx/
    baseURL: blpapi://localhost:8194
    tags:
      - EMSX
      - Order Management
      - FIX
      - Electronic Trading
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/emsx/
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
        description: Professional workstation integrating data, analytics, news, and messaging.
      - name: Enterprise Data Distribution
        description: B-PIPE for institution-wide Bloomberg data sharing.
      - name: Electronic Trading
        description: EMSX for electronic order routing and execution management.
      - name: Cloud Products
        description: Cloud-native Bloomberg data and analytics via cloud connectivity.
      - name: Mobile Access
        description: Bloomberg Anywhere for mobile and remote product access.
  - type: UseCases
    data:
      - name: Buy-Side Investment Workflows
        description: End-to-end data, analytics, and trading workflow for asset managers.
      - name: Sell-Side Market Making
        description: Data and trading tools for bank trading desks and market makers.
      - name: Financial Research
        description: Bloomberg Intelligence and data for research teams.
      - name: Risk Operations
        description: Risk data and analytics integration for risk management operations.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
