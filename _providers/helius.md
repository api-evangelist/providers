---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
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
  score: 40.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Helius Agentic Access
  operation_count: 31
  slug: helius-agentic-access
  summary_line: 31 operations · 16 acting
api_count: 7
apis:
- description: Solana JSON-RPC and WebSocket endpoints with enhanced WebSockets, archival data, and staked connections.
  name: Helius Solana RPC
  slug: rpc
- description: Solana JSON-RPC API for unified asset queries (compressed NFTs, regular NFTs, tokens) including getAsset, getAssetsByOwner, searchAssets.
  name: Helius Digital Asset Standard (DAS) API
  slug: das
- description: REST API for parsed and human-readable Solana transaction history with token metadata.
  name: Helius Enhanced Transactions API
  slug: enhanced-tx
- description: REST API for managing webhook subscriptions for Solana on-chain events with parsed transaction payloads.
  name: Helius Webhooks
  slug: webhooks
- description: Low-latency gRPC streaming of Solana account, slot, transaction, and block updates (Geyser-compatible).
  name: Helius LaserStream
  slug: laserstream
- description: Parallel transaction routing through Helius and Jito for inclusion latency optimization.
  name: Helius Sender
  slug: sender
- description: Indexed RPC for Solana ZK compression (compressed accounts).
  name: Helius Photon RPC (ZK Compression)
  slug: photon
artifact_total: 17
asyncapis:
- description: 'AsyncAPI 2.6 description of Helius''s real-time WebSocket interfaces for Solana. Coverage: * Standard Solana JSON-RPC PubSub subscriptions exposed by Helius RPC. * Helius enhanced subscriptions (transa'
  name: Helius WebSocket APIs
  slug: helius-asyncapi
collections:
- collection_type: open
  name: Helius API Catalog
  slug: open-helius
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/helius-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/helius-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/helius-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helius-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/helius-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/helius-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heliusapi
- group: company
  title: ''
  type: Website
  url: https://www.helius.dev/
- group: commercial
  title: ''
  type: Plans
  url: plans/helius-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/helius-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/helius-finops.yml
created: '2026-05-08'
description: Helius is a Solana developer platform offering Solana JSON-RPC, the Digital Asset Standard (DAS) API for NFTs/tokens, Enhanced Transactions, Webhooks, LaserStream gRPC streaming, Sender (transaction routing), Photon RPC, and Dedicated Nodes.
finops:
- name: Helius Finops
  service_category: Web3
  slug: helius-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-05-29'
name: Helius
nav: Providers
network: true
overview: 'Helius publishes 1 API on the [APIs.io](https://apis.io/) network: Solana RPC. Tagged areas include Web3, Blockchain, Solana, RPC, and DAS.


  The Helius catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Helius'' developer surface includes authentication and 10 more developer resources.'
plans:
- name: Helius Plans Pricing
  plan_count: 5
  slug: helius-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Helius Rate Limits
  slug: helius-rate-limits
rules:
- name: Helius API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: helius-asyncapi-spectral-rules
score:
  band: developing
  composite: 43.1
  delta: -6.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.5
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/helius/refs/heads/main/screenshots/helius-2026-06-20T182630.png
security:
- kind: authentication
  name: Helius Authentication
  slug: helius-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Helius Domain Security
  slug: helius-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Helius Vulnerability Disclosure
  slug: helius-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: helius
tags:
- Web3
- Blockchain
- Solana
- RPC
- DAS
- Streams
website: https://www.helius.dev/
---
