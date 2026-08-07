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
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: 'Hosted public REST API (the block-explorer and faucet backend) exposing blocks, transactions, and network data with a list/object JSON envelope and cursor-style pagination. No authentication required '
  name: Iron Fish Public REST API
  slug: iron-fish-public-rest-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://ironfish.network/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ironfish.network/developers/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://ironfish.network/developers/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://ironfish.network/developers/documentation/integration_rpc
- group: start
  title: ''
  type: GettingStarted
  url: https://ironfish.network/developers/documentation/install-npm
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iron-fish
- group: company
  title: ''
  type: Blog
  url: https://ironfish.network/learn/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.ironfish.network/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ironfish.network/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ironfish.network/privacy-policy
- group: other
  title: ''
  type: Whitepaper
  url: https://ironfish.network/learn/whitepaper
- group: build
  title: ''
  type: Packages
  url: packages/iron-fish-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/iron-fish-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/iron-fish-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/iron-fish-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/iron-fish-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/iron-fish-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iron-fish-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iron-fish-domain-security.yml
created: '2026-07-17'
description: Iron Fish is a zero-knowledge Layer 1 blockchain that brings optional, best-in-class privacy to cryptocurrency. Built on zk-SNARK cryptography, it lets anyone send, receive, and bridge assets privately across 20+ EVM-compatible chains while running their own node. For developers, Iron Fish exposes a self-hosted node RPC server (over TCP, IPC, and HTTP with JSON and streaming responses) organized into chain, wallet, node, peer, miner, config, event, mempool, and worker namespaces, plus a hosted public REST API at api.ironfish.network powering the block explorer and faucet. Integration is supported by a first-party JavaScript SDK (@ironfish/sdk), Rust/Node bindings, and the ironfish CLI for node operation, wallet management, mining, and multisig. Backed by a16z and Electric Capital.
image: https://avatars.githubusercontent.com/u/43299557?v=4
layout: provider
modified: '2026-07-19'
name: Iron Fish
nav: Providers
network: true
overview: 'Iron Fish publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Cryptocurrency, Privacy, Zero Knowledge, and Layer 1.


  Iron Fish''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, authentication, and 12 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 28.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iron-fish/refs/heads/main/screenshots/iron-fish-2026-07-25T222911.png
security:
- kind: authentication
  name: Iron Fish Authentication
  slug: iron-fish-authentication
  summary_line: none · 2 schemes
- kind: domain-security
  name: Iron Fish Domain Security
  slug: iron-fish-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: iron-fish
tags:
- Blockchain
- Cryptocurrency
- Privacy
- Zero Knowledge
- Layer 1
- Web3
- RPC
- Wallet
website: https://ironfish.network/
---
