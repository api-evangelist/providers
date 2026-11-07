---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 6
  name: Verse Me Com Agentic Access
  operation_count: 12
  slug: verse-me-com-agentic-access
  summary_line: 12 operations · 6 acting · 6 human-in-the-loop
api_count: 2
apis:
- description: 'Agent2Agent surface declared by the card at https://api.verse-me.com/.well-known/agent.json (version 2.0.0, A2A 1.0 shape: supportedInterfaces[0] JSONRPC at https://api.verse-me.com, protocolVersion 1'
  name: Verse A2A Agent
  slug: verse-a2a-agent
- description: 'The REST paths the agent card names on api.verse-me.com, with no OpenAPI behind them: free reads GET /expertise/calibration, /expertise/calibration/signed, /expertise/calibration/history (+ /signed) a'
  name: Verse Expertise API
  slug: verse-expertise-api
artifact_total: 9
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://api.verse-me.com/.well-known/agent.json
- group: company
  title: ''
  type: Website
  url: https://api.verse-me.com/
- group: other
  href: https://artifacts.apis.io/verse-me-com/a2a/verse-me-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/verse-me-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/verse-me-com/well-known/verse-me-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/verse-me-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/verse-me-com/authentication/verse-me-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/verse-me-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/verse-me-com/conformance/verse-me-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/verse-me-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/verse-me-com/conventions/verse-me-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/verse-me-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/verse-me-com/errors/verse-me-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/verse-me-com-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/verse-me-com/rate-limits/verse-me-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/verse-me-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/verse-me-com/plans/verse-me-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/verse-me-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/verse-me-com/lifecycle/verse-me-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/verse-me-com-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/verse-me-com/llms/verse-me-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/verse-me-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/verse-me-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/verse-me-com/agentic-access/verse-me-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/verse-me-com-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/verse-me-com/packages/verse-me-com-packages.yml
  title: ''
  type: Packages
  url: packages/verse-me-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/verse-me-com/security/verse-me-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/verse-me-com-domain-security.yml
- group: other
  title: ''
  type: AITransparency
  url: https://api.verse-me.com/.well-known/agent.json
created: '2026-09-19'
description: 'Verse is an autonomous AI agent — self-described in its agent card as running claude-opus-4-6 with persistent memory — that sells calibrated probability estimates and strategic analysis on AI capabilities, markets, geopolitics and science, plus SEC EDGAR financial analysis, to other agents and to people. It has no accounts and no API keys: paid endpoints answer HTTP 402 and are settled per call in USDC on Base through the x402 protocol ($0.01 to $50 per request as published), while its prediction track record is served free and Ed25519-signed so a caller can audit the forecaster before paying. Its identity is bound on-chain to ERC-8004 agentId 29481 on Base. The only document it publishes is an A2A agent card at https://api.verse-me.com/.well-known/agent.json (also on brain.verse-me.com); there is no OpenAPI, docs site, SDK or MCP server, the apex verse-me.com does not resolve, and every application path answers a Cloudflare managed challenge to non-browser clients.'
layout: provider
modified: '2026-09-19'
name: Verse (autonomous agent)
nav: Providers
network: true
overview: 'Verse (autonomous agent) is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Autonomous Agents, A2A, and x402.


  Verse (autonomous agent)''s developer surface includes pricing, authentication, and 15 more developer resources.'
plans:
- name: Verse Me Com Plans Pricing
  plan_count: 8
  slug: verse-me-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Verse Me Com Rate Limits
  slug: verse-me-com-rate-limits
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 20.7
  provenance:
    agentic_access: first-party
    conformance: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 21.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/verse-me-com/verse-me-com-2026-10-11T194137.png
security:
- kind: authentication
  name: Verse Me Com Authentication
  slug: verse-me-com-authentication
  summary_line: payment/none · 3 schemes
- kind: domain-security
  name: Verse Me Com Domain Security
  slug: verse-me-com-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: Ask Verse a paid question via x402
  slug: verse-me-com-paid-consultation
- name: Verify Verse's prediction track record before paying
  slug: verse-me-com-verify-track-record
slug: verse-me-com
tags:
- Company
- AI Agents
- Autonomous Agents
- A2A
- x402
- Agentic Commerce
- Forecasting
- Predictions
- Calibration
- Financial Analysis
- SEC EDGAR
- Blockchain
- Base
- Agent-Native
website: https://api.verse-me.com/
---
