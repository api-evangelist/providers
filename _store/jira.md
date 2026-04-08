---
aid: jira
url: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/apis.yml
apis:
- name: Jira Cloud Platform REST API
  description: The Jira Cloud platform REST API for building apps and integrations.
  image: https://www.atlassian.com/dam/jcr:e33efd9e-e0b8-4d61-a24d-68a48ef9bbe4/jira-icon-blue.svg
  humanURL: https://developer.atlassian.com/cloud/jira/platform/
  baseURL: https://your-domain.atlassian.net/rest/api/3
  tags:
  - Agile
  - Issues
  - Project Management
  - Projects
  - Workflows
  properties:
  - type: Documentation
    url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/
  - type: OpenAPI
    url: https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json
  - type: OpenAPI
    url: openapi/jira-cloud-platform-rest-api-openapi.yml
  - type: AsyncAPI
    url: asyncapi/jira-webhooks-asyncapi.yml
  - type: Authentication
    url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#authentication
  - type: Rate Limits
    url: https://developer.atlassian.com/cloud/jira/platform/rate-limiting/
  - type: Change Log
    url: https://developer.atlassian.com/cloud/jira/platform/changelog/
  - type: Deprecation Policy
    url: https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/
  - type: Security
    url: https://developer.atlassian.com/cloud/jira/platform/security-overview/
  - type: OAuth Scopes
    url: https://developer.atlassian.com/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/
  - type: Basic Authentication
    url: https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/
  - type: Pagination
    url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#pagination
  - type: Expansion
    url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#expansion
  - type: Jira Expressions
    url: https://developer.atlassian.com/cloud/jira/platform/jira-expressions/
  - type: Getting Started
    url: https://developer.atlassian.com/cloud/jira/platform/getting-started/
- name: Jira Cloud Platform REST API v2
  description: Version 2 of the Jira Cloud platform REST API, offering the same operations as v3 but without Atlassian Document Format support.
  image: https://www.atlassian.com/dam/jcr:e33efd9e-e0b8-4d61-a24d-68a48ef9bbe4/jira-icon-blue.svg
  humanURL: https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/
  baseURL: https://your-domain.atlassian.net/rest/api/2
  tags:
  - Issues
  - Legacy
  - Project Management
  - Projects
  - Workflows
  properties:
  - type: Documentation
    url: https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/
  - type: Authentication
    url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#authentication
  - type: Change Log
    url: https://developer.atlassian.com/cloud/jira/platform/changelog/
  - type: Security
    url: https://developer.atlassian.com/cloud/jira/platform/security-overview/
  - type: Basic Authentication
    url: https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/
- name: Jira Software Cloud REST API
  description: REST API for Jira Software features including boards, sprints, and backlogs.
  image: https://www.atlassian.com/dam/jcr:e33efd9e-e0b8-4d61-a24d-68a48ef9bbe4/jira-icon-blue.svg
  humanURL: https://developer.atlassian.com/cloud/jira/software/
  baseURL: https://your-domain.atlassian.net/rest/agile/1.0
  tags:
  - Agile
  - Boards
  - Kanban
  - Scrum
  - Sprints
  properties:
  - type: Documentation
    url: https://developer.atlassian.com/cloud/jira/software/rest/intro/
  - type: OpenAPI
    url: https://dac-static.atlassian.com/cloud/jira/software/swagger.v3.json
  - type: Examples
    url: https://developer.atlassian.com/cloud/jira/software/rest/intro/#examples
  - type: Change Log
    url: https://developer.atlassian.com/cloud/jira/software/changelog/
  - type: Security
    url: https://developer.atlassian.com/cloud/jira/software/security-overview/
  - type: Getting Started
    url: https://developer.atlassian.com/cloud/jira/software/getting-started-with-forge/
  - type: Authentication
    url: https://developer.atlassian.com/cloud/jira/software/security-overview/
  - type: Basic Authentication
    url: https://developer.atlassian.com/cloud/jira/software/basic-auth-for-rest-apis/
  - type: OAuth 2.0
    url: https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/
- name: Jira Service Management REST API
  description: REST API for Jira Service Management features including queues, customers, requests, and SLAs.
  image: https://www.atlassian.com/dam/jcr:e33efd9e-e0b8-4d61-a24d-68a48ef9bbe4/jira-icon-blue.svg
  humanURL: https://developer.atlassian.com/cloud/jira/service-desk/
  baseURL: https://your-domain.atlassian.net/rest/servicedeskapi
  tags:
  - Customers
  - ITSM
  - Requests
  - Service Desk
  - SLA
  properties:
  - type: Documentation
    url: https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/
  - type: OpenAPI
    url: https://dac-static.atlassian.com/cloud/jira/service-desk/swagger.v3.json
  - type: Change Log
    url: https://developer.atlassian.com/cloud/jira/service-desk/changelog/
  - type: Security
    url: https://developer.atlassian.com/cloud/jira/service-desk/security-overview/
  - type: Basic Authentication
    url: https://developer.atlassian.com/cloud/jira/service-desk/basic-auth-for-rest-apis/
  - type: OAuth 2.0
    url: https://developer.atlassian.com/cloud/jira/service-desk/oauth-2-authorization-code-grants-3lo-for-apps/
- name: Jira Service Management Operations REST API
  description: Operations APIs for Jira Service Management covering schedules, on-call rotations, alerts, escalations, and incident management.
  image: https://www.atlassian.com/dam/jcr:e33efd9e-e0b8-4d61-a24d-68a48ef9bbe4/jira-icon-blue.svg
  humanURL: https://developer.atlassian.com/cloud/jira/service-desk-ops/introduction/introduction/
  baseURL: https://api.atlassian.com/jsm/ops/api/{cloudId}
  tags:
  - Alerts
  - Escalations
  - Incidents
  - On-Call
  - Operations
  - Schedules
  properties:
  - type: Documentation
    url: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/intro/
  - type: Authentication
    url: https://developer.atlassian.com/cloud/jira/service-desk-ops/security/basic-auth-for-rest-apis/
  - type: OAuth 2.0
    url: https://developer.atlassian.com/cloud/jira/service-desk-ops/security/oauth-2-3lo-apps/
  - type: Integration Events API
    url: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v1/
  - type: Services API
    url: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v3/
- name: Jira Align REST API
  description: REST API for Jira Align enterprise agile planning platform, providing access to portfolios, epics, features, and program management data.
  image: https://www.atlassian.com/dam/jcr:e33efd9e-e0b8-4d61-a24d-68a48ef9bbe4/jira-icon-blue.svg
  humanURL: https://help.jiraalign.com/hc/en-us/articles/360045371954-Getting-started-with-the-REST-API-2-0
  baseURL: https://your-domain.jiraalign.com/rest/align/api/2
  tags:
  - Enterprise Agile
  - Planning
  - Portfolios
  - Program Management
  - SAFe
  properties:
  - type: Documentation
    url: https://help.jiraalign.com/hc/en-us/sections/360008049974-API-2-0
  - type: Getting Started
    url: https://help.jiraalign.com/hc/en-us/articles/360045371954-Getting-started-with-the-REST-API-2-0
  - type: Rate Limits
    url: https://help.jiraalign.com/hc/en-us/articles/360045371954-Getting-started-with-the-REST-API-2-0
  - type: Authentication
    url: https://help.jiraalign.com/hc/en-us/articles/360045371954-Getting-started-with-the-REST-API-2-0
- name: Jira Customer Service Management REST API
  description: REST API for Atlassian Customer Service Management providing access to customers, organizations, products, and entitlements data.
  image: https://www.atlassian.com/dam/jcr:e33efd9e-e0b8-4d61-a24d-68a48ef9bbe4/jira-icon-blue.svg
  humanURL: https://developer.atlassian.com/cloud/customer-service-management/
  baseURL: https://your-domain.atlassian.net
  tags:
  - Customer Service
  - Customers
  - Entitlements
  - Organizations
  properties:
  - type: Documentation
    url: https://developer.atlassian.com/cloud/customer-service-management/rest/v1/api-group-customer/
  - type: Authentication
    url: https://developer.atlassian.com/cloud/customer-service-management/apis/narratives/authentication/
  - type: Getting Started
    url: https://developer.atlassian.com/cloud/customer-service-management/
name: Jira
tags:
- API
type: Contract
image: https://www.atlassian.com/dam/jcr:e33efd9e-e0b8-4d61-a24d-68a48ef9bbe4/jira-icon-blue.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for Atlassian Jira project management and issue tracking platform.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

