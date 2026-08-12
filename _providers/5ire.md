---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: Ethereum-compatible JSON-RPC 2.0 endpoint for the 5ireChain mainnet (EIP-155 chain ID 995, native currency 5ire, 18 decimals). Serves the standard eth_*, net_* and web3_* method families against the E
  name: 5ireChain Mainnet JSON-RPC
  slug: 5irechain-mainnet-json-rpc
- description: Ethereum-compatible JSON-RPC 2.0 endpoint for the 5ireChain Thunder testnet (EIP-155 chain ID 997, native currency T5IRE). Paired with a public faucet and a separate testnet block explorer, this is 5i
  name: 5ireChain Thunder Testnet JSON-RPC
  slug: 5irechain-thunder-testnet-json-rpc
- description: Substrate/Polkadot-SDK RPC surface of the 5ireChain node, reached over WebSocket (default port 9944) and consumed through the first-party @5ire/api JavaScript client, a fork of the Polkadot.js API. Th
  name: 5ireChain Native (Substrate) RPC
  slug: 5irechain-native-substrate-rpc
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/5ire-tech/5ireChain/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/5ire-tech/5ireChain/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/5ire-tech/5ireChain/blob/master/docs/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/5ire-tech/5ireChain/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://5ire.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.5ire.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.5ire.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.5ire.org/introduction-to-5irechain/
- group: company
  title: ''
  type: Blog
  url: https://5ire.medium.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://5ire.medium.com/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/5ire-tech
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/5ire-tech/5ireChain
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/5ire-tech/5ireChain/blob/master/docs/README.md
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/5ire
- group: company
  title: ''
  type: Twitter
  url: https://x.com/5ireChain
- group: other
  title: ''
  type: Telegram
  url: https://telegram.me/OfficialFireChain
- group: operate
  title: ''
  type: FAQ
  url: https://docs.5ire.org/faq/faq-list/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/5ire_stock/
- group: build
  title: ''
  type: Packages
  url: packages/5ire-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/5ire-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/5ire-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/5ire-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/5ire-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/5ire-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/5ire-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/5ire-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/5ire-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/5ire-domain-security.yml
created: '2026-08-02'
description: '5ire (5ireChain) is a layer-1, EVM-compatible smart contract blockchain built on the Polkadot SDK (Substrate), founded in 2021 and headquartered in Dubai with engineering in India. The chain positions sustainability as a first-class protocol concern: its Sustainable Proof of Stake / "Proof of 5ire" consensus scores validators against ESG data so block production and rewards are weighted by environmental and social performance, aligned to the UN Sustainable Development Goals. Developers reach the network through a standard Ethereum JSON-RPC endpoint (mainnet chain ID 995, Thunder testnet chain ID 997) using MetaMask, Hardhat, Foundry, Remix, wagmi and Ganache, or through the native Substrate/WASM side of the chain via the Polkadot-derived @5ire/api JavaScript client. Supporting surfaces include the 5irescan block explorer, a testnet faucet, validator and nominator applications, the 5ire wallet browser extension, and a 5ire IDE for contract deployment. 5ire has raised roughly
  USD 121M and trades on secondary private markets; it publishes no OpenAPI, AsyncAPI, MCP server or A2A agent card.'
image: https://avatars.githubusercontent.com/u/106282920?v=4
layout: provider
modified: '2026-08-02'
name: 5ire
nav: Providers
network: true
overview: '5ire publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include blockchain, layer-1, smart-contracts, evm, and web3.


  5ire''s developer surface includes documentation, getting-started guide, engineering blog, support, FAQ, sandbox, authentication, and 21 more developer resources.'
random_paper: 25
score:
  band: emerging
  composite: 23.7
  delta: -1.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 81.5
    governance: 3.1
    operational_transparency: 26.3
  previous_composite: 24.8
  provenance:
    conformance: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: 5Ire Authentication
  slug: 5ire-authentication
  summary_line: none · 3 schemes
- kind: domain-security
  name: 5Ire Domain Security
  slug: 5ire-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: 5ire
tags:
- blockchain
- layer-1
- smart-contracts
- evm
- web3
- substrate
- json-rpc
- sustainability
- esg
- proof-of-stake
- cryptocurrency
- developer-tools
website: https://5ire.org/
---
