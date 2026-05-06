---
aid: wrike
name: Wrike
description: Wrike is a collaborative work management platform used by 30,000+ organizations. The Wrike Developer Platform exposes a REST API v4 for building integrations and automations against tasks, folders, projects, contacts, workflows, time tracking, custom fields, audit logs, and webhooks. The platform also offers the DataHub Public API for raw analytical data, a BI Export API for piping data into Tableau, Power BI, or Looker, a Cloud Content Connector for managing cloud-based content assets, and a Wrike MCP Server for connecting Wrike to AI assistants such as Claude, ChatGPT, and Microsoft Copilot Studio. Authentication is handled via OAuth 2.0 or permanent access tokens.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Work Management
  - Project Management
  - Collaboration
  - Productivity
  - Workflow Automation
  - Task Management
created: '2025-01-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/wrike/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: wrike:wrike
    name: Wrike API
    description: The Wrike REST API v4 enables developers to build integrations and automations for Wrike. The API provides programmatic access to tasks, folders, projects, contacts, workflows, time tracking, timesheets, custom fields, audit logs, webhooks, and more. Authentication uses OAuth 2.0 or permanent access tokens, and the base URL is https://www.wrike.com/api/v4.
    humanURL: https://developers.wrike.com/api/v4/
    baseURL: https://www.wrike.com/api/v4
    tags:
      - REST API
      - Work Management
      - Project Management
      - Tasks
      - Workflows
      - Webhooks
    properties:
      - type: Documentation
        url: https://developers.wrike.com/
      - type: APIReference
        url: https://developers.wrike.com/api/v4/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/wrike/refs/heads/main/openapi/wrike-openapi.yml
      - type: Authentication
        url: https://developers.wrike.com/oauth-2-0-authorization
      - type: GettingStarted
        url: https://developers.wrike.com/getting-started/
      - type: ChangeLog
        url: https://developers.wrike.com/changelog/
  - aid: wrike:datahub
    name: Wrike DataHub Public API
    description: The Wrike DataHub Public API provides programmatic access to raw analytical data from Wrike, enabling custom reporting and integration with downstream analytics platforms.
    humanURL: https://developers.wrike.com/datahub-public-api/
    tags:
      - Analytics
      - Reporting
      - DataHub
    properties:
      - type: Documentation
        url: https://developers.wrike.com/datahub-public-api/
  - aid: wrike:bi-export
    name: Wrike BI Export API
    description: The Wrike BI Export API lets you export Wrike data into business intelligence tools such as Tableau, Power BI, and Looker for enterprise-grade reporting and analysis.
    humanURL: https://developers.wrike.com/bi-export-api/
    tags:
      - Business Intelligence
      - Export
      - Analytics
    properties:
      - type: Documentation
        url: https://developers.wrike.com/bi-export-api/
  - aid: wrike:cloud-content-connector
    name: Wrike Cloud Content Connector
    description: The Wrike Cloud Content Connector enables management of cloud-based content assets within Wrike workflows, integrating external content providers with Wrike tasks and projects.
    humanURL: https://developers.wrike.com/cloud-content-connector/
    tags:
      - Content Management
      - Cloud Storage
      - Connector
    properties:
      - type: Documentation
        url: https://developers.wrike.com/cloud-content-connector/
  - aid: wrike:mcp-server
    name: Wrike MCP Server
    description: The Wrike MCP Server connects Wrike directly to AI assistants such as Claude, ChatGPT, and Microsoft Copilot Studio using the Model Context Protocol, enabling AI-driven workflows over Wrike data.
    humanURL: https://developers.wrike.com/mcp-server/
    tags:
      - MCP
      - AI
      - Model Context Protocol
    properties:
      - type: Documentation
        url: https://developers.wrike.com/mcp-server/
common:
  - type: DeveloperPortal
    url: https://developers.wrike.com/
  - type: SignUp
    url: https://www.wrike.com/free-trial/
  - type: Pricing
    url: https://www.wrike.com/price/
  - type: TermsOfService
    url: https://www.wrike.com/developer-terms/
  - type: PrivacyPolicy
    url: https://www.wrike.com/security/privacy/
  - type: StatusPage
    url: https://status.wrike.com/
  - type: Support
    url: https://help.wrike.com/hc/en-us/
  - type: FAQ
    url: https://developers.wrike.com/faq/
  - type: Blog
    url: https://www.wrike.com/blog/
  - type: Webinars
    url: https://www.wrike.com/webinars/
  - type: Training
    url: https://www.wrike.com/discover/
  - type: ProfessionalServices
    url: https://www.wrike.com/professional-services/
  - type: GitHubOrganization
    url: https://github.com/wrike
  - type: ChangeLog
    url: https://developers.wrike.com/changelog/
  - type: Compliance
    url: https://www.wrike.com/security/
  - type: Features
    data:
      - name: AI Agents
        description: Autonomous AI agents that execute Wrike workflows on behalf of users.
      - name: Wrike Copilot
        description: Built-in AI assistant for question answering, summarization, and in-context productivity inside Wrike.
      - name: Task Management
        description: Assign, track, and complete tasks across teams and projects.
      - name: Gantt Charts
        description: Interactive timeline planning and dependency management.
      - name: Dashboards
        description: Real-time reporting and analytics dashboards on Wrike data.
      - name: Wrike Whiteboard
        description: Visual collaboration space for brainstorming and planning.
      - name: Resource Management
        description: Workload balancing and capacity planning for teams.
      - name: Workflow Automation
        description: Custom rule-based automation across Wrike entities.
      - name: Proofing & Approvals
        description: Review, markup, and sign-off tools for creative deliverables.
      - name: Time Tracking
        description: Hour logging, timesheets, and timelog lock periods.
      - name: Custom Request Forms
        description: Conditional logic forms for intake and request management.
      - name: Mobile and Desktop Apps
        description: Native cross-device clients for iOS, Android, macOS, and Windows.
      - name: 400+ Integrations
        description: Pre-built integrations with third-party SaaS and enterprise tools.
      - name: Wrike Work Intelligence
        description: Data-driven insights and predictive analytics across the platform.
      - name: MCP Server
        description: Model Context Protocol server for AI assistant integration.
      - name: Webhooks
        description: Subscribe to real-time event notifications from Wrike.
      - name: OAuth 2.0
        description: Standards-based authorization for third-party app integrations.
  - type: UseCases
    data:
      - name: Project Management
        description: Plan, execute, and track projects end to end.
      - name: Campaign Management
        description: Coordinate marketing campaigns across teams and channels.
      - name: Client Service Delivery
        description: Manage client engagements, deliverables, and SLAs in agencies and professional services.
      - name: Project Portfolio Management
        description: Govern portfolios of projects with prioritization and reporting.
      - name: Product Lifecycle Management
        description: Manage product roadmaps, releases, and cross-functional delivery.
      - name: Creative Production
        description: Run creative briefs, asset production, proofing, and approvals.
      - name: Task Management
        description: Coordinate individual and team tasks at scale.
      - name: Resource Management
        description: Forecast and balance workload across people and teams.
      - name: Agency Management
        description: Run a creative or marketing agency with billable time, projects, and client portals.
  - type: Solutions
    data:
      - name: Marketing Teams
        description: Solutions tailored for marketing operations and campaigns.
      - name: Product Management Teams
        description: Solutions for product roadmaps and lifecycle management.
      - name: PMO
        description: Project management office governance and portfolio reporting.
      - name: Operations Teams
        description: Streamline operational workflows across the business.
      - name: Creative and Design Teams
        description: Creative production, proofing, and asset management.
      - name: IT Teams
        description: IT request intake, change management, and project delivery.
      - name: Professional Services
        description: Manage client engagements, billable hours, and delivery.
      - name: Business Operations
        description: Cross-functional business process management.
  - type: Integrations
    data:
      - name: Microsoft Teams
        description: Collaborate on Wrike tasks and projects from Microsoft Teams.
      - name: Slack
        description: Receive Wrike notifications and update tasks from Slack.
      - name: Salesforce
        description: Connect Wrike work to Salesforce opportunities and accounts.
      - name: Google Workspace
        description: Integrate with Gmail, Google Calendar, and Google Drive for documents and scheduling.
      - name: Microsoft 365
        description: Integrate with Outlook, OneDrive, and SharePoint for email and document management.
      - name: Adobe Creative Cloud
        description: Integrate with Photoshop, Illustrator, and InDesign for creative asset workflows.
      - name: Tableau
        description: Visualize Wrike data in Tableau via the BI Export API.
      - name: Power BI
        description: Build BI reports on Wrike data via the BI Export API.
      - name: Looker
        description: Analyze Wrike data in Looker via the BI Export API.
      - name: Jira
        description: Sync issues and tasks between Jira and Wrike.
      - name: GitHub
        description: Link development activity in GitHub to Wrike tasks.
      - name: Zapier
        description: Connect Wrike with thousands of other apps via Zapier automations.
      - name: MCP Clients
        description: Claude, ChatGPT, and Microsoft Copilot Studio connect to Wrike via the Wrike MCP Server.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
