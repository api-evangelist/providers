---
aid: national-interagency-fire-center
name: National Interagency Fire Center
description: The National Interagency Fire Center (NIFC) is a collaborative effort between multiple federal agencies to address wildfires and other emergency incidents around the United States. NIFC serves as a centralized command center for coordinating resources, personnel, and information to effectively respond to and manage wildfires. NIFC publishes authoritative geospatial data through ArcGIS REST services and its open data portal.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/national-interagency-fire-center/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Emergency Management
  - Federal Government
  - Geospatial
  - Wildfire
apis:
  - aid: national-interagency-fire-center:nifc-arcgis-api
    name: NIFC ArcGIS REST Services API
    tags:
      - ArcGIS
      - Geospatial
      - Wildfire
    humanURL: https://data-nifc.opendata.arcgis.com
    baseURL: https://services3.arcgis.com/T4QMspbfLg3qTGWY/ArcGIS/rest/services
    properties:
      - url: https://data-nifc.opendata.arcgis.com
        type: Documentation
      - url: https://services3.arcgis.com/T4QMspbfLg3qTGWY/ArcGIS/rest/services
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/national-interagency-fire-center/main/openapi/national-interagency-fire-center-openapi.yml
        type: OpenAPI
    description: The NIFC ArcGIS REST services expose FeatureServer endpoints with authoritative geospatial data on wildfire incidents, fire perimeters, dispatch boundaries, fuel treatments, weather stations, and other fire management resources. Each FeatureServer supports attribute and spatial queries, paging, statistics, and standard ArcGIS output formats including JSON and GeoJSON.
common:
  - type: Website
    url: https://www.nifc.gov/
  - type: Portal
    url: https://data-nifc.opendata.arcgis.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
