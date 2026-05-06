---
name: Google Fit REST
description: The Google Fit REST API enables you to store and access health and wellness data in the fitness store from apps on any platform. You can manage data sources, datasets, sessions, and aggregate fitness data for activities like steps, heart rate, sleep, and workouts.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-fitness/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - Activity Tracking
  - Fitness
  - Google
  - Health
  - Sessions
  - Wearables
  - Wellness
apis:
  - name: Google Fit REST API v1
    description: The Google Fit REST API provides access to fitness and health data stored in the Google Fit platform. Manage data sources, datasets, and sessions for activity tracking, body measurements, and location data.
    humanURL: https://developers.google.com/fit
    baseURL: https://www.googleapis.com/fitness/v1
    properties:
      - type: OpenAPI
        url: openapi/fitness.yml
      - type: JSONSchema
        url: json-schema/fitness.json
    overlays: []
common:
  - type: GettingStarted
    url: https://developers.google.com/fit/rest/v1/get-started
  - type: Pricing
    url: https://developers.google.com/fit/terms
  - type: JSON-LD
    url: json-ld/fitness.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
