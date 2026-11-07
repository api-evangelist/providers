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
  band: agent-native
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
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Tickerbot Io Agentic Access
  operation_count: 41
  slug: tickerbot-io-agentic-access
  summary_line: 41 operations · 19 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.tickerbot.io
  baseurl_source: declared
  description: The Bars API from tickerbot-io — 1 operation(s) for bars.
  name: tickerbot-io Bars API
  slug: tickerbot-io-bars-api
- baseURL: https://api.tickerbot.io
  baseurl_source: declared
  description: Phone registrations backing the mobile_push webhook channel.
  name: tickerbot-io Devices API
  slug: tickerbot-io-devices-api
- baseURL: https://api.tickerbot.io
  baseurl_source: declared
  description: The ETF API from tickerbot-io — 2 operation(s) for etf.
  name: tickerbot-io ETF API
  slug: tickerbot-io-etf-api
- baseURL: https://api.tickerbot.io
  baseurl_source: declared
  description: One cross-ticker timeline over dividends, splits, insider transactions, and analyst actions, plus fire-on-ingest webhooks.
  name: tickerbot-io Events API
  slug: tickerbot-io-events-api
- baseURL: https://api.tickerbot.io
  baseurl_source: declared
  description: Health and version probes.
  name: tickerbot-io Meta API
  slug: tickerbot-io-meta-api
- baseURL: https://api.tickerbot.io
  baseurl_source: declared
  description: Article-level news with sentiment, queryable through the same SQL grammar as /scan.
  name: tickerbot-io News API
  slug: tickerbot-io-news-api
- baseURL: https://api.tickerbot.io
  baseurl_source: declared
  description: Universe-wide SQL queries, live and at any past moment, with resource-level subscribe.
  name: tickerbot-io Scan API
  slug: tickerbot-io-scan-api
- baseURL: https://api.tickerbot.io
  baseurl_source: declared
  description: The Series API from tickerbot-io — 1 operation(s) for series.
  name: tickerbot-io Series API
  slug: tickerbot-io-series-api
- baseURL: https://api.tickerbot.io
  baseurl_source: declared
  description: Unified catalog, live + as-of match sets, per-ticker time series, custom-signal CRUD (every plan), and resource-level subscribe.
  name: tickerbot-io Signals API
  slug: tickerbot-io-signals-api
- baseURL: https://api.tickerbot.io
  baseurl_source: declared
  description: Current state, point-in-time snapshot (?asof=), corporate-event log, and resource-level subscribe.
  name: tickerbot-io Tickers API
  slug: tickerbot-io-tickers-api
- baseURL: https://api.tickerbot.io
  baseurl_source: declared
  description: Named ticker lists — customer-defined and system-managed (top_10, top_100).
  name: tickerbot-io Universes API
  slug: tickerbot-io-universes-api
- baseURL: https://api.tickerbot.io
  baseurl_source: declared
  description: Registry for subscriptions created via resource-level subscribe endpoints. HMAC-signed delivery with retry semantics.
  name: tickerbot-io Webhooks API
  slug: tickerbot-io-webhooks-api
- baseURL: https://api.tickerbot.io
  baseurl_source: declared
  description: The Websockets API from tickerbot-io — 1 operation(s) for websockets.
  name: tickerbot-io WebSockets API
  slug: tickerbot-io-websockets-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/tickerbot-io/agentic-access/tickerbot-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tickerbot-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/tickerbot-io/rate-limits/tickerbot-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tickerbot-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tickerbot-io/plans/tickerbot-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tickerbot-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tickerbot-io/rules/tickerbot-io-rules.yml
  title: ''
  type: Spectral
  url: rules/tickerbot-io-rules.yml
- group: design
  href: https://artifacts.apis.io/tickerbot-io/json-ld/tickerbot-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tickerbot-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/tickerbot-io/vocabulary/tickerbot-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tickerbot-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tickerbot-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tickerbot-io/data-model/tickerbot-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tickerbot-io-data-model.yml
- group: build
  href: https://artifacts.apis.io/tickerbot-io/cli/tickerbot-io-cli.yml
  title: ''
  type: CLI
  url: cli/tickerbot-io-cli.yml
- group: design
  href: https://artifacts.apis.io/tickerbot-io/conventions/tickerbot-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/tickerbot-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/tickerbot-io/conventions/tickerbot-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tickerbot-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/tickerbot-io/authentication/tickerbot-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tickerbot-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/tickerbot-io/lifecycle/tickerbot-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tickerbot-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tickerbot-io/errors/tickerbot-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tickerbot-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tickerbot-io/conformance/tickerbot-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tickerbot-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tickerbot-io/llms/tickerbot-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tickerbot-io-llms.txt
- group: build
  href: https://artifacts.apis.io/tickerbot-io/mcp/tickerbot-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tickerbot-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/tickerbot-io/mcp/tickerbot-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tickerbot-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tickerbot-io/well-known/tickerbot-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tickerbot-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/tickerbot-io/hosts/tickerbot-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tickerbot-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/tickerbot-io/vendors/tickerbot-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tickerbot-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/tickerbot-io/packages/tickerbot-io-packages.yml
  title: ''
  type: SDKs
  url: packages/tickerbot-io-packages.yml
- group: build
  href: https://artifacts.apis.io/tickerbot-io/packages/tickerbot-io-packages.yml
  title: ''
  type: Packages
  url: packages/tickerbot-io-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://tickerbot.io/status/
- group: start
  title: ''
  type: SignUp
  url: https://tickerbot.io/signup/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.tickerbot.io</code
- group: docs
  title: ''
  type: APIReference
  url: https://tickerbot.io/docs/changelog/
- group: auth
  href: https://artifacts.apis.io/tickerbot-io/security/tickerbot-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tickerbot-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tickerbot.io/
- group: docs
  title: ''
  type: Documentation
  url: https://tickerbot.io/docs/
- group: operate
  title: ''
  type: Support
  url: https://tickerbot.io/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://tickerbot.io/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tickerbot.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tickerbot.io/privacy/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://tickerbot.io/openapi.yaml
  - status: 401
    url: https://api.tickerbot.io/mcp
  - status: 200
    url: https://tickerbot.io/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: 'Tickerbot is the stock market API designed for agents. We serve real-time and historical market data as one queryable table. You and your agents can ask it anything, without building anything custom. Every ticker is a row. Every data point is a column. 23,000+ tickers, covering US stocks and ETFs, FX, crypto, rates and metals. 452+ columns, covering raw data, calculations and conditions: price, volume, price action, technicals, fundamentals, events, profile, analyst ratings and news. Refreshed every minute, historized back to 2003. Free plan: 10,000 calls a month, no card required.'
image: https://tickerbot.io/opengraph-image?30d0ca57b71fec05
json_schemas:
- name: TickerRow
  property_count: 461
  slug: tickerbot-io-ticker-row
jsonld:
- class_count: 1
  name: Tickerbot Io Context
  property_count: 459
  slug: tickerbot-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.tickerbot.io.
  name: tickerbot-io MCP Server
  slug: tickerbot-io-mcp-yml
modified: '2026-10-31'
name: tickerbot-io
nav: Providers
network: true
overview: 'tickerbot-io publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bars API, Devices API, ETF API, and 10 more. Tagged areas include Company, Stock Market, Real-Time Data, Historical Data, and Financial-Agents.


  The tickerbot-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tickerbot-io''s developer surface includes CLI, authentication, signup flow, API reference, documentation, support, pricing, and 27 more developer resources.'
plans:
- name: Tickerbot Io Plans Pricing
  plan_count: 4
  slug: tickerbot-io-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Tickerbot Io Rate Limits
  slug: tickerbot-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: tickerbot-io API Rules
  rule_count: 19
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 5
  slug: tickerbot-io-rules
scopes:
- name: Tickerbot Io Scopes
  scope_count: 0
  slug: tickerbot-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 80.2
    catalog_earned_first_party: 24.0
    catalog_gap: 34.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 60.9
    developer_ergonomics: 48.1
    discoverability: 65.0
    operational_transparency: 39.5
  previous_composite: 63.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
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
security:
- kind: authentication
  name: Tickerbot Io Authentication
  slug: tickerbot-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tickerbot Io Domain Security
  slug: tickerbot-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: tickerbot
  slug: tickerbot-io-tickerbot
slug: tickerbot-io
tags:
- Company
- Stock Market
- Real-Time Data
- Historical Data
- Financial-Agents
website: https://tickerbot.io/
---
