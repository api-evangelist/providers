---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 51
  human_in_the_loop: 7
  name: Fxapis Com Agentic Access
  operation_count: 100
  slug: fxapis-com-agentic-access
  summary_line: 100 operations · 51 acting · 7 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: Connecting MT5 accounts and reading their state.
  name: fxapis-com Accounts API
  slug: fxapis-com-accounts-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: 'TradingView alert hooks: a secret URL that turns TradingView alerts into orders on your accounts, with no EA and no VPS. The URL is returned once, when a hook is created or rotated.'
  name: fxapis-com Alerts API
  slug: fxapis-com-alerts-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: Issuing, renaming, re-scoping and revoking this workspace's ordinary keys. Needs an admin key (`fx_admin_…`) — or a signed-in owner or admin in the console; ordinary keys are refused. A key's secret i
  name: fxapis-com API keys API
  slug: fxapis-com-api-keys-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: Plans, usage, what the month would cost, invoices, and paying for a plan.
  name: fxapis-com Billing API
  slug: fxapis-com-billing-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: 'Managed copy trading: mark an always-on account as a strategy, subscribe other accounts in this workspace, and fxapis repeats the master''s opens, closes, partial closes and stop moves on every followe'
  name: fxapis-com Copy trading API
  slug: fxapis-com-copy-trading-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: 'The event log: every event in this workspace, exactly as webhooks deliver it, kept 7, 30 or 90 days by plan. To catch up after downtime, ask for everything `after` the last event you read from this li'
  name: fxapis-com Events API
  slug: fxapis-com-events-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: Liveness and readiness. No key required.
  name: fxapis-com Health API
  slug: fxapis-com-health-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: 'The durable record: every order, every deal the broker recorded, and what it returned. Includes deals no order of yours caused.'
  name: fxapis-com History API
  slug: fxapis-com-history-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: 'Markets named once — `XAUUSD`, `US30`, `BTCUSD` — and how each maps onto an account''s broker symbols. An order can name an `instrument` instead of a `symbol`, and trades that account''s own symbol for '
  name: fxapis-com Instruments API
  slug: fxapis-com-instruments-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: Bringing an account online, taking it offline, and changing how it stays connected.
  name: fxapis-com Lifecycle API
  slug: fxapis-com-lifecycle-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: Prices from each account's own broker, read live from its terminal. Each broker quotes differently, and these are the prices that account trades at.
  name: fxapis-com Market data API
  slug: fxapis-com-market-data-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: Who is in this workspace, who has been invited, and what each may do. **Console only:** managed by a signed-in owner or admin in the fxapis console. Every API key and admin key is refused, so these op
  name: fxapis-com Members API
  slug: fxapis-com-members-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: Placing orders and reading positions. The endpoints that move money.
  name: fxapis-com Trading API
  slug: fxapis-com-trading-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: 'Multi-account orders: one trade placed on many accounts at once, with a result for each account. For signals that should reach every follower at the same moment.'
  name: fxapis-com Waves API
  slug: fxapis-com-waves-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: 'Event webhooks: a signed POST to your HTTPS endpoint when an order fills or is rejected, a position opens or closes, an account changes state, or a multi-account order finishes. Retried over about 44.'
  name: fxapis-com Webhooks API
  slug: fxapis-com-webhooks-api
- baseURL: https://api.fxapis.com
  baseurl_source: declared
  description: 'The workspace a credential belongs to: its plan, and whether trading is switched off.'
  name: fxapis-com Workspace API
  slug: fxapis-com-workspace-api
artifact_total: 22
asyncapis:
- description: ''
  name: Fxapis Com Webhooks
  slug: fxapis-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/fxapis-com/agentic-access/fxapis-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fxapis-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/fxapis-com/plans/fxapis-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fxapis-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fxapis-com/rules/fxapis-com-rules.yml
  title: ''
  type: Spectral
  url: rules/fxapis-com-rules.yml
- group: design
  href: https://artifacts.apis.io/fxapis-com/vocabulary/fxapis-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fxapis-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fxapis-com/asyncapi/fxapis-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fxapis-com-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/fxapis-com/changelog/fxapis-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fxapis-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/fxapis-com/conventions/fxapis-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/fxapis-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/fxapis-com/conventions/fxapis-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fxapis-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/fxapis-com/authentication/fxapis-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fxapis-com-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fxapis.com
- group: design
  href: https://artifacts.apis.io/fxapis-com/lifecycle/fxapis-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fxapis-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/fxapis-com/errors/fxapis-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fxapis-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fxapis-com/conformance/fxapis-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fxapis-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fxapis-com/llms/fxapis-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fxapis-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/fxapis-com/well-known/fxapis-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fxapis-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/fxapis-com/hosts/fxapis-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fxapis-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/fxapis-com/vendors/fxapis-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fxapis-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/fxapis-com/packages/fxapis-com-packages.yml
  title: ''
  type: SDKs
  url: packages/fxapis-com-packages.yml
- group: build
  href: https://artifacts.apis.io/fxapis-com/packages/fxapis-com-packages.yml
  title: ''
  type: Packages
  url: packages/fxapis-com-packages.yml
- group: start
  title: ''
  type: Login
  url: https://fxapis.com/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://fxapis.com/changelog
- group: auth
  href: https://artifacts.apis.io/fxapis-com/security/fxapis-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fxapis-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fxapis.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fxapis.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fxapis.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fxapis.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fxapis.com/quickstart
- group: company
  title: ''
  type: Blog
  url: https://fxapis.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://fxapis.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fxapis.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fxapis.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FXapis
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.fxapis.com/openapi.json
  - status: 401
    url: https://api.fxapis.com/mcp
  - status: 200
    url: https://fxapis.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Fxapis provides a cloud-hosted MetaTrader 5 (MT5) API that enables developers to connect, trade, and manage multiple MT5 broker accounts via a single RESTful interface. The platform offers scoped API keys, idempotent order execution, multi‑account batch trading, and comprehensive SDKs in TypeScript and Python. It targets fintech developers, signal providers, copy‑trading services, and prop‑firms seeking fast, reliable access to MT5 brokerage functionality without managing terminals or VPS infrastructure. Fxapis also supplies open‑source client libraries, example projects, and a hosted MCP server for AI agent integration.
image: https://fxapis.com/opengraph-image
layout: provider
modified: '2026-10-30'
name: fxapis-com
nav: Providers
network: true
overview: 'fxapis-com publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Alerts API, API keys API, and 13 more. Tagged areas include Company, Fintech, Trading, MT5, and Cloud.


  The fxapis-com catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  fxapis-com''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 25 more developer resources.'
plans:
- name: Fxapis Com Plans Pricing
  plan_count: 4
  slug: fxapis-com-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: fxapis-com API Rules
  rule_count: 55
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 9
  slug: fxapis-com-rules
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 57.5
    developer_ergonomics: 39.3
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 59.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fxapis-com/fxapis-com-2026-11-03T132411.png
security:
- kind: authentication
  name: Fxapis Com Authentication
  slug: fxapis-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fxapis Com Domain Security
  slug: fxapis-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fxapis-com
tags:
- Company
- Fintech
- Trading
- MT5
- Cloud
website: https://fxapis.com/
---
