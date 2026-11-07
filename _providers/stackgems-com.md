---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Stackgems Com Agentic Access
  operation_count: 8
  slug: stackgems-com-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- description: Public read-only JSON catalog. No registration or credentials.
  name: Stack Gems Catalog API
  slug: stack-gems-catalog-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/stackgems-com/agentic-access/stackgems-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/stackgems-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/stackgems-com/rules/stackgems-com-rules.yml
  title: ''
  type: Spectral
  url: rules/stackgems-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/stackgems-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/stackgems-com/conventions/stackgems-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/stackgems-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/stackgems-com/errors/stackgems-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stackgems-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/stackgems-com/conformance/stackgems-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stackgems-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/stackgems-com/llms/stackgems-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stackgems-com-llms.txt
- group: build
  href: https://artifacts.apis.io/stackgems-com/mcp/stackgems-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/stackgems-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/stackgems-com/mcp/stackgems-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/stackgems-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/stackgems-com/well-known/stackgems-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stackgems-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/stackgems-com/hosts/stackgems-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stackgems-com-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://stackgems.com/tag/security
- group: start
  title: ''
  type: Sandbox
  url: https://stackgems.com/tag/sandbox
- group: build
  title: ''
  type: SDKs
  url: https://stackgems.com/stacks/libraries
- group: auth
  href: https://artifacts.apis.io/stackgems-com/security/stackgems-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stackgems-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stackgems.com/
- group: docs
  title: ''
  type: Documentation
  url: https://stackgems.com/for-agents.md
- group: docs
  title: ''
  type: APIReference
  url: https://stackgems.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://stackgems.com/about
created: '2026-10-31'
description: Stack Gems is an agent‑operated catalog of developer tools, offering human‑vetted, opinionated reviews of 955 tools and 527 skills across 13 stacks. It provides a JSON API, MCP server, OpenAPI spec, and llms.txt for machine consumption, designed for LLMs, agents, and automated tools.
image: https://stackgems.com/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at stackgems.com.
  name: stackgems-com MCP Server
  slug: stackgems-com-mcp-yml
modified: '2026-10-31'
name: stackgems-com
nav: Providers
network: true
overview: 'stackgems-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Catalog, Agent-Operated, and OpenAPI.


  The stackgems-com catalog on APIs.io includes 1 Spectral governance ruleset.


  stackgems-com''s developer surface includes sandbox, documentation, API reference, getting-started guide, and 15 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 0
  name: Stackgems Com Rate Limits
  slug: stackgems-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: stackgems-com API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: stackgems-com-rules
scopes:
- name: Stackgems Com Scopes
  scope_count: 0
  slug: stackgems-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 0.0
    contract_governance: 15.9
    contract_quality: 0.0
    developer_ergonomics: 26.8
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 19.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/stackgems-com/stackgems-com-2026-11-03T143712.png
security:
- kind: authentication
  name: Stackgems Com Authentication
  slug: stackgems-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Stackgems Com Domain Security
  slug: stackgems-com-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: get-gem
  slug: stackgems-com-get-gem
- name: list-gems
  slug: stackgems-com-list-gems
slug: stackgems-com
tags:
- Company
- Developer Tools
- Catalog
- Agent-Operated
- OpenAPI
website: https://stackgems.com/
---
