---
aid: rollbar
name: Rollbar
description: Rollbar is a real-time error tracking and monitoring platform for software teams. It automatically captures exceptions and errors from web, mobile, and server-side applications, groups them by root cause, and provides actionable alerts to speed up debugging. Rollbar provides SDKs for over a dozen platforms including JavaScript, Python, PHP, Ruby, Go, Swift, .NET, and Java. The REST API enables programmatic management of projects, items, occurrences, deployments, teams, notifications, and source maps. The RQL (Rollbar Query Language) provides SQL-like queries for error analysis.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/rollbar/refs/heads/main/apis.yml
tags:
  - Error Tracking
  - Monitoring
  - Debugging
  - DevOps
  - Application Performance
created: '2026-05-02'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: rollbar:rollbar-rest-api
    name: Rollbar REST API
    description: The Rollbar REST API provides programmatic access to the Rollbar error tracking and monitoring platform. Manage projects, items, occurrences, deploys, teams, users, invites, notifications, and source maps through a RESTful JSON interface. Authentication is via project access tokens in the X-Rollbar-Access-Token header.
    tags:
      - Error Tracking
      - Monitoring
      - REST
      - Projects
      - Teams
    humanURL: https://docs.rollbar.com/reference/getting-started-1
    baseURL: https://api.rollbar.com/api/1
    properties:
      - url: https://docs.rollbar.com/reference/getting-started-1
        type: Documentation
      - url: https://explorer.docs.rollbar.com/
        type: OpenAPI
      - url: openapi/rollbar-rest-api-openapi.yml
        type: OpenAPI
    solutions:
      - Error Management
      - Project Administration
      - Team Management
      - Source Map Debugging
    features:
      - Item Management
      - Occurrence Retrieval
      - Project Management
      - Access Token Management
      - Team and User Management
      - Source Map Upload
      - Webhook Notifications
  - aid: rollbar:rollbar-deployment-api
    name: Rollbar Deployment API
    description: The Rollbar Deployment API allows developers to notify Rollbar of application deployments and releases. By reporting deploys, teams can correlate error spikes with specific releases, track deployment history, and manage rollbacks with full visibility into which code version is running in production.
    tags:
      - Deployment
      - Release Management
      - Error Tracking
      - REST
      - DevOps
    humanURL: https://docs.rollbar.com/reference/post_deploy
    baseURL: https://api.rollbar.com/api/1
    properties:
      - url: https://docs.rollbar.com/reference/post_deploy
        type: Documentation
      - url: openapi/rollbar-deployment-api-openapi.yml
        type: OpenAPI
  - aid: rollbar:rollbar-metrics-api
    name: Rollbar Metrics API
    description: The Rollbar Metrics API is part of Rollbar Analyze and provides programmatic access to metrics data for error tracking analysis and discovery. Enables developers to query resolution time metrics, occurrence counts, and item activation metrics across projects.
    tags:
      - Metrics
      - Analytics
      - Error Tracking
      - REST
      - Monitoring
    humanURL: https://docs.rollbar.com/reference/metrics
    baseURL: https://api.rollbar.com/api/1
    properties:
      - url: https://docs.rollbar.com/reference/metrics
        type: Documentation
      - url: openapi/rollbar-metrics-api-openapi.yml
        type: OpenAPI
  - aid: rollbar:rollbar-rql-api
    name: Rollbar RQL API
    description: The Rollbar RQL (Rollbar Query Language) API provides a SQL-like interface for querying error and deployment data stored in Rollbar. Supports SELECT queries against item_occurrence and deploy tables for advanced error analysis, reporting, and custom integrations.
    tags:
      - Query Language
      - Analytics
      - Error Tracking
      - REST
      - SQL
    humanURL: https://docs.rollbar.com/reference/rql
    baseURL: https://api.rollbar.com/api/1
    properties:
      - url: https://docs.rollbar.com/reference/rql
        type: Documentation
      - url: openapi/rollbar-rql-api-openapi.yml
        type: OpenAPI
  - aid: rollbar:rollbar-webhooks
    name: Rollbar Webhooks
    description: Rollbar supports outbound webhook notifications for real-time event-driven integrations. Webhooks deliver payload data when errors occur, items are resolved, or deployment events happen, enabling integration with Slack, PagerDuty, email, and custom HTTP endpoints.
    tags:
      - Webhooks
      - Event-Driven
      - Notifications
      - AsyncAPI
      - Monitoring
    humanURL: https://docs.rollbar.com/docs/webhooks
    baseURL: https://api.rollbar.com
    properties:
      - url: https://docs.rollbar.com/docs/webhooks
        type: Documentation
      - url: asyncapi/rollbar-webhooks-asyncapi.yml
        type: AsyncAPI
common:
  - url: https://rollbar.com/
    type: Website
  - url: https://docs.rollbar.com/
    type: Documentation
  - url: https://docs.rollbar.com/reference/getting-started-1
    type: Documentation
  - url: https://explorer.docs.rollbar.com/
    type: Portal
  - url: https://rollbar.com/pricing/
    type: Pricing
  - url: https://github.com/rollbar
    type: GitHubOrganization
  - url: https://rollbar.com/terms/
    type: TermsOfService
  - url: https://rollbar.com/privacy/
    type: PrivacyPolicy
  - url: https://rollbar.com/support/
    type: Support
  - url: openapi/rollbar-rest-api-openapi.yml
    type: OpenAPI
  - url: openapi/rollbar-deployment-api-openapi.yml
    type: OpenAPI
  - url: openapi/rollbar-metrics-api-openapi.yml
    type: OpenAPI
  - url: openapi/rollbar-rql-api-openapi.yml
    type: OpenAPI
  - url: asyncapi/rollbar-webhooks-asyncapi.yml
    type: AsyncAPI
  - url: json-schema/rollbar-item-schema.json
    type: JSONSchema
  - url: json-schema/rollbar-occurrence-schema.json
    type: JSONSchema
  - url: json-schema/rollbar-deploy-schema.json
    type: JSONSchema
  - url: json-schema/rollbar-webhook-payload-schema.json
    type: JSONSchema
  - url: json-ld/rollbar-context.jsonld
    type: JSONLDContext
  - type: Features
    data:
      - 'Free: 5K occurrences + 1K replays/month'
      - 'Essentials: 10K-50M occurrences/mo, 4K credits, 90-day retention'
      - 'Advanced: 8K credits, adaptive alerts, RQL/Metrics API, SCIM, 180-day retention'
      - 'Enterprise: 80M+ occurrences, Slack channel, custom retention, priority SLAs'
      - Real-time feed and alerts
      - Intelligent error grouping (RQL)
      - Stack traces with source maps and breadcrumbs
      - Deploy and version tracking
      - Item ingest tier-based limit
      - 'REST API: 5,000 req/min (read)'
      - 'Bulk Resolve API: 1,000 items/request'
      - Webhooks for new items, deploys, occurrences
      - OAuth 2.0 + project tokens
      - 30+ language SDKs
      - Adaptive alerts on Advanced+
      - RQL (Rollbar Query Language) for advanced querying
    sources:
      - https://rollbar.com/pricing/
    updated: '2026-05-04'
integrations:
  - Slack
  - PagerDuty
  - Jira
  - GitHub
  - Bitbucket
  - Heroku
solutions:
  - Error Tracking
  - Application Monitoring
  - Release Management
  - On-call Alerting
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
