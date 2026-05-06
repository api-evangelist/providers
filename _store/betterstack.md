---
aid: betterstack
name: Better Stack
description: Better Stack is a comprehensive infrastructure monitoring and observability platform combining uptime monitoring, log management, incident management, status pages, and AI-powered site reliability tools. This is an alias entry for the better-stack repository. See https://github.com/api-evangelist/better-stack for the full API profile with OpenAPI specs, capabilities, and vocabulary.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Observability
  - Uptime Monitoring
  - Incidents
  - Logs
  - Monitoring
  - Status Pages
  - On-Call
url: https://raw.githubusercontent.com/api-evangelist/betterstack/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: betterstack:betterstack-api
    name: Better Stack API
    description: The Better Stack API provides programmatic access to uptime monitoring, heartbeat monitoring, incident management, status pages, escalation policies, and team management. It follows the JSON:API specification and uses Bearer token authentication.
    humanURL: https://betterstack.com/docs/uptime/api/getting-started/
    baseURL: https://uptime.betterstack.com/api/v2
    tags:
      - Monitoring
      - Incidents
      - Uptime
      - Heartbeats
      - Status Pages
    properties:
      - type: Documentation
        url: https://betterstack.com/docs/uptime/api/getting-started/
      - type: APIReference
        url: https://betterstack.com/docs/uptime/api/monitors/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/better-stack/refs/heads/main/openapi/better-stack-openapi.yml
common:
  - type: Portal
    url: https://betterstack.com/docs/
  - type: GettingStarted
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
  - type: Features
    data:
      - name: Uptime Monitoring
        description: Monitor URLs, APIs, and services for availability with global region checks.
      - name: Heartbeat Monitoring
        description: Monitor scheduled jobs and cron tasks with heartbeat pings.
      - name: Incident Management
        description: On-call alerting with escalation policies, acknowledgement, and resolution workflows.
      - name: Status Pages
        description: Public and private status pages with custom domains and real-time component status.
      - name: Log Management
        description: Collect, search, and visualize logs across your infrastructure stack.
      - name: AI SRE
        description: AI-powered root cause analysis for automated incident investigation.
  - type: Integrations
    data:
      - name: Slack
        description: Receive incident alerts in Slack channels.
      - name: PagerDuty
        description: Forward incidents to PagerDuty.
      - name: Terraform
        description: Manage Better Stack resources as infrastructure as code.
      - name: OpenTelemetry
        description: Send metrics, logs, and traces using OpenTelemetry exporters.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
