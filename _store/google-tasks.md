---
aid: google-tasks
name: Google Tasks
description: The Google Tasks API lets you search, read, and update Google Tasks content and metadata. You can create, update, delete, and organize tasks across multiple task lists, move tasks between positions, and manage task completion status programmatically.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-tasks/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Google
  - Productivity
  - Task Management
  - Tasks
  - Todo
  - Workspace
apis:
  - name: Google Tasks API v1
    description: The Google Tasks API provides programmatic access to Google Tasks for managing task lists and individual tasks. Supports creating, reading, updating, deleting, moving, and clearing tasks.
    humanURL: https://developers.google.com/tasks
    baseURL: https://tasks.googleapis.com/tasks/v1
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/tasks/reference/rest
      - type: OpenAPI
        url: openapi/tasks.yml
      - type: Authentication
        url: https://developers.google.com/workspace/tasks/auth
      - type: Getting Started
        url: https://developers.google.com/workspace/tasks/overview
      - type: JSONSchema
        url: json-schema/tasks.json
common:
  - type: Portal
    url: https://developers.google.com/tasks
  - type: Getting Started
    url: https://developers.google.com/workspace/tasks/overview
  - type: Documentation
    url: https://developers.google.com/tasks
  - type: Authentication
    url: https://developers.google.com/workspace/tasks/auth
  - type: Terms of Service
    url: https://developers.google.com/workspace/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://developers.google.com/tasks/support
  - type: JSON-LD
    url: json-ld/tasks.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
