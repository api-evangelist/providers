---
aid: argus
url: https://raw.githubusercontent.com/api-evangelist/argus/refs/heads/main/apis.yml
apis:
- name: Argus Monitoring API
  description: Core API for managing monitors, metrics, and alerts in Argus.
  image: https://example.com/argus-api-icon.png
  humanURL: https://argus.example.com/docs
  baseURL: https://api.argus.example.com/v1
  tags:
  - Alerts
  - Metrics
  - Monitoring
  - Observability
  properties:
  - type: Documentation
    url: https://argus.example.com/docs/api
  - type: OpenAPI
    url: https://api.argus.example.com/v1/openapi.json
  - type: Authentication
    url: https://argus.example.com/docs/authentication
  - type: RateLimits
    url: https://argus.example.com/docs/rate-limits
  contact:
  - type: Support
    url: https://argus.example.com/support
  - type: Email
    url: mailto:support@argus.example.com
- name: Argus Alerts API
  description: API for creating, managing, and receiving alerts.
  humanURL: https://argus.example.com/docs/alerts
  baseURL: https://api.argus.example.com/v1/alerts
  tags:
  - Alerts
  - Incidents
  - Notifications
  properties:
  - type: Documentation
    url: https://argus.example.com/docs/alerts-api
  - type: Webhooks
    url: https://argus.example.com/docs/webhooks
- name: Argus Metrics API
  description: API for submitting and querying time-series metrics data.
  humanURL: https://argus.example.com/docs/metrics
  baseURL: https://api.argus.example.com/v1/metrics
  tags:
  - Analytics
  - Metrics
  - Time-Series
  properties:
  - type: Documentation
    url: https://argus.example.com/docs/metrics-api
  - type: Examples
    url: https://argus.example.com/docs/metrics-examples
name: Argus
tags:
- Alerts
- Metrics
- Monitoring
- Observability
- SaaS
type: Contract
image: https://example.com/argus-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for the Argus monitoring and alerting platform.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

