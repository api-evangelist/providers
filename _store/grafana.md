---
aid: grafana
url: https://raw.githubusercontent.com/api-evangelist/grafana/refs/heads/main/apis.yml
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
name: Grafana
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
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-07'
position: Consumer
description: Grafana is the open-source analytics and monitoring platform that connects to a wide range of data sources including Prometheus, Loki, Elasticsearch, InfluxDB, MySQL, PostgreSQL, and cloud providers. It provides a comprehensive HTTP API for managing dashboards, data sources, alert rules, users, organizations, folders, annotations, and teams.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

