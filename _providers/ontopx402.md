---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source: []
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.1
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://ontopx402.com
  baseurl_source: declared
  description: The bidding API from OnTopX402 — 1 operation(s) for bidding.
  name: OnTopX402 Bidding API
  slug: ontopx402-bidding-api
- baseURL: https://ontopx402.com
  baseurl_source: declared
  description: The leaderboard API from OnTopX402 — 2 operation(s) for leaderboard.
  name: OnTopX402 Leaderboard API
  slug: ontopx402-leaderboard-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ontopx402-domain-security.yml
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
- group: auth
  title: ''
  type: Authentication
  url: authentication/ontopx402-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ontopx402-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ontopx402-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ontopx402-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ontopx402-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ontopx402-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ontopx402-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ontopx402-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ontopx402-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://ontopx402.com/rules
created: '2026-08-24'
description: 'OnTopX402 is a single public leaderboard of links in which rank is decided solely by the amount paid, settled in USDC over x402. There is no account, no API key and no card: an agent reads the board, decides what a position is worth, pays, and is listed in one request with no human involved. Three operations — read the leaderboard, read an entry, and bid. The bid endpoint returns an HTTP 402 payment challenge at x402 version 2, priced at a $1 minimum and payable in USDC on Base or Solana. Operated by One Scales Inc.'
examples:
- key_count: 5
  name: Ontopx402 Leaderboard Example
  slug: ontopx402-leaderboard-example
layout: provider
modified: '2026-09-03'
name: OnTopX402
nav: Providers
network: true
overview: 'OnTopX402 publishes 2 APIs on the [APIs.io](https://apis.io/) network: Bidding API and Leaderboard API. Tagged areas include x402, USDC, Agent Payments, paid-placement, and Leaderboard.


  OnTopX402''s developer surface includes authentication, pricing, and 13 more developer resources.'
plans:
- name: Ontopx402 Plans Pricing
  plan_count: 1
  slug: ontopx402-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Ontopx402 Rate Limits
  slug: ontopx402-rate-limits
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 16.3
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 58.8
    developer_ergonomics: 35.7
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 20.4
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/ontopx402/refs/heads/main/screenshots/ontopx402-2026-09-02T150847.png
security:
- kind: authentication
  name: Ontopx402 Authentication
  slug: ontopx402-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ontopx402 Domain Security
  slug: ontopx402-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ontopx402
tags:
- x402
- USDC
- Agent Payments
- paid-placement
- Leaderboard
website: https://ontopx402.com/
---
