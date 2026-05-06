---
aid: apache-zipkin
name: Apache Zipkin
description: Apache Zipkin is a distributed tracing system that helps gather timing data needed to troubleshoot latency problems in service architectures. It manages both the collection and lookup of tracing data through a collector and query service. Zipkin provides a REST API, web UI, and multiple storage backends (Cassandra, Elasticsearch, MySQL). It supports the B3 propagation format and is compatible with OpenZipkin instrumentation libraries. Originally created at Twitter, it is now maintained as an open-source project.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Distributed Tracing
  - Microservices
  - Monitoring
  - Observability
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-zipkin/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-zipkin:apache-zipkin-api
    name: Apache Zipkin REST API
    description: The Zipkin REST API v2 provides endpoints for querying trace data, service names, span names, and dependencies. Key endpoints include GET /api/v2/services (list services), GET /api/v2/spans (list span names for a service), GET /api/v2/traces (search traces by service, span, tags, duration), GET /api/v2/trace/{traceId} (get a specific trace), and GET /api/v2/dependencies (service dependency graph). Span reporting uses POST /api/v2/spans for JSON format or POST /api/v2/spans for Thrift format.
    humanURL: https://zipkin.io/zipkin-api/
    tags:
      - REST
      - Distributed Tracing
      - Monitoring
      - Observability
    properties:
      - type: Documentation
        url: https://zipkin.io/zipkin-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/openzipkin/zipkin-api/master/zipkin2-api.yaml
common:
  - type: GitHubRepository
    url: https://github.com/openzipkin/zipkin
  - type: Documentation
    url: https://zipkin.io/pages/documentation.html
  - type: Portal
    url: https://zipkin.io/
  - type: GettingStarted
    url: https://zipkin.io/pages/quickstart.html
  - type: ReleaseNotes
    url: https://github.com/openzipkin/zipkin/releases
  - type: Support
    url: https://gitter.im/openzipkin/zipkin
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: SDK
    url: https://pypi.org/project/py_zipkin/
    title: Python SDK
  - type: SDK
    url: https://search.maven.org/search?q=io.zipkin
    title: Java SDK
  - type: Features
    data:
      - name: Distributed Trace Collection
        description: Collect timing and metadata for distributed service calls with B3 propagation headers.
      - name: Trace Query and Visualization
        description: Web UI and REST API for searching and visualizing distributed traces with latency analysis.
      - name: Service Dependency Graph
        description: Automatic service call graph generation from collected trace data.
      - name: Multiple Storage Backends
        description: Cassandra, Elasticsearch, and MySQL storage backends for different scale requirements.
      - name: OpenTelemetry Compatible
        description: Accepts OTLP/Zipkin spans from OpenTelemetry instrumented services.
      - name: B3 Propagation
        description: Standard B3 trace propagation headers for distributed context passing across services.
  - type: UseCases
    data:
      - name: Microservices Latency Troubleshooting
        description: Identify bottlenecks and slow service calls in distributed architectures.
      - name: Service Dependency Mapping
        description: Automatically discover and visualize service-to-service call graphs.
      - name: Performance Regression Detection
        description: Compare trace data before and after deployments to detect performance regressions.
      - name: Root Cause Analysis
        description: Follow distributed call chains to identify the root cause of errors and failures.
  - type: Integrations
    data:
      - name: Spring Cloud Sleuth
        description: Spring Boot auto-instrumentation for trace propagation and Zipkin reporting.
      - name: Brave
        description: Java instrumentation library (Brave) for adding Zipkin tracing to Java applications.
      - name: Elasticsearch
        description: Elasticsearch storage backend for scalable trace data storage and search.
      - name: Apache Cassandra
        description: Cassandra storage backend for high-volume trace data.
      - name: OpenTelemetry
        description: OpenTelemetry Zipkin exporter for reporting OTLP traces to Zipkin.
      - name: Kafka
        description: Kafka collector for ingesting spans from high-throughput microservice architectures.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
