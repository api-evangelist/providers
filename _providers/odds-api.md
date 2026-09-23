---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.4
  scored_at: '2026-09-23'
api_count: 1
apis:
- baseURL: https://api.odds-api.net/v1
  baseurl_source: declared
  description: REST API for sports and racing betting odds with SSE and WebSocket streaming, arbitrage, positive EV, line movement, bookmaker comparison, and results. API-key auth via X-API-Key.
  name: Odds API REST
  slug: odds-api-rest
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/odds-api/refs/heads/main/security/odds-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/odds-api-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/odds-api/refs/heads/main/security/odds-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/odds-api-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/odds-api/refs/heads/main/authentication/odds-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/odds-api-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/odds-api/refs/heads/main/security/odds-api-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/odds-api-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/odds-api/refs/heads/main/well-known/odds-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/odds-api-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/odds-api/refs/heads/main/well-known/odds-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/odds-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/odds-api/refs/heads/main/skills/_index.yml
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
overview: 'Odds API publishes 1 API on the [APIs.io](https://apis.io/) network: REST. Tagged areas include Sports, Sports Betting, betting-odds, bookmaker-odds, and live-odds.


  Odds API''s developer surface includes authentication and 11 more developer resources.'
plans:
- name: Odds Api Plans Pricing
  plan_count: 5
  slug: odds-api-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Odds Api Rate Limits
  slug: odds-api-rate-limits
score:
  band: strong
  composite: 57.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 51.6
    developer_ergonomics: 64.3
    discoverability: 75.9
    operational_transparency: 60.5
  previous_composite: 57.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
slug: odds-api
tags:
- Sports
- Sports Betting
- betting-odds
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
- llms-txt
- SDK
- Postman
website: https://odds-api.net/
---
