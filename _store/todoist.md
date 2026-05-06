---
aid: todoist
name: Todoist
description: Todoist is a productivity platform providing task management APIs for developers. The Todoist API v1 unifies the Sync and REST APIs into a single interface, offering programmatic access to tasks, projects, sections, labels, reminders, comments, workspaces, and webhooks. SDKs are available in Python and TypeScript.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Productivity
  - Tasks
  - To-Do
  - Task Management
  - Collaboration
created: '2025-01-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/todoist/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: todoist:todoist-api
    name: Todoist API
    description: The Todoist API v1 provides programmatic access to Todoist task management, projects, sections, labels, reminders, comments, workspaces, and more. Supports OAuth 2.0 and personal API tokens for authentication. Includes incremental sync via the /sync endpoint for efficient client-server data synchronization.
    humanURL: https://developer.todoist.com/api/v1/
    baseURL: https://api.todoist.com/api/v1
    tags:
      - Productivity
      - Tasks
      - Projects
      - Task Management
    properties:
      - type: Documentation
        url: https://developer.todoist.com/api/v1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/todoist/refs/heads/main/openapi/todoist-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/todoist/refs/heads/main/json-schema/todoist-task-schema.json
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/todoist/refs/heads/main/capabilities/task-management.yaml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/todoist/refs/heads/main/rules/todoist-rules.yml
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/todoist/refs/heads/main/vocabulary/todoist-vocabulary.yml
    contact:
      - FN: Todoist Developer Support
        url: https://developer.todoist.com/
  - aid: todoist:todoist-rest-api
    name: Todoist REST API v2
    description: The Todoist REST API v2 is the legacy recommended API for external integrations, providing access to tasks, projects, sections, labels, comments, and filters. Uses Bearer token authentication with OAuth 2.0 support.
    humanURL: https://developer.todoist.com/rest/v2/
    baseURL: https://api.todoist.com/rest/v2
    tags:
      - Productivity
      - Tasks
      - REST
    properties:
      - type: Documentation
        url: https://developer.todoist.com/rest/v2/
  - aid: todoist:todoist-sync-api
    name: Todoist Sync API v9
    description: The Todoist Sync API is designed for clients maintaining a local representation of user data, allowing incremental synchronization of projects, tasks, labels, filters, and reminders. Supports batch commands for efficient updates.
    humanURL: https://developer.todoist.com/sync/v9/
    baseURL: https://api.todoist.com/sync/v9
    tags:
      - Sync
      - Productivity
      - Tasks
    properties:
      - type: Documentation
        url: https://developer.todoist.com/sync/v9/
      - type: Reference
        url: https://developer.todoist.com/sync/v9/
common:
  - type: Website
    url: https://todoist.com/
  - type: Developer Portal
    url: https://developer.todoist.com/
  - type: Documentation
    url: https://developer.todoist.com/api/v1/
  - type: Sign Up
    url: https://todoist.com/users/showregister
  - type: Login
    url: https://todoist.com/auth/login
  - type: Authentication
    url: https://developer.todoist.com/guides/#oauth
  - type: Webhooks
    url: https://developer.todoist.com/api/v1/#webhooks
  - type: SDKs
    url: https://developer.todoist.com/guides/#sdks
  - type: Python SDK
    url: https://github.com/Doist/todoist-api-python
  - type: TypeScript SDK
    url: https://github.com/Doist/todoist-sdk-typescript
  - type: MCP Server
    url: https://github.com/doist/todoist-ai
  - type: GitHub Organization
    url: https://github.com/Doist
  - type: Blog
    url: https://doist.com/blog/
  - type: Pricing
    url: https://todoist.com/pricing
  - type: Terms of Service
    url: https://doist.com/terms-of-service
  - type: Privacy Policy
    url: https://doist.com/privacy-policy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
