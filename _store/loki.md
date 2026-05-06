---
aid: loki
name: Loki
description: Loki is an open source log aggregation system from Grafana Labs designed to store and query logs efficiently using labels instead of full-text indexing.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Logging
  - Observability
  - Open Source
  - Grafana
url: https://raw.githubusercontent.com/api-evangelist/loki/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: loki:loki-http-api
    name: Loki HTTP API
    description: The Loki HTTP API supports pushing logs, querying with LogQL, range queries, label discovery, series retrieval, index stats and volume, pattern detection, log tailing, deletion, and ruler operations. There is no published OpenAPI specification; see Grafana's HTTP API reference for endpoint details.
    humanURL: https://grafana.com/docs/loki/latest/reference/loki-http-api/
    tags:
      - Logging
      - Observability
      - HTTP API
    properties:
      - type: Documentation
        url: https://grafana.com/docs/loki/latest/reference/loki-http-api/
      - type: GitHub Repository
        url: https://github.com/grafana/loki
common:
  - type: Website
    url: https://grafana.com/oss/loki/
  - type: Documentation
    url: https://grafana.com/docs/loki/latest/
  - type: GitHub Organization
    url: https://github.com/grafana
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
