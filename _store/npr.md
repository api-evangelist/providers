---
aid: npr
name: NPR
description: National Public Radio (NPR) APIs. The APIs support station finding, authentication, user management, and listening with audio recommendations tailored to a user's preferences.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Media
  - News
  - Radio
url: https://raw.githubusercontent.com/api-evangelist/npr/refs/heads/main/apis.yml
created: '2024-04-14'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: npr:listening
    name: NPR Listening
    description: Audio recommendations tailored to a user's preferences.
    humanURL: https://dev.npr.org/guide/services/listening
    baseURL: https://listening.api.npr.org/
    tags:
      - Audio
      - Listening
    properties:
      - type: Documentation
        url: https://dev.npr.org/guide/services/listening
      - type: Swagger
        url: https://listening.api.npr.org/v2/swagger.json
  - aid: npr:station-finder
    name: NPR Station Finder
    description: NPR member station information lookup.
    humanURL: https://dev.npr.org/guide/services/station-finder
    baseURL: https://station.api.npr.org/
    tags:
      - Stations
    properties:
      - type: Documentation
        url: https://dev.npr.org/guide/services/station-finder
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/npr/main/openapi/npr-station-finder-openapi-original.yml
  - aid: npr:identity
    name: NPR Identity
    description: User management API and entry point to user-specific information.
    humanURL: https://dev.npr.org/guide/services/identity
    baseURL: https://identity.api.npr.org/
    tags:
      - Identity
      - Users
    properties:
      - type: Documentation
        url: https://dev.npr.org/guide/services/identity
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/npr/main/openapi/npr-identity-openapi-original.yml
  - aid: npr:authorization
    name: NPR Authorization
    description: API authorization service.
    humanURL: https://dev.npr.org/guide/services/authorization
    baseURL: https://authorization.api.npr.org/
    tags:
      - Authorization
    properties:
      - type: Documentation
        url: https://dev.npr.org/guide/services/authorization
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/npr/main/openapi/npr-authorization-openapi-original.yml
common:
  - type: Website
    url: https://www.npr.org/
  - type: Documentation
    url: https://dev.npr.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
