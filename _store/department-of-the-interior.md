---
aid: department-of-the-interior
name: Department of the Interior
description: The U.S. Department of the Interior manages federal lands, water, wildlife, energy and mineral resources, and trust responsibilities to American Indian, Alaska Native, and insular communities. Interior bureaus - National Park Service, U.S. Geological Survey, Bureau of Land Management, U.S. Fish and Wildlife Service, Bureau of Reclamation, Bureau of Indian Affairs, and the Office of Natural Resources Revenue - publish a number of public APIs and open-data portals.
url: https://raw.githubusercontent.com/api-evangelist/department-of-the-interior/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/apis-json.png
created: '2024-12-25'
modified: '2026-04-28'
type: Index
position: Consuming
access: 3rd-Party
specificationVersion: '0.20'
tags:
  - Federal Government
  - Public Lands
  - Natural Resources
  - Geospatial
common:
  - url: https://www.doi.gov/
    type: Portal
  - url: https://www.doi.gov/developer
    type: Documentation
  - url: https://data.doi.gov/
    type: Datasets
apis:
  - aid: department-of-the-interior:nps-data-api
    name: National Park Service Data API
    description: Search and retrieve parks, alerts, campgrounds, visitor centers, events, and articles for U.S. National Park Service units.
    humanURL: https://www.nps.gov/subjects/developer/api-documentation.htm
    baseURL: https://developer.nps.gov/api/v1
    tags:
      - NPS
      - Parks
    properties:
      - type: Documentation
        url: https://www.nps.gov/subjects/developer/api-documentation.htm
      - type: OpenAPI
        url: openapi/nps-data-api-openapi.yml
      - type: JSONSchema
        url: json-schema/nps-park-schema.json
      - type: Example
        url: examples/park-example.json
      - type: Authentication
        url: https://www.nps.gov/subjects/developer/get-started.htm
  - aid: department-of-the-interior:usgs-earthquake-api
    name: USGS Earthquake Hazards Program API
    description: FDSN-compatible earthquake catalog API returning GeoJSON FeatureCollections for queries by time, magnitude, location, and depth.
    humanURL: https://earthquake.usgs.gov/fdsnws/event/1/
    baseURL: https://earthquake.usgs.gov/fdsnws/event/1
    tags:
      - USGS
      - Earthquakes
      - Geospatial
    properties:
      - type: Documentation
        url: https://earthquake.usgs.gov/fdsnws/event/1/
      - type: OpenAPI
        url: openapi/usgs-earthquake-api-openapi.yml
      - type: JSONSchema
        url: json-schema/earthquake-feature-schema.json
      - type: Example
        url: examples/earthquake-example.json
  - aid: department-of-the-interior:usgs-water-services-api
    name: USGS Water Services API
    description: Real-time and historical surface-water, groundwater, and water-quality data via the National Water Information System.
    humanURL: https://waterservices.usgs.gov/
    baseURL: https://waterservices.usgs.gov/nwis
    tags:
      - USGS
      - Water
      - Hydrology
    properties:
      - type: Documentation
        url: https://waterservices.usgs.gov/
      - type: OpenAPI
        url: openapi/usgs-water-services-api-openapi.yml
  - aid: department-of-the-interior:doi-open-data
    name: DOI Open Data Catalog
    description: Department-wide open-data catalog at data.doi.gov, including datasets from all Interior bureaus.
    humanURL: https://data.doi.gov/
    tags:
      - Open Data
    properties:
      - type: Documentation
        url: https://data.doi.gov/
  - aid: department-of-the-interior:blm-public-lands
    name: BLM Public Lands Data
    description: Bureau of Land Management public-land data, including the Land Records System, mining claims, and recreation areas.
    humanURL: https://www.blm.gov/about/data
    tags:
      - BLM
      - Public Lands
    properties:
      - type: Documentation
        url: https://www.blm.gov/about/data
  - aid: department-of-the-interior:usfws-environmental-conservation-api
    name: USFWS Environmental Conservation Online System (ECOS) API
    description: U.S. Fish and Wildlife Service data on listed species under the Endangered Species Act and the National Wildlife Refuge System.
    humanURL: https://ecos.fws.gov/ecp/
    tags:
      - USFWS
      - Wildlife
      - Endangered Species
    properties:
      - type: Documentation
        url: https://ecos.fws.gov/ecp/
  - aid: department-of-the-interior:bor-water-data
    name: Bureau of Reclamation Water Data
    description: Reclamation reservoir, dam, and water-operations data for the western United States.
    humanURL: https://www.usbr.gov/projects/index.php
    tags:
      - Reclamation
      - Water
      - Dams
    properties:
      - type: Documentation
        url: https://www.usbr.gov/projects/index.php
  - aid: department-of-the-interior:onrr-revenue-data
    name: ONRR Natural Resources Revenue Data
    description: Office of Natural Resources Revenue datasets on royalty, rent, and bonus revenue from federal energy and mineral production.
    humanURL: https://revenuedata.doi.gov/
    tags:
      - ONRR
      - Revenue
    properties:
      - type: Documentation
        url: https://revenuedata.doi.gov/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
