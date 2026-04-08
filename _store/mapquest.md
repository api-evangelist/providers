---
aid: mapquest
url: https://raw.githubusercontent.com/api-evangelist/mapquest/refs/heads/main/apis.yml
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
name: MapQuest
tags:
- Geocoding
- Mapping
- Maps
- Navigation
- Routing
- Traffic
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-07'
modified: '2026-04-07'
position: Consumer
description: MapQuest provides mapping, geocoding, routing, and traffic data APIs for developers to build location-aware applications. The developer portal offers free API keys and documentation for directions, static maps, geocoding, and traffic incident services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

