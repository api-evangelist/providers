---
aid: sandp-global
name: S&P Global
description: 'S&P Global is a leading provider of credit ratings, benchmarks, analytics, and workflow solutions in the global capital, commodity, and automotive markets. S&P Global offers multiple API product lines across its business divisions: the Capital IQ API provides comprehensive financial and market intelligence data; the Commodity Insights API provides price assessments, market data, and analytics for energy and commodities markets; and the Marketplace API enables programmatic access to the S&P Global data marketplace catalog.'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Financial Data
  - Market Intelligence
  - Commodity Insights
  - Credit Ratings
  - Analytics
  - Fortune 500
  - Enterprise
created: '2026-05-02'
modified: '2026-05-02'
x-profiled: 2026-05
url: https://raw.githubusercontent.com/api-evangelist/sandp-global/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: sandp-global:sandp-global-capital-iq-api
    name: S&P Capital IQ API
    description: The S&P Capital IQ API provides programmatic access to one of the industry's most comprehensive sets of global financial data, including fundamental financials, industry-specific data, valuations and pricing, S&P Global Credit Ratings and Research, capital structure data, and reference data. The API uses REST with JSON responses and Bearer token authentication. The primary endpoint is https://api-ciq.marketintelligence.spglobal.com/gdsapi/rest/v3/clientservice.json.
    humanURL: https://www.marketplace.spglobal.com/en/solutions/api-solutions-(61953ac7-ea64-4fac-826a-feb7f846c2be)
    tags:
      - Financial Data
      - Fundamentals
      - Credit Ratings
      - Market Intelligence
      - REST
    properties:
      - type: Documentation
        url: https://www.marketplace.spglobal.com/en/solutions/api-solutions-(61953ac7-ea64-4fac-826a-feb7f846c2be)
      - type: Developer Guide
        url: https://www.support.marketplace.spglobal.com/content/dam/spglobal/mi/en/documents/marketplace/api/guides/spglobalapidevelopersguide.pdf
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sandp-global/refs/heads/main/openapi/sandp-global-capital-iq-openapi.yml
      - type: JSONSchema
        url: json-schema/sandp-global-financial-data-request-schema.json
  - aid: sandp-global:sandp-global-commodity-insights-api
    name: S&P Global Commodity Insights API
    description: The S&P Global Commodity Insights API (formerly Platts API) provides HTTP-based RESTful access to commodity price assessments, market data, and analytics across energy, metals, agriculture, and petrochemicals markets. Authentication uses Bearer token generated via the Token Generation API endpoint at https://developer.spglobal.com. The base domain for API requests is https://api.platts.com.
    humanURL: https://developer.spglobal.com/commodityinsights/
    tags:
      - Commodity Data
      - Energy
      - Metals
      - Platts
      - Price Assessments
      - REST
    properties:
      - type: Documentation
        url: https://developer.spglobal.com/commodityinsights/api/getting-started
      - type: Developer Portal
        url: https://developer.spglobal.com
      - type: Service Catalog
        url: https://developer.spglobal.com/commodityinsights/servicecatalog
      - type: Authentication
        url: https://developer.spglobal.com/Token_Generation_API.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sandp-global/refs/heads/main/openapi/sandp-global-commodity-insights-openapi.yml
      - type: JSONSchema
        url: json-schema/sandp-global-price-assessment-schema.json
  - aid: sandp-global:sandp-global-marketplace-catalog-api
    name: S&P Global Marketplace Catalog API
    description: The S&P Global Marketplace Catalog API provides programmatic access to the S&P Global data marketplace, enabling discovery and consumption of available data products, datasets, and API solutions across all S&P Global business units.
    humanURL: https://www.marketplace.spglobal.com/en/solutions/s-p-global-marketplace-catalog-api-(03f3c047-dcac-4fa7-a1ef-fb48a4d9b75d)
    tags:
      - Data Catalog
      - Marketplace
      - Discovery
      - REST
    properties:
      - type: Documentation
        url: https://www.marketplace.spglobal.com/en/solutions/s-p-global-marketplace-catalog-api-(03f3c047-dcac-4fa7-a1ef-fb48a4d9b75d)
common:
  - type: Website
    url: https://www.spglobal.com
  - type: Developer Portal
    url: https://developer.spglobal.com
  - type: Marketplace
    url: https://www.marketplace.spglobal.com
  - type: Documentation
    url: https://www.support.marketplace.spglobal.com
  - type: Authentication
    url: https://developer.spglobal.com/getting-started/Auth.html
  - type: Python SDK
    url: https://pypi.org/project/spgci/
  - type: Python SDK
    url: https://pypi.org/project/SPGMICIQ/
  - type: FAQ
    url: https://developer.spglobal.com/support/faq
  - type: Support
    url: https://commodityinsightssupport.spglobal.com
  - type: Vocabulary
    url: vocabulary/sandp-global-vocabulary.yml
  - type: SpectralRules
    url: rules/sandp-global-rules.yml
  - type: Capabilities
    url: capabilities/market-intelligence.yaml
  - type: JSONLD
    url: json-ld/sandp-global-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
