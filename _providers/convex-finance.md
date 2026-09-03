---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Subgraph-based GraphQL API for querying Convex Finance on-chain data including pools, deposits, withdrawals, revenue, and user activity via The Graph protocol.
  name: Convex Finance GraphQL API
  slug: convex-finance-graphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/convex-finance-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/@convexfinance
created: '2026-06-14'
description: Convex Finance is a DeFi protocol that boosts Curve Finance liquidity provider and CRV staker yields through its CVX token and pooled staking mechanism. It allows users to earn boosted CRV rewards and CVX without locking CRV directly.
graphqls:
- description: Convex Finance is a DeFi yield-boosting protocol built on top of Curve Finance. It allows liquidity providers and CRV stakers to earn boosted rewards via pooled CVX staking without individually lockin
  name: Convex Finance GraphQL API
  slug: convex-finance-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/convex-finance.png
layout: provider
modified: '2026-06-14'
name: Convex Finance
nav: Providers
network: true
overview: 'Convex Finance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include DeFi, Curve Finance, Yield Boosting, Liquidity Mining, and Ethereum.


  Convex Finance''s developer surface includes engineering blog and 1 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 31.9
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 18.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/convex-finance/refs/heads/main/screenshots/convex-finance-2026-07-25T210351.png
security:
- kind: domain-security
  name: Convex Finance Domain Security
  slug: convex-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: convex-finance
tags:
- DeFi
- Curve Finance
- Yield Boosting
- Liquidity Mining
- Ethereum
- GraphQL
- The Graph
website: https://www.convexfinance.com/
---
