---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nansen Agentic Access
  operation_count: 6
  slug: nansen-agentic-access
  summary_line: 6 operations
api_count: 2
apis:
- description: 'REST API surfacing Nansen''s on-chain intelligence: smart-money flows, profiler (wallet labels and balances), token screener, portfolio, points, Hyperliquid analytics, prediction markets, and the Nanse'
  name: Nansen REST API
  slug: rest-api
- description: Smart-money wallet flows and behavior.
  name: Nansen Smart Money API
  slug: nansen-smart-money-api
artifact_total: 9
collections:
- collection_type: open
  name: Nansen REST API
  slug: open-nansen
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nansen-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nansen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nansen-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nansen-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nansen
- group: start
  title: ''
  type: Portal
  url: https://www.nansen.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nansen.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nansen.ai/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/nansen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nansen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nansen-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.nansen.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://nansen.ai/blog
created: '2026-05-08'
description: Nansen is an onchain analytics platform with wallet labeling, smart-money tracking, token screener, portfolio, prediction markets, and AI Agent endpoints across 30+ chains. The Nansen API exposes REST endpoints under api.nansen.ai with Smart Money, Profiler, Token Screener, Portfolio, Points, Hyperliquid, Agent, and Prediction Markets categories.
finops:
- name: Nansen Finops
  service_category: Crypto Analytics
  slug: nansen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nansen.png
layout: provider
modified: '2026-05-08'
name: Nansen
nav: Providers
network: true
overview: 'Nansen publishes 1 API on the [APIs.io](https://apis.io/) network: Smart Money API. Tagged areas include Web3, Crypto, On-Chain, Wallet Labels, and Smart Money.


  Nansen''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Nansen Plans Pricing
  plan_count: 2
  slug: nansen-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 3
  name: Nansen Rate Limits
  slug: nansen-rate-limits
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.3
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nansen/refs/heads/main/screenshots/nansen-2026-06-20T185943.png
security:
- kind: authentication
  name: Nansen Authentication
  slug: nansen-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nansen Domain Security
  slug: nansen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nansen
tags:
- Web3
- Crypto
- On-Chain
- Wallet Labels
- Smart Money
- Analytics
- Multi-chain
website: https://www.nansen.ai/
---
