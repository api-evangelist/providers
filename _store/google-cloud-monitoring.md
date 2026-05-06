---
aid: google-cloud-monitoring
name: Google Cloud Monitoring
description: Google Cloud Monitoring provides comprehensive monitoring and observability for cloud infrastructure and applications. It collects metrics, events, and metadata from Google Cloud services, hosted uptime probes, and application instrumentation, enabling dashboards, alerting, uptime monitoring, and service level objective tracking.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-monitoring/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Alerting
  - Dashboards
  - Google Cloud
  - Metrics
  - Monitoring
  - Observability
  - SLO
  - Uptime
apis:
  - name: Google Cloud Monitoring API
    description: The Cloud Monitoring API provides programmatic access to time series data, alert policies, notification channels, uptime checks, dashboards, metric descriptors, monitored resource descriptors, and service level objectives for comprehensive infrastructure and application monitoring.
    humanURL: https://cloud.google.com/monitoring/docs
    baseURL: https://monitoring.googleapis.com
    properties:
      - type: Documentation
        url: https://cloud.google.com/monitoring/docs/reference/v3/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://cloud.google.com/monitoring/docs/access-control
      - type: Getting Started
        url: https://cloud.google.com/monitoring/docs/quickstart
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLDContext
        url: json-ld/json-ld.yml
common:
  - type: Portal
    url: https://cloud.google.com/monitoring
  - type: Getting Started
    url: https://cloud.google.com/monitoring/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/monitoring/docs
  - type: Authentication
    url: https://cloud.google.com/monitoring/docs/access-control
  - type: Pricing
    url: https://cloud.google.com/monitoring/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/monitoring/docs/support
  - type: JSONLDContext
    url: json-ld/json-ld.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
