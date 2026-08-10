---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Akash Network Agentic Access
  operation_count: 3
  slug: akash-network-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 11
apis:
- description: REST API for the managed Akash Console - deploy workloads with a managed wallet and credit-card billing, list and manage deployments, leases, and providers without needing to run a node or hold AKT di
  name: Akash Console API
  slug: console-api
- description: Indexed network data over REST - blocks, transactions, deployments, leases, providers, GPU availability, and marketplace stats. Used for analytics, provider discovery, and dashboards (the API powering
  name: Akash Network Data API
  slug: network-data-api
- description: Direct access to the Akash Cosmos-SDK chain over gRPC, REST (LCD), and Tendermint RPC. Used to query state, broadcast transactions, and stream events from a self-run or hosted Akash node.
  name: Akash Chain Node (gRPC / REST / RPC)
  slug: chain-grpc-rest-rpc
- description: HTTP API exposed by each Akash provider for lease management, manifest submission, log and event streaming, shell access, and service status. Used by tenants and tooling once a lease is established.
  name: Akash Provider API
  slug: provider-api
- description: Official Go SDK for the Akash chain - typed message types, client helpers for deployments, leases, and providers, AuthZ and fee-grant support, and the building blocks behind the akash CLI.
  name: Akash Blockchain SDK (Go)
  slug: sdk-go
- description: Official JavaScript / TypeScript SDK for building Akash applications and tooling - SDL parsing, wallet signing, deployment lifecycle, and lease management.
  name: Akashjs - Akash SDK (JavaScript / TypeScript)
  slug: sdk-js
- description: Reference command-line tool for the Akash network - keys, accounts, deployments, bids, leases, manifest send, and provider queries. Built on the Go SDK.
  name: Akash CLI
  slug: cli
- description: Hosted web console for browsing the marketplace, deploying SDL manifests, and managing leases - with optional managed wallet and credit-card billing.
  name: Akash Console (Web)
  slug: console
- description: Retrieve bids placed by Akash providers.
  name: Akash Network Bids API
  slug: akash-network-bids-api
- description: Create and manage SDL-based deployments.
  name: Akash Network Deployments API
  slug: akash-network-deployments-api
- description: Accept bids and manage leases with providers.
  name: Akash Network Leases API
  slug: akash-network-leases-api
artifact_total: 18
collections:
- collection_type: open
  name: Akash Console API
  slug: open-akash-network
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/akash-network-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akash-network-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/akash-network-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://akash.network/
- group: docs
  title: ''
  type: Documentation
  url: https://akash.network/docs/
- group: docs
  title: ''
  type: API Documentation
  url: https://akash.network/docs/api-documentation/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/akash-network
- group: start
  title: ''
  type: Console
  url: https://console.akash.network/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akash-network/
- group: company
  title: ''
  type: Blog
  url: https://akash.network/blog/
created: '2026-05-23'
description: Akash Network is a decentralized cloud marketplace for compute - including GPUs - built on a Cosmos-SDK chain settled in AKT. Tenants post deployment manifests (SDL) and providers bid to host them. Developer surface includes the Akash Console REST API with managed wallets and credit-card billing, the Network Data API for indexed chain and provider data, the underlying Cosmos-SDK chain accessible over gRPC / REST / RPC, the Provider API on each provider, an official Akash Blockchain SDK in Go and JavaScript/TypeScript, the Provider Console, and the akash CLI.
finops:
- name: Akash Network Finops
  service_category: API
  slug: akash-network-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/akash-network.png
layout: provider
modified: '2026-05-23'
name: Akash Network
nav: Providers
network: true
overview: 'Akash Network publishes 3 APIs on the [APIs.io](https://apis.io/) network: Bids API, Deployments API, and Leases API. Tagged areas include Decentralized Cloud, GPU, Compute, DePIN, and Cosmos.


  Akash Network''s developer surface includes authentication, documentation, GitHub presence, developer console, engineering blog, and 5 more developer resources.'
plans:
- name: Akash Network Plans Pricing
  plan_count: 1
  slug: akash-network-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 2
  name: Akash Network Rate Limits
  slug: akash-network-rate-limits
score:
  band: thin
  composite: 39.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 62.0
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/akash-network/refs/heads/main/screenshots/akash-network-2026-06-20T171449.png
security:
- kind: authentication
  name: Akash Network Authentication
  slug: akash-network-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Akash Network Domain Security
  slug: akash-network-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: akash-network
tags:
- Decentralized Cloud
- GPU
- Compute
- DePIN
- Cosmos
- Crypto
- Marketplace
website: https://akash.network/
---
