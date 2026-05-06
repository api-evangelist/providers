---
aid: regions-financial
url: https://raw.githubusercontent.com/api-evangelist/regions-financial/refs/heads/main/apis.yml
modified: '2026-05-02'
description: Regions Financial Corporation is a member of the S&P 500 Index and one of the nation's largest full-service providers of consumer and commercial banking, wealth management, and mortgage products and services. Regions Bank is implementing open banking capabilities through a partnership with Axway's Amplify Open Banking solution, building APIs aligned to the Financial Data Exchange (FDX) standard to enable secure financial data sharing with fintech partners and third-party platforms. Regions joined FDX in 2021 and is targeting compliance with CFPB open banking rules by April 2027.
apis:
  - aid: regions-financial:regions-open-banking-api
    name: Regions Open Banking API
    description: Regions Bank's FDX-compliant open banking API built on Axway Amplify Open Banking, providing consent-based access to account information, transaction history, customer data, payment initiation, and consent management for consumer banking, corporate banking, and wealth management customers. Uses OAuth 2.0 authorization with customer consent flows replacing legacy screen-scraping.
    humanURL: https://ir.regions.com/news-events/press-releases/news-details/2025/Enhancing-Customer-Control-of-Financial-Data-Regions-Bank-Selects-Axway-to-Accelerate-Open-Banking-Services/default.aspx
    baseURL: https://api.regions.com/v1
    tags:
      - Open Banking
      - Financial Data
      - FDX
      - Consumer Banking
      - Wealth Management
      - Account Data
      - Transactions
      - Payments
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/regions-financial/refs/heads/main/openapi/regions-open-banking-openapi.yml
      - type: PressRelease
        url: https://ir.regions.com/news-events/press-releases/news-details/2025/Enhancing-Customer-Control-of-Financial-Data-Regions-Bank-Selects-Axway-to-Accelerate-Open-Banking-Services/default.aspx
common:
  - type: Website
    url: https://www.regions.com
  - type: Website
    url: https://www.regions.com/personal-banking
  - type: Website
    url: https://www.regions.com/commercial-banking
  - type: LinkedIn
    url: https://www.linkedin.com/company/regions-financial-corporation
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/regions-financial/refs/heads/main/openapi/regions-open-banking-openapi.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/regions-financial/refs/heads/main/vocabulary/regions-financial-vocabulary.yml
tags:
  - Banking
  - Financial Services
  - Open Banking
  - FDX
  - Consumer Banking
  - Wealth Management
  - Fortune 500
---
