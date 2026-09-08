---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-09-07'
api_count: 1
apis:
- baseURL: https://parlay-api.com
  baseurl_source: declared
  description: 'REST API for live and historical sports odds, player props, prediction-market prices, arbitrage/EV scanning, and account webhooks, with keyless sandbox and try surfaces, credit-based metering, and an '
  name: ParlayAPI
  slug: parlayapi
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://parlay-api.com
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/parlay-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/parlay-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parlay-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parlay-api-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/parlay-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/parlay-api-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/parlay-api-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/parlay-api-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/parlay-api-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parlay-api-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/parlay-api-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parlay-api-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://parlay-api.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/parlay-api-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/parlay-api-plans-pricing.yml
- group: design
  title: ''
  type: Components
  url: components/parlay-api-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://parlay-api.com/support
- group: company
  title: ''
  type: Blog
  url: https://parlay-api.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://parlay-api.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://parlay-api.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://parlay-api.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JacobiusMakes
created: '2026-09-07'
description: Real-time sports odds aggregation API covering 30+ sportsbooks and sources — regulated US books, DFS apps, betting exchanges, and prediction markets (Kalshi, Polymarket) — across 92 sport keys, with player props, historical closing lines from 2005, arbitrage/EV/middles scanning, devig and parlay calculators, WebSocket/SSE streaming, webhooks, an official MCP server, and programmatic agent signup. Drop-in replacement for the-odds-api v4. Free tier 1,000 credits/month; public display and redistribution rights are not included.
image: https://parlay-api.com/static/logo.png
layout: provider
mcp_servers:
- description: 'Official first-party MCP server (parlayapi-mcp) exposing sports odds, props, prediction-market data, live previews, source-quality proof, and agent signup as 22 tools. Local stdio transport only — no '
  name: ParlayAPI MCP Server
  slug: parlayapi-mcp-server
modified: '2026-09-07'
name: ParlayAPI
nav: Providers
network: true
overview: 'ParlayAPI publishes 1 API on the [APIs.io](https://apis.io/) network: ParlayAPI. Tagged areas include Sports, Odds, Betting Data, Sports Data, and Prediction Markets.


  ParlayAPI''s developer surface includes authentication, changelog, support, engineering blog, signup flow, and 19 more developer resources.'
plans:
- name: Parlay Api Plans Pricing
  plan_count: 6
  slug: parlay-api-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 8
  name: Parlay Api Rate Limits
  slug: parlay-api-rate-limits
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 51.1
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 84.2
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Parlay Api Authentication
  slug: parlay-api-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Parlay Api Domain Security
  slug: parlay-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Parlay Api Vulnerability Disclosure
  slug: parlay-api-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: parlay-api
tags:
- Sports
- Odds
- Betting Data
- Sports Data
- Prediction Markets
- Player Props
- Arbitrage
- Streaming
website: https://parlay-api.com
---
