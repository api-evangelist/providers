---
aid: atlassian-jira
name: Atlassian Jira
description: |
  Jira is a leading issue tracking and project management platform developed by Atlassian. It provides REST APIs for Jira Cloud Platform, Jira Software, and Jira Service Management enabling programmatic management of issues, projects, workflows, boards, sprints, users, and service desk requests with OAuth 2.0 authentication.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agile
  - Atlassian
  - Bug Tracking
  - Issue Tracking
  - ITSM
  - Kanban
  - Project Management
  - Scrum
  - Service Desk
url: https://raw.githubusercontent.com/api-evangelist/atlassian-jira/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
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
      - Itsm
      - Service Desk
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/
      - type: OpenAPI
        url: https://developer.atlassian.com/cloud/jira/service-desk/swagger.v3.json
common:
  - type: Website
    url: https://www.atlassian.com/software/jira
  - type: Documentation
    url: https://developer.atlassian.com/cloud/jira/platform/
  - type: Getting Started
    url: https://developer.atlassian.com/cloud/jira/platform/getting-started/
  - type: Authentication
    url: https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/
  - type: Pricing
    url: https://www.atlassian.com/software/jira/pricing
  - type: Status
    url: https://status.atlassian.com/
  - type: Support
    url: https://support.atlassian.com/
  - type: Community
    url: https://community.developer.atlassian.com/
  - type: Terms of Service
    url: https://www.atlassian.com/legal/cloud-terms-of-service
  - type: Privacy Policy
    url: https://www.atlassian.com/legal/privacy-policy
  - type: GitHub Organization
    url: https://github.com/atlassian
  - type: Blog
    url: https://developer.atlassian.com/blog/
  - type: RateLimits
    url: https://developer.atlassian.com/cloud/jira/platform/rate-limiting/
  - type: Features
    data:
      - name: Issue Management
        description: Create, update, transition, and delete Jira issues with full support for custom fields, attachments, comments, and workflow transitions.
      - name: Project Management
        description: Manage Jira projects including project categories, components, versions, and project-level configurations.
      - name: Board and Sprint Management
        description: Create and manage Scrum boards, sprints, and Kanban boards for agile project planning and execution.
      - name: Service Desk
        description: Manage service desk projects, request types, queues, and SLA data for IT service management workflows.
      - name: Workflow Configuration
        description: Programmatically configure Jira workflows, statuses, transitions, and screen configurations.
      - name: Forge App Development
        description: Build Jira apps using the Atlassian Forge platform with serverless functions and UI modules.
  - type: UseCases
    data:
      - name: Issue Automation
        description: Automate issue creation, assignment, and transitions from CI/CD pipelines, monitoring alerts, and external systems.
      - name: Project Reporting
        description: Extract issue data, sprint velocity, and project metrics for custom reporting and analytics dashboards.
      - name: ITSM Integration
        description: Integrate Jira Service Management with external monitoring, CMDB, and ITSM tools for incident and change management.
      - name: DevOps Pipeline Integration
        description: Link Jira issues to commits, branches, builds, and deployments from GitHub, Bitbucket, and Jenkins.
      - name: Custom Field Automation
        description: Synchronize custom field data between Jira and external systems for portfolio tracking and compliance reporting.
  - type: Integrations
    data:
      - name: Confluence
        description: Link Jira projects and issues to Confluence spaces and pages for integrated project documentation.
      - name: Bitbucket
        description: Connect Bitbucket repositories to Jira for branch, commit, and pull request linking.
      - name: GitHub
        description: Integrate GitHub with Jira via the GitHub for Jira app for development activity tracking.
      - name: Slack
        description: Receive Jira issue notifications and create issues directly from Slack using the Jira for Slack app.
      - name: Jenkins
        description: Connect Jenkins build and deployment events to Jira issues via the Atlassian Jenkins plugin.
      - name: PagerDuty
        description: Create Jira issues automatically from PagerDuty incidents for integrated incident management.
  - type: Solutions
    data:
      - name: Agile Project Management
        description: Manage software development with Scrum and Kanban boards, sprint planning, and backlog management.
      - name: IT Service Management
        description: Provide enterprise ITSM with service catalogs, SLAs, queues, and approval workflows via Jira Service Management.
      - name: Business Process Tracking
        description: Track any business process or workflow using customizable Jira projects and issue types for non-software teams.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
