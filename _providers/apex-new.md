---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Apex by LeadShark provides a governed LinkedIn MCP server.
  name: Apex API
  slug: apex-api
- description: 'Apex by LeadShark API as documented publicly: 69 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Apex by LeadShark API
  slug: apex-new-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/apex-new/plans/apex-new-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apex-new-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apex-new/rules/apex-new-rules.yml
  title: ''
  type: Spectral
  url: rules/apex-new-rules.yml
- group: design
  href: https://artifacts.apis.io/apex-new/json-ld/apex-new-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apex-new-context.jsonld
- group: design
  href: https://artifacts.apis.io/apex-new/vocabulary/apex-new-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apex-new-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/apex-new/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apex-new/data-model/apex-new-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apex-new-data-model.yml
- group: design
  href: https://artifacts.apis.io/apex-new/conformance/apex-new-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apex-new-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apex-new/llms/apex-new-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apex-new-llms.txt
- group: agent
  href: https://artifacts.apis.io/apex-new/well-known/apex-new-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apex-new-well-known.yml
- group: other
  href: https://artifacts.apis.io/apex-new/hosts/apex-new-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apex-new-hosts.yml
- group: other
  href: https://artifacts.apis.io/apex-new/vendors/apex-new-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apex-new-vendors.yml
- group: auth
  href: https://artifacts.apis.io/apex-new/security/apex-new-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apex-new-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apex.new/
- group: docs
  title: ''
  type: Documentation
  url: https://apex.leadshark.io/docs/apex
- group: docs
  title: ''
  type: APIReference
  url: https://apex.leadshark.io/docs/apex
- group: start
  title: ''
  type: GettingStarted
  url: https://www.apex.new/loadouts
- group: company
  title: ''
  type: Blog
  url: https://www.apex.new/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apex.new/pricing
- group: start
  title: ''
  type: SignUp
  url: https://apex.leadshark.io
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://www.apex.new/mcp
  - status: 401
    url: https://apex.leadshark.io/mcp
  - status: 200
    url: https://www.apex.new/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Apex is a governed LinkedIn MCP server. Connect Claude, ChatGPT, or Cursor and run your LinkedIn in plain English — find buyers, comment, connect, and message. Agent writes paced, capped, approval-queued where needed, and logged.
image: https://www.apex.new/opengraph-image.png?8e1e1a27546ca148
json_schemas:
- name: GetApiAutomationsResponse
  property_count: 14
  slug: apex-new-get-api-automations-response
- name: GetApiLeadsResponse
  property_count: 23
  slug: apex-new-get-api-leads-response
- name: GetApiV1SignalsEventsResponse
  property_count: 11
  slug: apex-new-get-api-v1-signals-events-response
- name: GetApiV1SignalsResponse
  property_count: 12
  slug: apex-new-get-api-v1-signals-response
- name: PostApiScheduledPostsRequest
  property_count: 3
  slug: apex-new-post-api-scheduled-posts-request
- name: PostApiV1PagesRequest
  property_count: 5
  slug: apex-new-post-api-v1-pages-request
jsonld:
- class_count: 13
  name: Apex New Context
  property_count: 66
  slug: apex-new-context
layout: provider
modified: '2026-11-01'
name: Apex by LeadShark
nav: Providers
network: true
overview: 'Apex by LeadShark is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include LinkedIn, Artificial Intelligence, Automation, Lead Generation, and MCP.


  The Apex by LeadShark catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apex by LeadShark''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Apex New Plans Pricing
  plan_count: 1
  slug: apex-new-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Apex by LeadShark API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: apex-new-rules
scopes:
- name: Apex New Scopes
  scope_count: 0
  slug: apex-new-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 32.9
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 21.9
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 32.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apex New Authentication
  slug: apex-new-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Apex New Domain Security
  slug: apex-new-domain-security
  summary_line: TLSv1.3 · HSTS
slug: apex-new
tags:
- LinkedIn
- Artificial Intelligence
- Automation
- Lead Generation
- MCP
website: https://www.apex.new/
---
