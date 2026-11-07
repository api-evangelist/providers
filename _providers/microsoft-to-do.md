---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Microsoft To Do Agentic Access
  operation_count: 18
  slug: microsoft-to-do-agentic-access
  summary_line: 18 operations · 10 acting
api_count: 1
apis:
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The LinkedResources API from Microsoft to Do — 1 operation(s) for linkedresources.
  name: Microsoft to Do LinkedResources API
  slug: microsoft-to-do-linkedresources-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The TaskLists API from Microsoft to Do — 2 operation(s) for tasklists.
  name: Microsoft to Do TaskLists API
  slug: microsoft-to-do-tasklists-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The Tasks API from Microsoft to Do — 3 operation(s) for tasks.
  name: Microsoft to Do Tasks API
  slug: microsoft-to-do-tasks-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The me.todo API from Microsoft To Do — 30 operation(s) for me.todo.
  name: Microsoft To Do Me.todo API
  slug: microsoft-to-do-me-todo-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The users.todo API from Microsoft To Do — 30 operation(s) for users.todo.
  name: Microsoft To Do Users.todo API
  slug: microsoft-to-do-users-todo-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The Checklist Items API from Microsoft To Do — 2 operation(s) for checklist items.
  name: Microsoft To Do Checklist Items API
  slug: microsoft-to-do-checklist-items-api
artifact_total: 31
collections:
- collection_type: open
  name: Microsoft To Do API (Microsoft Graph) ChecklistItems API
  slug: open-microsoft-to-do-checklistitems-api
- collection_type: open
  name: Microsoft To Do API (Microsoft Graph) ChecklistItems LinkedResources API
  slug: open-microsoft-to-do-linkedresources-api
- collection_type: open
  name: Microsoft To Do API (Microsoft Graph) ChecklistItems TaskLists API
  slug: open-microsoft-to-do-tasklists-api
- collection_type: open
  name: Microsoft To Do API (Microsoft Graph) ChecklistItems Tasks API
  slug: open-microsoft-to-do-tasks-api
- collection_type: open
  name: Microsoft To Do API (Microsoft Graph)
  slug: open-microsoft-to-do
common:
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/analyticsonazure
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: design
  href: https://artifacts.apis.io/microsoft-to-do/rules/microsoft-to-do-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-to-do-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-to-do/json-ld/microsoft-to-do-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-to-do-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-to-do/vocabulary/microsoft-to-do-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-to-do-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-to-do/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-to-do/data-model/microsoft-to-do-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-to-do-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-to-do/conventions/microsoft-to-do-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-to-do-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/en-us/msrc/bounty-safe-harbor
- group: auth
  href: https://artifacts.apis.io/microsoft-to-do/scopes/microsoft-to-do-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-to-do-scopes.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/graph/versioning-and-support
- group: design
  href: https://artifacts.apis.io/microsoft-to-do/lifecycle/microsoft-to-do-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-to-do-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-to-do/errors/microsoft-to-do-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-to-do-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-to-do/conformance/microsoft-to-do-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-to-do-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-to-do/llms/microsoft-to-do-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-to-do-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-to-do/well-known/microsoft-to-do-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-to-do-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-to-do/well-known/microsoft-to-do-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-to-do-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-to-do/hosts/microsoft-to-do-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-to-do-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-to-do/integrations/microsoft-to-do-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-to-do-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-to-do/vendors/microsoft-to-do-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-to-do-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-to-do/packages/microsoft-to-do-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-to-do-packages.yml
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: operate
  href: https://artifacts.apis.io/microsoft-to-do/rate-limits/microsoft-to-do-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-to-do-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-to-do/finops/microsoft-to-do-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-to-do-finops.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-to-do/agentic-access/microsoft-to-do-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-to-do-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-to-do/security/microsoft-to-do-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-to-do-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-to-do/security/microsoft-to-do-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-to-do-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-to-do/authentication/microsoft-to-do-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-to-do-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://to-do.microsoft.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/microsoft-to-do-list-app
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/todo-concept-overview
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/graph/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/graph
created: '2024-01-01'
description: Microsoft To Do is Microsoft's task management application that helps users organize and manage their day across Windows, mobile and the web. Its data is exposed to developers through Microsoft Graph v1.0 (graph.microsoft.com), covering task lists, tasks, checklist items, linked resources, attachments and delta sync, secured with Microsoft identity platform OAuth and the Tasks.* permissions.
finops:
- has_sources: false
  method: generated
  name: Microsoft To Do Finops
  primary_unit: request
  service_category: API
  slug: microsoft-to-do-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-to-do.png
json_schemas:
- name: GenericList
  property_count: 1
  slug: microsoft-to-do-generic-list
- name: GenericObject
  property_count: 0
  slug: microsoft-to-do-generic-object
- name: microsoft.graph.attachmentBase
  property_count: 6
  slug: microsoft-to-do-microsoft-graph-attachment-base
- name: microsoft.graph.attachmentSession
  property_count: 5
  slug: microsoft-to-do-microsoft-graph-attachment-session
- name: microsoft.graph.checklistItem
  property_count: 6
  slug: microsoft-to-do-microsoft-graph-checklist-item
- name: microsoft.graph.todoTaskList
  property_count: 9
  slug: microsoft-to-do-microsoft-graph-todo-task-list
- name: microsoft.graph.todoTask
  property_count: 23
  slug: microsoft-to-do-microsoft-graph-todo-task
- name: uploadSession
  property_count: 4
  slug: microsoft-to-do-microsoft-graph-upload-session
jsonld:
- class_count: 24
  name: Microsoft To Do Context
  property_count: 34
  slug: microsoft-to-do-context
layout: provider
modified: '2026-11-04'
name: Microsoft To Do
nav: Providers
network: true
overview: 'Microsoft To Do publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including LinkedResources API, TaskLists API, Tasks API, and 3 more. Tagged areas include Microsoft, Microsoft 365, Productivity, Task, and Task Management.


  The Microsoft To Do catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft To Do''s developer surface includes engineering blog, getting-started guide, authentication, developer portal, documentation, support, changelog, and 32 more developer resources.'
plans:
- name: Microsoft To Do Plans Pricing
  plan_count: 0
  slug: microsoft-to-do-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Microsoft To Do Rate Limits
  slug: microsoft-to-do-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Microsoft To Do API Rules
  rule_count: 53
  severity_counts:
    error: 41
    hint: 0
    info: 7
    warn: 5
  slug: microsoft-to-do-rules
scopes:
- name: Microsoft To Do Scopes
  scope_count: 6
  slug: microsoft-to-do-scopes
  summary_line: 6 scopes
score:
  band: developing
  composite: 52.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 14.1
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 58.6
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 57.9
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-to-do/microsoft-to-do-2026-06-20T185539.png
security:
- kind: authentication
  name: Microsoft To Do Authentication
  slug: microsoft-to-do-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft To Do Domain Security
  slug: microsoft-to-do-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft To Do Vulnerability Disclosure
  slug: microsoft-to-do-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: microsoft-to-do-manage-tasks
  slug: microsoft-to-do-manage-tasks
- name: microsoft-to-do-sync-tasks
  slug: microsoft-to-do-sync-tasks
slug: microsoft-to-do
tags:
- Microsoft
- Microsoft 365
- Productivity
- Task
- Task Management
- Microsoft Graph
website: https://www.microsoft.com/en-us/microsoft-365/microsoft-to-do-list-app
---
