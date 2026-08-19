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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Public GraphQL API over DSCVR's SocialFi graph. Query users (by id or username), portals (by id or slug), content (posts and comments), on-chain wallets, reactions, and unpack Frame messages. Currentl
  name: DSCVR API
  slug: dscvr-api
artifact_total: 4
common:
- group: auth
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
  title: ''
  type: GraphQL
  url: graphql/dscvr-graphql.graphql
- group: build
  title: ''
  type: Packages
  url: packages/dscvr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dscvr-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dscvr-cli.yml
- group: design
  title: ''
  type: Components
  url: components/dscvr-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dscvr-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dscvr-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dscvr-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/dscvr-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dscvr-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dscvr-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dscvr-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dscvr-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dscvr-well-known.yml
created: '2026-07-17'
description: DSCVR (pronounced "discover") is a Web3 social platform that blends a Web2-style social experience with crypto-native ownership, monetization, and distribution. Users post and interact inside token-gated communities called Portals, earn DSCVR Points and daily streaks, and connect on-chain wallets across Solana and the Internet Computer. For developers, DSCVR exposes a public GraphQL API over its SocialFi graph — users, portals, content, wallets, reactions, and frame messages — alongside the DSCVR Canvas / Frames framework for embedding interactive mini-apps directly into the social feed, all backed by first-party TypeScript SDKs.
image: https://dscvr.one/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: dscvr-mcp.yml
  slug: dscvr-mcpyml
modified: '2026-07-18'
name: DSCVR
nav: Providers
network: true
overview: 'DSCVR publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Web3, GraphQL, and Blockchain.


  DSCVR''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 18 more developer resources.'
random_paper: 99
score:
  band: thin
  composite: 32.9
  delta: -2.7
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 33.3
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 35.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dscvr/refs/heads/main/screenshots/dscvr-2026-07-25T212432.png
security:
- kind: authentication
  name: Dscvr Authentication
  slug: dscvr-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Dscvr Domain Security
  slug: dscvr-domain-security
  summary_line: TLSv1.3 · DMARC
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
