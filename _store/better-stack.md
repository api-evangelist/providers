---
aid: better-stack
url: https://raw.githubusercontent.com/api-evangelist/better-stack/refs/heads/main/apis.yml
apis:
  - aid: better-stack:better-stack
    name: Better Stack API
    tags:
      - Monitoring
      - Incidents
      - Uptime
      - Heartbeats
      - Status Pages
    humanURL: https://betterstack.com/docs/uptime/api/getting-started/
    baseURL: https://uptime.betterstack.com/api/v2
    properties:
      - url: https://betterstack.com/docs/uptime/api/getting-started/
        type: Documentation
      - url: https://betterstack.com/docs/uptime/api/monitors/
        type: APIReference
      - url: https://raw.githubusercontent.com/api-evangelist/better-stack/refs/heads/main/openapi/better-stack-openapi.yml
        type: OpenAPI
    description: The Better Stack API provides programmatic access to uptime monitoring, heartbeat monitoring, incident management, status pages, escalation policies, and team management. It follows the JSON:API specification and uses Bearer token authentication.
name: Better Stack
tags:
  - Incidents
  - Logs
  - Monitoring
  - Platform
  - Status
  - Uptime
  - Observability
  - On-Call
  - Heartbeats
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-19'
position: Consuming
description: Better Stack is a comprehensive infrastructure monitoring and observability platform that combines uptime monitoring, log management, incident management, status pages, and AI-powered site reliability tools. It helps teams identify and resolve website and server issues quickly by providing real-time alerting, detailed diagnostics, on-call scheduling, and public/private status pages.
common:
  - type: Portal
    url: https://betterstack.com/docs/
  - type: GettingStarted
    url: https://betterstack.com/docs/uptime/api/getting-started/
  - type: Authentication
    url: https://betterstack.com/docs/uptime/api/getting-started/
  - type: Pricing
    url: https://betterstack.com/pricing
  - type: StatusPage
    url: https://status.betterstack.com/
  - type: Blog
    url: https://betterstack.com/community/blog
  - type: ChangeLog
    url: https://betterstack.com/tag/changelog
  - type: GitHubOrganization
    url: https://github.com/BetterStackHQ
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/better-stack/refs/heads/main/rules/better-stack-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/better-stack/refs/heads/main/vocabulary/better-stack-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/better-stack/refs/heads/main/capabilities/incident-response.yaml
  - type: Features
    data:
      - name: Uptime Monitoring
        description: Monitor URLs, APIs, and services for availability with checks from multiple global regions every 30 seconds.
      - name: Heartbeat Monitoring
        description: Monitor scheduled jobs, cron tasks, and background workers by pinging a unique URL on each run.
      - name: Incident Management
        description: Automatically create and manage incidents when monitors detect downtime, with acknowledgement and resolution workflows.
      - name: On-Call Scheduling
        description: Configure escalation policies with multi-step notification sequences via phone, SMS, email, and push.
      - name: Status Pages
        description: Create public and private status pages with custom domains, branding, and real-time component status.
      - name: Log Management
        description: Collect, search, and visualize logs across your entire infrastructure stack.
      - name: AI SRE
        description: AI-powered root cause analysis that automatically investigates incidents and suggests resolutions.
      - name: Infrastructure Monitoring
        description: OpenTelemetry-native monitoring with dashboards for metrics and infrastructure health.
      - name: Terraform Provider
        description: Manage Better Stack resources as code using the official Terraform provider.
      - name: MCP Server
        description: Model Context Protocol server for integrating Better Stack with AI tools and agents.
  - type: UseCases
    data:
      - name: Website Uptime Monitoring
        description: Monitor public websites and APIs for availability and alert on-call engineers when they go down.
      - name: API Health Checking
        description: Continuously verify that REST APIs return expected status codes and response times.
      - name: Cron Job Monitoring
        description: Use heartbeats to ensure scheduled tasks run on time and alert when they fail to check in.
      - name: Incident Response Automation
        description: Automate incident creation, on-call notifications, and resolution workflows to reduce MTTR.
      - name: Customer-Facing Status Communication
        description: Publish status pages that automatically reflect the real-time health of monitored services.
      - name: Infrastructure Observability
        description: Aggregate logs, metrics, and traces in a single platform for full-stack observability.
  - type: Integrations
    data:
      - name: Slack
        description: Receive incident alerts and status updates directly in Slack channels.
      - name: PagerDuty
        description: Forward incidents to PagerDuty for existing on-call workflows.
      - name: Terraform
        description: Manage monitors, status pages, and escalation policies as infrastructure as code.
      - name: OpenTelemetry
        description: Send metrics, logs, and traces using OpenTelemetry-compatible exporters.
      - name: Sentry
        description: Compatible with Sentry SDK for error tracking integration.
      - name: New Relic
        description: Connect Better Stack monitoring data with New Relic dashboards.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
