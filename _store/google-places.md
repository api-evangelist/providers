---
name: Google Places
description: The Google Places API is a service that accepts HTTP requests for location data through a variety of methods. It returns formatted location data and imagery about establishments, geographic locations, or prominent points of interest. Supports nearby search, text search, place details, place photos, and autocomplete.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-places/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - Geolocation
  - Google
  - Locations
  - Maps
  - Places
  - Points of Interest
apis:
  - name: Google Places API
    description: The Places API (New) provides programmatic access to Google's database of places, including establishments, geographic locations, and points of interest. It supports nearby search, text search, place details, photos, and autocomplete predictions.
    humanURL: https://developers.google.com/maps/documentation/places/web-service
    baseURL: https://places.googleapis.com/v1
    properties:
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: JSONSchema
        url: json-schema/Place.json
    tags:
      - Locations
      - Maps
      - Places
      - Search
common:
  - type: GettingStarted
    url: https://developers.google.com/maps/documentation/places/web-service/overview
  - type: Pricing
    url: https://developers.google.com/maps/billing-and-pricing/pricing
  - type: JSON-LD
    url: json-ld/context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
