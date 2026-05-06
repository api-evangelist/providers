---
aid: arch-coal
name: Arch Coal
description: Arch Coal (now Arch Resources) is a Fortune 500 producer and marketer of metallurgical and thermal coal from mines in the United States, supplying steel manufacturers, electric utilities, and industrial customers worldwide.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Mining
  - Coal
  - Metallurgical Coal
  - Thermal Coal
  - Energy
  - Fortune 500
url: https://raw.githubusercontent.com/api-evangelist/arch-coal/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: arch-coal:arch-coal-investor-relations
    name: Arch Coal Investor Relations
    description: Arch Coal provides investor relations data including SEC filings, financial reports, coal production data, and market information for shareholders and analysts.
    humanURL: https://archresources.com/investor-relations/
    tags:
      - Investor Relations
      - SEC Filings
      - Financial Data
      - Coal Production
    properties:
      - type: Documentation
        url: https://archresources.com/investor-relations/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/arch-coal/refs/heads/main/openapi/arch-coal-investor-relations-api.yaml
common:
  - type: Portal
    url: https://www.arch-coal.com/
  - type: Features
    data:
      - name: Metallurgical Coal
        description: High-quality metallurgical coal for steelmaking from mines in West Virginia and Virginia.
      - name: Thermal Coal
        description: Thermal coal for electricity generation from mines in Wyoming's Powder River Basin.
      - name: Safety Performance Data
        description: Publicly reported mine safety and environmental performance metrics.
      - name: Production Reporting
        description: Quarterly coal production and sales volume reporting for investors and analysts.
      - name: SEC Filings
        description: Annual reports, 10-K, 10-Q, and 8-K filings available through SEC EDGAR.
  - type: UseCases
    data:
      - name: Investment Research
        description: Analyze Arch Coal financial performance, production data, and market position for investment decisions.
      - name: ESG Reporting
        description: Access environmental, safety, and governance data for ESG analysis and reporting.
      - name: Supply Chain Planning
        description: Steel manufacturers and utilities use production data for supply chain planning and procurement.
      - name: Commodity Market Analysis
        description: Track coal pricing, production volumes, and export data for commodity market research.
  - type: Integrations
    data:
      - name: SEC EDGAR
        description: All SEC filings available through the EDGAR electronic filing system at sec.gov.
      - name: Bloomberg
        description: Financial data integrated with Bloomberg terminal for market analysis.
      - name: Refinitiv
        description: Production and financial data available through Refinitiv (formerly Thomson Reuters) data services.
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/arch-coal/refs/heads/main/rules/arch-coal-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/arch-coal/refs/heads/main/vocabulary/arch-coal-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/arch-coal/refs/heads/main/json-ld/arch-coal-investor-relations-api-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
