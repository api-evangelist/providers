---
aid: atlassian-jira
url: https://raw.githubusercontent.com/api-evangelist/atlassian-jira/refs/heads/main/apis.yml
apis:
- aid: atlassian-jira:jira-cloud-platform-rest-api
  name: Jira Cloud Platform REST API
  description: The Jira Cloud platform REST API enables developers to interact with Jira issues, projects, workflows, users, and more.
  humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/
  baseURL: https://your-domain.atlassian.net/rest/api/3
  tags:
  - Agile
  - Issues
  - Projects
  - Workflows
  properties:
  - type: Documentation
    url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/
  - type: OpenAPI
    url: https://developer.atlassian.com/cloud/jira/platform/swagger-v3.v3.json
  - type: Authentication
    url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#authentication
- aid: atlassian-jira:jira-software-cloud-rest-api
  name: Jira Software Cloud REST API
  description: REST API for Jira Software Cloud specific features including boards, sprints, and backlog management.
  humanURL: https://developer.atlassian.com/cloud/jira/software/rest/intro/
  baseURL: https://your-domain.atlassian.net/rest/agile/1.0
  tags:
  - Agile
  - Boards
  - Kanban
  - Scrum
  properties:
  - type: Documentation
    url: https://developer.atlassian.com/cloud/jira/software/rest/intro/
  - type: OpenAPI
    url: https://developer.atlassian.com/cloud/jira/software/swagger.v3.json
- aid: atlassian-jira:jira-service-management-rest-api
  name: Jira Service Management REST API
  description: REST API for Jira Service Management features including request types, service desk queues, and customer portals.
  humanURL: https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/
  baseURL: https://your-domain.atlassian.net/rest/servicedeskapi
  tags:
  - Customer Support
  - ITSM
  - Service Desk
  properties:
  - type: Documentation
    url: https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/
  - type: OpenAPI
    url: https://developer.atlassian.com/cloud/jira/service-desk/swagger.v3.json
name: Atlassian Jira
tags:
- Agile
- Bug Tracking
- Issue Tracking
- ITSM
- Kanban
- Project Management
- Scrum
- Service Desk
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Jira is a proprietary issue tracking product developed by Atlassian that allows bug tracking and agile project management. It provides REST APIs for managing issues, projects, workflows, users, and boards across Jira Cloud, Jira Software, and Jira Service Management.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

