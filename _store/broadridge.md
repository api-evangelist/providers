---
aid: broadridge
url: https://raw.githubusercontent.com/api-evangelist/broadridge/refs/heads/main/apis.yml
apis:
- aid: broadridge:broadridge-wealth-api
  name: Broadridge Wealth Management API
  tags:
  - Account Data
  - Financial Services
  - Positions
  - Transactions
  - Wealth Management
  image: https://raw.githubusercontent.com/api-evangelist/broadridge/refs/heads/main/image.png
  humanURL: https://www.broadridge.com/capability/middle-and-back-office-solutions/wealth-operations/
  baseURL: https://api.broadridge.example.com
  properties:
  - url: https://www.broadridge.com/capability/middle-and-back-office-solutions/wealth-operations/
    type: Documentation
  - url: https://github.com/wealthapiconnector/Broadridge-Wealth-API-Docs
    type: Reference
  - url: https://www.broadridge.com/resource/developer-api-contact
    type: GettingStarted
  - url: https://raw.githubusercontent.com/api-evangelist/broadridge/refs/heads/main/openapi/broadridge-wealth-openapi.yml
    type: OpenAPI
  description: The Broadridge Wealth Management API provides access to account activity, balances, positions, and transaction data for wealth management platforms. REST APIs enable broker-dealers and RIAs to integrate Broadridge back-office clearing and custody data into front-office wealth management applications.
- aid: broadridge:broadridge-fund-data-api
  name: Broadridge Fund Data Distribution (Galaxia) API
  tags:
  - Asset Management
  - Financial Services
  - Fund Data
  - Regulatory Reporting
  - UCITS
  image: https://raw.githubusercontent.com/api-evangelist/broadridge/refs/heads/main/image.png
  humanURL: https://www.broadridge.com/financial-services/asset-management/global-funds/simplify-financial-and-regulatory-reporting/fund-data-distribution-with-the-galaxia-data-api
  baseURL: https://dataapi-web.fundslibrary.net
  properties:
  - url: https://www.broadridge.com/financial-services/asset-management/global-funds/simplify-financial-and-regulatory-reporting/fund-data-distribution-with-the-galaxia-data-api
    type: Documentation
  - url: https://dataapi-web.fundslibrary.net/
    type: Reference
  description: The Broadridge Galaxia Fund Data API enables access to and distribution of global fund data for regulatory reporting and investor communications. APIs provide fund data dissemination for UCITS, PRIIPS, MiFID II, and other regulatory requirements across asset managers and distributors.
- aid: broadridge:broadridge-investor-communications-api
  name: Broadridge Investor Communications API
  tags:
  - Corporate Actions
  - Financial Services
  - Investor Communications
  - Proxy
  - Shareholder Services
  image: https://raw.githubusercontent.com/api-evangelist/broadridge/refs/heads/main/image.png
  humanURL: https://www.broadridge.com/
  baseURL: https://api.broadridge.example.com
  properties:
  - url: https://www.broadridge.com/
    type: Documentation
  - url: https://www.broadridge.com/resource/developer-api-contact
    type: Support
  description: The Broadridge Investor Communications API provides access to proxy distribution, shareholder vote management, and corporate action communications. APIs support electronic proxy delivery, vote tabulation, and regulatory compliance reporting for issuers, broker-dealers, and transfer agents.
- aid: broadridge:broadridge-post-trade-api
  name: Broadridge Post-Trade Processing API
  tags:
  - Financial Services
  - Post-Trade
  - Reconciliation
  - Settlement
  - SFTP
  image: https://raw.githubusercontent.com/api-evangelist/broadridge/refs/heads/main/image.png
  humanURL: https://www.broadridge.com/
  baseURL: https://api.broadridge.example.com
  properties:
  - url: https://www.broadridge.com/
    type: Documentation
  - url: https://www.broadridge.com/resource/developer-api-contact
    type: Support
  description: The Broadridge Post-Trade Processing API provides access to trade settlement, reconciliation, and regulatory reporting functions. APIs and SFTP interfaces enable post-trade processing automation, fail management, and securities operations for broker-dealers and asset managers.
name: Broadridge
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Best-in-class API components meet expert support to create the ideal wealth management operations environment. Optimize productivity, client experiences, and more.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

