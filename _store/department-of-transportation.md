---
aid: department-of-transportation
name: Department of Transportation
description: The U.S. Department of Transportation (DOT) and its operating administrations - NHTSA, FMCSA, FAA, FRA, FTA, MARAD, PHMSA, and BTS - publish a number of public APIs covering vehicles, motor carriers, aviation, transit, freight, and transportation statistics.
url: https://raw.githubusercontent.com/api-evangelist/department-of-transportation/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-12-03'
modified: '2026-04-28'
type: Index
position: Consuming
access: 3rd-Party
specificationVersion: '0.20'
tags:
  - Federal Government
  - Transportation
  - Vehicles
  - Aviation
  - Motor Carriers
common:
  - url: https://www.transportation.gov/
    type: Portal
  - url: https://www.transportation.gov/digitalstrategy/developer
    type: Documentation
apis:
  - aid: department-of-transportation:nhtsa-vpic-api
    name: NHTSA vPIC API
    description: Vehicle Product Information Catalog. Decode VINs and look up makes, models, manufacturers, and World Manufacturer Identifiers.
    humanURL: https://vpic.nhtsa.dot.gov/api/
    baseURL: https://vpic.nhtsa.dot.gov/api
    tags:
      - NHTSA
      - VIN
      - Vehicles
    properties:
      - type: Documentation
        url: https://vpic.nhtsa.dot.gov/api/
      - type: OpenAPI
        url: openapi/nhtsa-vpic-api-openapi.yml
      - type: JSONSchema
        url: json-schema/vehicle-schema.json
      - type: Example
        url: examples/vin-decode-example.json
  - aid: department-of-transportation:nhtsa-recalls-api
    name: NHTSA Vehicle Safety API
    description: Vehicle, equipment, child-seat, and tire recalls; consumer complaints; defect investigations; 5-Star Safety Ratings.
    humanURL: https://api.nhtsa.gov/
    baseURL: https://api.nhtsa.gov
    tags:
      - NHTSA
      - Recalls
      - Safety
    properties:
      - type: Documentation
        url: https://api.nhtsa.gov/
      - type: OpenAPI
        url: openapi/nhtsa-recalls-api-openapi.yml
      - type: JSONSchema
        url: json-schema/recall-schema.json
      - type: Example
        url: examples/recall-example.json
  - aid: department-of-transportation:fmcsa-qcmobile-api
    name: FMCSA QCMobile API
    description: Federal Motor Carrier Safety Administration carrier registration, operating-authority, inspection, and crash data.
    humanURL: https://mobile.fmcsa.dot.gov/qc/services/getting-started
    baseURL: https://mobile.fmcsa.dot.gov/qc/services
    tags:
      - FMCSA
      - Motor Carriers
    properties:
      - type: Documentation
        url: https://mobile.fmcsa.dot.gov/qc/services/getting-started
      - type: OpenAPI
        url: openapi/fmcsa-qcmobile-api-openapi.yml
      - type: JSONSchema
        url: json-schema/carrier-schema.json
      - type: Authentication
        url: https://mobile.fmcsa.dot.gov/qc/services/manage
  - aid: department-of-transportation:faa-airport-status-api
    name: FAA Airport Status API
    description: Real-time airport status, weather, and delay information for major U.S. airports.
    humanURL: https://www.faa.gov/data
    baseURL: https://soa.smext.faa.gov/asws/api/airport
    tags:
      - FAA
      - Aviation
      - Airports
    properties:
      - type: Documentation
        url: https://www.faa.gov/data
      - type: OpenAPI
        url: openapi/faa-system-status-api-openapi.yml
  - aid: department-of-transportation:bts-data-portal
    name: Bureau of Transportation Statistics Data Portal
    description: Public datasets and downloadable data products published by BTS.
    humanURL: https://www.bts.gov/data-portals
    tags:
      - BTS
      - Statistics
    properties:
      - type: Documentation
        url: https://www.bts.gov/data-portals
  - aid: department-of-transportation:fra-safety-data
    name: Federal Railroad Administration Safety Data
    description: FRA Office of Safety Analysis - rail incident, accident, and inspection data.
    humanURL: https://safetydata.fra.dot.gov/
    tags:
      - FRA
      - Rail
    properties:
      - type: Documentation
        url: https://safetydata.fra.dot.gov/OfficeofSafety/Default.aspx
  - aid: department-of-transportation:fta-ntd-api
    name: Federal Transit Administration National Transit Database
    description: Public-transportation operating, financial, and asset data submitted by transit agencies under the National Transit Database.
    humanURL: https://www.transit.dot.gov/ntd
    tags:
      - FTA
      - Transit
    properties:
      - type: Documentation
        url: https://www.transit.dot.gov/ntd
  - aid: department-of-transportation:phmsa-pipeline-data
    name: PHMSA Pipeline Safety Data
    description: Pipeline and Hazardous Materials Safety Administration incident, mileage, and operator data for U.S. pipelines.
    humanURL: https://www.phmsa.dot.gov/data-and-statistics
    tags:
      - PHMSA
      - Pipelines
    properties:
      - type: Documentation
        url: https://www.phmsa.dot.gov/data-and-statistics
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
