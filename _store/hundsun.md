---
aid: hundsun
name: Hundsun Technologies
description: Hundsun Technologies Inc. is a leading Chinese fintech company providing software solutions and services for financial institutions including securities, funds, futures, banking, asset management, and wealth management. Hundsun's products are typically delivered as enterprise software with bespoke customer integrations rather than as a public developer API platform.
url: https://raw.githubusercontent.com/api-evangelist/hundsun/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Asset Management
  - Banking Software
  - China
  - Financial Technology
  - Securities Trading
created: '2024'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hundsun:hundsun-trading-platform
    name: Hundsun Trading Platform
    description: Enterprise trading platform offered to brokerages and securities firms, covering order management, execution, clearing, and back-office settlement. Integration is typically delivered through enterprise contracts and on-premise deployments rather than a public hosted API.
    humanURL: https://www.hundsun.com/products/trading
    tags:
      - Brokerage
      - Securities
      - Trading
    properties:
      - type: Documentation
        url: https://www.hundsun.com/products/trading
  - aid: hundsun:hundsun-wealth-management-platform
    name: Hundsun Wealth Management Platform
    description: Wealth management platform for banks and wealth managers covering portfolio management, product distribution, customer analytics, and advisor workflows. Integration is delivered as an enterprise product, not a public hosted API.
    humanURL: https://www.hundsun.com/products/wealth-management
    tags:
      - Portfolio
      - Wealth Management
    properties:
      - type: Documentation
        url: https://www.hundsun.com/products/wealth-management
  - aid: hundsun:hundsun-fund-management-platform
    name: Hundsun Fund Management Platform
    description: Fund management platform supporting fund subscription, redemption, transaction processing, and NAV calculation for asset managers. Delivered as enterprise software for fund companies and custodians.
    humanURL: https://www.hundsun.com/products/fund-management
    tags:
      - Fund Management
      - Mutual Funds
    properties:
      - type: Documentation
        url: https://www.hundsun.com/products/fund-management
common:
  - type: Website
    url: https://www.hundsun.com
  - type: Support
    url: https://support.hundsun.com
  - type: Rules
    url: https://raw.githubusercontent.com/api-evangelist/hundsun/refs/heads/main/hundsun-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
