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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api.swishanalytics.com
  baseurl_source: declared
  description: The ATP Tennis API from Swish Analytics — 3 operation(s) for atp tennis.
  name: Swish Analytics ATP Tennis API
  slug: swish-analytics-atp-tennis-api
- baseURL: https://api.swishanalytics.com
  baseurl_source: declared
  description: The Bet Request API from Swish Analytics — 3 operation(s) for bet request.
  name: Swish Analytics Bet Request API
  slug: swish-analytics-bet-request-api
- baseURL: https://api.swishanalytics.com
  baseurl_source: declared
  description: The MLB API from Swish Analytics — 12 operation(s) for mlb.
  name: Swish Analytics MLB API
  slug: swish-analytics-mlb-api
- baseURL: https://api.swishanalytics.com
  baseurl_source: declared
  description: The NBA API from Swish Analytics — 10 operation(s) for nba.
  name: Swish Analytics NBA API
  slug: swish-analytics-nba-api
- baseURL: https://api.swishanalytics.com
  baseurl_source: declared
  description: The NCAA Basketball API from Swish Analytics — 4 operation(s) for ncaa basketball.
  name: Swish Analytics NCAA Basketball API
  slug: swish-analytics-ncaa-basketball-api
- baseURL: https://api.swishanalytics.com
  baseurl_source: declared
  description: The NCAA Football API from Swish Analytics — 6 operation(s) for ncaa football.
  name: Swish Analytics NCAA Football API
  slug: swish-analytics-ncaa-football-api
- baseURL: https://api.swishanalytics.com
  baseurl_source: declared
  description: The NFL API from Swish Analytics — 12 operation(s) for nfl.
  name: Swish Analytics NFL API
  slug: swish-analytics-nfl-api
- baseURL: https://api.swishanalytics.com
  baseurl_source: declared
  description: The NHL API from Swish Analytics — 5 operation(s) for nhl.
  name: Swish Analytics NHL API
  slug: swish-analytics-nhl-api
- baseURL: https://api.swishanalytics.com
  baseurl_source: declared
  description: The Soccer API from Swish Analytics — 8 operation(s) for soccer.
  name: Swish Analytics Soccer API
  slug: swish-analytics-soccer-api
- baseURL: https://api.swishanalytics.com
  baseurl_source: declared
  description: The WTA Tennis API from Swish Analytics — 3 operation(s) for wta tennis.
  name: Swish Analytics WTA Tennis API
  slug: swish-analytics-wta-tennis-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Swish Analytics Sportsbook ATP Tennis API
  slug: open-swish-analytics-atp-tennis-api
- collection_type: open
  name: Swish Analytics Sportsbook ATP Tennis Bet Request API
  slug: open-swish-analytics-bet-request-api
- collection_type: open
  name: Swish Analytics Sportsbook ATP Tennis MLB API
  slug: open-swish-analytics-mlb-api
- collection_type: open
  name: Swish Analytics Sportsbook ATP Tennis NBA API
  slug: open-swish-analytics-nba-api
- collection_type: open
  name: Swish Analytics Sportsbook ATP Tennis NCAA Basketball API
  slug: open-swish-analytics-ncaa-basketball-api
- collection_type: open
  name: Swish Analytics Sportsbook ATP Tennis NCAA Football API
  slug: open-swish-analytics-ncaa-football-api
- collection_type: open
  name: Swish Analytics Sportsbook ATP Tennis NFL API
  slug: open-swish-analytics-nfl-api
- collection_type: open
  name: Swish Analytics Sportsbook ATP Tennis NHL API
  slug: open-swish-analytics-nhl-api
- collection_type: open
  name: Swish Analytics Sportsbook ATP Tennis Soccer API
  slug: open-swish-analytics-soccer-api
- collection_type: open
  name: Swish Analytics Sportsbook ATP Tennis WTA Tennis API
  slug: open-swish-analytics-wta-tennis-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/swish-analytics-sportsbook-overlay.yaml
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
  name: Swish Analytics MCP Server
  slug: swish-analytics-mcp-server
modified: '2026-07-21'
name: Swish Analytics
nav: Providers
network: true
overview: 'Swish Analytics publishes 10 APIs on the [APIs.io](https://apis.io/) network, including ATP Tennis API, Bet Request API, MLB API, and 7 more. Tagged areas include Company, Sports, Sports Betting, Sportsbook, and Analytics.


  Swish Analytics'' developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, and 15 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 73.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 19.7
    contract_quality: 13.9
    developer_ergonomics: 13.7
    discoverability: 75.9
    governance: 19.7
    operational_transparency: 2.6
  previous_composite: 16.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swish-analytics/refs/heads/main/screenshots/swish-analytics-2026-09-02T161411.png
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
- Machine-Learning
- Odds
- Player Props
- Data
- Predictions
website: https://swishanalytics.com
---
