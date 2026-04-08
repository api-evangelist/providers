---
aid: zipkin
url: https://raw.githubusercontent.com/api-evangelist/zipkin/refs/heads/main/apis.yml
apis:
- aid: zipkin:zipkin-api-v2
  name: Zipkin API V2
  description: Zipkin's v2 HTTP API for querying and collecting distributed traces. Provides endpoints for submitting spans, querying traces, looking up services and span names, and retrieving dependency links between services.
  humanURL: https://zipkin.io/zipkin-api/
  tags:
  - Dependencies
  - Distributed Tracing
  - Observability
  - Spans
  - Traces
  properties:
  - type: Documentation
    url: https://zipkin.io/zipkin-api/
  - type: GitHub Repository
    url: https://github.com/openzipkin/zipkin
  - type: OpenAPI
    url: openapi/zipkin-api-v2.yml
  - type: JSONSchema
    url: json-schema/span.yml
name: Zipkin
tags:
- Distributed Tracing
- Observability
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Zipkin is an open source distributed tracing system for gathering timing data to troubleshoot latency problems in microservice architectures.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

