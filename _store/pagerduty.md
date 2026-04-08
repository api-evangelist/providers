---
aid: pagerduty
url: https://raw.githubusercontent.com/api-evangelist/pagerduty/refs/heads/main/apis.yml
apis:
- aid: pagerduty:pagerduty-rest-api
  name: PagerDuty REST API
  description: The PagerDuty REST API provides programmatic access to PagerDuty incidents, services, escalation policies, schedules, and users.
  humanURL: https://developer.pagerduty.com/api-reference/
  baseURL: https://api.pagerduty.com
  tags:
  - Alerting
  - Incidents
  - On-Call
  properties:
  - type: Documentation
    url: https://developer.pagerduty.com/api-reference/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/PagerDuty/api-schema/main/reference/REST/openapiv3.json
  - type: Authentication
    url: https://developer.pagerduty.com/docs/authentication
  - type: Getting Started
    url: https://developer.pagerduty.com/docs/rest-api-v2/rest-api/
- aid: pagerduty:pagerduty-events-api
  name: PagerDuty Events API
  description: The PagerDuty Events API is a system for triggering, acknowledging, and resolving alerts from monitoring tools and other data sources.
  humanURL: https://developer.pagerduty.com/docs/events-api-v2/overview/
  baseURL: https://events.pagerduty.com
  tags:
  - Alerting
  - Events
  - Monitoring
  properties:
  - type: Documentation
    url: https://developer.pagerduty.com/docs/events-api-v2/overview/
  - type: Getting Started
    url: https://developer.pagerduty.com/docs/events-api-v2/send-an-alert/
name: PagerDuty
tags:
- Alerting
- DevOps
- Incident Management
- On-Call Management
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: PagerDuty is a digital operations management platform that helps teams detect problems and resolve incidents with automated alerting, on-call management, and incident response workflows.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

