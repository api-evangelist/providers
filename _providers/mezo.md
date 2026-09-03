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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: EVM-compatible Ethereum JSON-RPC interface to the Mezo chain (eth_* methods) for reading chain state and submitting transactions. Mainnet EVM chain ID 31612, testnet 31611; BTC is the native gas token
  name: Mezo Chain EVM JSON-RPC
  slug: mezo-chain-evm-json-rpc
- description: Blockscout REST + JSON-RPC API for the Mezo chain explorer — blocks, transactions, addresses, tokens, and verified smart-contract data.
  name: Mezo Block Explorer API
  slug: mezo-block-explorer-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://mezo.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mezo.org/docs
- group: docs
  title: ''
  type: Documentation
  url: https://mezo.org/docs
- group: docs
  title: ''
  type: APIReference
  url: https://mezo.org/docs/developers/getting-started/configure-environment/
- group: start
  title: ''
  type: GettingStarted
  url: https://mezo.org/docs/developers/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/mezo
- group: company
  title: ''
  type: Blog
  url: https://mezo.org/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mezo-org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mezo.org/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mezo.org/legal/privacy
- group: start
  title: ''
  type: SignUp
  url: https://mezo.org/explore
- group: operate
  title: ''
  type: StatusPage
  url: https://monitoring.mezo.org/grafana/public-dashboards/ce8d1e04916244b0908cb967b8530f5f
- group: other
  title: ''
  type: Explorer
  url: https://explorer.mezo.org
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mezo-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/mezo-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mezo-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mezo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://mezo.org/SECURITY.md
- group: build
  title: ''
  type: Packages
  url: packages/mezo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mezo-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/mezo-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mezo-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mezo-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mezo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mezo-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mezo-changelog.yml
created: '2026-07-17'
description: 'Mezo is Bitcoin''s economic layer — a Cosmos SDK-based appchain with full EVM compatibility, built by Thesis (creators of tBTC, Fold, and Taho). It lets Bitcoiners borrow, lend, spend, save, and earn yield without selling their BTC: BTC is used natively for gas, tBTC provides reliable bridging, and MUSD is a Bitcoin-backed stablecoin pegged 1:1 to the U.S. dollar. The chain runs the mezod reference client (forked from Evmos) on CometBFT consensus with a dual-staking model, and exposes Ethereum JSON-RPC, Cosmos REST/gRPC + CometBFT RPC, and a Blockscout explorer API. Developers deploy Solidity contracts with Hardhat or Foundry against mainnet EVM chain ID 31612 and testnet 31611, and can accept MUSD payments over the x402 (HTTP 402) protocol.'
image: https://avatars.githubusercontent.com/u/175807022?v=4
layout: provider
modified: '2026-07-20'
name: Mezo
nav: Providers
network: true
overview: 'Mezo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Web3, Blockchain, Bitcoin, and DeFi.


  Mezo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 19 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 32.7
  provenance:
    conformance: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mezo/refs/heads/main/screenshots/mezo-2026-08-07T172807.png
security:
- kind: domain-security
  name: Mezo Domain Security
  slug: mezo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Mezo Vulnerability Disclosure
  slug: mezo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mezo
tags:
- Company
- Crypto Web3
- Blockchain
- Bitcoin
- DeFi
- EVM
- Cosmos SDK
- Stablecoins
- JSON-RPC
- Layer 2
website: https://mezo.org
---
