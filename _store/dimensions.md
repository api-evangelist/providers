---
aid: dimensions
name: Dimensions
url: https://raw.githubusercontent.com/api-evangelist/dimensions/refs/heads/main/apis.yml
description: Dimensions is a research data platform from Digital Science providing access to publications, grants, patents, clinical trials, datasets, and policy documents. The Dimensions Analytics API offers programmatic access to this research data via the Dimensions Search Language (DSL), enabling citation analysis, researcher discovery, organization benchmarking, and topic identification. The API is subscription-only and is not intended for bulk data extraction or to power dashboards or other derivative products.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
position: Consumer
access: 3rd-Party
tags:
  - Analytics
  - Research
  - Publications
  - Grants
  - Patents
  - Clinical Trials
  - Jupyter Notebooks
created: '2025-02-06'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: dimensions:dimensions-analytics-api
    name: Dimensions Analytics API
    description: The Dimensions Analytics API provides programmatic access to the Dimensions research data platform via the Dimensions Search Language (DSL). It supports queries against publications, grants, patents, clinical trials, datasets, organizations, and researchers. Authentication uses an API key exchanged for a JWT token via POST to /api/auth, with query requests sent to /api/dsl/v2 carrying the JWT in the Authorization header. The API is subscription-only and rate limited to 30 requests per IP per minute.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.dimensions.ai/dsl/
    baseURL: https://app.dimensions.ai/api
    tags:
      - Analytics
      - Research
      - Publications
      - Grants
      - Patents
      - Clinical Trials
    properties:
      - type: Documentation
        url: https://docs.dimensions.ai/dsl/
      - type: API Access
        url: https://docs.dimensions.ai/dsl/api.html
      - type: DSL Reference
        url: https://docs.dimensions.ai/dsl/language.html
      - type: API Lab
        url: https://api-lab.dimensions.ai/
      - type: SourceCode
        url: https://github.com/digital-science/dimcli
common:
  - type: Website
    url: https://www.dimensions.ai/
  - type: Documentation
    url: https://docs.dimensions.ai/dsl/
  - type: Support
    url: https://plus.dimensions.ai/support/
  - type: Blog
    url: https://www.dimensions.ai/blog/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
