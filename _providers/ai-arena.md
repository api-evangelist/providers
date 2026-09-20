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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.0
  scored_at: '2026-09-19'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://aiarena.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rlmesh.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rlmesh.dev
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rlmesh.dev/en/v0.1.0-rc.2/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rlmesh.dev/en/v0.1.0-rc.2/quickstart/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ArenaX-Labs
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@aiarena
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.rlmesh.dev/en/v0.1.0-rc.2/compatibility/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ai-arena/refs/heads/main/grpc/ai-arena-grpc.yml
  title: ''
  type: Protobuf
  url: grpc/ai-arena-grpc.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ai-arena/refs/heads/main/packages/ai-arena-packages.yml
  title: ''
  type: Packages
  url: packages/ai-arena-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ai-arena/refs/heads/main/packages/ai-arena-packages.yml
  title: ''
  type: SDKs
  url: packages/ai-arena-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ai-arena/refs/heads/main/cli/ai-arena-cli.yml
  title: ''
  type: CLI
  url: cli/ai-arena-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ai-arena/refs/heads/main/changelog/ai-arena-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ai-arena-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ai-arena/refs/heads/main/lifecycle/ai-arena-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ai-arena-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.rlmesh.dev/en/v0.1.0-rc.2/compatibility/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ai-arena/refs/heads/main/conformance/ai-arena-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ai-arena-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ai-arena/refs/heads/main/conventions/ai-arena-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ai-arena-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ai-arena/refs/heads/main/authentication/ai-arena-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ai-arena-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ai-arena/refs/heads/main/security/ai-arena-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ai-arena-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/ArenaX-Labs/rlmesh/blob/main/SECURITY.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ai-arena/refs/heads/main/security/ai-arena-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-arena-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ai-arena/refs/heads/main/llms/ai-arena-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-arena-llms.txt
created: '2026-07-17'
description: 'AI Arena is a web3/AI gaming company built by ArenaX Labs, backed by Paradigm and Framework Ventures. Its flagship title, AI Arena, is an Ethereum/Arbitrum-native PvP fighting game where players purchase, train through imitation learning, and battle characters powered by real artificial intelligence, with a native $NRN (Neuron) token and an on-chain marketplace for AI models. Beyond the game, ArenaX Labs ships developer infrastructure for reinforcement learning: RLMesh, an open-source, Gymnasium-compatible framework that connects RL models to environments across process, dependency, and machine boundaries over a gRPC wire protocol (rlmesh-wire-v1), with Python and Rust SDKs; and SAI (competesai.com), a gamified RL research and competition platform with its own CLI. This profile was enriched by the API Evangelist pipeline from public sources — GitHub, package registries, and the RLMesh documentation.'
image: https://raw.githubusercontent.com/api-evangelist/ai-arena/refs/heads/main/images/ai-arena.jpg
layout: provider
modified: '2026-07-17'
name: AI Arena
nav: Providers
network: true
overview: 'AI Arena is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Web3, Artificial Intelligence, and Reinforcement Learning.


  AI Arena''s developer surface includes documentation, API reference, getting-started guide, engineering blog, CLI, changelog, authentication, and 15 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 66.7
    discoverability: 57.4
    operational_transparency: 42.1
  previous_composite: 33.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/ai-arena/refs/heads/main/screenshots/ai-arena-2026-07-25T195331.png
security:
- kind: authentication
  name: Ai Arena Authentication
  slug: ai-arena-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Ai Arena Domain Security
  slug: ai-arena-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ai Arena Vulnerability Disclosure
  slug: ai-arena-vulnerability-disclosure
  summary_line: contact published
slug: ai-arena
tags:
- Company
- Gaming
- Web3
- Artificial Intelligence
- Reinforcement Learning
- Machine-Learning
- gRPC
- SDK
- Developer Tools
website: https://aiarena.io
---
