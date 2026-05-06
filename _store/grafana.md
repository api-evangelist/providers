---
aid: grafana
name: Grafana
description: Grafana is the open-source analytics and monitoring platform that connects to a wide range of data sources including Prometheus, Loki, Elasticsearch, InfluxDB, MySQL, PostgreSQL, and cloud providers. It provides a comprehensive HTTP API for managing dashboards, data sources, alert rules, users, organizations, folders, annotations, and teams.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://grafana.com
created: '2025-01-01'
modified: '2026-03-16'
specificationVersion: '0.19'
type: Index
tags:
  - Alerting
  - Analytics
  - Dashboards
  - Logs
  - Metrics
  - Monitoring
  - Observability
  - Traces
  - Visualization
apis:
  - name: Grafana HTTP API
    description: RESTful API for managing Grafana resources including dashboards, data sources, alert rules, users, organizations, folders, annotations, and teams. Supports authentication via API keys, basic auth, and OAuth tokens.
    humanURL: https://grafana.com/docs/grafana/latest/developers/http_api/
    baseURL: http://localhost:3000/api
    tags:
      - Alerts
      - Annotations
      - Dashboards
      - Data Sources
      - Folders
      - Organizations
      - Teams
      - Users
    properties:
      - type: Documentation
        url: https://grafana.com/docs/grafana/latest/developers/http_api/
      - type: OpenAPI
        url: openapi/grafana-api.yml
      - type: Authentication
        url: https://grafana.com/docs/grafana/latest/administration/service-accounts/
      - type: Getting Started
        url: https://grafana.com/docs/grafana/latest/getting-started/
      - type: JSONSchema
        url: json-schema/dashboard.json
common:
  - type: Portal
    url: https://grafana.com
  - type: Getting Started
    url: https://grafana.com/docs/grafana/latest/getting-started/
  - type: Documentation
    url: https://grafana.com/docs/grafana/latest/
  - type: Authentication
    url: https://grafana.com/docs/grafana/latest/administration/service-accounts/
  - type: Pricing
    url: https://grafana.com/pricing/
  - type: Terms of Service
    url: https://grafana.com/legal/terms/
  - type: Privacy Policy
    url: https://grafana.com/legal/privacy-policy/
  - type: Status
    url: https://status.grafana.com/
  - type: Support
    url: https://grafana.com/support/
  - type: Blog
    url: https://grafana.com/blog/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
