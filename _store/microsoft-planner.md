---
aid: microsoft-planner
url: https://raw.githubusercontent.com/api-evangelist/microsoft-planner/refs/heads/main/apis.yml
apis:
- name: Microsoft Planner API
  description: RESTful API for accessing and managing tasks, plans, and buckets in Microsoft Planner through Microsoft Graph.
  image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://developer.microsoft.com/en-us/graph/docs/api-reference/v1.0/resources/planner_overview
  baseURL: https://graph.microsoft.com/v1.0/planner
  tags:
  - Assignments
  - Buckets
  - Microsoft Graph
  - Plans
  - Tasks
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview
  - type: OpenAPI
    url: openapi/microsoft-planner-openapi.yml
  - type: JSON Schema
    url: json-schema/microsoft-planner-task-schema.json
  - type: JSON-LD Context
    url: json-ld/microsoft-planner-context.jsonld
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: Pricing
    url: https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft365-plans-and-pricing
  - type: Rate Limits
    url: https://learn.microsoft.com/en-us/graph/throttling
  - type: SDK - .NET
    url: https://github.com/microsoftgraph/msgraph-sdk-dotnet
  - type: SDK - JavaScript
    url: https://github.com/microsoftgraph/msgraph-sdk-javascript
  - type: SDK - Python
    url: https://github.com/microsoftgraph/msgraph-sdk-python
  - type: SDK - Java
    url: https://github.com/microsoftgraph/msgraph-sdk-java
  - type: Support
    url: https://developer.microsoft.com/en-us/graph/support
  - type: Changelog
    url: https://developer.microsoft.com/en-us/graph/changelog
  - type: Sandbox
    url: https://developer.microsoft.com/en-us/graph/graph-explorer
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/graph/planner-concept-overview
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview?view=graph-rest-1.0
  - type: Permissions
    url: https://learn.microsoft.com/en-us/graph/permissions-reference
  - type: SDK - Go
    url: https://github.com/microsoftgraph/msgraph-sdk-go
  - type: SDK - PHP
    url: https://github.com/microsoftgraph/msgraph-sdk-php
  - type: SDK - PowerShell
    url: https://github.com/microsoftgraph/msgraph-sdk-powershell
  - type: Quick Start
    url: https://developer.microsoft.com/en-us/graph/quick-start
  - type: OpenAPI Specification
    url: https://github.com/microsoftgraph/msgraph-metadata/blob/master/openapi/v1.0/openapi.yaml
  contact:
  - FN: Microsoft Graph Support
    url: https://developer.microsoft.com/en-us/graph/support
    email: graphsdksupport@microsoft.com
- name: Microsoft Graph Plans API
  description: API for creating, reading, updating, and deleting plans in Microsoft Planner through Microsoft Graph. Plans are the containers for tasks and are owned by groups or other containers.
  image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/plannerplan?view=graph-rest-1.0
  baseURL: https://graph.microsoft.com/v1.0/planner/plans
  tags:
  - Microsoft Graph
  - Planner
  - Plans
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/plannerplan?view=graph-rest-1.0
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/planner-post-plans?view=graph-rest-1.0
  - type: OpenAPI
    url: openapi/microsoft-planner-openapi.yml
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/graph/planner-concept-overview
  - type: Sandbox
    url: https://developer.microsoft.com/en-us/graph/graph-explorer
  contact:
  - FN: Microsoft Graph Support
    url: https://developer.microsoft.com/en-us/graph/support
    email: graphsdksupport@microsoft.com
- name: Microsoft Graph Tasks API
  description: API for creating, reading, updating, and deleting tasks in Microsoft Planner through Microsoft Graph. Tasks are contained in plans and can be assigned to buckets and users.
  image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/plannertask?view=graph-rest-1.0
  baseURL: https://graph.microsoft.com/v1.0/planner/tasks
  tags:
  - Assignments
  - Microsoft Graph
  - Planner
  - Tasks
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/plannertask?view=graph-rest-1.0
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/planner-post-tasks?view=graph-rest-1.0
  - type: OpenAPI
    url: openapi/microsoft-planner-openapi.yml
  - type: JSON Schema
    url: json-schema/microsoft-planner-task-schema.json
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/graph/planner-concept-overview
  - type: Sandbox
    url: https://developer.microsoft.com/en-us/graph/graph-explorer
  contact:
  - FN: Microsoft Graph Support
    url: https://developer.microsoft.com/en-us/graph/support
    email: graphsdksupport@microsoft.com
- name: Microsoft Graph Buckets API
  description: API for creating, reading, updating, and deleting buckets in Microsoft Planner through Microsoft Graph. Buckets represent custom columns for organizing tasks within a plan.
  image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/plannerbucket?view=graph-rest-1.0
  baseURL: https://graph.microsoft.com/v1.0/planner/buckets
  tags:
  - Buckets
  - Microsoft Graph
  - Organization
  - Planner
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/plannerbucket?view=graph-rest-1.0
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/planner-post-buckets?view=graph-rest-1.0
  - type: OpenAPI
    url: openapi/microsoft-planner-openapi.yml
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/graph/planner-concept-overview
  - type: Sandbox
    url: https://developer.microsoft.com/en-us/graph/graph-explorer
  contact:
  - FN: Microsoft Graph Support
    url: https://developer.microsoft.com/en-us/graph/support
    email: graphsdksupport@microsoft.com
- name: Microsoft Graph Planner API (Beta)
  description: Beta version of the Planner API in Microsoft Graph providing access to preview features including plannerRoster resources, business scenarios integration, and expanded container type support.
  image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview?view=graph-rest-beta
  baseURL: https://graph.microsoft.com/beta/planner
  tags:
  - Beta
  - Microsoft Graph
  - Planner
  - Preview
  - Rosters
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview?view=graph-rest-beta
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview?view=graph-rest-beta
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/graph/planner-concept-overview
  - type: Sandbox
    url: https://developer.microsoft.com/en-us/graph/graph-explorer
  contact:
  - FN: Microsoft Graph Support
    url: https://developer.microsoft.com/en-us/graph/support
    email: graphsdksupport@microsoft.com
- name: Microsoft Graph Business Scenarios Planner API (Beta)
  description: Beta API for integrating external business processes with Microsoft Planner through business scenarios, allowing creation of scenario-controlled Planner tasks and plans.
  image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/businessscenario-planner-overview?view=graph-rest-beta
  baseURL: https://graph.microsoft.com/beta/solutions/businessScenarios
  tags:
  - Beta
  - Business Scenarios
  - Integration
  - Microsoft Graph
  - Planner
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/businessscenario-planner-overview?view=graph-rest-beta
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/businessscenario-overview?view=graph-rest-beta
  - type: Overview
    url: https://learn.microsoft.com/en-us/graph/businessscenarios-concept-overview
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: Sandbox
    url: https://developer.microsoft.com/en-us/graph/graph-explorer
  contact:
  - FN: Microsoft Graph Support
    url: https://developer.microsoft.com/en-us/graph/support
    email: graphsdksupport@microsoft.com
name: Microsoft Planner
tags:
- Collaboration
- Microsoft 365
- Productivity
- Project Management
- Task Management
type: Contract
image: https://docs.microsoft.com/en-us/media/logos/logo-ms-social.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Planner is a task management tool that helps teams organize work, assign tasks, share files, and collaborate on projects within Microsoft 365.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

