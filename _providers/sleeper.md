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
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.9
  scored_at: '2026-08-19'
api_count: 8
apis:
- description: The Drafts API from Sleeper — 6 operation(s) for drafts.
  name: Sleeper Drafts API
  slug: sleeper-drafts-api
- description: The Leagues API from Sleeper — 4 operation(s) for leagues.
  name: Sleeper Leagues API
  slug: sleeper-leagues-api
- description: The Matchups API from Sleeper — 1 operation(s) for matchups.
  name: Sleeper Matchups API
  slug: sleeper-matchups-api
- description: The Players API from Sleeper — 2 operation(s) for players.
  name: Sleeper Players API
  slug: sleeper-players-api
- description: The Playoffs API from Sleeper — 2 operation(s) for playoffs.
  name: Sleeper Playoffs API
  slug: sleeper-playoffs-api
- description: The State API from Sleeper — 1 operation(s) for state.
  name: Sleeper State API
  slug: sleeper-state-api
- description: The Transactions API from Sleeper — 1 operation(s) for transactions.
  name: Sleeper Transactions API
  slug: sleeper-transactions-api
- description: The Users API from Sleeper — 1 operation(s) for users.
  name: Sleeper Users API
  slug: sleeper-users-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sleeper Drafts API
  slug: open-sleeper-drafts-api
- collection_type: open
  name: Sleeper Drafts Leagues API
  slug: open-sleeper-leagues-api
- collection_type: open
  name: Sleeper Drafts Matchups API
  slug: open-sleeper-matchups-api
- collection_type: open
  name: Sleeper Drafts Players API
  slug: open-sleeper-players-api
- collection_type: open
  name: Sleeper Drafts Playoffs API
  slug: open-sleeper-playoffs-api
- collection_type: open
  name: Sleeper Drafts State API
  slug: open-sleeper-state-api
- collection_type: open
  name: Sleeper Drafts Transactions API
  slug: open-sleeper-transactions-api
- collection_type: open
  name: Sleeper Drafts Users API
  slug: open-sleeper-users-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sleeper-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sleeper.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sleeper.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sleeper.com/
- group: start
  title: ''
  type: SignUp
  url: https://sleeper.com/
- group: operate
  title: ''
  type: Support
  url: https://support.sleeper.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.sleeper.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sleeper.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sleeper.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/sleeper-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sleeper-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sleeper-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sleeper-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sleeper-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sleeper-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/sleeper-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/sleeper-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sleeper-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sleeper-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/sleeper-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Sleeper is a fantasy sports platform — a mobile-first app for creating and managing fantasy football, basketball, and other sports leagues with chat, drafts, waivers, and real-time scoring built in. Sleeper publishes a free, read-only HTTP API at api.sleeper.app that exposes public fantasy data: users, leagues, rosters, matchups, transactions, drafts, draft picks, traded picks, trending players, and the current sport/season state. The API requires no API token or OAuth because no content can be modified through it; every endpoint is a GET request returning JSON, and callers are asked to stay under 1,000 requests per minute to avoid IP blocks. Sleeper is backed by a16z and General Catalyst.'
image: https://sleepercdn.com/images/v2/icons/app_icon_web.png
layout: provider
mcp_servers:
- description: ''
  name: sleeper-mcp.yml
  slug: sleeper-mcpyml
modified: '2026-07-21'
name: Sleeper
nav: Providers
network: true
overview: 'Sleeper publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Drafts API, Leagues API, Matchups API, and 5 more. Tagged areas include Company, Fantasy Sports, Sports, Fantasy Football, and Gaming.


  Sleeper''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, and 15 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 29.6
  delta: 0.8
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 12.7
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 28.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Sleeper Authentication
  slug: sleeper-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Sleeper Domain Security
  slug: sleeper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sleeper
tags:
- Company
- Fantasy Sports
- Sports
- Fantasy Football
- Gaming
- Sports Data
- Leagues
- Consumer
website: https://docs.sleeper.com/
---
