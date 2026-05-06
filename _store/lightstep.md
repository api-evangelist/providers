---
aid: lightstep
name: Lightstep
description: Lightstep, now ServiceNow Cloud Observability, is a distributed tracing and observability platform that helps teams monitor, debug, and optimize microservice performance. It provides deep visibility into distributed systems using OpenTelemetry-based tracing, metrics, and service health monitoring.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - APM
  - Distributed Tracing
  - Microservices
  - Monitoring
  - Observability
  - OpenTelemetry
url: https://raw.githubusercontent.com/api-evangelist/lightstep/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: lightstep:lightstep-api
    name: Lightstep API
    description: The Lightstep API provides programmatic access to observability data including traces, spans, streams, dashboards, alerting conditions, and service health. It enables teams to manage their observability configuration and query telemetry data programmatically.
    humanURL: https://docs.lightstep.com/docs/lightstep-api-overview
    tags:
      - APM
      - Distributed Tracing
      - Monitoring
      - Observability
      - Telemetry
    properties:
      - type: Documentation
        url: https://docs.lightstep.com/docs/lightstep-api-overview
      - type: OpenAPI
        url: https://docs.lightstep.com/openapi
      - type: GettingStarted
        url: https://docs.lightstep.com/docs/welcome-to-lightstep
      - type: Authentication
        url: https://docs.lightstep.com/docs/create-and-manage-api-keys
common:
  - type: Website
    url: https://lightstep.com
  - type: Documentation
    url: https://docs.lightstep.com
  - type: Blog
    url: https://lightstep.com/blog
  - type: Pricing
    url: https://lightstep.com/pricing
  - type: Login
    url: https://app.lightstep.com
  - type: Signup
    url: https://app.lightstep.com/signup
  - type: Support
    url: https://lightstep.com/support
  - type: GitHub
    url: https://github.com/lightstep
  - type: LinkedIn
    url: https://www.linkedin.com/company/lightstep
  - type: StatusPage
    url: https://status.lightstep.com
  - type: OpenTelemetry
    url: https://docs.lightstep.com/docs/opentelemetry
  - type: Features
    data:
      - Now ServiceNow Cloud Observability after acquisition
      - Community free for evaluation
      - 'Enterprise: custom pricing through ServiceNow'
      - Distributed tracing with intelligent sampling
      - Service maps (Enterprise)
      - Anomaly detection with notebooks
      - OpenTelemetry-native
      - Public API at api.lightstep.com
      - Default 600 req/min/org
      - Span ingest scales with plan
      - Streams (saved span queries)
      - Notebooks for collaborative root-cause analysis
      - ServiceNow ITSM integration (Enterprise)
      - API tokens per project
      - Webhooks for streams and conditions
      - AWS, GCP, Azure cloud support
    sources:
      - https://lightstep.com/
      - https://www.servicenow.com/products/observability.html
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
