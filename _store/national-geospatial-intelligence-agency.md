---
aid: national-geospatial-intelligence-agency
name: National Geospatial-Intelligence Agency
description: The National Geospatial-Intelligence Agency (NGA) is a combat support agency within the U.S. Department of Defense that provides geospatial intelligence in support of national security. Through its Office of Geomatics, NGA publishes the Earth-Info portal, which exposes a REST API in OpenAPI format for downloading GPS ephemeris products, Earth Orientation Parameter Predictions (EOPP), Navdata clock state files, and short-term orbit prediction products. NGA also maintains the WGS 84 reference frame, EGM2008 gravitational model, and the GEOTRANS coordinate conversion tool.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/national-geospatial-intelligence-agency/refs/heads/main/apis.yml
created: '2024-12-25'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Federal Government
  - Geospatial
  - Intelligence
  - Defense
  - Geomatics
apis:
  - aid: national-geospatial-intelligence-agency:earth-info-rest-api
    name: NGA Earth-Info REST API
    description: NGA Office of Geomatics REST API providing programmatic download of GPS ephemeris (Center of Mass and Antenna Phase Center), Earth Orientation Parameter Predictions, Navdata clock state files, and 9-day and 30-day orbit prediction products.
    humanURL: https://earth-info.nga.mil/
    baseURL: https://earth-info.nga.mil/
    tags:
      - Geospatial
      - GPS
      - Ephemeris
      - Geodesy
      - WGS84
    properties:
      - type: Documentation
        url: https://earth-info.nga.mil/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/national-geospatial-intelligence-agency/main/openapi/national-geospatial-intelligence-agency-openapi.json
      - type: Portal
        url: https://earth-info.nga.mil/
common:
  - type: Website
    url: https://www.nga.mil/
  - type: Portal
    url: https://earth-info.nga.mil/
  - type: Tearline
    url: https://www.tearline.mil/
  - type: Contact
    url: mailto:geomatics@nga.mil
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
