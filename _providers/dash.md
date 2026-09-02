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
  band: human-only
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Open-source REST and WebSocket API for querying the Dash Core (layer 1) blockchain. Provides endpoints for blocks (by hash or height), raw blocks, transactions (by txid), raw transactions, addresses (
  name: Dash Insight REST API
  slug: dash-insight-rest-api
- description: Decentralized HTTP API exposing gRPC and JSON-RPC endpoints for both Dash Core layer 1 and Dash Platform layer 2 (DashPay). Core gRPC endpoints cover broadcastTransaction, getBestBlockHeight, getBlock
  name: Dash Platform DAPI (Decentralized API)
  slug: dash-platform-dapi-decentralized-api
artifact_total: 7
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/dashpay/insight-api/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dash-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dash.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dash.org/en/stable/developers/
- group: docs
  title: ''
  type: PlatformDocumentation
  url: https://docs.dash.org/projects/platform/en/stable/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dashpay
- group: other
  title: ''
  type: BlockExplorer
  url: https://explorer.dash.org/insight/
- group: commercial
  title: ''
  type: Plans
  url: plans/dash-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dash-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dash-finops.yml
created: '2026-06-14'
description: Dash is a peer-to-peer cryptocurrency network offering fast, low-cost payments with InstantSend, privacy via CoinJoin mixing, and decentralized governance through Masternodes. Developers can query blocks, transactions, addresses, UTXOs, governance objects, and real-time network events through the open-source Insight REST and WebSocket API, and can access Dash Platform layer-2 (DashPay identity, data contracts, documents, tokens) through the Decentralized API (DAPI) over gRPC and JSON-RPC.
finops:
- name: Dash Finops
  service_category: Cryptocurrency Network & Data APIs
  slug: dash-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dash.png
jsonld:
- class_count: 0
  name: Dash Context
  property_count: 0
  slug: dash
layout: provider
modified: '2026-06-14'
name: Dash
nav: Providers
network: true
overview: 'Dash publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Blockchain, DASH, InstantSend, and Masternode.


  The Dash catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Dash Plans Pricing
  plan_count: 2
  slug: dash-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Dash Rate Limits
  slug: dash-rate-limits
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 50.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 21.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dash/refs/heads/main/screenshots/dash-2026-06-20T175502.png
security:
- kind: domain-security
  name: Dash Domain Security
  slug: dash-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dash
tags:
- Cryptocurrency
- Blockchain
- DASH
- InstantSend
- Masternode
- DashPay
- Governance
- Payments
website: https://www.dash.org
---
