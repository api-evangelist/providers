---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
  name: Fastballapi Com Agentic Access
  operation_count: 20
  slug: fastballapi-com-agentic-access
  summary_line: 20 operations
api_count: 1
apis:
- baseURL: https://mcp.fastballapi.com
  baseurl_source: declared
  description: The Basic lookup API from fastballapi-com — 5 operation(s) for basic lookup.
  name: fastballapi-com Basic lookup API
  slug: fastballapi-com-basic-lookup-api
- baseURL: https://mcp.fastballapi.com
  baseurl_source: declared
  description: The Multi-table API from fastballapi-com — 5 operation(s) for multi-table.
  name: fastballapi-com Multi Table API
  slug: fastballapi-com-multi-table-api
- baseURL: https://mcp.fastballapi.com
  baseurl_source: declared
  description: The Static reference API from fastballapi-com — 2 operation(s) for static reference.
  name: fastballapi-com Static reference API
  slug: fastballapi-com-static-reference-api
- baseURL: https://mcp.fastballapi.com
  baseurl_source: declared
  description: The Stats + aggregation API from fastballapi-com — 7 operation(s) for stats + aggregation.
  name: fastballapi-com Stats + aggregation API
  slug: fastballapi-com-stats-aggregation-api
- baseURL: https://mcp.fastballapi.com
  baseurl_source: declared
  description: The Time-series API from fastballapi-com — 1 operation(s) for time-series.
  name: fastballapi-com Time Series API
  slug: fastballapi-com-time-series-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/fastballapi-com/agentic-access/fastballapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fastballapi-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/fastballapi-com/rate-limits/fastballapi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fastballapi-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fastballapi-com/plans/fastballapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fastballapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fastballapi-com/rules/fastballapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/fastballapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/fastballapi-com/vocabulary/fastballapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fastballapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/fastballapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/fastballapi-com/conventions/fastballapi-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/fastballapi-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/fastballapi-com/conventions/fastballapi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fastballapi-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/fastballapi-com/authentication/fastballapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fastballapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/fastballapi-com/errors/fastballapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fastballapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fastballapi-com/conformance/fastballapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fastballapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fastballapi-com/llms/fastballapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fastballapi-com-llms.txt
- group: build
  href: https://artifacts.apis.io/fastballapi-com/mcp/fastballapi-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/fastballapi-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/fastballapi-com/mcp/fastballapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fastballapi-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/fastballapi-com/well-known/fastballapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fastballapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/fastballapi-com/hosts/fastballapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fastballapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/fastballapi-com/vendors/fastballapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fastballapi-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://fastballapi.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://fastballapi.com/status
- group: start
  title: ''
  type: Sandbox
  url: https://fastballapi.com/dashboard/playground
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fastballapi.com/for/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://fastballapi.com/changelog
- group: auth
  href: https://artifacts.apis.io/fastballapi-com/security/fastballapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fastballapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fastballapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fastballapi.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://fastballapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fastballapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fastballapi.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://fastballapi.com/signup
- group: start
  title: ''
  type: Login
  url: https://fastballapi.com/login
- group: docs
  title: ''
  type: APIReference
  url: https://fastballapi.com/docs
created: '2026-10-30'
description: FastballAPI provides a comprehensive baseball data API offering MLB and college baseball statistics, play‑by‑play details, pitch data, and betting odds. Since 2015 it serves developers with both REST endpoints and a Model Context Protocol (MCP) server, delivering real‑time game information, historical records, and analytical tools across 20 distinct endpoints. The service includes tiered pricing, a free credit tier, and extensive documentation to help integrate baseball data into apps, analytics platforms, and betting services.
image: https://fastballapi.com/opengraph-image?8a6b7f7b7786f567
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.fastballapi.com requiring an API key.
  name: fastballapi-com MCP Server
  slug: fastballapi-com-mcp-yml
modified: '2026-10-30'
name: fastballapi-com
nav: Providers
network: true
overview: 'fastballapi-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Basic lookup API, Multi Table API, Static reference API, and 2 more. Tagged areas include Baseball, Sports, Data, API, and MLB.


  The fastballapi-com catalog on APIs.io includes 1 Spectral governance ruleset.


  fastballapi-com''s developer surface includes authentication, support, sandbox, changelog, documentation, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Fastballapi Com Plans Pricing
  plan_count: 4
  slug: fastballapi-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Fastballapi Com Rate Limits
  slug: fastballapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: fastballapi-com API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: fastballapi-com-rules
score:
  band: strong
  composite: 62.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 75.7
    catalog_earned_first_party: 0.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 48.4
    developer_ergonomics: 56.4
    discoverability: 65.0
    operational_transparency: 50.5
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
  name: Fastballapi Com Authentication
  slug: fastballapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fastballapi Com Domain Security
  slug: fastballapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: fastballapi-com-get-game-skill
  slug: fastballapi-com-get-game-skill
slug: fastballapi-com
tags:
- Baseball
- Sports
- Data
- API
- MLB
website: https://fastballapi.com/
---
