---
aid: google-fitness
url: https://raw.githubusercontent.com/api-evangelist/google-fitness/refs/heads/main/apis.yml
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
name: Google Fit REST
tags:
- Activity Tracking
- Fitness
- Google
- Health
- Sessions
- Wearables
- Wellness
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Google Fit REST API enables you to store and access health and wellness data in the fitness store from apps on any platform. You can manage data sources, datasets, sessions, and aggregate fitness data for activities like steps, heart rate, sleep, and workouts.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

