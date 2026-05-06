---
aid: streamyard
name: StreamYard
description: StreamYard is a professional live streaming and recording studio in the browser. Stream directly to multiple platforms simultaneously including YouTube, Facebook, LinkedIn, Twitch, and Twitter/X. Interview remote guests, share screens, display overlays, and manage brand assets. The StreamYard API enables programmatic management of broadcasts, destinations, and recordings.
url: https://raw.githubusercontent.com/api-evangelist/streamyard/refs/heads/main/apis.yml
image: https://streamyard.com/assets/images/logo.png
tags:
  - Broadcasting
  - Live Streaming
  - Multi-Streaming
  - Recordings
  - Video
type: Index
access: 3rd-Party
position: Consumer
created: '2024-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: streamyard:streamyard-api
    name: StreamYard API
    description: The StreamYard API provides programmatic access to manage live broadcasts and recordings. Create and manage broadcasts, add streaming destinations (YouTube, Facebook, LinkedIn, Twitch, Twitter/X, custom RTMP), access recordings, and manage connected destination accounts. Authentication uses OAuth 2.0 with scope-based access control.
    humanURL: https://developers.streamyard.com/docs
    baseURL: https://api.streamyard.com
    tags:
      - Broadcasting
      - Live Streaming
      - Multi-Streaming
      - Recordings
      - Video
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/streamyard/refs/heads/main/openapi/streamyard-openapi.yml
      - type: Documentation
        url: https://developers.streamyard.com/docs
      - type: Authentication
        url: https://developers.streamyard.com/docs/authentication
      - type: OpenAPI
        url: https://api.streamyard.com/openapi.json
common:
  - type: Website
    url: https://streamyard.com
  - type: Developer Portal
    url: https://developers.streamyard.com
  - type: Documentation
    url: https://developers.streamyard.com/docs
  - type: Dashboard
    url: https://streamyard.com/dashboard
  - type: Sign Up
    url: https://streamyard.com/signup
  - type: Login
    url: https://streamyard.com/login
  - type: Pricing
    url: https://streamyard.com/pricing
  - type: Blog
    url: https://streamyard.com/blog
  - type: Terms of Service
    url: https://streamyard.com/resources/terms
  - type: Privacy Policy
    url: https://streamyard.com/resources/privacy
  - type: Status
    url: https://status.streamyard.com
  - type: Support
    url: https://streamyard.com/resources/support
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/streamyard/refs/heads/main/openapi/streamyard-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/streamyard/refs/heads/main/json-schema/streamyard-broadcast-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/streamyard/refs/heads/main/json-ld/streamyard-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
