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
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Botfriendly Xyz Agentic Access
  operation_count: 11
  slug: botfriendly-xyz-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 1
apis:
- baseURL: https://botfriendly.xyz/api/v1
  baseurl_source: declared
  description: The Categories API from BotFriendly — 1 operation(s) for categories.
  name: BotFriendly Categories API
  slug: botfriendly-xyz-categories-api
- baseURL: https://botfriendly.xyz/api/v1
  baseurl_source: declared
  description: The Check API from BotFriendly — 1 operation(s) for check.
  name: BotFriendly Check API
  slug: botfriendly-xyz-check-api
- baseURL: https://botfriendly.xyz/api/v1
  baseurl_source: declared
  description: The Featured API from BotFriendly — 1 operation(s) for featured.
  name: BotFriendly Featured API
  slug: botfriendly-xyz-featured-api
- baseURL: https://botfriendly.xyz/api/v1
  baseurl_source: declared
  description: The Health API from BotFriendly — 1 operation(s) for health.
  name: BotFriendly Health API
  slug: botfriendly-xyz-health-api
- baseURL: https://botfriendly.xyz/api/v1
  baseurl_source: declared
  description: The Protocols API from BotFriendly — 1 operation(s) for protocols.
  name: BotFriendly Protocols API
  slug: botfriendly-xyz-protocols-api
- baseURL: https://botfriendly.xyz/api/v1
  baseurl_source: declared
  description: The Search API from BotFriendly — 1 operation(s) for search.
  name: BotFriendly Search API
  slug: botfriendly-xyz-search-api
- baseURL: https://botfriendly.xyz/api/v1
  baseurl_source: declared
  description: The Services API from BotFriendly — 2 operation(s) for services.
  name: BotFriendly Services API
  slug: botfriendly-xyz-services-api
- baseURL: https://botfriendly.xyz/api/v1
  baseurl_source: declared
  description: The Stats API from BotFriendly — 1 operation(s) for stats.
  name: BotFriendly Stats API
  slug: botfriendly-xyz-stats-api
- baseURL: https://botfriendly.xyz/api/v1
  baseurl_source: declared
  description: The Submissions API from BotFriendly — 1 operation(s) for submissions.
  name: BotFriendly Submissions API
  slug: botfriendly-xyz-submissions-api
- baseURL: https://botfriendly.xyz/api/v1
  baseurl_source: declared
  description: The Verify API from BotFriendly — 1 operation(s) for verify.
  name: BotFriendly Verify API
  slug: botfriendly-xyz-verify-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/botfriendly-xyz/agentic-access/botfriendly-xyz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/botfriendly-xyz-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/botfriendly-xyz/rate-limits/botfriendly-xyz-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/botfriendly-xyz-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/botfriendly-xyz/rules/botfriendly-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/botfriendly-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/botfriendly-xyz/json-ld/botfriendly-xyz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/botfriendly-xyz-context.jsonld
- group: design
  href: https://artifacts.apis.io/botfriendly-xyz/vocabulary/botfriendly-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/botfriendly-xyz-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/botfriendly-xyz/data-model/botfriendly-xyz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/botfriendly-xyz-data-model.yml
- group: build
  href: https://artifacts.apis.io/botfriendly-xyz/cli/botfriendly-xyz-cli.yml
  title: ''
  type: CLI
  url: cli/botfriendly-xyz-cli.yml
- group: design
  href: https://artifacts.apis.io/botfriendly-xyz/conventions/botfriendly-xyz-conventions.yml
  title: ''
  type: Conventions
  url: conventions/botfriendly-xyz-conventions.yml
- group: design
  href: https://artifacts.apis.io/botfriendly-xyz/errors/botfriendly-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/botfriendly-xyz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/botfriendly-xyz/conformance/botfriendly-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botfriendly-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/botfriendly-xyz/llms/botfriendly-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botfriendly-xyz-llms.txt
- group: agent
  href: https://artifacts.apis.io/botfriendly-xyz/mcp/botfriendly-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/botfriendly-xyz-mcp.yml
- group: agent
  href: https://artifacts.apis.io/botfriendly-xyz/well-known/botfriendly-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/botfriendly-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/botfriendly-xyz/hosts/botfriendly-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botfriendly-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/botfriendly-xyz/vendors/botfriendly-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botfriendly-xyz-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://botfriendly.xyz/libraries
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botfriendly.xyz/privacy
- group: start
  title: ''
  type: Login
  url: https://botfriendly.xyz/auth/login
- group: docs
  title: ''
  type: Documentation
  url: https://botfriendly.xyz/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://botfriendly.xyz/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/botfriendly-xyz/security/botfriendly-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botfriendly-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botfriendly.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://botfriendly.xyz/api/v1/openapi.json
- group: agent
  title: ''
  type: MCP
  url: https://mcp.botfriendly.xyz
- group: agent
  title: ''
  type: llms
  url: https://botfriendly.xyz/llms.txt
created: '2026-11-02'
description: BotFriendly.xyz is a discovery platform for services that AI agents can actually use. It provides a curated directory of APIs, tools, and merchants designed for machine-to-machine interactions, featuring MCP servers, open OpenAPI specs, llms.txt listings, and agent payment rails. All services are free to use without API keys, emphasizing transparency and ease of integration for autonomous agents.
image: https://botfriendly.xyz/og.png
json_schemas:
- name: Probe
  property_count: 6
  slug: botfriendly-xyz-probe
- name: Service
  property_count: 42
  slug: botfriendly-xyz-service
jsonld:
- class_count: 3
  name: Botfriendly Xyz Context
  property_count: 49
  slug: botfriendly-xyz-context
layout: provider
mcp_servers:
- description: Remote MCP server at botfriendly.xyz.
  name: BotFriendly MCP Server
  slug: botfriendly-xyz-mcp-yml
modified: '2026-11-02'
name: BotFriendly
nav: Providers
network: true
overview: 'BotFriendly publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Categories API, Check API, Featured API, and 7 more. Tagged areas include BotFriendly, AI Agents, Machine-to-Machine, API Directory, and OpenAPI.


  The BotFriendly catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BotFriendly''s developer surface includes CLI, documentation, getting-started guide, API reference, and 21 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 3
  name: Botfriendly Xyz Rate Limits
  slug: botfriendly-xyz-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: BotFriendly API Rules
  rule_count: 43
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 2
  slug: botfriendly-xyz-rules
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 58.0
    developer_ergonomics: 28.6
    discoverability: 65.0
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Botfriendly Xyz Domain Security
  slug: botfriendly-xyz-domain-security
  summary_line: TLSv1.3 · HSTS
slug: botfriendly-xyz
tags:
- BotFriendly
- AI Agents
- Machine-to-Machine
- API Directory
- OpenAPI
website: https://botfriendly.xyz/
---
