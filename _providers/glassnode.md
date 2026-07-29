---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
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
  name: Glassnode Agentic Access
  operation_count: 14
  slug: glassnode-agentic-access
  summary_line: 14 operations
api_count: 13
apis:
- description: Time-series API for thousands of on-chain and market metrics across major crypto assets. Endpoints follow /v1/metrics/{category}/{name} pattern. Data is updated daily, hourly, or 10-minute depending o
  name: Glassnode Metrics API
  slug: metrics-api
- description: The Addresses API from Glassnode — 1 operation(s) for addresses.
  name: Glassnode Addresses API
  slug: glassnode-addresses-api
- description: The Derivatives API from Glassnode — 1 operation(s) for derivatives.
  name: Glassnode Derivatives API
  slug: glassnode-derivatives-api
- description: The Distribution API from Glassnode — 1 operation(s) for distribution.
  name: Glassnode Distribution API
  slug: glassnode-distribution-api
- description: The Indicators API from Glassnode — 1 operation(s) for indicators.
  name: Glassnode Indicators API
  slug: glassnode-indicators-api
- description: The Macro API from Glassnode — 1 operation(s) for macro.
  name: Glassnode Macro API
  slug: glassnode-macro-api
- description: The Market API from Glassnode — 1 operation(s) for market.
  name: Glassnode Market API
  slug: glassnode-market-api
- description: The Metadata API from Glassnode — 3 operation(s) for metadata.
  name: Glassnode Metadata API
  slug: glassnode-metadata-api
- description: The Options API from Glassnode — 1 operation(s) for options.
  name: Glassnode Options API
  slug: glassnode-options-api
- description: The Supply API from Glassnode — 1 operation(s) for supply.
  name: Glassnode Supply API
  slug: glassnode-supply-api
- description: The Transactions API from Glassnode — 1 operation(s) for transactions.
  name: Glassnode Transactions API
  slug: glassnode-transactions-api
- description: The Treasuries API from Glassnode — 1 operation(s) for treasuries.
  name: Glassnode Treasuries API
  slug: glassnode-treasuries-api
- description: The User API from Glassnode — 1 operation(s) for user.
  name: Glassnode User API
  slug: glassnode-user-api
artifact_total: 20
collections:
- collection_type: open
  name: Glassnode Metrics API
  slug: open-glassnode
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/glassnode-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glassnode-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/glassnode-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/glassnode
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/glassnode
- group: start
  title: ''
  type: Portal
  url: https://glassnode.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.glassnode.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://studio.glassnode.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/glassnode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/glassnode-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/glassnode-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.glassnode.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://research.glassnode.com/feed
created: '2026-05-08'
description: Glassnode provides on-chain analytics, market intelligence, and thousands of curated metrics covering Bitcoin, Ethereum, and other major chains. The Glassnode API serves time-series data for price, supply, addresses, transactions, derivatives, mining, market indicators, and proprietary signals (e.g. SOPR, MVRV, NUPL). Authentication uses an X-Api-Key header. API access requires an institutional plan or paid add-on.
finops:
- name: Glassnode Finops
  service_category: Crypto Analytics
  slug: glassnode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glassnode.png
layout: provider
modified: '2026-05-08'
name: Glassnode
nav: Providers
network: true
overview: 'Glassnode publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Derivatives API, Distribution API, and 9 more. Tagged areas include Web3, Crypto, On-Chain, Analytics, and Metrics.


  Glassnode''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Glassnode Plans Pricing
  plan_count: 4
  slug: glassnode-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Glassnode Rate Limits
  slug: glassnode-rate-limits
score:
  band: thin
  composite: 40.3
  delta: -2.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 53.4
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 42.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glassnode/refs/heads/main/screenshots/glassnode-2026-06-20T181914.png
security:
- kind: authentication
  name: Glassnode Authentication
  slug: glassnode-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Glassnode Domain Security
  slug: glassnode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: glassnode
tags:
- Web3
- Crypto
- On-Chain
- Analytics
- Metrics
- Bitcoin
- Ethereum
- Institutional
website: https://glassnode.com/
---
