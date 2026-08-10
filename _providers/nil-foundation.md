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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: 'Ethereum-style JSON-RPC 2.0 API exposing the =nil; cluster — blocks, transactions (messages), accounts, contract calls, gas pricing, shard enumeration, tokens, and event filters. Read methods require '
  name: =nil; JSON-RPC API
  slug: nil-json-rpc-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nil-foundation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nil.foundation
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nil.foundation/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nil.foundation/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nil.foundation/nil/references/json-rpc-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nil.foundation/nil/getting-started/prerequisites/
- group: company
  title: ''
  type: Blog
  url: https://nil.foundation/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NilFoundation
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nil.foundation/pages/privacy-policy
- group: build
  title: ''
  type: SDKs
  url: packages/nil-foundation-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/nil-foundation-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nil-foundation-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nil-foundation-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nil-foundation-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/nil-foundation-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nil-foundation-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/nil-foundation-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nil-foundation-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nil-foundation-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nil-foundation-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.nil.foundation/nil/migration-guides/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nil-foundation-changelog.yml
created: '2026-07-17'
description: =nil; Foundation is the developer of =nil;, an Ethereum Layer 2 blockchain powered by zkSharding that delivers horizontal scalability with built-in cross-shard communication and zero-knowledge proofs. On =nil; all accounts are smart contracts (no EOAs), state is partitioned across execution shards, and correctness is verified with zk proofs while Ethereum provides data availability and consensus. Developers build with Solidity smart contracts and interact with the cluster through an Ethereum-style JSON-RPC 2.0 API, the @nilfoundation/niljs TypeScript client library, the =nil; CLI, and a Hardhat plugin. =nil; Foundation also develops zkLLVM (a zero-knowledge proof circuit compiler) and the Placeholder proof system with an in-EVM verifier. The company is a portfolio company of Polychain Capital.
image: https://nil.foundation/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: nil-foundation-mcp.yml
  slug: nil-foundation-mcpyml
modified: '2026-07-20'
name: =nil; Foundation
nav: Providers
network: true
overview: '=nil; Foundation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Zk Infrastructure, Blockchain, Layer 2, and Ethereum.


  =nil; Foundation''s developer surface includes documentation, API reference, getting-started guide, engineering blog, CLI, authentication, changelog, and 15 more developer resources.'
random_paper: 55
score:
  band: emerging
  composite: 26.4
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 63.0
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 28.9
  previous_composite: 26.4
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nil-foundation/refs/heads/main/screenshots/nil-foundation-2026-08-07T185257.png
security:
- kind: authentication
  name: Nil Foundation Authentication
  slug: nil-foundation-authentication
  summary_line: none/signature · 2 schemes
- kind: domain-security
  name: Nil Foundation Domain Security
  slug: nil-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nil-foundation
tags:
- Company
- Zk Infrastructure
- Blockchain
- Layer 2
- Ethereum
- Zero Knowledge Proofs
- zkSharding
- JSON-RPC
- Smart Contracts
- Developer Tools
website: https://nil.foundation
---
