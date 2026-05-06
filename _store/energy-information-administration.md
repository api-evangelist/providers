---
aid: energy-information-administration
name: Energy Information Administration
url: https://raw.githubusercontent.com/api-evangelist/energy-information-administration/refs/heads/main/apis.yml
tags:
  - Energy
  - Federal Government
  - Open Data
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-28'
position: Consumer
description: The U.S. Energy Information Administration (EIA) is committed to its free and open data by making it available through an Application Programming Interface (API) and its open data tools. The EIA Open Data API v2 is multi-faceted and contains time-series datasets organized by the main energy categories, including electricity, natural gas, petroleum, coal, nuclear, renewables, total energy, international energy statistics, the State Energy Data System (SEDS), and CO2 emissions aggregates.
apis:
  - aid: energy-information-administration:open-data-api
    name: EIA Open Data API
    tags:
      - Energy
      - Federal Government
      - Open Data
      - Time Series
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.eia.gov/v2
    humanURL: https://www.eia.gov/opendata/
    properties:
      - url: https://www.eia.gov/opendata/
        type: Documentation
      - url: https://www.eia.gov/opendata/browser/
        type: API Browser
      - url: https://www.eia.gov/opendata/register.php
        type: Signup
      - url: openapi/energy-information-administration-open-data-api-openapi.yml
        type: OpenAPI
    description: The EIA Open Data API v2 provides programmatic access to free U.S. energy time-series data through a hierarchical route structure organized by energy category. An API key is required (free registration) and is passed as a URL query parameter on every request. Responses include rich metadata for navigating child routes, facets, frequencies, and available data columns. The API supports JSON (default) and XML output, with up to 5,000 rows per request for JSON and 300 rows for XML.
common:
  - type: Website
    url: https://www.eia.gov
  - type: Documentation
    url: https://www.eia.gov/opendata/
  - type: API Browser
    url: https://www.eia.gov/opendata/browser/
  - type: Signup
    url: https://www.eia.gov/opendata/register.php
  - type: Bulk Downloads
    url: https://www.eia.gov/opendata/bulkfiles.php
  - type: Excel Add-in
    url: https://www.eia.gov/opendata/excel/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.20'
---
