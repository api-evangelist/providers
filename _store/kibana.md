---
aid: kibana
name: Kibana
description: Kibana is an open-source data visualization and exploration tool used for log and time-series analytics, application monitoring, and operational intelligence. Kibana provides histograms, line graphs, pie charts, heat maps, geospatial visualizations, dashboards, alerting, and management of saved objects across spaces, exposing a comprehensive REST API for programmatic configuration and automation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Alerting
  - Analytics
  - Dashboards
  - Elastic Stack
  - Logging
  - Monitoring
  - Observability
  - Visualization
url: https://raw.githubusercontent.com/api-evangelist/kibana/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kibana:kibana-api
    name: Kibana API
    description: The Kibana REST API enables programmatic management of Kibana resources including spaces, saved objects, dashboards, data views, connectors, rules, and configuration. The API is stateless and uses standard HTTP verbs (GET, POST, PUT, DELETE) returning JSON responses, making it well suited for automation, CI/CD pipelines, and integrating Kibana with external systems.
    humanURL: https://www.elastic.co/guide/en/kibana/current/api.html
    baseURL: https://localhost:5601/api
    tags:
      - Configuration
      - Dashboards
      - Management
      - Saved Objects
      - Spaces
    properties:
      - type: Documentation
        url: https://www.elastic.co/guide/en/kibana/current/api.html
      - type: OpenAPI
        url: openapi/kibana-openapi-original.yml
      - type: Authentication
        url: https://www.elastic.co/guide/en/kibana/current/api-authentication.html
common:
  - type: Website
    url: https://www.elastic.co/kibana
  - type: Documentation
    url: https://www.elastic.co/guide/en/kibana/current/index.html
  - type: APIDocumentation
    url: https://www.elastic.co/guide/en/kibana/current/api.html
  - type: Downloads
    url: https://www.elastic.co/downloads/kibana
  - type: GitHub
    url: https://github.com/elastic/kibana
  - type: Blog
    url: https://www.elastic.co/blog/category/kibana
  - type: Pricing
    url: https://www.elastic.co/pricing
  - type: Support
    url: https://www.elastic.co/support
  - type: Forum
    url: https://discuss.elastic.co/c/kibana
  - type: TermsOfService
    url: https://www.elastic.co/legal/terms-of-service
  - type: PrivacyPolicy
    url: https://www.elastic.co/legal/privacy-statement
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
