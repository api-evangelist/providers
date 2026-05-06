---
aid: google-cloud-trace
name: Google Cloud Trace
description: Google Cloud Trace is a distributed tracing system that collects latency data from applications and displays it in near real-time. It helps developers understand how requests propagate through their application, identify performance bottlenecks, and analyze latency across microservices and distributed architectures running on Google Cloud.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-trace/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Distributed Tracing
  - Google Cloud
  - Latency
  - Observability
  - Performance
  - Spans
  - Tracing
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
common:
  - type: Portal
    url: https://cloud.google.com/trace
  - type: Getting Started
    url: https://cloud.google.com/trace/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/trace/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/trace/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/trace/docs/support
  - type: JSONLDContext
    url: json-ld/json-ld.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
