---
aid: bloomberg-emsx
name: Bloomberg EMSX
description: Bloomberg Execution Management System (EMSX) API provides programmatic access to Bloomberg's order and execution management platform for trading operations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Bloomberg
  - Execution Management
  - Financial Services
  - Order Management
  - Trading
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-emsx/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-03-16'
specificationVersion: '0.19'
apis:
  - aid: bloomberg-emsx:bloomberg-emsx-trading-api
    name: Bloomberg EMSX Trading API
    description: API for order creation, routing, management and execution monitoring through Bloomberg EMSX platform. Supports order lifecycle management, broker selection, route management, fill tracking, and real-time execution notifications for equity, fixed income, futures, and options trading.
    humanURL: https://emsx-api-doc.readthedocs.io/
    tags:
      - Brokers
      - Equity
      - Execution
      - Fills
      - Fixed Income
      - Orders
      - Routes
      - Trading
    properties:
      - type: Documentation
        url: https://emsx-api-doc.readthedocs.io/
      - type: Reference
        url: https://www.bloomberg.com/professional/support/api-library/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Terms of Service
    url: https://www.bloomberg.com/notices/tos/
  - type: Privacy Policy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
