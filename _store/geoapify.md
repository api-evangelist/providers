---
aid: geoapify
name: Geoapify
description: Geoapify Location Platform APIs for location-based services and mapping solutions.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-01-01'
modified: '2026-05-04'
position: Consumer
url: https://raw.githubusercontent.com/api-evangelist/geoapify/refs/heads/main/apis.yml
specificationVersion: '0.19'
tags:
  - Geocoding
  - Geospatial
  - Location
  - Maps
apis:
  - aid: geoapify:map-tiles
    name: Map Tiles API
    description: Retrieve map tiles for various types and styles.
    humanURL: https://apidocs.geoapify.com/maps/map-tiles
    baseURL: https://maps.geoapify.com/maptiles
    tags:
      - Maps
    properties:
      - type: Documentation
        url: https://apidocs.geoapify.com/maps/map-tiles
  - aid: geoapify:static-maps
    name: Static Maps API
    description: Generate static map images for embedding in applications.
    humanURL: https://apidocs.geoapify.com/maps/static-maps-api
    baseURL: https://maps.geoapify.com/staticmap
    tags:
      - Maps
    properties:
      - type: Documentation
        url: https://apidocs.geoapify.com/maps/static-maps-api
  - aid: geoapify:forward-geocoding
    name: Forward Geocoding API
    description: Convert addresses into geographic coordinates.
    humanURL: https://apidocs.geoapify.com/addresses-location/forward-geocoding-api
    baseURL: https://api.geoapify.com/geocode/search
    tags:
      - Geocoding
    properties:
      - type: Documentation
        url: https://apidocs.geoapify.com/addresses-location/forward-geocoding-api
      - type: OpenAPI
        url: openapi/geoapify-forward-geocoding-api-openapi.yml
  - aid: geoapify:reverse-geocoding
    name: Reverse Geocoding API
    description: Convert geographic coordinates into addresses.
    humanURL: https://apidocs.geoapify.com/addresses-location/reverse-geocoding-api
    baseURL: https://api.geoapify.com/geocode/reverse
    tags:
      - Geocoding
    properties:
      - type: Documentation
        url: https://apidocs.geoapify.com/addresses-location/reverse-geocoding-api
  - aid: geoapify:address-autocomplete
    name: Address Autocomplete API
    description: Address autocomplete suggestions for search fields.
    humanURL: https://apidocs.geoapify.com/addresses-location/address-autocomplete
    baseURL: https://api.geoapify.com/geocode/autocomplete
    tags:
      - Geocoding
    properties:
      - type: Documentation
        url: https://apidocs.geoapify.com/addresses-location/address-autocomplete
  - aid: geoapify:ip-geolocation
    name: IP Geolocation API
    description: Identify the location of an IP address.
    humanURL: https://apidocs.geoapify.com/addresses-location/ip-geolocation-api
    baseURL: https://api.geoapify.com/geocode/ip
    tags:
      - Geolocation
    properties:
      - type: Documentation
        url: https://apidocs.geoapify.com/addresses-location/ip-geolocation-api
  - aid: geoapify:routing
    name: Routing API
    description: Provides routing directions between multiple points.
    humanURL: https://apidocs.geoapify.com/routes-optimization/routing-api
    baseURL: https://api.geoapify.com/routing
    tags:
      - Routing
    properties:
      - type: Documentation
        url: https://apidocs.geoapify.com/routes-optimization/routing-api
  - aid: geoapify:places
    name: Places API
    description: Discover places based on various categories and parameters.
    humanURL: https://apidocs.geoapify.com/places-details/places-api
    baseURL: https://api.geoapify.com/places
    tags:
      - Places
    properties:
      - type: Documentation
        url: https://apidocs.geoapify.com/places-details/places-api
  - aid: geoapify:boundaries
    name: Boundaries API
    description: Retrieve boundary data for administrative regions.
    humanURL: https://apidocs.geoapify.com/boundaries/about-boundaries-api
    baseURL: https://api.geoapify.com/boundaries
    tags:
      - Boundaries
    properties:
      - type: Documentation
        url: https://apidocs.geoapify.com/boundaries/about-boundaries-api
  - aid: geoapify:isoline
    name: Isoline API
    description: Generate isolines to represent reachable areas.
    humanURL: https://apidocs.geoapify.com/reachability/isolines
    baseURL: https://api.geoapify.com/isolines
    tags:
      - Reachability
    properties:
      - type: Documentation
        url: https://apidocs.geoapify.com/reachability/isolines
common:
  - type: Website
    url: https://www.geoapify.com/
  - type: Documentation
    url: https://apidocs.geoapify.com/
  - type: Sign Up
    url: https://myprojects.geoapify.com/register
  - type: Terms of Service
    url: https://www.geoapify.com/terms
  - type: Privacy Policy
    url: https://www.geoapify.com/privacy
  - type: Features
    data:
      - 'Free: 3K credits/day, 5 RPS, limited commercial use'
      - 'API 10: $59/mo, 10K credits/day, 12 RPS'
      - 'API 25: $109/mo, 25K credits/day, 15 RPS'
      - 'API 50: $179/mo, 50K credits/day, 20 RPS'
      - 'API 100: $299/mo, 100K credits/day, 25 RPS'
      - 'API 250: $609/mo, 250K credits/day, 30 RPS'
      - 'Custom from $860/mo: unmetered, dedicated endpoint'
      - Geocoding API (forward + reverse)
      - Routing API (driving, walking, cycling, truck)
      - Isochrones up to 15-120 min by tier
      - Place Details API
      - Map Tiles API
      - Address Autocomplete
      - Static Maps API
      - Boundaries API
      - OpenStreetMap-based data with global coverage
    sources:
      - https://www.geoapify.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
