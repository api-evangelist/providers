---
aid: bloomberg-index-solutions-limited-bisl
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-index-solutions-limited-bisl/refs/heads/main/apis.yml
apis:
- name: Bloomberg Index Data API
  description: Access to Bloomberg index levels, constituents, and historical data for various asset classes including equities, fixed income, and commodities.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2023/01/bloomberg-logo-1.png
  baseURL: https://api.bloomberg.com/index/v1
  humanURL: https://www.bloomberg.com/professional/product/indices/
  tags:
  - Financial Indices
  - Index Data
  - Market Data
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Authentication
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Pricing
    url: https://www.bloomberg.com/professional/products/indices/resources/index-data-licensing/
  contact:
  - FN: Bloomberg Index Services
    email: indexhelp@bloomberg.net
    url: https://www.bloomberg.com/professional/product/indices/
- name: Bloomberg Index Metadata API
  description: Retrieve index specifications, methodology documents, constituent lists, and index governance information.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2023/01/bloomberg-logo-1.png
  baseURL: https://api.bloomberg.com/index-metadata/v1
  humanURL: https://www.bloomberg.com/professional/products/indices/documentation/
  tags:
  - Index Specifications
  - Metadata
  - Methodology
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Reference
    url: https://www.bloomberg.com/professional/products/indices/documentation/
- name: Bloomberg Fixed Income Indices API
  description: Provides access to Bloomberg fixed income index data including the Bloomberg Aggregate, Treasury, Corporate, Municipal, High-Yield, and Emerging Markets bond indices. Bloomberg is the most widely used fixed income indices provider globally, with more than 500 ETFs tracking Bloomberg fixed income indices.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2023/01/bloomberg-logo-1.png
  baseURL: https://api.bloomberg.com/indices/fixedincome/v1
  humanURL: https://www.bloomberg.com/professional/products/indices/fixed-income/
  tags:
  - Aggregate Index
  - Benchmarks
  - Bonds
  - Fixed Income
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Reference
    url: https://www.bloomberg.com/professional/products/indices/fixed-income/
- name: Bloomberg Equity Indices API
  description: Access to Bloomberg equity index data across global, regional, country, and sector exposures including traditional growth and value styles, factor index strategies, thematics, ESG, and climate benchmarks.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2023/01/bloomberg-logo-1.png
  baseURL: https://api.bloomberg.com/indices/equity/v1
  humanURL: https://www.bloomberg.com/professional/products/indices/equity/
  tags:
  - Benchmarks
  - Equity
  - Factor Indices
  - Stocks
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Reference
    url: https://www.bloomberg.com/professional/products/indices/equity/
- name: Bloomberg Commodity Indices API
  description: Access to Bloomberg Commodity Index (BCOM) data and sub-indices covering energy, metals, and agricultural commodities. BCOM is constructed using 24 commodities and rebalances annually, weighted two-thirds by trading volume and one-third by world production.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2023/01/bloomberg-logo-1.png
  baseURL: https://api.bloomberg.com/indices/commodities/v1
  humanURL: https://www.bloomberg.com/professional/products/indices/commodities/
  tags:
  - BCOM
  - Commodities
  - Energy
  - Metals
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Reference
    url: https://www.bloomberg.com/professional/products/indices/commodities/
- name: Bloomberg ESG and Climate Indices API
  description: Access to over 500 cross-asset indices covering climate, ESG, sustainable debt, and responsible investing. Includes approaches such as SRI screening, sustainability weighting, and ESG integration across equity and fixed income asset classes.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2023/01/bloomberg-logo-1.png
  baseURL: https://api.bloomberg.com/indices/esg/v1
  humanURL: https://www.bloomberg.com/professional/products/indices/esg-climate/
  tags:
  - Climate
  - ESG
  - Responsible Investing
  - Sustainable Finance
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Reference
    url: https://www.bloomberg.com/professional/products/indices/esg-climate/
- name: Bloomberg Multi-Asset Indices API
  description: Access to Bloomberg multi-asset index data for composite indices constructed from at least one fixed income index and one equity index, enabling cross-asset class benchmarking and portfolio construction.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2023/01/bloomberg-logo-1.png
  baseURL: https://api.bloomberg.com/indices/multiasset/v1
  humanURL: https://www.bloomberg.com/professional/products/indices/multi-asset/
  tags:
  - Asset Allocation
  - Cross-Asset
  - Multi-Asset
  - Portfolio Benchmarks
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Reference
    url: https://www.bloomberg.com/professional/products/indices/multi-asset/
- name: Bloomberg Thematic Indices API
  description: Access to Bloomberg thematic index data that captures structural macro trends disrupting the global economy. Employs proprietary research from Bloomberg Intelligence and BloombergNEF to form thematic investment baskets.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2023/01/bloomberg-logo-1.png
  baseURL: https://api.bloomberg.com/indices/thematic/v1
  humanURL: https://www.bloomberg.com/professional/products/indices/thematic/
  tags:
  - Innovation
  - Macro Trends
  - Strategic Indices
  - Thematic
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Reference
    url: https://www.bloomberg.com/professional/products/indices/thematic/
- name: Bloomberg BFIX API
  description: Bloomberg FX Fixings (BFIX) provides a family of FX benchmarks covering spots, forward, and non-deliverable forward rates. BFIX produces over 5,900 fixings covering over 160 core currencies, calculated and published every 30 minutes throughout the trading day. Administered by BISL and compliant with UK BMR and IOSCO principles.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2023/01/bloomberg-logo-1.png
  baseURL: https://api.bloomberg.com/bfix/v1
  humanURL: https://www.bloomberg.com/professional/products/indices/fx-findings-reference-rates/
  tags:
  - Benchmarks
  - Currency
  - FX Fixings
  - Reference Rates
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Reference
    url: https://www.bloomberg.com/professional/products/indices/fx-findings-reference-rates/
- name: Bloomberg Custom Index Solutions API
  description: Provides access to custom-built indices tailored to specific investment strategies, product requirements, and regulatory needs. Bloomberg offers end-to-end lifecycle support from index design and backtesting through production calculation, covering total return swaps, QIS platforms, and structured notes.
  image: https://www.bloomberg.com/company/wp-content/uploads/sites/2/2023/01/bloomberg-logo-1.png
  baseURL: https://api.bloomberg.com/indices/custom/v1
  humanURL: https://www.bloomberg.com/professional/products/indices/customization/
  tags:
  - Custom Indices
  - Index Design
  - Strategy
  - Structured Products
  properties:
  - type: Documentation
    url: https://www.bloomberg.com/professional/support/api-library/
  - type: Reference
    url: https://www.bloomberg.com/professional/products/indices/customization/
name: Bloomberg Index Solutions Limited (BISL)
tags:
- Benchmark Administration
- Financial Indices
- Financial Services
- Market Data
- Regulatory Compliance
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Bloomberg Index Solutions Limited (BISL) provides benchmark administration and index calculation services for financial market indices, ensuring compliance with global regulatory standards including the EU Benchmarks Regulation (BMR).
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

