---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/torquantis-com/security/torquantis-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/torquantis-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://torquantis.com/
coverage:
  checked: '2026-09-19'
  detail: torquantis.com now serves only the login-gated "Torquantis Desk" single-page app (Caddy, built 2026-09-19, allow GET/HEAD) - every path including the A2A agent card and llms.txt that a2aregistry.org recorded on 2026-09-11 returns the same 758-byte HTML shell, POST to the /mcp, /a2a and /x402/buy endpoints that awesome-remote-mcp-servers and gold-402 list answers 405, and the only live API, the desk backend at /api/*, answers 401 "Not logged in" with no public reference (/api/openapi.json and /api/docs are 404).
  evidence:
  - status: 200
    url: https://torquantis.com/.well-known/agent-card.json
  - status: 405
    url: https://torquantis.com/mcp
  - status: 405
    url: https://torquantis.com/a2a
  - status: 401
    url: https://torquantis.com/api/accounts
  - status: 404
    url: https://torquantis.com/api/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-09-19'
description: 'Torquantis is an AI agent work exchange: an order book where AI agents buy and sell units of work from each other in USDC on Base - GPU hours (A100, H100), inference, research briefs, code tasks, agent hours, transcription, web fetching and human checks, plus requests for quote - with escrow, AI-judged disputes and reputation. It registered an A2A 0.3.0 agent card on a2aregistry.org on 2026-09-11 naming a hosted MCP server at torquantis.com/mcp, an x402 pay-per-call door on every market and an llms.txt. As of 2026-09-19 torquantis.com serves only the login-gated Torquantis Desk web app: the agent card, llms.txt, /mcp, /a2a and /x402 paths all return the app shell or HTTP 405, and no public API documentation or contract is published.'
layout: provider
modified: '2026-09-19'
name: Torquantis
nav: Providers
network: true
overview: Torquantis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Agent Marketplace, A2A, and MCP.
random_paper: 14
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 5.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Torquantis Com Domain Security
  slug: torquantis-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: torquantis-com
tags:
- Company
- AI Agents
- Agent Marketplace
- A2A
- MCP
- x402
- USDC
- GPU Compute
- Inference
- Order Book
website: https://torquantis.com/
---
