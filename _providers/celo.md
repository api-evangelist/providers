---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Ethereum-compatible JSON-RPC API for the Celo Layer 2 network, served over the public Forno endpoints. Supports the standard eth_* / net_* / web3_* method set for reading chain state, submitting trans
  name: Celo JSON-RPC API
  slug: celo-json-rpc-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://celo.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.celo.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.celo.org
- group: docs
  title: ''
  type: APIReference
  url: https://docs.celo.org/build-on-celo/network-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.celo.org/build-on-celo/quickstart
- group: company
  title: ''
  type: Blog
  url: https://blog.celo.org
- group: operate
  title: ''
  type: Support
  url: https://forum.celo.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/celo-org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://celo.org/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://celo.org/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.celo.org
- group: build
  title: ''
  type: Packages
  url: packages/celo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/celo-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/celo-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/celo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/celo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/celo-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/celo-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/celo-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/celo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://celo.org/.well-known/security.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/celo-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/celo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/celo-conformance.yml
created: '2026-07-17'
description: Celo is a leading Ethereum Layer 2 (L2) blockchain built for real-world usage, mobile-first payments, and stablecoins, run by cLabs and the Celo Foundation. It offers a fully EVM- and Ethereum-JSON-RPC-compatible network reachable through the public Forno RPC endpoints, gas-fee abstraction that lets users pay fees in stablecoins, and a developer stack spanning TypeScript SDKs (ContractKit, @celo/connect, @celo/abis, @celo/identity), the Celo Composer CLI scaffolding tool, a published Model Context Protocol (MCP) server for AI agents, and agent-payment protocols (x402, MPP, ERC-8004). Developers build dApps, MiniPay mini-apps, DeFi, and AI agents against the Celo Mainnet (chain 42220) and the Celo Sepolia testnet.
image: https://framerusercontent.com/assets/vn0V92oZLFWJWDd5ypiVsqJilg.png
layout: provider
mcp_servers:
- description: 'Model Context Protocol server providing AI assistants and IDEs comprehensive access to the Celo blockchain: blockchain data, token operations, NFTs, smart contracts, transactions, and governance. Publ'
  name: Celo MCP Server
  slug: celo-mcp-server
modified: '2026-07-18'
name: Celo
nav: Providers
network: true
overview: 'Celo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Ethereum L2, Web3, and Stablecoins.


  Celo''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, and 18 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 28.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/celo/refs/heads/main/screenshots/celo-2026-07-25T204901.png
security:
- kind: domain-security
  name: Celo Domain Security
  slug: celo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Celo Vulnerability Disclosure
  slug: celo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: celo
tags:
- Company
- Blockchain
- Ethereum L2
- Web3
- Stablecoins
- Payments
- JSON-RPC
- Smart Contracts
- AI Agents
- Developer Tools
website: https://celo.org
---
