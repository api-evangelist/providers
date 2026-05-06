---
aid: pixie
name: Pixie
description: Pixie is a Kubernetes observability platform that uses eBPF to automatically collect telemetry data including full-body application requests, resource and network metrics, and application profiles without manual instrumentation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - eBPF
  - Kubernetes
  - Monitoring
  - Observability
url: https://raw.githubusercontent.com/api-evangelist/pixie/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-03-18'
specificationVersion: '0.19'
apis:
  - aid: pixie:pixie
    name: Pixie API
    description: Kubernetes observability platform using eBPF for automatic telemetry collection without manual instrumentation.
    humanURL: https://docs.px.dev/
    tags:
      - Kubernetes
      - Observability
    properties:
      - type: Documentation
        url: https://docs.px.dev/
      - type: Getting Started
        url: https://docs.px.dev/installing-pixie/
      - type: Reference
        url: https://docs.px.dev/reference/api/overview/
      - type: Client Libraries
        url: https://docs.px.dev/reference/api/
      - type: OpenAPI
        url: openapi/pixie-openapi.yml
  - aid: pixie:pixie-pxl-api
    name: Pixie PxL Script API
    description: Python-dialect domain-specific language and API for querying and analyzing telemetry data collected by Pixie within a Kubernetes cluster. PxL scripts allow developers to filter, aggregate, and visualize metrics, traces, and full-body request data collected via eBPF.
    humanURL: https://docs.px.dev/reference/pxl/
    tags:
      - eBPF
      - Kubernetes
      - Metrics
      - Observability
      - Scripting
    properties:
      - type: Documentation
        url: https://docs.px.dev/reference/pxl/
      - type: Reference
        url: https://docs.px.dev/reference/pxl/
      - type: JSONSchema
        url: json-schema/pixie-pxl-script-schema.json
  - aid: pixie:pixie-plugin-api
    name: Pixie Plugin System API
    description: Plugin API that allows configuring PxL scripts to export observability data from Pixie at regularly scheduled intervals to external systems. Supports integrations including a Grafana datasource plugin for visualizing Pixie data in Grafana dashboards.
    humanURL: https://docs.px.dev/reference/plugins/plugin-system/
    tags:
      - Grafana
      - Integrations
      - Kubernetes
      - Observability
      - Plugins
    properties:
      - type: Documentation
        url: https://docs.px.dev/reference/plugins/plugin-system/
      - type: Reference
        url: https://docs.px.dev/reference/plugins/grafana/
      - type: JSONSchema
        url: json-schema/pixie-plugin-schema.json
common:
  - type: Website
    url: https://px.dev/
  - type: JSON-LD
    url: json-ld/pixie-context.jsonld
  - type: JSONSchema
    url: json-schema/pixie-pxl-script-schema.json
  - type: JSONSchema
    url: json-schema/pixie-plugin-schema.json
  - type: Documentation
    url: https://docs.px.dev/
  - type: Getting Started
    url: https://docs.px.dev/installing-pixie/
  - type: GitHub Organization
    url: https://github.com/pixie-io
  - type: GitHubRepository
    url: https://github.com/pixie-io/pixie
  - type: Blog
    url: https://blog.px.dev/
  - type: Community
    url: https://px.dev/community/
  - type: Slack
    url: https://slackin.px.dev/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
