---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The Commands API from Arc Prize Foundation — 8 operation(s) for commands.
  name: Arc Prize Foundation Commands API
  slug: arc-prize-foundation-commands-api
- description: The Games API from Arc Prize Foundation — 1 operation(s) for games.
  name: Arc Prize Foundation Games API
  slug: arc-prize-foundation-games-api
- description: The Scorecards API from Arc Prize Foundation — 4 operation(s) for scorecards.
  name: Arc Prize Foundation Scorecards API
  slug: arc-prize-foundation-scorecards-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arc-prize-foundation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arc-prize-foundation-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/arc-prize-foundation-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/arc-prize-foundation-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/arc-prize-foundation-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arc-prize-foundation-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/arc-prize-foundation-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/arc-prize-foundation-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/arc-prize-foundation-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arc-prize-foundation-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arc-prize-foundation-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/arc-prize-foundation-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arc-prize-foundation-well-known.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.arcprize.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcprize.org
- group: docs
  title: ''
  type: APIReference
  url: https://docs.arcprize.org/rest_overview
- group: start
  title: ''
  type: Quickstart
  url: https://docs.arcprize.org/index
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arcprize
- group: company
  title: ''
  type: Blog
  url: https://arcprize.org/blog
- group: start
  title: ''
  type: SignUp
  url: https://arcprize.org/platform
- group: company
  title: ''
  type: Website
  url: https://arcprize.org
created: '2026-07-17'
description: The ARC Prize Foundation is a nonprofit advancing open artificial general intelligence research through scientifically rigorous benchmarks and competitive prizes. Its ARC-AGI benchmark series measures fluid intelligence on tasks that are easy for humans but hard for AI, and its ARC-AGI-3 Interactive Reasoning Benchmark exposes a public REST API (three.arcprize.org) plus an open-source Python toolkit and SDK for building agents that play, score, and generalize across novel game environments. The Foundation runs the ARC Prize competitions in partnership with Kaggle, with participation from OpenAI, Google, xAI, Anthropic, and NIST.
image: https://arcprize.org/media/images/og-image-default.jpg
layout: provider
mcp_servers:
- description: ''
  name: arc-prize-foundation-mcp.yml
  slug: arc-prize-foundation-mcpyml
modified: '2026-07-18'
name: Arc Prize Foundation
nav: Providers
network: true
overview: 'Arc Prize Foundation publishes 3 APIs on the [APIs.io](https://apis.io/) network: Commands API, Games API, and Scorecards API. Tagged areas include Company, Artificial Intelligence, AGI, Benchmarks, and Agents.


  Arc Prize Foundation''s developer surface includes authentication, changelog, documentation, API reference, quickstart, engineering blog, signup flow, and 15 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 42.7
  delta: -1.2
  facets:
    commercial_clarity: 13.2
    contract_quality: 60.2
    developer_ergonomics: 58.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 43.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arc-prize-foundation/refs/heads/main/screenshots/arc-prize-foundation-2026-07-25T201009.png
security:
- kind: authentication
  name: Arc Prize Foundation Authentication
  slug: arc-prize-foundation-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Arc Prize Foundation Domain Security
  slug: arc-prize-foundation-domain-security
  summary_line: TLSv1.2 · DMARC
slug: arc-prize-foundation
tags:
- Company
- Artificial Intelligence
- AGI
- Benchmarks
- Agents
- Reasoning
- Machine Learning
- Nonprofit
website: https://arcprize.org
---
