---
aid: knit
name: Knit
description: Knit is a unified API platform for B2B products, AI agents, and MCP clients, providing integrations infrastructure for HR, recruitment, and collaboration tools. Knit manages cron jobs, rate limits, and retries out of the box for predictable data syncing at scale.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - B2B
  - HR Integrations
  - HRIS
  - Unified API
url: https://raw.githubusercontent.com/api-evangelist/knit/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-18'
specificationVersion: '0.19'
apis:
  - aid: knit:unified-api
    name: Knit Unified API
    description: Knit's unified API provides standardized endpoints for connecting with multiple HR, recruitment, and chat tools in one integration. Access employee data, departments, locations, time-off records, job postings, and sync statuses through a single normalized interface.
    humanURL: https://developers.getknit.dev/
    baseURL: https://api.getknit.dev/v1
    tags:
      - Employees
      - HR
      - Integrations
      - Recruitment
      - Unified API
    properties:
      - type: Documentation
        url: https://developers.getknit.dev/
      - type: OpenAPI
        url: openapi/knit-unified-api-openapi.yml
      - type: GettingStarted
        url: https://developers.getknit.dev/
    contact:
      - type: Support
        url: https://www.getknit.dev/
common:
  - type: Portal
    url: https://developers.getknit.dev/
  - type: Documentation
    url: https://developers.getknit.dev/
  - type: Features
    data:
      - Unified API for multiple HRIS and ATS platforms
      - Automatic cron job management for data syncing
      - Built-in rate limiting and retry logic
      - Standardized data models across providers
      - MCP client and AI agent support
      - Real-time webhook notifications
      - Incremental sync with updated_after filtering
  - type: UseCases
    data:
      - Synchronizing employee data across HR platforms
      - Building B2B integrations without managing individual provider APIs
      - Powering AI agents with unified HR and recruitment data
      - Automating onboarding workflows across HRIS systems
      - Aggregating time-off and attendance data from multiple providers
  - type: Integrations
    data:
      - BambooHR
      - Gusto
      - Workday
      - ADP
      - Rippling
      - Greenhouse
      - Lever
      - Slack
      - Microsoft Teams
  - type: JSONSchema
    url: json-schema/knit-unified-api-schema.json
  - type: JSONLD
    url: json-ld/knit-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
