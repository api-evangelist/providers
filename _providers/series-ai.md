---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'Client-side JavaScript/TypeScript SDK (@series-inc/rundot-game-sdk) that gives an HTML5 game access to RUN.world platform services through a single RundotGameAPI import: storage scopes, profiles, lead'
  name: RUN.world SDK
  slug: runworld-sdk
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/series-ai-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://run.world
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/series-ai/venus-sdk-docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/series-ai/venus-sdk-docs/blob/main/SUMMARY.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/series-ai/venus-sdk-docs/blob/main/rundot-developer-platform/getting-started.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/series-ai
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/series-ai/run-workshop
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://series.inc/privacy
- group: build
  title: ''
  type: Packages
  url: packages/series-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/series-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/series-ai-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/series-ai-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/series-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/series-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/series-ai-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/series-ai-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/series-ai-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/series-ai-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/series-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/series-ai-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/series-ai-well-known.yml
created: '2026-07-17'
description: 'Series AI (Series Entertainment, Inc.) is an a16z-backed, AI-native game company behind RUN.world, a platform to create, publish, play, and monetize HTML5 games. Series ships a real first-party developer surface: the RUN.world SDK (@series-inc/rundot-game-sdk) exposes a single RundotGameAPI for player storage, profiles, leaderboards, ad monetization, purchases, entitlements, multiplayer, server-authoritative simulation, and generative AI (image, audio, video, and text), while the rundot CLI scaffolds, deploys, versions, and operates live titles. StowKit asset tooling, a Three.js-based 3D engine with ECS, the Syncplay deterministic-multiplayer core, and a community workshop of game starters round out the toolchain. Founded by veterans from Riot, Epic, Blizzard, Pocket Gems, and Telltale.'
image: https://avatars.githubusercontent.com/u/126116685?v=4
layout: provider
modified: '2026-07-21'
name: Series AI
nav: Providers
network: true
overview: 'Series AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Games, Game Development, Artificial Intelligence, and Generative AI.


  Series AI''s developer surface includes documentation, API reference, getting-started guide, CLI, sandbox, changelog, authentication, and 15 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 28.1
  provenance:
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/series-ai/refs/heads/main/screenshots/series-ai-2026-09-02T155010.png
security:
- kind: authentication
  name: Series Ai Authentication
  slug: series-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Series Ai Domain Security
  slug: series-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Series Ai Vulnerability Disclosure
  slug: series-ai-vulnerability-disclosure
  summary_line: disclosure policy published
slug: series-ai
tags:
- Company
- Games
- Game Development
- Artificial Intelligence
- Generative AI
- Game Engine
- SDK
- Developer Tools
- Multiplayer
- HTML5
website: https://run.world
---
