---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.succinct.xyz/rss/
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
  href: https://artifacts.apis.io/succinct/lifecycle/succinct-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/succinct-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/succinct/changelog/succinct-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/succinct-changelog.yml
- group: build
  href: https://artifacts.apis.io/succinct/packages/succinct-packages.yml
  title: ''
  type: Packages
  url: packages/succinct-packages.yml
- group: build
  href: https://artifacts.apis.io/succinct/packages/succinct-packages.yml
  title: ''
  type: SDKs
  url: packages/succinct-packages.yml
- group: build
  href: https://artifacts.apis.io/succinct/cli/succinct-cli.yml
  title: ''
  type: CLI
  url: cli/succinct-cli.yml
- group: auth
  href: https://artifacts.apis.io/succinct/authentication/succinct-authentication.yml
  title: ''
  type: Authentication
  url: authentication/succinct-authentication.yml
- group: design
  href: https://artifacts.apis.io/succinct/conformance/succinct-conformance.yml
  title: ''
  type: Conformance
  url: conformance/succinct-conformance.yml
- group: design
  href: https://artifacts.apis.io/succinct/conventions/succinct-conventions.yml
  title: ''
  type: Conventions
  url: conventions/succinct-conventions.yml
- group: agent
  href: https://artifacts.apis.io/succinct/llms/succinct-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/succinct-llms.txt
- group: auth
  href: https://artifacts.apis.io/succinct/security/succinct-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/succinct-domain-security.yml
- group: other
  href: https://artifacts.apis.io/succinct/grpc/succinct-network.proto
  title: ''
  type: Protobuf
  url: grpc/succinct-network.proto
- group: other
  href: https://artifacts.apis.io/succinct/grpc/succinct-artifact.proto
  title: ''
  type: Protobuf
  url: grpc/succinct-artifact.proto
- group: other
  href: https://artifacts.apis.io/succinct/grpc/succinct-verifier.proto
  title: ''
  type: Protobuf
  url: grpc/succinct-verifier.proto
- group: other
  href: https://artifacts.apis.io/succinct/grpc/succinct-types.proto
  title: ''
  type: Protobuf
  url: grpc/succinct-types.proto
created: '2026-07-17'
description: Succinct is an applied cryptography company building zero-knowledge proof infrastructure. Its flagship product is SP1, an open-source zkVM that proves the correct execution of RISC-V programs, and the Succinct Prover Network (SPN), a decentralized on-chain marketplace on Ethereum that coordinates a distributed network of provers to generate ZK proofs for any piece of software, settled with the PROVE token. Succinct's programmatic surface is a gRPC/protobuf API (the ProverNetwork, ArtifactStore, and Verifier services) rather than REST/OpenAPI; developers integrate in Rust via the SP1 SDK and CLI (cargo prove / sp1up) and authenticate to the network with a Secp256k1 key pair. Backed by Paradigm.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/succinct.png
layout: provider
modified: '2026-10-06'
name: Succinct
nav: Providers
network: true
overview: 'Succinct is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Infrastructure, Zero-Knowledge Proofs, zkVM, and Blockchain.


  Succinct''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, changelog, CLI, and 18 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 24.0
    developer_ergonomics: 66.7
    discoverability: 55.4
    operational_transparency: 42.1
  previous_composite: 33.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/succinct/succinct-2026-09-02T161107.png
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
