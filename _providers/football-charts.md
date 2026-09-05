---
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.3
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Free read-only REST API for football statistics, standings, results, fixtures, match probabilities, season projections, goal timing, and prediction track record. Bearer API key auth (or X-API-Key) wit
  name: Football Charts REST API
  slug: football-charts-rest-api
- description: Hosted MCP server (protocol 2025-06-18) exposing ten read-only football statistics tools (list_leagues, get_league_table, get_rankings, get_results, get_fixtures, get_match, get_season_projection, get
  name: Football Charts MCP Server
  slug: football-charts-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.football-charts.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.football-charts.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.football-charts.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.football-charts.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.football-charts.com/developers
- group: start
  title: ''
  type: SignUp
  url: https://www.football-charts.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://www.football-charts.com/developers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.football-charts.com/developers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.football-charts.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.football-charts.com/about
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ddevetak/footballcharts-mcp
- group: agent
  title: ''
  type: MCPServer
  url: mcp/football-charts-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/football-charts-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/football-charts-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/football-charts-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/football-charts-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/football-charts-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/football-charts-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/football-charts-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/football-charts-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/football-charts-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/football-charts-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/football-charts-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/football-charts-domain-security.yml
created: '2026-09-04'
description: 'Transparent football (soccer) statistics and model predictions across 90+ leagues: league tables (classic, luck-adjusted, goals-based), results, fixtures with model probabilities, Dixon-Coles match probabilities, Monte Carlo season projections, goal-timing distributions, team match logs, and a public prediction track record. A single Dixon-Coles scoreline model produces one joint distribution per match, so 1X2, over/under and BTTS probabilities are mutually consistent by construction; season outcomes come from 10,000-run Monte Carlo simulations re-run daily. Every model signal is logged before kickoff and settled publicly. Offers a free read-only REST API with a self-describing JSON descriptor and a hosted MCP server whose tools/list is answerable anonymously.'
image: https://www.football-charts.com/fc_logo4.png
layout: provider
mcp_servers:
- description: ''
  name: Football Charts MCP Server
  slug: football-charts-mcp-server
- description: ''
  name: Football Charts MCP Server
  slug: football-charts-mcp-server-2
modified: '2026-09-04'
name: Football Charts
nav: Providers
network: true
overview: 'Football Charts publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include football, soccer, sports, sports-data, and statistics.


  Football Charts'' developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, authentication, and 18 more developer resources.'
plans:
- name: Football Charts Plans Pricing
  plan_count: 2
  slug: football-charts-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Football Charts Rate Limits
  slug: football-charts-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 26.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Football Charts Authentication
  slug: football-charts-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Football Charts Domain Security
  slug: football-charts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: football-charts
tags:
- football
- soccer
- sports
- sports-data
- statistics
- results
- standings
- fixtures
- predictions
- probability-models
- monte-carlo
- mcp
- agent-native
- free-api
website: https://www.football-charts.com
---
