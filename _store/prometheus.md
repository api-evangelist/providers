---
aid: prometheus
name: Prometheus
description: An open-source systems monitoring and alerting toolkit originally built at SoundCloud. Prometheus collects and stores metrics as time series data and provides a powerful query language (PromQL) for analysis.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Alerting
  - Metrics
  - Monitoring
  - Observability
  - Time Series
url: https://raw.githubusercontent.com/api-evangelist/prometheus/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: prometheus:prometheus-http-api
    name: Prometheus HTTP API
    description: The Prometheus HTTP API provides endpoints for executing instant and range queries using PromQL, querying metadata such as labels and series, and managing targets and rules. The API is reachable under /api/v1 on a Prometheus server and returns JSON responses. An OpenAPI specification is served at /api/v1/openapi.yaml.
    humanURL: https://prometheus.io/docs/prometheus/latest/querying/api/
    tags:
      - Metrics
      - PromQL
      - Query
      - Time Series
    properties:
      - type: Documentation
        url: https://prometheus.io/docs/prometheus/latest/querying/api/
      - type: OpenAPI
        url: openapi/prometheus-http-api-openapi.yml
      - type: GitHubRepository
        url: https://github.com/prometheus/prometheus
      - type: Change Log
        url: https://github.com/prometheus/prometheus/blob/main/CHANGELOG.md
      - type: JSONSchema
        url: json-schema/prometheus-metrics-schema.json
  - aid: prometheus:prometheus-management-api
    name: Prometheus Management API
    description: The Prometheus Management API provides administrative endpoints for managing a running Prometheus server, including configuration reloads, taking snapshots of the TSDB, cleaning tombstones, and graceful shutdown. These endpoints are disabled by default and require the --web.enable-lifecycle flag.
    humanURL: https://prometheus.io/docs/prometheus/latest/management_api/
    tags:
      - Administration
      - Management
      - Monitoring
    properties:
      - type: Documentation
        url: https://prometheus.io/docs/prometheus/latest/management_api/
      - type: OpenAPI
        url: openapi/prometheus-management-api-openapi.yml
  - aid: prometheus:prometheus-pushgateway-api
    name: Prometheus Pushgateway API
    description: The Pushgateway API accepts metrics pushed from short-lived batch jobs and ephemeral processes via HTTP PUT, POST, and DELETE requests. Metrics are organized by job and optional grouping labels, and are exposed for Prometheus scraping until explicitly deleted.
    humanURL: https://github.com/prometheus/pushgateway
    tags:
      - Batch Jobs
      - Metrics
      - Pushgateway
    properties:
      - type: Documentation
        url: https://github.com/prometheus/pushgateway/blob/master/README.md
      - type: OpenAPI
        url: openapi/prometheus-pushgateway-api-openapi.yml
      - type: GitHubRepository
        url: https://github.com/prometheus/pushgateway
      - type: Change Log
        url: https://github.com/prometheus/pushgateway/releases
  - aid: prometheus:prometheus-alertmanager-api
    name: Prometheus Alertmanager API
    description: The Alertmanager API v2 provides HTTP endpoints for querying alert status, managing silences and inhibitions, retrieving receiver configurations, and checking cluster status. An OpenAPI 2.0 specification is available in the Alertmanager repository.
    humanURL: https://prometheus.io/docs/alerting/latest/alertmanager/
    tags:
      - Alerting
      - Notifications
      - Silences
    properties:
      - type: Documentation
        url: https://prometheus.io/docs/alerting/latest/alertmanager/
      - type: OpenAPI
        url: openapi/prometheus-alertmanager-api-openapi.yml
      - type: AsyncAPI
        url: asyncapi/prometheus-alertmanager-webhook-asyncapi.yml
      - type: GitHubRepository
        url: https://github.com/prometheus/alertmanager
      - type: Change Log
        url: https://github.com/prometheus/alertmanager/releases
  - aid: prometheus:prometheus-remote-write-api
    name: Prometheus Remote Write API
    description: The Prometheus Remote Write API defines a standard protocol for sending time series data from Prometheus or compatible agents to remote storage backends via HTTP POST with Snappy-compressed protobuf payloads. The specification documents the wire format, required headers, and retry semantics for interoperable remote write implementations.
    humanURL: https://prometheus.io/docs/specs/prw/remote_write_spec/
    tags:
      - Integration
      - Remote Write
      - Storage
      - Time Series
    properties:
      - type: Documentation
        url: https://prometheus.io/docs/specs/prw/remote_write_spec/
  - aid: prometheus:prometheus-client-libraries
    name: Prometheus Client Libraries
    description: Prometheus provides official client libraries for Go, Java/Scala, Python, Ruby, and Rust that enable application instrumentation. Libraries implement the Prometheus metric types (Counter, Gauge, Histogram, Summary) and expose metrics via an HTTP endpoint for Prometheus to scrape.
    humanURL: https://prometheus.io/docs/instrumenting/clientlibs/
    tags:
      - Client Libraries
      - Instrumentation
      - Metrics
      - SDK
    properties:
      - type: Documentation
        url: https://prometheus.io/docs/instrumenting/clientlibs/
      - type: Reference
        url: https://prometheus.io/docs/instrumenting/writing_clientlibs/
common:
  - type: JSON-LD
    url: json-ld/prometheus-context.jsonld
  - type: JSONSchema
    url: json-schema/prometheus-metrics-schema.json
  - type: Website
    url: https://prometheus.io
  - type: Documentation
    url: https://prometheus.io/docs/
  - type: Getting Started
    url: https://prometheus.io/docs/introduction/getting_started/
  - type: GitHub Organization
    url: https://github.com/prometheus
  - type: GitHubRepository
    url: https://github.com/prometheus/prometheus
  - type: Blog
    url: https://prometheus.io/blog/
  - type: Community
    url: https://prometheus.io/community/
  - type: Change Log
    url: https://github.com/prometheus/prometheus/releases
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/prometheus
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
