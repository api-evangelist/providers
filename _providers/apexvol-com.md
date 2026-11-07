---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Apexvol Com Agentic Access
  operation_count: 64
  slug: apexvol-com-agentic-access
  summary_line: 64 operations · 9 acting
api_count: 1
apis:
- baseURL: https://apexvol.com
  baseurl_source: declared
  description: The Account and index API from ApexVol — 2 operation(s) for account and index.
  name: ApexVol Account and index API
  slug: apexvol-com-account-and-index-api
- baseURL: https://apexvol.com
  baseurl_source: declared
  description: The Earnings and expected move API from ApexVol — 9 operation(s) for earnings and expected move.
  name: ApexVol Earnings and expected move API
  slug: apexvol-com-earnings-and-expected-move-api
- baseURL: https://apexvol.com
  baseurl_source: declared
  description: The Events and calendars API from ApexVol — 3 operation(s) for events and calendars.
  name: ApexVol Events and calendars API
  slug: apexvol-com-events-and-calendars-api
- baseURL: https://apexvol.com
  baseurl_source: declared
  description: The Gamma exposure API from ApexVol — 7 operation(s) for gamma exposure.
  name: ApexVol Gamma exposure API
  slug: apexvol-com-gamma-exposure-api
- baseURL: https://apexvol.com
  baseurl_source: declared
  description: The Implied volatility API from ApexVol — 12 operation(s) for implied volatility.
  name: ApexVol Implied volatility API
  slug: apexvol-com-implied-volatility-api
- baseURL: https://apexvol.com
  baseurl_source: declared
  description: The Options chain API from ApexVol — 6 operation(s) for options chain.
  name: ApexVol Options chain API
  slug: apexvol-com-options-chain-api
- baseURL: https://apexvol.com
  baseurl_source: declared
  description: The Options flow API from ApexVol — 2 operation(s) for options flow.
  name: ApexVol Options flow API
  slug: apexvol-com-options-flow-api
- baseURL: https://apexvol.com
  baseurl_source: declared
  description: The Options Greeks API from ApexVol — 3 operation(s) for options greeks.
  name: ApexVol Options Greeks API
  slug: apexvol-com-options-greeks-api
- baseURL: https://apexvol.com
  baseurl_source: declared
  description: The Portfolio risk API from ApexVol — 4 operation(s) for portfolio risk.
  name: ApexVol Portfolio risk API
  slug: apexvol-com-portfolio-risk-api
- baseURL: https://apexvol.com
  baseurl_source: declared
  description: The Screeners API from ApexVol — 4 operation(s) for screeners.
  name: ApexVol Screeners API
  slug: apexvol-com-screeners-api
- baseURL: https://apexvol.com
  baseurl_source: declared
  description: The Stock analytics API from ApexVol — 7 operation(s) for stock analytics.
  name: ApexVol Stock analytics API
  slug: apexvol-com-stock-analytics-api
- baseURL: https://apexvol.com
  baseurl_source: declared
  description: The Strategies API from ApexVol — 5 operation(s) for strategies.
  name: ApexVol Strategies API
  slug: apexvol-com-strategies-api
artifact_total: 28
common:
- group: agent
  href: https://artifacts.apis.io/apexvol-com/agentic-access/apexvol-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apexvol-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/apexvol-com/rate-limits/apexvol-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apexvol-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/apexvol-com/plans/apexvol-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apexvol-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apexvol-com/rules/apexvol-com-rules.yml
  title: ''
  type: Spectral
  url: rules/apexvol-com-rules.yml
- group: design
  href: https://artifacts.apis.io/apexvol-com/json-ld/apexvol-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apexvol-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/apexvol-com/vocabulary/apexvol-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apexvol-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/apexvol-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apexvol-com/data-model/apexvol-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apexvol-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/apexvol-com/conventions/apexvol-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apexvol-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/apexvol-com/authentication/apexvol-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apexvol-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/apexvol-com/errors/apexvol-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apexvol-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apexvol-com/conformance/apexvol-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apexvol-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apexvol-com/llms/apexvol-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apexvol-com-llms.txt
- group: build
  href: https://artifacts.apis.io/apexvol-com/mcp/apexvol-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/apexvol-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/apexvol-com/mcp/apexvol-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apexvol-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/apexvol-com/well-known/apexvol-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apexvol-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/apexvol-com/hosts/apexvol-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apexvol-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/apexvol-com/vendors/apexvol-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apexvol-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apexvol.com/terms_and_conditions
- group: start
  title: ''
  type: Login
  url: https://apexvol.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apexvol.com/developers/errors
- group: operate
  title: ''
  type: ChangeLog
  url: https://apexvol.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://apexvol.com/learn/claude-options-data-mcp
- group: auth
  href: https://artifacts.apis.io/apexvol-com/security/apexvol-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apexvol-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apexvol.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apexvol.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://apexvol.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://apexvol.com/blog
- group: operate
  title: ''
  type: Support
  url: https://apexvol.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apexvol.com/privacy-policy
created: '2026-11-01'
description: The ApexVol Terminal offers 50 options‑analytics modules, delivering live volatility surfaces, dealer GEX, Greeks, chains and a screener on a single professional screen. We built ApexVol because professional‑quality options data should not be locked behind a Bloomberg terminal; every trader deserves the same analytical edge. A 7‑day free trial is available.
image: https://apexvol.com/static/img/og-terminal.jpg
json_schemas:
- name: GetBatchGexResponse
  property_count: 7
  slug: apexvol-com-get-batch-gex-response
- name: GetCrossIndexGexResponse
  property_count: 2
  slug: apexvol-com-get-cross-index-gex-response
- name: GetEarningsVerdictByTickerResponse
  property_count: 9
  slug: apexvol-com-get-earnings-verdict-by-ticker-response
- name: GetGreeksExposureByTickerResponse
  property_count: 10
  slug: apexvol-com-get-greeks-exposure-by-ticker-response
- name: GetSeasonalityByTickerResponse
  property_count: 8
  slug: apexvol-com-get-seasonality-by-ticker-response
- name: GetZeroDteByTickerResponse
  property_count: 18
  slug: apexvol-com-get-zero-dte-by-ticker-response
jsonld:
- class_count: 64
  name: Apexvol Com Context
  property_count: 440
  slug: apexvol-com-context
layout: provider
mcp_servers:
- description: ''
  name: ApexVol MCP Server
  slug: apexvol-com-mcp-yml
modified: '2026-11-01'
name: ApexVol
nav: Providers
network: true
overview: 'ApexVol publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account and index API, Earnings and expected move API, Events and calendars API, and 9 more. Tagged areas include Options, Analytics, Trading, Finance, and Terminal.


  The ApexVol catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ApexVol''s developer surface includes authentication, changelog, getting-started guide, documentation, pricing, engineering blog, support, and 23 more developer resources.'
plans:
- name: Apexvol Com Plans Pricing
  plan_count: 3
  slug: apexvol-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Apexvol Com Rate Limits
  slug: apexvol-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: ApexVol API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: apexvol-com-rules
scopes:
- name: Apexvol Com Scopes
  scope_count: 0
  slug: apexvol-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 32
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 63.5
    developer_ergonomics: 37.4
    discoverability: 65.0
    operational_transparency: 39.5
  previous_composite: 60.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
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
  name: Apexvol Com Authentication
  slug: apexvol-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apexvol Com Domain Security
  slug: apexvol-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: options-chain
  slug: apexvol-com-options-chain-skill
slug: apexvol-com
tags:
- Options
- Analytics
- Trading
- Finance
- Terminal
website: https://apexvol.com/
---
