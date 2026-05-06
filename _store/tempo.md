---
name: Tempo
description: Tempo is an open source, high-scale distributed tracing backend from Grafana Labs. Designed for cost-efficient, object storage-backed trace storage with minimal operational overhead. Integrates with popular open telemetry standards including OpenTelemetry, Jaeger, Zipkin, and W3C Trace Context. Provides HTTP query APIs for trace retrieval, search, tag discovery, and metrics generation.
url: https://raw.githubusercontent.com/api-evangelist/tempo/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - Distributed Tracing
  - Observability
  - OpenTelemetry
  - Grafana
  - Monitoring
apis:
  - name: Tempo HTTP API
    description: Tempo exposes an HTTP API for querying traces, searching spans, discovering tag keys and values, and generating metrics from trace data. The API is compatible with Jaeger and Zipkin query protocols in addition to the native Tempo protocol. Used by Grafana dashboards, the Tempo CLI, and external integrations.
    humanURL: https://grafana.com/docs/tempo/latest/api_docs/
    baseURL: http://localhost:3200
    tags:
      - Distributed Tracing
      - Observability
      - Trace Querying
      - OpenTelemetry
    properties:
      - type: Documentation
        url: https://grafana.com/docs/tempo/latest/api_docs/
      - type: GitHub Repository
        url: https://github.com/grafana/tempo
      - type: OpenAPI
        url: openapi/tempo-openapi.yml
  - name: Tempo TraceQL API
    description: TraceQL is a query language developed for Grafana Tempo that allows filtering and selecting spans within traces. The TraceQL search API endpoint enables rich span-level filtering using a pipeline syntax with attribute matchers, duration filters, and structural operators.
    humanURL: https://grafana.com/docs/tempo/latest/traceql/
    baseURL: http://localhost:3200
    tags:
      - Distributed Tracing
      - Query Language
      - TraceQL
      - Observability
    properties:
      - type: Documentation
        url: https://grafana.com/docs/tempo/latest/traceql/
      - type: Reference
        url: https://grafana.com/docs/tempo/latest/traceql/query-editor/
common:
  - type: Website
    url: https://grafana.com/oss/tempo/
  - type: Documentation
    url: https://grafana.com/docs/tempo/latest/
  - type: GitHub Repository
    url: https://github.com/grafana/tempo
  - type: GitHub Organization
    url: https://github.com/grafana
  - type: Helm Chart
    url: https://grafana.github.io/helm-charts
  - type: Docker Hub
    url: https://hub.docker.com/r/grafana/tempo
  - type: Release Notes
    url: https://github.com/grafana/tempo/releases
  - type: Community
    url: https://community.grafana.com/c/grafana-tempo/
  - type: Slack
    url: https://grafana.slack.com/archives/C01BULREPHA
  - type: Blog
    url: https://grafana.com/blog/tag/traces/
  - type: Getting Started
    url: https://grafana.com/docs/tempo/latest/getting-started/
  - type: OpenAPI
    url: openapi/tempo-openapi.yml
  - type: JSON-LD
    url: json-ld/tempo-context.jsonld
  - type: JSONSchema
    url: json-schema/tempo-trace-schema.json
  - type: JSONStructure
    url: json-structure/tempo-trace-structure.json
  - type: SpectralRules
    url: rules/tempo-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/distributed-tracing.yaml
  - type: Vocabulary
    url: vocabulary/tempo-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
