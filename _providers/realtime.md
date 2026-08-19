---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.5
  scored_at: '2026-08-19'
api_count: 26
apis:
- description: A full-duplex communication protocol over a single TCP connection, standardized by the IETF as RFC 6455 and defined in the WHATWG WebSocket API on the client side. WebSocket is the most widely deploye
  name: WebSocket
  slug: websocket
- description: 'A unidirectional server-to-client streaming protocol over HTTP, defined by the WHATWG HTML Living Standard. SSE is simpler than WebSocket — it reuses HTTP and supports automatic reconnection — but is '
  name: Server-Sent Events (SSE)
  slug: server-sent-events
- description: A peer-to-peer realtime communication framework for audio, video, and arbitrary data channels, standardized by the W3C and IETF. WebRTC defines an SDP-based offer/answer signaling model, ICE/STUN/TURN
  name: WebRTC
  slug: webrtc
- description: 'A lightweight publish/subscribe protocol standardized by OASIS, designed for constrained devices and low-bandwidth networks. MQTT is the dominant realtime protocol in IoT, used by AWS IoT Core, Azure '
  name: MQTT
  slug: mqtt
- description: The Constrained Application Protocol, defined in IETF RFC 7252, is a RESTful protocol for constrained devices over UDP, with an Observe extension (RFC 7641) that provides realtime resource notificatio
  name: CoAP
  slug: coap
- description: gRPC supports four call patterns — unary, server streaming, client streaming, and bidirectional streaming — all carried over HTTP/2. gRPC streams are widely used for internal service-to-service realti
  name: gRPC Streaming
  slug: grpc-streaming
- description: A GraphQL operation type that delivers realtime updates to clients, typically carried over WebSocket using the graphql-ws or legacy graphql-transport-ws protocol, or over SSE using the GraphQL-SSE pro
  name: GraphQL Subscriptions
  slug: graphql-subscriptions
- description: A modern web API built on HTTP/3 and QUIC providing bidirectional and unidirectional streams plus unreliable datagrams to browsers. Designed as a higher-performance successor to WebSocket for streamin
  name: WebTransport
  slug: webtransport
- description: A hosted realtime platform offering Pub/Sub Channels, Chat, Spaces, LiveObjects, LiveSync, and AI Transport — built on a global edge network with low-latency multiprotocol fanout (WebSocket, MQTT, SSE
  name: Ably
  slug: ably
- description: A realtime platform offering Pub/Sub messaging, Presence detection, Chat SDKs, Functions (serverless), Events & Actions, Insights analytics, BizOps Workspace, Illuminate, and an Admin API. PubNub mark
  name: PubNub
  slug: pubnub
- description: A hosted realtime API from MessageBird offering two products — Channels (pub/sub messaging) and Beams (push notifications) — under the framing "Our hosted APIs are flexible, scalable, and easy to inte
  name: Pusher
  slug: pusher
- description: An open-source WebRTC platform marketed as "The platform for voice, video, and physical AI agents." LiveKit ships an SFU media server, Agents framework for production realtime AI, server SDKs in Go/No
  name: LiveKit
  slug: livekit
- description: A WebRTC video API provider offering Prebuilt embeddable video rooms, a Client SDK for custom apps, and Realtime Transport for AI Agents — the underlying infrastructure for Pipecat-deployed voice agen
  name: Daily
  slug: daily
- description: A realtime engagement platform offering Video Calling, Voice Calling, Signaling, Chat, and a Conversational AI Engine, framed as building "cutting-edge, voice-enabled applications by merging Agora's r
  name: Agora.io
  slug: agora
- description: Twilio's realtime video and live streaming products. Twilio Video provides WebRTC-based group rooms and peer rooms; Twilio Live (in select markets) layers low-latency interactive live streaming on top
  name: Twilio Video / Live
  slug: twilio-video
- description: A WebRTC video API (formerly TokBox / OpenTok) for embedding live video, audio, and screen sharing into web and mobile apps. Provides session/token-based access control, multiparty rooms, broadcasting
  name: Vonage Video API
  slug: vonage-video
- description: 'AWS''s low-latency interactive video service. IVS Real-Time Streaming offers WebRTC-based stages for multi-host interactivity; IVS Low-Latency Streaming offers HLS-based one-to-many delivery. IVS Chat '
  name: Amazon Interactive Video Service (IVS)
  slug: amazon-ivs
- description: Cloudflare's realtime media stack — RealtimeKit (SDKs and APIs for live video/voice), the Realtime SFU ("a powerful media server that efficiently routes video and audio"), and a managed TURN Service f
  name: Cloudflare Realtime
  slug: cloudflare-realtime
- description: 'A widely deployed open-source realtime engine for Node.js (with clients across JavaScript, Java, Swift, Kotlin, .NET, Python) that layers reconnection, rooms, namespaces, and binary support on top of '
  name: Socket.IO
  slug: socket-io
- description: The realtime layer of the Elixir Phoenix Framework — soft-realtime channels, presence, and pub/sub built on the BEAM VM. Channels carry WebSocket (or long-poll fallback) topics with broadcast/subscrib
  name: Phoenix Channels
  slug: phoenix-channels
- description: An open-source language-agnostic realtime messaging server providing WebSocket, SSE, HTTP streaming, and WebTransport transports with channel-based pub/sub, presence, history, and JWT-based access tok
  name: Centrifugo
  slug: centrifugo
- description: A multichannel customer messaging platform with Push (mobile + web), Email, SMS & RCS, and In-App Messages — framed as letting teams "set up and send mobile and web push notifications with advanced ta
  name: OneSignal
  slug: onesignal
- description: Google's cross-platform push notification and message delivery service for Android, iOS, and web. FCM uses HTTP v1 API for server-to-FCM message submission and a long-lived connection (XMPP-derived on
  name: Firebase Cloud Messaging (FCM)
  slug: firebase-cloud-messaging
- description: Apple's push notification system for iOS, iPadOS, macOS, tvOS, watchOS, and visionOS. APNs uses an HTTP/2-based provider API with token-based or certificate-based authentication for server-to-Apple de
  name: Apple Push Notification Service (APNs)
  slug: apple-push-notification-service
- description: An IETF-standardized push system for the web, comprising the W3C Push API (browser-side subscription), the IETF Web Push Protocol (RFC 8030, server-to-push-service delivery), and Message Encryption fo
  name: Web Push API
  slug: web-push
- description: A customer engagement platform offering push notifications (mobile + web), in-app messaging, email, and SMS with segmentation, journeys, and a Customer Journey Builder. Uses native vendor push gateway
  name: Pushwoosh
  slug: pushwoosh
artifact_total: 43
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/realtime-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://github.com/api-evangelist/realtime
- group: build
  title: ''
  type: GitHub
  url: https://github.com/api-evangelist/realtime
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/realtime-channel.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/realtime-message-envelope.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/realtime-subscription.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/realtime-presence.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/realtime-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/realtime-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/
created: '2026-05-22'
description: A topic catalog of realtime APIs, protocols, providers, and patterns. Realtime distinguishes itself from streaming by being interactive and typically bidirectional — channels, presence, signaling, and message envelopes flowing in both directions between clients and servers — where streaming is one-way firehose delivery. This index documents the major realtime protocols (WebSocket, Server-Sent Events, WebRTC, MQTT, CoAP, gRPC streaming, GraphQL Subscriptions), hosted realtime providers (Ably, Pusher, PubNub, LiveKit, Daily, Agora, Twilio, Vonage, Amazon IVS, Cloudflare Realtime), open-source frameworks (Socket.IO), and push notification systems (OneSignal, FCM, APNs, Web Push, Pushwoosh).
examples:
- key_count: 15
  name: Realtime Channel Mqtt Topic Example
  slug: realtime-channel-mqtt-topic-example
- key_count: 15
  name: Realtime Channel Pubsub Example
  slug: realtime-channel-pubsub-example
- key_count: 15
  name: Realtime Channel Webrtc Room Example
  slug: realtime-channel-webrtc-room-example
- key_count: 14
  name: Realtime Message Chat Example
  slug: realtime-message-chat-example
- key_count: 7
  name: Realtime Message Presence Event Example
  slug: realtime-message-presence-event-example
- key_count: 11
  name: Realtime Message Sensor Telemetry Example
  slug: realtime-message-sensor-telemetry-example
- key_count: 11
  name: Realtime Push Notification Example
  slug: realtime-push-notification-example
- key_count: 10
  name: Realtime Subscription Graphql Example
  slug: realtime-subscription-graphql-example
- key_count: 11
  name: Realtime Webrtc Signaling Offer Example
  slug: realtime-webrtc-signaling-offer-example
graphqls:
- description: A GraphQL operation type that delivers realtime updates to clients, typically carried over WebSocket using the graphql-ws or legacy graphql-transport-ws protocol, or over SSE using the GraphQL-SSE pro
  name: Realtime GraphQL API
  slug: realtime-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/realtime.png
json_schemas:
- name: Realtime Channel
  property_count: 15
  slug: realtime-channel
- name: Realtime Message Envelope
  property_count: 17
  slug: realtime-message-envelope
- name: Realtime Presence
  property_count: 7
  slug: realtime-presence
- name: Realtime Subscription
  property_count: 11
  slug: realtime-subscription
jsonld:
- class_count: 37
  name: Realtime Context
  property_count: 18
  slug: realtime-context
layout: provider
modified: '2026-05-22'
name: Realtime
nav: Providers
network: true
overview: 'Realtime publishes 26 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Realtime, WebSocket, WebRTC, Server-Sent Events, and MQTT.


  The Realtime catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Realtime''s developer surface includes developer portal, GitHub presence, code examples, and 7 more developer resources.'
random_paper: 106
rules:
- effective_rule_count: 5
  extends: []
  name: Realtime API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: realtime-jsonschema-spectral-rules
score:
  band: emerging
  composite: 15.9
  delta: -5.7
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 16.9
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 2.6
  previous_composite: 21.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/realtime/refs/heads/main/screenshots/realtime-2026-06-20T192649.png
security:
- kind: domain-security
  name: Realtime Domain Security
  slug: realtime-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: realtime
tags:
- Realtime
- WebSocket
- WebRTC
- Server-Sent Events
- MQTT
- Push Notifications
- Pub Sub
- Presence
- Signaling
- Topic
---
