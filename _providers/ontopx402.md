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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Read the leaderboard, read a single entry, and bid for rank. GET /api/leaderboard returns the board unauthenticated; POST /api/bid returns an x402 payment challenge rather than requiring an account.
  name: OnTopX402 API
  slug: ontopx402-api
artifact_total: 2
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ontopx402-llms.txt
- group: company
  title: ''
  type: Website
  url: https://ontopx402.com/
- group: commercial
  title: ''
  type: FinOps
  url: finops/ontopx402-x402-challenge.json
created: '2026-08-24'
description: 'OnTopX402 is a single public leaderboard of links in which rank is decided solely by the amount paid, settled in USDC over x402. There is no account, no API key and no card: an agent reads the board, decides what a position is worth, pays, and is listed in one request with no human involved. Three operations — read the leaderboard, read an entry, and bid. The bid endpoint returns an HTTP 402 payment challenge at x402 version 2, priced at a $1 minimum and payable in USDC on Base or Solana. Operated by One Scales Inc.'
examples:
- key_count: 5
  name: Ontopx402 Leaderboard Example
  slug: ontopx402-leaderboard-example
layout: provider
modified: '2026-08-24'
name: OnTopX402
nav: Providers
network: true
overview: OnTopX402 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include x402, Agent Commerce, Machine Payments, Advertising, and Paid Placement.
random_paper: 11
score:
  band: emerging
  composite: 20.7
  delta: 4.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 59.9
    developer_ergonomics: 16.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 0.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
slug: ontopx402
tags:
- x402
- Agent Commerce
- Machine Payments
- Advertising
- Paid Placement
- Leaderboard
- USDC
website: https://ontopx402.com/
---
