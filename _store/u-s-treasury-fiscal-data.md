---
aid: u-s-treasury-fiscal-data
url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/apis.yml
apis:
  - aid: u-s-treasury-fiscal-data:fiscal-data-api
    name: Treasury Fiscal Data API
    tags:
      - National Debt
      - Exchange Rates
      - Treasury Statements
      - Securities
      - Federal Finance
    humanURL: https://fiscaldata.treasury.gov/
    baseURL: https://api.fiscaldata.treasury.gov/services/api/fiscal_service
    properties:
      - url: https://fiscaldata.treasury.gov/api-documentation/
        type: Documentation
      - url: https://fiscaldata.treasury.gov/api-documentation/
        type: GettingStarted
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/openapi/treasury-fiscal-data-api-openapi.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/json-schema/treasury-debt-record-schema.json
        type: JSONSchema
        title: Debt Record Schema
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/json-schema/treasury-exchange-rate-record-schema.json
        type: JSONSchema
        title: Exchange Rate Record Schema
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/json-schema/treasury-interest-rate-record-schema.json
        type: JSONSchema
        title: Interest Rate Record Schema
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/json-schema/treasury-daily-treasury-record-schema.json
        type: JSONSchema
        title: Daily Treasury Statement Record Schema
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/json-schema/treasury-monthly-treasury-record-schema.json
        type: JSONSchema
        title: Monthly Treasury Statement Record Schema
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/json-ld/treasury-fiscal-data-api-context.jsonld
        type: JSON-LD
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/examples/treasury-debt-record-example.json
        type: Example
        title: Debt Record Example
      - url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/examples/treasury-exchange-rate-record-example.json
        type: Example
        title: Exchange Rate Record Example
    description: The U.S. Treasury Fiscal Data API provides free, open access to federal financial data published by the Bureau of the Fiscal Service. Covers 80+ datasets including the Debt to the Penny dataset, Treasury Reporting Rates of Exchange, average interest rates on Treasury securities, Daily Treasury Statements, Monthly Treasury Statements, U.S. savings bond redemption tables, and public debt outstanding by security type. No authentication required. Supports filtering, sorting, field selection, and pagination.
name: U.S. Treasury Fiscal Data
tags:
  - Federal Government
  - Finance
  - Treasury
  - National Debt
  - Exchange Rates
  - Economics
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - type: Website
    url: https://fiscaldata.treasury.gov/
  - type: Documentation
    url: https://fiscaldata.treasury.gov/api-documentation/
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/rules/treasury-fiscal-data-api-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/vocabulary/u-s-treasury-fiscal-data-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/capabilities/fiscal-data-intelligence.yaml
    title: Fiscal Data Intelligence
  - type: Features
    data:
      - name: No Authentication Required
        description: All Treasury Fiscal Data API endpoints are publicly accessible without API keys or registration, enabling immediate programmatic access.
      - name: Flexible Field Selection
        description: Use the fields parameter to request only the specific data fields needed, reducing response payload size and improving performance.
      - name: Advanced Filtering
        description: Filter datasets using field:operator:value syntax supporting equality, range, and set membership operators across any field in the dataset.
      - name: Pagination Support
        description: All endpoints support page[number] and page[size] pagination with metadata indicating total record count and total pages available.
      - name: Multiple Output Formats
        description: API responses available in JSON, XML, and CSV formats suitable for programmatic consumption, data warehousing, and spreadsheet analysis.
      - name: Comprehensive Coverage
        description: 80+ datasets covering all major Bureau of the Fiscal Service financial reports from the Debt to the Penny to Monthly Treasury Statements.
  - type: UseCases
    data:
      - name: National Debt Tracking
        description: Journalists, economists, and citizens monitor daily changes in U.S. public debt outstanding including amounts held by the public and intragovernmental holdings.
      - name: Exchange Rate Research
        description: Federal agencies, researchers, and businesses use Treasury exchange rates for reporting foreign currency transactions in accordance with federal accounting standards.
      - name: Budget Analysis
        description: Policy analysts and budget offices track federal government receipts and outlays from Monthly Treasury Statements to assess deficit trends.
      - name: Interest Rate Monitoring
        description: Economists and investors track average interest rates on Treasury securities to analyze government borrowing costs and monetary policy.
      - name: Treasury Cash Management
        description: Financial researchers analyze Daily Treasury Statement data to understand federal government cash flows and liquidity management.
  - type: Integrations
    data:
      - name: FRED Economic Database
        description: Federal Reserve Economic Database (FRED) integrates Treasury Fiscal Data series for economic research and modeling applications.
      - name: USASpending.gov
        description: Federal spending transparency portal uses Bureau of the Fiscal Service data alongside Treasury Fiscal Data for comprehensive spending analysis.
      - name: Federal Accounting Standards
        description: Treasury exchange rates and fiscal data support OMB/FASAB-compliant financial reporting across federal agencies and programs.
      - name: fiscaldata.treasury.gov
        description: The official Treasury Fiscal Data portal provides data visualization, dataset explorer, and download tools built on the same API.
created: '2024-12-25'
modified: '2026-05-03'
position: Consuming
description: The U.S. Treasury Bureau of the Fiscal Service manages the government's finances including collecting revenue, paying federal bills, managing federal debt, and producing the nation's financial accounts. Their Fiscal Data API provides free, open access to federal financial data through a standardized RESTful API covering 80+ datasets. Key datasets include the Debt to the Penny (daily public debt outstanding), Treasury Reporting Rates of Exchange (quarterly foreign currency rates), Average Interest Rates on U.S. Treasury Securities, Daily Treasury Statements, Monthly Treasury Statements, and U.S. savings bond data. No authentication required.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
