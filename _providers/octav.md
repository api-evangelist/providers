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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.3
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Octav Agentic Access
  operation_count: 25
  slug: octav-agentic-access
  summary_line: 25 operations · 1 acting
api_count: 14
apis:
- description: Airdrop eligibility endpoints
  name: Octav Airdrops API
  slug: octav-airdrops-api
- description: Token approval endpoints
  name: Octav Approvals API
  slug: octav-approvals-api
- description: Ethereum beacon chain validator endpoints — details, rewards, withdrawals, and deposits (mainnet only)
  name: Octav Beacon Validators API
  slug: octav-beacon-validators-api
- description: Blockchain network and protocol endpoints
  name: Octav Chains API
  slug: octav-chains-api
- description: Resolve a contract address to its DeFi protocol
  name: Octav Contract Protocol API
  slug: octav-contract-protocol-api
- description: Credit balance endpoints
  name: Octav Credits API
  slug: octav-credits-api
- description: Net Asset Value endpoints
  name: Octav Nav API
  slug: octav-nav-api
- description: Portfolio and holdings endpoints
  name: Octav Portfolio API
  slug: octav-portfolio-api
- description: Status check endpoints
  name: Octav Status API
  slug: octav-status-api
- description: Data synchronization endpoints
  name: Octav Sync API
  slug: octav-sync-api
- description: Token data endpoints
  name: Octav Tokens API
  slug: octav-tokens-api
- description: Transaction history endpoints
  name: Octav Transactions API
  slug: octav-transactions-api
- description: Virtual user management and portfolio endpoints (Pro only)
  name: Octav Virtual Users API
  slug: octav-virtual-users-api
- description: Wallet information endpoints
  name: Octav Wallet API
  slug: octav-wallet-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/octav-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/octav-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/octav-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/octav-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/octav-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/octav-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/octav-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/octav-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/octav-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/octav-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/octav-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/octav-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/octav-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/octav-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/octav-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/octav-well-known.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/octav-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.octav.fi/docs/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.octav.fi
- group: docs
  title: ''
  type: Documentation
  url: https://docs.octav.fi
- group: docs
  title: ''
  type: APIReference
  url: https://docs.octav.fi/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.octav.fi/api/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.octav.fi/api/pricing
- group: start
  title: ''
  type: SignUp
  url: https://data.octav.fi
- group: commercial
  title: ''
  type: TermsOfService
  url: https://octav.fi/terms-of-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://octav.fi/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Octav-Labs
- group: operate
  title: ''
  type: Support
  url: https://docs.octav.fi/docs/contact-us
- group: company
  title: ''
  type: Website
  url: https://octav.fi
created: '2026-07-17'
description: Octav is a cryptocurrency portfolio intelligence platform that provides real-time, multi-chain portfolio data, transaction history, DeFi protocol positions, and historical snapshots across 65+ blockchain networks and 2M+ tokens. Its credit-based, read-only REST API lets developers and AI agents build portfolio dashboards, tax tools, NAV reporting, alerting, and analytics applications, with decoded DeFi positions (lending, LPs, staking, vaults, perps), Solana and EVM address support, Ethereum Beacon validator data, and drop-in migration guides from DeBank, Zerion, Zapper, Nansen, Covalent, and others. Octav is SOC 2 Type 1 & 2 certified and ships official MCP server, Rust CLI, and Agent Skill tooling. Backed by Speedinvest.
image: https://framerusercontent.com/images/mzciJN6fJmiKcfU39pZcq3Zn3z4.png
layout: provider
mcp_servers:
- description: ''
  name: octav-mcp.yml
  slug: octav-mcpyml
modified: '2026-07-20'
name: Octav
nav: Providers
network: true
overview: 'Octav publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Airdrops API, Approvals API, Beacon Validators API, and 11 more. Tagged areas include Company, Cryptocurrency, Blockchain, Portfolio, and DeFi.


  Octav''s developer surface includes authentication, CLI, changelog, documentation, API reference, getting-started guide, pricing, and 23 more developer resources.'
random_paper: 66
score:
  band: developing
  composite: 54.2
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 64.3
    developer_ergonomics: 71.7
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Octav Authentication
  slug: octav-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Octav Domain Security
  slug: octav-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: octav
tags:
- Company
- Cryptocurrency
- Blockchain
- Portfolio
- DeFi
- Analytics
- Web3
- Financial Data
- Wallet
website: https://octav.fi
---
