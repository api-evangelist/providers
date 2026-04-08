---
aid: grafana-tempo
url: https://raw.githubusercontent.com/api-evangelist/grafana-tempo/refs/heads/main/apis.yml
apis:
- aid: grafana-tempo:tempo-http-api
  name: Grafana Tempo HTTP API
  description: Grafana Tempo HTTP API for querying traces, searching with TraceQL, retrieving tag names and values, and computing metrics summaries from distributed trace data.
  humanURL: https://grafana.com/docs/tempo/latest/api_docs/
  tags:
  - Distributed Tracing
  - Observability
  - Search
  - TraceQL
  - Traces
  properties:
  - type: Documentation
    url: https://grafana.com/docs/tempo/latest/api_docs/
  - type: OpenAPI
    url: openapi/tempo-http-api.yml
  - type: JSONSchema
    url: json-schema/trace.yml
name: Grafana Tempo
tags:
- Distributed Tracing
- Grafana
- Microservices
- Observability
- Open Source
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Grafana Tempo is an open-source, high-scale distributed tracing backend that requires only object storage to operate, making it cost-effective and easy to run. It integrates deeply with Grafana, Prometheus, and Loki for seamless observability across metrics, logs, and traces.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

