---
aid: tomtom
name: TomTom
description: TomTom provides a comprehensive suite of location technology APIs and SDKs including maps, search, routing, traffic, navigation, and automotive data services. The TomTom developer platform is trusted by major automotive manufacturers, logistics companies, and application developers. APIs cover real-time traffic incidents and flow, route calculation, geocoding, points of interest search, geofencing, parking availability, fuel prices, and electric vehicle routing. TomTom also provides an MCP Server for AI integration with location intelligence.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Maps
  - Traffic
  - Transportation
  - Navigation
  - Location
  - Geospatial
  - Routing
  - Geocoding
created: '2025-01-07'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/tomtom/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tomtom:tomtom-maps-api
    name: TomTom Maps API
    description: The TomTom Maps API provides raster and vector map tiles for display in web and mobile applications. Includes copyright information endpoints and supports 19+ zoom levels. Returns PNG/JPG tiles for raster and Protocol Buffer format for vector tiles.
    humanURL: https://developer.tomtom.com/map-display-api/documentation/product-information/introduction
    baseURL: https://api.tomtom.com
    tags:
      - Maps
      - Tiles
      - Raster
      - Vector
    properties:
      - type: Documentation
        url: https://developer.tomtom.com/map-display-api/documentation/product-information/introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tomtom/refs/heads/main/openapi/tomtom-maps-openapi.yml
  - aid: tomtom:tomtom-search-api
    name: TomTom Search API
    description: The TomTom Search API provides fuzzy search for addresses, points of interest, and geographic features. Returns latitude/longitude coordinates, place details, and geometry data. Includes additional data retrieval, structured geocoding, and batch search capabilities.
    humanURL: https://developer.tomtom.com/search-api/documentation/product-information/introduction
    baseURL: https://api.tomtom.com
    tags:
      - Search
      - Geocoding
      - Points of Interest
      - Location
    properties:
      - type: Documentation
        url: https://developer.tomtom.com/search-api/documentation/product-information/introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tomtom/refs/heads/main/openapi/tomtom-search-openapi.yml
      - type: API Explorer
        url: https://developer.tomtom.com/search-api/api-explorer
  - aid: tomtom:tomtom-routing-api
    name: TomTom Routing API
    description: The TomTom Routing API calculates routes between origins and destinations with support for up to 150 waypoints, real-time and historical traffic, vehicle type optimization, EV consumption models, reachable range calculation, and batch routing for multiple route requests.
    humanURL: https://developer.tomtom.com/routing-api/documentation/tomtom-maps/product-information/introduction
    baseURL: https://api.tomtom.com
    tags:
      - Routing
      - Navigation
      - Transportation
      - Electric Vehicle
    properties:
      - type: Documentation
        url: https://developer.tomtom.com/routing-api/documentation/tomtom-maps/product-information/introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tomtom/refs/heads/main/openapi/tomtom-routing-openapi.yml
      - type: API Explorer
        url: https://developer.tomtom.com/routing-api/api-explorer
  - aid: tomtom:tomtom-traffic-api
    name: TomTom Traffic API
    description: The TomTom Traffic API provides real-time traffic incidents and flow data. The Traffic Incidents service delivers accurate information about jams, accidents, and delays. The Traffic Flow service provides observed speeds and travel times updated every minute for key roads. Includes raster and vector tile formats.
    humanURL: https://developer.tomtom.com/traffic-api/documentation/product-information/introduction
    baseURL: https://api.tomtom.com
    tags:
      - Traffic
      - Incidents
      - Real-Time
      - Transportation
    properties:
      - type: Documentation
        url: https://developer.tomtom.com/traffic-api/documentation/product-information/introduction
      - type: API Explorer
        url: https://developer.tomtom.com/traffic-api/api-explorer
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tomtom/refs/heads/main/openapi/tomtom-traffic-openapi.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/tomtom/refs/heads/main/capabilities/location-intelligence.yaml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/tomtom/refs/heads/main/rules/tomtom-rules.yml
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/tomtom/refs/heads/main/vocabulary/tomtom-vocabulary.yml
  - aid: tomtom:tomtom-geocoding-api
    name: TomTom Geocoding API
    description: The TomTom Geocoding API converts structured addresses into geographic coordinates and supports reverse geocoding to translate coordinates into human-readable addresses. The Premium Geocoding API adds parking and building entrance location data.
    humanURL: https://developer.tomtom.com/geocoding-api/documentation/product-information/introduction
    baseURL: https://api.tomtom.com
    tags:
      - Geocoding
      - Location
      - Address
    properties:
      - type: Documentation
        url: https://developer.tomtom.com/geocoding-api/documentation/product-information/introduction
      - type: API Explorer
        url: https://developer.tomtom.com/geocoding-api/api-explorer
  - aid: tomtom:tomtom-fuel-prices-api
    name: TomTom Fuel Prices API
    description: The TomTom Fuel Prices API provides current fuel price information at specific fueling stations, including price by fuel type.
    humanURL: https://developer.tomtom.com/fuel-prices-api/documentation/tomtom-maps/product-information/introduction
    baseURL: https://api.tomtom.com
    tags:
      - Fuel
      - Prices
      - Automotive
    properties:
      - type: Documentation
        url: https://developer.tomtom.com/fuel-prices-api/documentation/tomtom-maps/product-information/introduction
  - aid: tomtom:tomtom-parking-availability-api
    name: TomTom Parking Availability API
    description: The TomTom Parking Availability API provides real-time availability status of parking sites and on-street parking, including pricing information.
    humanURL: https://developer.tomtom.com/parking-availability-api/documentation/tomtom-maps/product-information/introduction
    baseURL: https://api.tomtom.com
    tags:
      - Parking
      - Transportation
      - Real-Time
    properties:
      - type: Documentation
        url: https://developer.tomtom.com/parking-availability-api/documentation/tomtom-maps/product-information/introduction
  - aid: tomtom:tomtom-geofencing-api
    name: TomTom Geofencing API
    description: The TomTom Geofencing API enables creation and management of geofence boundaries, location history tracking, and notification delivery when assets enter or exit defined perimeters.
    humanURL: https://developer.tomtom.com/geofencing-api/documentation/product-information/introduction
    baseURL: https://api.tomtom.com
    tags:
      - Geofencing
      - Location
      - Tracking
      - Notifications
    properties:
      - type: Documentation
        url: https://developer.tomtom.com/geofencing-api/documentation/product-information/introduction
  - aid: tomtom:tomtom-autostream-api
    name: TomTom AutoStream API
    description: TomTom AutoStream is a map data delivery platform optimized for on-demand and over-the-air cloud-to-device and cloud-to-cloud data streaming for automotive applications.
    humanURL: https://developer.tomtom.com/autostream-sdk/documentation/product-information/introduction
    baseURL: https://api.tomtom.com
    tags:
      - Maps
      - Streaming
      - Automotive
    properties:
      - type: Documentation
        url: https://developer.tomtom.com/autostream-sdk/documentation/product-information/introduction
features:
  - Real-time traffic flow and incidents
  - Route calculation with traffic optimization
  - Fuzzy address and POI search
  - Raster and vector map tiles
  - Geocoding and reverse geocoding
  - Electric vehicle routing
  - Geofencing and location tracking
  - Parking availability and pricing
  - Fuel price lookup
  - Batch routing and search
  - Waypoint optimization
  - MCP Server for AI integration
useCases:
  - Navigation application development
  - Fleet management and logistics
  - Automotive infotainment systems
  - Delivery route optimization
  - Location-based services
  - Traffic monitoring dashboards
  - EV trip planning
  - Smart city applications
solutions:
  - Automotive navigation
  - Enterprise logistics
  - Mobile mapping
  - Location intelligence
integrations:
  - MCP Server for AI agents
  - Android SDK
  - iOS SDK
  - ADAS SDK
common:
  - type: Website
    url: https://www.tomtom.com/
  - type: Developer Portal
    url: https://developer.tomtom.com/
  - type: Documentation
    url: https://developer.tomtom.com/
  - type: Sign Up
    url: https://developer.tomtom.com/
  - type: API Explorer
    url: https://developer.tomtom.com/api-explorer-index/documentation/product-information/introduction
  - type: MCP Server
    url: https://developer.tomtom.com/tomtom-mcp-server
  - type: Blog
    url: https://developer.tomtom.com/blog
  - type: GitHub Organization
    url: https://github.com/tomtom-international
  - type: Pricing
    url: https://developer.tomtom.com/pricing
  - type: Terms of Service
    url: https://developer.tomtom.com/terms-and-conditions
  - type: Features
    data:
      - 'Freemium: 50K tile + 2.5K non-tile requests/day across all APIs'
      - 'Pay-as-you-grow: $0.08/1,000 tile requests above free'
      - 'Enterprise: custom annual contract'
      - Maps Display API (vector + raster tiles)
      - Search API (geocoding, reverse geocoding, fuzzy search)
      - Routing API (driving, traffic-aware, EV routing)
      - Traffic API (real-time + historical)
      - Geofencing API
      - Map Matching API
      - Snap to Roads
      - Default 5 req/sec/key (can be raised)
      - API key authentication
      - TomTom Genesis Maps for automotive (Enterprise)
      - AutoStream for vehicle streaming maps (Enterprise)
      - Move Connected Services for fleet (Enterprise)
      - Global map coverage with frequent updates
    sources:
      - https://developer.tomtom.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
