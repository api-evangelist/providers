---
aid: ibisworld
name: IBISWorld
description: IBISWorld is a leading provider of industry research and market intelligence, offering data on thousands of industries across global markets. IBISWorld provides APIs for accessing industry reports, market size data, and economic forecasts programmatically.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Business Intelligence
  - Economics
  - Industry Data
  - Market Research
url: https://raw.githubusercontent.com/api-evangelist/ibisworld/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: ibisworld:ibisworld-api
    name: IBISWorld API
    description: The IBISWorld API provides programmatic access to industry research data, market intelligence reports, business environment profiles, classification systems, and economic forecasts for thousands of industries across global markets.
    humanURL: https://www.ibisworld.com/api/
    baseURL: https://api.ibisworld.com/v3
    tags:
      - Industry Data
      - Market Research
    properties:
      - type: Documentation
        url: https://www.ibisworld.com/api/
      - type: Reference
        url: https://api.ibisworld.com/docs/
      - type: OpenAPI
        url: openapi/ibisworld-openapi.yml
common:
  - type: Website
    url: https://www.ibisworld.com/
  - type: Portal
    url: https://www.ibisworld.com/api/
  - type: Documentation
    url: https://api.ibisworld.com/docs/
  - type: Data Navigator
    url: https://data-navigator.ibisworld.com/
  - type: Terms of Service
    url: https://www.ibisworld.com/terms-of-use/
  - type: Rules
    url: rules/ibisworld-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
