---
aid: timken
name: Timken
description: The Timken Company is a global manufacturer of engineered bearings and industrial motion products including ball bearings, tapered roller bearings, seals, lubrication systems, gear drives, belts, clutches, couplings, and related motion control products serving aerospace, automotive, industrial, and energy markets.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Bearings
  - Industrial
  - Manufacturing
  - Motion Control
created: '2026-05-03'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/timken/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: timken:engineering-tools
    name: Timken Engineering Tools
    description: Interactive engineering tools for bearing selection, bearing life calculation, tolerance lookup, lubrication, gear force calculations, and precision bearing selection. Accessible through Timken's engineering portal.
    humanURL: https://engineering.timken.com/engineering-tools/
    baseURL: https://engineering.timken.com
    tags:
      - Bearings
      - Engineering
      - Industrial
      - Manufacturing
    properties:
      - type: Documentation
        url: https://engineering.timken.com/engineering-tools/
      - type: Website
        url: https://engineering.timken.com/
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/timken/refs/heads/main/json-schema/timken-bearing-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/timken/refs/heads/main/json-structure/timken-bearing-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/timken/refs/heads/main/json-ld/timken-context.jsonld
features:
  - Bearing Search and Selection
  - Bearing Fatigue Life Calculation
  - Bearing Tolerance Lookup
  - Bearing Clearance Calculations
  - Grease Lubrication Calculator
  - Gear Force Calculations
  - Unit Conversion Tool
  - Precision Bearing Selector
  - CAD Drawing Downloads
useCases:
  - Bearing selection for industrial machinery
  - Life estimation for bearing applications
  - Lubrication system design
  - Gear drive engineering calculations
integrations:
  - CAD software integration via drawings portal
  - Engineering catalog downloads
solutions:
  - Aerospace bearing solutions
  - Automotive bearing solutions
  - Industrial motion control
  - Renewable energy bearings
  - Medical device motion components
common:
  - type: Website
    url: https://www.timken.com/
  - type: Documentation
    url: https://engineering.timken.com/
  - type: Engineering Tools
    url: https://engineering.timken.com/engineering-tools/
  - type: Catalog
    url: https://www.timken.com/resources/
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/timken/refs/heads/main/json-schema/timken-bearing-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/timken/refs/heads/main/json-structure/timken-bearing-structure.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/timken/refs/heads/main/json-ld/timken-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/timken/refs/heads/main/vocabulary/timken-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
