---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The unified REST entry point for all crosschain operations on Across — request swap/bridge quotes and approval data, execute embedded crosschain actions on the destination chain, run gasless flows, en
  name: Across Swap API
  slug: across-swap-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/across-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://across.to
- group: docs
  title: ''
  type: Documentation
  url: https://docs.across.to
- group: docs
  title: ''
  type: APIReference
  url: https://docs.across.to/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.across.to/introduction
- group: company
  title: ''
  type: Blog
  url: https://across.to/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/across-protocol
- group: start
  title: ''
  type: SignUp
  url: https://docs.across.to/introduction/api-keys
- group: agent
  title: ''
  type: MCPServer
  url: mcp/across-mcp.yml
- group: build
  title: ''
  type: SDKs
  url: packages/across-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/across-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/across-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/across-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/across-conventions.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/across-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/across-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/across-trust-center.yml
created: '2026-07-17'
description: Across is a crosschain interoperability protocol powering fast, low-cost token transfers and swaps across 20+ EVM chains and Solana. Built on an intents-based design with a permissionless relayer network and UMA optimistic oracle settlement, Across fills crosschain transfers in roughly two seconds with no custodial risk. Developers integrate a single unified Swap API (plus embedded crosschain actions, gasless flows, and deposit tracking) to move native USDC, USDT, ETH, and other assets between Ethereum, Arbitrum, Base, Optimism, Polygon, Solana, and more. The protocol has facilitated over $36 billion in volume for 5M+ users. Across is a Paradigm portfolio company in the crypto-infrastructure sector.
image: https://across.to/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: across-mcp.yml
  slug: across-mcpyml
modified: '2026-07-17'
name: Across
nav: Providers
network: true
overview: 'Across publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Infrastructure, Cross Chain, Bridge, and Interoperability.


  Across'' developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, and 11 more developer resources.'
random_paper: 35
score:
  band: emerging
  composite: 26.4
  delta: -3.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 29.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/across/refs/heads/main/screenshots/across-2026-07-25T181521.png
security:
- kind: authentication
  name: Across Authentication
  slug: across-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Across Domain Security
  slug: across-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Across Vulnerability Disclosure
  slug: across-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Across Trust Center
  slug: across-trust-center
  summary_line: trust center published
slug: across
tags:
- Company
- Crypto Infrastructure
- Cross Chain
- Bridge
- Interoperability
- Blockchain
- DeFi
- Web3
- Swap
- Payments
website: https://across.to
---
