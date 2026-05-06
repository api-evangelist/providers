---
aid: pagerduty
name: PagerDuty
description: PagerDuty is a digital operations management platform that helps teams detect problems and resolve incidents with automated alerting, on-call management, and incident response workflows.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Alerting
  - DevOps
  - Incident Management
  - On-Call Management
url: https://raw.githubusercontent.com/api-evangelist/pagerduty/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-04'
specificationVersion: '0.19'
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
        url: openapi/pagerduty-openapi-original.yml
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
common:
  - type: Portal
    url: https://developer.pagerduty.com/
  - type: Documentation
    url: https://developer.pagerduty.com/docs/
  - type: Getting Started
    url: https://developer.pagerduty.com/docs/getting-started/
  - type: Authentication
    url: https://developer.pagerduty.com/docs/authentication
  - type: Sign Up
    url: https://www.pagerduty.com/sign-up-free/
  - type: Login
    url: https://identity.pagerduty.com/sign_in
  - type: Blog
    url: https://www.pagerduty.com/blog/
  - type: Community
    url: https://community.pagerduty.com/
  - type: Support
    url: https://support.pagerduty.com/
  - type: Status
    url: https://status.pagerduty.com/
  - type: Terms of Service
    url: https://www.pagerduty.com/terms-of-service/
  - type: Privacy Policy
    url: https://www.pagerduty.com/privacy-policy/
  - type: GitHub Organization
    url: https://github.com/PagerDuty
  - type: Website
    url: https://www.pagerduty.com/
  - type: Features
    data:
      - REST API for incidents, services, escalations, and on-call schedules
      - Events API v2 for inbound alert ingestion (480 events/min/integration_key)
      - Webhooks v3 with HMAC signing
      - 750+ integrations with monitoring, ticketing, and chat tools
      - Free tier up to 5 users with 1 schedule and 1 escalation policy
      - Professional plan at $21/user/month with chat and Major Incident Workflow
      - Business plan at $41/user/month with custom incident types and ITSM integrations
      - Enterprise plan with incident workflows, post-incident reviews, ServiceNow sync
      - PagerDuty Advance AI credits (1k/5k/20k by tier)
      - Rundeck Automation (separate licensing)
      - Status Pages (external up to 250/500 subscribers by tier)
      - Internal Status Pages (Business+)
      - REST API default rate of 960 req/min/token
      - Analytics API rate-limited to 5 req/min/token
      - Single Sign-On (Pro+) and SCIM provisioning
    sources:
      - https://www.pagerduty.com/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
