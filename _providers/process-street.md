---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 88
  human_in_the_loop: 0
  name: Process Street Agentic Access
  operation_count: 150
  slug: process-street-agentic-access
  summary_line: 150 operations · 88 acting
api_count: 28
apis:
- description: An attachment is a file uploaded to a task within a workflow run. Use these endpoints to list, upload, and delete task-level attachments.
  name: Process Street Attachments API
  slug: process-street-attachments-api
- description: A comment is a discussion message on a task within a workflow run. Use these endpoints to create, list, update, and delete comments.
  name: Process Street Comments API
  slug: process-street-comments-api
- description: An incoming webhook triggers data set row creation or updates from external systems. Use these endpoints to create, view, update, and delete incoming webhooks for a data set.
  name: Process Street Data Set Incoming Webhooks API
  slug: process-street-data-set-incoming-webhooks-api
- description: A data set is a structured collection of records that can be linked to workflow form fields. Use these endpoints to manage data sets and their records.
  name: Process Street Data Sets API
  slug: process-street-data-sets-api
- description: A file upload is a two-step upload for large files. Create one to get an upload URL and a `fileUploadId`, send the file's bytes to that URL, then attach the upload to a target (form field value, attac
  name: Process Street File Uploads API
  slug: process-street-file-uploads-api
- description: A folder organizes workflows, pages, and other templates within your organization. Use these endpoints to create and manage folders.
  name: Process Street Folders API
  slug: process-street-folders-api
- description: A form field value is the data entered into a form field within a workflow run. Use these endpoints to read and update form field values for a specific workflow run.
  name: Process Street Form Field Values API
  slug: process-street-form-field-values-api
- description: A form field is a data-collection element defined on a workflow template. Use these endpoints to inspect the form fields and their available options on a workflow.
  name: Process Street Form Fields API
  slug: process-street-form-fields-api
- description: My Work is your personal task inbox — a consolidated view of all tasks and checklist items assigned to you across all workflows. Use these endpoints to list, search, and manage your assigned work item
  name: Process Street My Work API
  slug: process-street-my-work-api
- description: A one-off task is a standalone task that can optionally be linked to a workflow run. Use these endpoints to create, view, and manage one-off tasks.
  name: Process Street One-Off Tasks API
  slug: process-street-one-off-tasks-api
- description: A page revision is a versioned snapshot of a page's content. Use these endpoints to list, inspect, and manage revisions.
  name: Process Street Page Revisions API
  slug: process-street-page-revisions-api
- description: A page widget is a content element (text, image, video, file, embed, cross-link, or table) on a page revision. Use these endpoints to create and manage widgets on draft revisions.
  name: Process Street Page Widgets API
  slug: process-street-page-widgets-api
- description: A page is a document template for sharing information. Use these endpoints to create and manage pages.
  name: Process Street Pages API
  slug: process-street-pages-api
- description: A scheduled workflow is a recurring schedule that automatically creates workflow runs. Use these endpoints to list scheduled workflows and their recurrence rules.
  name: Process Street Scheduled Workflows API
  slug: process-street-scheduled-workflows-api
- description: A task is a step within a workflow run. Tasks can be checked off, assigned to users, and may contain form fields for collecting data. Use these endpoints to view and update tasks within a workflow run
  name: Process Street Tasks API
  slug: process-street-tasks-api
- description: These endpoints let you list the users in your organization.
  name: Process Street Users API
  slug: process-street-users-api
- description: Helper endpoints for testing authentication and checking rate limits.
  name: Process Street Utilities API
  slug: process-street-utilities-api
- description: A webhook delivers real-time notifications to your application when events occur in Process Street. Use these endpoints to create and manage webhook subscriptions.
  name: Process Street Webhooks API
  slug: process-street-webhooks-api
- description: A workflow due date rule defines how the checklist-level due date is calculated for workflow runs — either relative to the run's start date or derived from a Date form field value. Use these endpoints
  name: Process Street Workflow Due Date Rules API
  slug: process-street-workflow-due-date-rules-api
- description: An incoming webhook triggers workflow runs from external systems. Use these endpoints to create, view, update, and delete incoming webhooks for a workflow.
  name: Process Street Workflow Incoming Webhooks API
  slug: process-street-workflow-incoming-webhooks-api
- description: Workflow logic rules are conditional rules that control the visibility of tasks and form fields within a workflow revision. Use these endpoints to create, view, and manage logic rules.
  name: Process Street Workflow Logic Rules API
  slug: process-street-workflow-logic-rules-api
- description: A workflow revision is a versioned snapshot of a workflow's structure. Use these endpoints to list, inspect, and manage revisions.
  name: Process Street Workflow Revisions API
  slug: process-street-workflow-revisions-api
- description: A workflow run is an active instance of a workflow. Each run tracks its own progress, assignees, and form field values as it moves through the process. Use these endpoints to create, update, and manag
  name: Process Street Workflow Runs API
  slug: process-street-workflow-runs-api
- description: A workflow task assignment rule assigns a task template on a draft workflow revision to a specific user (static) or derives assignees from a source such as the workflow run initiator, a Members form f
  name: Process Street Workflow Task Assignment Rules API
  slug: process-street-workflow-task-assignment-rules-api
- description: A task due date rule defines how an individual task's due date is calculated within a workflow run — relative to the run's start/due date, a form field value, or another task. Use these endpoints to s
  name: Process Street Workflow Task Due Date Rules API
  slug: process-street-workflow-task-due-date-rules-api
- description: 'A workflow task is a task template within a workflow revision. Use these endpoints to create, view, update, and delete task templates on draft revisions. > 💡 Notes for MCP clients: > - Don''t prefix ta'
  name: Process Street Workflow Tasks API
  slug: process-street-workflow-tasks-api
- description: A workflow widget is a form field or content element on a task within a workflow revision. Use these endpoints to create and manage widgets on draft revisions.
  name: Process Street Workflow Widgets API
  slug: process-street-workflow-widgets-api
- description: A workflow is a reusable process template that defines the structure, tasks, and form fields for a repeatable process. Use these endpoints to browse and inspect your organization's workflows.
  name: Process Street Workflows API
  slug: process-street-workflows-api
artifact_total: 35
asyncapis:
- description: ''
  name: Process Street Webhooks
  slug: process-street-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/process-street-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/process-street-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.process.st/responsible-disclosure/
- group: auth
  title: ''
  type: Compliance
  url: https://www.process.st/security/
- group: company
  title: ''
  type: Website
  url: https://www.process.st/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://public-api.process.st/api/v1.1/docs/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.process.st/help/
- group: docs
  title: ''
  type: APIReference
  url: https://public-api.process.st/api/v1.1/docs/index.html
- group: agent
  title: ''
  type: MCPServer
  url: mcp/process-street-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/process-street-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.process.st/
- group: company
  title: ''
  type: Blog
  url: https://www.process.st/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.process.st/help/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.process.st/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.process.st/organizations/create
- group: start
  title: ''
  type: Login
  url: https://app.process.st/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.process.st/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.process.st/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/process-street
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/process-street-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/process-street-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/process-street-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Process Street is a no-code workflow and process management platform for building, running, and automating recurring team processes as workflows (reusable templates) and workflow runs (checklists). Its REST Public API is organized around resource-oriented URLs, accepts and returns JSON, and covers workflows, workflow runs, tasks, form fields and values, pages, folders, data sets, users, one-off tasks, scheduled workflows, comments, attachments, outgoing webhooks, and incoming (data set + workflow) webhooks. Authentication is via an X-API-KEY header; results paginate through an opaque cursor with HATEOAS next links; and a hosted Model Context Protocol (MCP) server exposes most endpoints as tools for AI agents.
image: https://www.process.st/wp-content/uploads/2020/09/process-street-logo.png
layout: provider
mcp_servers:
- description: ''
  name: process-street-mcp.yml
  slug: process-street-mcpyml
modified: '2026-07-20'
name: Process Street
nav: Providers
network: true
overview: 'Process Street publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, Comments API, Data Set Incoming Webhooks API, and 25 more. Tagged areas include Company, Productivity, Workflow, Workflow Automation, and Process Management.


  The Process Street catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Process Street''s developer surface includes documentation, API reference, authentication, engineering blog, support, pricing, signup flow, and 16 more developer resources.'
random_paper: 53
score:
  band: developing
  composite: 53.6
  delta: -0.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.8
    developer_ergonomics: 51.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Process Street Authentication
  slug: process-street-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Process Street Domain Security
  slug: process-street-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Process Street Vulnerability Disclosure
  slug: process-street-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Process Street Trust Center
  slug: process-street-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: process-street
tags:
- Company
- Productivity
- Workflow
- Workflow Automation
- Process Management
- No-Code
- Business Process
- Task Management
- SaaS
- MCP
website: https://www.process.st/
---
