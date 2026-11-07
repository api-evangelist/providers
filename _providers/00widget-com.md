---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: '00Widget API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: 00Widget API
  slug: 00widget-com-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/00widget-com/rules/00widget-com-rules.yml
  title: ''
  type: Spectral
  url: rules/00widget-com-rules.yml
- group: design
  href: https://artifacts.apis.io/00widget-com/json-ld/00widget-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/00widget-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/00widget-com/vocabulary/00widget-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/00widget-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/00widget-com/data-model/00widget-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/00widget-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/00widget-com/authentication/00widget-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/00widget-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/00widget-com/conformance/00widget-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/00widget-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/00widget-com/llms/00widget-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/00widget-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/00widget-com/mcp/00widget-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/00widget-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/00widget-com/well-known/00widget-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/00widget-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/00widget-com/hosts/00widget-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/00widget-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/00widget-com/vendors/00widget-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/00widget-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://api.00widget.com/login
- group: auth
  href: https://artifacts.apis.io/00widget-com/security/00widget-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/00widget-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://00widget.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.00widget.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.00widget.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.00widget.com/
- group: operate
  title: ''
  type: Support
  url: https://00widget.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://00widget.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://00widget.com/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/morais/00widget
coverage:
  checked: '2026-10-31'
  detail: API endpoints require authentication and the MCP endpoint returned 401 Unauthorized.
  evidence:
  - status: 401
    url: https://api.00widget.com/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: 00Widget provides native status widgets for Apple devices and Meta Quest, allowing agents and automations to display progress, results, and approvals directly on the Lock Screen, Dynamic Island, Apple TV, and Meta Quest. The platform offers real‑time visibility of agent activities, integrates with existing workflows, and supports subscription‑based access, delivering a native status layer that keeps users informed without opening a chat.
image: https://00widget.com/assets/launch/social-card.png?v=69c3ae44ae
json_schemas:
- name: GetV1StatusResponse
  property_count: 7
  slug: 00widget-com-get-v1-status-response
- name: PostDashboardRequest
  property_count: 7
  slug: 00widget-com-post-dashboard-request
- name: PostV1ActionsRequest
  property_count: 6
  slug: 00widget-com-post-v1-actions-request
- name: PostV1LiveActivitiesEndRequest
  property_count: 8
  slug: 00widget-com-post-v1-live-activities-end-request
- name: PostV1LiveActivitiesUpdateRequest
  property_count: 13
  slug: 00widget-com-post-v1-live-activities-update-request
- name: PutV1IntegrationsWebhooksRequest
  property_count: 2
  slug: 00widget-com-put-v1-integrations-webhooks-request
jsonld:
- class_count: 17
  name: 00Widget Com Context
  property_count: 50
  slug: 00widget-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.00widget.com.
  name: 00Widget MCP Server
  slug: 00widget-com-mcp-yml
modified: '2026-10-31'
name: 00Widget
nav: Providers
network: true
overview: '00Widget is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Apple, Meta Quest, Widgets, Agents, and MCP.


  The 00Widget catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  00Widget''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 16 more developer resources.'
plans:
- name: 00Widget Com Plans Pricing
  plan_count: 0
  slug: 00widget-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: 00Widget Com Rate Limits
  slug: 00widget-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: 00Widget API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: 00widget-com-rules
scopes:
- name: 00Widget Com Scopes
  scope_count: 0
  slug: 00widget-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 28.6
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 33.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 00Widget Com Authentication
  slug: 00widget-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 00Widget Com Domain Security
  slug: 00widget-com-domain-security
  summary_line: TLSv1.3
slug: 00widget-com
tags:
- Apple
- Meta Quest
- Widgets
- Agents
- MCP
- Status
website: https://00widget.com/
---
