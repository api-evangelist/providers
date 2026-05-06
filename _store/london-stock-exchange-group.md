---
aid: london-stock-exchange-group
name: London Stock Exchange Group
description: London Stock Exchange Group plc is a United Kingdom-based stock exchange and financial information company headquartered in the City of London, England. LSEG provides capital markets, data and analytics, risk management, and post-trade services including the World-Check screening platform for KYC and anti-money-laundering due diligence.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Financial
  - Stock Exchange
  - Market Data
  - KYC
  - Compliance
url: https://raw.githubusercontent.com/api-evangelist/london-stock-exchange-group/refs/heads/main/apis.yml
created: '2024-04-14'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: london-stock-exchange-group:lseg-world-check-one-api
    name: LSEG World-Check One API
    description: The World-Check One API enables developers to integrate the next generation of LSEG screening capabilities into existing workflows and internal systems (such as CRMs) in order to help streamline the processes for on-boarding, KYC and third party due diligence.
    humanURL: https://www.lseg.com/en/risk-intelligence/screening-solutions/world-check-kyc-screening
    tags:
      - KYC
      - Screening
      - Compliance
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/world-check-one/world-check-one-api
      - type: OpenAPI
        url: openapi/lseg-world-check-one-openapi-original.yml
common:
  - type: Website
    url: https://www.lseg.com/
  - type: Developer Portal
    url: https://developers.lseg.com/
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
