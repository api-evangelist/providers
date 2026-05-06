---
aid: envoy-proxy
url: https://raw.githubusercontent.com/api-evangelist/envoy-proxy/refs/heads/main/apis.yml
apis:
  - aid: envoy-proxy:admin-api
    name: Envoy Proxy Admin API
    tags:
      - Gateways
      - Proxies
      - Service Mesh
    humanURL: https://www.envoyproxy.io/docs/envoy/latest/operations/admin
    properties:
      - url: openapi/envoy-proxy-admin-api-openapi.yml
        type: OpenAPI
      - url: https://www.envoyproxy.io/docs/envoy/latest/operations/admin
        type: Documentation
      - url: https://github.com/envoyproxy/envoy
        type: GitHubRepository
      - url: https://github.com/envoyproxy/envoy/releases
        type: Change Log
    description: The Envoy Proxy Administration Interface provides a local HTTP-based management API for querying and modifying various aspects of the Envoy server at runtime. It serves as a critical operational tool for monitoring, debugging, and managing Envoy proxy instances including statistics, clusters, listeners, certificates, runtime settings, logging, and health checks.
  - aid: envoy-proxy:xds-discovery-api
    name: Envoy Proxy xDS Discovery API
    tags:
      - Discovery
      - Gateways
      - Proxies
      - Service Mesh
    humanURL: https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol
    properties:
      - url: openapi/envoy-proxy-xds-discovery-api-openapi.yml
        type: OpenAPI
      - url: https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol
        type: Documentation
      - url: https://www.envoyproxy.io/docs/envoy/latest/configuration/overview/xds_api
        type: Reference
      - url: https://github.com/envoyproxy/envoy
        type: GitHubRepository
    description: The Envoy xDS (x Discovery Service) REST API provides endpoints for dynamically discovering and configuring Envoy proxy resources including clusters (CDS), listeners (LDS), routes (RDS), endpoints (EDS), secrets (SDS), and runtime configuration (RTDS). The xDS protocol is the foundation of Envoy's dynamic configuration model, enabling control planes to push configuration updates to Envoy instances without requiring restarts.
  - aid: envoy-proxy:rate-limit-service-api
    name: Envoy Proxy Rate Limit Service API
    tags:
      - gRPC
      - Proxies
      - Rate Limiting
      - Service Mesh
    humanURL: https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/rate_limit_filter
    properties:
      - url: https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/rate_limit_filter
        type: Documentation
      - url: https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/ratelimit/v3/rls.proto
        type: Reference
      - url: https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/other_features/global_rate_limiting
        type: Documentation
      - url: https://github.com/envoyproxy/envoy
        type: GitHubRepository
    description: The Envoy Rate Limit Service (RLS) is a gRPC-based API that allows Envoy to delegate rate limiting decisions to an external service. When a request matches a configured rate limit rule, Envoy calls the RLS to check whether the request should be allowed or throttled based on descriptors extracted from the request context.
  - aid: envoy-proxy:health-discovery-service-api
    name: Envoy Proxy Health Discovery Service API
    tags:
      - Discovery
      - gRPC
      - Health
      - Proxies
    humanURL: https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/health/v3/hds.proto
    properties:
      - url: https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/health/v3/hds.proto
        type: Documentation
      - url: https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/service
        type: Reference
      - url: https://github.com/envoyproxy/envoy
        type: GitHubRepository
    description: The Envoy Health Discovery Service (HDS) is a gRPC-based API that enables a management server to instruct Envoy to perform health checks on behalf of the control plane and report results back. This allows centralized health state management across a fleet of Envoy instances without requiring the control plane to perform health checks directly.
  - aid: envoy-proxy:access-log-service-api
    name: Envoy Proxy gRPC Access Log Service API
    tags:
      - Access Logs
      - gRPC
      - Observability
      - Proxies
    humanURL: https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/accesslog/v3/als.proto
    properties:
      - url: https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/accesslog/v3/als.proto
        type: Documentation
      - url: https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/service
        type: Reference
      - url: https://github.com/envoyproxy/envoy
        type: GitHubRepository
    description: The Envoy gRPC Access Log Service (ALS) API provides a streaming gRPC interface for receiving access log entries from Envoy instances in real time. It enables centralized log aggregation by allowing Envoy to stream HTTP and TCP access logs to a remote endpoint rather than writing them locally.
  - aid: envoy-proxy:external-processing-api
    name: Envoy Proxy External Processing API
    tags:
      - Extensibility
      - gRPC
      - Proxies
      - Request Processing
    humanURL: https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter
    properties:
      - url: https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter
        type: Documentation
      - url: https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/ext_proc/v3/external_processor.proto
        type: Reference
      - url: https://github.com/envoyproxy/envoy
        type: GitHubRepository
    description: The Envoy External Processing API is a gRPC-based service that enables an external server to inspect and modify HTTP requests and responses as they pass through Envoy. This extensibility mechanism supports use cases such as custom authentication, header manipulation, body transformation, and dynamic routing decisions without requiring Envoy filter plugins.
  - aid: envoy-proxy:external-authorization-api
    name: Envoy Proxy External Authorization API
    tags:
      - Authorization
      - gRPC
      - Proxies
      - Security
    humanURL: https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_authz_filter
    properties:
      - url: https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_authz_filter
        type: Documentation
      - url: https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/http/ext_authz/v3/ext_authz.proto
        type: Reference
      - url: https://github.com/envoyproxy/envoy
        type: GitHubRepository
    description: The Envoy External Authorization API provides a gRPC or HTTP interface for delegating authorization decisions to an external service. When a request arrives, Envoy calls the ext_authz service, which can approve, deny, or modify the request before it is forwarded to the upstream. This enables policy-based access control enforced at the proxy layer.
  - aid: envoy-proxy:metrics-service-api
    name: Envoy Proxy Metrics Service API
    tags:
      - gRPC
      - Metrics
      - Observability
      - Proxies
    humanURL: https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/metrics/v3/metrics_service.proto
    properties:
      - url: https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/metrics/v3/metrics_service.proto
        type: Documentation
      - url: https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/service
        type: Reference
      - url: https://github.com/envoyproxy/envoy
        type: GitHubRepository
    description: The Envoy Metrics Service API is a gRPC-based interface for streaming Envoy's statistics and metrics to a remote metrics collection service. It allows operators to centralize telemetry data from multiple Envoy instances, supporting integration with observability platforms for monitoring proxy performance and traffic patterns.
  - aid: envoy-proxy:tap-service-api
    name: Envoy Proxy Tap Service API
    tags:
      - Debugging
      - gRPC
      - Proxies
      - Traffic Capture
    humanURL: https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/tap_filter
    properties:
      - url: https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/tap_filter
        type: Documentation
      - url: https://www.envoyproxy.io/docs/envoy/latest/api-v3/service/tap/v3/tap.proto
        type: Reference
      - url: https://github.com/envoyproxy/envoy
        type: GitHubRepository
    description: The Envoy Tap Service API provides a mechanism for intercepting and recording HTTP and TCP traffic passing through Envoy. The tap filter matches requests and responses based on configurable conditions and streams the captured data to a sink such as a gRPC service or local file, enabling debugging, auditing, and traffic analysis use cases.
name: Envoy Proxy
tags:
  - Gateways
  - Proxies
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.envoyproxy.io/
    name: Website | Envoy Proxy
    type: Website
  - url: https://www.envoyproxy.io/docs/envoy/latest/
    name: Documentation | Envoy Proxy
    type: Documentation
  - url: https://www.envoyproxy.io/docs/envoy/latest/start/start
    name: Getting Started | Envoy Proxy
    type: Getting Started
  - url: https://blog.envoyproxy.io/
    name: Blog | Envoy Proxy
    type: Blog
  - url: https://github.com/envoyproxy/envoy/releases
    name: Change Log | Envoy Proxy
    type: Change Log
  - url: https://github.com/envoyproxy
    name: GitHub Organization | Envoy Proxy
    type: GitHub Organization
  - url: https://github.com/envoyproxy/envoy
    name: GitHub Repository | Envoy Proxy
    type: GitHubRepository
  - url: https://www.envoyproxy.io/community
    name: Community | Envoy Proxy
    type: Community
  - url: https://github.com/envoyproxy/envoy/blob/main/SECURITY.md
    name: Security Policy | Envoy Proxy
    type: Security
  - url: json-ld/envoy-proxy-context.jsonld
    name: JSON-LD Context | Envoy Proxy
    type: JSON-LD
  - url: json-schema/envoy-proxy-cluster.json
    name: Cluster JSON Schema
    type: JSONSchema
  - url: json-schema/envoy-proxy-listener.json
    name: Listener JSON Schema
    type: JSONSchema
  - url: json-schema/envoy-proxy-route.json
    name: Route Configuration JSON Schema
    type: JSONSchema
  - url: json-schema/envoy-proxy-endpoint.json
    name: Endpoint JSON Schema
    type: JSONSchema
  - url: https://github.com/envoyproxy/envoy/issues
    name: Issue Tracker | Envoy Proxy
    type: Issue Tracker
  - url: https://envoyslack.cncf.io/
    name: Slack Community | Envoy Proxy
    type: Community
  - url: https://www.cncf.io/projects/envoy/
    name: CNCF Project | Envoy Proxy
    type: Community
  - url: https://www.envoyproxy.io/docs/envoy/latest/api-v3/api
    name: v3 API Reference | Envoy Proxy
    type: Reference
created: '2026-01-02'
modified: '2026-04-28'
position: Consumer
description: Envoy Proxy is an open-source edge and service proxy that is designed for cloud-native applications. It acts as a gateway for all incoming and outgoing traffic within a microservices architecture, providing functionalities such as load balancing, service discovery, encryption, authentication, and observability. Envoy Proxy is known for its high performance and low latency, making it a popular choice for companies seeking to optimize their network traffic and improve overall system efficiency.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
