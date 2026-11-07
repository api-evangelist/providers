---
access_model:
  confidence: high
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
  - rate-limits
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Arkolith Com Agentic Access
  operation_count: 1
  slug: arkolith-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://arkolith.com/api/v1
  baseurl_source: declared
  description: The Funds API from Arkolith — 1 operation(s) for funds.
  name: Arkolith Funds API
  slug: arkolith-com-funds-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/arkolith-com/agentic-access/arkolith-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/arkolith-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/arkolith-com/rate-limits/arkolith-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/arkolith-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/arkolith-com/plans/arkolith-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arkolith-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/arkolith-com/rules/arkolith-com-rules.yml
  title: ''
  type: Spectral
  url: rules/arkolith-com-rules.yml
- group: design
  href: https://artifacts.apis.io/arkolith-com/json-ld/arkolith-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arkolith-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/arkolith-com/vocabulary/arkolith-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arkolith-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/arkolith-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/arkolith-com/data-model/arkolith-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arkolith-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/arkolith-com/security/arkolith-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/arkolith-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arkolith-com/authentication/arkolith-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arkolith-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/arkolith-com/errors/arkolith-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arkolith-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/arkolith-com/conformance/arkolith-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arkolith-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arkolith-com/llms/arkolith-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arkolith-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/arkolith-com/mcp/arkolith-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arkolith-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/arkolith-com/well-known/arkolith-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arkolith-com-security.txt
- group: agent
  href: https://artifacts.apis.io/arkolith-com/well-known/arkolith-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arkolith-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/arkolith-com/hosts/arkolith-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arkolith-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/arkolith-com/vendors/arkolith-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arkolith-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://arkolith.com/news
- group: start
  title: ''
  type: GettingStarted
  url: https://arkolith.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/arkolith-com/security/arkolith-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arkolith-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arkolith-com/security/arkolith-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arkolith-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arkolith.com/
- group: docs
  title: ''
  type: Documentation
  url: https://arkolith.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://arkolith.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://arkolith.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arkolith.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arkolith.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://arkolith.com/auth/signup
- group: operate
  title: ''
  type: Support
  url: https://arkolith.com/contact
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://arkolith.com/openapi.json
  - status: 401
    url: https://arkolith.com/api/mcp
  - status: 200
    url: https://arkolith.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Arkolith provides real-time institutional market-data APIs and an MCP server that surface SEC filings, 13F holdings, Form 4 insider trades, and derived signals. Users can start with a $1 trial for 300 research credits over 3 days, then subscribe for $29/mo. The platform offers searchable data, dashboards, and integration guides for AI agents, enabling agents to query market data with provenance.
image: https://arkolith.com/arkolith-mark-strata.svg
json_schemas:
- name: FundList
  property_count: 0
  slug: arkolith-com-fund-list
jsonld:
- class_count: 2
  name: Arkolith Com Context
  property_count: 19
  slug: arkolith-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at arkolith.com.
  name: Arkolith MCP Server
  slug: arkolith-com-mcp-yml
modified: '2026-11-01'
name: Arkolith
nav: Providers
network: true
overview: 'Arkolith publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Funds API. Tagged areas include Finance, Market Data, SEC, and MCP.


  The Arkolith catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arkolith''s developer surface includes authentication, getting-started guide, documentation, pricing, engineering blog, signup flow, support, and 23 more developer resources.'
plans:
- name: Arkolith Com Plans Pricing
  plan_count: 5
  slug: arkolith-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Arkolith Com Rate Limits
  slug: arkolith-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: Arkolith API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: arkolith-com-rules
scopes:
- name: Arkolith Com Scopes
  scope_count: 0
  slug: arkolith-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 32
    catalog_earned: 75.2
    catalog_earned_first_party: 24.0
    catalog_gap: 39.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 54.4
    developer_ergonomics: 32.6
    discoverability: 57.5
    operational_transparency: 42.1
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 39.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arkolith Com Authentication
  slug: arkolith-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Arkolith Com Domain Security
  slug: arkolith-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arkolith Com Vulnerability Disclosure
  slug: arkolith-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: capital-change-brief
  slug: arkolith-com-capital-change-brief
slug: arkolith-com
tags:
- Finance
- Market Data
- SEC
- MCP
website: https://arkolith.com/
---
