---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Kanban Agentic Access
  operation_count: 22
  slug: kanban-agentic-access
  summary_line: 22 operations · 14 acting
api_count: 12
apis:
- description: Legacy REST API for Kanban Tool. Supports both XML and JSON formats, uses a resource-oriented endpoint structure. Remains supported for existing integrations.
  name: Kanban Tool REST API v1
  slug: kanban-tool-rest-api-v1
- description: Browser-side SDK for customizing the Kanban Tool interface. Enables adding custom buttons to context menus, modifying styles, and extending UI behavior.
  name: Kanban Tool Browser SDK
  slug: kanban-tool-sdk
- description: The Attachments API from Kanban Tool — 2 operation(s) for attachments.
  name: Kanban Tool Attachments API
  slug: kanban-attachments-api
- description: The Attachments.json API from Kanban Tool — 1 operation(s) for attachments.json.
  name: Kanban Tool Attachments.json API
  slug: kanban-attachments-json-api
- description: The Boards API from Kanban Tool — 3 operation(s) for boards.
  name: Kanban Tool Boards API
  slug: kanban-boards-api
- description: The Subtasks API from Kanban Tool — 2 operation(s) for subtasks.
  name: Kanban Tool Subtasks API
  slug: kanban-subtasks-api
- description: The Subtasks.json API from Kanban Tool — 1 operation(s) for subtasks.json.
  name: Kanban Tool Subtasks.json API
  slug: kanban-subtasks-json-api
- description: The Tasks API from Kanban Tool — 5 operation(s) for tasks.
  name: Kanban Tool Tasks API
  slug: kanban-tasks-api
- description: The Tasks.json API from Kanban Tool — 1 operation(s) for tasks.json.
  name: Kanban Tool Tasks.json API
  slug: kanban-tasks-json-api
- description: The Time Trackers API from Kanban Tool — 1 operation(s) for time trackers.
  name: Kanban Tool Time Trackers API
  slug: kanban-time-trackers-api
- description: The Time Trackers.json API from Kanban Tool — 1 operation(s) for time trackers.json.
  name: Kanban Tool Time Trackers.json API
  slug: kanban-time-trackers-json-api
- description: The Users API from Kanban Tool — 2 operation(s) for users.
  name: Kanban Tool Users API
  slug: kanban-users-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kanban Tool API v3 Attachments API
  slug: open-kanban-attachments-api
- collection_type: open
  name: Kanban Tool API v3 Attachments Attachments.json API
  slug: open-kanban-attachments-json-api
- collection_type: open
  name: Kanban Tool API v3 Attachments Boards API
  slug: open-kanban-boards-api
- collection_type: open
  name: Kanban Tool API v3 Attachments Subtasks API
  slug: open-kanban-subtasks-api
- collection_type: open
  name: Kanban Tool API v3 Attachments Subtasks.json API
  slug: open-kanban-subtasks-json-api
- collection_type: open
  name: Kanban Tool API v3 Attachments Tasks API
  slug: open-kanban-tasks-api
- collection_type: open
  name: Kanban Tool API v3 Attachments Tasks.json API
  slug: open-kanban-tasks-json-api
- collection_type: open
  name: Kanban Tool API v3 Attachments Time Trackers API
  slug: open-kanban-time-trackers-api
- collection_type: open
  name: Kanban Tool API v3 Attachments Time Trackers.json API
  slug: open-kanban-time-trackers-json-api
- collection_type: open
  name: Kanban Tool API v3 Attachments Users API
  slug: open-kanban-users-api
- collection_type: open
  name: Kanban Tool API v3
  slug: open-kanban
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kanban-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kanban-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kanbantool.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kanbantool.com/developer
- group: company
  title: ''
  type: Blog
  url: https://kanbantool.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://kanbantool.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://kanbantool.com/signup/new
- group: operate
  title: ''
  type: Support
  url: https://kanbantool.com/support/introduction
- group: docs
  title: ''
  type: Kanban Guide
  url: https://kanbantool.com/kanban-guide/introduction
created: '2024-01-15'
description: Kanban Tool is a visual project management platform for managing boards, tasks, and workflows using the Kanban methodology. It provides REST APIs (v1 and v3), browser SDK, and DevKit for programmatic access to boards, tasks, columns, comments, attachments, time tracking, and team members.
finops:
- name: Kanban Finops
  service_category: API
  slug: kanban-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kanban.png
layout: provider
modified: '2026-05-19'
name: Kanban Tool
nav: Providers
network: true
overview: 'Kanban Tool publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, Attachments.json API, Boards API, and 7 more. Tagged areas include Agile, Boards, Kanban, Project Management, and Task Management.


  Kanban Tool''s developer surface includes engineering blog, pricing, signup flow, support, and 5 more developer resources.'
plans:
- name: Kanban Plans Pricing
  plan_count: 3
  slug: kanban-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Kanban Rate Limits
  slug: kanban-rate-limits
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 42.9
    developer_ergonomics: 38.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kanban/refs/heads/main/screenshots/kanban-2026-06-20T183911.png
security:
- kind: domain-security
  name: Kanban Domain Security
  slug: kanban-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kanban
tags:
- Agile
- Boards
- Kanban
- Project Management
- Task Management
- Time Tracking
- Workflows
website: https://kanbantool.com
---
