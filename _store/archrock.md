---
aid: archrock
name: Archrock
description: 'Archrock (NYSE: AROC) is the premier provider of natural gas compression services and equipment to customers in the oil and natural gas industry throughout the United States. The company operates a large fleet of compression equipment and provides contract operations and aftermarket services.'
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Natural Gas
  - Compression Services
  - Oil And Gas
  - Energy
  - Industrial
  - 'NYSE: AROC'
url: https://raw.githubusercontent.com/api-evangelist/archrock/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: archrock:archrock-investor-relations-api
    name: Archrock Investor Relations API
    description: Archrock provides investor relations data including SEC filings, financial reports, compression fleet statistics, and operational performance metrics for shareholders and analysts.
    humanURL: https://www.archrock.com/investor-relations
    tags:
      - Investor Relations
      - SEC Filings
      - Financial Data
      - Compression Services
      - Natural Gas
    properties:
      - type: Documentation
        url: https://www.archrock.com/investor-relations
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/archrock/refs/heads/main/openapi/archrock-investor-relations-api.yaml
common:
  - type: Portal
    url: https://www.archrock.com/
  - type: Documentation
    url: https://www.archrock.com/investor-relations
  - type: Blog
    url: https://www.archrock.com/news
  - type: Features
    data:
      - name: Natural Gas Compression
        description: Contract operations and maintenance of natural gas compression equipment across the US.
      - name: Fleet Management
        description: Management of one of the largest compression fleets in North America with diverse horsepower ratings.
      - name: Aftermarket Services
        description: Parts, service, and maintenance for third-party compression equipment.
      - name: Investor Relations Data
        description: Financial performance, fleet statistics, and operational metrics for investors and analysts.
      - name: SEC Filings
        description: Annual reports, 10-K, 10-Q, and 8-K filings available through SEC EDGAR.
  - type: UseCases
    data:
      - name: Investment Research
        description: Analyze Archrock financial performance and fleet utilization for investment decisions.
      - name: Energy Sector Analysis
        description: Track natural gas compression services market trends and operational data.
      - name: ESG Reporting
        description: Access environmental and safety performance data for ESG analysis.
      - name: Supply Chain Planning
        description: Operators use Archrock fleet data for compression capacity planning.
  - type: Integrations
    data:
      - name: SEC EDGAR
        description: All SEC filings available through the EDGAR electronic filing system.
      - name: Bloomberg
        description: Financial and operational data integrated with Bloomberg terminal.
      - name: Refinitiv
        description: Production and financial data available through Refinitiv data services.
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/archrock/refs/heads/main/rules/archrock-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/archrock/refs/heads/main/vocabulary/archrock-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/archrock/refs/heads/main/json-ld/archrock-investor-relations-api-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
