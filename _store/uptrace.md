---
aid: uptrace
name: Uptrace
description: Uptrace is an open source APM and distributed tracing platform powered by OpenTelemetry for monitoring application traces, metrics, and logs. The Uptrace API provides programmatic access to annotations, Prometheus metrics ingestion, PromQL querying, alert rules, project management, and dashboards.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - APM
  - Observability
  - OpenTelemetry
  - Distributed Tracing
  - Monitoring
url: https://raw.githubusercontent.com/api-evangelist/uptrace/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: uptrace:uptrace
    name: Uptrace API
    description: The Uptrace REST API provides programmatic management of projects, chart annotations for deployment tracking, alert rules using PromQL, dashboard management, and Prometheus Remote Write for metrics ingestion. Uptrace accepts OpenTelemetry data via OTLP/gRPC and OTLP/HTTP.
    humanURL: https://uptrace.dev
    baseURL: https://api.uptrace.dev
    tags:
      - APM
      - Observability
      - OpenTelemetry
      - Distributed Tracing
      - Alerting
    properties:
      - type: Documentation
        url: https://uptrace.dev/get/get-started.html
      - type: GitHub Repository
        url: https://github.com/uptrace/uptrace
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/uptrace/refs/heads/main/openapi/uptrace-openapi.yml
common:
  - type: Website
    url: https://uptrace.dev
  - type: Documentation
    url: https://uptrace.dev/get/get-started.html
  - type: GitHub Organization
    url: https://github.com/uptrace/uptrace
  - type: Docker Hub
    url: https://hub.docker.com/r/uptrace/uptrace
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
