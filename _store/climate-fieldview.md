---
aid: climate-fieldview
url: https://raw.githubusercontent.com/api-evangelist/climate-fieldview/refs/heads/main/apis.yml
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
  image: https://raw.githubusercontent.com/api-evangelist/climate-fieldview/refs/heads/main/image.png
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
  - url: https://raw.githubusercontent.com/api-evangelist/climate-fieldview/refs/heads/main/openapi/climate-fieldview-platform-openapi.yml
    type: OpenAPI
  description: Climate FieldView (a Bayer product) provides a digital agriculture platform for field-level agronomic data including planting maps, soil sampling, yield data, and weather overlays. The REST API uses OAuth 2.0 for authentication with access tokens issued via authorization code grant. APIs enable access to field boundaries, as-planted and as-harvested layers, soil sample results, and agronomic recommendations. The base token endpoint is https://api.climate.com/api/oauth/token.
name: Climate Fieldview
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Climate FieldView™ is a unique platform that gives you the power to put your solutions in front of farmers across the country and around the world. Our platform offers farmers the ability to:.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

