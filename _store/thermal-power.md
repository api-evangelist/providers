---
aid: thermal-power
url: https://raw.githubusercontent.com/api-evangelist/thermal-power/refs/heads/main/apis.yml
apis:
  - aid: thermal-power:thermal-power
    name: Thermal Power API
    tags:
      - Energy
      - Thermal Power
      - Power Generation
      - Electricity
      - Fossil Fuels
      - Nuclear
    humanURL: https://www.eia.gov/opendata/
    baseURL: https://api.eia.gov/v2
    properties:
      - url: https://www.eia.gov/opendata/documentation.php
        type: Documentation
      - url: openapi/thermal-power-openapi.yml
        type: OpenAPI
      - url: json-schema/thermal-power-plant-schema.json
        type: JSONSchema
      - url: json-ld/thermal-power-context.jsonld
        type: JSONLD
      - url: json-structure/thermal-power-structure.json
        type: JSONStructure
      - url: rules/thermal-power-rules.yml
        type: SpectralRules
      - url: capabilities/thermal-power-monitoring.yaml
        type: NaftikoCapabilities
      - url: vocabulary/thermal-power-vocabulary.yml
        type: Vocabulary
    description: The Thermal Power API provides access to thermal power generation data including plant-level operational metrics, fuel consumption, heat rate performance, and capacity utilization for coal, natural gas, petroleum, and nuclear generation assets. Data sourced from the U.S. Energy Information Administration (EIA) Open Data API.
name: Thermal Power
tags:
  - Energy
  - Thermal Power
  - Power Generation
  - Electricity
  - Coal
  - Natural Gas
  - Nuclear
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-16'
modified: '2026-05-03'
position: Consuming
description: Thermal power generation data APIs providing access to plant-level operational metrics, fuel consumption, heat rates, and generating capacity for coal, natural gas, petroleum, and nuclear power plants in the United States. Primary data source is the U.S. Energy Information Administration (EIA) Open Data API.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: EIA Open Data API
    url: https://www.eia.gov/opendata/
    type: Website
  - name: EIA API Documentation
    url: https://www.eia.gov/opendata/documentation.php
    type: Documentation
  - name: EIA API Registration
    url: https://www.eia.gov/opendata/register.php
    type: SignUp
  - name: EIA API Browser
    url: https://www.eia.gov/opendata/browser/
    type: Explorer
  - name: EIA Developer Resources
    url: https://www.eia.gov/developer/
    type: Documentation
---
