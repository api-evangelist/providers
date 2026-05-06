---
aid: fluent-bit
name: Fluent Bit
description: Fluent Bit is an open source lightweight log processor and forwarder for collecting, parsing, and routing logs and metrics at scale. It exposes an embedded HTTP monitoring server with v1 and v2 endpoints for build info, uptime, internal metrics (JSON, Prometheus, cmetrics), storage stats, health checks, and hot reload.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Logging
  - Observability
  - Metrics
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/fluent-bit/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: fluent-bit:fluent-bit-monitoring-http-api
    name: Fluent Bit Monitoring HTTP API
    description: Fluent Bit's embedded HTTP server (default port 2020) exposes endpoints for build information, uptime, internal plugin metrics in JSON, Prometheus, and cmetrics formats, storage layer statistics, health checks, and hot reload.
    humanURL: https://docs.fluentbit.io/manual/administration/monitoring
    baseURL: http://127.0.0.1:2020
    tags:
      - Logging
      - Observability
      - Metrics
      - Health Check
      - Prometheus
    properties:
      - type: Documentation
        url: https://docs.fluentbit.io/manual/administration/monitoring
      - type: OpenAPI
        url: openapi/fluent-bit-monitoring-openapi.yml
common:
  - type: Website
    url: https://fluentbit.io
  - type: Documentation
    url: https://docs.fluentbit.io
  - type: GitHub Repository
    url: https://github.com/fluent/fluent-bit
  - type: Slack
    url: https://launchpass.com/fluent-all
  - type: Community
    url: https://fluentbit.io/community/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
