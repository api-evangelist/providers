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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nansen Agentic Access
  operation_count: 6
  slug: nansen-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: 'REST API surfacing Nansen''s on-chain intelligence: smart-money flows, profiler (wallet labels and balances), token screener, portfolio, points, Hyperliquid analytics, prediction markets, and the Nanse'
  name: Nansen REST API
  slug: rest-api
- description: Smart-money wallet flows and behavior.
  name: Nansen Smart Money API
  slug: nansen-smart-money-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nansen REST Smart Money API
  slug: open-nansen-smart-money-api
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
overview: 'Nansen publishes 1 API on the [APIs.io](https://apis.io/) network: Smart Money API. Tagged areas include Web3, Crypto, Onchain, Wallet Labels, and Smart Money.


  Nansen''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Nansen Plans Pricing
  plan_count: 2
  slug: nansen-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Nansen Rate Limits
  slug: nansen-rate-limits
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.1
  provenance:
    agentic_access: derived
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
    score: 18.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Onchain
- Wallet Labels
- Smart Money
- Analytics
- Multi-Chain
website: https://www.nansen.ai/
---
