---
aid: restream
name: Restream
description: Restream is a multistreaming platform that enables content creators and businesses to simultaneously broadcast live video to 30+ platforms including YouTube, Twitch, Facebook, LinkedIn, and more. The platform offers REST APIs and WebSocket connections for managing streams, channels, events, and chat.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Broadcast
  - Chat
  - Content Delivery
  - Live Streaming
  - Multistreaming
  - Video Streaming
url: https://raw.githubusercontent.com/api-evangelist/restream/refs/heads/main/apis.yml
created: '2025-03-15'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: restream:restream-api
    name: Restream API
    description: REST API for managing Restream channels, stream keys, events, and user profiles. Uses OAuth2 authorization code flow for authentication with scopes for profile, channels, streams, events, and chat. Base URL is https://api.restream.io/v2.
    humanURL: https://developers.restream.io
    baseURL: https://api.restream.io/v2
    tags:
      - Channels
      - Events
      - Live Video
      - OAuth2
      - Streaming
      - Users
    properties:
      - type: Documentation
        url: https://developers.restream.io/docs
      - type: Authentication
        url: https://developers.restream.io/guide/getting-started
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/restream/refs/heads/main/openapi/restream-openapi.yml
  - aid: restream:restream-streaming-updates-api
    name: Restream Streaming Updates API
    description: WebSocket API for real-time streaming status updates. Connect to wss://streaming.api.restream.io/ws with an OAuth access token to receive incoming and outgoing stream events, platform status updates, and viewer counts in real time.
    humanURL: https://developers.restream.io/private-api/streaming-updates
    baseURL: wss://streaming.api.restream.io
    tags:
      - Real-Time
      - Streaming
      - WebSocket
    properties:
      - type: Documentation
        url: https://developers.restream.io/private-api/streaming-updates
  - aid: restream:restream-chat-api
    name: Restream Chat API
    description: WebSocket API for accessing and managing Restream Chat. Receive real-time chat messages from all connected streaming platforms (Twitch, YouTube, Facebook, Discord, LinkedIn, DLive) in a unified event stream. Supports reply and relay actions.
    humanURL: https://developers.restream.io/chat/getting-started
    baseURL: wss://chat.api.restream.io
    tags:
      - Chat
      - Real-Time
      - Streaming
      - WebSocket
    properties:
      - type: Documentation
        url: https://developers.restream.io/chat/getting-started
common:
  - type: TermsOfService
    url: https://restream.io/terms
  - type: PrivacyPolicy
    url: https://restream.io/privacy
  - type: SignUp
    url: https://app.restream.io/sign-up
  - type: Login
    url: https://app.restream.io/login
  - type: Blog
    url: https://restream.io/blog
  - type: Pricing
    url: https://restream.io/pricing
  - type: Website
    url: https://restream.io
  - type: Developer Portal
    url: https://developers.restream.io
  - type: Authentication
    url: https://developers.restream.io/guide/getting-started
  - type: GitHub Organization
    url: https://github.com/restreamio
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
