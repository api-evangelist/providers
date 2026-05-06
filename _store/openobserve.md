---
aid: openobserve
name: OpenObserve
description: OpenObserve is an open source petabyte-scale observability platform with unified logs, metrics, traces, and front-end telemetry in a single UI with SQL and PromQL querying. The HTTP API exposes ingestion, search, alerting, dashboards, pipelines, RUM, and administration endpoints.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/openobserve/refs/heads/main/apis.yml
tags:
  - Observability
  - Logs
  - Metrics
  - Traces
  - RUM
  - Open Source
created: '2026-03-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: openobserve:openobserve
    name: OpenObserve
    description: OpenObserve HTTP API for ingesting logs, metrics, and traces; running SQL and PromQL search; managing alerts, dashboards, folders, pipelines, reports, RUM, saved views, service streams, and short URLs; and administering organizations, users, roles, groups, service accounts, rate limits, and meta resources.
    humanURL: https://openobserve.ai
    baseURL: https://api.openobserve.ai
    tags:
      - Observability
      - Logs
      - Metrics
      - Traces
      - RUM
      - Search
      - Alerts
      - Dashboards
      - Pipelines
    properties:
      - type: Documentation
        url: https://openobserve.ai/docs/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/openobserve/refs/heads/main/openapi/openobserve-openapi.json
      - type: SwaggerUI
        url: https://api.openobserve.ai/swagger/
      - type: GitHubRepository
        url: https://github.com/openobserve/openobserve
common:
  - type: Website
    name: OpenObserve Website
    url: https://openobserve.ai
  - type: Documentation
    name: OpenObserve Documentation
    url: https://openobserve.ai/docs/
  - type: GitHubOrg
    name: OpenObserve GitHub
    url: https://github.com/openobserve
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
