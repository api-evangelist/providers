---
aid: microsoft-to-do
name: Microsoft to Do
description: Microsoft To Do is a task management application that helps users organize and manage their day. It provides API access through Microsoft Graph for managing task lists and tasks across Microsoft 365.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Microsoft
  - Microsoft 365
  - Productivity
  - Tasks
url: https://raw.githubusercontent.com/api-evangelist/microsoft-to-do/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-to-do:graph-tasks-api
    name: Microsoft Graph to Do Tasks API
    tags:
      - Microsoft Graph
      - Productivity
      - Tasks
      - To Do
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0/
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/todo-overview
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/todo-overview
        type: Documentation
      - url: https://learn.microsoft.com/en-us/graph/api/resources/todotask
        type: Reference
      - url: https://learn.microsoft.com/en-us/graph/auth/
        type: Authentication
    description: The Microsoft Graph To Do Tasks API provides access to Microsoft To Do task lists and tasks. Developers can create, read, update, and delete task lists and individual tasks, manage task completion status, set due dates and reminders, add file attachments, and organize tasks with linked resources across Microsoft 365.
common:
  - type: Portal
    url: https://to-do.microsoft.com/
  - type: Website
    url: https://www.microsoft.com/en-us/microsoft-365/microsoft-to-do-list-app
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/todo-concept-overview
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: SDKs
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
