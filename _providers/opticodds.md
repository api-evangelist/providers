---
access_model:
  confidence: high
  label: Contact sales · Sales-assisted onboarding
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 3
  name: Opticodds Agentic Access
  operation_count: 51
  slug: opticodds-agentic-access
  summary_line: 51 operations · 8 acting · 3 human-in-the-loop
api_count: 2
apis:
- description: First-party Model Context Protocol server exposing 16 read-only OpticOdds tools — odds, fixtures, player props, injuries, results, line history, best-price and outlier detection, line comparison and b
  name: OpticOdds MCP Server
  slug: opticodds-mcp
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: Fixtures and odds.
  name: OpticOdds Fixtures API
  slug: opticodds-fixtures-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: Futures markets and odds.
  name: OpticOdds Futures API
  slug: opticodds-futures-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: Injuries and injury predictions.
  name: OpticOdds Injuries API
  slug: opticodds-injuries-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: Game and player results.
  name: OpticOdds Results API
  slug: opticodds-results-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The conferences API from OpticOdds — 1 operation(s) for conferences.
  name: OpticOdds Conferences API
  slug: opticodds-conferences-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The copilot API from OpticOdds — 5 operation(s) for copilot.
  name: OpticOdds Copilot API
  slug: opticodds-copilot-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The divisions API from OpticOdds — 1 operation(s) for divisions.
  name: OpticOdds Divisions API
  slug: opticodds-divisions-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The grader API from OpticOdds — 2 operation(s) for grader.
  name: OpticOdds Grader API
  slug: opticodds-grader-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The leagues API from OpticOdds — 2 operation(s) for leagues.
  name: OpticOdds Leagues API
  slug: opticodds-leagues-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The market-types API from OpticOdds — 1 operation(s) for market-types.
  name: OpticOdds Market Types API
  slug: opticodds-market-types-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The markets API from OpticOdds — 2 operation(s) for markets.
  name: OpticOdds Markets API
  slug: opticodds-markets-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The odds API from OpticOdds — 3 operation(s) for odds.
  name: OpticOdds Odds API
  slug: opticodds-odds-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The parlay API from OpticOdds — 3 operation(s) for parlay.
  name: OpticOdds Parlay API
  slug: opticodds-parlay-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The players API from OpticOdds — 1 operation(s) for players.
  name: OpticOdds Players API
  slug: opticodds-players-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The queue API from OpticOdds — 10 operation(s) for queue.
  name: OpticOdds Queue API
  slug: opticodds-queue-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The sports API from OpticOdds — 2 operation(s) for sports.
  name: OpticOdds Sports API
  slug: opticodds-sports-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The sportsbooks API from OpticOdds — 3 operation(s) for sportsbooks.
  name: OpticOdds Sportsbooks API
  slug: opticodds-sportsbooks-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The teams API from OpticOdds — 1 operation(s) for teams.
  name: OpticOdds Teams API
  slug: opticodds-teams-api
- baseURL: https://api.opticodds.com/api/v3
  baseurl_source: declared
  description: The tournaments API from OpticOdds — 2 operation(s) for tournaments.
  name: OpticOdds Tournaments API
  slug: opticodds-tournaments-api
artifact_total: 38
collections:
- collection_type: open
  name: OpticOdds Sports Betting Fixtures API
  slug: open-opticodds-fixtures-api
- collection_type: open
  name: OpticOdds Sports Betting Fixtures Futures API
  slug: open-opticodds-futures-api
- collection_type: open
  name: OpticOdds Sports Betting Fixtures Injuries API
  slug: open-opticodds-injuries-api
- collection_type: open
  name: OpticOdds Sports Betting Fixtures Reference API
  slug: open-opticodds-reference-api
- collection_type: open
  name: OpticOdds Sports Betting Fixtures Results API
  slug: open-opticodds-results-api
- collection_type: open
  name: OpticOdds Sports Betting API
  slug: open-opticodds
common:
- group: company
  title: ''
  type: Website
  url: https://opticodds.com/
- group: agent
  href: https://artifacts.apis.io/opticodds/agentic-access/opticodds-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/opticodds-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/opticodds/security/opticodds-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opticodds-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/opticodds/authentication/opticodds-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opticodds-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpticOdds
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opticodds
- group: agent
  title: ''
  type: LlmsText
  url: https://opticodds.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/opticodds/llms/opticodds-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/opticodds-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://opticodds.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.opticodds.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.opticodds.com/reference/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.opticodds.com/reference/get_fixtures-odds
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.opticodds.com/docs/odds-api-getting-started-guide
- group: operate
  title: ''
  type: Support
  url: https://opticodds.com/contact
- group: operate
  title: ''
  type: Community
  url: https://developer.opticodds.com/discuss
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opticodds.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opticodds.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opticodds.com/
- group: design
  href: https://artifacts.apis.io/opticodds/lifecycle/opticodds-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/opticodds-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/opticodds/changelog/opticodds-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/opticodds-changelog.yml
- group: design
  href: https://artifacts.apis.io/opticodds/conventions/opticodds-conventions.yml
  title: ''
  type: Conventions
  url: conventions/opticodds-conventions.yml
- group: design
  href: https://artifacts.apis.io/opticodds/errors/opticodds-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/opticodds-problem-types.yml
- group: design
  href: https://artifacts.apis.io/opticodds/data-model/opticodds-data-model.yml
  title: ''
  type: DataModel
  url: data-model/opticodds-data-model.yml
- group: design
  href: https://artifacts.apis.io/opticodds/conformance/opticodds-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opticodds-conformance.yml
- group: build
  href: https://artifacts.apis.io/opticodds/packages/opticodds-packages.yml
  title: ''
  type: Packages
  url: packages/opticodds-packages.yml
- group: agent
  href: https://artifacts.apis.io/opticodds/mcp/opticodds-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/opticodds-mcp.yml
- group: build
  href: https://artifacts.apis.io/opticodds/mcp/opticodds-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/opticodds-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/opticodds/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/opticodds/overlays/opticodds-api-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/opticodds-api-v3-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/opticodds/plans/opticodds-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/opticodds-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/opticodds/rate-limits/opticodds-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/opticodds-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/opticodds/finops/opticodds-finops.yml
  title: ''
  type: FinOps
  url: finops/opticodds-finops.yml
- group: agent
  href: https://artifacts.apis.io/opticodds/well-known/opticodds-well-known.yml
  title: ''
  type: WellKnownProbe
  url: well-known/opticodds-well-known.yml
created: '2025-02-08'
description: OpticOdds is a B2B sports betting data provider whose v3 REST API delivers real-time and historical odds aggregated from 200+ sportsbooks, covering main lines, player props, alternate markets, futures, injuries and injury predictions, fixtures, results, and same-game-parlay pricing. The platform serves sportsbook operators and traders, prediction markets, platform providers, DFS operators, betting apps, and media and affiliate businesses. Alongside the polling API it publishes Server-Sent Events streaming endpoints and RabbitMQ push queues, a bet-settlement grader, and a first-party Model Context Protocol server available both as a hosted endpoint and as an npm package. OpticOdds is part of Gambling.com Group.
finops:
- has_sources: true
  method: derived
  name: Opticodds Finops
  primary_unit: ''
  service_category: ''
  slug: opticodds-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opticodds.png
layout: provider
mcp_servers:
- description: 'OpticOdds ships a first-party Model Context Protocol server in BOTH deployment shapes: a hosted remote endpoint an MCP client can POST to today, and an npm-distributed local stdio server launched with'
  name: OpticOdds MCP
  slug: opticodds-mcp
modified: '2026-08-27'
name: OpticOdds
nav: Providers
network: true
overview: 'OpticOdds publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Fixtures API, Futures API, Injuries API, and 17 more. Tagged areas include Odds, Sports Betting, Sports Data, Real-Time Data, and Streaming.


  The OpticOdds catalog on APIs.io includes 1 Spectral governance ruleset.


  OpticOdds'' developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, changelog, and 26 more developer resources.'
plans:
- name: Opticodds Plans Pricing
  plan_count: 0
  slug: opticodds-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Opticodds Rate Limits
  slug: opticodds-rate-limits
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: OpticOdds API Rules
  rule_count: 70
  severity_counts:
    error: 65
    hint: 0
    info: 2
    warn: 3
  slug: opticodds-rules
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.8
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 51.0
    developer_ergonomics: 54.2
    discoverability: 75.0
    operational_transparency: 57.9
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/opticodds/opticodds-2026-06-20T191108.png
security:
- kind: authentication
  name: Opticodds Authentication
  slug: opticodds-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Opticodds Domain Security
  slug: opticodds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: opticodds-compare-lines
  slug: opticodds-compare-lines
- name: opticodds-grade-settled-bets
  slug: opticodds-grade-settled-bets
- name: opticodds-stream-live-odds
  slug: opticodds-stream-live-odds
- name: opticodds-track-injuries
  slug: opticodds-track-injuries
slug: opticodds
tags:
- Odds
- Sports Betting
- Sports Data
- Real-Time Data
- Streaming
- Fixtures
- Injuries
- Prediction Markets
- MCP
website: https://opticodds.com/
---
