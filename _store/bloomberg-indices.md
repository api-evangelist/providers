---
aid: bloomberg-indices
name: Bloomberg Indices
description: Bloomberg Indices are a comprehensive family of fixed income, equity, commodity, and multi-asset benchmark indices used by institutional investors worldwide. The Bloomberg Global Aggregate Bond Index, US Aggregate Bond Index, and related indices serve as key benchmarks for fixed income markets. Bloomberg provides index data, analytics, and constituent information through its Terminal and data delivery platforms.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-indices/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Indices
  - Fixed Income
  - Equity
  - Commodities
  - Benchmark
  - Global Aggregate
  - Bloomberg
apis:
  - aid: bloomberg-indices:index-data-api
    name: Bloomberg Index Data API
    description: Access index constituent data, weights, analytics, total returns, and historical data for Bloomberg's family of fixed income, equity, and multi-asset indices via BLPAPI and Data License.
    humanURL: https://www.bloomberg.com/professional/solution/indices/
    baseURL: blpapi://localhost:8194
    tags:
      - Index Data
      - Fixed Income
      - Equity
      - Constituents
      - Returns
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/indices/
  - aid: bloomberg-indices:commodity-index-api
    name: Bloomberg Commodity Index (BCOM)
    description: Access Bloomberg Commodity Index data including futures-based commodity index returns, constituent weights, and rebalancing data. BCOM is a broadly diversified index tracking commodity futures across energy, metals, and agriculture.
    humanURL: https://www.bloomberg.com/professional/solution/indices/
    baseURL: blpapi://localhost:8194
    tags:
      - Commodity Index
      - BCOM
      - Futures
      - Energy
      - Metals
      - Agriculture
    properties:
      - type: Documentation
        url: https://www.bloomberg.com/professional/solution/indices/
  - aid: bloomberg-indices:galaxy-crypto-index
    name: Bloomberg Galaxy Crypto Index
    description: Access cryptocurrency index data from the Bloomberg Galaxy Crypto Index family, tracking the performance of the largest and most liquid cryptocurrencies.
    humanURL: https://www.bloomberg.com/professional/solution/indices/
    baseURL: blpapi://localhost:8194
    tags:
      - Crypto Index
      - Cryptocurrency
      - Digital Assets
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
      - name: Fixed Income Indices
        description: Global Aggregate, US Aggregate, Euro Aggregate, and other fixed income benchmarks.
      - name: Equity Indices
        description: Bloomberg equity indices across regions, sectors, and themes.
      - name: Commodity Indices
        description: Bloomberg Commodity Index (BCOM) and sub-indices for energy, metals, and agriculture.
      - name: Multi-Asset Indices
        description: Blended fixed income and equity indices for balanced portfolio benchmarking.
      - name: Crypto Indices
        description: Bloomberg Galaxy Crypto Index and cryptocurrency benchmark series.
      - name: ESG Indices
        description: Sustainability-screened index variants for ESG-oriented portfolios.
  - type: UseCases
    data:
      - name: Passive Fund Management
        description: Replicate Bloomberg indices in ETFs and index funds.
      - name: Benchmark Attribution
        description: Compare active portfolio performance against Bloomberg benchmarks.
      - name: Structured Product Design
        description: Use Bloomberg indices as underlying benchmarks for notes and structured products.
      - name: Risk Measurement
        description: Measure portfolio risk relative to Bloomberg index benchmarks.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
