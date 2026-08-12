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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Google Tasks Agentic Access
  operation_count: 13
  slug: google-tasks-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 2
apis:
- description: The Lists API from Google Tasks — 4 operation(s) for lists.
  name: Google Tasks Lists API
  slug: google-tasks-lists-api
- description: The Users API from Google Tasks — 2 operation(s) for users.
  name: Google Tasks Users API
  slug: google-tasks-users-api
artifact_total: 16
collections:
- collection_type: postman
  name: Google Tasks Lists API
  slug: postman-google-tasks-lists-api
- collection_type: postman
  name: Google Tasks Lists Users API
  slug: postman-google-tasks-users-api
- collection_type: open
  name: Google Tasks API
  slug: open-tasks
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-tasks/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-tasks-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-tasks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-tasks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-tasks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-tasks-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/tasks
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/tasks/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/tasks
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/workspace/tasks/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/workspace/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/tasks/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tasks.jsonld
- group: company
  title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com/feeds/posts/default?alt=rss
created: '2026-03-13'
description: The Google Tasks API lets you search, read, and update Google Tasks content and metadata. You can create, update, delete, and organize tasks across multiple task lists, move tasks between positions, and manage task completion status programmatically.
finops:
- name: Google Tasks Finops
  service_category: API
  slug: google-tasks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-tasks.png
json_schemas:
- name: Google Task
  property_count: 15
  slug: tasks
jsonld:
- class_count: 9
  name: Tasks Context
  property_count: 4
  slug: tasks
layout: provider
modified: '2026-05-19'
name: Google Tasks
nav: Providers
network: true
overview: 'Google Tasks publishes 2 APIs on the [APIs.io](https://apis.io/) network: Lists API and Users API. Tagged areas include Google, Productivity, Task Management, Tasks, and Todo.


  The Google Tasks catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Tasks'' developer surface includes authentication, developer portal, getting-started guide, documentation, support, engineering blog, and 11 more developer resources.'
plans:
- name: Google Tasks Plans Pricing
  plan_count: 3
  slug: google-tasks-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Google Tasks Rate Limits
  slug: google-tasks-rate-limits
rules:
- name: Google Tasks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: google-tasks-jsonschema-spectral-rules
scopes:
- name: Google Tasks Scopes
  scope_count: 2
  slug: google-tasks-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 52.5
  delta: -8.5
  facets:
    commercial_clarity: 36.8
    contract_quality: 70.1
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 61.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-tasks/refs/heads/main/screenshots/google-tasks-2026-06-20T182240.png
security:
- kind: authentication
  name: Google Tasks Authentication
  slug: google-tasks-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Tasks Domain Security
  slug: google-tasks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Tasks Vulnerability Disclosure
  slug: google-tasks-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-tasks
tags:
- Google
- Productivity
- Task Management
- Tasks
- Todo
- Workspace
website: https://developers.google.com/tasks
---
