---
aid: crs-credit-api
url: https://raw.githubusercontent.com/api-evangelist/crs-credit-api/refs/heads/main/apis.yml
x-type: company
name: CRS Credit API
description: CRS Credit API delivers credit data-as-a-service for fast, compliant financial decisioning. The platform aggregates consumer and business credit, identity, fraud, and public records data from major bureaus (Equifax, Experian, TransUnion, LexisNexis, CIC, PitchPoint) through a single contract and developer interface.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Credit
  - Consumer Credit
  - Business Credit
  - Identity
  - Fraud
  - Data
type: Contract
access: 3rd-Party
position: Consuming
specificationVersion: '0.19'
created: '2024-11-14'
modified: '2026-04-28'
apis:
  - aid: crs-credit-api:credit-data-api
    name: CRS Credit Data API
    description: Single-contract API providing access to consumer and business credit reports across major bureaus (Equifax, Experian, TransUnion). Supports soft and hard credit pulls, FICO and Vantage scoring models, and public record data. Documentation is published via Redocly.
    humanURL: https://crscreditapi.redoc.ly/
    baseURL: https://api-sandbox.stitchcredit.com
    tags:
      - Credit
      - Consumer Credit
      - Business Credit
      - Bureau
      - REST
    properties:
      - url: https://crscreditapi.redoc.ly/
        type: Documentation
      - url: https://crscreditapi.com/
        type: Website
  - aid: crs-credit-api:credit-monitoring-api
    name: CRS Credit Monitoring API
    description: API powering the eCredit Monitoring service for continuous consumer credit monitoring including alerts on credit profile changes.
    humanURL: https://crsecreditmonitoringapi.redoc.ly/
    tags:
      - Credit Monitoring
      - Alerts
      - Consumer Credit
    properties:
      - url: https://crsecreditmonitoringapi.redoc.ly/
        type: Documentation
  - aid: crs-credit-api:data-furnishing-api
    name: CRS Data Furnishing API
    description: API for furnishing data to credit bureaus. Currently announced as coming soon on the CRS developer portal.
    humanURL: https://crscreditapi.redoc.ly/developer-portal/data-furnishing/
    tags:
      - Data Furnishing
      - Bureau Reporting
    properties:
      - url: https://crscreditapi.redoc.ly/developer-portal/data-furnishing/
        type: Documentation
features:
  - name: Multi-Bureau Coverage
    description: Aggregates Equifax, Experian, TransUnion, LexisNexis, CIC, and PitchPoint into one API contract.
  - name: Soft and Hard Credit Pulls
    description: Supports both soft inquiries that do not affect credit and hard inquiries used for underwriting.
  - name: FICO and Vantage Scores
    description: Returns standard FICO and Vantage credit score models alongside report data.
  - name: Identity and Fraud
    description: Identity verification, KYC, and fraud signals returned alongside credit data.
  - name: Public Records
    description: Access to public records data including bankruptcies, liens, and judgments.
  - name: Multi-Format Responses
    description: Returns credit data as JSON, XML, HTML5, or PDF.
  - name: Bearer Token Authentication
    description: REST API uses bearer token authentication over HTTPS.
  - name: Multi-Language SDKs
    description: Examples available for Ruby, Python, JavaScript, Java, Node.js, Go, PHP, .NET, and cURL.
useCases:
  - name: Loan Underwriting
    description: Lenders pull bureau reports and scores to make credit decisions.
  - name: Tenant Screening
    description: Property managers run consumer credit and public records checks on applicants.
  - name: Business Credit Decisioning
    description: B2B vendors evaluate the creditworthiness of business customers for terms and limits.
  - name: KYC and Identity Verification
    description: Fintechs verify identity and screen for fraud during onboarding.
  - name: Credit Monitoring Services
    description: Consumer fintech apps surface real-time alerts on credit profile changes to end users.
common:
  - url: https://crscreditapi.com/
    type: Website
  - url: https://crscreditapi.redoc.ly/
    type: Documentation
  - url: https://crscreditapi.redoc.ly/
    type: Reference
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
