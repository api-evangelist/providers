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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Acesapi Com Agentic Access
  operation_count: 13
  slug: acesapi-com-agentic-access
  summary_line: 13 operations
api_count: 1
apis:
- baseURL: https://mcp.acesapi.com
  baseurl_source: declared
  description: The Basic lookup API from acesapi-com — 6 operation(s) for basic lookup.
  name: acesapi-com Basic lookup API
  slug: acesapi-com-basic-lookup-api
- baseURL: https://mcp.acesapi.com
  baseurl_source: declared
  description: The Multi-table API from acesapi-com — 3 operation(s) for multi-table.
  name: acesapi-com Multi Table API
  slug: acesapi-com-multi-table-api
- baseURL: https://mcp.acesapi.com
  baseurl_source: declared
  description: The Static reference API from acesapi-com — 2 operation(s) for static reference.
  name: acesapi-com Static reference API
  slug: acesapi-com-static-reference-api
- baseURL: https://mcp.acesapi.com
  baseurl_source: declared
  description: The Stats + aggregation API from acesapi-com — 2 operation(s) for stats + aggregation.
  name: acesapi-com Stats + aggregation API
  slug: acesapi-com-stats-aggregation-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/acesapi-com/agentic-access/acesapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/acesapi-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/acesapi-com/rules/acesapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/acesapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/acesapi-com/vocabulary/acesapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/acesapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/acesapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/acesapi-com/errors/acesapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/acesapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/acesapi-com/conformance/acesapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/acesapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/acesapi-com/llms/acesapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acesapi-com-llms.txt
- group: build
  href: https://artifacts.apis.io/acesapi-com/mcp/acesapi-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/acesapi-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/acesapi-com/mcp/acesapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/acesapi-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/acesapi-com/well-known/acesapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/acesapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/acesapi-com/hosts/acesapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acesapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/acesapi-com/vendors/acesapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/acesapi-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://acesapi.com/status
- group: start
  title: ''
  type: Sandbox
  url: https://acesapi.com/dashboard/playground
- group: start
  title: ''
  type: DeveloperPortal
  url: https://acesapi.com/for/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://acesapi.com/changelog
- group: auth
  href: https://artifacts.apis.io/acesapi-com/authentication/acesapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/acesapi-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/acesapi-com/security/acesapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acesapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acesapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://acesapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://acesapi.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://acesapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://acesapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acesapi.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://acesapi.com/support
- group: start
  title: ''
  type: SignUp
  url: https://acesapi.com/signup
- group: start
  title: ''
  type: Login
  url: https://acesapi.com/login
created: '2026-10-30'
description: AcesAPI provides a comprehensive tennis data API offering ATP and WTA match results, player rankings, head‑to‑head records, surface Elo ratings, and sportsbook lines since 2007. The service includes 13 endpoints accessible via REST or Model Context Protocol (MCP), with free and paid tiers, detailed documentation, and a developer portal.
image: https://acesapi.com/opengraph-image?8a6b7f7b7786f567
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.acesapi.com requiring an API key.
  name: acesapi-com MCP Server
  slug: acesapi-com-mcp-yml
modified: '2026-10-30'
name: acesapi-com
nav: Providers
network: true
overview: 'acesapi-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Basic lookup API, Multi Table API, Static reference API, and 1 more. Tagged areas include Tennis, Sports, Data, API, and MCP.


  The acesapi-com catalog on APIs.io includes 1 Spectral governance ruleset.


  acesapi-com''s developer surface includes sandbox, changelog, authentication, documentation, API reference, pricing, support, and 20 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: acesapi-com API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: acesapi-com-rules
score:
  band: developing
  composite: 53.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.7
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 48.4
    developer_ergonomics: 56.4
    discoverability: 65.0
    operational_transparency: 31.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Acesapi Com Authentication
  slug: acesapi-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Acesapi Com Domain Security
  slug: acesapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 13
skills:
- name: get-head-to-head
  slug: get-head-to-head
- name: get-match
  slug: get-match
- name: get-matches
  slug: get-matches
- name: get-player-matches
  slug: get-player-matches
- name: get-player-stats
  slug: get-player-stats
- name: get-player
  slug: get-player
- name: get-rankings
  slug: get-rankings
- name: get-ratings
  slug: get-ratings
- name: get-schedule
  slug: get-schedule
- name: get-surface-splits
  slug: get-surface-splits
- name: get-tournament
  slug: get-tournament
- name: list-tournaments
  slug: list-tournaments
- name: search-players
  slug: search-players
slug: acesapi-com
tags:
- Tennis
- Sports
- Data
- API
- MCP
- Rankings
website: https://acesapi.com/
---
