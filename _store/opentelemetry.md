---
aid: opentelemetry
url: https://raw.githubusercontent.com/api-evangelist/opentelemetry/refs/heads/main/apis.yml
apis:
- aid: opentelemetry:opentelemetry-protocol-otlp-http-api
  name: OpenTelemetry Protocol (OTLP) HTTP API
  description: The OTLP HTTP API provides endpoints for exporting traces, metrics, and logs using the OpenTelemetry Protocol, the native wire format for transmitting telemetry data between instrumented applications, collectors, and observability backends.
  humanURL: https://opentelemetry.io/docs/specs/otlp/
  tags:
  - Logging
  - Metrics
  - Observability
  - Tracing
  properties:
  - type: Documentation
    url: https://opentelemetry.io/docs/specs/otlp/
  - type: OpenAPI
    url: openapi.yml
  - type: AsyncAPI
    url: asyncapi/opentelemetry-otlp-asyncapi.yml
  - type: JSONSchema
    url: json-schema.json
  - type: JSON-LD
    url: context.jsonld
  - type: Reference
    url: https://opentelemetry.io/docs/specs/otlp/#otlphttp
  - type: Getting Started
    url: https://opentelemetry.io/docs/collector/
  - type: Client Libraries
    url: https://opentelemetry.io/docs/languages/
- aid: opentelemetry:opentelemetry-protocol-otlp-grpc-api
  name: OpenTelemetry Protocol (OTLP) gRPC API
  description: The OTLP gRPC API defines Protocol Buffers service definitions for exporting traces, metrics, and logs over gRPC. It is the primary transport for OpenTelemetry data between SDK instrumentation, the OpenTelemetry Collector, and observability backends, offering bidirectional streaming and efficient binary encoding.
  humanURL: https://opentelemetry.io/docs/specs/otlp/#otlpgrpc
  tags:
  - gRPC
  - Logging
  - Metrics
  - Observability
  - Tracing
  properties:
  - type: Documentation
    url: https://opentelemetry.io/docs/specs/otlp/#otlpgrpc
  - type: Reference
    url: https://opentelemetry.io/docs/specs/otlp/#otlpgrpc-response
  - type: GitHubRepository
    url: https://github.com/open-telemetry/opentelemetry-proto
- aid: opentelemetry:opentelemetry-collector-api
  name: OpenTelemetry Collector API
  description: The OpenTelemetry Collector is a vendor-agnostic proxy for receiving, processing, and exporting telemetry data. It exposes HTTP and gRPC endpoints for receiving OTLP data and provides a configuration API for managing pipelines, receivers, processors, and exporters at runtime via the zPages diagnostic extension and config file hot-reloading.
  humanURL: https://opentelemetry.io/docs/collector/
  tags:
  - Collector
  - Configuration
  - Observability
  - Pipeline
  properties:
  - type: Documentation
    url: https://opentelemetry.io/docs/collector/
  - type: Reference
    url: https://opentelemetry.io/docs/collector/configuration/
  - type: GitHubRepository
    url: https://github.com/open-telemetry/opentelemetry-collector
- aid: opentelemetry:opentelemetry-sdk-api
  name: OpenTelemetry SDK API
  description: The OpenTelemetry SDK API specifies language-level interfaces for instrumentation, including the Tracer, Meter, and Logger APIs used by application code to create spans, record metrics, and emit log records. Implementations are available for all major programming languages including Java, Python, Go, JavaScript, .NET, Ruby, and others.
  humanURL: https://opentelemetry.io/docs/specs/otel/
  tags:
  - Instrumentation
  - Logging
  - Metrics
  - SDK
  - Tracing
  properties:
  - type: Documentation
    url: https://opentelemetry.io/docs/specs/otel/
  - type: Reference
    url: https://opentelemetry.io/docs/specs/otel/trace/api/
  - type: Client Libraries
    url: https://opentelemetry.io/docs/languages/
  - type: GitHubRepository
    url: https://github.com/open-telemetry/opentelemetry-specification
name: OpenTelemetry
tags:
- Cloud Native
- Logging
- Metrics
- Monitoring
- Observability
- Open Source
- Tracing
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Vendor-neutral open-source observability framework for cloud-native software, providing a collection of tools, APIs, and SDKs for instrumenting, generating, collecting, and exporting telemetry data including metrics, logs, and traces.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

