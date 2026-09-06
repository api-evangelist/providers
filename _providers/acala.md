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
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Acala EVM+ exposes a standard Ethereum JSON-RPC API through the EVM+ RPC Adapter, which wraps Substrate RPC calls to provide Ethereum execution-apis compatible endpoints (eth_*, net_*, web3_*) so Ethe
  name: Acala EVM+ JSON-RPC
  slug: acala-evm-json-rpc
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acala-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acala.network/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://evmdocs.acala.network/
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.acala.network/
- group: start
  title: ''
  type: GettingStarted
  url: https://evmdocs.acala.network/readme.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AcalaNetwork
- group: company
  title: ''
  type: Blog
  url: https://acala.network/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/5JJgXKSznc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acala.network/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://acala.network/terms-of-use
- group: build
  title: ''
  type: Packages
  url: packages/acala-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/acala-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acala-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/acala-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/acala-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acala-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/acala-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/acala-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/acala-conventions.yml
created: '2026-07-17'
description: Acala is the decentralized finance (DeFi) and liquidity hub of the Polkadot ecosystem, operating the Acala parachain (and its Kusama-based sister network Karura). Acala offers a scalable, Ethereum-compatible smart-contract platform called Acala EVM+, a decentralized stablecoin (aUSD), a liquid staking derivative (LDOT/LcDOT), and a trustless staking and swap layer. For developers, Acala EVM+ exposes a standard Ethereum JSON-RPC interface through its EVM+ RPC Adapter (eth-rpc-adapter), letting existing Ethereum dApps, wallets (MetaMask), and tooling (Hardhat, Remix, ethers.js, Truffle) interact with the Substrate-based chain with minimal changes, alongside a Substrate WebSocket RPC via the @acala-network Polkadot.js API and SDK packages.
image: https://acala.network/acala-og-card2.png
layout: provider
modified: '2026-07-17'
name: Acala
nav: Providers
network: true
overview: 'Acala publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Blockchain, DeFi, and Polkadot.


  Acala''s developer surface includes documentation, getting-started guide, engineering blog, support, sandbox, and 14 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 20.1
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acala/refs/heads/main/screenshots/acala-2026-07-25T181421.png
security:
- kind: domain-security
  name: Acala Domain Security
  slug: acala-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: acala
tags:
- Company
- Crypto
- Blockchain
- DeFi
- Polkadot
- Smart Contracts
- EVM
- Stablecoins
- JSON-RPC
- Web3
website: https://acala.network/
---
