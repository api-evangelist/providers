---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Endzoneapi Com Agentic Access
  operation_count: 20
  slug: endzoneapi-com-agentic-access
  summary_line: 20 operations
api_count: 1
apis:
- baseURL: https://mcp.endzoneapi.com
  baseurl_source: declared
  description: The Basic lookup API from endzoneapi-com — 5 operation(s) for basic lookup.
  name: endzoneapi-com Basic lookup API
  slug: endzoneapi-com-basic-lookup-api
- baseURL: https://mcp.endzoneapi.com
  baseurl_source: declared
  description: The Multi-table API from endzoneapi-com — 7 operation(s) for multi-table.
  name: endzoneapi-com Multi Table API
  slug: endzoneapi-com-multi-table-api
- baseURL: https://mcp.endzoneapi.com
  baseurl_source: declared
  description: The Static reference API from endzoneapi-com — 1 operation(s) for static reference.
  name: endzoneapi-com Static reference API
  slug: endzoneapi-com-static-reference-api
- baseURL: https://mcp.endzoneapi.com
  baseurl_source: declared
  description: The Stats + aggregation API from endzoneapi-com — 6 operation(s) for stats + aggregation.
  name: endzoneapi-com Stats + aggregation API
  slug: endzoneapi-com-stats-aggregation-api
- baseURL: https://mcp.endzoneapi.com
  baseurl_source: declared
  description: The Time-series API from endzoneapi-com — 1 operation(s) for time-series.
  name: endzoneapi-com Time Series API
  slug: endzoneapi-com-time-series-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/endzoneapi-com/agentic-access/endzoneapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/endzoneapi-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/endzoneapi-com/rate-limits/endzoneapi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/endzoneapi-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/endzoneapi-com/plans/endzoneapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/endzoneapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/endzoneapi-com/rules/endzoneapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/endzoneapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/endzoneapi-com/vocabulary/endzoneapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/endzoneapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/endzoneapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/endzoneapi-com/changelog/endzoneapi-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/endzoneapi-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/endzoneapi-com/authentication/endzoneapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/endzoneapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/endzoneapi-com/lifecycle/endzoneapi-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/endzoneapi-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/endzoneapi-com/errors/endzoneapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/endzoneapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/endzoneapi-com/conformance/endzoneapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/endzoneapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/endzoneapi-com/llms/endzoneapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/endzoneapi-com-llms.txt
- group: build
  href: https://artifacts.apis.io/endzoneapi-com/mcp/endzoneapi-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/endzoneapi-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/endzoneapi-com/mcp/endzoneapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/endzoneapi-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/endzoneapi-com/well-known/endzoneapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/endzoneapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/endzoneapi-com/hosts/endzoneapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/endzoneapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/endzoneapi-com/vendors/endzoneapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/endzoneapi-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://endzoneapi.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://endzoneapi.com/status
- group: start
  title: ''
  type: Sandbox
  url: https://endzoneapi.com/dashboard/playground
- group: operate
  title: ''
  type: ChangeLog
  url: https://endzoneapi.com/changelog
- group: auth
  href: https://artifacts.apis.io/endzoneapi-com/security/endzoneapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/endzoneapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://endzoneapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://endzoneapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://endzoneapi.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://endzoneapi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://endzoneapi.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://endzoneapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://endzoneapi.com/privacy
created: '2026-10-30'
description: EndzoneAPI provides comprehensive NFL data including player props, play‑by‑play, EPA, stats, odds, and related college football data via REST and MCP endpoints. It offers over 1.2 million plays, 470 k weekly player stats, injury reports, depth charts, snap counts, and betting odds, with a free tier of 500 credits per month.
image: https://endzoneapi.com/opengraph-image?8a6b7f7b7786f567
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.endzoneapi.com requiring an API key.
  name: endzoneapi-com MCP Server
  slug: endzoneapi-com-mcp-yml
modified: '2026-10-30'
name: endzoneapi-com
nav: Providers
network: true
overview: 'endzoneapi-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Basic lookup API, Multi Table API, Static reference API, and 2 more. Tagged areas include Sports, Football, NFL, Data API, and Odds.


  The endzoneapi-com catalog on APIs.io includes 1 Spectral governance ruleset.


  endzoneapi-com''s developer surface includes changelog, authentication, support, sandbox, documentation, API reference, pricing, and 22 more developer resources.'
plans:
- name: Endzoneapi Com Plans Pricing
  plan_count: 4
  slug: endzoneapi-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Endzoneapi Com Rate Limits
  slug: endzoneapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: endzoneapi-com API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: endzoneapi-com-rules
scopes:
- name: Endzoneapi Com Scopes
  scope_count: 0
  slug: endzoneapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 75.7
    catalog_earned_first_party: 0.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 48.4
    developer_ergonomics: 58.8
    discoverability: 65.0
    operational_transparency: 50.5
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
  name: Endzoneapi Com Authentication
  slug: endzoneapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Endzoneapi Com Domain Security
  slug: endzoneapi-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: list-teams
  slug: endzoneapi-com-list_teams
slug: endzoneapi-com
tags:
- Sports
- Football
- NFL
- Data API
- Odds
- MCP
website: https://endzoneapi.com/
---
