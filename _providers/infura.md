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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Infura Agentic Access
  operation_count: 1
  slug: infura-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
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
artifact_total: 17
asyncapis:
- description: AsyncAPI specification for Infura's (now MetaMask Developer Services) Ethereum-compatible WebSocket JSON-RPC subscription interface. Infura now defers its Ethereum reference documentation to the MetaM
  name: Infura (MetaMask Developer) WebSocket Subscription API
  slug: infura-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Infura (MetaMask Developer) JSON-RPC Infura (MetaMask Developer) JSON RPC API API
  slug: open-infura-infura-metamask-developer-json-rpc-api-api
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
random_paper: 15
rate_limits:
- limit_count: 4
  name: Infura Rate Limits
  slug: infura-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Infura API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: infura-asyncapi-spectral-rules
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 64.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 61.4
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
