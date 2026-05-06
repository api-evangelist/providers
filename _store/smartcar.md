---
aid: smartcar
name: Smartcar
description: Smartcar is a connected vehicle platform that provides a standardized REST API for accessing vehicle data and sending commands to connected cars. The API enables developers to retrieve battery levels, odometer readings, location, lock/unlock doors, start/stop charging, and access vehicle attributes across multiple vehicle brands through a single integration. Smartcar supports OAuth 2.0 authorization and covers EVs and ICE vehicles from dozens of OEMs including Tesla, Ford, BMW, Honda, and more.
url: https://raw.githubusercontent.com/api-evangelist/smartcar/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Automotive
  - Connected Vehicles
  - IoT
  - Mobility
  - Fleet Management
  - EV Management
  - Telematics
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
apis:
  - aid: smartcar:vehicles-api
    name: Smartcar Vehicles API
    description: The Smartcar Vehicles API lets you access standardized vehicle data and send commands to connected vehicles. Retrieve signals such as battery level, odometer, location, fuel, engine oil, and diagnostic codes, as well as issue commands like lock/unlock doors, start/stop charging, set charge limit, and set navigation destinations across multiple vehicle brands. Uses OAuth 2.0 bearer token authentication.
    humanURL: https://smartcar.com/docs/api/
    tags:
      - Connected Cars
      - Telematics
      - Vehicles
      - Fleet
      - EV
    properties:
      - type: Documentation
        url: https://smartcar.com/docs/api/
      - type: Reference
        url: https://smartcar.com/docs/api-reference/intro
      - type: Authentication
        url: https://smartcar.com/docs/api-reference/intro
      - type: OpenAPI
        url: openapi/smartcar-vehicles-openapi.yml
      - type: Postman
        url: https://www.postman.com/smartcar/smartcar-api/documentation/fqmwehs/smartcar-api
common:
  - type: Portal
    url: https://smartcar.com/
  - type: Documentation
    url: https://smartcar.com/docs/api/
  - type: Website
    url: https://smartcar.com/
  - type: GitHubOrganization
    url: https://github.com/smartcar
  - type: Pricing
    url: https://smartcar.com/pricing/
  - type: OpenAPI
    url: openapi/smartcar-vehicles-openapi.yml
  - type: Spectral
    url: rules/smartcar-rules.yml
  - type: Capabilities
    url: capabilities/connected-vehicle-management.yaml
  - type: JSONSchema
    url: json-schema/smartcar-vehicle-schema.json
  - type: JSONSchema
    url: json-schema/smartcar-battery-schema.json
  - type: JSONStructure
    url: json-structure/smartcar-vehicles-structure.json
  - type: JSONLD
    url: json-ld/smartcar-context.jsonld
  - type: Vocabulary
    url: vocabulary/smartcar-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
