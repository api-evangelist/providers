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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: The primary JSON-RPC interface exposed by zcashd, the original Zcash full node. Backwards compatible with Bitcoin Core 0.11.2 with Zcash-specific extensions for shielded address management and private
  name: Zcash JSON-RPC API (zcashd)
  slug: zcash-json-rpc-api-zcashd
- description: The Zcash-specific extension to the JSON-RPC interface that enables shielded (private) transaction operations using zero-knowledge proofs. Includes methods for managing shielded addresses (z-addrs), s
  name: Zcash Payment API (z_ methods)
  slug: zcash-payment-api-z-methods
- description: A bandwidth-efficient gRPC service that provides a compact block streaming interface to the Zcash blockchain, enabling lightweight mobile and web wallet clients to sync shielded transactions without d
  name: Lightwalletd gRPC API
  slug: lightwalletd-grpc-api
- description: The JSON-RPC API provided by zebrad, the Zcash Foundation's independent Zcash full node implementation written in Rust. Designed to be a drop-in replacement for zcashd's RPC interface as zcashd is dep
  name: Zebra JSON-RPC API
  slug: zebra-json-rpc-api
artifact_total: 8
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/zcash/lightwalletd/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/zcash/lightwalletd/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/zcash/lightwalletd/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/zcash/lightwalletd/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/zcash/lightwalletd/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zcash-domain-security.yml
description: Zcash is a privacy-preserving cryptocurrency that uses zero-knowledge proofs (zk-SNARKs) to enable shielded transactions. It provides JSON-RPC APIs via zcashd and zebrad for wallet operations, shielded transaction management, blockchain data access, and network interaction.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://z.cash/wp-content/uploads/2022/01/zcash-icon-gold.png
layout: provider
modified: '2026-06-14'
name: Zcash
nav: Providers
network: true
overview: 'Zcash publishes 1 API on the [APIs.io](https://apis.io/) network: JSON-RPC API (zcashd). Tagged areas include Cryptocurrency, Privacy, Blockchain, Zero-Knowledge Proofs, and Shielded Transactions.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 12
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 60.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 9.5
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 21.1
  open_source:
    applies: true
    score: 65.0
  previous_composite: 31.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zcash/refs/heads/main/screenshots/zcash-2026-06-20T201803.png
security:
- kind: domain-security
  name: Zcash Domain Security
  slug: zcash-domain-security
  summary_line: TLSv1.3 · HSTS
slug: zcash
tags:
- Cryptocurrency
- Privacy
- Blockchain
- Zero-Knowledge Proofs
- Shielded Transactions
- ZEC
website: https://z.cash/
---
