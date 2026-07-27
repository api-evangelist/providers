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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Infura Agentic Access
  operation_count: 1
  slug: infura-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 6
apis:
- description: Multi-chain JSON-RPC over HTTPS and WebSockets across 23+ networks (Ethereum, Linea, Polygon, Arbitrum, Optimism, Base, Avalanche, BNB, Scroll, Mantle, Blast, Starknet, etc.).
  name: Infura JSON-RPC API
  slug: json-rpc
- description: Solana JSON-RPC and WebSocket endpoints.
  name: Infura Solana JSON-RPC
  slug: solana-rpc
- description: REST API for EIP-1559 gas estimation, gas prices, and base-fee history across supported chains.
  name: Infura Gas API
  slug: gas-api
- description: REST API for pinning and retrieving content on IPFS.
  name: Infura IPFS API
  slug: ipfs
- description: REST API for NFT metadata, ownership, and collection data on EVM chains.
  name: Infura NFT API
  slug: nft-api
- description: The Infura (MetaMask Developer) JSON RPC API API from Infura — 1 operation(s) for infura (metamask developer) json rpc api.
  name: Infura Infura (MetaMask Developer) JSON RPC API API
  slug: infura-infura-metamask-developer-json-rpc-api-api
artifact_total: 15
asyncapis:
- description: AsyncAPI specification for Infura's (now MetaMask Developer Services) Ethereum-compatible WebSocket JSON-RPC subscription interface. Infura now defers its Ethereum reference documentation to the MetaM
  name: Infura (MetaMask Developer) WebSocket Subscription API
  slug: infura-asyncapi
collections:
- collection_type: open
  name: Infura (MetaMask Developer) JSON-RPC API
  slug: open-infura
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/infura-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infura-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/infura-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/INFURA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/infuraio
- group: company
  title: ''
  type: Website
  url: https://www.infura.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/infura-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/infura-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/infura-finops.yml
created: '2026-05-08'
description: Infura (now MetaMask Developer) is a Web3 RPC provider operated by ConsenSys/MetaMask offering JSON-RPC and REST APIs for 23+ blockchain networks including Ethereum, Linea, Polygon, Arbitrum, Optimism, Base, Avalanche, BNB, Solana, Starknet, plus IPFS and a Gas API. Backed by the Decentralized Infrastructure Network (DIN) for failover.
finops:
- name: Infura Finops
  service_category: Web3
  slug: infura-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/infura.png
layout: provider
modified: '2026-05-29'
name: Infura
nav: Providers
network: true
overview: 'Infura publishes 2 APIs on the [APIs.io](https://apis.io/) network: JSON-RPC API and Infura (MetaMask Developer) JSON RPC API API. Tagged areas include Web3, Blockchain, RPC, Infrastructure, and MetaMask.


  The Infura catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Infura''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: Infura Plans Pricing
  plan_count: 4
  slug: infura-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 4
  name: Infura Rate Limits
  slug: infura-rate-limits
rules:
- name: Infura API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: infura-asyncapi-spectral-rules
score:
  band: developing
  composite: 49.0
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.4
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 60.5
    operational_transparency: 36.8
  previous_composite: 45.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infura/refs/heads/main/screenshots/infura-2026-06-20T183349.png
security:
- kind: authentication
  name: Infura Authentication
  slug: infura-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Infura Domain Security
  slug: infura-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: infura
tags:
- Web3
- Blockchain
- RPC
- Infrastructure
- MetaMask
- ConsenSys
website: https://www.infura.io/
---
