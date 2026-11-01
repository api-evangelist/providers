---
agent_readiness:
  band: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
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
  score: 41.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Puckapi Com Agentic Access
  operation_count: 22
  slug: puckapi-com-agentic-access
  summary_line: 22 operations
api_count: 1
apis:
- baseURL: https://mcp.puckapi.com
  baseurl_source: declared
  description: The Basic lookup API from puckapi-com — 3 operation(s) for basic lookup.
  name: puckapi-com Basic lookup API
  slug: puckapi-com-basic-lookup-api
- baseURL: https://mcp.puckapi.com
  baseurl_source: declared
  description: The Model projections API from puckapi-com — 1 operation(s) for model projections.
  name: puckapi-com Model projections API
  slug: puckapi-com-model-projections-api
- baseURL: https://mcp.puckapi.com
  baseurl_source: declared
  description: The Multi-table API from puckapi-com — 9 operation(s) for multi-table.
  name: puckapi-com Multi Table API
  slug: puckapi-com-multi-table-api
- baseURL: https://mcp.puckapi.com
  baseurl_source: declared
  description: The Static reference API from puckapi-com — 1 operation(s) for static reference.
  name: puckapi-com Static reference API
  slug: puckapi-com-static-reference-api
- baseURL: https://mcp.puckapi.com
  baseurl_source: declared
  description: The Stats + aggregation API from puckapi-com — 7 operation(s) for stats + aggregation.
  name: puckapi-com Stats + aggregation API
  slug: puckapi-com-stats-aggregation-api
- baseURL: https://mcp.puckapi.com
  baseurl_source: declared
  description: The Time-series API from puckapi-com — 1 operation(s) for time-series.
  name: puckapi-com Time Series API
  slug: puckapi-com-time-series-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/puckapi-com/agentic-access/puckapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/puckapi-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/puckapi-com/rate-limits/puckapi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/puckapi-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/puckapi-com/plans/puckapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/puckapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/puckapi-com/rules/puckapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/puckapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/puckapi-com/vocabulary/puckapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/puckapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/puckapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/puckapi-com/changelog/puckapi-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/puckapi-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/puckapi-com/conventions/puckapi-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/puckapi-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/puckapi-com/conventions/puckapi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/puckapi-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/puckapi-com/authentication/puckapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/puckapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/puckapi-com/errors/puckapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/puckapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/puckapi-com/conformance/puckapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/puckapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/puckapi-com/llms/puckapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/puckapi-com-llms.txt
- group: build
  href: https://artifacts.apis.io/puckapi-com/mcp/puckapi-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/puckapi-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/puckapi-com/mcp/puckapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/puckapi-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/puckapi-com/well-known/puckapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/puckapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/puckapi-com/hosts/puckapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/puckapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/puckapi-com/vendors/puckapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/puckapi-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/puckapi-com/packages/puckapi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/puckapi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/puckapi-com/packages/puckapi-com-packages.yml
  title: ''
  type: Packages
  url: packages/puckapi-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://puckapi.com/status
- group: start
  title: ''
  type: Sandbox
  url: https://puckapi.com/dashboard/playground
- group: start
  title: ''
  type: Login
  url: https://puckapi.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://puckapi.com/for/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://puckapi.com/changelog
- group: auth
  href: https://artifacts.apis.io/puckapi-com/security/puckapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/puckapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://puckapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://puckapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://puckapi.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://puckapi.com/signup
- group: operate
  title: ''
  type: Support
  url: https://puckapi.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://puckapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://puckapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://puckapi.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/puckapi
created: '2026-10-31'
description: PuckAPI provides comprehensive hockey data through a REST API and Model Context Protocol (MCP) server. It offers NHL and PWHL statistics, play‑by‑play data, expected goals, and betting odds. Users can start for free with 500 credits per month and upgrade to paid plans for higher limits. The service includes detailed documentation, pricing information, and support channels.
image: https://puckapi.com/opengraph-image?8a6b7f7b7786f567
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.puckapi.com requiring an API key.
  name: puckapi-com MCP Server
  slug: puckapi-com-mcp-yml
modified: '2026-10-31'
name: puckapi-com
nav: Providers
network: true
overview: 'puckapi-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Basic lookup API, Model projections API, Multi Table API, and 3 more. Tagged areas include Sports, Hockey, Data, API, and Statistics.


  The puckapi-com catalog on APIs.io includes 1 Spectral governance ruleset.


  puckapi-com''s developer surface includes changelog, authentication, sandbox, documentation, API reference, getting-started guide, support, and 28 more developer resources.'
plans:
- name: Puckapi Com Plans Pricing
  plan_count: 4
  slug: puckapi-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Puckapi Com Rate Limits
  slug: puckapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: puckapi-com API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: puckapi-com-rules
scopes:
- name: Puckapi Com Scopes
  scope_count: 0
  slug: puckapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 68.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 75.7
    catalog_earned_first_party: 0.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 48.4
    developer_ergonomics: 75.5
    discoverability: 65.0
    operational_transparency: 55.8
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
  name: Puckapi Com Authentication
  slug: puckapi-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Puckapi Com Domain Security
  slug: puckapi-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: get-standings
  slug: puckapi-com-get-standings
- name: get-team-stats
  slug: puckapi-com-get-team-stats
- name: list-teams
  slug: puckapi-com-list-teams
slug: puckapi-com
tags:
- Sports
- Hockey
- Data
- API
- Statistics
website: https://puckapi.com/
---
