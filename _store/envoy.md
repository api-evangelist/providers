---
aid: envoy
name: Envoy
description: Envoy is a high-performance, open-source edge and service proxy designed for cloud-native applications and microservice architectures. It provides advanced load balancing, observability, and traffic management features, and serves as the data plane for many service mesh implementations including Istio.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Load Balancing
  - Proxy
  - Service Mesh
url: https://www.envoyproxy.io/
created: '2025-01-01'
modified: '2026-04-28'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
apis:
  - aid: envoy:envoy-admin-api
    name: Envoy Admin API
    description: The Envoy Admin API provides local administrative access to a running Envoy proxy instance, exposing endpoints for inspecting clusters, listeners, configuration, statistics, health status, and runtime settings.
    humanURL: https://www.envoyproxy.io/docs/envoy/latest/operations/admin
    tags:
      - Admin
      - Management
      - Observability
    properties:
      - type: Documentation
        url: https://www.envoyproxy.io/docs/envoy/latest/operations/admin
      - type: OpenAPI
        url: openapi/envoy-admin-api-openapi.yml
  - aid: envoy:envoy-xds-api
    name: Envoy xDS APIs
    description: The xDS (x Discovery Service) APIs provide dynamic configuration for Envoy proxies via a management server, including LDS, RDS, CDS, EDS, SDS, and ADS. xDS APIs are served over gRPC or REST and allow management servers to push Listener, Route, Cluster, Endpoint, and Secret configurations to Envoy proxies at runtime without restarts.
    humanURL: https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol
    tags:
      - Discovery Service
      - Dynamic Configuration
      - gRPC
      - xDS
    properties:
      - type: Documentation
        url: https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol
      - type: Reference
        url: https://www.envoyproxy.io/docs/envoy/latest/configuration/overview/xds_api
      - type: GitHubRepository
        url: https://github.com/envoyproxy/envoy
  - aid: envoy:envoy-api-v3
    name: Envoy API V3
    description: The Envoy API v3 is the current stable protobuf-based configuration and extension API for Envoy proxy. It defines the configuration types for all Envoy subsystems including listeners, clusters, routes, endpoints, HTTP filters, network filters, transport sockets, and access logging. The API is defined using Protocol Buffers and published in the envoy-api repository.
    humanURL: https://www.envoyproxy.io/docs/envoy/latest/api/api
    tags:
      - Configuration
      - Extensions
      - Filters
      - Protobuf
    properties:
      - type: Documentation
        url: https://www.envoyproxy.io/docs/envoy/latest/api/api
      - type: GitHubRepository
        url: https://github.com/envoyproxy/envoy
      - type: JSONSchema
        url: json-schema/envoy-cluster.json
      - type: JSONSchema
        url: json-schema/envoy-listener.json
      - type: JSONSchema
        url: json-schema/envoy-route-configuration.json
  - aid: envoy:envoy-gateway-api
    name: Envoy Gateway API
    description: Envoy Gateway manages Envoy Proxy as a standalone or Kubernetes-based application gateway, implementing and extending the Kubernetes Gateway API. It provides Gateway API extensions including BackendTrafficPolicy, ClientTrafficPolicy, SecurityPolicy, and EnvoyPatchPolicy for advanced traffic management without requiring direct Envoy configuration knowledge.
    humanURL: https://gateway.envoyproxy.io/
    tags:
      - Cloud Native
      - Gateway
      - Kubernetes
      - Traffic Management
    properties:
      - type: Documentation
        url: https://gateway.envoyproxy.io/docs/
      - type: Reference
        url: https://gateway.envoyproxy.io/docs/concepts/gateway-api/
      - type: Getting Started
        url: https://gateway.envoyproxy.io/docs/
      - type: GitHubRepository
        url: https://github.com/envoyproxy/gateway
  - aid: envoy:envoy-ai-gateway-api
    name: Envoy AI Gateway API
    description: The Envoy AI Gateway manages unified access to Generative AI services built on Envoy Gateway. It provides OpenAI-compatible and Anthropic-compatible API endpoints for routing LLM traffic across multiple AI backends with backend rate limiting, policy control, and security configuration via Kubernetes custom resources.
    humanURL: https://aigateway.envoyproxy.io/
    tags:
      - AI
      - Cloud Native
      - Gateway
      - LLM
    properties:
      - type: Documentation
        url: https://aigateway.envoyproxy.io/docs/
      - type: Reference
        url: https://aigateway.envoyproxy.io/docs/api/
      - type: Getting Started
        url: https://aigateway.envoyproxy.io/docs/getting-started/basic-usage/
      - type: GitHubRepository
        url: https://github.com/envoyproxy/ai-gateway
      - type: Change Log
        url: https://aigateway.envoyproxy.io/release-notes/
      - type: OpenAPI
        url: openapi/envoy-ai-gateway-openapi.yml
common:
  - type: Website
    url: https://www.envoyproxy.io/
  - type: Documentation
    url: https://www.envoyproxy.io/docs/envoy/latest/
  - type: Getting Started
    url: https://www.envoyproxy.io/docs/envoy/latest/start/start
  - type: Blog
    url: https://blog.envoyproxy.io/
  - type: Change Log
    url: https://github.com/envoyproxy/envoy/releases
  - type: GitHub Organization
    url: https://github.com/envoyproxy
  - type: GitHubRepository
    url: https://github.com/envoyproxy/envoy
  - type: Community
    url: https://www.envoyproxy.io/community
  - type: JSONSchema
    url: json-schema/envoy-bootstrap.json
  - type: JSONSchema
    url: json-schema/envoy-cluster.json
  - type: JSONSchema
    url: json-schema/envoy-listener.json
  - type: JSONSchema
    url: json-schema/envoy-route-configuration.json
  - type: JSON-LD
    url: json-ld/envoy-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
