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
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-07-28'
api_count: 10
apis:
- description: The ATP Tennis API from Swish Analytics — 3 operation(s) for atp tennis.
  name: Swish Analytics ATP Tennis API
  slug: swish-analytics-atp-tennis-api
- description: The Bet Request API from Swish Analytics — 3 operation(s) for bet request.
  name: Swish Analytics Bet Request API
  slug: swish-analytics-bet-request-api
- description: The MLB API from Swish Analytics — 12 operation(s) for mlb.
  name: Swish Analytics MLB API
  slug: swish-analytics-mlb-api
- description: The NBA API from Swish Analytics — 10 operation(s) for nba.
  name: Swish Analytics NBA API
  slug: swish-analytics-nba-api
- description: The NCAA Basketball API from Swish Analytics — 4 operation(s) for ncaa basketball.
  name: Swish Analytics NCAA Basketball API
  slug: swish-analytics-ncaa-basketball-api
- description: The NCAA Football API from Swish Analytics — 6 operation(s) for ncaa football.
  name: Swish Analytics NCAA Football API
  slug: swish-analytics-ncaa-football-api
- description: The NFL API from Swish Analytics — 12 operation(s) for nfl.
  name: Swish Analytics NFL API
  slug: swish-analytics-nfl-api
- description: The NHL API from Swish Analytics — 5 operation(s) for nhl.
  name: Swish Analytics NHL API
  slug: swish-analytics-nhl-api
- description: The Soccer API from Swish Analytics — 8 operation(s) for soccer.
  name: Swish Analytics Soccer API
  slug: swish-analytics-soccer-api
- description: The WTA Tennis API from Swish Analytics — 3 operation(s) for wta tennis.
  name: Swish Analytics WTA Tennis API
  slug: swish-analytics-wta-tennis-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swish-analytics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swish-analytics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/swish-analytics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/swish-analytics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/swish-analytics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/swish-analytics-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/swish-analytics-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/swish-analytics-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/swish-analytics-reference.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/swish-analytics-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swish-analytics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.swishanalytics.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.swishanalytics.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.swishanalytics.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.swishanalytics.com/guides
- group: operate
  title: ''
  type: Support
  url: https://docs.swishanalytics.com/faq
- group: start
  title: ''
  type: SignUp
  url: https://docs.swishanalytics.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SwishAnalytics
- group: company
  title: ''
  type: Website
  url: https://swishanalytics.com
created: '2026-07-17'
description: Swish Analytics is a machine-learning sports analytics company that prices and originates sportsbook markets. Its B2B API delivers hyper-accurate player-prop pricing, pre-match and in-play match/team markets, single and parlay (accumulator) bet-request pricing, and market results across NFL, NBA, MLB, NHL, NCAA basketball and football, ATP and WTA tennis, and soccer. The read-only JSON API is authenticated with an ApiKey header, supports multi-value filtering and incremental delta sync via a modifiedAtGreater timestamp, and is documented at docs.swishanalytics.com. Swish positions itself as a global leader in player-props pricing and odds origination, risk-management and trading software for U.S. sportsbooks.
image: https://swish-assets.s3-us-west-2.amazonaws.com/imgs/spawn/api-logo-2023-full-black.png
layout: provider
mcp_servers:
- description: ''
  name: swish-analytics-mcp.yml
  slug: swish-analytics-mcpyml
modified: '2026-07-21'
name: Swish Analytics
nav: Providers
network: true
overview: 'Swish Analytics publishes 10 APIs on the [APIs.io](https://apis.io/) network, including ATP Tennis API, Bet Request API, MLB API, and 7 more. Tagged areas include Company, Sports, Sports Betting, Sportsbook, and Analytics.


  Swish Analytics'' developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, and 14 more developer resources.'
random_paper: 51
score:
  band: thin
  composite: 40.4
  delta: -1.6
  facets:
    commercial_clarity: 13.2
    contract_quality: 57.6
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 21.9
    operational_transparency: 5.3
  previous_composite: 42.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Swish Analytics Authentication
  slug: swish-analytics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Swish Analytics Domain Security
  slug: swish-analytics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: swish-analytics
tags:
- Company
- Sports
- Sports Betting
- Sportsbook
- Analytics
- Machine Learning
- Odds
- Player Props
- Data
- Predictions
website: https://swishanalytics.com
---
