---
aid: sumo-logic
name: Sumo Logic
description: Sumo Logic is a cloud-native, machine data analytics platform delivering real-time, continuous intelligence for operations, security, and business insights. It provides a comprehensive REST API with 289 endpoints spanning log analytics, dashboards, monitors, roles, users, metrics, traces, and more.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Logging
  - Observability
  - Security
  - Monitoring
  - Analytics
  - DevOps
  - SIEM
url: https://raw.githubusercontent.com/api-evangelist/sumo-logic/refs/heads/main/apis.yml
created: '2025-01-08'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: sumo-logic:sumo-logic
    name: Sumo Logic API
    description: Sumo Logic REST API providing 289 endpoints for managing log analytics, users, roles, dashboards, monitors, connections, collectors, sources, search jobs, ingest budgets, partitions, field extraction, metrics, traces, and security operations. Uses Basic Auth with Access ID and Key.
    humanURL: https://help.sumologic.com/docs/api/
    baseURL: https://api.sumologic.com/api
    tags:
      - Logging
      - Observability
      - Security
      - Monitoring
      - Analytics
      - Users
      - Roles
      - Dashboards
    properties:
      - type: Documentation
        url: https://help.sumologic.com/docs/api/
      - type: Reference
        url: https://api.sumologic.com/docs/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sumo-logic/refs/heads/main/openapi/sumo-logic-openapi.yml
      - type: GettingStarted
        url: https://help.sumologic.com/docs/api/about-apis/getting-started/
common:
  - type: Portal
    url: https://developer.sumologic.com/
  - type: Documentation
    url: https://help.sumologic.com/docs/api/
  - type: Reference
    url: https://api.sumologic.com/docs/
  - type: Website
    url: https://www.sumologic.com/
  - type: GettingStarted
    url: https://help.sumologic.com/docs/api/about-apis/getting-started/
  - type: Status
    url: https://status.sumologic.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
