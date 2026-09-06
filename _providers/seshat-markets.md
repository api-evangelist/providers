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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://kronos.seshat.markets/api
  baseurl_source: declared
  description: Live REST/JSON API with 32 endpoints for price-path forecasting, market/risk context, accuracy audits, and agent signals. Several endpoints are free; the rest are paid per-request via x402 USDC microp
  name: Kronos Quant Signal REST API
  slug: kronos-quant-signal-rest-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://seshat.markets
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/seshat-markets-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seshat-markets-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seshat-markets-authentication.yml
- group: auth
  title: ''
  type: Security
  url: security/seshat-markets-vulnerability-disclosure.yml
- group: docs
  title: ''
  type: Documentation
  url: https://kronos.seshat.markets/docs
- group: docs
  title: ''
  type: APIReference
  url: https://kronos.seshat.markets/api
- group: start
  title: ''
  type: GettingStarted
  url: https://kronos.seshat.markets/docs#start
- group: commercial
  title: ''
  type: Pricing
  url: https://kronos.seshat.markets/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kronos.seshat.markets/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kronos.seshat.markets/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://seshat.markets/status.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seshat-markets-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/seshat-markets-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/seshat-markets-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/seshat-markets-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/seshat-markets-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/seshat-markets-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/seshat-markets-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/seshat-markets-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/seshat-markets-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/seshat-markets-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/seshat-markets-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/seshat-markets-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/seshat-markets-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/seshat-markets-packages.yml
created: '2026-09-05'
description: A public, keyless, agent-native quantitative forecasting API by Seshat providing multi-timeframe price-path forecasts, market/risk context, accuracy audits, and agent-intelligence signals for crypto, commodities, and pre-market equities. Authenticated entirely via x402 USDC micropayments on Solana and Base mainnet, with no API keys or subscriptions.
image: https://kronos.seshat.markets/assets/kronos-seshat-logo.webp
layout: provider
mcp_servers:
- description: ''
  name: Seshat Markets MCP Server
  slug: seshat-markets-mcp-server
modified: '2026-09-05'
name: Seshat Markets
nav: Providers
network: true
overview: 'Seshat Markets publishes 1 API on the [APIs.io](https://apis.io/) network: Kronos Quant Signal REST API. Tagged areas include finance, fintech, crypto, commodities, and forecasting.


  Seshat Markets'' developer surface includes authentication, documentation, API reference, getting-started guide, pricing, sandbox, and 21 more developer resources.'
plans:
- name: Seshat Markets Plans Pricing
  plan_count: 0
  slug: seshat-markets-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 9
  name: Seshat Markets Rate Limits
  slug: seshat-markets-rate-limits
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 51.7
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 57.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 61.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Seshat Markets Authentication
  slug: seshat-markets-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Seshat Markets Domain Security
  slug: seshat-markets-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Seshat Markets Vulnerability Disclosure
  slug: seshat-markets-vulnerability-disclosure
  summary_line: disclosure policy published
slug: seshat-markets
tags:
- finance
- fintech
- crypto
- commodities
- forecasting
- prediction
- market-data
- trading-signals
- research
- ai-agents
- mcp
- a2a
- x402
- llms-txt
- agent-skills
website: https://seshat.markets
---
