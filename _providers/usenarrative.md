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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Usenarrative Agentic Access
  operation_count: 24
  slug: usenarrative-agentic-access
  summary_line: 24 operations · 10 acting · 1 human-in-the-loop
api_count: 1
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
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Narrative Sports Health API
  slug: open-usenarrative-health-api
- collection_type: open
  name: Narrative Sports Health Highlight Packages API
  slug: open-usenarrative-highlight-packages-api
- collection_type: open
  name: Narrative Sports Health Highlights API
  slug: open-usenarrative-highlights-api
- collection_type: open
  name: Narrative Sports Health Projects API
  slug: open-usenarrative-projects-api
- collection_type: open
  name: Narrative Sports Health Recaps API
  slug: open-usenarrative-recaps-api
- collection_type: open
  name: Narrative Sports Health Tasks API
  slug: open-usenarrative-tasks-api
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
  name: Narrative Sports MCP Server
  slug: narrative-sports-mcp-server
modified: '2026-07-21'
name: Narrative Sports
nav: Providers
network: true
overview: 'Narrative Sports publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Health API, Highlight Packages API, Highlights API, and 3 more. Tagged areas include Sports, Video, Artificial Intelligence, Highlights, and Broadcasting.


  Narrative Sports'' developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, authentication, and 18 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 48.5
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 40.2
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usenarrative/refs/heads/main/screenshots/usenarrative-2026-08-17T082657.png
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
