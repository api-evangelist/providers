---
aid: clickup
url: https://raw.githubusercontent.com/api-evangelist/clickup/refs/heads/main/apis.yml
modified: '2026-05-04'
apis:
  - aid: clickup:tasks-api
    name: ClickUp Tasks API
    tags:
      - Collaboration
      - Productivity
      - Project Management
      - Tasks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.clickup.com
    humanURL: https://developer.clickup.com/docs/tasks
    properties:
      - url: https://developer.clickup.com/docs/tasks
        type: Documentation
      - url: openapi/clickup-tasks-openapi.yml
        type: OpenAPI
    description: The ClickUp Tasks API allows developers to create, read, update, and delete tasks within ClickUp workspaces. Tasks are the core unit of work in ClickUp and can include custom fields, assignees, due dates, tags, priorities, and attachments. The API supports filtering tasks by list, space, or project, and enables bulk operations for managing large numbers of tasks programmatically.
  - aid: clickup:spaces-api
    name: ClickUp Spaces API
    tags:
      - Organization
      - Project Management
      - Workspaces
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.clickup.com
    humanURL: https://developer.clickup.com/reference/get-spaces
    properties:
      - url: https://developer.clickup.com/reference/get-spaces
        type: Documentation
      - url: openapi/clickup-spaces-openapi.yml
        type: OpenAPI
    description: The ClickUp Spaces API provides endpoints for managing Spaces, which are the top-level organizational containers within a ClickUp Workspace. Spaces contain Folders and Lists that organize tasks into logical groupings. Developers can create, update, and delete Spaces, as well as retrieve Space details and configure Space-level settings such as enabled features and statuses.
  - aid: clickup:lists-api
    name: ClickUp Lists API
    tags:
      - Lists
      - Project Management
      - Task Organization
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.clickup.com
    humanURL: https://developer.clickup.com/reference/get-lists
    properties:
      - url: https://developer.clickup.com/reference/get-lists
        type: Documentation
      - url: openapi/clickup-lists-openapi.yml
        type: OpenAPI
    description: The ClickUp Lists API enables developers to manage Lists, which are containers that hold tasks within a Space or Folder. Lists define the workflow statuses available to tasks and serve as the primary grouping mechanism for related work items. The API supports creating, updating, and deleting Lists, as well as retrieving List details and the tasks they contain.
  - aid: clickup:folders-api
    name: ClickUp Folders API
    tags:
      - Folders
      - Organization
      - Project Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.clickup.com
    humanURL: https://developer.clickup.com/reference/get-folders
    properties:
      - url: https://developer.clickup.com/reference/get-folders
        type: Documentation
      - url: openapi/clickup-folders-openapi.yml
        type: OpenAPI
    description: The ClickUp Folders API provides endpoints for managing Folders, which are optional organizational containers that sit between Spaces and Lists in the ClickUp hierarchy. Folders group related Lists together and can be used to organize projects or workstreams within a Space. Developers can create, update, delete, and retrieve Folders and their associated Lists.
  - aid: clickup:goals-api
    name: ClickUp Goals API
    tags:
      - Goals
      - OKR
      - Project Management
      - Tracking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.clickup.com
    humanURL: https://developer.clickup.com/reference/get-goals
    properties:
      - url: https://developer.clickup.com/reference/get-goals
        type: Documentation
      - url: openapi/clickup-goals-openapi.yml
        type: OpenAPI
    description: The ClickUp Goals API allows developers to create and manage goals within a Workspace. Goals can track progress toward objectives using targets based on numbers, currency, percentages, or task completion. The API supports creating goals, adding key results and targets, updating progress, and retrieving goal details. This is useful for building OKR tracking and reporting integrations.
  - aid: clickup:comments-api
    name: ClickUp Comments API
    tags:
      - Collaboration
      - Comments
      - Project Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.clickup.com
    humanURL: https://developer.clickup.com/reference/get-task-comments
    properties:
      - url: https://developer.clickup.com/reference/get-task-comments
        type: Documentation
      - url: openapi/clickup-comments-openapi.yml
        type: OpenAPI
    description: The ClickUp Comments API provides endpoints for creating and retrieving comments on tasks, views, and lists. Comments support rich text formatting, mentions, and attachments. Developers can use this API to build integrations that synchronize discussions between ClickUp and other collaboration tools, or to programmatically add status updates and notes to tasks.
  - aid: clickup:teams-api
    name: ClickUp Teams (Workspaces) API
    tags:
      - Project Management
      - Teams
      - Users
      - Workspaces
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.clickup.com
    humanURL: https://developer.clickup.com/reference/get-teams
    properties:
      - url: https://developer.clickup.com/reference/get-teams
        type: Documentation
      - url: openapi/clickup-teams-openapi.yml
        type: OpenAPI
    description: The ClickUp Teams API provides access to Workspace-level information and membership. In the ClickUp API, Teams correspond to Workspaces, which are the top-level organizational unit. The API allows developers to retrieve a list of Workspaces the authenticated user belongs to, along with member details and roles. This is typically the starting point for navigating the ClickUp hierarchy.
  - aid: clickup:webhooks-api
    name: ClickUp Webhooks API
    tags:
      - Events
      - Project Management
      - Real-Time
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.clickup.com
    humanURL: https://developer.clickup.com/docs/webhooks
    properties:
      - url: https://developer.clickup.com/docs/webhooks
        type: Documentation
      - url: openapi/clickup-webhooks-openapi.yml
        type: OpenAPI
      - url: asyncapi/clickup-webhooks-asyncapi.yml
        type: AsyncAPI
    description: The ClickUp Webhooks API enables developers to subscribe to real-time events within a Workspace. When subscribed events occur, ClickUp sends HTTP POST requests to a specified endpoint URL with event details. Webhooks support events for tasks, lists, folders, spaces, and goals. Each webhook payload is signed with a shared secret for verification, ensuring the event originated from ClickUp.
  - aid: clickup:custom-fields-api
    name: ClickUp Custom Fields API
    tags:
      - Custom Fields
      - Metadata
      - Project Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.clickup.com
    humanURL: https://developer.clickup.com/reference/get-accessible-custom-fields
    properties:
      - url: https://developer.clickup.com/reference/get-accessible-custom-fields
        type: Documentation
      - url: openapi/clickup-custom-fields-openapi.yml
        type: OpenAPI
    description: The ClickUp Custom Fields API allows developers to retrieve available custom fields for a list and set or update custom field values on tasks. Custom fields extend the default task data model with user-defined attributes such as dropdowns, labels, numbers, dates, and relationships. This API is essential for integrations that need to read or write structured metadata beyond the standard task fields.
  - aid: clickup:time-tracking-api
    name: ClickUp Time Tracking API
    tags:
      - Productivity
      - Project Management
      - Reporting
      - Time Tracking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.clickup.com
    humanURL: https://developer.clickup.com/reference/get-time-entries-within-a-date-range
    properties:
      - url: https://developer.clickup.com/reference/get-time-entries-within-a-date-range
        type: Documentation
      - url: openapi/clickup-time-tracking-openapi.yml
        type: OpenAPI
    description: The ClickUp Time Tracking API provides endpoints for recording and retrieving time entries associated with tasks. Developers can create manual time entries, start and stop timers, and query time entries within date ranges and across team members. This API supports building time reporting dashboards, invoicing integrations, and productivity analysis tools.
  - aid: clickup:views-api
    name: ClickUp Views API
    tags:
      - Dashboards
      - Project Management
      - Views
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.clickup.com
    humanURL: https://developer.clickup.com/reference/get-views
    properties:
      - url: https://developer.clickup.com/reference/get-views
        type: Documentation
      - url: openapi/clickup-views-openapi.yml
        type: OpenAPI
    description: The ClickUp Views API enables developers to create and manage views at the team, space, folder, and list levels. Views define how tasks are displayed and filtered, supporting formats such as list, board, calendar, gantt, and table. The API allows programmatic creation of saved views with specific filters, groupings, and sort configurations.
  - aid: clickup:oauth-api
    name: ClickUp OAuth API
    tags:
      - Authentication
      - Authorization
      - OAuth
      - Project Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.clickup.com
    humanURL: https://developer.clickup.com/docs/authentication
    properties:
      - url: https://developer.clickup.com/docs/authentication
        type: Documentation
      - url: openapi/clickup-oauth-openapi.yml
        type: OpenAPI
    description: The ClickUp OAuth API implements the authorization code grant type, allowing third-party applications to authenticate users and access their ClickUp Workspaces. Workspace owners or admins can create OAuth apps, and users authorize access by granting permissions to specific Workspaces. The API provides endpoints for obtaining authorization codes, exchanging them for access tokens, and retrieving the authenticated user's information.
common:
  - type: JSON-LD
    url: json-ld/clickup-context.jsonld
  - type: JSONSchema
    url: json-schema/clickup-task-schema.json
  - type: JSONSchema
    url: json-schema/clickup-webhook-payload-schema.json
  - type: Features
    data:
      - 'Free plan: 60MB storage, unlimited tasks/members'
      - Unlimited at $7/user/mo annual with unlimited everything
      - Business at $12/user/mo with dashboards, automations (5K/mo), Google SSO
      - 'Enterprise: SAML/SCIM, MSA/HIPAA, 250K automations/mo, data residency'
      - 'REST API v2: 100/min Free, 1000/min Unlimited/Business, 10K/min Enterprise'
      - Webhooks for task, list, space, doc events
      - OAuth 2.0 and personal API tokens
      - Custom Fields API
      - Goals, Portfolios, Time Tracking APIs
      - Docs, Whiteboards, Forms
      - ClickUp Chat (Business+)
      - ClickUp AI for content and automation (per-user add-on)
      - Sprint management with story points
      - Mind maps and Gantt charts
      - 1,000+ integrations
      - Custom branding and audit log on Enterprise
    sources:
      - https://clickup.com/pricing
    updated: '2026-05-04'
description: Work with tasks using the ClickUp API.
---
