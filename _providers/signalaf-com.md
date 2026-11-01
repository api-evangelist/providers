---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: self
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
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Signalaf Com Agentic Access
  operation_count: 5
  slug: signalaf-com-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://signalaf.com/api/v1
  baseurl_source: declared
  description: The hall API from signalaf-com — 1 operation(s) for hall.
  name: signalaf-com Hall API
  slug: signalaf-com-hall-api
- baseURL: https://signalaf.com/api/v1
  baseurl_source: declared
  description: The leaderboard API from signalaf-com — 1 operation(s) for leaderboard.
  name: signalaf-com Leaderboard API
  slug: signalaf-com-leaderboard-api
- baseURL: https://signalaf.com/api/v1
  baseurl_source: declared
  description: The metrics API from signalaf-com — 1 operation(s) for metrics.
  name: signalaf-com Metrics API
  slug: signalaf-com-metrics-api
- baseURL: https://signalaf.com/api/v1
  baseurl_source: declared
  description: The operators API from signalaf-com — 2 operation(s) for operators.
  name: signalaf-com Operators API
  slug: signalaf-com-operators-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/signalaf-com/agentic-access/signalaf-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/signalaf-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/signalaf-com/rate-limits/signalaf-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/signalaf-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/signalaf-com/rules/signalaf-com-rules.yml
  title: ''
  type: Spectral
  url: rules/signalaf-com-rules.yml
- group: design
  href: https://artifacts.apis.io/signalaf-com/json-ld/signalaf-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/signalaf-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/signalaf-com/vocabulary/signalaf-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/signalaf-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/signalaf-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/signalaf-com/data-model/signalaf-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/signalaf-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/signalaf-com/authentication/signalaf-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/signalaf-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/signalaf-com/scopes/signalaf-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/signalaf-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/signalaf-com/errors/signalaf-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/signalaf-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/signalaf-com/conformance/signalaf-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/signalaf-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/signalaf-com/llms/signalaf-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/signalaf-com-llms.txt
- group: other
  href: https://artifacts.apis.io/signalaf-com/a2a/signalaf-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/signalaf-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/signalaf-com/mcp/signalaf-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/signalaf-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/signalaf-com/mcp/signalaf-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/signalaf-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/signalaf-com/well-known/signalaf-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/signalaf-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/signalaf-com/hosts/signalaf-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/signalaf-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/signalaf-com/vendors/signalaf-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/signalaf-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/signalaf-com/packages/signalaf-com-packages.yml
  title: ''
  type: SDKs
  url: packages/signalaf-com-packages.yml
- group: build
  href: https://artifacts.apis.io/signalaf-com/packages/signalaf-com-packages.yml
  title: ''
  type: Packages
  url: packages/signalaf-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://signalaf.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://signalaf.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://signalaf.com/pricing
- group: start
  title: ''
  type: Login
  url: https://signalaf.com/login
- group: auth
  href: https://artifacts.apis.io/signalaf-com/security/signalaf-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/signalaf-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://signalaf.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://signalaf.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://signalaf.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://signalaf.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://signalaf.com/auth.md
- group: operate
  title: ''
  type: Support
  url: https://signalaf.com/contact
- group: company
  title: ''
  type: Blog
  url: https://signalaf.com/blog
created: '2026-10-30'
description: SignalAF (legal name Ello Cello LLC) provides the SigRank AI leaderboard platform that ranks AI operators by Yield, a metric combining cache reads, output and input efficiency. The service offers a public REST API with OpenAPI 3.0 specification, authentication via Supabase OAuth and API keys, rate‑limit policies, error handling with RFC 9457 problem details, versioned endpoints under /api/v1, and extensive developer documentation hosted at https://signalaf.com/developers. The organization is based in Buffalo, NY, and maintains open‑source SDKs and tools.
image: https://signalaf.com/logo.png
json_schemas:
- name: HallOfSignal
  property_count: 2
  slug: signalaf-com-hall-of-signal
- name: Leaderboard
  property_count: 1
  slug: signalaf-com-leaderboard
- name: Operator
  property_count: 6
  slug: signalaf-com-operator
jsonld:
- class_count: 3
  name: Signalaf Com Context
  property_count: 9
  slug: signalaf-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at signalaf.com.
  name: signalaf-com MCP Server
  slug: signalaf-com-mcp-yml
modified: '2026-10-30'
name: signalaf-com
nav: Providers
network: true
overview: 'signalaf-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Hall API, Leaderboard API, Metrics API, and 1 more. Tagged areas include AI, Analytics, Leaderboard, OpenAPI, and PublicAPI.


  The signalaf-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  signalaf-com''s developer surface includes authentication, pricing, documentation, API reference, getting-started guide, support, engineering blog, and 25 more developer resources.'
plans:
- name: Signalaf Com Plans Pricing
  plan_count: 0
  slug: signalaf-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Signalaf Com Rate Limits
  slug: signalaf-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: signalaf-com API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: signalaf-com-rules
scopes:
- name: Signalaf Com Scopes
  scope_count: 4
  slug: signalaf-com-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 64.8
    catalog_earned_first_party: 8.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 55.4
    developer_ergonomics: 70.7
    discoverability: 65.0
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Signalaf Com Authentication
  slug: signalaf-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Signalaf Com Domain Security
  slug: signalaf-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: get-hall-of-signal
  slug: signalaf-com-get-hall-of-signal
- name: get-leaderboard
  slug: signalaf-com-get-leaderboard
- name: get-metrics
  slug: signalaf-com-get-metrics
- name: get-operator
  slug: signalaf-com-get-operator
slug: signalaf-com
tags:
- AI
- Analytics
- Leaderboard
- OpenAPI
- PublicAPI
website: https://signalaf.com/
---
