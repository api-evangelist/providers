---
aid: federal-reserve
name: Federal Reserve
description: The FRED API is a web service that allows developers to write programs and build applications that retrieve economic data from the FRED and ALFRED websites hosted by the Economic Research Division of the Federal Reserve Bank of St. Louis.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-28'
position: Consumer
tags:
  - Economics
  - Federal Government
  - Finance
url: https://raw.githubusercontent.com/api-evangelist/federal-reserve/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: federal-reserve:federal-reserve
    name: Federal Reserve FRED API
    tags:
      - Economics
      - Finance
    humanURL: https://fred.stlouisfed.org/docs/api/fred
    baseURL: https://api.stlouisfed.org/fred
    properties:
      - url: https://fred.stlouisfed.org/docs/api/fred
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/federal-reserve/refs/heads/main/openapi/federal-reserve-fred-openapi.yml
        type: OpenAPI
    description: The FRED API allows developers to retrieve economic data from the Federal Reserve Bank of St. Louis including categories, releases, series, sources, tags, and observations across thousands of economic time series.
common:
  - type: Website
    url: https://www.federalreserve.gov/
  - type: Documentation
    url: https://fred.stlouisfed.org/docs/api/fred
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
