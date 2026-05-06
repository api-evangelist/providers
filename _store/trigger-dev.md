---
aid: trigger-dev
name: Trigger.dev
description: Trigger.dev is an open source background jobs and workflow automation platform for TypeScript developers. It enables building and deploying fully-managed AI agents and background workflows with real-time observability, scheduled tasks, durable execution, and an extensive management API. Tasks are written in plain async TypeScript and can be triggered via REST API, SDK, or on a schedule. Supports cloud-hosted and self-hosted deployments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Developer-First
  - Workflow Automation
  - Background Jobs
  - TypeScript
  - AI Agents
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/trigger-dev/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: trigger-dev:trigger-dev-management
    name: Trigger.dev Management API
    description: The Trigger.dev Management API provides comprehensive REST endpoints for managing workflow runs, tasks, schedules, deployments, queues, environment variables, batches, and waitpoints. Enables programmatic control over the full lifecycle of background job workflows including triggering, monitoring, cancellation, and observability. Authenticated via bearer token (secret API key).
    humanURL: https://trigger.dev/docs/management/overview
    tags:
      - Workflow Automation
      - Background Jobs
      - Task Management
      - Scheduling
      - Deployments
      - Queue Management
    properties:
      - type: Documentation
        url: https://trigger.dev/docs/management/overview
      - type: GettingStarted
        url: https://trigger.dev/docs/introduction
      - type: OpenAPI
        url: openapi/trigger-dev-management-openapi.yml
      - type: SDK
        url: https://www.npmjs.com/package/@trigger.dev/sdk
  - aid: trigger-dev:trigger-dev-realtime
    name: Trigger.dev Realtime API
    description: The Trigger.dev Realtime API provides streaming updates and React hooks for monitoring workflow run status in real-time. Includes useRealtimeRun, useRealtimeRunsWithTag, and useRealtimeStream hooks for frontend integration. Supports AI streaming responses and live run status updates.
    humanURL: https://trigger.dev/docs/realtime/overview
    tags:
      - Realtime
      - Streaming
      - React
      - WebSockets
      - AI Streaming
    properties:
      - type: Documentation
        url: https://trigger.dev/docs/realtime/overview
features:
  - Durable background task execution with automatic retries
  - Scheduled tasks with cron expressions and timezone support
  - AI agent workflow orchestration
  - Realtime run monitoring with React hooks
  - Queue management with concurrency controls
  - Environment variable management per project
  - Deployment management with version promotion
  - Waitpoint tokens for human-in-the-loop workflows
  - Batch task triggering
  - Comprehensive observability with traces and spans
useCases:
  - Background job processing for TypeScript/Node.js applications
  - AI agent task orchestration with durable execution
  - Scheduled data processing and reporting jobs
  - Long-running workflow automation
  - Email and notification delivery pipelines
  - Data synchronization and ETL workflows
  - Human-in-the-loop approval workflows
integrations:
  - TypeScript/Node.js via @trigger.dev/sdk
  - React via @trigger.dev/react-hooks
  - CLI via trigger.dev/cli
  - Next.js, Remix, and other full-stack frameworks
  - Self-hosted deployment via Docker
solutions:
  - TypeScript developers needing reliable background jobs
  - Teams building AI agent workflows requiring durable execution
  - Applications requiring scheduled task automation
  - Platforms needing human-in-the-loop approval workflows
github:
  - name: trigger.dev
    url: https://github.com/triggerdotdev/trigger.dev
    description: Main Trigger.dev monorepo - platform, SDK, and CLI
    language: TypeScript
    stars: 14763
  - name: api-reference
    url: https://github.com/triggerdotdev/api-reference
    description: Job code samples for SDK and REST API integrations
    language: TypeScript
common:
  - type: Website
    url: https://trigger.dev
  - type: Documentation
    url: https://trigger.dev/docs
  - type: GettingStarted
    url: https://trigger.dev/docs/introduction
  - type: GitHub
    url: https://github.com/triggerdotdev/trigger.dev
  - type: SDK
    url: https://www.npmjs.com/package/@trigger.dev/sdk
  - type: CLI
    url: https://www.npmjs.com/package/trigger.dev
  - type: SignUp
    url: https://cloud.trigger.dev/login
  - type: Pricing
    url: https://trigger.dev/pricing
  - type: Blog
    url: https://trigger.dev/blog
  - type: Changelog
    url: https://trigger.dev/changelog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
