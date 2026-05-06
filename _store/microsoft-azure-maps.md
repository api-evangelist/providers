---
name: Azure Maps
description: Azure Maps provides geospatial APIs for maps, routing, geocoding, traffic, weather, and spatial analysis. The service offers a comprehensive suite of REST APIs to embed location intelligence into applications spanning mobile, web, and IoT scenarios across multiple transport modes.
image: https://azure.microsoft.com/svghandler/azure-maps/
tags:
  - Geocoding
  - Geospatial
  - Location
  - Maps
  - Mobility
  - Routing
  - Traffic
  - Weather
created: '2026-03-13'
modified: '2026-04-28'
url: https://azure.microsoft.com/en-us/services/azure-maps/
specificationVersion: '0.18'
apis:
  - name: Azure Maps Search API
    description: Provides geocoding, reverse geocoding, address parsing, point of interest search, and structured search. Returns candidate matches ranked by relevance for free-form, structured, and POI queries with worldwide coverage.
    image: https://azure.microsoft.com/svghandler/azure-maps/
    humanURL: https://learn.microsoft.com/en-us/rest/api/maps/search
    baseURL: https://atlas.microsoft.com
    tags:
      - Address
      - Geocoding
      - POI
      - Reverse Geocoding
      - Search
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/maps/search
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/azure-maps/azure-maps-authentication
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/azure-maps/how-to-use-search-service
  - name: Azure Maps Route API
    description: Calculates routes between origin and destination, provides turn-by-turn directions, supports multiple travel modes, traffic-aware routing, route matrices, and route range (isochrone) calculations.
    image: https://azure.microsoft.com/svghandler/azure-maps/
    humanURL: https://learn.microsoft.com/en-us/rest/api/maps/route
    baseURL: https://atlas.microsoft.com
    tags:
      - Directions
      - Isochrone
      - Routing
      - Traffic-Aware
      - Travel Modes
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/maps/route
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/azure-maps/how-to-use-best-practices-for-routing
  - name: Azure Maps Render API
    description: Returns map tiles, static images, and vector tiles in multiple styles including satellite, road, and hybrid. Supports raster and vector tile formats, custom imagery, and traffic overlays for embedding maps into applications.
    image: https://azure.microsoft.com/svghandler/azure-maps/
    humanURL: https://learn.microsoft.com/en-us/rest/api/maps/render
    baseURL: https://atlas.microsoft.com
    tags:
      - Map Tiles
      - Raster
      - Render
      - Static Images
      - Vector Tiles
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/maps/render
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/azure-maps/zoom-levels-and-tile-grid
  - name: Azure Maps Traffic API
    description: Provides real-time and historical traffic data including traffic flow, incident reports, and traffic tile imagery. Useful for routing, fleet management, and applications requiring up-to-date road conditions.
    image: https://azure.microsoft.com/svghandler/azure-maps/
    humanURL: https://learn.microsoft.com/en-us/rest/api/maps/traffic
    baseURL: https://atlas.microsoft.com
    tags:
      - Flow
      - Incidents
      - Real-Time
      - Traffic
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/maps/traffic
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/azure-maps/traffic-coverage
  - name: Azure Maps Weather API
    description: Provides current weather conditions, hourly and daily forecasts, severe weather alerts, weather along a route, and historical weather. Powered by AccuWeather data and global coverage.
    image: https://azure.microsoft.com/svghandler/azure-maps/
    humanURL: https://learn.microsoft.com/en-us/rest/api/maps/weather
    baseURL: https://atlas.microsoft.com
    tags:
      - Alerts
      - Forecast
      - Historical
      - Weather
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/maps/weather
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/azure-maps/weather-coverage
  - name: Azure Maps Timezone API
    description: Returns time zone information for a given coordinate, IANA time zone ID, or Windows time zone ID. Includes current time, daylight saving offsets, and time zone metadata.
    image: https://azure.microsoft.com/svghandler/azure-maps/
    humanURL: https://learn.microsoft.com/en-us/rest/api/maps/timezone
    baseURL: https://atlas.microsoft.com
    tags:
      - DST
      - IANA
      - Time Zone
      - UTC Offset
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/maps/timezone
  - name: Azure Maps Geolocation API
    description: Returns the ISO country code for a supplied IP address, useful for content localization, regulatory compliance, and access control based on user geographic location.
    image: https://azure.microsoft.com/svghandler/azure-maps/
    humanURL: https://learn.microsoft.com/en-us/rest/api/maps/geolocation
    baseURL: https://atlas.microsoft.com
    tags:
      - Country Code
      - Geolocation
      - IP Address
      - Localization
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/maps/geolocation
  - name: Azure Maps Spatial API
    description: Performs spatial computations such as distance, closest point, point in polygon, geofence evaluation, and great circle distance. Enables location analytics and spatial reasoning workloads.
    image: https://azure.microsoft.com/svghandler/azure-maps/
    humanURL: https://learn.microsoft.com/en-us/rest/api/maps/spatial
    baseURL: https://atlas.microsoft.com
    tags:
      - Geofencing
      - Point in Polygon
      - Spatial Analysis
      - Spatial Operations
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/maps/spatial
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/azure-maps/geofence-geojson
  - name: Azure Maps Elevation API
    description: Returns elevation data in meters above sea level for points, polylines, and bounding boxes. Useful for terrain analysis, topographic visualization, and elevation profile calculations along a route.
    image: https://azure.microsoft.com/svghandler/azure-maps/
    humanURL: https://learn.microsoft.com/en-us/rest/api/maps/elevation
    baseURL: https://atlas.microsoft.com
    tags:
      - DEM
      - Elevation
      - Terrain
      - Topography
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/maps/elevation
  - name: Azure Maps Creator API
    description: Indoor maps service for creating, managing, and rendering custom indoor maps. Supports drawing package conversion, dataset and tileset management, feature state, and wayfinding for indoor environments.
    image: https://azure.microsoft.com/svghandler/azure-maps/
    humanURL: https://learn.microsoft.com/en-us/rest/api/maps/creator
    baseURL: https://atlas.microsoft.com
    tags:
      - Creator
      - Indoor Maps
      - Tileset
      - Wayfinding
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/maps/creator
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/azure-maps/creator-indoor-maps
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/azure-maps/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/azure-maps/quick-demo-map-app
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/azure-maps/azure-maps-authentication
  - type: SDKs
    url: https://learn.microsoft.com/en-us/azure/azure-maps/about-azure-maps
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/azure-maps/
  - type: Status
    url: https://status.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/options/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/tag/azure-maps/
  - type: Change Log
    url: https://learn.microsoft.com/en-us/azure/azure-maps/release-notes-map-control
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: Website
    url: https://azure.microsoft.com/en-us/products/azure-maps
  - type: Login
    url: https://portal.azure.com
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
