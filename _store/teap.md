---
aid: teap
url: https://raw.githubusercontent.com/api-evangelist/teap/refs/heads/main/apis.yml
apis:
- name: Teap Core API
  description: Main API for Teap platform operations including user management, authentication, and core functionality.
  image: https://teap.io/images/api-logo.png
  humanURL: https://teap.io/docs
  baseURL: https://api.teap.io/v1
  tags:
  - Collaboration
  - Productivity
  - Teams
  - Workspace
  properties:
  - type: Documentation
    url: https://docs.teap.io/api
  - type: OpenAPI
    url: https://api.teap.io/v1/openapi.json
  - type: Swagger
    url: https://api.teap.io/v1/swagger
  - type: Authentication
    url: https://docs.teap.io/api/authentication
  contact:
  - type: Email
    url: mailto:api@teap.io
  - type: Support
    url: https://support.teap.io
  - type: Twitter
    url: https://twitter.com/teap
- name: Teap Webhooks API
  description: Webhook management and event notification system.
  baseURL: https://webhooks.teap.io/v1
  tags:
  - Events
  - Notifications
  - Webhooks
  properties:
  - type: Documentation
    url: https://docs.teap.io/webhooks
  - type: OpenAPI
    url: https://webhooks.teap.io/v1/openapi.json
- name: Teap Analytics API
  description: Analytics and reporting endpoints for workspace insights.
  baseURL: https://analytics.teap.io/v1
  tags:
  - Analytics
  - Metrics
  - Reporting
  properties:
  - type: Documentation
    url: https://docs.teap.io/analytics
  - type: OpenAPI
    url: https://analytics.teap.io/v1/openapi.json
name: Teap
tags:
- Collaboration
- Productivity
- Teams
- Workspace
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: API definitions for Teap platform services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

