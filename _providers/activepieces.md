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
  band: agent-aware
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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Activepieces Agentic Access
  operation_count: 27
  slug: activepieces-agentic-access
  summary_line: 27 operations · 14 acting
api_count: 9
apis:
- description: Manage third-party app connections
  name: Activepieces Connections API
  slug: activepieces-connections-api
- description: Access execution history and run details
  name: Activepieces Flow Runs API
  slug: activepieces-flow-runs-api
- description: Manage automation workflows
  name: Activepieces Flows API
  slug: activepieces-flows-api
- description: Organize flows with folders
  name: Activepieces Folders API
  slug: activepieces-folders-api
- description: Manage integration pieces
  name: Activepieces Pieces API
  slug: activepieces-pieces-api
- description: Project management
  name: Activepieces Projects API
  slug: activepieces-projects-api
- description: Flow templates
  name: Activepieces Templates API
  slug: activepieces-templates-api
- description: User management
  name: Activepieces Users API
  slug: activepieces-users-api
- description: Worker queue metrics
  name: Activepieces Worker Machines API
  slug: activepieces-worker-machines-api
artifact_total: 134
collections:
- collection_type: postman
  name: Activepieces Connections API
  slug: postman-activepieces-connections-api
- collection_type: postman
  name: Activepieces Connections Flow Runs API
  slug: postman-activepieces-flow-runs-api
- collection_type: postman
  name: Activepieces Connections Flows API
  slug: postman-activepieces-flows-api
- collection_type: postman
  name: Activepieces Connections Folders API
  slug: postman-activepieces-folders-api
- collection_type: postman
  name: Activepieces Connections Pieces API
  slug: postman-activepieces-pieces-api
- collection_type: postman
  name: Activepieces Connections Projects API
  slug: postman-activepieces-projects-api
- collection_type: postman
  name: Activepieces Connections Templates API
  slug: postman-activepieces-templates-api
- collection_type: postman
  name: Activepieces Connections Users API
  slug: postman-activepieces-users-api
- collection_type: postman
  name: Activepieces Connections Worker Machines API
  slug: postman-activepieces-worker-machines-api
- collection_type: open
  name: Activepieces API
  slug: open-activepieces
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/activepieces/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/activepieces-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/activepieces-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/activepieces-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/activepieces
- group: start
  title: ''
  type: Portal
  url: https://www.activepieces.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.activepieces.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.activepieces.com/docs/getting-started/introduction
- group: auth
  title: ''
  type: Authentication
  url: https://www.activepieces.com/docs/endpoints/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.activepieces.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/activepieces
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/activepieces/activepieces
- group: operate
  title: ''
  type: StatusPage
  url: https://status.activepieces.com/
- group: design
  title: ''
  type: SpectralRules
  url: rules/activepieces-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/activepieces-vocabulary.yaml
- group: design
  title: Activepieces Context
  type: JSONLD
  url: json-ld/activepieces-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://www.activepieces.com/rss.xml
created: '2026-03-16'
description: Activepieces is an open-source, no-code automation platform that enables users to streamline workflows by connecting various applications and automating tasks. It supports over 400 MCP servers and integrations, allowing developers to build custom TypeScript-based pieces. The platform offers AI agents, MCPs, and workflow automation capabilities with both cloud and self-hosted deployment options.
examples:
- key_count: 8
  name: Activepieces Connection Example
  slug: activepieces-connection-example
- key_count: 3
  name: Activepieces Connection List Example
  slug: activepieces-connection-list-example
- key_count: 5
  name: Activepieces Create Flow Request Example
  slug: activepieces-create-flow-request-example
- key_count: 2
  name: Activepieces Create Folder Request Example
  slug: activepieces-create-folder-request-example
- key_count: 1
  name: Activepieces Create Project Request Example
  slug: activepieces-create-project-request-example
- key_count: 3
  name: Activepieces Create Template Request Example
  slug: activepieces-create-template-request-example
- key_count: 9
  name: Activepieces Flow Example
  slug: activepieces-flow-example
- key_count: 3
  name: Activepieces Flow List Example
  slug: activepieces-flow-list-example
- key_count: 9
  name: Activepieces Flow Run Example
  slug: activepieces-flow-run-example
- key_count: 3
  name: Activepieces Flow Run List Example
  slug: activepieces-flow-run-list-example
- key_count: 5
  name: Activepieces Folder Example
  slug: activepieces-folder-example
- key_count: 3
  name: Activepieces Folder List Example
  slug: activepieces-folder-list-example
- key_count: 6
  name: Activepieces Piece Example
  slug: activepieces-piece-example
- key_count: 6
  name: Activepieces Project Example
  slug: activepieces-project-example
- key_count: 3
  name: Activepieces Project List Example
  slug: activepieces-project-list-example
- key_count: 1
  name: Activepieces Queue Metrics Example
  slug: activepieces-queue-metrics-example
- key_count: 5
  name: Activepieces Template Example
  slug: activepieces-template-example
- key_count: 3
  name: Activepieces Template List Example
  slug: activepieces-template-list-example
- key_count: 3
  name: Activepieces Update Flow Request Example
  slug: activepieces-update-flow-request-example
- key_count: 1
  name: Activepieces Update Folder Request Example
  slug: activepieces-update-folder-request-example
- key_count: 2
  name: Activepieces Update Project Request Example
  slug: activepieces-update-project-request-example
- key_count: 3
  name: Activepieces Update User Request Example
  slug: activepieces-update-user-request-example
- key_count: 5
  name: Activepieces Upsert Connection Request Example
  slug: activepieces-upsert-connection-request-example
- key_count: 8
  name: Activepieces User Example
  slug: activepieces-user-example
- key_count: 3
  name: Activepieces User List Example
  slug: activepieces-user-list-example
features:
- description: No-code drag-and-drop interface for building automation workflows with triggers and actions.
  name: Visual Flow Builder
- description: Over 400 pre-built integrations (pieces) written in TypeScript, available as MCP servers for AI agents.
  name: 400+ Integration Pieces
- description: Native AI agent creation and orchestration within automation workflows.
  name: AI Agents
- description: Every piece automatically becomes an MCP server for use with AI agents and LLMs like Claude.
  name: MCP Servers
- description: Build custom TypeScript-based integration pieces and publish them to npm.
  name: Custom Pieces
- description: Version control for flows with publish/draft states and rollback capabilities.
  name: Flow Versioning
- description: Add approval steps, delays, and human decision points in automation workflows.
  name: Human-in-the-Loop
- description: Deploy on Docker, Kubernetes, AWS, GCP, or any cloud provider with full data control.
  name: Self-Hosting
- description: Synchronize flows with Git repositories for version control and CI/CD integration.
  name: Git Sync
- description: Trigger flows via webhooks from any external system or service.
  name: Webhook Triggers
- description: Full programmatic access to manage flows, connections, projects, and execution history.
  name: REST API
- description: Share and reuse flow templates across projects and teams.
  name: Flow Templates
finops:
- name: Activepieces Finops
  service_category: API
  slug: activepieces-finops
image: /assets/icons/activepieces.png
integrations:
- description: Trigger workflows on GitHub events and automate repository operations.
  name: GitHub
- description: Send emails, parse inbound mail, and automate email workflows.
  name: Gmail
- description: Send notifications, create channels, and respond to Slack events.
  name: Slack
- description: Integrate GPT models for AI-powered automation and content generation.
  name: OpenAI
- description: Read and write data to Google Sheets for data synchronization workflows.
  name: Google Sheets
- description: Sync records and trigger workflows from Airtable database changes.
  name: Airtable
- description: Create and update Salesforce records from automation workflows.
  name: Salesforce
- description: Trigger flows on payment events and automate billing operations.
  name: Stripe
json_schemas:
- name: ConnectionList
  property_count: 3
  slug: activepieces-connection-list
- name: Connection
  property_count: 8
  slug: activepieces-connection
- name: CreateFlowRequest
  property_count: 5
  slug: activepieces-create-flow-request
- name: CreateFolderRequest
  property_count: 2
  slug: activepieces-create-folder-request
- name: CreateProjectRequest
  property_count: 1
  slug: activepieces-create-project-request
- name: CreateTemplateRequest
  property_count: 3
  slug: activepieces-create-template-request
- name: FlowList
  property_count: 3
  slug: activepieces-flow-list
- name: FlowRunList
  property_count: 3
  slug: activepieces-flow-run-list
- name: FlowRun
  property_count: 9
  slug: activepieces-flow-run
- name: Flow
  property_count: 9
  slug: activepieces-flow
- name: FolderList
  property_count: 3
  slug: activepieces-folder-list
- name: Folder
  property_count: 5
  slug: activepieces-folder
- name: Piece
  property_count: 6
  slug: activepieces-piece
- name: ProjectList
  property_count: 3
  slug: activepieces-project-list
- name: Project
  property_count: 6
  slug: activepieces-project
- name: QueueMetrics
  property_count: 1
  slug: activepieces-queue-metrics
- name: TemplateList
  property_count: 3
  slug: activepieces-template-list
- name: Template
  property_count: 5
  slug: activepieces-template
- name: UpdateFlowRequest
  property_count: 3
  slug: activepieces-update-flow-request
- name: UpdateFolderRequest
  property_count: 1
  slug: activepieces-update-folder-request
- name: UpdateProjectRequest
  property_count: 2
  slug: activepieces-update-project-request
- name: UpdateUserRequest
  property_count: 3
  slug: activepieces-update-user-request
- name: UpsertConnectionRequest
  property_count: 5
  slug: activepieces-upsert-connection-request
- name: UserList
  property_count: 3
  slug: activepieces-user-list
- name: User
  property_count: 8
  slug: activepieces-user
json_structures:
- name: Activepieces Connection List Structure
  property_count: 3
  slug: activepieces-connection-list-structure
- name: Activepieces Connection Structure
  property_count: 8
  slug: activepieces-connection-structure
- name: Activepieces Create Flow Request Structure
  property_count: 5
  slug: activepieces-create-flow-request-structure
- name: Activepieces Create Folder Request Structure
  property_count: 2
  slug: activepieces-create-folder-request-structure
- name: Activepieces Create Project Request Structure
  property_count: 1
  slug: activepieces-create-project-request-structure
- name: Activepieces Create Template Request Structure
  property_count: 3
  slug: activepieces-create-template-request-structure
- name: Activepieces Flow List Structure
  property_count: 3
  slug: activepieces-flow-list-structure
- name: Activepieces Flow Run List Structure
  property_count: 3
  slug: activepieces-flow-run-list-structure
- name: Activepieces Flow Run Structure
  property_count: 9
  slug: activepieces-flow-run-structure
- name: Activepieces Flow Structure
  property_count: 9
  slug: activepieces-flow-structure
- name: Activepieces Folder List Structure
  property_count: 3
  slug: activepieces-folder-list-structure
- name: Activepieces Folder Structure
  property_count: 5
  slug: activepieces-folder-structure
- name: Activepieces Piece Structure
  property_count: 6
  slug: activepieces-piece-structure
- name: Activepieces Project List Structure
  property_count: 3
  slug: activepieces-project-list-structure
- name: Activepieces Project Structure
  property_count: 6
  slug: activepieces-project-structure
- name: Activepieces Queue Metrics Structure
  property_count: 1
  slug: activepieces-queue-metrics-structure
- name: Activepieces Template List Structure
  property_count: 3
  slug: activepieces-template-list-structure
- name: Activepieces Template Structure
  property_count: 5
  slug: activepieces-template-structure
- name: Activepieces Update Flow Request Structure
  property_count: 3
  slug: activepieces-update-flow-request-structure
- name: Activepieces Update Folder Request Structure
  property_count: 1
  slug: activepieces-update-folder-request-structure
- name: Activepieces Update Project Request Structure
  property_count: 2
  slug: activepieces-update-project-request-structure
- name: Activepieces Update User Request Structure
  property_count: 3
  slug: activepieces-update-user-request-structure
- name: Activepieces Upsert Connection Request Structure
  property_count: 5
  slug: activepieces-upsert-connection-request-structure
- name: Activepieces User List Structure
  property_count: 3
  slug: activepieces-user-list-structure
- name: Activepieces User Structure
  property_count: 8
  slug: activepieces-user-structure
jsonld:
- class_count: 25
  name: Activepieces Context
  property_count: 35
  slug: activepieces-context
layout: provider
modified: '2026-05-19'
name: Activepieces
nav: Providers
network: true
overview: 'Activepieces publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Connections API, Flow Runs API, Flows API, and 6 more. Tagged areas include Automation, No-Code, Open Source, Workflow, and AI Agents.


  The Activepieces catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Activepieces'' developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Activepieces Plans Pricing
  plan_count: 3
  slug: activepieces-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Activepieces Rate Limits
  slug: activepieces-rate-limits
rules:
- name: Activepieces API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: activepieces-jsonschema-spectral-rules
- name: Activepieces API Rules
  rule_count: 31
  severity_counts:
    error: 10
    hint: 0
    info: 5
    warn: 16
  slug: activepieces-spectral-rules
score:
  band: strong
  composite: 57.7
  delta: -7.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.3
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 65.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/activepieces/refs/heads/main/screenshots/activepieces-2026-06-20T164235.png
security:
- kind: authentication
  name: Activepieces Authentication
  slug: activepieces-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Activepieces Domain Security
  slug: activepieces-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: activepieces
solutions:
- description: Free, open-source self-hosted deployment with unlimited flows and no task limits.
  name: Community Edition
- description: Cloud plan at $25/mo with 10 active flows, AI agents, and 500 AI credits.
  name: Plus
- description: Cloud plan at $150/mo with 50 active flows, team collaboration, and 1,000 AI credits.
  name: Business
- description: Custom pricing with unlimited flows, SSO, audit logs, and custom AI model support.
  name: Enterprise
tags:
- Automation
- No-Code
- Open Source
- Workflow
- AI Agents
- MCP
use_cases:
- description: Automate lead capture, email sequences, and CRM updates from marketing platforms.
  name: Marketing Automation
- description: Sync contacts, deals, and activities between CRM, email, and communication tools.
  name: Sales Operations
- description: Keep data in sync across databases, spreadsheets, and SaaS applications.
  name: Data Synchronization
- description: Use Activepieces as an MCP server to give AI agents access to 400+ integrations.
  name: AI Agent Orchestration
- description: Automate user provisioning, notifications, and system integrations.
  name: IT Automation
- description: Automate order processing, inventory updates, and customer notifications.
  name: E-Commerce Operations
- description: Embed Activepieces as a white-label automation platform in SaaS products.
  name: Developer Integration Platform
website: https://www.activepieces.com/
---
