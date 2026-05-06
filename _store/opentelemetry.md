---
aid: opentelemetry
name: OpenTelemetry
description: Vendor-neutral open-source observability framework for cloud-native software, providing a collection of tools, APIs, and SDKs for instrumenting, generating, collecting, and exporting telemetry data including metrics, logs, and traces.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Logging
  - Metrics
  - Monitoring
  - Observability
  - Open Source
  - Tracing
created: '2025-01-01'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/opentelemetry/refs/heads/main/apis.yml
specificationVersion: '0.19'
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
common:
  - url: https://opentelemetry.io/
    name: OpenTelemetry
    type: Website
    description: Official OpenTelemetry project website.
  - url: https://opentelemetry.io/docs/
    name: Documentation
    type: Documentation
    description: Official OpenTelemetry documentation hub.
  - url: https://opentelemetry.io/docs/getting-started/
    name: Getting Started
    type: Getting Started
    description: Guides for getting started with OpenTelemetry instrumentation.
  - url: https://github.com/open-telemetry
    name: GitHub Organization
    type: GitHub Organization
    description: OpenTelemetry GitHub organization containing all project repositories.
  - url: https://github.com/open-telemetry/opentelemetry-specification
    name: OpenTelemetry Specification
    type: GitHubRepository
    description: The OpenTelemetry specification defining APIs, SDKs, and data models.
  - url: https://opentelemetry.io/docs/languages/
    name: SDKs
    type: SDKs
    description: OpenTelemetry SDK implementations for all supported programming languages.
  - url: https://opentelemetry.io/blog/
    name: Blog
    type: Blog
    description: OpenTelemetry project blog with announcements and technical articles.
  - url: https://opentelemetry.io/community/
    name: Community
    type: Community
    description: Community resources including CNCF Slack, SIG meetings, and contribution guides.
  - url: https://cloud-native.slack.com/archives/CJFCJHG4Q
    name: Slack
    type: Slack
    description: OpenTelemetry community Slack channel in the CNCF Slack workspace.
  - url: https://stackoverflow.com/questions/tagged/open-telemetry
    name: Stack Overflow
    type: Stack Overflow
    description: OpenTelemetry-tagged questions and answers on Stack Overflow.
  - url: https://github.com/open-telemetry/opentelemetry-specification/blob/main/CHANGELOG.md
    name: Change Log
    type: Change Log
    description: Changelog for the OpenTelemetry specification.
  - url: https://github.com/open-telemetry/opentelemetry-collector/security/policy
    name: Security
    type: Security
    description: Security disclosure policy for the OpenTelemetry project.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
