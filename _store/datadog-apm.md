---
aid: datadog-apm
url: https://raw.githubusercontent.com/api-evangelist/datadog-apm/refs/heads/main/apis.yml
apis:
- aid: datadog-apm:datadog-apm-api
  name: Datadog APM API
  description: Datadog APM REST API for traces, spans, services, service definitions, and SLOs. Provides endpoints for searching traces, managing service catalog entries, and configuring service level objectives.
  humanURL: https://docs.datadoghq.com/api/latest/tracing/
  tags:
  - APM
  - Distributed Tracing
  - Service Definitions
  - SLOs
  - Spans
  - Traces
  properties:
  - type: Documentation
    url: https://docs.datadoghq.com/api/latest/tracing/
  - type: OpenAPI
    url: openapi/datadog-apm-api.yml
  - type: JSONSchema
    url: json-schema/trace.yml
name: Datadog APM
tags:
- APM
- Distributed Tracing
- Microservices
- Observability
- Performance Monitoring
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Datadog APM provides end-to-end distributed tracing, continuous profiling, and real-time performance monitoring for applications and microservices. It automatically instruments applications to provide deep visibility into request traces, latency, and error rates across distributed systems.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

