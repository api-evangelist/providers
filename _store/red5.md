---
aid: red5
url: https://raw.githubusercontent.com/api-evangelist/red5/refs/heads/main/apis.yml
apis:
- aid: red5:server-api
  name: Red5 Pro Server API
  tags:
  - Media
  - Real-Time
  - REST
  - Streaming
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: http://localhost:5080/api/v1
  humanURL: https://www.red5.net/docs/red5-pro/development/api/server/red5-pro-server-api-overview/
  properties:
  - url: https://www.red5.net/docs/red5-pro/development/api/server/red5-pro-server-api-overview/
    type: Documentation
  - url: https://www.red5.net/docs/red5-pro/development/api/server/red5-pro-server-api/
    type: APIReference
  - url: https://www.red5.net/docs/red5-pro/development/api/server/red5-pro-server-applications-api/
    type: APIReference
  - url: https://www.red5.net/docs/red5-pro/development/api/server/red5-pro-server-streams-api/
    type: APIReference
  - url: openapi/red5-server-api-openapi.yml
    type: OpenAPI
  description: The Red5 Pro Server API is an HTTP-based REST API for gathering server, application, client, and stream statistics from a running Red5 Pro instance. It exposes endpoints for server health checks, application scope statistics, active stream enumeration and control, and log access. The API uses token-based authentication and is accessible at port 5080 on any Red5 Pro server deployment. Developers can use it to monitor and manage live streaming infrastructure programmatically.
- aid: red5:stream-manager-2-api
  name: Red5 Pro Stream Manager 2.0 API
  tags:
  - Autoscaling
  - Media
  - REST
  - Streaming
  - WebRTC
  - WHEP
  - WHIP
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://streammanager.example.com/as/v1
  humanURL: https://www.red5.net/docs/red5-pro/development/api/stream-manager-2-0/
  properties:
  - url: https://www.red5.net/docs/red5-pro/development/api/stream-manager-2-0/
    type: Documentation
  - url: https://www.red5.net/docs/red5-pro/development/api/stream-manager-2-0/stream-manager-2-openapi-api/
    type: OpenAPI
  - url: https://www.red5.net/docs/red5-pro/development/api/stream-manager-2-0/stream-manager-2-streams-api/
    type: APIReference
  - url: https://www.red5.net/docs/red5-pro/development/api/stream-manager-2-0/stream-manager-2-admin-api/
    type: APIReference
  - url: https://www.red5.net/docs/red5-pro/development/api/stream-manager-2-0/stream-manager-2-proxy-api/
    type: APIReference
  - url: openapi/red5-stream-manager-2-openapi.yml
    type: OpenAPI
  description: The Red5 Pro Stream Manager 2.0 API orchestrates autoscaling clusters of Red5 Pro streaming nodes across cloud infrastructure. It provides REST endpoints for managing live stream publishing and playback sessions, provisioning stream configurations, monitoring node metrics, and proxying WHIP and WHEP WebRTC connections. The API supports dynamic scaling of streaming capacity and is documented with an interactive Swagger UI available on each Stream Manager deployment.
- aid: red5:brew-mixer-api
  name: Red5 Pro Brew Mixer API
  tags:
  - Audio
  - Media
  - Mixing
  - REST
  - Streaming
  - Video
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com/brewmixer/2.0
  humanURL: https://www.red5.net/docs/red5-pro/development/api/mixer/brew-mixer-api/
  properties:
  - url: https://www.red5.net/docs/red5-pro/development/api/mixer/brew-mixer-api/
    type: Documentation
  - url: openapi/red5-brew-mixer-api-openapi.yml
    type: OpenAPI
  description: The Red5 Pro Brew Mixer API is a REST interface for the Cauldron Media Engine that enables dynamic composition of multiple live video and audio streams into a single mixed output stream. It supports creating and managing mixers, controlling input sources and layout, and producing composite streams suitable for broadcasting.
- aid: red5:restreamer-api
  name: Red5 Pro Restreamer API
  tags:
  - Media
  - REST
  - Restreaming
  - RTMP
  - Streaming
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://www.red5.net/docs/red5-pro/development/api/restreamer/
  properties:
  - url: https://www.red5.net/docs/red5-pro/development/api/restreamer/
    type: Documentation
  - url: https://www.red5.net/docs/red5-pro/development/api/restreamer/red5-pro-restreamer-api-rtmp/
    type: APIReference
  - url: openapi/red5-restreamer-api-openapi.yml
    type: OpenAPI
  description: The Red5 Pro Restreamer API controls live stream retransmission to external RTMP, RTMPS, SRT, and Zixi destinations including social media platforms like Facebook and YouTube. It accepts JSON-based provisions via POST requests to configure push and pull restreaming sessions from a Red5 Pro server. The API supports file-based pseudo-live restreaming of FLV and MP4 files, as well as real-time forwarding of live ingest streams.
- aid: red5:webrtc-sdk
  name: Red5 Pro WebRTC SDK
  tags:
  - JavaScript
  - Media
  - SDK
  - Streaming
  - WebRTC
  - WHEP
  - WHIP
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://www.red5.net/docs/red5-pro/development/sdks/red5-webrtc-sdk/
  properties:
  - url: https://www.red5.net/docs/red5-pro/development/sdks/red5-webrtc-sdk/
    type: Documentation
  - url: https://www.red5.net/docs/red5-pro/development/sdks/red5-webrtc-sdk/red5-webrtc-sdk-api-documentation/
    type: APIReference
  - url: https://github.com/red5pro/red5pro-webrtc-sdk
    type: GitHub
  - url: https://www.npmjs.com/package/red5pro-webrtc-sdk
    type: NPM
  - url: asyncapi/red5-webrtc-streaming-asyncapi.yml
    type: AsyncAPI
  description: The Red5 Pro WebRTC SDK is a JavaScript library for integrating low-latency live streaming publish and subscribe capabilities into web applications. It supports WHIP for WebRTC publishing and WHEP for WebRTC playback, enabling sub-second latency streaming directly in the browser without plugins. The SDK provides APIs for managing stream sessions, configuring media constraints, handling connection lifecycle events, and interacting with Stream Manager for scalable deployments.
- aid: red5:core-sdk
  name: Red5 Core SDK
  tags:
  - Desktop
  - Linux
  - Media
  - Native
  - SDK
  - Streaming
  - Windows
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://www.red5.net/docs/red5-pro/development/sdks/red5-core-sdk/
  properties:
  - url: https://www.red5.net/docs/red5-pro/development/sdks/red5-core-sdk/
    type: Documentation
  - url: https://www.red5.net/live-streaming-sdks/
    type: SDKs
  description: The Red5 Core SDK is a native client library that provides APIs for building real-time streaming applications on Linux, Windows, and macOS desktop platforms. It offers interfaces for server connection management, media capture and processing, audio and video source configuration, renderer control, and integration with Stream Manager for autoscaled deployments.
name: Red5
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Red5 is an open-source media server that delivers live and on-demand streaming video, audio, and data to web and mobile applications using RTMP, RTSP, HLS, and WebRTC protocols.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

