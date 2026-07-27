---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 33.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: 'Public gRPC-Web / REST gateway (sgn.gateway.v1.Web) for the cBridge cross-chain bridge: chain and token discovery, transfer fee estimation, transfer status, transfer history, and signed liquidity with'
  name: cBridge Gateway API
  slug: cbridge-gateway-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.celer.network/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cbridge-docs.celer.network/developer/cbridge-sdk
- group: docs
  title: ''
  type: Documentation
  url: https://cbridge-docs.celer.network/developer/cbridge-sdk
- group: docs
  title: ''
  type: APIReference
  url: https://cbridge-docs.celer.network/developer/cbridge-sdk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/celer-network
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/Trhab5w
- group: other
  title: ''
  type: Protobuf
  url: grpc/celer-network-gateway.proto
- group: build
  title: ''
  type: Packages
  url: packages/celer-network-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/celer-network-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/celer-network-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/celer-network-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/celer-network-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/celer-network-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/celer-network-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/celer-network-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/celer-network-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/celer-network-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/celer-network-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/celer-network-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://immunefi.com/bounty/celer/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Celer Network is a blockchain interoperability protocol that enables seamless cross-chain experiences for dApps, assets, and users. Its flagship cBridge is a decentralized cross-chain asset bridge supporting 40+ blockchains with over $14B in cumulative transfer volume, and Celer IM (Inter-chain Messaging) is a framework for building multi-blockchain applications with efficient liquidity, coherent logic, and shared state. For developers, the cBridge gateway exposes a public gRPC-Web / REST API (sgn.gateway.v1.Web) for discovering supported chains and tokens, estimating cross-chain transfer fees, tracking transfer status, and withdrawing liquidity. Celer was surfaced as a portfolio company of Pantera Capital.
image: https://www.celer.network/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: celer-network-mcp.yml
  slug: celer-network-mcpyml
modified: '2026-07-18'
name: Celer Network
nav: Providers
network: true
overview: 'Celer Network publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Blockchain, Interoperability, and Cross-Chain.


  Celer Network''s developer surface includes documentation, API reference, support, authentication, and 17 more developer resources.'
random_paper: 54
score:
  band: emerging
  composite: 23.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 23.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/celer-network/refs/heads/main/screenshots/celer-network-2026-07-25T204846.png
security:
- kind: authentication
  name: Celer Network Authentication
  slug: celer-network-authentication
  summary_line: none/signature · 2 schemes
- kind: domain-security
  name: Celer Network Domain Security
  slug: celer-network-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Celer Network Vulnerability Disclosure
  slug: celer-network-vulnerability-disclosure
  summary_line: contact published
slug: celer-network
tags:
- Company
- Crypto
- Blockchain
- Interoperability
- Cross-Chain
- Bridge
- DeFi
- Web3
website: https://www.celer.network/
---
