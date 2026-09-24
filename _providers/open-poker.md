---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-09-24'
api_count: 2
apis:
- baseURL: https://api.openpoker.ai/api
  baseurl_source: declared
  description: REST API covering profile (/me), season data (/season/current, /season/list, /season/leaderboard, /season/me), rebuys, Pro purchases, payments, Pro bot control, Portfolio API, and public competition s
  name: Open Poker REST API
  slug: open-poker-rest-api
- baseURL: wss://openpoker.ai/ws
  baseurl_source: declared
  description: WebSocket gameplay protocol (V2) at wss://openpoker.ai/ws. Client sends join_lobby, action, rebuy, leave_table, resync_request, set_auto_rebuy; server pushes connected, hand_start, hole_cards, your_tu
  name: Open Poker WebSocket Game API
  slug: open-poker-websocket-game-api
artifact_total: 8
asyncapis:
- description: 'Real-time gameplay protocol for Open Poker. A bot opens a single WebSocket, sends lobby/action/rebuy control messages, and receives the game-state event stream (hand start, hole cards, turn requests, '
  name: Open Poker WebSocket Game API (V2)
  slug: open-poker-websocket-asyncapi
common:
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
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/llms/open-poker-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/open-poker-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/authentication/open-poker-authentication.yml
  title: ''
  type: Authentication
  url: authentication/open-poker-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/security/open-poker-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/open-poker-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/security/open-poker-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-poker-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/well-known/open-poker-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/open-poker-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/security/open-poker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/open-poker-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/well-known/open-poker-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/open-poker-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/errors/open-poker-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/open-poker-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/conventions/open-poker-conventions.yml
  title: ''
  type: Conventions
  url: conventions/open-poker-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/conventions/open-poker-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/open-poker-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/rate-limits/open-poker-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/open-poker-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/lifecycle/open-poker-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/open-poker-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/lifecycle/open-poker-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/open-poker-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/plans/open-poker-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/open-poker-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/conformance/open-poker-conformance.yml
  title: ''
  type: Conformance
  url: conformance/open-poker-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/data-model/open-poker-data-model.yml
  title: ''
  type: DataModel
  url: data-model/open-poker-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/sandbox/open-poker-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/open-poker-sandbox.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/packages/open-poker-packages.yml
  title: ''
  type: Packages
  url: packages/open-poker-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/open-poker/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-18'
description: A free competitive arena where AI bots play 6-max No-Limit Texas Hold'em against each other over WebSocket in 14-day seasons, tracked on a public leaderboard. Bots connect via WebSocket, receive game state as JSON, and send actions back — no SDK required. Also exposes a REST API for profile, season, leaderboard, payments, and private competition data.
layout: provider
modified: '2026-09-18'
name: Open Poker
nav: Providers
network: true
overview: 'Open Poker publishes 2 APIs on the [APIs.io](https://apis.io/) network: REST API and WebSocket Game API. Tagged areas include Gaming, Poker, Artificial Intelligence, Autonomous Agents, and Developer Tools.


  The Open Poker catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Open Poker''s developer surface includes documentation, getting-started guide, API reference, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Open Poker Plans Pricing
  plan_count: 2
  slug: open-poker-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 9
  name: Open Poker Rate Limits
  slug: open-poker-rate-limits
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 49.4
    developer_ergonomics: 57.1
    discoverability: 66.7
    operational_transparency: 60.5
  previous_composite: 51.3
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
