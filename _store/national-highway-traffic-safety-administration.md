---
aid: national-highway-traffic-safety-administration
name: National Highway Traffic Safety Administration
description: The National Highway Traffic Safety Administration (NHTSA) provides APIs for vehicle safety information including vehicle recall data and the Product Information Catalog Vehicle Listing (vPIC) for decoding Vehicle Identification Numbers (VINs) and accessing vehicle specifications submitted by manufacturers.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/national-highway-traffic-safety-administration/refs/heads/main/apis.yml
created: '2024-03-30'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Federal Government
  - Safety
  - Transportation
  - Vehicles
apis:
  - aid: national-highway-traffic-safety-administration:vehicle-api
    name: NHTSA vPIC Vehicle API
    description: The NHTSA Product Information Catalog Vehicle Listing (vPIC) API provides different ways to gather information on vehicles and their specifications, including decoding VINs, retrieving manufacturer details, and accessing makes, models, equipment, and reference data.
    humanURL: https://vpic.nhtsa.dot.gov/api/
    baseURL: https://vpic.nhtsa.dot.gov/api/vehicles
    tags:
      - Safety
      - Vehicles
      - VIN
    properties:
      - type: Documentation
        url: https://vpic.nhtsa.dot.gov/api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/national-highway-traffic-safety-administration/refs/heads/main/openapi/national-highway-traffic-safety-administration-openapi.yml
common:
  - type: Website
    url: https://www.nhtsa.gov/
  - type: Portal
    url: https://vpic.nhtsa.dot.gov/api/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
