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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 19.2
  scored_at: '2026-11-06'
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
  href: https://artifacts.apis.io/harmonic-gg/grpc/harmonic-gg-searcher-searcher.proto
  title: ''
  type: Protobuf
  url: grpc/harmonic-gg-searcher-searcher.proto
- group: other
  href: https://artifacts.apis.io/harmonic-gg/grpc/harmonic-gg-validator-block_engine.proto
  title: ''
  type: Protobuf
  url: grpc/harmonic-gg-validator-block_engine.proto
- group: agent
  href: https://artifacts.apis.io/harmonic-gg/llms/harmonic-gg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/harmonic-gg-llms.txt
- group: auth
  href: https://artifacts.apis.io/harmonic-gg/authentication/harmonic-gg-authentication.yml
  title: ''
  type: Authentication
  url: authentication/harmonic-gg-authentication.yml
- group: start
  href: https://artifacts.apis.io/harmonic-gg/sandbox/harmonic-gg-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/harmonic-gg-sandbox.yml
- group: design
  href: https://artifacts.apis.io/harmonic-gg/conventions/harmonic-gg-conventions.yml
  title: ''
  type: Conventions
  url: conventions/harmonic-gg-conventions.yml
- group: design
  href: https://artifacts.apis.io/harmonic-gg/conformance/harmonic-gg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/harmonic-gg-conformance.yml
- group: design
  href: https://artifacts.apis.io/harmonic-gg/errors/harmonic-gg-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/harmonic-gg-error-codes.yml
- group: design
  href: https://artifacts.apis.io/harmonic-gg/lifecycle/harmonic-gg-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/harmonic-gg-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/harmonic-gg/data-model/harmonic-gg-data-model.yml
  title: ''
  type: DataModel
  url: data-model/harmonic-gg-data-model.yml
- group: agent
  href: https://artifacts.apis.io/harmonic-gg/mcp/harmonic-gg-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/harmonic-gg-mcp.yml
- group: agent
  href: https://artifacts.apis.io/harmonic-gg/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/harmonic-gg/packages/harmonic-gg-packages.yml
  title: ''
  type: Packages
  url: packages/harmonic-gg-packages.yml
- group: auth
  href: https://artifacts.apis.io/harmonic-gg/security/harmonic-gg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/harmonic-gg-domain-security.yml
created: '2026-07-17'
description: Harmonic is a highly-configurable, open block-building system for Solana. Validators keep full autonomy over how their blocks are built, choosing their own block builder and scheduling strategy (FBA, FIFO, MREV, or custom) while the block engine streams the constructed block for broadcast. A Remote TPU aggregation layer collects proposals from independent builders in real time, HFT-router style, to raise validator revenue and strengthen network decentralization. Searchers submit atomic transaction bundles over a gRPC interface that is backwards-compatible with Jito's searcher protos, with revert protection, bundle privacy, and tips paid as ordinary priority fees (no protocol cut). Harmonic raised a $6M seed round led by Paradigm.
image: https://harmonic.gg/api/og?v=home
layout: provider
modified: '2026-07-19'
name: Harmonic GG
nav: Providers
network: true
overview: 'Harmonic GG is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Solana, Block Building, and MEV.


  Harmonic GG''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, sandbox, and 18 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 24.0
    developer_ergonomics: 63.7
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 29.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/harmonic-gg/harmonic-gg-2026-07-25T220716.png
security:
- kind: authentication
  name: Harmonic Gg Authentication
  slug: harmonic-gg-authentication
  summary_line: challenge-response/bearer · 2 schemes
- kind: domain-security
  name: Harmonic Gg Domain Security
  slug: harmonic-gg-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: Send a searcher bundle to Harmonic
  slug: harmonic-gg-send-bundle
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
