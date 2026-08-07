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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: GraphQL API for querying Compound Finance v2 protocol data via The Graph subgraph, including markets, accounts, borrows, repays, liquidations, and token transfers.
  name: Compound Finance GraphQL API
  slug: compound-finance-graphql-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/compound-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/compound-domain-security.yml
created: '2026-06-14'
description: Compound is a decentralized, blockchain-based protocol that allows users to lend and borrow cryptocurrencies (DeFi lending protocol) built on Ethereum.
graphqls:
- description: Compound Finance is a decentralized, blockchain-based DeFi lending protocol built on Ethereum. It allows users to supply assets to earn interest or borrow assets against supplied collateral. The proto
  name: Compound Finance GraphQL API
  slug: compound-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/compound.png
layout: provider
modified: '2026-06-14'
name: Compound Finance
nav: Providers
network: true
overview: Compound Finance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include DeFi, Lending, Borrowing, Ethereum, and Blockchain.
random_paper: 78
score:
  band: emerging
  composite: 16.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 42.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/compound/refs/heads/main/screenshots/compound-2026-06-20T174841.png
security:
- kind: domain-security
  name: Compound Domain Security
  slug: compound-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Compound Vulnerability Disclosure
  slug: compound-vulnerability-disclosure
  summary_line: disclosure policy published
slug: compound
tags:
- DeFi
- Lending
- Borrowing
- Ethereum
- Blockchain
- Finance
- Cryptocurrency
---
