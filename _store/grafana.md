---
aid: grafana
url: >-
  https://raw.githubusercontent.com/api-evangelist/grafana/refs/heads/main/apis.yml
apis:
  - aid: grafana:grafana
    name: Grafana
    tags:
      - Analytics
      - Visualizations
      - Monitoring
      - Analysis
    humanURL: https://grafana.com
    properties:
      - url: https://grafana.com
        type: Documentation
      - url: openapi/grafana-openapi.yml
        type: OpenAPI
    description: >-
      Grafana is an open-source analytics and visualization platform that helps
      you monitor and analyze data from various sources. It lets you create
      customizable dashboards with charts, graphs, and alerts to visualize
      metrics and logs in real-time. Commonly used for monitoring
      infrastructure, applications, and business metrics, Grafana connects to
      dozens of data sources like Prometheus, Elasticsearch, and cloud
      platforms, making it easier to understand system performance, troubleshoot
      issues, and track key indicators all in one place.
name: Grafana
tags:
  - Observability
  - Analytics
  - Role-Based Access Control
  - RBAC
  - Platform
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2025-12-28'
position: Consumer
description: >-
  RBAC API Role-based access control API is only available in Grafana Cloud or
  Grafana Enterprise. Read more about Grafana Enterprise. The API can be used to
  ...
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---