---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Taskbullet Com Agentic Access
  operation_count: 2
  slug: taskbullet-com-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: Delegate tasks from AI agents and LLMs to real human virtual assistants (Human-in-the-loop).
  name: TaskBullet Agent API
  slug: taskbullet-agent-api
- baseURL: https://taskbullet.com/api/v1
  baseurl_source: declared
  description: Delegate tasks from AI agents and LLMs to real human virtual assistants (Human-in-the-loop).
  name: TaskBullet Agent API API
  slug: taskbullet-agent-api-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/taskbullet-com/rules/taskbullet-com-rules.yml
  title: ''
  type: Spectral
  url: rules/taskbullet-com-rules.yml
- group: design
  href: https://artifacts.apis.io/taskbullet-com/json-ld/taskbullet-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/taskbullet-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/taskbullet-com/vocabulary/taskbullet-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/taskbullet-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/taskbullet-com/conventions/taskbullet-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/taskbullet-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/taskbullet-com/conventions/taskbullet-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/taskbullet-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/taskbullet-com/conformance/taskbullet-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/taskbullet-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/taskbullet-com/data-model/taskbullet-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/taskbullet-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/taskbullet-com/errors/taskbullet-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/taskbullet-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/taskbullet-com/llms/taskbullet-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/taskbullet-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/taskbullet-com/mcp/taskbullet-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/taskbullet-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/taskbullet-com/hosts/taskbullet-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/taskbullet-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/taskbullet-com/vendors/taskbullet-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/taskbullet-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taskbullet.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taskbullet.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://taskbullet.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://taskbullet.com/integrations/basecamp/getting-started
- group: auth
  href: https://artifacts.apis.io/taskbullet-com/security/taskbullet-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/taskbullet-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://taskbullet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://taskbullet.com/about
- group: company
  title: ''
  type: Blog
  url: https://taskbullet.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://taskbullet.com/pricing
created: '2026-10-30'
description: TaskBullet provides managed virtual assistant services for US businesses, offering flexible hour and dedicated virtual assistant models since 2013. Their platform helps companies save time and reduce costs by handling administrative, operational, and personal tasks, with a focus on reliability and high customer satisfaction.
image: https://taskbullet.com/brand/taskbullet-logo.png
json_schemas:
- name: ActionRequest
  property_count: 13
  slug: taskbullet-com-action-request
- name: TaskPriority
  property_count: 0
  slug: taskbullet-com-task-priority
- name: TaskStatus
  property_count: 0
  slug: taskbullet-com-task-status
jsonld:
- class_count: 3
  name: Taskbullet Com Context
  property_count: 13
  slug: taskbullet-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at taskbullet.com.
  name: taskbullet-com MCP Server
  slug: taskbullet-com-mcp-yml
modified: '2026-10-30'
name: taskbullet-com
nav: Providers
network: true
overview: 'taskbullet-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including TaskBullet Agent API API, and 1 more. Tagged areas include Company, Virtual Assistant, Software-as-a-Service, USBusiness, and Productivity.


  The taskbullet-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  taskbullet-com''s developer surface includes getting-started guide, documentation, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Taskbullet Com Plans Pricing
  plan_count: 8
  slug: taskbullet-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Taskbullet Com Rate Limits
  slug: taskbullet-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: taskbullet-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: taskbullet-com-rules
scopes:
- name: Taskbullet Com Scopes
  scope_count: 0
  slug: taskbullet-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 79.8
    catalog_earned_first_party: 20.0
    catalog_gap: 35.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 54.4
    developer_ergonomics: 11.9
    discoverability: 75.0
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/taskbullet-com/taskbullet-com-2026-11-03T144524.png
security:
- kind: authentication
  name: Taskbullet Com Authentication
  slug: taskbullet-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Taskbullet Com Domain Security
  slug: taskbullet-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: get-task
  slug: taskbullet-com-getTask-skill
- name: list-tasks
  slug: taskbullet-com-listTasks-skill
slug: taskbullet-com
tags:
- Company
- Virtual Assistant
- Software-as-a-Service
- USBusiness
- Productivity
website: https://taskbullet.com/
---
