---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Defillama Agentic Access
  operation_count: 31
  slug: defillama-agentic-access
  summary_line: 31 operations
api_count: 8
apis:
- description: Free, no-auth REST API exposing 31+ endpoints for protocol TVL, chain TVL, coin prices, stablecoin metrics, yield pools, DEX volumes, and fees. Underpins thousands of dashboards and integrations.
  name: DefiLlama Public API
  slug: public-api
- description: Paid REST API ($300/month) with higher rate limits and 38 exclusive endpoints covering token unlocks, cross-chain bridges, digital-asset treasury data, and other advanced datasets. Authenticated via A
  name: DefiLlama Pro API
  slug: pro-api
- description: The Coins API from DefiLlama — 7 operation(s) for coins.
  name: DefiLlama Coins API
  slug: defillama-coins-api
- description: The Fees API from DefiLlama — 3 operation(s) for fees.
  name: DefiLlama Fees API
  slug: defillama-fees-api
- description: The Stablecoins API from DefiLlama — 6 operation(s) for stablecoins.
  name: DefiLlama Stablecoins API
  slug: defillama-stablecoins-api
- description: The TVL API from DefiLlama — 6 operation(s) for tvl.
  name: DefiLlama TVL API
  slug: defillama-tvl-api
- description: The Volumes API from DefiLlama — 7 operation(s) for volumes.
  name: DefiLlama Volumes API
  slug: defillama-volumes-api
- description: The Yields API from DefiLlama — 2 operation(s) for yields.
  name: DefiLlama Yields API
  slug: defillama-yields-api
artifact_total: 15
collections:
- collection_type: open
  name: DefiLlama Public API
  slug: open-defillama
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/defillama-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defillama-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/defillama-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/defillama
- group: start
  title: ''
  type: Portal
  url: https://defillama.com/
- group: docs
  title: ''
  type: Documentation
  url: https://defillama.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://defillama.com/pro-api
- group: build
  title: ''
  type: GitHub
  url: https://github.com/DefiLlama
- group: commercial
  title: ''
  type: Plans
  url: plans/defillama-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/defillama-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/defillama-finops.yml
created: '2026-05-08'
description: DefiLlama is the largest open-source DeFi TVL and yield aggregator. It publishes a free public REST API (api.llama.fi) and a Pro API (pro-api.llama.fi) that adds higher rate limits and exclusive endpoints for token unlocks, bridges, digital-asset treasuries, and other advanced datasets. Free API requires no authentication; Pro is $300/month.
finops:
- name: Defillama Finops
  service_category: Crypto Analytics
  slug: defillama-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/defillama.png
layout: provider
modified: '2026-05-08'
name: DefiLlama
nav: Providers
network: true
overview: 'DefiLlama publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Coins API, Fees API, Stablecoins API, and 3 more. Tagged areas include Web3, DeFi, TVL, Crypto, and Stablecoins.


  DefiLlama''s developer surface includes authentication, developer portal, documentation, pricing, GitHub presence, and 6 more developer resources.'
plans:
- name: Defillama Plans Pricing
  plan_count: 2
  slug: defillama-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 2
  name: Defillama Rate Limits
  slug: defillama-rate-limits
score:
  band: thin
  composite: 37.1
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.8
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/defillama/refs/heads/main/screenshots/defillama-2026-06-20T175849.png
security:
- kind: authentication
  name: Defillama Authentication
  slug: defillama-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Defillama Domain Security
  slug: defillama-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: defillama
tags:
- Web3
- DeFi
- TVL
- Crypto
- Stablecoins
- Yields
- Bridges
- Aggregator
- Open Source
website: https://defillama.com/
---
