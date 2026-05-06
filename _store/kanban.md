---
aid: kanban
name: Kanban Tool
description: Kanban Tool is a visual project management platform for managing boards, tasks, and workflows using the Kanban methodology. It provides REST APIs (v1 and v3), browser SDK, and DevKit for programmatic access to boards, tasks, columns, comments, attachments, time tracking, and team members.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agile
  - Boards
  - Kanban
  - Project Management
  - Task Management
  - Time Tracking
  - Workflow
url: https://raw.githubusercontent.com/api-evangelist/kanban/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kanban:kanban-tool-rest-api-v3
    name: Kanban Tool REST API v3
    description: Current REST API for Kanban Tool. Returns JSON responses, supports bulk task modifications, attachment operations, and uses a flat namespace with associated objects in single responses. Authenticated via Bearer token.
    humanURL: https://kanbantool.com/developer/api-v3
    baseURL: https://YOUR_DOMAIN.kanbantool.com/api/v3
    tags:
      - Boards
      - Cards
      - Comments
      - Attachments
      - Tasks
      - Subtasks
      - Time Tracking
      - Users
    properties:
      - type: Documentation
        url: https://kanbantool.com/developer/api-v3
      - type: Authentication
        url: https://kanbantool.com/developer/api-v3
  - aid: kanban:kanban-tool-rest-api-v1
    name: Kanban Tool REST API v1
    description: Legacy REST API for Kanban Tool. Supports both XML and JSON formats, uses a resource-oriented endpoint structure. Remains supported for existing integrations.
    humanURL: https://kanbantool.com/developer
    tags:
      - Boards
      - Legacy
      - Tasks
      - Workflow
    properties:
      - type: Documentation
        url: https://kanbantool.com/developer
  - aid: kanban:kanban-tool-sdk
    name: Kanban Tool Browser SDK
    description: Browser-side SDK for customizing the Kanban Tool interface. Enables adding custom buttons to context menus, modifying styles, and extending UI behavior.
    humanURL: https://kanbantool.com/developer
    tags:
      - SDK
      - Browser
      - Customization
    properties:
      - type: Documentation
        url: https://kanbantool.com/developer
common:
  - type: Website
    url: https://kanbantool.com
  - type: Developer Portal
    url: https://kanbantool.com/developer
  - type: Blog
    url: https://kanbantool.com/blog
  - type: Pricing
    url: https://kanbantool.com/pricing
  - type: Sign Up
    url: https://kanbantool.com/signup/new
  - type: Support
    url: https://kanbantool.com/support/introduction
  - type: Integrations
    url: https://kanbantool.com/integrations
  - type: Kanban Guide
    url: https://kanbantool.com/kanban-guide/introduction
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
