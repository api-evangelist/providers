---
aid: thanos
name: Thanos
description: Open-source, highly available Prometheus setup with long-term storage capabilities that provides a global query view across multiple Prometheus servers.
url: https://thanos.io/
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Metrics
  - Monitoring
  - Observability
  - Prometheus
  - Time Series Database
created: '2025'
modified: '2026-05-03'
type: Index
apis:
  - aid: thanos:thanos-query-api
    name: Thanos Query API
    description: Prometheus-compatible HTTP API for querying metrics across multiple Prometheus servers and long-term storage backends with global query view, deduplication, and partial response support.
    humanURL: https://thanos.io/tip/components/query.md/
    baseURL: http://localhost:9090
    tags:
      - Metrics
      - Monitoring
      - PromQL
      - Query
      - Time Series
    properties:
      - url: https://thanos.io/tip/components/query.md/
        type: Documentation
      - url: openapi/thanos-query-api.yml
        type: OpenAPI
      - url: json-schema/query-response.json
        type: JSONSchema
      - url: json-schema/store-info.json
        type: JSONSchema
      - url: json-ld/thanos-context.jsonld
        type: JSONLD
  - aid: thanos:thanos-store-gateway-api
    name: Thanos Store Gateway API
    description: gRPC-based Store API that serves metrics stored in object storage buckets, allowing Thanos Querier to access historical time series data from long-term storage backends such as S3, GCS, and Azure Blob Storage.
    humanURL: https://thanos.io/tip/components/store.md/
    baseURL: http://localhost:10902
    tags:
      - Metrics
      - Monitoring
      - Object Storage
      - Store
      - Time Series
    properties:
      - type: Documentation
        url: https://thanos.io/tip/components/store.md/
      - type: OpenAPI
        url: openapi/thanos-store-gateway-openapi.yml
  - aid: thanos:thanos-sidecar-api
    name: Thanos Sidecar API
    description: Component deployed alongside a Prometheus instance that implements the Thanos Store API on top of Prometheus remote-read API, enabling Queriers to access real-time Prometheus data and optionally uploading blocks to object storage.
    humanURL: https://thanos.io/tip/components/sidecar.md/
    baseURL: http://localhost:10902
    tags:
      - Metrics
      - Monitoring
      - Prometheus
      - Sidecar
      - Store
    properties:
      - type: Documentation
        url: https://thanos.io/tip/components/sidecar.md/
      - type: OpenAPI
        url: openapi/thanos-sidecar-openapi.yml
  - aid: thanos:thanos-ruler-api
    name: Thanos Ruler API
    description: Component that evaluates Prometheus recording and alerting rules against the Thanos Query API, exposes results as metrics via a Store API endpoint, and optionally uploads rule evaluation blocks to object storage.
    humanURL: https://thanos.io/tip/components/rule.md/
    baseURL: http://localhost:10902
    tags:
      - Alerting
      - Metrics
      - Monitoring
      - Prometheus
      - Rules
    properties:
      - type: Documentation
        url: https://thanos.io/tip/components/rule.md/
      - type: OpenAPI
        url: openapi/thanos-ruler-openapi.yml
  - aid: thanos:thanos-receive-api
    name: Thanos Receive API
    description: Implements the Prometheus Remote Write API to accept metrics pushed from Prometheus instances, storing them in a local TSDB and optionally uploading blocks to object storage for long-term retention and horizontal scalability.
    humanURL: https://thanos.io/tip/components/receive.md/
    baseURL: http://localhost:10902
    tags:
      - Metrics
      - Monitoring
      - Receive
      - Remote Write
      - Time Series
    properties:
      - type: Documentation
        url: https://thanos.io/tip/components/receive.md/
      - type: OpenAPI
        url: openapi/thanos-receive-openapi.yml
  - aid: thanos:thanos-compact-api
    name: Thanos Compact API
    description: Singleton process that applies Prometheus compaction procedures to block data stored in object storage, performing downsampling and retention policy enforcement to reduce storage costs and improve query performance over long time ranges.
    humanURL: https://thanos.io/tip/components/compact.md/
    baseURL: http://localhost:10902
    tags:
      - Compaction
      - Downsampling
      - Monitoring
      - Object Storage
      - Retention
    properties:
      - type: Documentation
        url: https://thanos.io/tip/components/compact.md/
      - type: OpenAPI
        url: openapi/thanos-compact-openapi.yml
common:
  - url: https://thanos.io/
    type: Website
  - url: json-ld/thanos-context.jsonld
    type: JSON-LD
  - url: json-schema/query-response.json
    type: JSONSchema
  - url: json-schema/store-info.json
    type: JSONSchema
  - url: json-structure/thanos-query-structure.json
    type: JSONStructure
  - url: rules/thanos-rules.yml
    type: SpectralRules
  - url: vocabulary/thanos-vocabulary.yml
    type: Vocabulary
  - url: capabilities/metrics-observability.yaml
    type: NaftikoCapability
  - url: https://thanos.io/tip/thanos/getting-started.md/
    type: Getting Started
  - url: https://thanos.io/tip/
    type: Documentation
  - url: https://github.com/thanos-io/thanos
    type: GitHubRepository
  - url: https://github.com/thanos-io
    type: GitHub Organization
  - url: https://thanos.io/tip/contributing/community.md/
    type: Community
  - url: https://thanos.io/tip/operating/troubleshooting.md/
    type: Troubleshooting
  - url: https://www.apache.org/licenses/LICENSE-2.0
    type: License
maintainers:
  - FN: Kin Lane
    url: http://apievangelist.com
    email: kin@apievangelist.com
---
