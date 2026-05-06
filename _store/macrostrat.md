---
aid: macrostrat
name: Macrostrat
description: Macrostrat is a platform for the aggregation and distribution of geological data relevant to the spatial and temporal distribution of sedimentary, igneous, and metamorphic rocks as well as data extracted from them.
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/macrostrat/refs/heads/main/apis.yml
tags:
  - Geological Data
  - Geology
  - Rocks
  - Paleontology
  - Earth Science
created: '2024-11-14'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: macrostrat:macrostrat
    name: Macrostrat API
    description: The Macrostrat API exposes geological data including columns, units, sections, fossils, geologic maps, paleogeography reconstructions, measurements, age models, and cartography services. It is linked to the xDD digital library and machine reading system.
    humanURL: https://macrostrat.org
    baseURL: https://macrostrat.org/api/v2
    tags:
      - Geological Data
      - Geology
      - Rocks
      - Paleontology
      - Earth Science
    properties:
      - type: Documentation
        url: https://macrostrat.org/api/v2
      - type: Homepage
        url: https://macrostrat.org
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/macrostrat/refs/heads/main/openapi/macrostrat-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
