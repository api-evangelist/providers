---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Todoist Agentic Access
  operation_count: 41
  slug: todoist-agentic-access
  summary_line: 41 operations · 23 acting
api_count: 11
apis:
- description: The Todoist REST API v2 is the legacy recommended API for external integrations, providing access to tasks, projects, sections, labels, comments, and filters. Uses Bearer token authentication with OAu
  name: Todoist REST API v2
  slug: todoist-rest-api
- description: The Todoist Sync API is designed for clients maintaining a local representation of user data, allowing incremental synchronization of projects, tasks, labels, filters, and reminders. Supports batch co
  name: Todoist Sync API v9
  slug: todoist-sync-api
- description: Comment and note operations
  name: Todoist Comments API
  slug: todoist-comments-api
- description: Label management operations
  name: Todoist Labels API
  slug: todoist-labels-api
- description: Project management operations
  name: Todoist Projects API
  slug: todoist-projects-api
- description: Reminder management operations
  name: Todoist Reminders API
  slug: todoist-reminders-api
- description: Section management operations
  name: Todoist Sections API
  slug: todoist-sections-api
- description: Incremental sync operations
  name: Todoist Sync API
  slug: todoist-sync-api
- description: Task (item) management operations
  name: Todoist Tasks API
  slug: todoist-tasks-api
- description: User account and settings operations
  name: Todoist User API
  slug: todoist-user-api
- description: Workspace management operations
  name: Todoist Workspaces API
  slug: todoist-workspaces-api
artifact_total: 50
collections:
- collection_type: postman
  name: Todoist Comments API
  slug: postman-todoist-comments-api
- collection_type: postman
  name: Todoist Comments Labels API
  slug: postman-todoist-labels-api
- collection_type: postman
  name: Todoist Comments Projects API
  slug: postman-todoist-projects-api
- collection_type: postman
  name: Todoist Comments Reminders API
  slug: postman-todoist-reminders-api
- collection_type: postman
  name: Todoist Comments Sections API
  slug: postman-todoist-sections-api
- collection_type: postman
  name: Todoist Comments Sync API
  slug: postman-todoist-sync-api
- collection_type: postman
  name: Todoist Comments Tasks API
  slug: postman-todoist-tasks-api
- collection_type: postman
  name: Todoist Comments User API
  slug: postman-todoist-user-api
- collection_type: postman
  name: Todoist Comments Workspaces API
  slug: postman-todoist-workspaces-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Todoist Webhooks
  slug: open-todoist-asyncapi
- collection_type: open
  name: Todoist Comments API
  slug: open-todoist-comments-api
- collection_type: open
  name: Todoist Comments Labels API
  slug: open-todoist-labels-api
- collection_type: open
  name: Todoist Comments Projects API
  slug: open-todoist-projects-api
- collection_type: open
  name: Todoist Comments Reminders API
  slug: open-todoist-reminders-api
- collection_type: open
  name: Todoist Comments Sections API
  slug: open-todoist-sections-api
- collection_type: open
  name: Todoist Comments Sync API
  slug: open-todoist-sync-api
- collection_type: open
  name: Todoist Comments Tasks API
  slug: open-todoist-tasks-api
- collection_type: open
  name: Todoist Comments User API
  slug: open-todoist-user-api
- collection_type: open
  name: Todoist Comments Workspaces API
  slug: open-todoist-workspaces-api
- collection_type: open
  name: Todoist API
  slug: open-todoist
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/todoist/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/todoist-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/todoist-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/todoist-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/todoist-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/todoist-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/doist
- group: company
  title: ''
  type: Website
  url: https://todoist.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.todoist.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.todoist.com/api/v1/
- group: start
  title: ''
  type: Signup
  url: https://todoist.com/users/showregister
- group: start
  title: ''
  type: Login
  url: https://todoist.com/auth/login
- group: auth
  title: ''
  type: Authentication
  url: https://developer.todoist.com/guides/#oauth
- group: design
  title: ''
  type: Webhooks
  url: https://developer.todoist.com/api/v1/#webhooks
- group: build
  title: ''
  type: SDKs
  url: https://developer.todoist.com/guides/#sdks
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/Doist/todoist-api-python
- group: build
  title: ''
  type: TypeScript SDK
  url: https://github.com/Doist/todoist-sdk-typescript
- group: agent
  title: ''
  type: MCP Server
  url: https://github.com/doist/todoist-ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Doist
- group: company
  title: ''
  type: Blog
  url: https://doist.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://todoist.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doist.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doist.com/privacy-policy
created: '2025-01-08'
description: Todoist is a productivity platform providing task management APIs for developers. The Todoist API v1 unifies the Sync and REST APIs into a single interface, offering programmatic access to tasks, projects, sections, labels, reminders, comments, workspaces, and webhooks. SDKs are available in Python and TypeScript.
examples:
- key_count: 2
  name: Todoist Create Project Example
  slug: todoist-create-project-example
- key_count: 2
  name: Todoist Create Task Example
  slug: todoist-create-task-example
- key_count: 2
  name: Todoist List Tasks Example
  slug: todoist-list-tasks-example
finops:
- name: Todoist Finops
  service_category: Productivity SaaS
  slug: todoist-finops
graphqls:
- description: Todoist does not expose a native public GraphQL API. The platform is served
  name: Todoist GraphQL
  slug: todoist-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/todoist.png
json_schemas:
- name: Todoist Project
  property_count: 12
  slug: todoist-project
- name: Todoist Task
  property_count: 18
  slug: todoist-task
json_structures:
- name: Todoist Task Structure
  property_count: 0
  slug: todoist-task-structure
jsonld:
- class_count: 21
  name: Todoist Context
  property_count: 7
  slug: todoist-context
layout: provider
modified: '2026-05-30'
name: Todoist
nav: Providers
network: true
overview: 'Todoist publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Sync API v9, Comments API, Labels API, and 7 more. Tagged areas include Productivity, Tasks, To-Do, Task Management, and Collaboration.


  The Todoist catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Todoist''s developer surface includes authentication, documentation, signup flow, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Todoist Plans Pricing
  plan_count: 3
  slug: todoist-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 3
  name: Todoist Rate Limits
  slug: todoist-rate-limits
rules:
- name: Todoist API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: todoist-jsonschema-spectral-rules
- name: Todoist API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: todoist-rules
score:
  band: strong
  composite: 57.5
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 73.5
    developer_ergonomics: 41.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 90.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/todoist/refs/heads/main/screenshots/todoist-2026-06-20T195429.png
security:
- kind: authentication
  name: Todoist Authentication
  slug: todoist-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Todoist Domain Security
  slug: todoist-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Todoist Vulnerability Disclosure
  slug: todoist-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Todoist Trust Center
  slug: todoist-trust-center
  summary_line: GDPR
slug: todoist
tags:
- Productivity
- Tasks
- To-Do
- Task Management
- Collaboration
website: https://todoist.com/
---
