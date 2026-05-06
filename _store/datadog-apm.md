---
aid: datadog-apm
name: Datadog APM
description: Datadog APM provides end-to-end distributed tracing, continuous profiling, and real-time performance monitoring for applications and microservices. It automatically instruments applications to provide deep visibility into request traces, latency, and error rates across distributed systems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - APM
  - Distributed Tracing
  - Microservices
  - Observability
  - Performance Monitoring
url: https://raw.githubusercontent.com/api-evangelist/datadog-apm/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
position: Consumer
access: 3rd-Party
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
common:
  - type: Website
    url: https://www.datadoghq.com/
  - type: Documentation
    url: https://docs.datadoghq.com/tracing/
  - type: Getting Started
    url: https://docs.datadoghq.com/getting_started/tracing/
  - type: GitHub
    url: https://github.com/DataDog
  - type: Blog
    url: https://www.datadoghq.com/blog/
  - type: Pricing
    url: https://www.datadoghq.com/pricing/
  - type: Sign Up
    url: https://www.datadoghq.com/free-datadog-trial/
  - type: JSON-LD
    url: json-ld/datadog-apm-context.jsonld
  - type: Vocabulary
    url: vocabulary/datadog-apm-vocabulary.yml
  - type: Capabilities
    url: capabilities/datadog-apm-capabilities.yml
  - type: Rules
    url: rules/datadog-apm-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
