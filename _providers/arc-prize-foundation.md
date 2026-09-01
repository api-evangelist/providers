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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-01'
api_count: 1
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
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ARC‑AGI‑3 REST Commands API
  slug: open-arc-prize-foundation-commands-api
- collection_type: open
  name: ARC‑AGI‑3 REST Commands Games API
  slug: open-arc-prize-foundation-games-api
- collection_type: open
  name: ARC‑AGI‑3 REST Commands Scorecards API
  slug: open-arc-prize-foundation-scorecards-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/arc-prize-foundation-arc-agi-3-overlay.yaml
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
  name: Arc Prize Foundation MCP Server
  slug: arc-prize-foundation-mcp-server
modified: '2026-07-18'
name: Arc Prize Foundation
nav: Providers
network: true
overview: 'Arc Prize Foundation publishes 3 APIs on the [APIs.io](https://apis.io/) network: Commands API, Games API, and Scorecards API. Tagged areas include Company, Artificial Intelligence, AGI, Benchmarks, and Agents.


  Arc Prize Foundation''s developer surface includes authentication, changelog, documentation, API reference, quickstart, engineering blog, signup flow, and 16 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 56.5
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 39.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Machine-Learning
- Non-Profit
website: https://arcprize.org
---
