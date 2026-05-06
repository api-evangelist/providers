---
aid: consumer-financial-protection-bureau
name: Consumer Financial Protection Bureau
url: https://raw.githubusercontent.com/api-evangelist/consumer-financial-protection-bureau/refs/heads/main/apis.yml
tags:
  - Banking
  - Complaints
  - Consumer Protection
  - Federal Government
  - Financial Services
  - HMDA
  - Mortgages
  - Open Data
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-25'
modified: '2026-04-29'
position: Consumer
specificationVersion: '0.19'
x-type: government
description: The Consumer Financial Protection Bureau (CFPB) is the U.S. federal agency that supervises banks, lenders, and other financial companies, enforces federal consumer financial laws, and publishes large public datasets via open APIs. The CFPB Open Tech program publishes the Consumer Complaint Database (CCDB) search API and the HMDA Platform's Data Browser and Institutions APIs at ffiec.cfpb.gov, all unauthenticated and CC0-licensed for public use.
apis:
  - aid: consumer-financial-protection-bureau:ccdb
    name: Consumer Complaint Database API
    tags:
      - Complaints
      - Consumer Protection
      - Open Data
      - Search
    humanURL: https://www.consumerfinance.gov/data-research/consumer-complaints/
    baseURL: https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1
    properties:
      - url: https://cfpb.github.io/api/ccdb/
        type: Documentation
      - url: https://github.com/cfpb/ccdb5-api
        type: GitHubRepository
      - url: openapi/cfpb-ccdb-openapi.yml
        type: OpenAPI
    description: Public REST + JSON search API for the Consumer Complaint Database, a daily-updated record of complaints submitted by U.S. consumers about financial products and services. Supports full-text search, complaint detail lookups, faceted aggregations, autocomplete, geo breakdowns by state, and CSV export. No API key required.
  - aid: consumer-financial-protection-bureau:hmda-data-browser
    name: HMDA Data Browser API
    tags:
      - HMDA
      - Mortgages
      - Open Data
    humanURL: https://ffiec.cfpb.gov/documentation/api/data-browser/
    baseURL: https://ffiec.cfpb.gov/v2/data-browser-api
    properties:
      - url: https://ffiec.cfpb.gov/documentation/api/data-browser/
        type: Documentation
      - url: openapi/cfpb-hmda-data-browser-openapi.yml
        type: OpenAPI
    description: The HMDA Data Browser API exposes Home Mortgage Disclosure Act submission data with both nationwide and filtered (LEI, state, county, MSA/MD) aggregation reports as JSON, plus raw CSV streams and an HMDA filer lookup. Used by researchers, fair-lending analysts, and journalists.
  - aid: consumer-financial-protection-bureau:hmda-institutions
    name: HMDA Institutions API
    tags:
      - HMDA
      - Institutions
      - Open Data
    humanURL: https://ffiec.cfpb.gov/documentation/api/institutions-api/
    baseURL: https://ffiec.cfpb.gov/v2
    properties:
      - url: https://ffiec.cfpb.gov/documentation/api/institutions-api/
        type: Documentation
      - url: openapi/cfpb-hmda-institutions-openapi.yml
        type: OpenAPI
    description: Returns the financial institutions registered to file HMDA data with the CFPB, keyed by year and Legal Entity Identifier (LEI). Used by filers and researchers to confirm filer identifiers, registration status, and contact info.
common:
  - type: Website
    url: https://www.consumerfinance.gov/
  - type: Open Tech
    url: https://cfpb.github.io/
  - type: GitHub Organization
    url: https://github.com/cfpb
  - type: Data and Research
    url: https://www.consumerfinance.gov/data-research/
  - type: Consumer Complaints
    url: https://www.consumerfinance.gov/data-research/consumer-complaints/
  - type: HMDA Platform
    url: https://ffiec.cfpb.gov/
  - type: Privacy Policy
    url: https://www.consumerfinance.gov/privacy/
  - type: Terms of Service
    url: https://www.consumerfinance.gov/privacy/website-privacy-policy/
  - type: JSON-LD
    url: json-ld/consumer-financial-protection-bureau-context.jsonld
  - type: JSONSchema
    url: json-schema/cfpb-complaint-schema.json
  - type: JSONSchema
    url: json-schema/cfpb-hmda-institution-schema.json
  - type: Spectral
    url: rules/consumer-financial-protection-bureau-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/consumer-financial-protection-bureau-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
