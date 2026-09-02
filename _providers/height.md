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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Height Agentic Access
  operation_count: 22
  slug: height-agentic-access
  summary_line: 22 operations · 10 acting
api_count: 1
apis:
- description: Activities can be messages, status updates of the task or integration updates (i.e. GitHub).
  name: Height Activities API
  slug: height-activities-api
- description: The Field Templates API from Height — 3 operation(s) for field templates.
  name: Height Field Templates API
  slug: height-field-templates-api
- description: The Groups API from Height — 1 operation(s) for groups.
  name: Height Groups API
  slug: height-groups-api
- description: Tasks belong to one list. To create tasks, it's necessary to know in which list you want to create them.
  name: Height Lists API
  slug: height-lists-api
- description: The Security Log Events API from Height — 1 operation(s) for security log events.
  name: Height Security Log Events API
  slug: height-security-log-events-api
- description: The Task Forms API from Height — 2 operation(s) for task forms.
  name: Height Task Forms API
  slug: height-task-forms-api
- description: The Tasks API from Height — 3 operation(s) for tasks.
  name: Height Tasks API
  slug: height-tasks-api
- description: The Users API from Height — 3 operation(s) for users.
  name: Height Users API
  slug: height-users-api
- description: The Workspace API from Height — 1 operation(s) for workspace.
  name: Height Workspace API
  slug: height-workspace-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Height APP Activities API
  slug: open-height-activities-api
- collection_type: open
  name: Height APP Activities Field Templates API
  slug: open-height-field-templates-api
- collection_type: open
  name: Height APP Activities Groups API
  slug: open-height-groups-api
- collection_type: open
  name: Height APP Activities Lists API
  slug: open-height-lists-api
- collection_type: open
  name: Height APP Activities Security Log Events API
  slug: open-height-security-log-events-api
- collection_type: open
  name: Height APP Activities Task Forms API
  slug: open-height-task-forms-api
- collection_type: open
  name: Height APP Activities Tasks API
  slug: open-height-tasks-api
- collection_type: open
  name: Height APP Activities Users API
  slug: open-height-users-api
- collection_type: open
  name: Height APP Activities Workspace API
  slug: open-height-workspace-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/height-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/height-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/height-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://height.app
- group: docs
  title: ''
  type: Documentation
  url: https://www.notion.so/API-documentation-643aea5bf01742de9232e5971cb4afda
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/heightapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heightapp
- group: company
  title: ''
  type: Blog
  url: https://height.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://height.app/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.height.app
- group: other
  title: ''
  type: X
  url: https://twitter.com/height_app
- group: commercial
  title: ''
  type: Plans
  url: plans/height-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/height-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/height-finops.yml
created: '2026-06-13'
description: Height is an AI-powered collaborative project management tool that provides a REST API for managing tasks, lists, workspaces, attributes, dependencies, and automation triggers. The API enables developers to programmatically create, read, update, and delete tasks and task lists, manage workspace users and groups, post activity comments, and configure webhook integrations for real-time event notifications. Authentication is handled via secret API keys generated from workspace settings, with OAuth 2.0 available for third-party application integrations. Height announced the shutdown of its service with a final date of September 24, 2025, making this a historical profile of the platform's public developer footprint.
finops:
- name: Height Finops
  service_category: ''
  slug: height-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/height.png
jsonld:
- class_count: 71
  name: Height Context
  property_count: 0
  slug: height-context
layout: provider
modified: '2026-06-13'
name: Height
nav: Providers
network: true
overview: 'Height publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Field Templates API, Groups API, and 6 more. Tagged areas include Project Management, Task Management, Collaboration, Productivity, and Workflow-Automation.


  The Height catalog on APIs.io includes 1 JSON-LD context.


  Height''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Height Plans Pricing
  plan_count: 4
  slug: height-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Height Rate Limits
  slug: height-rate-limits
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 43.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 54.9
    developer_ergonomics: 13.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/height/refs/heads/main/screenshots/height-2026-06-20T182618.png
security:
- kind: authentication
  name: Height Authentication
  slug: height-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Height Domain Security
  slug: height-domain-security
  summary_line: no transport/DNS hardening detected
slug: height
tags:
- Project Management
- Task Management
- Collaboration
- Productivity
- Workflow-Automation
- Artificial Intelligence
website: https://height.app
---
