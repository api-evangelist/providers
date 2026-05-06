---
aid: tableaux-de-bord
name: Tableaux De Bord
description: Tableaux de Bord (French for "dashboards") is an API industry topic covering dashboard and data visualization APIs. The landscape includes open-source platforms such as Grafana (with its comprehensive HTTP API for dashboards, datasources, and alerting) and Metabase (with its REST API for questions, dashboards, and administration). These tools enable programmatic creation and management of business intelligence dashboards for monitoring, analytics, and operational visibility.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Dashboards
  - Business Intelligence
  - Analytics
  - Data Visualization
  - Monitoring
  - Grafana
  - Metabase
url: https://raw.githubusercontent.com/api-evangelist/tableaux-de-bord/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tableaux-de-bord:grafana
    name: Grafana HTTP API
    description: The Grafana HTTP API provides programmatic access to Grafana's dashboard, datasource, alerting, organization, user, and annotation management capabilities. Grafana is an open-source observability and analytics platform widely used for infrastructure and application monitoring.
    humanURL: https://grafana.com/docs/grafana/latest/developer-resources/api-reference/http-api/
    baseURL: https://your-grafana-instance.com
    tags:
      - Grafana
      - Dashboards
      - Monitoring
      - Observability
    properties:
      - type: Documentation
        url: https://grafana.com/docs/grafana/latest/developer-resources/api-reference/http-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/tableaux-de-bord/refs/heads/main/openapi/grafana-dashboard-openapi.yml
      - type: GitHub
        url: https://github.com/grafana/grafana
  - aid: tableaux-de-bord:metabase
    name: Metabase API
    description: The Metabase REST API enables automation of business intelligence workflows including creating and managing dashboards, running questions (queries), managing users and groups, and embedding analytics in applications.
    humanURL: https://www.metabase.com/learn/metabase-basics/administration/administration-and-operation/metabase-api
    baseURL: https://your-metabase-instance.com
    tags:
      - Metabase
      - Business Intelligence
      - Analytics
      - Dashboards
    properties:
      - type: Documentation
        url: https://www.metabase.com/learn/metabase-basics/administration/administration-and-operation/metabase-api
      - type: GitHub
        url: https://github.com/metabase/metabase
common:
  - type: Grafana Website
    url: https://grafana.com/
  - type: Metabase Website
    url: https://www.metabase.com/
  - type: Grafana Documentation
    url: https://grafana.com/docs/grafana/latest/developer-resources/api-reference/http-api/
  - type: Metabase Documentation
    url: https://www.metabase.com/learn/metabase-basics/administration/administration-and-operation/metabase-api
  - type: Grafana GitHub
    url: https://github.com/grafana/grafana
  - type: Metabase GitHub
    url: https://github.com/metabase/metabase
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/tableaux-de-bord/refs/heads/main/vocabulary/tableaux-de-bord-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
