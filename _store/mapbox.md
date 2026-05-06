---
aid: mapbox
name: Mapbox
description: Mapbox is a leading mapping and location data platform that provides tools and services to help developers and businesses create custom maps, visualize geospatial data, and build location-aware applications. Their platform offers a wide range of mapping technologies, from interactive maps and map design tools to geocoding and routing services.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consuming
tags:
  - Mapping
  - Maps
  - Geospatial
  - Location
url: https://raw.githubusercontent.com/api-evangelist/mapbox/refs/heads/main/apis.yml
created: '2023-11-22'
modified: '2026-05-04'
specificationVersion: '0.20'
apis:
  - aid: mapbox:mapbox-tiling-service
    name: Mapbox Tiling Service
    description: Mapbox Tiling Service (MTS) is a tool for creating vector tilesets. With MTS, you use sets of configuration options (tileset recipes) to transform your geospatial data into vector tiles. The resulting tiles are hosted on Mapbox servers for use in your applications.
    humanURL: https://docs.mapbox.com/api/maps/mapbox-tiling-service/
    baseURL: https://api.mapbox.com
    tags:
      - Mapping
      - Tiles
      - Vector Tiles
    properties:
      - type: Documentation
        url: https://docs.mapbox.com/api/maps/mapbox-tiling-service/
  - aid: mapbox:vector-tiles-api
    name: Mapbox Vector Tiles API
    description: The Mapbox Vector Tiles API serves vector tiles from Mapbox-hosted vector tilesets.
    humanURL: https://docs.mapbox.com/api/maps/vector-tiles/
    baseURL: https://api.mapbox.com
    tags:
      - Mapping
      - Tiles
      - Vector Tiles
    properties:
      - type: Documentation
        url: https://docs.mapbox.com/api/maps/vector-tiles/
  - aid: mapbox:mapbox-raster-tiles-api
    name: Mapbox Raster Tiles API
    description: The Mapbox Raster Tiles API serves raster tiles generated from satellite imagery tilesets and tilesets generated from raster data uploaded to Mapbox.com.
    humanURL: https://docs.mapbox.com/api/maps/raster-tiles/
    baseURL: https://api.mapbox.com
    tags:
      - Mapping
      - Tiles
      - Raster Tiles
    properties:
      - type: Documentation
        url: https://docs.mapbox.com/api/maps/raster-tiles/
  - aid: mapbox:mapbox-static-images-api
    name: Mapbox Static Images API
    description: The Mapbox Static Images API serves standalone, static map images generated from Mapbox Studio styles. These images can be displayed on web and mobile devices without the aid of a mapping library or API.
    humanURL: https://docs.mapbox.com/api/maps/static-images/
    baseURL: https://api.mapbox.com
    tags:
      - Mapping
      - Static Images
    properties:
      - type: Documentation
        url: https://docs.mapbox.com/api/maps/static-images/
  - aid: mapbox:mapbox-static-tiles-api
    name: Mapbox Static Tiles API
    description: The Mapbox Static Tiles API serves raster tiles generated from Mapbox Studio styles. Raster tiles can be used in traditional web mapping libraries like Mapbox.js, Leaflet, OpenLayers, and others to create interactive slippy maps.
    humanURL: https://docs.mapbox.com/api/maps/static-tiles/
    baseURL: https://api.mapbox.com
    tags:
      - Mapping
      - Tiles
      - Static Tiles
    properties:
      - type: Documentation
        url: https://docs.mapbox.com/api/maps/static-tiles/
  - aid: mapbox:mapbox-styles-api
    name: Mapbox Styles API
    description: The Mapbox Styles API lets you read and change map styles, fonts, and images. This API is the basis for Mapbox Studio.
    humanURL: https://docs.mapbox.com/api/maps/styles/
    baseURL: https://api.mapbox.com
    tags:
      - Mapping
      - Styles
    properties:
      - type: Documentation
        url: https://docs.mapbox.com/api/maps/styles/
  - aid: mapbox:mapbox-tilequery-api
    name: Mapbox Tilequery API
    description: The Mapbox Tilequery API allows you to retrieve data about specific features from a vector tileset, based on a given latitude and longitude. The Tilequery API makes it possible to query for features within a radius, do point-in-polygon queries, query for features in multiple composite layers, and augment data from the Mapbox Geocoding API with custom data.
    humanURL: https://docs.mapbox.com/api/maps/tilequery/
    baseURL: https://api.mapbox.com
    tags:
      - Mapping
      - Tile Query
      - Geospatial
    properties:
      - type: Documentation
        url: https://docs.mapbox.com/api/maps/tilequery/
  - aid: mapbox:mapbox-uploads-api
    name: Mapbox Uploads API
    description: The Mapbox Uploads API transforms geographic data into tilesets that can be used with maps and geographic applications. Given a wide variety of geospatial formats, it normalizes projections and generates tiles at multiple zoom levels to make data viewable on the web.
    humanURL: https://docs.mapbox.com/api/maps/uploads/
    baseURL: https://api.mapbox.com
    tags:
      - Mapping
      - Uploads
      - Geospatial
    properties:
      - type: Documentation
        url: https://docs.mapbox.com/api/maps/uploads/
  - aid: mapbox:mapbox-datasets-api
    name: Mapbox Datasets API
    description: The Mapbox Datasets API supports reading, creating, updating, and removing features from a dataset. Datasets contain one or more collections of GeoJSON features.
    humanURL: https://docs.mapbox.com/api/maps/datasets/
    baseURL: https://api.mapbox.com
    tags:
      - Mapping
      - Datasets
      - GeoJSON
    properties:
      - type: Documentation
        url: https://docs.mapbox.com/api/maps/datasets/
  - aid: mapbox:mapbox-fonts-api
    name: Mapbox Fonts API
    description: 'The Mapbox Fonts API accepts fonts as raw binary data, allows those fonts to be deleted, and generates encoded letters for map renderers. Two types of fonts are supported: TrueType fonts (.ttf) and OpenType fonts (.otf).'
    humanURL: https://docs.mapbox.com/api/maps/fonts/
    baseURL: https://api.mapbox.com
    tags:
      - Mapping
      - Fonts
    properties:
      - type: Documentation
        url: https://docs.mapbox.com/api/maps/fonts/
common:
  - type: Support
    url: https://docs.mapbox.com/help/
  - type: SDK
    url: https://docs.mapbox.com/api/overview/#sdk-and-library-support
  - type: Authentication
    url: https://docs.mapbox.com/api/overview/#access-tokens-and-token-scopes
  - type: Versioning
    url: https://docs.mapbox.com/api/overview/#api-versioning
  - type: Rate Limits
    url: https://docs.mapbox.com/api/overview/#rate-limits
  - type: CORS
    url: https://docs.mapbox.com/api/overview/#https-and-cors
  - type: Pagination
    url: https://docs.mapbox.com/api/overview/#pagination
  - type: Login
    url: https://account.mapbox.com/auth/signin/
  - type: Sign Up
    url: https://account.mapbox.com/auth/signup/
  - type: Terms of Service
    url: https://www.mapbox.com/tos/
  - type: Privacy
    url: https://www.mapbox.com/privacy/
  - type: Security
    url: https://www.mapbox.com/platform/security/
  - type: Cheatsheet
    url: https://labs.mapbox.com/developer-cheatsheet/
  - type: Getting Started
    url: https://docs.mapbox.com/help/getting-started
  - type: Tutorials
    url: https://docs.mapbox.com/help/tutorials
  - type: Videos
    url: https://docs.mapbox.com/help/how-to-videos
  - type: Troubleshooting
    url: https://docs.mapbox.com/help/troubleshooting
  - type: Glossary
    url: https://docs.mapbox.com/help/glossary
  - type: Website
    url: https://www.mapbox.com/
  - type: Features
    data:
      - Maps SDKs for iOS and Android (free up to 25k MAU, then $4/1k MAU)
      - Mapbox GL JS for web map loads (free up to 50k loads, then $5/1k)
      - Static Images API (free up to 50k req, then $1/1k)
      - Directions API for driving/walking/cycling routes (free up to 100k req, then $2/1k)
      - Temporary Geocoding API ($0.75/1k above 100k free)
      - Search Box API session-based pricing ($3/1k sessions)
      - Address Autofill ($12.50/1k sessions above 1k free)
      - Navigation SDK v3 metered ($0.30/MAU + $0.08/trip) or unlimited (custom)
      - Per-token, per-endpoint rate limits (60-1,250 req/min defaults)
      - Volume discounts at higher usage levels
      - Statistics API for usage reporting
      - Vector and raster tile services
      - Mapbox Studio for custom map design
      - Tilequery API for spatial point-in-polygon queries
      - Map Matching API to snap GPS traces to road networks
    sources:
      - https://www.mapbox.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
---
