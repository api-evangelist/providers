---
aid: sec-edgar
url: https://raw.githubusercontent.com/api-evangelist/sec-edgar/refs/heads/main/apis.yml
apis:
  - aid: sec-edgar:sec-edgar-full-text-search-api
    name: SEC EDGAR Full-Text Search API
    tags:
      - Filings
      - Finance
      - Regulatory
      - Search
      - SEC
    image: https://raw.githubusercontent.com/api-evangelist/sec-edgar/refs/heads/main/image.png
    humanURL: https://efts.sec.gov/LATEST/search-index
    baseURL: https://efts.sec.gov
    properties:
      - url: https://efts.sec.gov/LATEST/search-index
        type: Documentation
      - url: openapi/sec-edgar-submissions-openapi.yml
        type: OpenAPI
    description: The SEC EDGAR Full-Text Search API (EFTS) allows searching the full text of all EDGAR filings. Supports keyword search, date range filtering, form type filtering, and entity-based queries returning metadata for matching filings.
  - aid: sec-edgar:sec-edgar-submissions-api
    name: SEC EDGAR Submissions API
    tags:
      - Filings
      - Finance
      - Regulatory
      - SEC
    image: https://raw.githubusercontent.com/api-evangelist/sec-edgar/refs/heads/main/image.png
    humanURL: https://data.sec.gov/submissions/
    baseURL: https://data.sec.gov
    properties:
      - url: https://data.sec.gov/submissions/
        type: Documentation
      - url: https://www.sec.gov/developer
        type: Reference
      - url: openapi/sec-edgar-submissions-openapi.yml
        type: OpenAPI
    description: The SEC EDGAR Submissions API returns all company filing metadata (10-K, 10-Q, 8-K, etc.) in JSON format for a given CIK number. Returns recent and historical submission data including form type, filing date, accession numbers, and document indexes.
  - aid: sec-edgar:sec-edgar-xbrl-api
    name: SEC EDGAR XBRL Company Facts API
    tags:
      - Filings
      - Finance
      - Regulatory
      - SEC
      - XBRL
    image: https://raw.githubusercontent.com/api-evangelist/sec-edgar/refs/heads/main/image.png
    humanURL: https://data.sec.gov/api/xbrl/companyfacts/
    baseURL: https://data.sec.gov/api/xbrl
    properties:
      - url: https://data.sec.gov/api/xbrl/companyfacts/
        type: Documentation
      - url: https://www.sec.gov/developer
        type: Reference
      - url: openapi/sec-edgar-submissions-openapi.yml
        type: OpenAPI
    description: The SEC EDGAR XBRL Company Facts API delivers structured financial data extracted from XBRL-tagged filings. Returns all reported facts for a company including income statement, balance sheet, and cash flow data in JSON format organized by taxonomy concept.
  - aid: sec-edgar:sec-edgar-company-filings-api
    name: SEC EDGAR Company Filings API
    tags:
      - Filings
      - Finance
      - Regulatory
      - SEC
      - XBRL
    image: https://raw.githubusercontent.com/api-evangelist/sec-edgar/refs/heads/main/image.png
    humanURL: https://www.sec.gov/developer
    baseURL: https://efts.sec.gov
    properties:
      - url: https://www.sec.gov/developer
        type: Documentation
      - url: https://www.sec.gov/developer
        type: Reference
    description: The SEC EDGAR (Electronic Data Gathering, Analysis, and Retrieval) system provides REST APIs for accessing company filings, XBRL financial data, and full-text search across SEC submissions. APIs deliver 10-K, 10-Q, 8-K, and other filing data in JSON, XML, and XBRL formats.
common:
  - url: https://www.sec.gov/developer
    type: Portal
  - url: https://www.sec.gov/developer
    type: Documentation
  - url: https://www.sec.gov/developer
    type: GettingStarted
  - url: https://www.sec.gov/privacy-policy
    type: PrivacyPolicy
  - url: https://www.sec.gov/
    type: Website
  - url: json-schema/sec-edgar-filing-schema.json
    type: JSONSchema
  - url: json-schema/sec-edgar-company-schema.json
    type: JSONSchema
  - url: json-ld/sec-edgar-context.jsonld
    type: JSONLDContext
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
modified: '2026-03-18'
description: SEC EDGAR (Electronic Data Gathering, Analysis, and Retrieval) is the U.S. Securities and Exchange Commission's online database where public companies file mandatory disclosures and other corporate filings.
---
