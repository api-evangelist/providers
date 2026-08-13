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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 40
  human_in_the_loop: 0
  name: Hive Agentic Access
  operation_count: 72
  slug: hive-agentic-access
  summary_line: 72 operations · 40 acting
api_count: 13
apis:
- description: REST API for the Hive work management platform, providing CRUD access to workspaces, projects, actions (tasks), users, comments, labels, and attachments. Authentication uses workspace-scoped API token
  name: Hive Public API
  slug: public-api
- description: The Actions API from Hive — 9 operation(s) for actions.
  name: Hive Actions API
  slug: hive-actions-api
- description: The Agile Sprints API from Hive — 1 operation(s) for agile sprints.
  name: Hive Agile Sprints API
  slug: hive-agile-sprints-api
- description: The Dashboard Widgets API from Hive — 2 operation(s) for dashboard widgets.
  name: Hive Dashboard Widgets API
  slug: hive-dashboard-widgets-api
- description: The Form Submissions API from Hive — 1 operation(s) for form submissions.
  name: Hive Form Submissions API
  slug: hive-form-submissions-api
- description: The Messages API from Hive — 1 operation(s) for messages.
  name: Hive Messages API
  slug: hive-messages-api
- description: The Projects API from Hive — 6 operation(s) for projects.
  name: Hive Projects API
  slug: hive-projects-api
- description: The Resource Assignments API from Hive — 2 operation(s) for resource assignments.
  name: Hive Resource Assignments API
  slug: hive-resource-assignments-api
- description: The Teams API from Hive — 3 operation(s) for teams.
  name: Hive Teams API
  slug: hive-teams-api
- description: The Users API from Hive — 2 operation(s) for users.
  name: Hive Users API
  slug: hive-users-api
- description: The Webhooks API from Hive — 2 operation(s) for webhooks.
  name: Hive Webhooks API
  slug: hive-webhooks-api
- description: The Workflows API from Hive — 1 operation(s) for workflows.
  name: Hive Workflows API
  slug: hive-workflows-api
- description: The Workspaces API from Hive — 15 operation(s) for workspaces.
  name: Hive Workspaces API
  slug: hive-workspaces-api
artifact_total: 17
collections:
- collection_type: open
  name: Hive Public API
  slug: open-hive
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hive-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hive-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hive-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://hive.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hiveai
- group: company
  title: ''
  type: Website
  url: https://hive.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hive.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hive.com/reference/introduction
- group: start
  title: ''
  type: Signup
  url: https://hive.com/get-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://hive.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.hive.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.hive.com/llms.txt
created: '2026-05-11'
description: Hive (hive.com) is a project management and team collaboration platform that centralizes projects, tasks, time tracking, messaging, and workflow automation across teams, with multiple project views including Kanban, Gantt, Timeline, and Calendar. The Hive Public API gives developers programmatic access to workspaces, projects, actions (tasks), users, comments, and other core resources, authenticated via API tokens scoped to a workspace.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hive.png
layout: provider
modified: '2026-05-11'
name: Hive
nav: Providers
network: true
overview: 'Hive publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Agile Sprints API, Dashboard Widgets API, and 9 more. Tagged areas include Project Management, Task Management, Team Collaboration, Productivity, and Workflow Automation.


  Hive''s developer surface includes authentication, engineering blog, documentation, API reference, signup flow, pricing, support, and 5 more developer resources.'
random_paper: 68
score:
  band: thin
  composite: 33.2
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 55.2
    developer_ergonomics: 32.6
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hive/refs/heads/main/screenshots/hive-2026-06-20T182800.png
security:
- kind: authentication
  name: Hive Authentication
  slug: hive-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hive Domain Security
  slug: hive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hive
tags:
- Project Management
- Task Management
- Team Collaboration
- Productivity
- Workflow Automation
- Time Tracking
website: https://hive.com/
---
