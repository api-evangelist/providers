---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: Solidity smart contracts that implement the EigenLayer restaking protocol - StrategyManager, DelegationManager, EigenPodManager, AVSDirectory, and the slasher. Operators register, stakers delegate, an
  name: EigenLayer Core Contracts
  slug: eigenlayer-contracts
- description: Go SDK for building AVS operator software and AVS-side services on top of EigenLayer. Provides typed bindings for the core contracts, BLS aggregation primitives, chain clients, and helpers for registe
  name: EigenSDK (Go)
  slug: eigensdk-go
- description: TypeScript SDK for interacting with the EigenLayer restaking protocol and AVS contracts from Node.js and browser apps - typed contract clients, operator and staker flows, and AVS task helpers.
  name: EigenSDK (TypeScript)
  slug: eigensdk-ts
- description: Operator-facing command-line tool for keys, operator registration, delegation, AVS opt-in, and node-runner administration on EigenLayer.
  name: EigenLayer CLI
  slug: eigenlayer-cli
- description: EigenDA is the data-availability service secured by EigenLayer restakers. Provides client libraries and a disperser API for posting and retrieving blobs of data, used by rollups and other consumers ne
  name: EigenDA
  slug: eigenda
- description: EigenCompute lets developers run arbitrary code in any language, with the execution secured by restakers and the result attested on-chain. Ships an SDK and CLI for packaging workloads, submitting jobs
  name: EigenCompute SDK & CLI
  slug: eigencompute
- description: EigenAI exposes deterministic, verifiable LLM inference over an OpenAI-compatible API surface, with execution and provenance secured by EigenLayer restakers.
  name: EigenAI
  slug: eigenai
artifact_total: 13
asyncapis:
- description: Bidirectional gRPC streaming surface exposed by the EigenDA v1 Disperser. EigenDA is the data-availability service secured by EigenLayer restakers; the Disperser is the consumer-facing entry point use
  name: EigenDA Streaming Surface
  slug: eigenlayer-streaming-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eigenlayer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eigenlayer.xyz/
- group: company
  title: ''
  type: Website
  url: https://www.eigencloud.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.eigencloud.xyz/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Layr-Labs
- group: operate
  title: ''
  type: Forums
  url: https://forum.eigenlayer.xyz/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eigen-labs/
created: '2026-05-23'
description: EigenLayer is a restaking protocol on Ethereum operated by Layr Labs that lets stakers re-use staked ETH (or liquid-staking tokens) to secure additional off-chain services called Actively Validated Services (AVSs). The team has since unified the restaking layer with EigenDA (data availability), EigenCompute (verifiable off-chain compute), and EigenAI (deterministic inference) under the EigenCloud brand. Developer surface includes the EigenLayer core smart contracts, AVS framework, EigenSDK in Go and TypeScript, EigenCloud CLI, and language SDKs for EigenCompute / EigenDA / EigenAI.
finops:
- name: Eigenlayer Finops
  service_category: API
  slug: eigenlayer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eigenlayer.png
layout: provider
modified: '2026-05-30'
name: EigenLayer
nav: Providers
network: true
overview: 'EigenLayer publishes 1 API on the [APIs.io](https://apis.io/) network: EigenDA. Tagged areas include Restaking, AVS, Ethereum, Data Availability, and Verifiable Compute.


  The EigenLayer catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  EigenLayer''s developer surface includes documentation, GitHub presence, and 5 more developer resources.'
plans:
- name: Eigenlayer Plans Pricing
  plan_count: 1
  slug: eigenlayer-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Eigenlayer Rate Limits
  slug: eigenlayer-rate-limits
rules:
- name: EigenLayer API Rules
  rule_count: 2
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 2
  slug: eigenlayer-asyncapi-spectral-rules
score:
  band: thin
  composite: 37.0
  delta: 1.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 49.4
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 52.1
    operational_transparency: 26.3
  previous_composite: 35.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eigenlayer/refs/heads/main/screenshots/eigenlayer-2026-06-20T180610.png
security:
- kind: domain-security
  name: Eigenlayer Domain Security
  slug: eigenlayer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: eigenlayer
tags:
- Restaking
- AVS
- Ethereum
- Data Availability
- Verifiable Compute
- Crypto
- Web3
website: https://www.eigenlayer.xyz/
---
