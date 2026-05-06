---
name: Jira
description: APIs for Atlassian Jira project management and issue tracking platform.
image: https://www.atlassian.com/dam/jcr:e33efd9e-e0b8-4d61-a24d-68a48ef9bbe4/jira-icon-blue.svg
url: https://www.atlassian.com/software/jira
created: '2024'
modified: '2026-05-04'
specificationVersion: '0.18'
tags:
  - Agile
  - Issue Tracking
  - ITSM
  - Project Management
  - Service Management
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
      - type: RateLimits
        url: https://developer.atlassian.com/cloud/jira/platform/rate-limiting/
      - type: ChangeLog
        url: https://developer.atlassian.com/cloud/jira/platform/changelog/
      - type: Security
        url: https://developer.atlassian.com/cloud/jira/platform/security-overview/
      - type: GettingStarted
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
      - type: ChangeLog
        url: https://developer.atlassian.com/cloud/jira/platform/changelog/
      - type: Security
        url: https://developer.atlassian.com/cloud/jira/platform/security-overview/
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
      - type: CodeExamples
        url: https://developer.atlassian.com/cloud/jira/software/rest/intro/#examples
      - type: ChangeLog
        url: https://developer.atlassian.com/cloud/jira/software/changelog/
      - type: Security
        url: https://developer.atlassian.com/cloud/jira/software/security-overview/
      - type: GettingStarted
        url: https://developer.atlassian.com/cloud/jira/software/getting-started-with-forge/
      - type: Authentication
        url: https://developer.atlassian.com/cloud/jira/software/security-overview/
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
      - type: ChangeLog
        url: https://developer.atlassian.com/cloud/jira/service-desk/changelog/
      - type: Security
        url: https://developer.atlassian.com/cloud/jira/service-desk/security-overview/
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
      - type: GettingStarted
        url: https://help.jiraalign.com/hc/en-us/articles/360045371954-Getting-started-with-the-REST-API-2-0
      - type: RateLimits
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
      - type: GettingStarted
        url: https://developer.atlassian.com/cloud/customer-service-management/
maintainers:
  - name: Atlassian
    email: ecosystem@atlassian.com
    url: https://www.atlassian.com
  - name: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://developer.atlassian.com/cloud/jira/platform/
  - type: GettingStarted
    url: https://developer.atlassian.com/cloud/jira/platform/getting-started/
  - type: SDK
    url: https://developer.atlassian.com/cloud/jira/platform/libraries/
  - type: Authentication
    url: https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/
    title: OAuth 2.0
  - type: Support
    url: https://support.atlassian.com/
  - type: StatusPage
    url: https://status.atlassian.com/
  - type: TermsOfService
    url: https://www.atlassian.com/legal/cloud-terms-of-service
  - type: PrivacyPolicy
    url: https://www.atlassian.com/legal/privacy-policy
  - type: ChangeLog
    url: https://developer.atlassian.com/changelog/
  - type: Blog
    url: https://www.atlassian.com/blog/developer
  - type: Marketplace
    url: https://developer.atlassian.com/platform/marketplace/getting-started/
  - type: RateLimits
    url: https://developer.atlassian.com/cloud/jira/platform/rate-limiting/
  - type: Security
    url: https://developer.atlassian.com/cloud/jira/platform/security-overview/
  - type: JSONSchema
    url: json-schema/jira-issue-schema.json
    name: Jira Issue Schema
  - type: JSONSchema
    url: json-schema/jira-project-schema.json
    name: Jira Project Schema
  - type: JSONLD
    url: json-ld/jira-context.jsonld
    name: Jira JSON-LD Context
  - type: Features
    data:
      - 'Free: up to 10 users'
      - 'Standard: $7.91-$9.05/user/mo (volume tiered)'
      - 'Premium: $14.54-$18.30/user/mo with Advanced Roadmaps'
      - 'Enterprise custom: Atlassian Intelligence, 99.95% uptime, data residency'
      - 'Volume discount: rates drop above 100 users (max 50K)'
      - REST API v3 at api.atlassian.com
      - GraphQL API for some products
      - Token-bucket rate limit ~10 req/sec/app/user
      - Bulk operations max 100 items/request
      - Webhooks v3 for issue/project events
      - OAuth 2.0 (3LO) and API tokens
      - Atlassian Connect framework for marketplace apps
      - Forge for serverless app development
      - JQL (Jira Query Language) for advanced search
      - Atlassian Intelligence AI assistant (Enterprise)
      - Cross-product Analytics + Atlas integrations
    sources:
      - https://www.atlassian.com/software/jira/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Issue Tracking Automation
        description: Automate issue creation, assignment, and transitions based on external events from CI/CD pipelines, monitoring tools, or customer feedback systems.
      - name: Sprint Management
        description: Programmatically manage sprints, backlogs, and board configurations for automated agile workflow orchestration.
      - name: Service Desk Integration
        description: Integrate customer support channels with Jira Service Management for automated ticket creation and SLA tracking.
      - name: Incident Management
        description: Automate incident response workflows with on-call scheduling, alert routing, and escalation management.
      - name: Enterprise Agile Planning
        description: Connect portfolio planning tools with Jira Align for cross-team dependency tracking and program-level reporting.
  - type: Integrations
    data:
      - name: Confluence
        description: Link Jira issues to Confluence pages for seamless knowledge management and documentation alongside project tracking.
      - name: Bitbucket
        description: Connect code repositories to Jira issues for automated status updates, smart commits, and development tracking.
      - name: GitHub
        description: Link GitHub pull requests, branches, and commits to Jira issues for end-to-end development visibility.
      - name: Slack
        description: Create and manage Jira issues from Slack channels with bi-directional notifications and status updates.
      - name: Microsoft Teams
        description: Receive Jira notifications and manage issues directly from Microsoft Teams conversations.
---
