---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Wrike Agentic Access
  operation_count: 48
  slug: wrike-agentic-access
  summary_line: 48 operations · 23 acting
api_count: 17
apis:
- description: The Wrike DataHub Public API provides programmatic access to raw analytical data from Wrike, enabling custom reporting and integration with downstream analytics platforms.
  name: Wrike DataHub Public API
  slug: datahub
- description: The Wrike BI Export API lets you export Wrike data into business intelligence tools such as Tableau, Power BI, and Looker for enterprise-grade reporting and analysis.
  name: Wrike BI Export API
  slug: bi-export
- description: The Wrike Cloud Content Connector enables management of cloud-based content assets within Wrike workflows, integrating external content providers with Wrike tasks and projects.
  name: Wrike Cloud Content Connector
  slug: cloud-content-connector
- description: The Wrike MCP Server connects Wrike directly to AI assistants such as Claude, ChatGPT, and Microsoft Copilot Studio using the Model Context Protocol, enabling AI-driven workflows over Wrike data.
  name: Wrike MCP Server
  slug: mcp-server
- description: Access role and permission management
  name: Wrike Access Roles API
  slug: wrike-access-roles-api
- description: Account settings and configuration
  name: Wrike Accounts API
  slug: wrike-accounts-api
- description: Available color palette
  name: Wrike Colors API
  slug: wrike-colors-api
- description: Task and folder comment management
  name: Wrike Comments API
  slug: wrike-comments-api
- description: Users and user groups in Wrike accounts
  name: Wrike Contacts API
  slug: wrike-contacts-api
- description: Custom field definitions and management
  name: Wrike Custom Fields API
  slug: wrike-custom-fields-api
- description: Folder and project hierarchy management
  name: Wrike Folders And Projects API
  slug: wrike-folders-and-projects-api
- description: User group management
  name: Wrike Groups API
  slug: wrike-groups-api
- description: Task creation, retrieval, updates, and deletion
  name: Wrike Tasks API
  slug: wrike-tasks-api
- description: Time tracking and timelog records
  name: Wrike Time Logs API
  slug: wrike-time-logs-api
- description: User management and profile operations
  name: Wrike Users API
  slug: wrike-users-api
- description: Event-driven webhook subscriptions
  name: Wrike Webhooks API
  slug: wrike-webhooks-api
- description: Workflow and status management
  name: Wrike Workflows API
  slug: wrike-workflows-api
artifact_total: 123
collections:
- collection_type: postman
  name: Wrike Access Roles API
  slug: postman-wrike-access-roles-api
- collection_type: postman
  name: Wrike Access Roles Accounts API
  slug: postman-wrike-accounts-api
- collection_type: postman
  name: Wrike Access Roles Colors API
  slug: postman-wrike-colors-api
- collection_type: postman
  name: Wrike Access Roles Comments API
  slug: postman-wrike-comments-api
- collection_type: postman
  name: Wrike Access Roles Contacts API
  slug: postman-wrike-contacts-api
- collection_type: postman
  name: Wrike Access Roles Custom Fields API
  slug: postman-wrike-custom-fields-api
- collection_type: postman
  name: Wrike Access Roles Folders And Projects API
  slug: postman-wrike-folders-and-projects-api
- collection_type: postman
  name: Wrike Access Roles Groups API
  slug: postman-wrike-groups-api
- collection_type: postman
  name: Wrike Access Roles Tasks API
  slug: postman-wrike-tasks-api
- collection_type: postman
  name: Wrike Access Roles Time Logs API
  slug: postman-wrike-time-logs-api
- collection_type: postman
  name: Wrike Access Roles Users API
  slug: postman-wrike-users-api
- collection_type: postman
  name: Wrike Access Roles Webhooks API
  slug: postman-wrike-webhooks-api
- collection_type: postman
  name: Wrike Access Roles Workflows API
  slug: postman-wrike-workflows-api
- collection_type: open
  name: Wrike API
  slug: open-wrike
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/wrike/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wrike-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wrike-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wrike-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wrike-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wrike-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wrike
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.wrike.com/
- group: start
  title: ''
  type: Signup
  url: https://www.wrike.com/free-trial/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wrike.com/price/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wrike.com/developer-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wrike.com/security/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wrike.com/
- group: operate
  title: ''
  type: Support
  url: https://help.wrike.com/hc/en-us/
- group: operate
  title: ''
  type: FAQ
  url: https://developers.wrike.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://www.wrike.com/blog/
- group: learn
  title: ''
  type: Webinars
  url: https://www.wrike.com/webinars/
- group: learn
  title: ''
  type: Training
  url: https://www.wrike.com/discover/
- group: other
  title: ''
  type: ProfessionalServices
  url: https://www.wrike.com/professional-services/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wrike
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.wrike.com/changelog/
- group: auth
  title: ''
  type: Compliance
  url: https://www.wrike.com/security/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/wrike/datahub-mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.wrike.com/llms.txt
created: '2025-01-08'
description: Wrike is a collaborative work management platform used by 30,000+ organizations. The Wrike Developer Platform exposes a REST API v4 for building integrations and automations against tasks, folders, projects, contacts, workflows, time tracking, custom fields, audit logs, and webhooks. The platform also offers the DataHub Public API for raw analytical data, a BI Export API for piping data into Tableau, Power BI, or Looker, a Cloud Content Connector for managing cloud-based content assets, and a Wrike MCP Server for connecting Wrike to AI assistants such as Claude, ChatGPT, and Microsoft Copilot Studio. Authentication is handled via OAuth 2.0 or permanent access tokens.
features:
- description: Autonomous AI agents that execute Wrike workflows on behalf of users.
  name: AI Agents
- description: Built-in AI assistant for question answering, summarization, and in-context productivity inside Wrike.
  name: Wrike Copilot
- description: Assign, track, and complete tasks across teams and projects.
  name: Task Management
- description: Interactive timeline planning and dependency management.
  name: Gantt Charts
- description: Real-time reporting and analytics dashboards on Wrike data.
  name: Dashboards
- description: Visual collaboration space for brainstorming and planning.
  name: Wrike Whiteboard
- description: Workload balancing and capacity planning for teams.
  name: Resource Management
- description: Custom rule-based automation across Wrike entities.
  name: Workflow Automation
- description: Review, markup, and sign-off tools for creative deliverables.
  name: Proofing & Approvals
- description: Hour logging, timesheets, and timelog lock periods.
  name: Time Tracking
- description: Conditional logic forms for intake and request management.
  name: Custom Request Forms
- description: Native cross-device clients for iOS, Android, macOS, and Windows.
  name: Mobile and Desktop Apps
- description: Pre-built integrations with third-party SaaS and enterprise tools.
  name: 400+ Integrations
- description: Data-driven insights and predictive analytics across the platform.
  name: Wrike Work Intelligence
- description: Model Context Protocol server for AI assistant integration.
  name: MCP Server
- description: Subscribe to real-time event notifications from Wrike.
  name: Webhooks
- description: Standards-based authorization for third-party app integrations.
  name: OAuth 2.0
finops:
- name: Wrike Finops
  service_category: Work Management SaaS
  slug: wrike-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Wrike work management and collaboration platform. Wrike exposes a REST API v4 at https://www.wrike.com/api/v4, and this schema models the eq
  name: Wrike GraphQL Schema
  slug: wrike-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wrike.png
integrations:
- description: Collaborate on Wrike tasks and projects from Microsoft Teams.
  name: Microsoft Teams
- description: Receive Wrike notifications and update tasks from Slack.
  name: Slack
- description: Connect Wrike work to Salesforce opportunities and accounts.
  name: Salesforce
- description: Integrate with Gmail, Google Calendar, and Google Drive for documents and scheduling.
  name: Google Workspace
- description: Integrate with Outlook, OneDrive, and SharePoint for email and document management.
  name: Microsoft 365
- description: Integrate with Photoshop, Illustrator, and InDesign for creative asset workflows.
  name: Adobe Creative Cloud
- description: Visualize Wrike data in Tableau via the BI Export API.
  name: Tableau
- description: Build BI reports on Wrike data via the BI Export API.
  name: Power BI
- description: Analyze Wrike data in Looker via the BI Export API.
  name: Looker
- description: Sync issues and tasks between Jira and Wrike.
  name: Jira
- description: Link development activity in GitHub to Wrike tasks.
  name: GitHub
- description: Connect Wrike with thousands of other apps via Zapier automations.
  name: Zapier
- description: Claude, ChatGPT, and Microsoft Copilot Studio connect to Wrike via the Wrike MCP Server.
  name: MCP Clients
json_schemas:
- name: AccessRole
  property_count: 4
  slug: wrike-accessrole
- name: AccessRoleListResponse
  property_count: 2
  slug: wrike-accessrolelistresponse
- name: Account
  property_count: 10
  slug: wrike-account
- name: AccountListResponse
  property_count: 2
  slug: wrike-accountlistresponse
- name: Color
  property_count: 2
  slug: wrike-color
- name: ColorListResponse
  property_count: 2
  slug: wrike-colorlistresponse
- name: Comment
  property_count: 7
  slug: wrike-comment
- name: CommentListResponse
  property_count: 2
  slug: wrike-commentlistresponse
- name: Contact
  property_count: 15
  slug: wrike-contact
- name: ContactListResponse
  property_count: 2
  slug: wrike-contactlistresponse
- name: CustomField
  property_count: 7
  slug: wrike-customfield
- name: CustomFieldListResponse
  property_count: 2
  slug: wrike-customfieldlistresponse
- name: CustomFieldValue
  property_count: 2
  slug: wrike-customfieldvalue
- name: Dates
  property_count: 4
  slug: wrike-dates
- name: Error
  property_count: 2
  slug: wrike-error
- name: Folder
  property_count: 13
  slug: wrike-folder
- name: FolderListResponse
  property_count: 2
  slug: wrike-folderlistresponse
- name: Group
  property_count: 7
  slug: wrike-group
- name: GroupListResponse
  property_count: 2
  slug: wrike-grouplistresponse
- name: Metadata
  property_count: 2
  slug: wrike-metadata
- name: Profile
  property_count: 6
  slug: wrike-profile
- name: Project
  property_count: 6
  slug: wrike-project
- name: Task
  property_count: 27
  slug: wrike-task
- name: TaskListResponse
  property_count: 4
  slug: wrike-tasklistresponse
- name: Timelog
  property_count: 7
  slug: wrike-timelog
- name: TimelogListResponse
  property_count: 2
  slug: wrike-timeloglistresponse
- name: User
  property_count: 10
  slug: wrike-user
- name: UserResponse
  property_count: 2
  slug: wrike-userresponse
- name: Webhook
  property_count: 10
  slug: wrike-webhook
- name: WebhookListResponse
  property_count: 2
  slug: wrike-webhooklistresponse
- name: Workflow
  property_count: 5
  slug: wrike-workflow
- name: WorkflowListResponse
  property_count: 2
  slug: wrike-workflowlistresponse
- name: WorkflowStatus
  property_count: 6
  slug: wrike-workflowstatus
json_structures:
- name: Wrike Structure
  property_count: 0
  slug: wrike-structure
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Wrike
nav: Providers
network: true
overview: 'Wrike publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Access Roles API, Accounts API, Colors API, and 10 more. Tagged areas include Work Management, Project Management, Collaboration, Productivity, and Workflow Automation.


  The Wrike catalog on APIs.io includes 1 Spectral governance ruleset.


  Wrike''s developer surface includes authentication, signup flow, pricing, support, FAQ, engineering blog, training material, and 17 more developer resources.'
plans:
- name: Wrike Plans Pricing
  plan_count: 11
  slug: wrike-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 1
  name: Wrike Rate Limits
  slug: wrike-rate-limits
rules:
- name: Wrike API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wrike-jsonschema-spectral-rules
scopes:
- name: Wrike Scopes
  scope_count: 6
  slug: wrike-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: strong
  composite: 61.0
  delta: -2.3
  facets:
    commercial_clarity: 78.9
    contract_quality: 65.7
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 57.9
  previous_composite: 63.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wrike/refs/heads/main/screenshots/wrike-2026-06-20T201636.png
security:
- kind: authentication
  name: Wrike Authentication
  slug: wrike-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Wrike Domain Security
  slug: wrike-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wrike Vulnerability Disclosure
  slug: wrike-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wrike
solutions:
- description: Solutions tailored for marketing operations and campaigns.
  name: Marketing Teams
- description: Solutions for product roadmaps and lifecycle management.
  name: Product Management Teams
- description: Project management office governance and portfolio reporting.
  name: PMO
- description: Streamline operational workflows across the business.
  name: Operations Teams
- description: Creative production, proofing, and asset management.
  name: Creative and Design Teams
- description: IT request intake, change management, and project delivery.
  name: IT Teams
- description: Manage client engagements, billable hours, and delivery.
  name: Professional Services
- description: Cross-functional business process management.
  name: Business Operations
tags:
- Work Management
- Project Management
- Collaboration
- Productivity
- Workflow Automation
- Task Management
use_cases:
- description: Plan, execute, and track projects end to end.
  name: Project Management
- description: Coordinate marketing campaigns across teams and channels.
  name: Campaign Management
- description: Manage client engagements, deliverables, and SLAs in agencies and professional services.
  name: Client Service Delivery
- description: Govern portfolios of projects with prioritization and reporting.
  name: Project Portfolio Management
- description: Manage product roadmaps, releases, and cross-functional delivery.
  name: Product Lifecycle Management
- description: Run creative briefs, asset production, proofing, and approvals.
  name: Creative Production
- description: Coordinate individual and team tasks at scale.
  name: Task Management
- description: Forecast and balance workload across people and teams.
  name: Resource Management
- description: Run a creative or marketing agency with billable time, projects, and client portals.
  name: Agency Management
website: https://developers.wrike.com/
---
