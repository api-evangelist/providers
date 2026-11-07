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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Routinerun Com Agentic Access
  operation_count: 3
  slug: routinerun-com-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 2
apis:
- baseURL: https://api.routinerun.com
  baseurl_source: declared
  description: The Events API from routinerun-com — 1 operation(s) for events.
  name: routinerun-com Events API
  slug: routinerun-com-events-api
- baseURL: https://api.routinerun.com
  baseurl_source: declared
  description: The Runs API from routinerun-com — 1 operation(s) for runs.
  name: routinerun-com Runs API
  slug: routinerun-com-runs-api
- baseURL: https://api.routinerun.com
  baseurl_source: declared
  description: The Commands API from routinerun-com — 1 operation(s) for commands.
  name: routinerun-com Commands API
  slug: routinerun-com-commands-api
- baseURL: https://api.routinerun.com
  baseurl_source: declared
  description: The History API from routinerun-com — 1 operation(s) for history.
  name: routinerun-com History API
  slug: routinerun-com-history-api
- baseURL: https://api.routinerun.com
  baseurl_source: declared
  description: The Pagerduty API from routinerun-com — 1 operation(s) for pagerduty.
  name: routinerun-com Pagerduty API
  slug: routinerun-com-pagerduty-api
- baseURL: https://api.routinerun.com
  baseurl_source: declared
  description: The Routines API from routinerun-com — 3 operation(s) for routines.
  name: routinerun-com Routines API
  slug: routinerun-com-routines-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/routinerun-com/agentic-access/routinerun-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/routinerun-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/routinerun-com/rules/routinerun-com-rules.yml
  title: ''
  type: Spectral
  url: rules/routinerun-com-rules.yml
- group: design
  href: https://artifacts.apis.io/routinerun-com/json-ld/routinerun-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/routinerun-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/routinerun-com/vocabulary/routinerun-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/routinerun-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/routinerun-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/routinerun-com/data-model/routinerun-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/routinerun-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/routinerun-com/changelog/routinerun-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/routinerun-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/routinerun-com/authentication/routinerun-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/routinerun-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/routinerun-com/errors/routinerun-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/routinerun-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/routinerun-com/conformance/routinerun-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/routinerun-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/routinerun-com/llms/routinerun-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/routinerun-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/routinerun-com/mcp/routinerun-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/routinerun-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/routinerun-com/well-known/routinerun-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/routinerun-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/routinerun-com/hosts/routinerun-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/routinerun-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/routinerun-com/vendors/routinerun-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/routinerun-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://routinerun.com/press
- group: auth
  href: https://artifacts.apis.io/routinerun-com/security/routinerun-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/routinerun-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://routinerun.com/
- group: docs
  title: ''
  type: Documentation
  url: https://routinerun.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://api.routinerun.com/mcp/public
- group: commercial
  title: ''
  type: Pricing
  url: https://routinerun.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://routinerun.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://routinerun.com/terms
- group: operate
  title: ''
  type: Support
  url: https://routinerun.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/routinerun
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.routinerun.com/mcp
  - status: 200
    url: https://routinerun.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Say what you do, paste a list, pick a starter or just start, and Routine Run walks you through it one step at a time. It handles what it can, asks before anything irreversible, and keeps what you change for the next run.
image: https://routinerun.com/img/logo-mark.webp
json_schemas:
- name: Accepted
  property_count: 1
  slug: routinerun-com-accepted
jsonld:
- class_count: 2
  name: Routinerun Com Context
  property_count: 2
  slug: routinerun-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.routinerun.com.
  name: routinerun-com MCP Server
  slug: routinerun-com-mcp-yml
modified: '2026-10-30'
name: routinerun-com
nav: Providers
network: true
overview: 'routinerun-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Events API, Runs API, Commands API, and 3 more. Tagged areas include Company, Automation, Productivity, Task Management, and No-Code.


  The routinerun-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  routinerun-com''s developer surface includes changelog, authentication, documentation, API reference, pricing, support, and 19 more developer resources.'
plans:
- name: Routinerun Com Plans Pricing
  plan_count: 2
  slug: routinerun-com-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: routinerun-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: routinerun-com-rules
scopes:
- name: Routinerun Com Scopes
  scope_count: 0
  slug: routinerun-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 61.2
    catalog_earned_first_party: 8.0
    catalog_gap: 53.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 51.6
    developer_ergonomics: 29.0
    discoverability: 74.1
    operational_transparency: 18.4
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: unknown
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
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/routinerun-com/routinerun-com-2026-11-03T142432.png
security:
- kind: authentication
  name: Routinerun Com Authentication
  slug: routinerun-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Routinerun Com Domain Security
  slug: routinerun-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: list-runs
  slug: routinerun-com-list-runs
slug: routinerun-com
tags:
- Company
- Automation
- Productivity
- Task Management
- No-Code
website: https://routinerun.com/
---
