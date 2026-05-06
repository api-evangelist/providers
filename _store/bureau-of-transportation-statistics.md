---
aid: bureau-of-transportation-statistics
url: https://raw.githubusercontent.com/api-evangelist/bureau-of-transportation-statistics/refs/heads/main/apis.yml
name: Bureau of Transportation Statistics
tags:
  - Federal Government
  - Statistics
  - Transportation
  - Aviation
  - Freight
  - Open Data
type: Index
x-type: government
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-30'
modified: '2026-04-23'
position: Consumer
description: The Bureau of Transportation Statistics (BTS), part of the Department of Transportation (DOT) is the preeminent source of statistics on commercial aviation, multimodal freight activity, and transportation economics, and provides context to decision makers and the public for understanding statistics on transportation.
apis:
  - aid: bureau-of-transportation-statistics:bts-open-data-soda-api
    name: BTS Open Data SODA API
    tags:
      - Federal Government
      - Transportation
      - Open Data
      - Statistics
    humanURL: https://data.bts.gov/
    baseURL: https://data.bts.gov/resource/
    properties:
      - url: https://data.bts.gov/
        type: Portal
      - url: https://dev.socrata.com/
        type: Documentation
      - url: https://catalog.data.gov/dataset?organization=dot-gov&q=bts
        type: DataAPI
    description: The BTS Open Data portal powered by Socrata provides programmatic access to transportation datasets via the Socrata Open Data API (SODA). Supports filtering, querying, and aggregation across aviation, freight, and transportation economics datasets. Also supports OData V2/V4 for tools like Tableau and Excel.
    features:
      - SODA Query Language (SOQL)
      - OData V2 and V4 Endpoints
      - JSON and CSV Formats
      - Filtering and Aggregation
      - Pagination
      - Dataset Downloads
    useCases:
      - Aviation performance analysis
      - Freight activity monitoring
      - Transportation economics research
      - Supply chain analytics
  - aid: bureau-of-transportation-statistics:transtats
    name: TranStats - Airline On-Time Performance Data
    tags:
      - Federal Government
      - Transportation
      - Aviation
      - Statistics
    humanURL: https://www.transtats.bts.gov/
    properties:
      - url: https://www.transtats.bts.gov/
        type: Portal
      - url: https://www.transtats.bts.gov/ONTIME/
        type: Tool
    description: TranStats is BTS's aviation and transportation statistics database providing flight on-time performance data, carrier and airport snapshots, fuel consumption data, and comprehensive airline statistics. Enables custom queries and downloads across hundreds of aviation data tables.
    features:
      - On-Time Flight Performance Data
      - Carrier Snapshots
      - Airport Snapshots
      - Fuel Consumption Data
      - Custom Database Queries
      - Commodity Flow Survey Data
      - Freight Analysis Framework (FAF)
    useCases:
      - Airline performance analysis
      - Airport capacity planning
      - Flight delay research
      - Aviation industry benchmarking
  - aid: bureau-of-transportation-statistics:bts-freight-data
    name: BTS Freight Analysis Framework (FAF)
    tags:
      - Federal Government
      - Freight
      - Transportation
      - Statistics
    humanURL: https://www.bts.gov/faf
    properties:
      - url: https://www.bts.gov/faf
        type: Documentation
    description: The Freight Analysis Framework integrates data from multiple sources to create a comprehensive picture of freight flows to, from, within, and through the United States. Includes volume, value, and mode of shipment data for domestic and international freight.
    features:
      - Freight Flow Data
      - Shipment Volume and Value
      - Mode of Transportation Data
      - Origin-Destination Analysis
      - Commodity-Level Data
    useCases:
      - Freight infrastructure planning
      - Supply chain analysis
      - Trade flow research
      - Transportation policy development
common:
  - type: Website
    url: https://www.bts.gov
  - type: Portal
    url: https://data.bts.gov/
  - type: Privacy Policy
    url: https://www.bts.gov/privacy-policy
  - type: TranStats
    url: https://www.transtats.bts.gov/
  - type: Data Portal
    url: https://catalog.data.gov/dataset?organization=dot-gov&q=bts
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
