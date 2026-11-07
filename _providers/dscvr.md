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
  score: 16.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public GraphQL API over DSCVR's SocialFi graph. Query users (by id or username), portals (by id or slug), content (posts and comments), on-chain wallets, reactions, and unpack Frame messages. Currentl
  name: DSCVR API
  slug: dscvr-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/dscvr/security/dscvr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dscvr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dscvr.one
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dscvr.one/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dscvr.one/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dscvr.one/build/dscvr-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dscvr.one/build/dscvr-canvas/build-a-canvas
- group: company
  title: ''
  type: Blog
  url: https://blog.dscvr.one/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dscvr-one
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/DX4CaFph3s
- group: start
  title: ''
  type: SignUp
  url: https://dscvr.one/
- group: docs
  href: https://artifacts.apis.io/dscvr/graphql/dscvr-graphql.graphql
  title: ''
  type: GraphQL
  url: graphql/dscvr-graphql.graphql
- group: build
  href: https://artifacts.apis.io/dscvr/packages/dscvr-packages.yml
  title: ''
  type: Packages
  url: packages/dscvr-packages.yml
- group: build
  href: https://artifacts.apis.io/dscvr/packages/dscvr-packages.yml
  title: ''
  type: SDKs
  url: packages/dscvr-packages.yml
- group: build
  href: https://artifacts.apis.io/dscvr/cli/dscvr-cli.yml
  title: ''
  type: CLI
  url: cli/dscvr-cli.yml
- group: design
  href: https://artifacts.apis.io/dscvr/components/dscvr-components.yml
  title: ''
  type: Components
  url: components/dscvr-components.yml
- group: start
  href: https://artifacts.apis.io/dscvr/sandbox/dscvr-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/dscvr-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/dscvr/mcp/dscvr-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dscvr-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dscvr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/dscvr/llms/dscvr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dscvr-llms.txt
- group: auth
  href: https://artifacts.apis.io/dscvr/authentication/dscvr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dscvr-authentication.yml
- group: design
  href: https://artifacts.apis.io/dscvr/conventions/dscvr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dscvr-conventions.yml
- group: design
  href: https://artifacts.apis.io/dscvr/data-model/dscvr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dscvr-data-model.yml
- group: design
  href: https://artifacts.apis.io/dscvr/conformance/dscvr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dscvr-conformance.yml
- group: design
  href: https://artifacts.apis.io/dscvr/lifecycle/dscvr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dscvr-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/dscvr/well-known/dscvr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dscvr-well-known.yml
created: '2026-07-17'
description: DSCVR (pronounced "discover") is a Web3 social platform that blends a Web2-style social experience with crypto-native ownership, monetization, and distribution. Users post and interact inside token-gated communities called Portals, earn DSCVR Points and daily streaks, and connect on-chain wallets across Solana and the Internet Computer. For developers, DSCVR exposes a public GraphQL API over its SocialFi graph — users, portals, content, wallets, reactions, and frame messages — alongside the DSCVR Canvas / Frames framework for embedding interactive mini-apps directly into the social feed, all backed by first-party TypeScript SDKs.
image: https://dscvr.one/favicon.ico
layout: provider
modified: '2026-07-18'
name: DSCVR
nav: Providers
network: true
overview: 'DSCVR is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Web3, GraphQL, and Blockchain.


  DSCVR''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 18 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 29.8
    developer_ergonomics: 80.4
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 32.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
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
screenshot: https://apis.io/screenshots/dscvr/dscvr-2026-07-25T212432.png
security:
- kind: authentication
  name: Dscvr Authentication
  slug: dscvr-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Dscvr Domain Security
  slug: dscvr-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Inspect a DSCVR portal and its content
  slug: dscvr-inspect-portal-and-content
- name: Look up a DSCVR user profile and social graph
  slug: dscvr-lookup-user-profile
- name: Verify and decode a DSCVR Frame message
  slug: dscvr-verify-frame-message
slug: dscvr
tags:
- Company
- Social
- Web3
- GraphQL
- Blockchain
- Solana
- Internet Computer
- SocialFi
- Social Graph
- Developer Platform
website: https://dscvr.one
---
