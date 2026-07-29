---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lido Finance Agentic Access
  operation_count: 18
  slug: lido-finance-agentic-access
  summary_line: 18 operations
api_count: 8
apis:
- description: GraphQL subgraph deployed to The Graph Decentralized Network that indexes Lido smart-contract events — rewards distribution, oracle reports, stETH transfers and submissions, node operator keys — and e
  name: Lido Subgraph (GraphQL)
  slug: lido-subgraph
- description: The APR for Eth and stEth API from Lido Finance — 8 operation(s) for apr for eth and steth.
  name: Lido Finance APR for Eth and stEth API
  slug: lido-finance-apr-for-eth-and-steth-api
- description: The Estimate API from Lido Finance — 1 operation(s) for estimate.
  name: Lido Finance Estimate API
  slug: lido-finance-estimate-api
- description: The NFT API from Lido Finance — 2 operation(s) for nft.
  name: Lido Finance NFT API
  slug: lido-finance-nft-api
- description: The Request Time API from Lido Finance — 3 operation(s) for request time.
  name: Lido Finance Request Time API
  slug: lido-finance-request-time-api
- description: The Rewards API from Lido Finance — 1 operation(s) for rewards.
  name: Lido Finance Rewards API
  slug: lido-finance-rewards-api
- description: The Swap rate for stETH and wstETH API from Lido Finance — 2 operation(s) for swap rate for steth and wsteth.
  name: Lido Finance Swap rate for stETH and wstETH API
  slug: lido-finance-swap-rate-for-steth-and-wsteth-api
- description: The Validators API from Lido Finance — 1 operation(s) for validators.
  name: Lido Finance Validators API
  slug: lido-finance-validators-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://lido.fi/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lido.fi/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lido.fi/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lido.fi/integrations/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lido.fi/integrations/api
- group: company
  title: ''
  type: Blog
  url: https://blog.lido.fi/
- group: operate
  title: ''
  type: Support
  url: https://help.lido.fi/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.lido.fi/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lidofinance
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lido.fi/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lido.fi/privacy-notice
- group: start
  title: ''
  type: SignUp
  url: https://stake.lido.fi/
- group: operate
  title: ''
  type: Roadmap
  url: https://research.lido.fi/
- group: other
  title: ''
  type: Governance
  url: https://dao.lido.fi/
- group: auth
  title: ''
  type: Security
  url: https://immunefi.com/bug-bounty/lido/information/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lido-finance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/lido-finance-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lido-finance-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lido-finance-domain-security.yml
- group: other
  title: ''
  type: Audits
  url: https://github.com/lidofinance/audits
- group: build
  title: ''
  type: Packages
  url: packages/lido-finance-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lido-finance-packages.yml
- group: design
  title: ''
  type: Components
  url: components/lido-finance-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lido-finance-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lido-finance-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lido-finance-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lido-finance-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lido-finance-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lido-finance-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lido-finance-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lido-finance-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lido-finance-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lido-finance-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lido-finance-agentic-access.yml
created: '2026-07-17'
description: Lido is a liquid staking protocol for Ethereum, live since 2020, that lets holders stake ETH without running validator infrastructure and receive stETH — a rebasing ERC-20 liquid staking token that accrues staking rewards while remaining transferable and usable as collateral across DeFi. wstETH is the non-rebasing wrapped form. The protocol is governed by the Lido DAO and operated by a curated and permissionless (CSM) set of node operators, with on-chain accounting, oracles, a withdrawal queue, and staking vaults (stVaults) introduced in Lido V3. For developers, Lido publishes a set of strictly read-only public REST APIs — the Lido Ethereum API (protocol and stETH APR, prices, stats, swap rates), the Withdrawals API (withdrawal queue wait-time estimation, withdrawal NFT metadata, gas estimation, validator info), and the Reward History Backend (per-address stETH interactions and daily reward accounting) — alongside a GraphQL subgraph on The Graph, the Lido Ethereum SDK for TypeScript,
  a Python SDK, and a React UI component library.
image: https://lido.fi/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: lido-finance-mcp.yml
  slug: lido-finance-mcpyml
modified: '2026-07-19'
name: Lido Finance
nav: Providers
network: true
overview: 'Lido Finance publishes 7 APIs on the [APIs.io](https://apis.io/) network, including APR for Eth and stEth API, Estimate API, NFT API, and 4 more. Tagged areas include Company, Blockchain, Ethereum, Liquid Staking, and DeFi.


  Lido Finance''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 28 more developer resources.'
random_paper: 38
score:
  band: developing
  composite: 45.6
  delta: -1.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 38.1
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lido-finance/refs/heads/main/screenshots/lido-finance-2026-07-25T225027.png
security:
- kind: authentication
  name: Lido Finance Authentication
  slug: lido-finance-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lido Finance Domain Security
  slug: lido-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lido Finance Vulnerability Disclosure
  slug: lido-finance-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lido-finance
tags:
- Company
- Blockchain
- Ethereum
- Liquid Staking
- DeFi
- Cryptocurrency
- Staking
- Web3
- Financial Services
- GraphQL
website: https://lido.fi/
---
