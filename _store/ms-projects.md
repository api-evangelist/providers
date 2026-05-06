---
aid: ms-projects
name: Microsoft Project APIs
description: APIs for Microsoft Project, including Project for the web, Project Online, and Project Server.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Collaboration
  - Microsoft 365
  - Project Management
  - Resources
  - Scheduling
  - Tasks
created: '2024-01-15'
modified: '2026-04-28'
url: https://www.microsoft.com/en-us/microsoft-365/project
specificationVersion: '0.19'
apis:
  - name: Microsoft Project Online API
    description: REST API for accessing and managing Project Online data, including projects, tasks, resources, and assignments.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.microsoft.com/en-us/project/
    baseURL: https://graph.microsoft.com/v1.0/
    tags:
      - Project Online
      - REST
      - SharePoint
      - Tasks
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/previous-versions/office/project-javascript-api/jj712612(v=office.15)
      - type: Authentication
        url: https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/authorization-and-authentication-of-sharepoint-add-ins
  - name: Microsoft Graph Project API
    description: Microsoft Graph API for Project for the web, enabling access to projects, tasks, and bucket management.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.microsoft.com/en-us/graph
    baseURL: https://graph.microsoft.com/v1.0/
    tags:
      - Microsoft Graph
      - Project for the Web
      - Tasks
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/api/resources/project-rome-overview
      - type: Authentication
        url: https://docs.microsoft.com/en-us/graph/auth/
  - name: Microsoft Project Server CSOM API
    description: Client-Side Object Model (CSOM) API for Project Server, providing programmatic access to Project Server data.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.microsoft.com/en-us/project/
    tags:
      - CSOM
      - .NET
      - On-Premises
      - Project Server
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/previous-versions/office/project-server-2010/ee767622(v=office.14)
      - type: Code Samples
        url: https://docs.microsoft.com/en-us/project/api/project-api-code-samples
      - type: SDKs
        url: https://www.nuget.org/packages/Microsoft.SharePointOnline.CSOM/
common:
  - type: Portal
    url: https://developer.microsoft.com/
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/project-blog/bg-p/ProjectBlog
  - type: Status
    url: https://status.microsoft.com/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/servicesagreement
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
