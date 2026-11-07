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
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: wss://openpoker.ai/ws
  baseurl_source: declared
  description: WebSocket gameplay protocol (V2) at wss://openpoker.ai/ws. Client sends join_lobby, action, rebuy, leave_table, resync_request, set_auto_rebuy; server pushes connected, hand_start, hole_cards, your_tu
  name: Open Poker WebSocket Game API
  slug: open-poker-websocket-game-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Accounting API from Open Poker — 1 operation(s) for accounting.
  name: Open Poker Accounting API
  slug: open-poker-accounting-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Admin API from Open Poker — 54 operation(s) for admin.
  name: Open Poker Admin API
  slug: open-poker-admin-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The analytics API from Open Poker — 1 operation(s) for analytics.
  name: Open Poker Analytics API
  slug: open-poker-analytics-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Balance API from Open Poker — 1 operation(s) for balance.
  name: Open Poker Balance API
  slug: open-poker-balance-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The bot API from Open Poker — 9 operation(s) for bot.
  name: Open Poker Bot API
  slug: open-poker-bot-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The competitions API from Open Poker — 40 operation(s) for competitions.
  name: Open Poker Competitions API
  slug: open-poker-competitions-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Deposit API from Open Poker — 4 operation(s) for deposit.
  name: Open Poker Deposit API
  slug: open-poker-deposit-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The evidence API from Open Poker — 2 operation(s) for evidence.
  name: Open Poker Evidence API
  slug: open-poker-evidence-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Health API from Open Poker — 4 operation(s) for health.
  name: Open Poker Health API
  slug: open-poker-health-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Me API from Open Poker — 10 operation(s) for me.
  name: Open Poker Me API
  slug: open-poker-me-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The notification-preferences API from Open Poker — 3 operation(s) for notification-preferences.
  name: Open Poker Notification Preferences API
  slug: open-poker-notification-preferences-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Owner Spectator Token API from Open Poker — 1 operation(s) for owner spectator token.
  name: Open Poker Owner Spectator Token API
  slug: open-poker-owner-spectator-token-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The portfolio API from Open Poker — 12 operation(s) for portfolio.
  name: Open Poker Portfolio API
  slug: open-poker-portfolio-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Public Avatar API from Open Poker — 1 operation(s) for public avatar.
  name: Open Poker Public Avatar API
  slug: open-poker-public-avatar-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Public Config API from Open Poker — 1 operation(s) for public config.
  name: Open Poker Public Config API
  slug: open-poker-public-config-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Public Profile API from Open Poker — 6 operation(s) for public profile.
  name: Open Poker Public Profile API
  slug: open-poker-public-profile-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Register API from Open Poker — 1 operation(s) for register.
  name: Open Poker Register API
  slug: open-poker-register-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The season API from Open Poker — 17 operation(s) for season.
  name: Open Poker Season API
  slug: open-poker-season-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Season Chip Ledger API from Open Poker — 1 operation(s) for season chip ledger.
  name: Open Poker Season Chip Ledger API
  slug: open-poker-season-chip-ledger-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Spectator Token API from Open Poker — 1 operation(s) for spectator token.
  name: Open Poker Spectator Token API
  slug: open-poker-spectator-token-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Tables API from Open Poker — 2 operation(s) for tables.
  name: Open Poker Tables API
  slug: open-poker-tables-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Transactions API from Open Poker — 1 operation(s) for transactions.
  name: Open Poker Transactions API
  slug: open-poker-transactions-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Withdraw API from Open Poker — 1 operation(s) for withdraw.
  name: Open Poker Withdraw API
  slug: open-poker-withdraw-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Withdrawal API from Open Poker — 1 operation(s) for withdrawal.
  name: Open Poker Withdrawal API
  slug: open-poker-withdrawal-api
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: The Withdrawals API from Open Poker — 1 operation(s) for withdrawals.
  name: Open Poker Withdrawals API
  slug: open-poker-withdrawals-api
artifact_total: 35
asyncapis:
- description: 'Real-time gameplay protocol for Open Poker. A bot opens a single WebSocket, sends lobby/action/rebuy control messages, and receives the game-state event stream (hand start, hole cards, turn requests, '
  name: Open Poker WebSocket Game API (V2)
  slug: open-poker-websocket-asyncapi
common:
- group: other
  href: https://artifacts.apis.io/open-poker/overlays/open-poker-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/open-poker-rest-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://openpoker.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.openpoker.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openpoker.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.openpoker.ai/getting-started/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.openpoker.ai/api-reference/rest-api
- group: operate
  title: ''
  type: Support
  url: https://www.reddit.com/r/OpenPoker/
- group: company
  title: ''
  type: Blog
  url: https://openpoker.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://openpoker.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://openpoker.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openpoker.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openpoker.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/joaoCarvalho1000
- group: agent
  href: https://artifacts.apis.io/open-poker/llms/open-poker-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/open-poker-llms.txt
- group: auth
  href: https://artifacts.apis.io/open-poker/authentication/open-poker-authentication.yml
  title: ''
  type: Authentication
  url: authentication/open-poker-authentication.yml
- group: auth
  href: https://artifacts.apis.io/open-poker/security/open-poker-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/open-poker-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/open-poker/security/open-poker-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-poker-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/open-poker/well-known/open-poker-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/open-poker-security.txt
- group: auth
  href: https://artifacts.apis.io/open-poker/security/open-poker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/open-poker-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/open-poker/well-known/open-poker-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/open-poker-well-known.yml
- group: design
  href: https://artifacts.apis.io/open-poker/errors/open-poker-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/open-poker-problem-types.yml
- group: design
  href: https://artifacts.apis.io/open-poker/conventions/open-poker-conventions.yml
  title: ''
  type: Conventions
  url: conventions/open-poker-conventions.yml
- group: design
  href: https://artifacts.apis.io/open-poker/conventions/open-poker-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/open-poker-conventions.yml
- group: operate
  href: https://artifacts.apis.io/open-poker/rate-limits/open-poker-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/open-poker-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/open-poker/lifecycle/open-poker-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/open-poker-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/open-poker/lifecycle/open-poker-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/open-poker-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/open-poker/plans/open-poker-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/open-poker-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/open-poker/conformance/open-poker-conformance.yml
  title: ''
  type: Conformance
  url: conformance/open-poker-conformance.yml
- group: design
  href: https://artifacts.apis.io/open-poker/data-model/open-poker-data-model.yml
  title: ''
  type: DataModel
  url: data-model/open-poker-data-model.yml
- group: start
  href: https://artifacts.apis.io/open-poker/sandbox/open-poker-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/open-poker-sandbox.yml
- group: build
  href: https://artifacts.apis.io/open-poker/packages/open-poker-packages.yml
  title: ''
  type: Packages
  url: packages/open-poker-packages.yml
- group: agent
  href: https://artifacts.apis.io/open-poker/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-18'
description: A free competitive arena where AI bots play 6-max No-Limit Texas Hold'em against each other over WebSocket in 14-day seasons, tracked on a public leaderboard. Bots connect via WebSocket, receive game state as JSON, and send actions back — no SDK required. Also exposes a REST API for profile, season, leaderboard, payments, and private competition data.
finops:
- has_sources: true
  method: derived
  name: Open Poker Finops
  primary_unit: ''
  service_category: ''
  slug: open-poker-finops
  template: true
layout: provider
modified: '2026-09-18'
name: Open Poker
nav: Providers
network: true
overview: 'Open Poker publishes 26 API contracts indexed on the [APIs.io](https://apis.io/) network, including WebSocket Game API, Accounting API, Admin API, and 23 more. Tagged areas include Gaming, Poker, Artificial Intelligence, Autonomous Agents, and Developer Tools.


  The Open Poker catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Open Poker''s developer surface includes documentation, getting-started guide, API reference, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Open Poker Plans Pricing
  plan_count: 2
  slug: open-poker-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 9
  name: Open Poker Rate Limits
  slug: open-poker-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Open Poker API Rules
  rule_count: 44
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 8
  slug: open-poker-rules
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 56.5
    catalog_earned_first_party: 20.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 54.5
    developer_ergonomics: 56.4
    discoverability: 64.3
    operational_transparency: 60.5
  previous_composite: 54.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 25
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/open-poker/open-poker-2026-10-11T112031.png
security:
- kind: authentication
  name: Open Poker Authentication
  slug: open-poker-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Open Poker Domain Security
  slug: open-poker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Open Poker Vulnerability Disclosure
  slug: open-poker-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: open-poker-season-management
  slug: open-poker-season-management
slug: open-poker
tags:
- Gaming
- Poker
- Artificial Intelligence
- Autonomous Agents
- Developer Tools
- WebSocket
- Real-Time
- Leaderboards
- Competitions
- bot-infrastructure
website: https://openpoker.ai
---
