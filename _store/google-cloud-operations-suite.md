---
aid: google-cloud-operations-suite
name: Google Cloud Operations Suite
description: Google Cloud Operations Suite (formerly Stackdriver) provides integrated monitoring, logging, and diagnostics for applications and infrastructure running on Google Cloud. It encompasses Cloud Monitoring, Cloud Logging, Cloud Trace, Cloud Profiler, and Error Reporting to deliver comprehensive observability, real-time visibility, alerting, log analysis, distributed tracing, and performance profiling across cloud environments.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-operations-suite/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Error Reporting
  - Google Cloud
  - Logging
  - Monitoring
  - Observability
  - Operations
  - Profiling
  - Stackdriver
  - Tracing
apis:
  - name: Google Cloud Operations Suite API
    description: The Operations Suite API provides a unified interface for managing observability across Google Cloud services, including monitoring metrics and dashboards, centralized logging, distributed tracing, continuous profiling, and automated error reporting. It integrates the capabilities of Cloud Monitoring, Cloud Logging, Cloud Trace, Cloud Profiler, and Error Reporting into a cohesive operations platform.
    humanURL: https://cloud.google.com/products/operations
    baseURL: https://monitoring.googleapis.com
    properties:
      - type: Documentation
        url: https://cloud.google.com/monitoring/docs/reference/v3/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://cloud.google.com/docs/authentication
      - type: Getting Started
        url: https://cloud.google.com/monitoring/docs/quickstart
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLDContext
        url: json-ld/json-ld.yml
common:
  - type: Portal
    url: https://cloud.google.com/products/operations
  - type: Getting Started
    url: https://cloud.google.com/monitoring/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/products/operations
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/stackdriver/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/support
  - type: JSONLDContext
    url: json-ld/json-ld.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
