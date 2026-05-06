---
aid: department-of-the-treasury
name: Department of the Treasury
description: The U.S. Department of the Treasury manages federal finances, public debt, Treasury securities, U.S. currency production, tax administration, financial sanctions, and economic-statistical reporting. Treasury bureaus publish several public APIs, anchored by the Bureau of the Fiscal Service's Fiscal Data API and the Office of Foreign Assets Control's Sanctions List Service.
url: https://raw.githubusercontent.com/api-evangelist/department-of-the-treasury/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-12-03'
modified: '2026-04-28'
type: Index
position: Consuming
access: 3rd-Party
specificationVersion: '0.20'
tags:
  - Federal Government
  - Finance
  - Debt
  - Sanctions
common:
  - url: https://home.treasury.gov/
    type: Portal
  - url: https://fiscaldata.treasury.gov/api-documentation/
    type: Documentation
  - url: https://ofac.treasury.gov/
    type: Reference
apis:
  - aid: department-of-the-treasury:fiscal-data-api
    name: Treasury Fiscal Data API
    description: Standardized federal-finance datasets from the Bureau of the Fiscal Service - Debt to the Penny, Daily and Monthly Treasury Statements, auctions, interest rates, exchange rates, and federal spending.
    humanURL: https://fiscaldata.treasury.gov/api-documentation/
    baseURL: https://api.fiscaldata.treasury.gov/services/api/fiscal_service
    tags:
      - Finance
      - Debt
      - Open Data
    properties:
      - type: Documentation
        url: https://fiscaldata.treasury.gov/api-documentation/
      - type: OpenAPI
        url: openapi/fiscal-data-api-openapi.yml
      - type: JSONSchema
        url: json-schema/treasury-debt-record-schema.json
      - type: Example
        url: examples/debt-to-penny-example.json
      - type: Datasets
        url: https://fiscaldata.treasury.gov/datasets/
  - aid: department-of-the-treasury:ofac-sanctions-list-service-api
    name: OFAC Sanctions List Service API
    description: Specially Designated Nationals (SDN) and Consolidated Sanctions lists from the Office of Foreign Assets Control, with structured search.
    humanURL: https://sanctionslistservice.ofac.treas.gov/
    baseURL: https://sanctionslistservice.ofac.treas.gov/api
    tags:
      - Sanctions
      - Compliance
    properties:
      - type: Documentation
        url: https://ofac.treasury.gov/sanctions-list-service
      - type: OpenAPI
        url: openapi/ofac-sdn-api-openapi.yml
      - type: JSONSchema
        url: json-schema/sanctioned-entity-schema.json
      - type: Example
        url: examples/sanctioned-entity-example.json
      - type: Reference
        url: https://ofac.treasury.gov/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists
  - aid: department-of-the-treasury:treasury-direct-api
    name: TreasuryDirect Securities API
    description: Public reference data on marketable Treasury securities (auctions, results, security details) published via TreasuryDirect.
    humanURL: https://www.treasurydirect.gov/TA_WS/securities/announced
    tags:
      - Securities
      - Auctions
    properties:
      - type: Documentation
        url: https://www.treasurydirect.gov/webapis/webapisindex.htm
      - type: Reference
        url: https://www.treasurydirect.gov/instit/instit.htm
  - aid: department-of-the-treasury:sam-entity-management-api
    name: SAM.gov Entity Management API
    description: Federal Service for Award Management (SAM) entity registration, exclusions, and assistance-listings data published via api.data.gov.
    humanURL: https://open.gsa.gov/api/entity-api/
    tags:
      - Procurement
      - Awards
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/entity-api/
      - type: Reference
        url: https://sam.gov/
  - aid: department-of-the-treasury:irs-public-apis
    name: IRS Public APIs
    description: The Internal Revenue Service exposes select public datasets and tools through download endpoints, including Tax-Exempt Organization Search.
    humanURL: https://www.irs.gov/charities-non-profits/tax-exempt-organization-search
    tags:
      - Tax
      - Charities
    properties:
      - type: Documentation
        url: https://www.irs.gov/charities-non-profits/tax-exempt-organization-search
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
