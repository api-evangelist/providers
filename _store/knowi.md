---
aid: knowi
name: Knowi
description: Knowi is an analytics and business intelligence platform with native integration to NoSQL, SQL, and REST API data sources, providing AI-powered analytics, embedded dashboards, and natural language querying.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Analytics
  - API Analytics
  - Business Intelligence
  - Data Visualization
  - Embedded Analytics
  - NoSQL Analytics
url: https://raw.githubusercontent.com/api-evangelist/knowi/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: knowi:knowi-management-api
    name: Knowi Management API
    description: The Knowi Management API enables programmatic administration of users, groups, and dashboards in a Knowi workspace using OAuth 2.0 bearer tokens. It supports automation of provisioning, permissions, and embedded dashboard sharing.
    humanURL: https://www.knowi.com/docs/managementAPI.html
    properties:
      - type: Documentation
        url: https://www.knowi.com/docs/managementAPI.html
      - type: APIDocumentation
        url: https://www.knowi.com/docs/managementAPI.html
      - type: OpenAPI
        url: openapi/knowi-management-api-openapi.yml
    tags:
      - Administration
      - Business Intelligence
      - Dashboards
      - Embedded Analytics
  - aid: knowi:knowi-push-data-api
    name: Knowi Push Data API
    description: The Knowi Push Data API enables real-time data ingestion to and pull retrieval from Knowi datasets. Push data over HTTP to create or update datasets on the fly, and query results back with SQL-like filters and multiple export formats.
    humanURL: https://www.knowi.com/docs/pushApi.html
    properties:
      - type: Documentation
        url: https://www.knowi.com/docs/pushApi.html
      - type: APIDocumentation
        url: https://www.knowi.com/docs/pushApi.html
      - type: OpenAPI
        url: openapi/knowi-push-data-api-openapi.yml
    tags:
      - Data Ingestion
      - Real-Time
      - Streaming
common:
  - type: Website
    url: https://www.knowi.com
  - type: Documentation
    url: https://www.knowi.com/docs
  - type: Blog
    url: https://www.knowi.com/blog
  - type: Pricing
    url: https://www.knowi.com/pricing
  - type: Login
    url: https://www.knowi.com/login
  - type: Signup
    url: https://www.knowi.com/signup
  - type: Support
    url: https://www.knowi.com/support
  - type: Integrations
    url: https://www.knowi.com/integrations
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
