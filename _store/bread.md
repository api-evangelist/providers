---
aid: bread
url: https://raw.githubusercontent.com/api-evangelist/bread/refs/heads/main/apis.yml
name: Bread Financial
tags:
  - Buy Now Pay Later
  - BNPL
  - Financing
  - Payments
  - Credit
  - Retail Finance
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-14'
modified: '2026-04-21'
position: Consumer
description: Bread Financial is a technology-driven financial services company offering white-label buy now pay later (BNPL), installment financing, and branded credit card products for merchants. The platform processes $27 billion in annual sales volume for 35.6 million active customers. Bread Pay enables merchants to embed financing options directly into their checkout flow for both online and in-store purchases, including installment plans (Bread Pay) and short-term split payment options (SplitPay).
apis:
  - aid: bread:bread-pay-api
    name: Bread Pay API
    tags:
      - Installment Financing
      - Checkout
      - Payments
      - BNPL
    humanURL: https://developers.breadfinancial.com/
    properties:
      - url: https://developers.breadfinancial.com/
        type: Documentation
    description: The Bread Pay API enables merchants to integrate installment financing options into online and in-store checkout flows. Supports creating financing applications, retrieving loan statuses, managing transactions, and handling merchant-side operations for buy now pay later programs.
  - aid: bread:split-pay-api
    name: Bread SplitPay API
    tags:
      - Short-Term Financing
      - Split Payments
      - Retail
    humanURL: https://developers.breadfinancial.com/
    properties:
      - url: https://developers.breadfinancial.com/
        type: Documentation
    description: SplitPay is a short-term financing alternative for retail merchants, enabling customers to split purchases into manageable payments and helping retailers attract price-sensitive customers while increasing average transaction values.
common:
  - type: Website
    url: https://www.breadfinancial.com
  - type: Documentation
    url: https://developers.breadfinancial.com/
  - type: BusinessSolutions
    url: https://www.breadfinancial.com/en/business-solutions.html
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
