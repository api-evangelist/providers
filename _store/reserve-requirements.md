---
aid: reserve-requirements
name: Reserve Requirements
description: Reserve Requirements refers to the Federal Reserve's Regulation D framework governing reserve requirement ratios for depository institutions. As of March 26, 2020, the Federal Reserve reduced all reserve requirement ratios to zero percent, eliminating reserve requirements for all depository institutions. The Federal Reserve provides data access through FRED (Federal Reserve Economic Data), the H.6 Money Stock Measures release, and the federalreserve.gov data download program for historical reserve and monetary base data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Reserve Requirements
  - Federal Reserve
  - Banking Regulation
  - Monetary Policy
  - Regulation D
  - Finance
url: https://raw.githubusercontent.com/api-evangelist/reserve-requirements/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: reserve-requirements:fred-api
    name: FRED API - Reserve Data
    description: The Federal Reserve Economic Data (FRED) API provided by the Federal Reserve Bank of St. Louis offers programmatic access to reserve requirement data, monetary base data, and historical H.3 and H.6 statistical release data. FRED provides a comprehensive REST API with API key authentication for accessing economic time series data.
    humanURL: https://fred.stlouisfed.org/
    baseURL: https://api.stlouisfed.org/fred
    tags:
      - Federal Reserve
      - Economic Data
      - Reserve Requirements
      - Monetary Base
      - Time Series
    properties:
      - type: Documentation
        url: https://fred.stlouisfed.org/docs/api/fred/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/reserve-requirements/refs/heads/main/openapi/fred-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/reserve-requirements/refs/heads/main/json-schema/fred-series-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/reserve-requirements/refs/heads/main/json-schema/fred-observation-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/reserve-requirements/refs/heads/main/json-structure/fred-series-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/reserve-requirements/refs/heads/main/json-ld/reserve-requirements-context.jsonld
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/reserve-requirements/refs/heads/main/rules/reserve-requirements-rules.yml
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/reserve-requirements/refs/heads/main/vocabulary/reserve-requirements-vocabulary.yml
    contact:
      - FN: Federal Reserve Bank of St. Louis
        url: https://fred.stlouisfed.org/
  - aid: reserve-requirements:fed-data-download
    name: Federal Reserve Data Download Program
    description: The Federal Reserve Board's Data Download Program provides structured access to Federal Reserve statistical releases including Regulation D reserve requirement data, H.6 Money Stock Measures, and historical reserve data through a web-based data download interface.
    humanURL: https://www.federalreserve.gov/datadownload/
    tags:
      - Federal Reserve
      - Statistical Releases
      - Regulation D
      - Reserve Requirements
      - Data Download
    properties:
      - type: Documentation
        url: https://www.federalreserve.gov/datadownload/
      - type: About
        url: https://www.federalreserve.gov/monetarypolicy/reservereq.htm
common:
  - type: Website
    url: https://www.federalreserve.gov/monetarypolicy/reservereq.htm
  - type: Documentation
    url: https://www.federalreserve.gov/monetarypolicy/reservereq.htm
  - type: Policy
    url: https://www.federalreserve.gov/monetarypolicy/reservereq.htm
  - type: Regulation
    url: https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-204
  - type: DataDownload
    url: https://www.federalreserve.gov/datadownload/
  - type: FRED
    url: https://fred.stlouisfed.org/categories/32217
  - type: H6Release
    url: https://www.federalreserve.gov/releases/h6/
  - type: GitHubOrganization
    url: https://github.com/federalreserve
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
