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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-09-15'
api_count: 1
apis:
- baseURL: https://edge.arakelproof.space
  baseurl_source: declared
  description: Read-only REST API providing compact market context, topic-specific context, and richer decision-support context for AI agents. Payment-gated via x402 (USDC on Base); no API key or signup. Also expose
  name: EventEdge Oracle Agent Context API
  slug: eventedge-oracle-agent-context-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://edge.arakelproof.space
created: '2026-09-15'
description: Read-only, machine-readable prediction-market context (Polymarket + Kalshi) built for autonomous AI agents. Provides decision-support data only (no trade execution), accessed via the x402 pay-per-request payment protocol (USDC on Base). Exposes a REST API (OpenAPI 3.1), a live remote MCP server, an A2A agent card backed by a live /a2a JSON-RPC endpoint, and llms.txt / ai-plugin / x402 discovery surfaces.
layout: provider
mcp_servers:
- description: ''
  name: EventEdge Oracle MCP Server
  slug: eventedge-oracle-mcp-server
modified: '2026-09-15'
name: EventEdge Oracle
nav: Providers
network: true
overview: 'EventEdge Oracle publishes 1 API on the [APIs.io](https://apis.io/) network: Agent Context API. Tagged areas include Prediction Markets, x402, AI Agents, Polymarket, and Kalshi.'
plans:
- name: Eventedge Oracle Plans Pricing
  plan_count: 0
  slug: eventedge-oracle-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Eventedge Oracle Rate Limits
  slug: eventedge-oracle-rate-limits
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 55.2
    developer_ergonomics: 30.4
    discoverability: 72.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Eventedge Oracle Authentication
  slug: eventedge-oracle-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Eventedge Oracle Domain Security
  slug: eventedge-oracle-domain-security
  summary_line: TLSv1.3
slug: eventedge-oracle
tags:
- Prediction Markets
- x402
- AI Agents
- Polymarket
- Kalshi
- market-context
- Decision Support
- Finance
website: https://edge.arakelproof.space
---
