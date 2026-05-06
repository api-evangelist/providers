---
aid: natural-resources-conservation-service
name: Natural Resources Conservation Service
description: The Natural Resources Conservation Service (NRCS) is a federal agency under the United States Department of Agriculture that works to help farmers, ranchers, and landowners conserve and protect natural resources. They provide technical assistance, financial assistance, and conservation planning to help individuals and communities implement conservation practices that improve soil health, water quality, and wildlife habitat.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Federal Government
  - Agriculture
  - Conservation
  - Soil
  - Natural Resources
url: https://raw.githubusercontent.com/api-evangelist/natural-resources-conservation-service/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: natural-resources-conservation-service:soil-data-access-api
    name: NRCS Soil Data Access
    description: Soil Data Access (SDA) is a USDA-NRCS web service that supports ad hoc query and real-time delivery of official soil survey data (SSURGO and STATSGO2) for any user-defined geographic area. The service exposes tabular query and spatial query endpoints that accept SQL-like requests and return JSON or XML responses.
    humanURL: https://sdmdataaccess.nrcs.usda.gov
    baseURL: https://sdmdataaccess.nrcs.usda.gov
    tags:
      - Soil
      - Data
      - SSURGO
      - STATSGO2
    properties:
      - url: https://sdmdataaccess.nrcs.usda.gov
        type: Documentation
      - url: https://sdmdataaccess.nrcs.usda.gov/WebServiceHelp.aspx
        type: Reference
common:
  - url: https://www.nrcs.usda.gov
    type: Website
  - url: https://www.nrcs.usda.gov/resources/data-and-reports
    type: Documentation
  - url: https://sdmdataaccess.nrcs.usda.gov
    type: Data
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
