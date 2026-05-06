---
aid: red5
name: Red5
description: Red5 provides real-time streaming infrastructure for live video and audio delivery at scale. The Red5 Pro platform includes a media server, Stream Manager 2.0 for autoscaling cloud deployments, the Brew Mixer for composite stream production, a Restreamer for pushing live streams to social media and RTMP destinations, and WebRTC and native SDKs for browser and mobile integration. Red5 APIs enable programmatic management of streams, mixers, restreaming, cluster orchestration, and node monitoring. Use cases include live events, sports broadcasting, interactive video, gaming, surveillance, and enterprise communications requiring ultra-low latency streaming.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Live Streaming
  - Media
  - Real-Time
  - RTMP
  - Streaming
  - Video
  - WebRTC
url: https://raw.githubusercontent.com/api-evangelist/red5/refs/heads/main/apis.yml
created: '2026-03-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: red5:server-api
    name: Red5 Pro Server API
    description: The Red5 Pro Server API is an HTTP-based REST API for gathering server, application, client, and stream statistics from a running Red5 Pro instance. It exposes endpoints for server health checks, application scope statistics, active stream enumeration and control, connection management, and log access. The API uses token-based authentication via the accessToken parameter and is accessible at port 5080 on any Red5 Pro server deployment. Developers can use it to monitor and manage live streaming infrastructure programmatically.
    humanURL: https://www.red5.net/docs/red5-pro/development/api/server/red5-pro-server-api-overview/
    baseURL: http://localhost:5080/api/v1
    tags:
      - Media
      - Real-Time
      - REST
      - Server Management
      - Streaming
    properties:
      - type: Documentation
        url: https://www.red5.net/docs/red5-pro/development/api/server/red5-pro-server-api-overview/
      - type: APIReference
        url: https://www.red5.net/docs/red5-pro/development/api/server/red5-pro-server-api/
      - type: APIReference
        url: https://www.red5.net/docs/red5-pro/development/api/server/red5-pro-server-applications-api/
      - type: APIReference
        url: https://www.red5.net/docs/red5-pro/development/api/server/red5-pro-server-streams-api/
      - type: OpenAPI
        url: openapi/red5-server-api-openapi.yml
  - aid: red5:stream-manager-2-api
    name: Red5 Pro Stream Manager 2.0 API
    description: The Red5 Pro Stream Manager 2.0 API orchestrates autoscaling clusters of Red5 Pro streaming nodes across cloud infrastructure. It provides REST endpoints for managing live stream publishing and playback sessions, provisioning stream configurations, monitoring node metrics, managing cluster node lifecycles, and proxying WHIP and WHEP WebRTC connections. The API supports dynamic scaling of streaming capacity and is documented with an interactive Swagger UI available on each Stream Manager deployment.
    humanURL: https://www.red5.net/docs/red5-pro/development/api/stream-manager-2-0/
    baseURL: https://streammanager.example.com/as/v1
    tags:
      - Autoscaling
      - Cluster Management
      - Media
      - REST
      - Streaming
      - WebRTC
      - WHEP
      - WHIP
    properties:
      - type: Documentation
        url: https://www.red5.net/docs/red5-pro/development/api/stream-manager-2-0/
      - type: APIReference
        url: https://www.red5.net/docs/red5-pro/development/api/stream-manager-2-0/stream-manager-2-streams-api/
      - type: APIReference
        url: https://www.red5.net/docs/red5-pro/development/api/stream-manager-2-0/stream-manager-2-admin-api/
      - type: APIReference
        url: https://www.red5.net/docs/red5-pro/development/api/stream-manager-2-0/stream-manager-2-proxy-api/
      - type: OpenAPI
        url: openapi/red5-stream-manager-2-openapi.yml
  - aid: red5:brew-mixer-api
    name: Red5 Pro Brew Mixer API
    description: The Red5 Pro Brew Mixer API is a REST interface for the Cauldron Media Engine that enables dynamic composition of multiple live video and audio streams into a single mixed output stream. It supports creating and managing mixers, controlling input sources and layout, configuring composite output parameters, and producing mixed streams suitable for broadcasting. The Brew Mixer is used for multi-presenter live events and production-quality stream composition.
    humanURL: https://www.red5.net/docs/red5-pro/development/api/mixer/brew-mixer-api/
    baseURL: https://api.example.com/brewmixer/2.0
    tags:
      - Audio
      - Composition
      - Media
      - Mixing
      - REST
      - Streaming
      - Video
    properties:
      - type: Documentation
        url: https://www.red5.net/docs/red5-pro/development/api/mixer/brew-mixer-api/
      - type: OpenAPI
        url: openapi/red5-brew-mixer-api-openapi.yml
  - aid: red5:restreamer-api
    name: Red5 Pro Restreamer API
    description: The Red5 Pro Restreamer API controls live stream retransmission to external RTMP, RTMPS, SRT, and Zixi destinations including social media platforms like Facebook, YouTube, and Twitch. It accepts JSON-based provisions via POST requests to configure push and pull restreaming sessions from a Red5 Pro server. The API supports file-based pseudo-live restreaming of FLV and MP4 files as well as real-time forwarding of live ingest streams.
    humanURL: https://www.red5.net/docs/red5-pro/development/api/restreamer/
    baseURL: https://api.example.com
    tags:
      - Media
      - REST
      - Restreaming
      - RTMP
      - Social Media
      - Streaming
    properties:
      - type: Documentation
        url: https://www.red5.net/docs/red5-pro/development/api/restreamer/
      - type: APIReference
        url: https://www.red5.net/docs/red5-pro/development/api/restreamer/red5-pro-restreamer-api-rtmp/
      - type: OpenAPI
        url: openapi/red5-restreamer-api-openapi.yml
  - aid: red5:webrtc-sdk
    name: Red5 Pro WebRTC SDK
    description: The Red5 Pro WebRTC SDK is a JavaScript library for integrating low-latency live streaming publish and subscribe capabilities into web applications. It supports WHIP for WebRTC publishing and WHEP for WebRTC playback, enabling sub-second latency streaming directly in the browser without plugins. The SDK provides APIs for managing stream sessions, configuring media constraints, handling connection lifecycle events, and interacting with Stream Manager for scalable deployments.
    humanURL: https://www.red5.net/docs/red5-pro/development/sdks/red5-webrtc-sdk/
    baseURL: https://api.example.com
    tags:
      - JavaScript
      - Media
      - SDK
      - Streaming
      - WebRTC
      - WHEP
      - WHIP
    properties:
      - type: Documentation
        url: https://www.red5.net/docs/red5-pro/development/sdks/red5-webrtc-sdk/
      - type: APIReference
        url: https://www.red5.net/docs/red5-pro/development/sdks/red5-webrtc-sdk/red5-webrtc-sdk-api-documentation/
      - type: GitHub
        url: https://github.com/red5pro/red5pro-webrtc-sdk
      - type: NPM
        url: https://www.npmjs.com/package/red5pro-webrtc-sdk
      - type: AsyncAPI
        url: asyncapi/red5-webrtc-streaming-asyncapi.yml
  - aid: red5:core-sdk
    name: Red5 Core SDK
    description: The Red5 Core SDK is a native client library for building real-time streaming applications on Linux, Windows, and macOS desktop platforms. It offers interfaces for server connection management, media capture and processing, audio and video source configuration, renderer control, and integration with Stream Manager for autoscaled deployments. Bindings are available for C++, Python, and other native environments.
    humanURL: https://www.red5.net/docs/red5-pro/development/sdks/red5-core-sdk/
    baseURL: https://api.example.com
    tags:
      - Desktop
      - Linux
      - Media
      - Native
      - SDK
      - Streaming
      - Windows
    properties:
      - type: Documentation
        url: https://www.red5.net/docs/red5-pro/development/sdks/red5-core-sdk/
      - type: SDKs
        url: https://www.red5.net/live-streaming-sdks/
  - aid: red5:ios-sdk
    name: Red5 Pro iOS Streaming SDK
    description: The Red5 Pro iOS Streaming SDK is a native iOS library for integrating real-time live streaming publish and subscribe capabilities into iOS applications. It supports H.264 video and AAC/Opus audio encoding, WebRTC-based streaming with WHIP/WHEP, and integration with Stream Manager for cluster-aware streaming deployments. Example code and testbeds are available on GitHub.
    humanURL: https://www.red5.net/docs/red5-pro/development/sdks/
    baseURL: https://api.example.com
    tags:
      - iOS
      - Media
      - Mobile
      - SDK
      - Streaming
      - Swift
    properties:
      - type: Documentation
        url: https://www.red5.net/docs/red5-pro/development/sdks/
      - type: GitHub
        url: https://github.com/red5pro/streaming-ios
  - aid: red5:android-sdk
    name: Red5 Pro Android Streaming SDK
    description: The Red5 Pro Android Streaming SDK is a native Android library for integrating real-time live streaming publish and subscribe capabilities into Android applications. It supports H.264/H.265 video encoding, AAC audio, WebRTC-based streaming, and adaptive bitrate control. SDK examples and testbeds are available on GitHub for common streaming use cases.
    humanURL: https://www.red5.net/docs/red5-pro/development/sdks/
    baseURL: https://api.example.com
    tags:
      - Android
      - Java
      - Media
      - Mobile
      - SDK
      - Streaming
    properties:
      - type: Documentation
        url: https://www.red5.net/docs/red5-pro/development/sdks/
      - type: GitHub
        url: https://github.com/red5pro/streaming-android
common:
  - type: Website
    url: https://www.red5.net/
  - type: Documentation
    url: https://www.red5.net/docs/red5-pro/
  - type: GitHub Organization
    url: https://github.com/red5pro
  - type: GitHub Organization
    url: https://github.com/Red5
  - type: SDKs
    url: https://www.red5.net/live-streaming-sdks/
  - type: Pricing
    url: https://www.red5.net/pricing/
  - type: Blog
    url: https://www.red5.net/blog/
  - type: Contact
    url: https://www.red5.net/contact/
  - type: JSONLDContext
    url: json-ld/red5-context.jsonld
  - type: JSONSchema
    url: json-schema/red5-stream-schema.json
  - type: JSONSchema
    url: json-schema/red5-restream-provision-schema.json
  - type: OpenAPI
    url: openapi/red5-server-api-openapi.yml
  - type: OpenAPI
    url: openapi/red5-stream-manager-2-openapi.yml
  - type: OpenAPI
    url: openapi/red5-brew-mixer-api-openapi.yml
  - type: OpenAPI
    url: openapi/red5-restreamer-api-openapi.yml
  - type: AsyncAPI
    url: asyncapi/red5-webrtc-streaming-asyncapi.yml
  - type: JSONStructure
    url: json-structure/red5-stream-structure.json
  - type: SpectralRuleset
    url: rules/red5-rules.yml
  - type: NaftikoCapability
    url: capabilities/live-streaming.yaml
  - type: Vocabulary
    url: vocabulary/red5-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
