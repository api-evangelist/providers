---
agent_readiness:
  band: agent-aware
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: REST API providing heuristic risk briefs for EVM addresses, tokens, and URLs via GET /v1/brief. Includes x402 discovery manifest and health endpoint. Supports free tier, Stripe Bearer keys, and x402 p
  name: 54ch10 Brief API
  slug: 54ch10-brief-api
artifact_total: 1
created: '2026-08-24'
description: Pre-interaction JSON risk 'briefs' (heuristic scoring) for EVM addresses, tokens, and URLs, intended to be called before a wallet signs, approves, bridges, or opens a dapp URL. Returns a score, band, flags, summary, and sources. Supports free tier, Stripe API keys, and x402 agent-native pay-per-brief in USDC.
layout: provider
modified: '2026-08-24'
name: 54ch10 Brief API
nav: Providers
network: true
overview: '54ch10 Brief API publishes 1 API on the [APIs.io](https://apis.io/) network: 54ch10 Brief API. Tagged areas include Web3, blockchain-security, EVM, wallet-risk, and phishing-screening.'
random_paper: 6
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 0.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: 54ch10-brief-api
tags:
- Web3
- blockchain-security
- EVM
- wallet-risk
- phishing-screening
- url-screening
- token-reputation
- address-reputation
- pre-transaction-analytics
- Agent Tooling
- x402
- pay-per-call
- Machine Payments
- USDC
- agent-native
---
