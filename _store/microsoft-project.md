---
aid: microsoft-project
url: https://raw.githubusercontent.com/api-evangelist/microsoft-project/refs/heads/main/apis.yml
apis:
- aid: microsoft-project:rest-api
  name: Microsoft Project REST API
  description: REST API for accessing and managing Microsoft Project data, including projects, tasks, resources, and assignments.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://learn.microsoft.com/en-us/project/api/project-rest-api
  baseURL: https://api.project.microsoft.com/v1.0
  tags:
  - Projects
  - Resources
  - REST
  - Tasks
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/project/api/project-rest-api
  - type: Authentication
    url: https://learn.microsoft.com/en-us/project/api/project-api-authentication
- aid: microsoft-project:csom-api
  name: Microsoft Project Online CSOM API
  description: Client-Side Object Model API for programmatic access to Project Online and Project Server.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://learn.microsoft.com/en-us/project/api/client-side-object-model-csom-for-project-2013
  baseURL: https://{tenant}.sharepoint.com/_api/ProjectServer
  tags:
  - .NET
  - Client Library
  - CSOM
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/project/api/client-side-object-model-csom-for-project-2013
  - type: SDKs
    url: https://www.nuget.org/packages/Microsoft.SharePointOnline.CSOM/
- aid: microsoft-project:graph-project-api
  name: Microsoft Graph Project API
  description: Access Project for the web data through Microsoft Graph API.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/project-rome-overview
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Dataverse
  - Microsoft Graph
  - Project for the Web
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/overview
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
name: Microsoft Project
tags:
- Microsoft
- Project Management
- Resource Management
- Scheduling
- Task Management
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Project is a project management software product developed by Microsoft for developing plans, assigning resources to tasks, tracking progress, managing budgets, and analyzing workloads. It provides REST APIs and Microsoft Graph access for programmatic project management.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

