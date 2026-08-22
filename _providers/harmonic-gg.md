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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: gRPC bundle-submission interface for searchers. Authenticate with a Solana keypair (challenge-response to Bearer tokens), then submit atomic transaction bundles with revert protection. Backwards-compa
  name: Harmonic Searcher API (gRPC)
  slug: harmonic-searcher-api-grpc
- description: 'gRPC services the Harmonic validator clients (Salsa/Samba) use to bind to a block builder: subscribe to packet and bundle streams, set the scheduling strategy, discover block engine endpoints, report '
  name: Harmonic Validator API (gRPC)
  slug: harmonic-validator-api-grpc
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/harmonic/searcher-protos/issues
- group: company
  title: ''
  type: Website
  url: https://harmonic.gg
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.harmonic.gg
- group: docs
  title: ''
  type: Documentation
  url: https://docs.harmonic.gg
- group: docs
  title: ''
  type: APIReference
  url: https://docs.harmonic.gg/searchers/harmonic-bundles
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.harmonic.gg/run-a-validator/setup
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/23GfZkkyAG
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/harmonic
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/harmonic/searcher-protos
- group: start
  title: ''
  type: SignUp
  url: https://form.typeform.com/to/UlJMfbPH
- group: commercial
  title: ''
  type: TermsOfService
  url: https://harmonic.gg/terms-and-conditions
- group: other
  title: ''
  type: Protobuf
  url: grpc/harmonic-gg-searcher-searcher.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/harmonic-gg-validator-block_engine.proto
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/harmonic-gg-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/harmonic-gg-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/harmonic-gg-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/harmonic-gg-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/harmonic-gg-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/harmonic-gg-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/harmonic-gg-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/harmonic-gg-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/harmonic-gg-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/harmonic-gg-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harmonic-gg-domain-security.yml
created: '2026-07-17'
description: Harmonic is a highly-configurable, open block-building system for Solana. Validators keep full autonomy over how their blocks are built, choosing their own block builder and scheduling strategy (FBA, FIFO, MREV, or custom) while the block engine streams the constructed block for broadcast. A Remote TPU aggregation layer collects proposals from independent builders in real time, HFT-router style, to raise validator revenue and strengthen network decentralization. Searchers submit atomic transaction bundles over a gRPC interface that is backwards-compatible with Jito's searcher protos, with revert protection, bundle privacy, and tips paid as ordinary priority fees (no protocol cut). Harmonic raised a $6M seed round led by Paradigm.
image: https://harmonic.gg/api/og?v=home
layout: provider
mcp_servers:
- description: ''
  name: harmonic-gg-mcp.yml
  slug: harmonic-gg-mcpyml
modified: '2026-07-19'
name: Harmonic GG
nav: Providers
network: true
overview: 'Harmonic GG publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Solana, Block Building, and MEV.


  Harmonic GG''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, sandbox, and 18 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 30.4
  delta: 4.9
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 28.2
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 25.5
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harmonic-gg/refs/heads/main/screenshots/harmonic-gg-2026-07-25T220716.png
security:
- kind: authentication
  name: Harmonic Gg Authentication
  slug: harmonic-gg-authentication
  summary_line: challenge-response/bearer · 2 schemes
- kind: domain-security
  name: Harmonic Gg Domain Security
  slug: harmonic-gg-domain-security
  summary_line: TLSv1.3 · HSTS
slug: harmonic-gg
tags:
- Company
- Blockchain
- Solana
- Block Building
- MEV
- Validator
- Searcher
- Infrastructure
- gRPC
- DeFi
website: https://harmonic.gg
---
