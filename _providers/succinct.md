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
  score: 9.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://succinct.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.succinct.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.succinct.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.succinct.xyz/docs/provers/building-a-prover/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.succinct.xyz/docs/sp1/getting-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://blog.succinct.xyz
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/succinctlabs
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.succinct.xyz/docs/protocol/prove/pay
- group: operate
  title: ''
  type: StatusPage
  url: https://status.succinct.xyz
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.succinct.xyz/docs/sp1/developers/upgrades
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/succinct-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/succinct-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/succinct-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/succinct-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/succinct-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/succinct-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/succinct-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/succinct-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/succinct-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/succinct-domain-security.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/succinct-network.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/succinct-artifact.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/succinct-verifier.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/succinct-types.proto
created: '2026-07-17'
description: Succinct is an applied cryptography company building zero-knowledge proof infrastructure. Its flagship product is SP1, an open-source zkVM that proves the correct execution of RISC-V programs, and the Succinct Prover Network (SPN), a decentralized on-chain marketplace on Ethereum that coordinates a distributed network of provers to generate ZK proofs for any piece of software, settled with the PROVE token. Succinct's programmatic surface is a gRPC/protobuf API (the ProverNetwork, ArtifactStore, and Verifier services) rather than REST/OpenAPI; developers integrate in Rust via the SP1 SDK and CLI (cargo prove / sp1up) and authenticate to the network with a Secp256k1 key pair. Backed by Paradigm.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/succinct.png
layout: provider
modified: '2026-07-21'
name: Succinct
nav: Providers
network: true
overview: 'Succinct is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Infrastructure, Zero-Knowledge Proofs, zkVM, and Blockchain.


  Succinct''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, changelog, CLI, and 17 more developer resources.'
random_paper: 40
score:
  band: emerging
  composite: 26.2
  delta: -0.6
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 57.4
    governance: 3.1
    operational_transparency: 44.7
  previous_composite: 26.8
  provenance:
    conformance: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Succinct Authentication
  slug: succinct-authentication
  summary_line: signature · 2 schemes
- kind: domain-security
  name: Succinct Domain Security
  slug: succinct-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: succinct
tags:
- Company
- Crypto Infrastructure
- Zero-Knowledge Proofs
- zkVM
- Blockchain
- Ethereum
- Cryptography
- Developer Tools
- Prover Network
- gRPC
website: https://succinct.xyz
---
