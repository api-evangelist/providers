---
aid: pulsoid
name: Pulsoid
description: Pulsoid enables real-time heart rate data transmission from peripherals (BLE heart rate monitors, smartwatches, etc.) to clients. The Pulsoid API allows reading and writing real-time heart rate data, accessing statistics, and managing widgets and profile.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Heart Rate
  - Health
  - Wearables
  - Real-Time
  - Streaming
  - WebSocket
  - OAuth2
created: '2025-02-17'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/pulsoid/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: pulsoid:pulsoid
    name: Pulsoid
    description: Pulsoid enables real-time heart rate data transmission from peripherals (BLE heart rate monitors, smartwatches, etc.) to clients. The REST API provides endpoints to validate tokens, read latest heart rate, submit heart rate data, retrieve statistics, manage widgets, and access user profile. Real-time streaming is delivered via WebSocket endpoints.
    humanURL: https://docs.pulsoid.net/
    baseURL: https://dev.pulsoid.net
    tags:
      - Heart Rate
      - Wearables
      - Real-Time
      - Streaming
    properties:
      - type: Documentation
        url: https://docs.pulsoid.net/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/pulsoid/refs/heads/main/openapi/pulsoid-openapi.yml
common:
  - type: Website
    url: https://pulsoid.net/
  - type: Documentation
    url: https://docs.pulsoid.net/
  - type: Sign Up
    url: https://pulsoid.net/auth/sign_up
  - type: Login
    url: https://pulsoid.net/auth/sign_in
  - type: Authentication
    url: https://docs.pulsoid.net/access-token-and-authentication/about-access-token
  - type: OAuth
    url: https://docs.pulsoid.net/access-token-and-authentication/oauth-authorization-code-grant
  - type: GitHub Organization
    url: https://github.com/Pulsoid
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
