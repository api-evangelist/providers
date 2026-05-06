---
aid: opentopography-api
name: OpenTopography API
description: OpenTopography API is a web service that provides users with access to high-resolution topographic data and tools for analysis and visualization. The API allows users to query a vast collection of LiDAR and other topographic data from around the world, making it easier for researchers, engineers, and scientists to study the Earth's surface and its features.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - DEM
  - Data
  - Elevation
  - Geospatial
  - LiDAR
  - Topographical
  - Topography
created: '2024-11-14'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/opentopography-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: opentopography-api:opentopography-api
    name: OpenTopography API
    description: Access global and regional topographic raster datasets including SRTM, ALOS World 3D, NASADEM, Copernicus DSM, USGS 3DEP DEMs (1m, 10m, 30m), and bathymetry products. Provides programmatic retrieval of digital elevation models for analysis, visualization, and downstream geospatial workflows. Quotas vary by dataset; the 1m USGS DEM is restricted to academic users.
    humanURL: https://portal.opentopography.org/apidocs
    tags:
      - DEM
      - Data
      - Elevation
      - Geospatial
      - LiDAR
      - Topography
    properties:
      - type: Documentation
        url: https://portal.opentopography.org/apidocs
      - type: OpenAPI
        url: openapi/opentopography-api-openapi.yml
      - type: Portal
        url: https://portal.opentopography.org/
      - type: SignUp
        url: https://portal.opentopography.org/myopentopo
common:
  - url: https://opentopography.org/
    name: OpenTopography
    type: Website
    description: Official OpenTopography website.
  - url: https://portal.opentopography.org/
    name: Portal
    type: Portal
    description: OpenTopography data portal for browsing and accessing datasets.
  - url: https://portal.opentopography.org/apidocs
    name: API Documentation
    type: Documentation
    description: API documentation for OpenTopography web services.
  - url: https://opentopography.org/blog
    name: Blog
    type: Blog
    description: News, updates, and articles from the OpenTopography team.
  - url: https://github.com/OpenTopography
    name: GitHub Organization
    type: GitHub Organization
    description: OpenTopography open-source projects and tooling.
  - url: https://opentopography.org/contact
    name: Contact
    type: Support
    description: Contact and support resources for OpenTopography users.
  - url: https://opentopography.org/citations
    name: Citations
    type: Citations
    description: Guidance for citing OpenTopography data and services.
  - url: https://opentopography.org/privacy
    name: Privacy
    type: Privacy
    description: OpenTopography privacy policy.
  - url: https://opentopography.org/usageterms
    name: Terms of Service
    type: Terms of Service
    description: OpenTopography terms of use for data and services.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
