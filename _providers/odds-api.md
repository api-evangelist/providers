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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.odds-api.net/v1
  baseurl_source: declared
  description: Current API identity, usage counters, and contract limits.
  name: Odds API Account API
  slug: odds-api-account-api
- baseURL: https://api.odds-api.net/v1
  baseurl_source: declared
  description: Positive EV, arbitrage, middle, and bonus-bet opportunity feeds.
  name: Odds API Betting opportunities API
  slug: odds-api-betting-opportunities-api
- baseURL: https://api.odds-api.net/v1
  baseurl_source: declared
  description: Supported sports, leagues, bookmakers, and approximate market coverage.
  name: Odds API Catalog API
  slug: odds-api-catalog-api
- baseURL: https://api.odds-api.net/v1
  baseurl_source: declared
  description: Event-linked prediction-market order books with probability ladders, liquidity, and live updates.
  name: Odds API Prediction markets API
  slug: odds-api-prediction-markets-api
- baseURL: https://api.odds-api.net/v1
  baseurl_source: declared
  description: Racing event discovery and live racing event updates.
  name: Odds API Racing events API
  slug: odds-api-racing-events-api
- baseURL: https://api.odds-api.net/v1
  baseurl_source: declared
  description: Racing odds snapshots, home racing feeds, Server-Sent Events, and WebSocket updates.
  name: Odds API Racing odds API
  slug: odds-api-racing-odds-api
- baseURL: https://api.odds-api.net/v1
  baseurl_source: declared
  description: Sports event result lookup.
  name: Odds API Results API
  slug: odds-api-results-api
- baseURL: https://api.odds-api.net/v1
  baseurl_source: declared
  description: Upcoming and live sports events plus event metadata.
  name: Odds API Sports events API
  slug: odds-api-sports-events-api
- baseURL: https://api.odds-api.net/v1
  baseurl_source: declared
  description: Sports betting exchange order books with back/lay ladders, liquidity, and live updates.
  name: Odds API Sports exchange API
  slug: odds-api-sports-exchange-api
- baseURL: https://api.odds-api.net/v1
  baseurl_source: declared
  description: Sports odds snapshots, line movement, Server-Sent Events, and WebSocket updates.
  name: Odds API Sports odds API
  slug: odds-api-sports-odds-api
- baseURL: https://api.odds-api.net/v1
  baseurl_source: declared
  description: API identity, base URL, authentication, and reference links.
  name: Odds API Start here API
  slug: odds-api-start-here-api
- baseURL: https://api.odds-api.net/v1
  baseurl_source: declared
  description: Buyer-facing API availability, latency, stream health, and rate-limit health.
  name: Odds API Status API
  slug: odds-api-status-api
- baseURL: https://api.odds-api.net/v1
  baseurl_source: declared
  description: Public-safe embeddable widget feeds for approved API clients.
  name: Odds API Widgets API
  slug: odds-api-widgets-api
artifact_total: 26
common:
- group: other
  href: https://artifacts.apis.io/odds-api/capabilities/odds-api-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/odds-api-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/odds-api/plans/odds-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/odds-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/odds-api/rate-limits/odds-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/odds-api-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://odds-api.net/pricing
- group: agent
  title: ''
  type: AgentSkill
  url: https://github.com/odds-api/odds-api/blob/main/AGENTS.md
- group: other
  href: https://artifacts.apis.io/odds-api/overlays/odds-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/odds-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/odds-api/mcp/odds-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/odds-api-mcp.yml
- group: auth
  href: https://artifacts.apis.io/odds-api/security/odds-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/odds-api-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/odds-api/security/odds-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/odds-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/odds-api/authentication/odds-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/odds-api-authentication.yml
- group: auth
  href: https://artifacts.apis.io/odds-api/security/odds-api-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/odds-api-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/odds-api/well-known/odds-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/odds-api-well-known.yml
- group: auth
  href: https://artifacts.apis.io/odds-api/well-known/odds-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/odds-api-security.txt
- group: agent
  href: https://artifacts.apis.io/odds-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/odds-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://odds-api.net/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://odds-api.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://odds-api.net/privacy
- group: company
  title: ''
  type: Website
  url: https://odds-api.net/
created: '2026-09-17'
description: OpenAPI-first sports betting odds API (odds-api.net) providing bookmaker odds, odds comparison, arbitrage, positive EV, line movement, and racing/sports coverage via REST plus SSE and WebSocket streaming. Agent-native with an MCP server, llms.txt, and agent instruction files, plus TypeScript and Python SDKs.
finops:
- has_sources: true
  method: derived
  name: Odds Api Finops
  primary_unit: subscription
  service_category: ''
  slug: odds-api-finops
  template: false
image: https://raw.githubusercontent.com/odds-api/odds-api/main/assets/odds-api-hero.svg
layout: provider
mcp_servers:
- description: Official MCP server for sports and racing odds workflows. Distributed as a locally-run stdio package (npx @odds-api/mcp); wraps the Odds API REST V1 contract as agent tools, including bookmaker compar
  name: Odds API MCP Server
  slug: odds-api-mcp-server
modified: '2026-09-17'
name: Odds API
nav: Providers
network: true
overview: 'Odds API publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Betting opportunities API, Catalog API, and 10 more. Tagged areas include Sports, Sports Betting, Betting Odds, bookmaker-odds, and live-odds.


  The Odds API catalog on APIs.io includes 1 Spectral governance ruleset.


  Odds API''s developer surface includes pricing, authentication, and 17 more developer resources.'
plans:
- name: Odds Api Plans Pricing
  plan_count: 5
  slug: odds-api-plans-pricing
- name: Odds Api Price Estimates
  plan_count: 0
  slug: odds-api-price-estimates
random_paper: 17
rate_limits:
- limit_count: 5
  name: Odds Api Rate Limits
  slug: odds-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Odds API API Rules
  rule_count: 67
  severity_counts:
    error: 54
    hint: 0
    info: 3
    warn: 10
  slug: odds-api-rules
score:
  band: strong
  composite: 63.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 57.9
    developer_ergonomics: 63.6
    discoverability: 71.7
    operational_transparency: 60.5
  previous_composite: 62.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 13
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/odds-api/odds-api-2026-10-11T111805.png
security:
- kind: authentication
  name: Odds Api Authentication
  slug: odds-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Odds Api Domain Security
  slug: odds-api-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Odds Api Vulnerability Disclosure
  slug: odds-api-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: Odds API arbitrage scanner
  slug: odds-api-arbitrage-scanner
- name: Odds API line movement tracker
  slug: odds-api-line-movement
- name: Odds API positive EV scanner
  slug: odds-api-positive-ev-scanner
- name: odds-api
  slug: odds-api-provider-skill
slug: odds-api
tags:
- Sports
- Sports Betting
- Betting Odds
- bookmaker-odds
- live-odds
- Sportsbook
- Racing
- REST
- Server-Sent Events
- WebSocket
- OpenAPI
- MCP
- Agent-Native
- Llms.txt
- SDK
- Postman
website: https://odds-api.net/
---
