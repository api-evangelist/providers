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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Usenarrative Agentic Access
  operation_count: 24
  slug: usenarrative-agentic-access
  summary_line: 24 operations · 10 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: The Health API from Narrative Sports — 1 operation(s) for health.
  name: Narrative Sports Health API
  slug: usenarrative-health-api
- description: The Highlight Packages API from Narrative Sports — 3 operation(s) for highlight packages.
  name: Narrative Sports Highlight Packages API
  slug: usenarrative-highlight-packages-api
- description: The Highlights API from Narrative Sports — 4 operation(s) for highlights.
  name: Narrative Sports Highlights API
  slug: usenarrative-highlights-api
- description: The Projects API from Narrative Sports — 1 operation(s) for projects.
  name: Narrative Sports Projects API
  slug: usenarrative-projects-api
- description: The Recaps API from Narrative Sports — 3 operation(s) for recaps.
  name: Narrative Sports Recaps API
  slug: usenarrative-recaps-api
- description: The Tasks API from Narrative Sports — 8 operation(s) for tasks.
  name: Narrative Sports Tasks API
  slug: usenarrative-tasks-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.narrative-sports.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.narrative-sports.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.narrative-sports.com/api-reference/sports/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.narrative-sports.com/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.narrative-sports.com/api-dashboard
- group: start
  title: ''
  type: Login
  url: https://app.narrative-sports.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://narrative-sports.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://narrative-sports.com/blog
- group: operate
  title: ''
  type: Support
  url: https://narrative-sports.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://narrative-sports.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://narrative-sports.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.narrative-sports.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Narrative-Sports
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/usenarrative-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/usenarrative-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/usenarrative-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/usenarrative-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/usenarrative-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/usenarrative-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/usenarrative-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/usenarrative-sports-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usenarrative-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/usenarrative-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/usenarrative-authentication.yml
created: '2026-07-17'
description: Narrative Sports (Narrative AI Inc., YC Fall 2025, listed by Y Combinator as "usenarrative") is an AI-powered sports content platform that automates the creation and distribution of broadcast-ready highlight videos for broadcasters, teams, and leagues. Its API ingests live SRT streams for soccer and MMA, detects key moments in real time, and returns rendered clips in multiple aspect ratios, single-game recaps, multi-game highlight packages, and OTIO edit timelines.
image: https://narrative-sports.com/largelogofrontend_white2.png
layout: provider
mcp_servers:
- description: ''
  name: usenarrative-mcp.yml
  slug: usenarrative-mcpyml
modified: '2026-07-21'
name: Narrative Sports
nav: Providers
network: true
overview: 'Narrative Sports publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Health API, Highlight Packages API, Highlights API, and 3 more. Tagged areas include Sports, Video, Artificial Intelligence, Highlights, and Broadcasting.


  Narrative Sports'' developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, authentication, and 18 more developer resources.'
random_paper: 70
score:
  band: developing
  composite: 46.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 53.4
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Usenarrative Authentication
  slug: usenarrative-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Usenarrative Domain Security
  slug: usenarrative-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: usenarrative
tags:
- Sports
- Video
- Artificial Intelligence
- Highlights
- Broadcasting
- Media
- Sports Technology
website: https://www.narrative-sports.com/
---
