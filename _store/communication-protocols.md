---
aid: communication-protocols
url: https://raw.githubusercontent.com/api-evangelist/communication-protocols/refs/heads/main/apis.yml
name: Communication Protocols
x-type: topic
description: Communication protocols are systems of rules that allow two or more entities in a networked system to exchange information. Modern API platforms rely on layered protocol stacks that span the physical and link layers, network and transport layers, and application protocols such as HTTP, gRPC, MQTT, AMQP, WebSockets, SSE, and Webhooks. The communication protocols topic surveys the most relevant standards bodies (IETF, W3C, IEEE, ITU, ISO), the most widely deployed protocols at each layer, and the way protocol choice shapes API design, performance, security, and interoperability.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - APIs
  - Application Protocols
  - Communication Protocols
  - Internet
  - IETF
  - Networking
  - Real-Time
  - Standards
  - Transport
  - Web
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: communication-protocols:http
    name: Hypertext Transfer Protocol (HTTP)
    description: The application layer protocol that powers the World Wide Web and the majority of REST and HTTP APIs. HTTP/1.1 is defined in RFC 9110-9114, HTTP/2 in RFC 9113, and HTTP/3 in RFC 9114, the latter running over QUIC. HTTP defines methods, status codes, headers, content negotiation, caching, and conditional requests that underpin modern web APIs.
    humanURL: https://httpwg.org/specs/
    baseURL: https://httpwg.org
    tags:
      - Application Protocol
      - HTTP
      - IETF
      - REST
      - Web
    properties:
      - type: Specification
        url: https://www.rfc-editor.org/rfc/rfc9110
      - type: Specification
        url: https://www.rfc-editor.org/rfc/rfc9112
      - type: Specification
        url: https://www.rfc-editor.org/rfc/rfc9113
      - type: Specification
        url: https://www.rfc-editor.org/rfc/rfc9114
      - type: Working Group
        url: https://datatracker.ietf.org/wg/httpbis/about/
    x-features:
      - Stateless request/response model
      - Methods, status codes, headers, content negotiation
      - HTTP/2 multiplexing and HPACK header compression
      - HTTP/3 over QUIC for low-latency, head-of-line-free transport
      - Strong caching semantics with conditional requests
    x-useCases:
      - REST and resource-oriented APIs
      - GraphQL and gRPC-Web transport
      - Webhook delivery
      - Browser-to-API communication
  - aid: communication-protocols:grpc
    name: gRPC
    description: A high-performance, contract-first RPC framework built on HTTP/2 with Protocol Buffers as the default IDL. gRPC supports unary, server streaming, client streaming, and bidirectional streaming and is widely used for microservice-to-microservice communication and for polyglot APIs across cloud-native platforms.
    humanURL: https://grpc.io/
    baseURL: https://grpc.io
    tags:
      - CNCF
      - HTTP/2
      - Protocol Buffers
      - RPC
      - Streaming
    properties:
      - type: Documentation
        url: https://grpc.io/docs/
      - type: Specification
        url: https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md
      - type: GitHub Organization
        url: https://github.com/grpc
    x-features:
      - HTTP/2 multiplexed transport with Protobuf payloads
      - Four streaming modes (unary, server, client, bidi)
      - Polyglot code generation across 11+ languages
      - Pluggable authentication, deadlines, and interceptors
    x-useCases:
      - Internal microservice communication
      - Mobile-to-backend APIs with low latency
      - High-throughput streaming workloads
      - Polyglot service interfaces
  - aid: communication-protocols:graphql
    name: GraphQL
    description: A query language and runtime for client-driven data APIs over HTTP and WebSockets. GraphQL exposes a single endpoint with a typed schema defining queries, mutations, and subscriptions, allowing clients to request precisely the data they need.
    humanURL: https://graphql.org/
    baseURL: https://graphql.org
    tags:
      - API
      - GraphQL
      - HTTP
      - Schema
      - Subscriptions
    properties:
      - type: Specification
        url: https://spec.graphql.org/
      - type: Documentation
        url: https://graphql.org/learn/
      - type: Reference
        url: https://github.com/graphql/graphql-spec
    x-features:
      - Strongly typed schema definition language (SDL)
      - Single endpoint with arbitrary query shapes
      - Subscriptions for real-time pushes over WebSocket
      - Introspection enabling tooling and codegen
    x-useCases:
      - Aggregating data from multiple backends
      - Tailored mobile and web client payloads
      - BFF (backend for frontend) APIs
      - Real-time dashboards via subscriptions
  - aid: communication-protocols:websocket
    name: WebSocket
    description: A bidirectional, full-duplex communication protocol over a single TCP connection, defined in RFC 6455. WebSocket upgrades from HTTP and is widely used for chat, collaborative editing, live dashboards, and game servers.
    humanURL: https://www.rfc-editor.org/rfc/rfc6455
    baseURL: https://www.rfc-editor.org
    tags:
      - Bidirectional
      - IETF
      - Real-Time
      - Web
      - WebSocket
    properties:
      - type: Specification
        url: https://www.rfc-editor.org/rfc/rfc6455
      - type: Documentation
        url: https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
    x-features:
      - HTTP upgrade handshake to TCP-level full-duplex frames
      - Text and binary frame types
      - Subprotocol negotiation (e.g. graphql-ws, mqtt)
      - Native support in browsers and most server runtimes
    x-useCases:
      - Real-time chat and collaboration
      - Live tickers and dashboards
      - GraphQL subscription transport
      - Multiplayer games and signaling
  - aid: communication-protocols:mqtt
    name: MQTT
    description: A lightweight publish-subscribe messaging protocol designed for constrained devices and unreliable networks. MQTT is an OASIS standard and is widely used in IoT, automotive, and edge environments. MQTT 5 adds user properties, reason codes, shared subscriptions, and other modern features.
    humanURL: https://mqtt.org/
    baseURL: https://mqtt.org
    tags:
      - IoT
      - Lightweight
      - OASIS
      - Pub/Sub
    properties:
      - type: Specification
        url: https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html
      - type: Documentation
        url: https://mqtt.org/getting-started/
      - type: Reference
        url: https://www.hivemq.com/mqtt/mqtt-essentials/
    x-features:
      - Tiny binary protocol with three QoS levels
      - Hierarchical topic-based pub/sub
      - Retained messages and last-will-and-testament
      - MQTT 5 reason codes, properties, and shared subscriptions
    x-useCases:
      - IoT telemetry and command/control
      - Automotive and industrial messaging
      - Mobile push and presence
      - Edge-to-cloud streaming
  - aid: communication-protocols:amqp
    name: AMQP
    description: The Advanced Message Queuing Protocol, an OASIS standard for interoperable, broker-mediated messaging. AMQP 1.0 defines a wire protocol with strong typing, links, sessions, and connection-level security and is used by RabbitMQ, Azure Service Bus, and many other brokers.
    humanURL: https://www.amqp.org/
    baseURL: https://www.amqp.org
    tags:
      - Brokered
      - Enterprise Messaging
      - OASIS
      - Queuing
    properties:
      - type: Specification
        url: https://docs.oasis-open.org/amqp/core/v1.0/os/amqp-core-overview-v1.0-os.html
      - type: Documentation
        url: https://www.rabbitmq.com/protocol.html
    x-features:
      - Wire-level interoperability across brokers
      - Reliable, transactional messaging with sessions and links
      - SASL-based authentication and TLS transport
    x-useCases:
      - Enterprise integration and ESB scenarios
      - Cross-language work queues and task distribution
      - Cloud broker messaging on Azure Service Bus
  - aid: communication-protocols:webhooks
    name: Webhooks
    description: An HTTP-based pattern for delivering event notifications from one service to another by performing an outbound HTTP POST to a URL registered by the consumer. Webhooks are not a single specification but the broader pattern is increasingly governed by efforts such as the CloudEvents specification and the IETF Webhook security drafts.
    humanURL: https://webhooks.fyi/
    baseURL: https://webhooks.fyi
    tags:
      - Async
      - Events
      - HTTP
      - Push
    properties:
      - type: Reference
        url: https://webhooks.fyi/
      - type: Specification
        url: https://cloudevents.io/
      - type: Documentation
        url: https://www.standardwebhooks.com/
    x-features:
      - Outbound HTTP POST event delivery
      - Pluggable signing schemes (HMAC, JWT) for verification
      - Replay protection with timestamps and nonces
      - Aligns with CloudEvents and Standard Webhooks
    x-useCases:
      - Asynchronous event delivery between SaaS platforms
      - Build, deploy, and CI pipeline notifications
      - Payment and billing event hooks
      - Third-party integrations without polling
  - aid: communication-protocols:server-sent-events
    name: Server-Sent Events (SSE)
    description: A simple, one-way, server-to-client streaming protocol defined as part of the HTML living standard. SSE runs over plain HTTP, supports automatic reconnection, and is widely used for live status feeds and LLM token streaming.
    humanURL: https://html.spec.whatwg.org/multipage/server-sent-events.html
    baseURL: https://html.spec.whatwg.org
    tags:
      - HTML
      - HTTP
      - Real-Time
      - Streaming
    properties:
      - type: Specification
        url: https://html.spec.whatwg.org/multipage/server-sent-events.html
      - type: Documentation
        url: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events
    x-features:
      - Plain HTTP text/event-stream responses
      - Automatic browser reconnection with Last-Event-ID
      - Simpler than WebSocket for one-way fan-out
    x-useCases:
      - LLM token streaming
      - Live status and activity feeds
      - Server-pushed dashboards
common:
  - type: Documentation
    url: https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml
  - type: Reference
    url: https://www.rfc-editor.org/standards
  - type: Reference
    url: https://www.iso.org/standard/74534.html
  - type: Reference
    url: https://en.wikipedia.org/wiki/Communication_protocol
  - type: Resources
    url: https://www.cncf.io/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
