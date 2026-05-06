---
aid: first-street
name: First Street
description: First Street models use validated and proven methodologies to ensure model accuracy. We measure and predict the impact of a peril based on the underlying physics of how an actual event would transpire. First Street exposes Climate Risk, Enterprise, and Raster Map APIs for property-level climate risk data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-28'
position: Consumer
tags:
  - Environment
  - Modeling
  - Risk
  - Climate
url: https://raw.githubusercontent.com/api-evangelist/first-street/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: first-street:climate-risk
    name: First Street Climate Risk API
    tags:
      - Environment
      - Modeling
      - Risk
      - Climate
    humanURL: https://docs.firststreet.org/api
    properties:
      - url: https://firststreet.org/
        type: Website
      - url: https://docs.firststreet.org/api
        type: Documentation
    description: The Climate Risk API provides physical climate risk data globally, delivering property-level insights into hazards including flood, wildfire, heat, wind, and air quality.
  - aid: first-street:enterprise
    name: First Street Enterprise API
    tags:
      - Environment
      - Modeling
      - Risk
      - Climate
    humanURL: https://docs.firststreet.org/api
    properties:
      - url: https://firststreet.org/
        type: Website
      - url: https://docs.firststreet.org/api
        type: Documentation
    description: The Enterprise API offers aggregated climate risk views for portfolios, enabling enterprise users to assess risk across multiple properties and geographic regions.
  - aid: first-street:raster-map
    name: First Street Raster Map API
    tags:
      - Environment
      - Modeling
      - Risk
      - Climate
      - Mapping
    humanURL: https://docs.firststreet.org/api
    properties:
      - url: https://firststreet.org/
        type: Website
      - url: https://docs.firststreet.org/api
        type: Documentation
    description: The Raster Map API delivers visual raster layers of climate perils for mapping and visualization use cases.
common:
  - type: Website
    url: https://firststreet.org/
  - type: Documentation
    url: https://docs.firststreet.org/api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
