---
aid: bloomberg-index-solutions-limited-bisl
name: Bloomberg Index Solutions Limited (BISL)
description: Bloomberg Index Solutions Limited (BISL) is the entity that administers Bloomberg's fixed income and multi-asset indices, including the Bloomberg Global Aggregate Bond Index and other benchmark indices. BISL provides index data, calculations, and licensing for asset managers and financial institutions using Bloomberg indices as benchmarks or for financial product construction.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-index-solutions-limited-bisl/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Index
  - Fixed Income
  - Benchmark
  - Multi-Asset
  - Index Administration
  - Bloomberg
apis:
  - aid: bloomberg-index-solutions-limited-bisl:index-data-api
    name: Bloomberg Index Data API
    description: Access Bloomberg index constituent data, returns, analytics, and historical data for the Bloomberg Global Aggregate, US Aggregate, Euro Aggregate, and other benchmark indices via BLPAPI and Data License.
    humanURL: https://www.bloomberg.com/professional/solution/indices/
    baseURL: blpapi://localhost:8194
    tags:
      - Index Data
      - Fixed Income
      - Returns
      - Constituents
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/indices/
  - aid: bloomberg-index-solutions-limited-bisl:index-licensing
    name: Bloomberg Index Licensing
    description: License Bloomberg indices for use in ETFs, mutual funds, structured products, and other financial instruments. BISL provides benchmark administration services compliant with EU Benchmark Regulation (BMR) and other global frameworks.
    humanURL: https://www.bloomberg.com/professional/solution/indices/
    baseURL: https://indices.bloomberg.com
    tags:
      - Index Licensing
      - ETF
      - Benchmark Regulation
      - BMR
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/indices/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://www.bloomberg.com/professional/solution/indices/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://www.bloomberg.com/professional/support/
  - type: Features
    data:
      - name: Index Constituents
        description: Daily constituent data including weights, yields, durations, and analytics.
      - name: Index Returns
        description: Daily, monthly, and historical total and excess returns for Bloomberg indices.
      - name: Index Analytics
        description: Duration, spread, yield, and risk analytics for fixed income indices.
      - name: Benchmark Administration
        description: EU BMR-compliant benchmark administration and governance.
      - name: Custom Index Construction
        description: Custom index design and calculation services for institutional clients.
  - type: UseCases
    data:
      - name: Benchmark Comparison
        description: Compare portfolio performance against Bloomberg benchmark indices.
      - name: ETF and Fund Replication
        description: Replicate Bloomberg indices for passive investment products.
      - name: Risk Attribution
        description: Attribute portfolio risk relative to Bloomberg index benchmarks.
      - name: Product Structuring
        description: Use Bloomberg indices as underlying benchmarks for structured products.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
