---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Adios Hr Agentic Access
  operation_count: 14
  slug: adios-hr-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 1
apis:
- baseURL: https://adios.hr
  baseurl_source: declared
  description: The Radar API API from adios-hr — 13 operation(s) for radar api.
  name: adios-hr Radar API
  slug: adios-hr-radar-api-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/adios-hr/llms/adios-hr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adios-hr-llms.txt
- group: agent
  href: https://artifacts.apis.io/adios-hr/agentic-access/adios-hr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adios-hr-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/adios-hr/rules/adios-hr-rules.yml
  title: ''
  type: Spectral
  url: rules/adios-hr-rules.yml
- group: design
  href: https://artifacts.apis.io/adios-hr/json-ld/adios-hr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adios-hr-context.jsonld
- group: design
  href: https://artifacts.apis.io/adios-hr/vocabulary/adios-hr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adios-hr-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/adios-hr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/adios-hr/data-model/adios-hr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adios-hr-data-model.yml
- group: design
  href: https://artifacts.apis.io/adios-hr/conventions/adios-hr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adios-hr-conventions.yml
- group: auth
  href: https://artifacts.apis.io/adios-hr/authentication/adios-hr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adios-hr-authentication.yml
- group: operate
  href: https://artifacts.apis.io/adios-hr/lifecycle/adios-hr-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/adios-hr-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/adios-hr/lifecycle/adios-hr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adios-hr-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/adios-hr/errors/adios-hr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adios-hr-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adios-hr/conformance/adios-hr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adios-hr-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adios-hr/mcp/adios-hr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adios-hr-mcp.yml
- group: other
  href: https://artifacts.apis.io/adios-hr/hosts/adios-hr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adios-hr-hosts.yml
- group: other
  href: https://artifacts.apis.io/adios-hr/vendors/adios-hr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adios-hr-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://adios.hr/account/login
- group: docs
  title: ''
  type: Documentation
  url: https://adios.hr/developers/radar/docs
- group: docs
  title: ''
  type: APIReference
  url: https://adios.hr/developers
- group: company
  title: ''
  type: Website
  url: https://adios.hr/
- group: auth
  href: https://artifacts.apis.io/adios-hr/security/adios-hr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adios-hr-domain-security.yml
created: '2026-10-31'
description: 'adios-hr is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://adios.hr/img/og/adios-hr-home-overview-v1.jpg?v=Bovv4yF8JuMkCoYnYTyBH9rNHXoTzgjSFIgUkQX-Iqk
json_schemas:
- name: radar_articles_response
  property_count: 2
  slug: adios-hr-radar-articles-response
- name: radar_catalogue_response
  property_count: 2
  slug: adios-hr-radar-catalogue-response
- name: radar_subscription_response
  property_count: 2
  slug: adios-hr-radar-subscription-response
- name: radar_webhook_create_response
  property_count: 2
  slug: adios-hr-radar-webhook-create-response
- name: radar_webhook_deliveries_response
  property_count: 2
  slug: adios-hr-radar-webhook-deliveries-response
- name: radar_webhook_test_response
  property_count: 2
  slug: adios-hr-radar-webhook-test-response
jsonld:
- class_count: 20
  name: Adios Hr Context
  property_count: 71
  slug: adios-hr-context
layout: provider
mcp_servers:
- description: Remote MCP server at adios.hr.
  name: adios-hr MCP Server
  slug: adios-hr-mcp-yml
modified: '2026-10-31'
name: adios-hr
nav: Providers
network: true
overview: 'adios-hr publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Radar API. Tagged areas include Company.


  The adios-hr catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  adios-hr''s developer surface includes authentication, documentation, API reference, and 18 more developer resources.'
random_paper: 23
rate_limits:
- limit_count: 0
  name: Adios Hr Rate Limits
  slug: adios-hr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: adios-hr API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: adios-hr-rules
scopes:
- name: Adios Hr Scopes
  scope_count: 0
  slug: adios-hr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 6.6
    contract_governance: 22.0
    contract_quality: 67.2
    developer_ergonomics: 26.7
    discoverability: 48.3
    operational_transparency: 7.9
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adios Hr Authentication
  slug: adios-hr-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Adios Hr Domain Security
  slug: adios-hr-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: adios-hr-radar
  slug: adios-hr-radar
slug: adios-hr
tags:
- Company
website: https://adios.hr/
---
