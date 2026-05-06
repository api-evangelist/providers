---
aid: s-and-p-global
name: S&P Global
description: S&P Global is a leading provider of credit ratings, benchmarks, analytics, and workflow solutions in the global capital, commodity, and automotive markets. Through its divisions — S&P Global Market Intelligence, S&P Global Ratings, S&P Global Commodity Insights, S&P Global Mobility, and S&P Dow Jones Indices — the company delivers data, analytics, and decisioning capabilities to financial institutions, corporations, governments, and individuals worldwide. S&P Global APIs enable programmatic access to financial data, market prices, energy market data, credit ratings, and geospatial intelligence.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/s-and-p-global/refs/heads/main/apis.yml
tags:
  - Financial Data
  - Credit Ratings
  - Market Intelligence
  - Commodity Insights
  - Energy Markets
  - Capital Markets
  - Fortune 500
created: '2026-03-21'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: s-and-p-global:commodity-insights
    name: S&P Global Commodity Insights API
    description: HTTP-based RESTful API providing access to energy market data, commodity prices, assessments, and market intelligence across the Platts and S&P Global Commodity Insights business lines. Supports market data, reference data, and historical prices for oil, gas, petrochemicals, power, shipping, and metals.
    humanURL: https://developer.spglobal.com/commodityinsights/
    baseURL: https://api.platts.com
    tags:
      - Commodity Insights
      - Energy Markets
      - Market Data
      - Platts
    properties:
      - type: Documentation
        url: https://developer.spglobal.com/commodityinsights/api/getting-started
      - type: OpenAPI
        url: https://developer.spglobal.com/commodityinsights/servicecatalog
      - type: Authentication
        url: https://developer.spglobal.com/commodityinsights/api/getting-started?tab=authentication
      - type: SDKs
        url: https://pypi.org/project/spgci/
  - aid: s-and-p-global:market-intelligence
    name: S&P Capital IQ Market Intelligence API
    description: Comprehensive financial data API providing access to fundamental data, industry-specific and segment data, valuations and pricing, S&P Global Credit Ratings and Research, and reference and terms and conditions data. Uses Bearer token authentication with tokens valid for 60 minutes.
    humanURL: https://developer.marketintelligence.spglobal.com/
    baseURL: https://api-ciq.marketintelligence.spglobal.com
    tags:
      - Market Intelligence
      - Capital IQ
      - Financial Data
      - Credit Ratings
    properties:
      - type: Documentation
        url: https://developer.marketintelligence.spglobal.com/catalog-service/
      - type: Authentication
        url: https://developer.marketintelligence.spglobal.com/catalog-service/
  - aid: s-and-p-global:marketplace-catalog
    name: S&P Global Marketplace Catalog API
    description: API providing programmatic access to the S&P Global Marketplace catalog of premium fundamental and alternative datasets. Enables discovery and integration of datasets available on the marketplace platform.
    humanURL: https://www.marketplace.spglobal.com/en/solutions/s-p-global-marketplace-catalog-api-(03f3c047-dcac-4fa7-a1ef-fb48a4d9b75d)
    baseURL: https://marketplace.spglobal.com
    tags:
      - Marketplace
      - Catalog
      - Datasets
    properties:
      - type: Documentation
        url: https://www.marketplace.spglobal.com/en/solutions/api-solutions-(61953ac7-ea64-4fac-926a-feb7f846c2be)
  - aid: s-and-p-global:kensho-link
    name: Kensho Link API
    description: S&P Global Kensho Link REST API for entity resolution and linking across financial instruments, companies, and other entities. Provides a canonical entity identifier layer across S&P Global data assets.
    humanURL: https://api.link.kensho.com/docs/guides/rest-api/
    baseURL: https://api.link.kensho.com
    tags:
      - Kensho
      - Entity Resolution
      - Data Linking
    properties:
      - type: Documentation
        url: https://api.link.kensho.com/docs/guides/rest-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/s-and-p-global/refs/heads/main/openapi/s-and-p-global-kensho-link-openapi.yml
common:
  - type: Website
    url: https://www.spglobal.com
  - type: Developer
    url: https://developer.spglobal.com/
  - type: Marketplace
    url: https://www.marketplace.spglobal.com
  - type: Documentation
    url: https://developer.spglobal.com/commodityinsights/api/getting-started
  - type: Authentication
    url: https://developer.spglobal.com/commodityinsights/api/getting-started?tab=authentication
  - type: Blog
    url: https://www.spglobal.com/en/research-insights/articles
  - type: LinkedIn
    url: https://www.linkedin.com/company/spglobal/
  - type: X
    url: https://twitter.com/SPGlobal
  - type: Pricing
    url: https://www.marketplace.spglobal.com/en/solutions/api-solutions-(61953ac7-ea64-4fac-926a-feb7f846c2be)
  - type: SDKs
    url: https://pypi.org/project/spgci/
features:
  - Credit Ratings
  - Market Data
  - Commodity Prices
  - Financial Analytics
  - Entity Resolution
  - ESG Data
  - Alternative Data
  - Fixed Income Analytics
solutions:
  - Financial Risk Management
  - Investment Research
  - Energy Trading
  - Regulatory Compliance
  - ESG Reporting
  - Credit Analysis
integrations:
  - Bloomberg
  - FactSet
  - Refinitiv
  - Python SDK
  - R SDK
  - Excel Add-in
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
