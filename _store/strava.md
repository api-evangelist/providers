---
aid: strava
name: Strava
description: 'Strava is a popular fitness tracking app and social network that allows athletes to track and analyze workouts including running, cycling, swimming, and 200+ other sport types. The Strava API enables developers to access athlete profiles, activities, segments, routes, clubs, gear, and time-series data streams. OAuth 2.0 is used for authentication with granular scope control. Rate limits apply: 100 requests per 15 minutes, 1000 per day.'
url: https://raw.githubusercontent.com/api-evangelist/strava/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cycling
  - Fitness
  - Fitness Tracking
  - Running
  - Sports
type: Index
access: 3rd-Party
position: Consumer
created: '2025-03-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: strava:strava
    name: Strava API
    description: The Strava API provides access to athlete profiles, activities (workouts), segments, routes, clubs, gear, and time-series data streams. Supports OAuth 2.0 with fine-grained scopes for reading activities, accessing private data, and writing updates. Rate limited to 100 requests/15 min and 1000 requests/day for default applications.
    humanURL: https://developers.strava.com/
    baseURL: https://www.strava.com/api/v3
    tags:
      - Cycling
      - Fitness
      - Fitness Tracking
      - Running
      - Sports
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/strava/refs/heads/main/openapi/strava-openapi.yml
      - type: Documentation
        url: https://developers.strava.com/docs/reference/
      - type: Authentication
        url: https://developers.strava.com/docs/authentication/
      - type: Getting Started
        url: https://developers.strava.com/docs/getting-started/
      - type: RateLimits
        url: https://developers.strava.com/docs/rate-limits/
      - type: Webhooks
        url: https://developers.strava.com/docs/webhooks/
common:
  - type: Website
    url: https://www.strava.com
  - type: Developer Portal
    url: https://developers.strava.com/
  - type: Documentation
    url: https://developers.strava.com/docs/
  - type: Authentication
    url: https://developers.strava.com/docs/authentication/
  - type: Terms of Service
    url: https://www.strava.com/legal/api
  - type: Privacy Policy
    url: https://www.strava.com/legal/privacy
  - type: Status
    url: https://status.strava.com
  - type: Blog
    url: https://blog.strava.com
  - type: Forum
    url: https://communityhub.strava.com/developers
  - type: Sign Up
    url: https://www.strava.com/register
  - type: Login
    url: https://www.strava.com/login
  - type: App Registration
    url: https://www.strava.com/settings/api
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/strava/refs/heads/main/openapi/strava-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/strava/refs/heads/main/json-schema/strava-activity-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/strava/refs/heads/main/json-ld/strava-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
