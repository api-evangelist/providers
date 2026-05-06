---
aid: grpc
name: gRPC
description: gRPC is a high-performance, open-source universal RPC framework that uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features such as authentication, bidirectional streaming and flow control, blocking or nonblocking bindings, and cancellation and timeouts. Originally developed at Google, it is now a CNCF project.
url: https://raw.githubusercontent.com/api-evangelist/grpc/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CNCF
  - HTTP/2
  - Microservices
  - Protocol Buffers
  - RPC
created: '2025'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: grpc:grpc-web-proxy-api
    name: gRPC-Web Proxy API
    description: OpenAPI specification for gRPC-Web proxy endpoints covering health checking, server reflection, and channelz introspection services exposed over HTTP for browser-based and REST clients.
    humanURL: https://grpc.io/docs/platforms/web/
    tags:
      - Channelz
      - gRPC-Web
      - Health Checking
      - Reflection
    properties:
      - type: OpenAPI
        url: openapi.yml
      - type: Documentation
        url: https://grpc.io/docs/platforms/web/
      - type: Reference
        url: https://grpc.io/docs/platforms/web/basics/
      - type: JSONSchema
        url: json-schema.yml
  - aid: grpc:grpc-core
    name: gRPC Core Framework
    description: The gRPC core framework defines the RPC protocol, service definition format using Protocol Buffers, and the fundamental call lifecycle including unary, server-streaming, client-streaming, and bidirectional streaming patterns over HTTP/2. It is the foundational specification implemented by all language-specific gRPC SDKs.
    humanURL: https://grpc.io/docs/what-is-grpc/introduction/
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://grpc.io/docs/what-is-grpc/introduction/
      - type: Reference
        url: https://grpc.io/docs/what-is-grpc/core-concepts/
      - type: Authentication
        url: https://grpc.io/docs/guides/auth/
      - type: GitHubRepository
        url: https://github.com/grpc/grpc
      - type: JSONSchema
        url: service-config-schema.json
      - type: JSONSchema
        url: json-schema.yml
      - type: JSON-LD
        url: context.jsonld
    tags:
      - HTTP/2
      - Protocol Buffers
      - RPC
      - Streaming
  - aid: grpc:protobuf-service-definition
    name: Protocol Buffers Service Definition Schema
    description: JSON Schema for Protocol Buffers service definition format (.proto files). Describes the structure of gRPC service declarations, RPC methods, message types, enums, oneofs, maps, and file-level options used to define gRPC APIs.
    humanURL: https://protobuf.dev/programming-guides/proto3/
    tags:
      - IDL
      - Protocol Buffers
      - Schema
      - Service Definition
    properties:
      - type: Documentation
        url: https://protobuf.dev/programming-guides/proto3/
      - type: JSONSchema
        url: json-schema/protobuf-service-definition.yml
  - aid: grpc:grpc-health-checking
    name: gRPC Health Checking Service
    description: The gRPC Health Checking Protocol defines a standard service that gRPC servers implement to expose health status information to clients and load balancers. Servers implement the Health service proto to report per-service readiness, and clients can configure automatic health-check-based connection management.
    humanURL: https://grpc.io/docs/guides/health-checking/
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://grpc.io/docs/guides/health-checking/
      - type: Reference
        url: https://github.com/grpc/grpc-proto/blob/master/grpc/health/v1/health.proto
      - type: GitHubRepository
        url: https://github.com/grpc/grpc-proto
      - type: AsyncAPI
        url: asyncapi.yml
    tags:
      - Health Checking
      - Load Balancing
      - Observability
  - aid: grpc:grpc-server-reflection
    name: gRPC Server Reflection
    description: The gRPC Server Reflection Protocol allows gRPC servers to declare the protobuf-defined APIs they export over a standardized RPC service, including all types referenced by request and response messages. This enables command-line debugging tools and clients to dynamically discover and invoke gRPC services without pre-compiled stubs.
    humanURL: https://grpc.io/docs/guides/reflection/
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://grpc.io/docs/guides/reflection/
      - type: Reference
        url: https://github.com/grpc/grpc/blob/master/doc/server-reflection.md
      - type: AsyncAPI
        url: asyncapi.yml
    tags:
      - Debugging
      - Reflection
      - Service Discovery
common:
  - type: Website
    url: https://grpc.io/
  - type: Documentation
    url: https://grpc.io/docs/
  - type: Getting Started
    url: https://grpc.io/docs/languages/
  - type: GitHub Organization
    url: https://github.com/grpc
  - type: Blog
    url: https://grpc.io/blog/
  - type: Community
    url: https://grpc.io/community/
  - type: FAQ
    url: https://grpc.io/docs/what-is-grpc/faq/
  - type: SDKs
    url: https://grpc.io/docs/languages/
  - type: Change Log
    url: https://github.com/grpc/grpc/releases
  - type: JSONSchema
    url: json-schema.yml
  - type: JSONSchema
    url: service-config-schema.json
  - type: AsyncAPI
    url: asyncapi.yml
  - type: JSON-LD
    url: context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
