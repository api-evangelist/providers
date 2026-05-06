---
aid: united-states-army-corps-of-engineers
name: United States Army Corps of Engineers
description: The U.S. Army Corps of Engineers (USACE) provides engineering and construction services for the nation, managing water resources, infrastructure, and environmental projects. USACE operates the Corps Water Management System (CWMS) Data API, a RESTful service for accessing real-time and historical water management data including time series measurements, location information, ratings, forecasts, and project data for USACE-managed water resources across the United States.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/united-states-army-corps-of-engineers/refs/heads/main/apis.yml
type: Index
created: '2024-12-25'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Engineering
  - Federal Government
  - Water Resources
  - Hydrology
  - Civil Engineering
apis:
  - aid: united-states-army-corps-of-engineers:cwms-data-api
    name: CWMS Data API
    description: The Corps Water Management System (CWMS) Data API provides a RESTful interface for retrieving water management data from the U.S. Army Corps of Engineers. Supports access to time series, locations, ratings, forecasts, levels, projects, basins, and parameters for USACE-managed water resources nationwide.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cwms-data.usace.army.mil/cwms-data/
    baseURL: https://cwms-data.usace.army.mil/cwms-data
    tags:
      - Water Management
      - Hydrology
      - Time Series
      - REST API
    properties:
      - type: Documentation
        url: https://cwms-data.usace.army.mil/cwms-data/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/united-states-army-corps-of-engineers/refs/heads/main/openapi/cwms-data-api-openapi.yml
      - type: GitHubRepository
        url: https://github.com/USACE/cwms-data-api
      - type: SwaggerUI
        url: https://cwms-data.usace.army.mil/cwms-data/swagger-ui.html
common:
  - type: Website
    url: https://www.usace.army.mil/
  - type: OpenData
    url: https://www.usace.army.mil/open/
  - type: GeospatialData
    url: https://geospatial-usace.opendata.arcgis.com/
  - type: WaterData
    url: https://water.usace.army.mil/data
  - type: DigitalLibrary
    url: https://usace.contentdm.oclc.org/
  - type: GitHub
    url: https://github.com/USACE
  - type: PermitsData
    url: https://permits.ops.usace.army.mil/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
