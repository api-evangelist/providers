---
aid: climatiq
name: Climatiq
url: https://raw.githubusercontent.com/api-evangelist/climatiq/refs/heads/main/apis.yml
created: '2025-02-24'
modified: '2026-04-27'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
position: Consumer
x-type: company
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Carbon Accounting
  - Carbon Emissions
  - Climate
  - Energy
  - Environment
  - GHG Protocol
  - Sustainability
description: Climatiq provides a developer-first API for carbon accounting and emissions calculations. The platform packages a curated emission-factor database together with calculation endpoints that turn activity or spend data into auditable CO2-equivalent estimates aligned with the GHG Protocol. Capabilities span search across the factor catalog, generic activity-based estimation, and purpose-built endpoints for travel, freight (GLEC), energy, cloud computing, procurement, and the EU Carbon Border Adjustment Mechanism. The API is keyed (Bearer token) and hosted at api.climatiq.io.
apis:
  - aid: climatiq:climatiq-api
    name: Climatiq API
    tags:
      - Carbon Emissions
      - Emission Factors
      - GHG Protocol
      - Sustainability
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.climatiq.io/docs/api-reference
    baseURL: https://api.climatiq.io
    properties:
      - url: https://www.climatiq.io/docs/api-reference
        type: Documentation
      - url: https://www.climatiq.io/docs/guides/tutorials/quickstart
        type: GettingStarted
      - url: https://www.climatiq.io/docs/api-reference/search
        type: Reference
      - url: https://www.climatiq.io/docs/api-reference/estimate
        type: Reference
      - url: https://www.climatiq.io/docs/api-reference/travel
        type: Reference
      - url: https://www.climatiq.io/docs/api-reference/intermodal-freight
        type: Reference
      - url: https://www.climatiq.io/docs/api-reference/energy
        type: Reference
      - url: https://www.climatiq.io/docs/api-reference/computing
        type: Reference
      - url: https://www.climatiq.io/docs/api-reference/procurement
        type: Reference
      - url: https://www.climatiq.io/docs/api-reference/autopilot
        type: Reference
      - url: https://www.climatiq.io/docs/api-reference/classifications
        type: Reference
      - url: https://www.climatiq.io/docs/api-reference/custom-mappings
        type: Reference
      - url: https://www.climatiq.io/docs/api-reference/cbam
        type: Reference
      - url: https://www.climatiq.io/docs/changelogs/api-release
        type: ChangeLog
      - url: openapi/climatiq-openapi.yml
        type: OpenAPI
    description: The Climatiq API is a single REST surface at api.climatiq.io that groups search, estimation, and reference operations under a shared API-key (Bearer) auth model. It exposes /data/v1/search for discovering emission factors; /data/v1/estimate for activity-based estimation; family endpoints under /travel, /freight, /energy, /compute, /procurement, /autopilot, /classifications, and /cbam for purpose-built calculations; and reference endpoints for regions and unit types. All endpoints return CO2e in kilograms together with the underlying factor and gas breakdown.
common:
  - type: Website
    url: https://www.climatiq.io/
  - type: Portal
    url: https://www.climatiq.io/docs
  - type: Documentation
    url: https://www.climatiq.io/docs/api-reference
  - type: GettingStarted
    url: https://www.climatiq.io/docs/guides/tutorials/quickstart
  - type: Pricing
    url: https://www.climatiq.io/pricing
  - type: Blog
    url: https://www.climatiq.io/blog
  - type: Trust
    url: https://trust.climatiq.io/
  - type: Support
    url: https://www.climatiq.io/support
  - type: Customers
    url: https://www.climatiq.io/customers
  - type: Login
    url: https://auth.climatiq.io/login
  - type: Playground
    url: https://www.climatiq.io/demo
  - type: Partners
    url: https://www.climatiq.io/partner-with-climatiq
  - type: Newsletter
    url: https://www.climatiq.io/newsletter
  - type: Versioning
    url: https://www.climatiq.io/docs/changelogs/api-release
  - type: OpenAPI
    url: openapi/climatiq-openapi.yml
  - type: JSONSchema
    url: json-schema/climatiq-emission-estimate-schema.json
  - type: JSONLDContext
    url: json-ld/climatiq-context.jsonld
  - type: Spectral
    url: rules/climatiq-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/climatiq-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
