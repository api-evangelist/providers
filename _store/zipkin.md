---
aid: zipkin
name: Zipkin
description: Zipkin is an open source distributed tracing system for gathering timing data to troubleshoot latency problems in microservice architectures. It was originally developed at Twitter based on the Google Dapper paper, and is now a CNCF-related project maintained by the OpenZipkin community. Zipkin provides a collector, storage, and query service with a UI for visualizing trace data across distributed services.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Distributed Tracing
  - Observability
  - Open Source
  - Microservices
url: https://raw.githubusercontent.com/api-evangelist/zipkin/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: zipkin:zipkin-api-v2
    name: Zipkin API V2
    description: Zipkin's v2 HTTP API for querying and collecting distributed traces. Provides endpoints for submitting spans, querying traces, looking up services and span names, and retrieving dependency links between services.
    humanURL: https://zipkin.io/zipkin-api/
    tags:
      - Dependencies
      - Distributed Tracing
      - Observability
      - Spans
      - Traces
    properties:
      - type: Documentation
        url: https://zipkin.io/zipkin-api/
      - type: GitHubRepository
        url: https://github.com/openzipkin/zipkin
      - type: OpenAPI
        url: openapi/zipkin-api-v2.yml
      - type: JSONSchema
        url: json-schema/zipkin-api-v2-span-schema.json
      - type: JSONSchema
        url: json-schema/zipkin-api-v2-endpoint-schema.json
      - type: JSONSchema
        url: json-schema/zipkin-api-v2-annotation-schema.json
      - type: JSONSchema
        url: json-schema/zipkin-api-v2-dependency-link-schema.json
      - type: JSONStructure
        url: json-structure/zipkin-api-v2-span-structure.json
      - type: JSONStructure
        url: json-structure/zipkin-api-v2-endpoint-structure.json
      - type: JSONStructure
        url: json-structure/zipkin-api-v2-annotation-structure.json
      - type: JSONStructure
        url: json-structure/zipkin-api-v2-dependency-link-structure.json
      - type: Example
        url: examples/zipkin-api-v2-get-services-example.json
      - type: Example
        url: examples/zipkin-api-v2-get-dependencies-example.json
      - type: Example
        url: examples/zipkin-api-v2-report-spans-example.json
      - type: Example
        url: examples/zipkin-api-v2-search-traces-example.json
common:
  - type: Website
    url: https://zipkin.io
  - type: Documentation
    url: https://zipkin.io/pages/quickstart.html
  - type: GitHubOrganization
    url: https://github.com/openzipkin
  - type: SDK
    url: https://github.com/openzipkin/brave
    name: Brave (Java)
  - type: SDK
    url: https://github.com/openzipkin/zipkin-go
    name: zipkin-go (Go)
  - type: SDK
    url: https://github.com/openzipkin/zipkin-js
    name: zipkin-js (JavaScript/Node.js)
  - type: SDK
    url: https://github.com/openzipkin/zipkin-ruby
    name: zipkin-ruby (Ruby)
  - type: JSONLD
    url: json-ld/zipkin-context.jsonld
  - type: SpectralRules
    url: rules/zipkin-spectral.yaml
  - type: NaftikoCapability
    url: capabilities/distributed-tracing-investigation.yaml
  - type: Vocabulary
    url: vocabulary/zipkin-vocabulary.yaml
  - data:
      - name: Distributed Tracing
        description: End-to-end tracing of requests across microservices.
      - name: Span Collection
        description: Ingestion of spans via HTTP, Kafka, and other transports.
      - name: Trace Search
        description: Query traces by service, span name, tags, and time range.
      - name: Dependency Graph
        description: Derived service-to-service dependency links from spans.
      - name: UI
        description: Web-based UI for exploring traces and dependency graphs.
      - name: Pluggable Storage
        description: Pluggable backends including in-memory, MySQL, Cassandra, and Elasticsearch.
    name: Features
    type: Features
  - data:
      - name: Microservices Latency Debugging
        description: Identify slow services and operations in a microservice architecture.
      - name: Error Investigation
        description: Trace failed requests across services to find error origin.
      - name: Service Dependency Mapping
        description: Visualize which services call which, with call counts.
      - name: Performance Optimization
        description: Identify hotspots and optimize critical-path operations.
    name: UseCases
    type: UseCases
  - data:
      - name: Brave
        description: Java instrumentation library for OpenZipkin.
      - name: OpenTelemetry
        description: OpenTelemetry can export traces to Zipkin.
      - name: Spring Cloud Sleuth
        description: Spring framework integration emitting Zipkin traces.
      - name: Kafka
        description: Span transport via Kafka for asynchronous ingestion.
      - name: Elasticsearch
        description: Storage backend for spans and traces at scale.
    name: Integrations
    type: Integrations
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
