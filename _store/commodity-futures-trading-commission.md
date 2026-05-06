---
aid: commodity-futures-trading-commission
url: https://raw.githubusercontent.com/api-evangelist/commodity-futures-trading-commission/refs/heads/main/apis.yml
name: Commodity Futures Trading Commission
x-type: government
description: The Commodity Futures Trading Commission (CFTC) is the U.S. federal regulator for commodity futures and options markets. The CFTC publishes the weekly Commitments of Traders (COT) report and other public data through a Socrata Open Data API at publicreporting.cftc.gov, providing programmatic access to Legacy, Disaggregated, Traders in Financial Futures, and Supplemental Commodity Index Trader datasets, as well as swap data and large trader reports.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CFTC
  - Commitments of Traders
  - Federal Government
  - Financial
  - Futures
  - Open Data
  - SODA
  - Trading
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: commodity-futures-trading-commission:cftc-cot-api
    name: CFTC Commitments of Traders SODA API
    description: Programmatic access to the CFTC Commitments of Traders weekly reports via the Socrata Open Data API hosted at publicreporting.cftc.gov. Datasets cover Legacy, Disaggregated, Traders in Financial Futures, and Supplemental Commodity Index Trader formats for both futures-only and combined futures-and-options positions.
    humanURL: https://publicreporting.cftc.gov/
    baseURL: https://publicreporting.cftc.gov/resource
    tags:
      - COT
      - Open Data
      - SODA
      - Trading
    properties:
      - type: Documentation
        url: https://publicreporting.cftc.gov/
      - type: Reference
        url: https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm
      - type: Reference
        url: https://dev.socrata.com/foundry/publicreporting.cftc.gov
      - type: OpenAPI
        url: openapi/cftc-cot-openapi.yml
      - type: JSONSchema
        url: json-schema/cftc-cot-schema.json
    x-features:
      - SoQL query language for filtering ($where, $select, $order)
      - Page through up to 50,000 rows per request
      - JSON, CSV, XML, RDF, RSS output formats
      - No authentication token required for typical use
      - Weekly Tuesday data updates
    x-useCases:
      - Build positioning dashboards for futures markets
      - Compute net commercial vs non-commercial open interest
      - Track managed money positioning in Disaggregated reports
      - Integrate COT data into quantitative trading models
  - aid: commodity-futures-trading-commission:cftc-swap-data-repositories
    name: CFTC Swap Data Repositories
    description: The CFTC oversees Swap Data Repositories (SDRs) that collect and maintain swap transaction records as required by the Dodd-Frank Act. SDRs publish certain real-time public data and the CFTC publishes aggregate weekly swap reports.
    humanURL: https://www.cftc.gov/MarketReports/SwapsReports/index.htm
    baseURL: https://www.cftc.gov
    tags:
      - Dodd-Frank
      - Swaps
      - SDR
      - Reporting
    properties:
      - type: Documentation
        url: https://www.cftc.gov/MarketReports/SwapsReports/index.htm
      - type: Reference
        url: https://www.cftc.gov/IndustryOversight/DataRepositories/index.htm
    x-features:
      - Weekly Swaps Report aggregates dealer activity
      - Real-time public dissemination of swap transactions via SDRs
      - Coverage of credit, interest rate, FX, and commodity asset classes
    x-useCases:
      - Monitor weekly swap dealer activity
      - Research aggregate gross notional outstanding by asset class
      - Track post-Dodd-Frank market structure changes
  - aid: commodity-futures-trading-commission:cftc-large-trader-reporting
    name: CFTC Bank Participation and Large Trader Reports
    description: The CFTC publishes monthly Bank Participation reports and other aggregate large trader reports that complement the weekly COT data. These reports are released as PDFs and HTML tables on cftc.gov.
    humanURL: https://www.cftc.gov/MarketReports/BankParticipationReports/index.htm
    baseURL: https://www.cftc.gov
    tags:
      - Bank Participation
      - Large Trader
      - Reporting
    properties:
      - type: Documentation
        url: https://www.cftc.gov/MarketReports/BankParticipationReports/index.htm
      - type: Reference
        url: https://www.cftc.gov/MarketReports/index.htm
    x-features:
      - Monthly bank participation in futures markets
      - Industry-level breakdowns of large trader positions
      - Released as HTML and PDF; not currently exposed via SODA
    x-useCases:
      - Track bank participation in major futures markets
      - Research banks' net exposure across commodity sectors
common:
  - type: Website
    url: https://www.cftc.gov/
  - type: JSON-LD
    url: json-ld/cftc-cot-context.jsonld
  - type: JSONSchema
    url: json-schema/cftc-cot-schema.json
  - type: Vocabulary
    url: vocabulary/cftc-cot-vocabulary.yml
  - type: SpectralRules
    url: rules/cftc-cot-rules.yml
  - type: Capability
    url: capabilities/query-commitments-of-traders.yml
  - type: Documentation
    url: https://publicreporting.cftc.gov/
  - type: Reference
    url: https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm
  - type: Privacy Policy
    url: https://www.cftc.gov/About/AbouttheCFTC/Privacy.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
