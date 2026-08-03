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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Blockchair Agentic Access
  operation_count: 16
  slug: blockchair-agentic-access
  summary_line: 16 operations · 1 acting
api_count: 7
apis:
- description: Per-address balance and transaction dashboards.
  name: Blockchair Address Dashboards API
  slug: blockchair-address-dashboards-api
- description: Parsed block dashboards.
  name: Blockchair Block Dashboards API
  slug: blockchair-block-dashboards-api
- description: Signed transaction broadcasting.
  name: Blockchair Broadcast API
  slug: blockchair-broadcast-api
- description: SQL-like database query interface.
  name: Blockchair Outputs Database API
  slug: blockchair-outputs-database-api
- description: Raw node-level block and transaction data.
  name: Blockchair Raw Data API
  slug: blockchair-raw-data-api
- description: Network and chain statistics.
  name: Blockchair Stats API
  slug: blockchair-stats-api
- description: Parsed transaction dashboards.
  name: Blockchair Transaction Dashboards API
  slug: blockchair-transaction-dashboards-api
artifact_total: 14
collections:
- collection_type: open
  name: Blockchair API
  slug: open-blockchair
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blockchair-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blockchair-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blockchair-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Blockchair
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blockchair
- group: company
  title: ''
  type: Website
  url: https://blockchair.com
- group: docs
  title: ''
  type: Documentation
  url: https://blockchair.com/api/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/blockchair-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/blockchair-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/blockchair-finops.yml
created: '2026-06-21'
description: Blockchair is a multi-blockchain explorer and data API providing unified access to on-chain data across 40+ blockchains (Bitcoin, Ethereum, Litecoin, Dogecoin, Ripple, Stellar, Monero, Cardano, and more). The REST API at api.blockchair.com exposes per-chain dashboards (address, transaction, block), raw node data, network stats, a SQL-like database query interface over outputs and other tables, and transaction broadcasting, authenticated with a simple key query parameter.
finops:
- name: Blockchair Finops
  service_category: Blockchain and Web3
  slug: blockchair-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blockchair.png
layout: provider
modified: '2026-06-21'
name: Blockchair
nav: Providers
network: true
overview: 'Blockchair publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Address Dashboards API, Block Dashboards API, Broadcast API, and 4 more. Tagged areas include Blockchain, Cryptocurrency, Explorer, Bitcoin, and Ethereum.


  Blockchair''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Blockchair Plans Pricing
  plan_count: 6
  slug: blockchair-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 5
  name: Blockchair Rate Limits
  slug: blockchair-rate-limits
score:
  band: thin
  composite: 38.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.1
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Blockchair Authentication
  slug: blockchair-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Blockchair Domain Security
  slug: blockchair-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: blockchair
tags:
- Blockchain
- Cryptocurrency
- Explorer
- Bitcoin
- Ethereum
- On-Chain Data
website: https://blockchair.com
---
