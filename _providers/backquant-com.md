---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST and WebSocket API for real-time and historical crypto gamma exposure, dealer positioning, options flow, and IV surfaces. BTC, ETH, SOL and HYPE across 10 venues.
  name: BackQuant API v2
  slug: backquant-api-v2
- description: Options + gamma-exposure focused public API. Built on the same data the
  name: BackQuant API v2 API
  slug: backquant-api-v2-api
artifact_total: 17
common:
- group: operate
  href: https://artifacts.apis.io/backquant-com/rate-limits/backquant-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/backquant-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/backquant-com/rules/backquant-com-rules.yml
  title: ''
  type: Spectral
  url: rules/backquant-com-rules.yml
- group: design
  href: https://artifacts.apis.io/backquant-com/json-ld/backquant-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/backquant-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/backquant-com/vocabulary/backquant-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/backquant-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/backquant-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/backquant-com/data-model/backquant-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/backquant-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/backquant-com/authentication/backquant-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/backquant-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/backquant-com/errors/backquant-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/backquant-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/backquant-com/conformance/backquant-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/backquant-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/backquant-com/llms/backquant-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/backquant-com-llms.txt
- group: other
  href: https://artifacts.apis.io/backquant-com/a2a/backquant-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/backquant-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/backquant-com/mcp/backquant-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/backquant-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/backquant-com/well-known/backquant-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/backquant-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/backquant-com/hosts/backquant-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backquant-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/backquant-com/vendors/backquant-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backquant-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.backquant.com/signup?redirect=terminal-equities
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.backquant.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.backquant.com/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/backquant
- group: auth
  href: https://artifacts.apis.io/backquant-com/security/backquant-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backquant-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://backquant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.backquant.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.backquant.com/gex-api
- group: company
  title: ''
  type: Blog
  url: https://www.backquant.com/articles
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.backquant.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.backquant.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.backquant.com/contact
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.backquant.com/documentation
created: '2026-11-02'
description: BackQuant provides live gamma exposure, dealer positioning, and options flow analytics for equities and crypto, featuring a full charting engine with order flow and 24/7 TradFi charts across SPX, NDX, BTC, ETH, SOL, and HYPE.
image: https://www.backquant.com/biglogowhite.png
json_schemas:
- name: ExpectedMoveResponse
  property_count: 3
  slug: backquant-com-expected-move-response
- name: ExpirySummaryResponse
  property_count: 3
  slug: backquant-com-expiry-summary-response
- name: GexStrikeProfileResponse
  property_count: 3
  slug: backquant-com-gex-strike-profile-response
- name: IvTermStructureResponse
  property_count: 3
  slug: backquant-com-iv-term-structure-response
- name: MultiGexLevelsResponse
  property_count: 3
  slug: backquant-com-multi-gex-levels-response
- name: ProbabilityDensityResponse
  property_count: 3
  slug: backquant-com-probability-density-response
jsonld:
- class_count: 59
  name: Backquant Com Context
  property_count: 194
  slug: backquant-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at status.backquant.com.
  name: BackQuant MCP Server
  slug: backquant-com-mcp-yml
modified: '2026-11-02'
name: BackQuant
nav: Providers
network: true
overview: 'BackQuant publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API v2 API, and 1 more. Tagged areas include Finance, Trading, Options, Cryptocurrency, and Analytics.


  The BackQuant catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BackQuant''s developer surface includes authentication, signup flow, changelog, getting-started guide, documentation, API reference, engineering blog, and 21 more developer resources.'
plans:
- name: Backquant Com Plans Pricing
  plan_count: 0
  slug: backquant-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 2
  name: Backquant Com Rate Limits
  slug: backquant-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: BackQuant API Rules
  rule_count: 55
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 11
  slug: backquant-com-rules
scopes:
- name: Backquant Com Scopes
  scope_count: 0
  slug: backquant-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 41.0
    discoverability: 56.7
    operational_transparency: 31.6
  previous_composite: 48.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Backquant Com Authentication
  slug: backquant-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Backquant Com Domain Security
  slug: backquant-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: gex-api
  slug: backquant-com-gex-api
slug: backquant-com
tags:
- Finance
- Trading
- Options
- Cryptocurrency
- Analytics
website: https://backquant.com/
---
