---
aid: mapquest
name: MapQuest
description: MapQuest provides mapping, geocoding, routing, and traffic data APIs for developers to build location-aware applications. The developer portal offers free API keys and documentation for directions, static maps, geocoding, and traffic incident services.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Geocoding
  - Mapping
  - Maps
  - Navigation
  - Routing
  - Traffic
url: https://raw.githubusercontent.com/api-evangelist/mapquest/refs/heads/main/apis.yml
created: '2025-01-07'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: mapquest:mapquest-directions-api
    name: MapQuest Directions API
    description: The MapQuest Directions API provides routing capabilities with turn-by-turn directions, alternate routes, optimized routes, and travel time estimates using real-time traffic data.
    humanURL: https://developer.mapquest.com/documentation/directions-api/
    baseURL: https://www.mapquestapi.com/directions/v2
    tags:
      - Directions
      - Navigation
      - Routing
    properties:
      - type: Documentation
        url: https://developer.mapquest.com/documentation/directions-api/
  - aid: mapquest:mapquest-geocoding-api
    name: MapQuest Geocoding API
    description: The MapQuest Geocoding API converts addresses into geographic coordinates and vice versa, supporting both single and batch geocoding requests.
    humanURL: https://developer.mapquest.com/documentation/geocoding-api/
    baseURL: https://www.mapquestapi.com/geocoding/v1
    tags:
      - Geocoding
      - Location
    properties:
      - type: Documentation
        url: https://developer.mapquest.com/documentation/geocoding-api/
  - aid: mapquest:mapquest-static-map-api
    name: MapQuest Static Map API
    description: The MapQuest Static Map API returns a map image based on specified parameters including center, zoom, size, and map type.
    humanURL: https://developer.mapquest.com/documentation/static-map-api/v5/
    baseURL: https://www.mapquestapi.com/staticmap/v5
    tags:
      - Maps
      - Static Maps
    properties:
      - type: Documentation
        url: https://developer.mapquest.com/documentation/static-map-api/v5/
  - aid: mapquest:mapquest-traffic-api
    name: MapQuest Traffic API
    description: The MapQuest Traffic API returns traffic incidents for a specified bounding box in JSON or XML formats, including road construction and collisions.
    humanURL: https://developer.mapquest.com/documentation/traffic-api/
    baseURL: https://www.mapquestapi.com/traffic/v2
    tags:
      - Incidents
      - Traffic
    properties:
      - type: Documentation
        url: https://developer.mapquest.com/documentation/traffic-api/
      - type: Reference
        url: https://developer.mapquest.com/documentation/api/traffic/incidents/get.html
  - aid: mapquest:mapquest-search-api
    name: MapQuest Search API
    description: The MapQuest Search API supports radius, rectangle, polygon, and corridor searches against MapQuest hosted data tables, returning matching points of interest with attributes.
    humanURL: https://developer.mapquest.com/documentation/searchapi/
    baseURL: https://www.mapquestapi.com/search/v2
    tags:
      - Points of Interest
      - Search
    properties:
      - type: Documentation
        url: https://developer.mapquest.com/documentation/searchapi/
  - aid: mapquest:mapquest-place-search-api
    name: MapQuest Place Search API
    description: The MapQuest Place Search API returns places matching a search query, with support for category, location, and bounding-box filtering.
    humanURL: https://developer.mapquest.com/documentation/place-search-api/v5/
    baseURL: https://www.mapquestapi.com/search/v5
    tags:
      - Place Search
      - Points of Interest
      - Search
    properties:
      - type: Documentation
        url: https://developer.mapquest.com/documentation/place-search-api/v5/
  - aid: mapquest:mapquest-search-ahead-api
    name: MapQuest Search Ahead API
    description: The MapQuest Search Ahead API delivers prediction-based search suggestions as users type, supporting addresses, places, categories, and admin areas.
    humanURL: https://developer.mapquest.com/documentation/searchahead-api/v5/
    baseURL: https://www.mapquestapi.com/search/v5
    tags:
      - Autocomplete
      - Search
      - Search Ahead
    properties:
      - type: Documentation
        url: https://developer.mapquest.com/documentation/searchahead-api/v5/
  - aid: mapquest:mapquest-geolocation-api
    name: MapQuest Geolocation API
    description: The MapQuest Geolocation API returns the approximate location of a device based on cell tower and Wi-Fi access point information.
    humanURL: https://developer.mapquest.com/documentation/geolocation-api/
    baseURL: https://www.mapquestapi.com/geolocation/v1
    tags:
      - Geolocation
      - Location
    properties:
      - type: Documentation
        url: https://developer.mapquest.com/documentation/geolocation-api/
  - aid: mapquest:mapquest-icons-api
    name: MapQuest Icons API
    description: The MapQuest Icons API serves customizable map marker icons for use with MapQuest static and interactive maps.
    humanURL: https://developer.mapquest.com/documentation/icons-api/
    baseURL: https://www.mapquestapi.com/icons/v2
    tags:
      - Icons
      - Maps
    properties:
      - type: Documentation
        url: https://developer.mapquest.com/documentation/icons-api/
  - aid: mapquest:mapquest-data-manager-api
    name: MapQuest Data Manager API
    description: The MapQuest Data Manager API allows developers to upload, manage, and query custom hosted data tables for use with MapQuest search and mapping services.
    humanURL: https://developer.mapquest.com/documentation/data-manager-api/v2/
    baseURL: https://www.mapquestapi.com/datamanager/v2
    tags:
      - Custom Data
      - Data Management
    properties:
      - type: Documentation
        url: https://developer.mapquest.com/documentation/data-manager-api/v2/
common:
  - type: Portal
    url: https://developer.mapquest.com/
  - type: Getting Started
    url: https://developer.mapquest.com/documentation/
  - type: Sign Up
    url: https://developer.mapquest.com/plan_purchase/steps/business_edition/business_edition_free/register
  - type: Login
    url: https://developer.mapquest.com/user/login
  - type: Support
    url: https://developer.mapquest.com/support/
  - type: Terms of Service
    url: https://hello.mapquest.com/terms-of-use
  - type: Privacy Policy
    url: https://hello.mapquest.com/privacy-policy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
