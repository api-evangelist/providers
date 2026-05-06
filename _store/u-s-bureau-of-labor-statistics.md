---
aid: u-s-bureau-of-labor-statistics
name: U.S. Bureau of Labor Statistics
description: The U.S. Bureau of Labor Statistics (BLS) is the principal federal statistical agency responsible for measuring labor market activity, working conditions, and price changes in the U.S. economy. BLS collects, processes, analyzes, and disseminates statistical data on employment, unemployment, inflation, wages, productivity, and occupational safety through a public API that provides programmatic access to published historical time series data.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/apis.yml
type: Index
created: '2024-12-25'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Federal Government
  - Labor
  - Statistics
  - Employment
  - Economic Data
apis:
  - aid: u-s-bureau-of-labor-statistics:bls-api
    name: BLS Public Data API
    description: The BLS Public Data API provides programmatic access to published historical time series data covering employment, unemployment, consumer prices, wages, productivity, and other labor market indicators. Version 2 (registration required) supports up to 50 series per request, 20 years of data, and optional calculations including net and percent changes.
    humanURL: https://www.bls.gov/developers/
    baseURL: https://api.bls.gov/publicAPI/v2
    tags:
      - Labor Statistics
      - Employment
      - Unemployment
      - Consumer Prices
      - Wages
    properties:
      - type: Documentation
        url: https://www.bls.gov/developers/api_signature_v2.htm
      - type: GettingStarted
        url: https://www.bls.gov/developers/
      - type: Authentication
        url: https://data.bls.gov/registrationEngine/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/openapi/bls-public-data-api-openapi.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/json-schema/bls-series-data-schema.json
        title: Series Data Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/json-schema/bls-data-point-schema.json
        title: Data Point Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/json-schema/bls-survey-schema.json
        title: Survey Schema
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/json-structure/bls-series-data-structure.json
        title: Series Data Structure
      - type: JSON-LD
        url: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/json-ld/bls-public-data-api-context.jsonld
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/examples/bls-series-data-example.json
        title: Series Data Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/examples/bls-data-point-example.json
        title: Data Point Example
common:
  - type: Website
    url: https://www.bls.gov/
  - type: Documentation
    url: https://www.bls.gov/developers/
  - type: GettingStarted
    url: https://www.bls.gov/developers/home.htm
  - type: PrivacyPolicy
    url: https://www.bls.gov/bls/bls-privacy.htm
  - type: FAQ
    url: https://www.bls.gov/developers/api_faqs.htm
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/rules/bls-public-data-api-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/vocabulary/u-s-bureau-of-labor-statistics-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/capabilities/labor-market-intelligence.yaml
    title: Labor Market Intelligence
  - type: Features
    data:
      - name: Time Series Data Access
        description: Retrieve historical labor statistics data using BLS series IDs covering employment, unemployment, CPI, wages, and productivity.
      - name: Multiple Series in One Request
        description: Version 2 API allows requesting up to 50 series in a single POST request, returning 20 years of data per series.
      - name: Net and Percent Change Calculations
        description: Optional calculations including net change and percent change from prior periods are available in Version 2 responses.
      - name: Survey Catalog Discovery
        description: Retrieve metadata for all available BLS surveys and discover popular series IDs through the catalog endpoint.
      - name: Annual Averages
        description: Request annual average values (M13 period) alongside monthly data for trend analysis.
      - name: Public API with Free Registration
        description: The BLS API is free to use. Version 1 requires no registration; Version 2 requires a free API key for higher query limits.
  - type: UseCases
    data:
      - name: Economic Research
        description: Economists and researchers use BLS time series data to analyze labor market trends, wage growth, and employment cycles.
      - name: Inflation Monitoring
        description: Track CPI and PPI data for measuring inflation trends across consumer goods, food, energy, and other categories.
      - name: Employment Policy Analysis
        description: Policy analysts use unemployment and employment statistics to evaluate labor market conditions and inform policy decisions.
      - name: Dashboard and Application Development
        description: Developers integrate BLS data into economic dashboards, journalism applications, and data visualization tools.
      - name: Academic Research
        description: Universities and think tanks use BLS historical data for econometric modeling, academic papers, and policy reports.
  - type: Integrations
    data:
      - name: Python blsapi
        description: Open-source Python package for querying the BLS API with support for v1 and v2 endpoints.
      - name: R blsAPI
        description: CRAN R package providing a simple interface to the BLS Public Data API for statistical computing.
      - name: Microsoft Power Platform
        description: BLS connector available in Power Automate, Power Apps, and Copilot Studio for low-code BLS data access.
      - name: data.gov
        description: BLS datasets are cataloged on data.gov as part of the federal open data initiative.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
