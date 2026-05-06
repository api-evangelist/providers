---
aid: climate-fieldview
name: Climate FieldView
url: https://raw.githubusercontent.com/api-evangelist/climate-fieldview/refs/heads/main/apis.yml
created: '2025-03-05'
modified: '2026-04-26'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
position: Consumer
x-type: company
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agriculture
  - Bayer
  - Crop Data
  - Field Boundaries
  - Harvest
  - OAuth2
  - Planting
  - Precision Ag
description: Climate FieldView is a digital agriculture platform from Bayer (originally developed by The Climate Corporation) that gives growers, agronomists, and agribusiness partners a single view of field-level operations. The platform ingests as-planted, as-applied, and as-harvested data from field equipment, combines it with imagery, weather, and soil layers, and exposes those agronomic datasets through a REST API at api.climate.com. Authentication is via OAuth 2.0 authorization-code grant, and resources include fields, planting and harvest activities, application records, and soil samples.
apis:
  - aid: climate-fieldview:fieldview-platform-api
    name: Climate FieldView Platform API
    tags:
      - Agriculture
      - Bayer
      - Crop Data
      - Field Boundaries
      - Harvest
      - OAuth2
      - Planting
      - Precision Ag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://dev.fieldview.com/
    baseURL: https://api.climate.com
    properties:
      - url: https://dev.fieldview.com/technical-documentation/
        type: Documentation
      - url: https://dev.fieldview.com/api-details/
        type: Authentication
      - url: https://dev.fieldview.com/faq/
        type: FAQ
      - url: https://dev.fieldview.com/technical-documentation/next-versions/
        type: ChangeLog
      - url: https://github.com/TheClimateCorporation/api-example
        type: SDKs
      - url: openapi/climate-fieldview-platform-openapi.yml
        type: OpenAPI
    description: The Climate FieldView Platform API is a partner-oriented REST API for reading and writing field-level agronomic data on behalf of growers who have linked their FieldView account. Endpoints expose fields (with GeoJSON boundaries), planting layers, harvest layers, application activities, and soil sample results, and use OAuth 2.0 access tokens passed in the Authorization header. The token endpoint is https://api.climate.com/api/oauth/token; data endpoints live under https://api.climate.com/api/v4 and return JSON with paginated list responses.
common:
  - type: Website
    url: https://climate.com/
  - type: Portal
    url: https://dev.fieldview.com/
  - type: Documentation
    url: https://dev.fieldview.com/technical-documentation/
  - type: Authentication
    url: https://dev.fieldview.com/api-details/
  - type: GettingStarted
    url: https://dev.fieldview.com/faq/
  - type: TermsOfService
    url: https://climate.com/en-us/legal/terms-of-service.html
  - type: PrivacyPolicy
    url: https://climate.com/legal/privacy-policy
  - type: GitHubOrg
    url: https://github.com/TheClimateCorporation/api-example
  - type: Partners
    url: https://climate.com/partners
  - type: OpenAPI
    url: openapi/climate-fieldview-platform-openapi.yml
  - type: JSONSchema
    url: json-schema/climate-fieldview-field-schema.json
  - type: JSONLDContext
    url: json-ld/climate-fieldview-context.jsonld
  - type: Spectral
    url: rules/climate-fieldview-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/climate-fieldview-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
