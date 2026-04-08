---
aid: google-cloud-trace
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-trace/refs/heads/main/apis.yml
apis:
- name: Google Cloud Trace API
  description: The Cloud Trace API enables sending and retrieving latency data for distributed applications. The v2 API supports writing trace spans via batchWrite and createSpan methods, while the v1 API supports both reading and writing trace data including listing and getting traces.
  humanURL: https://cloud.google.com/trace/docs
  baseURL: https://cloudtrace.googleapis.com
  properties:
  - type: Documentation
    url: https://cloud.google.com/trace/docs/reference/v2/rest
  - type: OpenAPI
    url: openapi/openapi.yml
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Getting Started
    url: https://cloud.google.com/trace/docs/quickstart
  - type: JSONSchema
    url: json-schema/json-schema.yml
  - type: JSONLDContext
    url: json-ld/json-ld.yml
name: Google Cloud Trace
tags:
- Distributed Tracing
- Google Cloud
- Latency
- Observability
- Performance
- Spans
- Tracing
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Trace is a distributed tracing system that collects latency data from applications and displays it in near real-time. It helps developers understand how requests propagate through their application, identify performance bottlenecks, and analyze latency across microservices and distributed architectures running on Google Cloud.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

