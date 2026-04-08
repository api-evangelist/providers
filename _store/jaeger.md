---
aid: jaeger
url: https://raw.githubusercontent.com/api-evangelist/jaeger/refs/heads/main/apis.yml
apis:
- aid: jaeger:jaeger-query-api
  name: Jaeger Query API
  description: The Jaeger Query API is an HTTP/JSON API exposed by the Jaeger Query service for retrieving distributed traces, listing services and operations, querying service dependency graphs, and accessing performance metrics including latency, call rates, and error rates. A gRPC version of the Query API is also available defined in the jaeger-idl query.proto IDL.
  humanURL: https://www.jaegertracing.io/docs/latest/apis/
  tags:
  - Distributed Tracing
  - Observability
  - Query
  - Traces
  properties:
  - type: Documentation
    url: https://www.jaegertracing.io/docs/latest/apis/
  - type: OpenAPI
    url: openapi/jaeger-query-api.yml
  - type: GitHubRepository
    url: https://github.com/jaegertracing/jaeger
  - type: Change Log
    url: https://github.com/jaegertracing/jaeger/blob/main/CHANGELOG.md
- aid: jaeger:jaeger-collector-api
  name: Jaeger Collector API
  description: The Jaeger Collector API receives trace spans from instrumented applications and SDKs. Since Jaeger v1.11 the primary protocol is the jaeger.api_v2.CollectorService gRPC endpoint; the collector also accepts OTLP traces (binary gRPC, Protobuf over HTTP, JSON over HTTP) since v1.35, as well as legacy Thrift over UDP and HTTP formats.
  humanURL: https://www.jaegertracing.io/docs/latest/apis/
  tags:
  - Collector
  - Distributed Tracing
  - gRPC
  - OTLP
  properties:
  - type: Documentation
    url: https://www.jaegertracing.io/docs/latest/apis/
  - type: Reference
    url: https://github.com/jaegertracing/jaeger-idl/blob/main/proto/api_v2/collector.proto
  - type: GitHubRepository
    url: https://github.com/jaegertracing/jaeger
- aid: jaeger:jaeger-remote-storage-api
  name: Jaeger Remote Storage API
  description: The Jaeger Remote Storage API is a gRPC-based interface that allows extending Jaeger with custom storage backends. Any backend implementing this API can be deployed as a remote gRPC server and plugged into Jaeger components in place of built-in storage engines (available since v1.30).
  humanURL: https://www.jaegertracing.io/docs/latest/apis/
  tags:
  - Distributed Tracing
  - Extensions
  - gRPC
  - Storage
  properties:
  - type: Documentation
    url: https://www.jaegertracing.io/docs/latest/apis/
  - type: Reference
    url: https://github.com/jaegertracing/jaeger-idl/blob/main/proto/api_v2/query.proto
  - type: GitHubRepository
    url: https://github.com/jaegertracing/jaeger
- aid: jaeger:jaeger-remote-sampling-api
  name: Jaeger Remote Sampling API
  description: The Jaeger Remote Sampling API provides HTTP and gRPC endpoints that SDKs use to retrieve sampling strategies for distributed trace collection. It is implemented by the jaeger-collector and defined in the sampling.proto IDL, supporting both static file-based and adaptive sampling strategies.
  humanURL: https://www.jaegertracing.io/docs/latest/apis/
  tags:
  - Configuration
  - Distributed Tracing
  - gRPC
  - Sampling
  properties:
  - type: Documentation
    url: https://www.jaegertracing.io/docs/latest/apis/
  - type: Reference
    url: https://github.com/jaegertracing/jaeger-idl/blob/main/proto/api_v2/sampling.proto
  - type: GitHubRepository
    url: https://github.com/jaegertracing/jaeger
name: Jaeger
tags:
- Distributed Tracing
- Microservices
- Monitoring
- Observability
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Jaeger is an open source, end-to-end distributed tracing system for monitoring and troubleshooting microservices-based architectures. Jaeger provides visibility into distributed system behavior through trace collection, storage, and visualization.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

