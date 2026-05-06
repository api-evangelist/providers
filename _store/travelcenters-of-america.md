---
aid: travelcenters-of-america
name: TravelCenters of America
description: TravelCenters of America is the largest publicly traded full-service travel center network in the United States, operating under the TA, Petro Stopping Centers, and TA Express brands. The company provides REST APIs for truck service work order management, retail location data, fuel codes, pricing, parking availability, and shower availability.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Travel Centers
  - Truck Service
  - Retail
  - Fuel
  - Locations
  - Trucking
  - Fleet Management
created: '2026-03-24'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/travelcenters-of-america/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: travelcenters-of-america:travelcenters-of-america
    name: TravelCenters of America API
    description: REST APIs for TA and Petro travel center operations including truck service work order management, retail location data, fuel codes, pricing, parking, and shower availability across the largest US travel center network.
    humanURL: https://developer.accessta.com/
    baseURL: https://api.accessta.com/v1
    tags:
      - Travel Centers
      - Truck Service
      - Retail
      - Fuel
      - Locations
      - Trucking
      - Fleet Management
    properties:
      - type: Documentation
        url: https://developer.accessta.com/
      - type: OpenAPI
        url: openapi/travelcenters-of-america-openapi.yml
      - type: JSONSchema
        url: json-schema/travelcenters-of-america-location-schema.json
      - type: JSONStructure
        url: json-structure/travelcenters-of-america-location-structure.json
      - type: JSONLD
        url: json-ld/travelcenters-of-america-context.jsonld
      - type: SpectralRules
        url: rules/travelcenters-of-america-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/fleet-and-driver-services.yaml
      - type: Vocabulary
        url: vocabulary/travelcenters-of-america-vocabulary.yml
      - type: Sign Up
        url: https://services.accessta.com/APIRequest/DevApiRequest
      - type: Mobile App
        url: https://apps.apple.com/us/app/trucksmart/id420579235
    x-services:
      - Location and Amenities Lookup
      - Parking Availability
      - Shower Availability
      - Work Order Management
      - Documentation Search and Retrieval
      - Fuel Code Management
      - Fuel Pricing
common:
  - type: Website
    url: https://www.ta-petro.com/
  - type: Documentation
    url: https://developer.accessta.com/
  - type: Developers
    url: https://www.ta-petro.com/developers/
  - type: Sign Up
    url: https://services.accessta.com/APIRequest/DevApiRequest
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
