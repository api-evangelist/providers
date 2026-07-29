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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.5
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Ethereum-compatible JSON-RPC 2.0 API (eth_*, net_*, web3_*) plus Morph-specific methods such as morph_getBlockByNumber that return additional L2 fields. No API key required; chain id 2818.
  name: Morph JSON-RPC API
  slug: morph-json-rpc-api
- description: Blockscout-based block explorer API for Morph — REST v2 and GraphQL over blocks, transactions, addresses, tokens, and verified contracts. No API key required.
  name: Morph Explorer API
  slug: morph-explorer-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.morphl2.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.morph.network/docs/build-on-morph/developer-navigation-page/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.morph.network/docs/build-on-morph/intro/
- group: docs
  title: ''
  type: APIReference
  url: https://explorer.morph.network/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.morph.network/docs/build-on-morph/build-on-morph/development-setup/
- group: company
  title: ''
  type: Blog
  url: https://morph.network/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/morph-l2
- group: auth
  title: ''
  type: Authentication
  url: authentication/morph-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/morph-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/morph-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/morph-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/morph-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/morph-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/morph-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/morph-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/morph-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/morph-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/morph-sandbox.yml
created: '2026-07-17'
description: Morph is an Optimistic zkEVM Ethereum Layer-2 blockchain (chain id 2818) focused on consumer-facing applications, backed by Pantera Capital. Its modular design combines a decentralized sequencer network with a Responsive Validity Proof system. Developers integrate with Morph through an Ethereum-compatible JSON-RPC API (rpc.morph.network) that adds Morph-specific methods, a Blockscout block explorer REST/GraphQL API (explorer-api.morph.network), the official @morph-l2/sdk JavaScript library, and an official AI Agent Skill and CLI (morph-l2/morph-skill) covering wallet operations, DEX swaps, cross-chain bridging, EIP-8004 agent identity and reputation, alternative-token gas payment, EIP-7702 delegation, and the x402 HTTP payment protocol.
image: https://morph.network/share/share-morph.jpeg
layout: provider
modified: '2026-07-20'
name: Morph
nav: Providers
network: true
overview: 'Morph publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Blockchain, Layer 2, and Ethereum.


  Morph''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, changelog, CLI, and 12 more developer resources.'
random_paper: 70
score:
  band: emerging
  composite: 26.6
  delta: -0.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 73.9
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 26.8
  provenance:
    conformance: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Morph Authentication
  slug: morph-authentication
  summary_line: none/jwt/wallet-signature · 4 schemes
- kind: domain-security
  name: Morph Domain Security
  slug: morph-domain-security
  summary_line: TLSv1.3 · DMARC
slug: morph
tags:
- Company
- Crypto
- Blockchain
- Layer 2
- Ethereum
- zkEVM
- Web3
- Developer Tools
website: https://www.morphl2.io/
---
