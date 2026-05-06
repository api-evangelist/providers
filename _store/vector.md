---
aid: vector
name: Vector
description: Vector is an open source high-performance observability data pipeline from Datadog for collecting, transforming, and routing logs, metrics, and traces. Built in Rust for performance and reliability, Vector supports 50+ sources, 20+ transforms, and 80+ sinks. It provides a built-in API for health monitoring and component inspection, plus Vector Remap Language (VRL) for powerful data transformation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Pipeline
  - Logs
  - Metrics
  - Observability
  - Open Source
  - Rust
  - Traces
url: https://raw.githubusercontent.com/api-evangelist/vector/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vector:vector-observability-api
    name: Vector Observability API
    description: 'The Vector Observability API provides HTTP endpoints for health monitoring of running Vector instances and gRPC endpoints for component inspection and event streaming. Enable via api.enabled: true in Vector configuration. Binds to 127.0.0.1:8686 by default. Note: the API does not support authentication and should only be used in isolated environments.'
    humanURL: https://vector.dev/docs/reference/api/
    baseURL: http://127.0.0.1:8686
    tags:
      - Health Monitoring
      - Observability
      - Pipeline Management
    properties:
      - type: Documentation
        url: https://vector.dev/docs/reference/api/
      - type: OpenAPI
        url: openapi/vector-observability-api-openapi.yml
      - type: JSONSchema
        url: json-schema/vector-observability-api-health-response-schema.json
        title: Health Response Schema
      - type: JSONStructure
        url: json-structure/vector-observability-api-health-response-structure.json
        title: Health Response Structure
      - type: Example
        url: examples/vector-observability-api-health-response-example.json
        title: Health Response Example
      - type: JSON-LD
        url: json-ld/vector-observability-api-context.jsonld
  - aid: vector:vector-vrl
    name: Vector Remap Language (VRL)
    description: Vector Remap Language (VRL) is a purpose-built expression language for transforming observability data in Vector. Provides 100+ built-in functions for parsing, filtering, enriching, and transforming logs, metrics, and traces without leaving the Vector pipeline.
    humanURL: https://vector.dev/docs/reference/vrl/
    tags:
      - Data Transformation
      - Expression Language
      - VRL
    properties:
      - type: Documentation
        url: https://vector.dev/docs/reference/vrl/
      - type: GitHub Repository
        url: https://github.com/vectordotdev/vrl
  - aid: vector:vector-helm
    name: Vector Helm Charts
    description: Official Helm charts for deploying Vector on Kubernetes as a DaemonSet (agent mode) or Deployment (aggregator mode).
    humanURL: https://vector.dev/docs/setup/installation/package-managers/helm/
    tags:
      - Helm
      - Kubernetes
      - Deployment
    properties:
      - type: Documentation
        url: https://vector.dev/docs/setup/installation/package-managers/helm/
      - type: GitHub Repository
        url: https://github.com/vectordotdev/helm-charts
common:
  - type: Website
    url: https://vector.dev
  - type: Documentation
    url: https://vector.dev/docs/
  - type: GitHubOrganization
    url: https://github.com/vectordotdev
  - type: GitHubRepository
    url: https://github.com/vectordotdev/vector
  - type: ReleaseNotes
    url: https://vector.dev/releases/
  - type: Blog
    url: https://vector.dev/blog/
  - type: Forum
    url: https://discord.com/invite/n2yjjZR
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/vector-dev
  - type: SpectralRules
    url: rules/vector-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/pipeline-monitoring.yaml
    title: Pipeline Monitoring
  - type: Vocabulary
    url: vocabulary/vector-vocabulary.yaml
  - type: Features
    data:
      - name: High-Performance Pipeline
        description: Built in Rust with benchmarks showing 86+ MiB/s throughput for log pipeline workloads.
      - name: Unified Data Plane
        description: Single binary handles logs, metrics, and traces from collection through routing.
      - name: 50+ Sources
        description: Native integrations for files, Kafka, Kubernetes, AWS S3/CloudWatch, Splunk, and more.
      - name: 80+ Sinks
        description: Route data to Elasticsearch, Datadog, S3, BigQuery, Splunk, Loki, and many more destinations.
      - name: Vector Remap Language (VRL)
        description: Purpose-built expression language with 100+ functions for transforming observability data.
      - name: Observability API
        description: Built-in HTTP/gRPC API for health checks and component inspection (must be explicitly enabled).
      - name: Kubernetes Native
        description: Deploy as DaemonSet (agent) or Deployment (aggregator) with official Helm charts.
      - name: Agent and Aggregator Modes
        description: Run as a lightweight agent on each node or as a centralized aggregator for fan-in routing.
  - type: UseCases
    data:
      - name: Log Pipeline Unification
        description: Replace multiple log shippers with a single Vector pipeline for all log collection and routing.
      - name: Observability Cost Reduction
        description: Filter, sample, and transform data before sending to expensive SaaS observability platforms.
      - name: Vendor Switching
        description: Route observability data to multiple backends simultaneously to facilitate migration.
      - name: Kubernetes Log Collection
        description: Deploy Vector as a DaemonSet to collect container logs from all Kubernetes nodes.
      - name: Log Enrichment
        description: Parse, enrich, and normalize log events using VRL before routing to downstream systems.
      - name: Metrics Collection
        description: Collect host and service metrics using Vector's built-in sources and forward to Prometheus or DataDog.
      - name: Splunk Cost Reduction
        description: Use Vector to filter and route Splunk data to reduce indexing volume and licensing costs.
  - type: Integrations
    data:
      - name: Datadog
        description: Native Datadog logs and metrics sink; Vector was created and is maintained by Datadog.
      - name: Elasticsearch
        description: Elasticsearch sink for forwarding logs and metrics to Elasticsearch clusters.
      - name: Splunk HEC
        description: Splunk HTTP Event Collector sink for sending data to Splunk Enterprise and Cloud.
      - name: Kafka
        description: Kafka source and sink for consuming and producing observability data streams.
      - name: AWS S3
        description: S3 sink for archiving logs and metrics to Amazon S3 for long-term storage.
      - name: Grafana Loki
        description: Loki sink for forwarding logs to Grafana's log aggregation system.
      - name: Prometheus
        description: Prometheus remote write sink and scrape source for metrics pipelines.
      - name: Kubernetes
        description: Kubernetes source for collecting container logs, pod metadata, and events.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
