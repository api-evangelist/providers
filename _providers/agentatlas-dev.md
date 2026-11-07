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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: MCP endpoint providing tool list and other services
  name: AgentAtlas MCP
  slug: agentatlas-mcp
- description: 'AgentAtlas API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: AgentAtlas API
  slug: agentatlas-dev-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/agentatlas-dev/plans/agentatlas-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentatlas-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentatlas-dev/rules/agentatlas-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/agentatlas-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/agentatlas-dev/json-ld/agentatlas-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentatlas-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentatlas-dev/vocabulary/agentatlas-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentatlas-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentatlas-dev/data-model/agentatlas-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentatlas-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/agentatlas-dev/changelog/agentatlas-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agentatlas-dev-changelog.yml
- group: auth
  href: https://artifacts.apis.io/agentatlas-dev/authentication/agentatlas-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentatlas-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentatlas-dev/conformance/agentatlas-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentatlas-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentatlas-dev/llms/agentatlas-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentatlas-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/agentatlas-dev/hosts/agentatlas-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentatlas-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentatlas-dev/vendors/agentatlas-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentatlas-dev-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://agentatlas.dev/cursorrules/security
- group: commercial
  title: ''
  type: Pricing
  url: https://agentatlas.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://agentatlas.dev/login
- group: docs
  title: ''
  type: Documentation
  url: https://agentatlas.dev/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentatlas.dev/mcp/category/developer
- group: start
  title: ''
  type: GettingStarted
  url: https://agentatlas.dev/tools/setup-kit
- group: auth
  href: https://artifacts.apis.io/agentatlas-dev/security/agentatlas-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentatlas-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentatlas.dev/
coverage:
  checked: '2026-11-01'
  detail: MCP endpoint only accepts POST; GET returns 405, no OpenAPI or other spec discovered.
  evidence:
  - status: 405
    url: https://agentatlas.dev/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 'agentatlas-dev is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://agentatlas.dev/og.png
json_schemas:
- name: PostMcpRequest
  property_count: 10
  slug: agentatlas-dev-post-mcp-request
jsonld:
- class_count: 1
  name: Agentatlas Dev Context
  property_count: 7
  slug: agentatlas-dev-context
layout: provider
modified: '2026-10-31'
name: AgentAtlas
nav: Providers
network: true
overview: 'AgentAtlas is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Agents, MCP, Tools, and Platform.


  The AgentAtlas catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentAtlas'' developer surface includes changelog, authentication, pricing, documentation, getting-started guide, and 14 more developer resources.'
plans:
- name: Agentatlas Dev Plans Pricing
  plan_count: 23
  slug: agentatlas-dev-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AgentAtlas API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: agentatlas-dev-rules
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 55.2
    catalog_earned_first_party: 12.0
    catalog_gap: 59.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 17.6
    developer_ergonomics: 27.4
    discoverability: 48.2
    operational_transparency: 21.1
  previous_composite: 35.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentatlas Dev Authentication
  slug: agentatlas-dev-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Agentatlas Dev Domain Security
  slug: agentatlas-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentatlas-dev
tags:
- Artificial Intelligence
- Agents
- MCP
- Tools
- Platform
website: https://agentatlas.dev/
---
