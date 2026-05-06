---
aid: signoz
name: SigNoz
description: SigNoz is an open source observability platform with logs, traces, and metrics in a single pane, built natively on OpenTelemetry. It is a full-stack open-source APM and observability tool that serves as an open-source alternative to DataDog, NewRelic, and other proprietary monitoring solutions. SigNoz provides distributed tracing, log management, infrastructure monitoring, and alerting capabilities unified under a single interface.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - APM
  - Alerting
  - Cloud Monitoring
  - Dashboards
  - Distributed Tracing
  - Infrastructure Monitoring
  - Logs
  - Metrics
  - Observability
  - OpenTelemetry
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/signoz/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: signoz:signoz
    name: SigNoz
    description: The SigNoz REST API provides programmatic access to the SigNoz observability platform. The API enables management of alerts, dashboards, notification channels, cloud integrations, users, organizations, service accounts, and ingestion keys. It also exposes query endpoints for traces, logs, metrics, and infrastructure monitoring data. The API uses API key authentication via the SigNoz-Api-Key header.
    humanURL: https://signoz.io
    baseURL: https://{host}:{port}
    tags:
      - APM
      - Alerting
      - Dashboards
      - Distributed Tracing
      - Logs
      - Metrics
      - Observability
      - OpenTelemetry
    properties:
      - type: Documentation
        url: https://signoz.io/docs/
      - type: API Reference
        url: https://signoz.io/api-reference/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/signoz/refs/heads/main/openapi/signoz-openapi.yml
      - type: GitHub Repository
        url: https://github.com/SigNoz/signoz
      - type: Pricing
        url: https://signoz.io/pricing/
      - type: Getting Started
        url: https://signoz.io/docs/introduction/
      - type: Changelog
        url: https://signoz.io/changelog/
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/signoz/refs/heads/main/rules/signoz-rules.yml
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/signoz/refs/heads/main/vocabulary/signoz-vocabulary.yml
common:
  - type: Website
    url: https://signoz.io
  - type: Documentation
    url: https://signoz.io/docs/
  - type: API Reference
    url: https://signoz.io/api-reference/
  - type: GitHub Organization
    url: https://github.com/SigNoz
  - type: Blog
    url: https://signoz.io/blog/
  - type: Pricing
    url: https://signoz.io/pricing/
  - type: Support
    url: https://signoz.io/support/
  - type: Community
    url: https://signoz.io/slack/
  - type: Enterprise
    url: https://signoz.io/enterprise/
  - type: Changelog
    url: https://signoz.io/changelog/
  - type: Status
    url: https://status.signoz.io/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
