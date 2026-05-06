---
aid: resurface
name: Resurface
description: Resurface (now Graylog API Security) is an API runtime security and observability platform that captures and analyzes complete API request and response payloads in real time. It provides full API call logging, threat detection, data leak prevention, and compliance auditing for API traffic without sampling or aggregation. Acquired by Graylog and integrated into the Graylog SIEM platform.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Analytics
  - API Compliance
  - API Logging
  - API Observability
  - API Security
  - Data Leak Prevention
  - Runtime Security
  - SIEM
  - Threat Detection
url: https://raw.githubusercontent.com/api-evangelist/resurface/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: resurface:resurface-platform
    name: Resurface Platform
    description: Resurface captures complete API request and response data in real time, providing full-payload API call logging with no sampling. Security teams use it to detect threats, identify data leaks, and ensure compliance across all API traffic using a custom columnar database and SQL query interface.
    humanURL: https://resurface.io
    tags:
      - API Compliance
      - API Logging
      - API Observability
      - API Security
      - Runtime Security
      - Threat Detection
    properties:
      - type: Documentation
        url: https://resurface.io/docs
      - type: GettingStarted
        url: https://resurface.io/docs/getting-started
      - type: HelmChart
        url: https://artifacthub.io/packages/helm/resurfaceio/resurface
      - type: GitHub
        url: https://github.com/resurfaceio
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/resurface/refs/heads/main/json-schema/resurface-api-call-log-schema.json
  - aid: resurface:resurface-logger-go
    name: Resurface Logger for Go
    description: Open-source Go library for logging API requests and responses to the Resurface database. Integrates with gorilla/mux and other Go HTTP frameworks.
    humanURL: https://github.com/resurfaceio/logger-go
    tags:
      - Go
      - Integration
      - Logger
      - SDK
    properties:
      - type: GitHub
        url: https://github.com/resurfaceio/logger-go
  - aid: resurface:resurface-logger-ebpf
    name: Resurface Logger for eBPF
    description: eBPF-based kernel-level API call logger that captures HTTP traffic without application code changes for zero-instrumentation observability.
    humanURL: https://github.com/resurfaceio/logger-ebpf
    tags:
      - eBPF
      - Integration
      - Kubernetes
      - Logger
    properties:
      - type: GitHub
        url: https://github.com/resurfaceio/logger-ebpf
  - aid: resurface:resurface-containers
    name: Resurface Containers
    description: Official Helm charts and container images for deploying the Resurface API security database on Kubernetes.
    humanURL: https://resurfaceio.github.io/containers/
    tags:
      - Containers
      - Docker
      - Helm
      - Kubernetes
    properties:
      - type: Documentation
        url: https://resurfaceio.github.io/containers/
      - type: HelmChart
        url: https://artifacthub.io/packages/helm/resurfaceio/resurface
      - type: GitHub
        url: https://github.com/resurfaceio/containers
  - aid: resurface:resurface-trino-connector
    name: Resurface Trino Connector
    description: Connector for querying Resurface API call data via Trino distributed SQL query engine.
    humanURL: https://github.com/resurfaceio/trino-connector
    tags:
      - Analytics
      - Integration
      - SQL
      - Trino
    properties:
      - type: GitHub
        url: https://github.com/resurfaceio/trino-connector
common:
  - type: Website
    url: https://resurface.io
  - type: Documentation
    url: https://resurface.io/docs
  - type: Blog
    url: https://resurface.io/blog
  - type: GitHub
    url: https://github.com/resurfaceio
  - type: Pricing
    url: https://resurface.io/pricing
  - type: Support
    url: https://resurface.io/support
  - type: Login
    url: https://resurface.io/login
  - type: Twitter
    url: https://twitter.com/resabordeio
  - type: LinkedIn
    url: https://www.linkedin.com/company/resurfacelabs
  - type: HelmChart
    url: https://artifacthub.io/packages/helm/resurfaceio/resurface
  - type: AcquiredBy
    url: https://graylog.org
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/resurface/refs/heads/main/vocabulary/resurface-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
