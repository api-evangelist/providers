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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Resolvedmarkets Com Agentic Access
  operation_count: 49
  slug: resolvedmarkets-com-agentic-access
  summary_line: 49 operations · 12 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.resolvedmarkets.com
  baseurl_source: declared
  description: API key management and tier information (Clerk session required).
  name: resolvedmarkets-com Account API
  slug: resolvedmarkets-com-account-api
- baseURL: https://api.resolvedmarkets.com
  baseurl_source: declared
  description: Owner-only chat operator endpoints.
  name: resolvedmarkets-com Admin API
  slug: resolvedmarkets-com-admin-api
- baseURL: https://api.resolvedmarkets.com
  baseurl_source: declared
  description: Event-driven backtesting engine and natural-language strategy agent. Pro / Enterprise only.
  name: resolvedmarkets-com Backtest API
  slug: resolvedmarkets-com-backtest-api
- baseURL: https://api.resolvedmarkets.com
  baseurl_source: declared
  description: Hyperliquid perpetual futures L2 book.
  name: resolvedmarkets-com Exchange API
  slug: resolvedmarkets-com-exchange-api
- baseURL: https://api.resolvedmarkets.com
  baseurl_source: declared
  description: Polymarket prediction market data.
  name: resolvedmarkets-com Markets API
  slug: resolvedmarkets-com-markets-api
- baseURL: https://api.resolvedmarkets.com
  baseurl_source: declared
  description: Subscription status, credit-pack pricing, and checkout flows.
  name: resolvedmarkets-com Payments API
  slug: resolvedmarkets-com-payments-api
- baseURL: https://api.resolvedmarkets.com
  baseurl_source: declared
  description: No authentication required.
  name: resolvedmarkets-com Public API
  slug: resolvedmarkets-com-public-api
- baseURL: https://api.resolvedmarkets.com
  baseurl_source: declared
  description: Point-in-time and time-series orderbook snapshots.
  name: resolvedmarkets-com Snapshots API
  slug: resolvedmarkets-com-snapshots-api
- baseURL: https://api.resolvedmarkets.com
  baseurl_source: declared
  description: Saved strategy specs.
  name: resolvedmarkets-com Strategies API
  slug: resolvedmarkets-com-strategies-api
- baseURL: https://api.resolvedmarkets.com
  baseurl_source: declared
  description: Platform-wide stats and diagnostics.
  name: resolvedmarkets-com System API
  slug: resolvedmarkets-com-system-api
- baseURL: https://api.resolvedmarkets.com
  baseurl_source: declared
  description: Executed-trade tape (last_trade_price fills), joinable to snapshots.
  name: resolvedmarkets-com Trades API
  slug: resolvedmarkets-com-trades-api
- baseURL: https://api.resolvedmarkets.com
  baseurl_source: declared
  description: The Wallets API from resolvedmarkets-com — 1 operation(s) for wallets.
  name: resolvedmarkets-com Wallets API
  slug: resolvedmarkets-com-wallets-api
- baseURL: https://api.resolvedmarkets.com
  baseurl_source: declared
  description: Inbound webhooks from Stripe, NOWPayments, and Clerk.
  name: resolvedmarkets-com Webhooks API
  slug: resolvedmarkets-com-webhooks-api
artifact_total: 28
common:
- group: agent
  href: https://artifacts.apis.io/resolvedmarkets-com/agentic-access/resolvedmarkets-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/resolvedmarkets-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/resolvedmarkets-com/rate-limits/resolvedmarkets-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/resolvedmarkets-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/resolvedmarkets-com/plans/resolvedmarkets-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/resolvedmarkets-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/resolvedmarkets-com/rules/resolvedmarkets-com-rules.yml
  title: ''
  type: Spectral
  url: rules/resolvedmarkets-com-rules.yml
- group: design
  href: https://artifacts.apis.io/resolvedmarkets-com/json-ld/resolvedmarkets-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/resolvedmarkets-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/resolvedmarkets-com/vocabulary/resolvedmarkets-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/resolvedmarkets-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/resolvedmarkets-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/resolvedmarkets-com/data-model/resolvedmarkets-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/resolvedmarkets-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/resolvedmarkets-com/cli/resolvedmarkets-com-cli.yml
  title: ''
  type: CLI
  url: cli/resolvedmarkets-com-cli.yml
- group: design
  href: https://artifacts.apis.io/resolvedmarkets-com/conventions/resolvedmarkets-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/resolvedmarkets-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/resolvedmarkets-com/authentication/resolvedmarkets-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/resolvedmarkets-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/resolvedmarkets-com/errors/resolvedmarkets-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/resolvedmarkets-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/resolvedmarkets-com/conformance/resolvedmarkets-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/resolvedmarkets-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/resolvedmarkets-com/llms/resolvedmarkets-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/resolvedmarkets-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/resolvedmarkets-com/well-known/resolvedmarkets-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/resolvedmarkets-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/resolvedmarkets-com/hosts/resolvedmarkets-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/resolvedmarkets-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/resolvedmarkets-com/vendors/resolvedmarkets-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/resolvedmarkets-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://resolvedmarkets.com/docs/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.resolvedmarkets.com`
- group: auth
  href: https://artifacts.apis.io/resolvedmarkets-com/security/resolvedmarkets-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/resolvedmarkets-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://resolvedmarkets.com/
- group: docs
  title: ''
  type: Documentation
  url: https://resolvedmarkets.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://resolvedmarkets.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://resolvedmarkets.com/docs
- group: company
  title: ''
  type: Blog
  url: https://resolvedmarkets.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/resolvedmarkets
- group: commercial
  title: ''
  type: Pricing
  url: https://resolvedmarkets.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://resolvedmarkets.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://resolvedmarkets.com/privacy
created: '2026-10-31'
description: Resolved Markets provides an independent high‑frequency data platform delivering over 4.2 billion historical order‑book snapshots from Polymarket prediction markets and Hyperliquid perpetual futures. The service offers REST, WebSocket, and MCP APIs plus a backtester, with a free tier and paid plans for deeper access.
image: https://resolvedmarkets.com/images/green.png
json_schemas:
- name: BacktestRunStatus
  property_count: 9
  slug: resolvedmarkets-com-backtest-run-status
- name: MarketAtTime
  property_count: 7
  slug: resolvedmarkets-com-market-at-time
- name: Market
  property_count: 14
  slug: resolvedmarkets-com-market
- name: RecentMarketRow
  property_count: 12
  slug: resolvedmarkets-com-recent-market-row
- name: Snapshot
  property_count: 19
  slug: resolvedmarkets-com-snapshot
- name: Trade
  property_count: 9
  slug: resolvedmarkets-com-trade
jsonld:
- class_count: 11
  name: Resolvedmarkets Com Context
  property_count: 62
  slug: resolvedmarkets-com-context
layout: provider
modified: '2026-10-31'
name: resolvedmarkets-com
nav: Providers
network: true
overview: 'resolvedmarkets-com publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Admin API, Backtest API, and 10 more. Tagged areas include Data, Finance, Prediction Markets, and Backtesting.


  The resolvedmarkets-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  resolvedmarkets-com''s developer surface includes CLI, authentication, changelog, documentation, API reference, getting-started guide, engineering blog, and 22 more developer resources.'
plans:
- name: Resolvedmarkets Com Plans Pricing
  plan_count: 4
  slug: resolvedmarkets-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Resolvedmarkets Com Rate Limits
  slug: resolvedmarkets-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: resolvedmarkets-com API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 4
  slug: resolvedmarkets-com-rules
scopes:
- name: Resolvedmarkets Com Scopes
  scope_count: 0
  slug: resolvedmarkets-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 33
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 61.3
    developer_ergonomics: 45.7
    discoverability: 57.1
    operational_transparency: 42.1
  previous_composite: 61.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
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
screenshot: https://apis.io/screenshots/resolvedmarkets-com/resolvedmarkets-com-2026-11-03T142215.png
security:
- kind: authentication
  name: Resolvedmarkets Com Authentication
  slug: resolvedmarkets-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Resolvedmarkets Com Domain Security
  slug: resolvedmarkets-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: get-data-skill
  slug: resolvedmarkets-com-get-data-skill
slug: resolvedmarkets-com
tags:
- Data
- Finance
- Prediction Markets
- Backtesting
website: https://resolvedmarkets.com/
---
