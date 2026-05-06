---
aid: huntington-bancshares
name: Huntington Bancshares
description: Huntington Bancshares is a regional bank holding company that provides full-service consumer and business banking, insurance, investment, mortgage, equipment leasing, and commercial banking services. Huntington operates a developer portal at hnbdevportal.huntington.com built on Apigee X, offering API-first treasury management solutions with over 500 interfaces that process more than 10 million transaction events daily.
url: https://raw.githubusercontent.com/api-evangelist/huntington-bancshares/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking
  - ERP Integration
  - Open Banking
  - Payments
  - Treasury
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: huntington-bancshares:treasury-management-api
    name: Huntington Bank Treasury Management API
    description: The Huntington Bank Treasury Management API is part of Huntington's Treasury Management Connectivity Ecosystem, an API-first platform that enables businesses to unify banking, ERP, and financial tools. Built on Apigee X, the platform supports over 500 interfaces and processes more than 10 million transaction events daily, providing real-time visibility into treasury operations, automated payment processing, and seamless integration with enterprise systems.
    humanURL: https://hnbdevportal.huntington.com/
    baseURL: https://api.huntington.com
    tags:
      - Banking
      - ERP Integration
      - Open Banking
      - Payments
      - Treasury
    properties:
      - type: Portal
        url: https://hnbdevportal.huntington.com/
      - type: OpenAPI
        url: openapi/huntington-bank-treasury-management-api-openapi.yml
common:
  - type: Portal
    url: https://hnbdevportal.huntington.com/
  - type: Website
    url: https://www.huntington.com/
  - type: PrivacyPolicy
    url: https://www.huntington.com/privacy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
