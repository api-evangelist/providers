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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dunkapi Com Agentic Access
  operation_count: 18
  slug: dunkapi-com-agentic-access
  summary_line: 18 operations
api_count: 1
apis:
- baseURL: https://mcp.dunkapi.com
  baseurl_source: declared
  description: The Basic lookup API from dunkapi-com — 5 operation(s) for basic lookup.
  name: dunkapi-com Basic lookup API
  slug: dunkapi-com-basic-lookup-api
- baseURL: https://mcp.dunkapi.com
  baseurl_source: declared
  description: The Multi-table API from dunkapi-com — 4 operation(s) for multi-table.
  name: dunkapi-com Multi Table API
  slug: dunkapi-com-multi-table-api
- baseURL: https://mcp.dunkapi.com
  baseurl_source: declared
  description: The Static reference API from dunkapi-com — 2 operation(s) for static reference.
  name: dunkapi-com Static reference API
  slug: dunkapi-com-static-reference-api
- baseURL: https://mcp.dunkapi.com
  baseurl_source: declared
  description: The Stats + aggregation API from dunkapi-com — 6 operation(s) for stats + aggregation.
  name: dunkapi-com Stats + aggregation API
  slug: dunkapi-com-stats-aggregation-api
- baseURL: https://mcp.dunkapi.com
  baseurl_source: declared
  description: The Time-series API from dunkapi-com — 1 operation(s) for time-series.
  name: dunkapi-com Time Series API
  slug: dunkapi-com-time-series-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/dunkapi-com/agentic-access/dunkapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dunkapi-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dunkapi-com/plans/dunkapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dunkapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dunkapi-com/rules/dunkapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dunkapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dunkapi-com/vocabulary/dunkapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dunkapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dunkapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/dunkapi-com/changelog/dunkapi-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dunkapi-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/dunkapi-com/authentication/dunkapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dunkapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dunkapi-com/errors/dunkapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dunkapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dunkapi-com/conformance/dunkapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dunkapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dunkapi-com/llms/dunkapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dunkapi-com-llms.txt
- group: build
  href: https://artifacts.apis.io/dunkapi-com/mcp/dunkapi-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dunkapi-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dunkapi-com/mcp/dunkapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dunkapi-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dunkapi-com/well-known/dunkapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dunkapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dunkapi-com/hosts/dunkapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dunkapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dunkapi-com/vendors/dunkapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dunkapi-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/dunkapi-com/packages/dunkapi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/dunkapi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/dunkapi-com/packages/dunkapi-com-packages.yml
  title: ''
  type: Packages
  url: packages/dunkapi-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://dunkapi.com/status
- group: start
  title: ''
  type: Sandbox
  url: https://dunkapi.com/dashboard/playground
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dunkapi.com/for/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://dunkapi.com/changelog
- group: auth
  href: https://artifacts.apis.io/dunkapi-com/security/dunkapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dunkapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dunkapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dunkapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dunkapi.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://dunkapi.com/docs
- group: operate
  title: ''
  type: Support
  url: https://dunkapi.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://dunkapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dunkapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dunkapi.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://dunkapi.com/signup
created: '2026-10-30'
description: DunkAPI provides real‑time NBA data including player statistics, game odds, play‑by‑play events, shot locations and historical odds. The service offers both a traditional REST API and a Model Context Protocol (MCP) server, delivering data to developers building sports‑analytics, betting, fantasy‑sports and fan‑engagement applications. Since 2023 the platform covers NBA, WNBA and college basketball, with tiered pricing plans and a free tier granting 500 monthly credits. Documentation, pricing, support and terms are publicly available on the company’s website.
image: https://dunkapi.com/opengraph-image?8a6b7f7b7786f567
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.dunkapi.com requiring an API key.
  name: dunkapi-com MCP Server
  slug: dunkapi-com-mcp-yml
modified: '2026-10-30'
name: dunkapi-com
nav: Providers
network: true
overview: 'dunkapi-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Basic lookup API, Multi Table API, Static reference API, and 2 more. Tagged areas include Company, Sports, Basketball, NBA, and Data.


  The dunkapi-com catalog on APIs.io includes 1 Spectral governance ruleset.


  dunkapi-com''s developer surface includes changelog, authentication, sandbox, documentation, API reference, getting-started guide, support, and 24 more developer resources.'
plans:
- name: Dunkapi Com Plans Pricing
  plan_count: 4
  slug: dunkapi-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Dunkapi Com Rate Limits
  slug: dunkapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: dunkapi-com API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: dunkapi-com-rules
scopes:
- name: Dunkapi Com Scopes
  scope_count: 0
  slug: dunkapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.1
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 51.4
    developer_ergonomics: 50.5
    discoverability: 65.0
    operational_transparency: 15.8
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dunkapi-com/dunkapi-com-2026-11-03T131121.png
security:
- kind: authentication
  name: Dunkapi Com Authentication
  slug: dunkapi-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dunkapi Com Domain Security
  slug: dunkapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: dunkapi-com-basic
  slug: dunkapi-com-basic
slug: dunkapi-com
tags:
- Company
- Sports
- Basketball
- NBA
- Data
website: https://dunkapi.com/
---
