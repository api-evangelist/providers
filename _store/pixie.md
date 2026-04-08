---
aid: pixie
url: https://raw.githubusercontent.com/api-evangelist/pixie/refs/heads/main/apis.yml
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
name: Pixie
tags:
- eBPF
- Kubernetes
- Monitoring
- Observability
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Pixie is a Kubernetes observability platform that uses eBPF to automatically collect telemetry data including full-body application requests, resource and network metrics, and application profiles without manual instrumentation.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

