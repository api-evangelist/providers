---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: StrikerAPI provides soccer data via REST and MCP, including goals, lineups, odds, and statistics.
  name: StrikerAPI API
  slug: api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/strikerapi-com/rules/strikerapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/strikerapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/strikerapi-com/vocabulary/strikerapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/strikerapi-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/strikerapi-com/conformance/strikerapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/strikerapi-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/strikerapi-com/plans/strikerapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/strikerapi-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/strikerapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/strikerapi-com/authentication/strikerapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/strikerapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/strikerapi-com/errors/strikerapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/strikerapi-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/strikerapi-com/llms/strikerapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/strikerapi-com-llms.txt
- group: build
  href: https://artifacts.apis.io/strikerapi-com/mcp/strikerapi-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/strikerapi-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/strikerapi-com/mcp/strikerapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/strikerapi-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/strikerapi-com/well-known/strikerapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/strikerapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/strikerapi-com/hosts/strikerapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/strikerapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/strikerapi-com/vendors/strikerapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/strikerapi-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://strikerapi.com/status
- group: start
  title: ''
  type: Sandbox
  url: https://strikerapi.com/dashboard/playground
- group: docs
  title: ''
  type: APIReference
  url: https://strikerapi.com/changelog
- group: auth
  href: https://artifacts.apis.io/strikerapi-com/security/strikerapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/strikerapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://strikerapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://strikerapi.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://strikerapi.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://strikerapi.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://strikerapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://strikerapi.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://strikerapi.com/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://strikerapi.com/docs
created: '2026-10-31'
description: StrikerAPI provides comprehensive soccer data, including goalscorer odds, lineups, shot maps, expected goals (xG), and detailed statistics across 17 major leagues. It offers both REST and Model Context Protocol (MCP) access, with free tier credits and paid plans for higher usage.
image: https://strikerapi.com/opengraph-image?8a6b7f7b7786f567
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.strikerapi.com requiring an API key.
  name: strikerapi-com MCP Server
  slug: strikerapi-com-mcp-yml
modified: '2026-10-31'
name: strikerapi-com
nav: Providers
network: true
overview: 'strikerapi-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Soccer, Sports Data, Odds, Statistics, and API.


  The strikerapi-com catalog on APIs.io includes 1 Spectral governance ruleset.


  strikerapi-com''s developer surface includes authentication, sandbox, API reference, documentation, pricing, support, signup flow, and 18 more developer resources.'
plans:
- name: Strikerapi Com Plans Pricing
  plan_count: 4
  slug: strikerapi-com-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: strikerapi-com API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: strikerapi-com-rules
scopes:
- name: Strikerapi Com Scopes
  scope_count: 0
  slug: strikerapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 63.5
    catalog_earned_first_party: 0.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 0.0
    developer_ergonomics: 68.3
    discoverability: 56.7
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Strikerapi Com Authentication
  slug: strikerapi-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Strikerapi Com Domain Security
  slug: strikerapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: get-events
  slug: strikerapi-com-get-events
slug: strikerapi-com
tags:
- Soccer
- Sports Data
- Odds
- Statistics
- API
website: https://strikerapi.com/
---
