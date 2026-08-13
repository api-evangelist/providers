---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Yearn Agentic Access
  operation_count: 9
  slug: yearn-agentic-access
  summary_line: 9 operations
api_count: 5
apis:
- description: An integrated indexing service and GraphQL API providing comprehensive data on Yearn V2 and V3 vault ecosystems, including contract snapshots, event histories, vault-strategy relationships, fees, rewa
  name: Kong GraphQL API
  slug: kong-graphql-api
- description: Supported blockchain network information
  name: Yearn Finance Chains API
  slug: yearn-chains-api
- description: Protocol information and metadata
  name: Yearn Finance Info API
  slug: yearn-info-api
- description: Total Value Locked metrics
  name: Yearn Finance TVL API
  slug: yearn-tvl-api
- description: Endpoints for querying Yearn vault data
  name: Yearn Finance Vaults API
  slug: yearn-vaults-api
artifact_total: 14
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/yearn/kong/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yearn-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yearn-domain-security.yml
description: Yearn Finance is a DeFi yield aggregator that automates yield farming strategies across EVM-compatible networks. It provides REST and GraphQL APIs for accessing vault data, APY rates, strategy information, user positions, TVL metrics, and protocol analytics across Ethereum, Optimism, Polygon, Fantom, Base, and Arbitrum.
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: Yearn Finance's Kong GraphQL API is an integrated indexing and querying service that provides comprehensive on-chain data for Yearn V2 and V3 vault ecosystems. It exposes vault snapshots, strategy dat
  name: Yearn Finance GraphQL API
  slug: yearn-graphql
image: https://yearn.fi/logo.svg
json_schemas:
- name: Vault
  property_count: 22
  slug: vault
jsonld:
- class_count: 37
  name: context Context
  property_count: 11
  slug: context
layout: provider
modified: 2026-06-13
name: Yearn Finance
nav: Providers
network: true
overview: 'Yearn Finance publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chains API, Info API, TVL API, and 1 more. Tagged areas include DeFi, Yield Aggregator, Vaults, EVM, and Web3.


  The Yearn Finance catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 63
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Yearn Finance API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: yearn-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 66.4
    developer_ergonomics: 0.0
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yearn/refs/heads/main/screenshots/yearn-2026-06-20T201735.png
security:
- kind: domain-security
  name: Yearn Domain Security
  slug: yearn-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: yearn
tags:
- DeFi
- Yield Aggregator
- Vaults
- EVM
- Web3
- Blockchain
- Finance
website: https://yearn.fi
---
