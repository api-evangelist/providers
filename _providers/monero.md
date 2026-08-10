---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Monero Agentic Access
  operation_count: 17
  slug: monero-agentic-access
  summary_line: 17 operations · 17 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: Blockchain data and block operations
  name: Monero Blockchain API
  slug: monero-blockchain-api
- description: JSON-RPC 2.0 dispatch endpoint
  name: Monero JSON-RPC API
  slug: monero-json-rpc-api
- description: Mining control and block template operations
  name: Monero Mining API
  slug: monero-mining-api
- description: Peer and network management
  name: Monero Network API
  slug: monero-network-api
- description: Node status and info
  name: Monero Node Info API
  slug: monero-node-info-api
- description: Output and key image operations
  name: Monero Outputs API
  slug: monero-outputs-api
- description: Mempool / transaction pool operations
  name: Monero Transaction Pool API
  slug: monero-transaction-pool-api
- description: Transaction submission and lookup
  name: Monero Transactions API
  slug: monero-transactions-api
artifact_total: 16
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/monero-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getmonero.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getmonero.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.getmonero.org/resources/developer-guides/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/monero-project
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/monero-project/monero
- group: build
  title: ''
  type: GitHubEcosystem
  url: https://github.com/monero-ecosystem
- group: operate
  title: ''
  type: StackOverflow
  url: https://monero.stackexchange.com
- group: operate
  title: ''
  type: Forums
  url: https://forum.getmonero.org/
- group: other
  title: ''
  type: IRC
  url: https://matrix.to/#/#monero:libera.chat
- group: company
  title: ''
  type: Blog
  url: https://www.getmonero.org/blog/
- group: other
  title: ''
  type: ResearchLab
  url: https://www.getmonero.org/resources/research-lab/
- group: other
  title: ''
  type: Downloads
  url: https://www.getmonero.org/downloads/
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/monero/refs/heads/main/json-schema/monero-types.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/monero/refs/heads/main/json-ld/monero-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/monero/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/monero/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/monero/refs/heads/main/finops/finops.yml
created: '2026-06-14'
description: Monero is a privacy-focused, decentralized cryptocurrency providing JSON-RPC APIs for wallet management, transaction creation, mining coordination, and blockchain data access on the Monero (XMR) network. The daemon RPC exposes node and chain operations while the wallet RPC provides comprehensive wallet and transfer management.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/monero.png
json_schemas:
- name: Monero API Types
  property_count: 0
  slug: monero-types
jsonld:
- class_count: 10
  name: Monero Context
  property_count: 49
  slug: monero-context
layout: provider
modified: '2026-06-14'
name: Monero
nav: Providers
network: true
overview: 'Monero publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Blockchain API, JSON-RPC API, Mining API, and 5 more. Tagged areas include Cryptocurrency, Privacy, Blockchain, JSON-RPC, and Wallet.


  The Monero catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Monero''s developer surface includes documentation, Stack Overflow tag, engineering blog, and 16 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 76
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Monero API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: monero-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.4
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monero/refs/heads/main/screenshots/monero-2026-06-20T185722.png
security:
- kind: domain-security
  name: Monero Domain Security
  slug: monero-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: monero
tags:
- Cryptocurrency
- Privacy
- Blockchain
- JSON-RPC
- Wallet
- Mining
- Transactions
website: https://www.getmonero.org/
---
