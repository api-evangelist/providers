---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Flow Blockchain Agentic Access
  operation_count: 22
  slug: flow-blockchain-agentic-access
  summary_line: 22 operations · 2 acting
api_count: 11
apis:
- description: The Accounts API from Flow — 4 operation(s) for accounts.
  name: Flow Accounts API
  slug: flow-blockchain-accounts-api
- description: The Blocks API from Flow — 3 operation(s) for blocks.
  name: Flow Blocks API
  slug: flow-blockchain-blocks-api
- description: The Collections API from Flow — 1 operation(s) for collections.
  name: Flow Collections API
  slug: flow-blockchain-collections-api
- description: The Events API from Flow — 1 operation(s) for events.
  name: Flow Events API
  slug: flow-blockchain-events-api
- description: The Execution Receipts API from Flow — 2 operation(s) for execution receipts.
  name: Flow Execution Receipts API
  slug: flow-blockchain-execution-receipts-api
- description: The Execution Results API from Flow — 2 operation(s) for execution results.
  name: Flow Execution Results API
  slug: flow-blockchain-execution-results-api
- description: The Network API from Flow — 1 operation(s) for network.
  name: Flow Network API
  slug: flow-blockchain-network-api
- description: The NodeVersionInfo API from Flow — 1 operation(s) for nodeversioninfo.
  name: Flow NodeVersionInfo API
  slug: flow-blockchain-nodeversioninfo-api
- description: The Scripts API from Flow — 1 operation(s) for scripts.
  name: Flow Scripts API
  slug: flow-blockchain-scripts-api
- description: The Subscribe events API from Flow — 1 operation(s) for subscribe events.
  name: Flow Subscribe events API
  slug: flow-blockchain-subscribe-events-api
- description: The Transactions API from Flow — 4 operation(s) for transactions.
  name: Flow Transactions API
  slug: flow-blockchain-transactions-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flow-blockchain-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flow-blockchain-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://flow.com/blog
created: '2026-06-13'
description: Flow is a developer-friendly Layer 1 proof-of-stake blockchain built for consumer applications, NFTs, games, AI agents, and DeFi at scale. The Flow REST API (Access API) enables developers to query accounts, blocks, collections, events, and transactions, execute Cadence scripts, and submit signed transactions to the network. Flow supports both native Cadence smart contracts and EVM-compatible Solidity deployments.
examples:
- key_count: 6
  name: Account
  slug: account
- key_count: 4
  name: Block
  slug: block
- key_count: 5
  name: Event
  slug: event
- key_count: 9
  name: Submit Transaction
  slug: submit-transaction
- key_count: 13
  name: Transaction
  slug: transaction
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://developers.flow.com/img/flow-docs-logo.png
json_schemas:
- name: Account
  property_count: 6
  slug: account
- name: Block
  property_count: 5
  slug: block
- name: Event
  property_count: 5
  slug: event
- name: Transaction
  property_count: 13
  slug: transaction
jsonld:
- class_count: 30
  name: context Context
  property_count: 77
  slug: context
layout: provider
modified: '2026-06-13'
name: Flow
nav: Providers
network: true
overview: 'Flow publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Blocks API, Collections API, and 8 more. Tagged areas include Blockchain, NFTs, Games, DeFi, and Layer 1.


  The Flow catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Flow''s developer surface includes engineering blog and 2 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 44
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Flow API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: flow-blockchain-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.9
    developer_ergonomics: 2.2
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 0.0
  previous_composite: 40.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flow-blockchain/refs/heads/main/screenshots/flow-blockchain-2026-06-20T181322.png
security:
- kind: domain-security
  name: Flow Blockchain Domain Security
  slug: flow-blockchain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flow-blockchain
tags:
- Blockchain
- NFTs
- Games
- DeFi
- Layer 1
- Cadence
- Smart Contracts
- Web3
---
