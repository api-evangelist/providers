---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Omniyond Com Agentic Access
  operation_count: 30
  slug: omniyond-com-agentic-access
  summary_line: 30 operations · 20 acting
api_count: 1
apis:
- baseURL: https://omniyond.com
  baseurl_source: declared
  description: Model Context Protocol surface.
  name: omniyond-com MCP API
  slug: omniyond-com-mcp-api
- baseURL: https://omniyond.com
  baseurl_source: declared
  description: Schedule and manage HTTP jobs.
  name: omniyond-com Scheduler API
  slug: omniyond-com-scheduler-api
- baseURL: https://omniyond.com
  baseurl_source: declared
  description: Standalone paid utility endpoints.
  name: omniyond-com Utility API
  slug: omniyond-com-utility-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/omniyond-com/agentic-access/omniyond-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/omniyond-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/omniyond-com/plans/omniyond-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/omniyond-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/omniyond-com/rules/omniyond-com-rules.yml
  title: ''
  type: Spectral
  url: rules/omniyond-com-rules.yml
- group: design
  href: https://artifacts.apis.io/omniyond-com/json-ld/omniyond-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/omniyond-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/omniyond-com/vocabulary/omniyond-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/omniyond-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/omniyond-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/omniyond-com/data-model/omniyond-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/omniyond-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/omniyond-com/errors/omniyond-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/omniyond-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/omniyond-com/conformance/omniyond-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/omniyond-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/omniyond-com/llms/omniyond-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/omniyond-com-llms.txt
- group: build
  href: https://artifacts.apis.io/omniyond-com/mcp/omniyond-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/omniyond-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/omniyond-com/mcp/omniyond-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/omniyond-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/omniyond-com/hosts/omniyond-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/omniyond-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/omniyond-com/vendors/omniyond-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/omniyond-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://omniyond.com/login
- group: docs
  title: ''
  type: APIReference
  url: https://omniyond.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/omniyond-com/authentication/omniyond-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/omniyond-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/omniyond-com/security/omniyond-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/omniyond-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://omniyond.com/
- group: company
  title: ''
  type: Blog
  url: https://omniyond.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://omniyond.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://omniyond.com/terms-of-service
created: '2026-10-30'
description: Omniyond provides a pay‑per‑use API toolbox for AI builders, allowing scheduling of any HTTP call with granular pricing, a single API key, and built‑in retries. Users can create accounts, obtain API keys, and run scheduled jobs via a simple dashboard. The platform offers tools like a cron‑expression generator, MCP integration, and transparent pricing starting at $0.01 per run. It targets developers needing reliable, on‑demand API execution without managing infrastructure.
image: https://omniyond.com/images/preview-1.png
json_schemas:
- name: CancelResult
  property_count: 3
  slug: omniyond-com-cancel-result
- name: JobDetail
  property_count: 15
  slug: omniyond-com-job-detail
- name: RestartResult
  property_count: 5
  slug: omniyond-com-restart-result
- name: ScheduleInput
  property_count: 11
  slug: omniyond-com-schedule-input
- name: ScheduledJob
  property_count: 10
  slug: omniyond-com-scheduled-job
- name: StoredFile
  property_count: 4
  slug: omniyond-com-stored-file
jsonld:
- class_count: 10
  name: Omniyond Com Context
  property_count: 44
  slug: omniyond-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at omniyond.com requiring an API key.
  name: omniyond-com MCP Server
  slug: omniyond-com-mcp-yml
modified: '2026-10-30'
name: omniyond-com
nav: Providers
network: true
overview: 'omniyond-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: MCP API, Scheduler API, and Utility API. Tagged areas include Artificial Intelligence, Pay-Per-Use, Scheduling, and Automation.


  The omniyond-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  omniyond-com''s developer surface includes API reference, authentication, engineering blog, and 19 more developer resources.'
plans:
- name: Omniyond Com Plans Pricing
  plan_count: 4
  slug: omniyond-com-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: omniyond-com API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 1
  slug: omniyond-com-rules
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 64.5
    developer_ergonomics: 23.1
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/omniyond-com/omniyond-com-2026-11-03T140540.png
security:
- kind: authentication
  name: Omniyond Com Authentication
  slug: omniyond-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Omniyond Com Domain Security
  slug: omniyond-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: schedule-job
  slug: omniyond-com-schedule-job
slug: omniyond-com
tags:
- Artificial Intelligence
- Pay-Per-Use
- Scheduling
- Automation
website: https://omniyond.com/
---
