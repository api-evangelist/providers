---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Oddsjam Agentic Access
  operation_count: 38
  slug: oddsjam-agentic-access
  summary_line: 38 operations · 3 acting · 1 human-in-the-loop
api_count: 12
apis:
- description: The Fixtures API from OddsJam — 11 operation(s) for fixtures.
  name: OddsJam Fixtures API
  slug: oddsjam-fixtures-api
- description: The Futures API from OddsJam — 2 operation(s) for futures.
  name: OddsJam Futures API
  slug: oddsjam-futures-api
- description: The Grader API from OddsJam — 3 operation(s) for grader.
  name: OddsJam Grader API
  slug: oddsjam-grader-api
- description: The Injuries API from OddsJam — 2 operation(s) for injuries.
  name: OddsJam Injuries API
  slug: oddsjam-injuries-api
- description: The Leagues API from OddsJam — 2 operation(s) for leagues.
  name: OddsJam Leagues API
  slug: oddsjam-leagues-api
- description: The Markets API from OddsJam — 4 operation(s) for markets.
  name: OddsJam Markets API
  slug: oddsjam-markets-api
- description: The Players API from OddsJam — 1 operation(s) for players.
  name: OddsJam Players API
  slug: oddsjam-players-api
- description: The Sports API from OddsJam — 2 operation(s) for sports.
  name: OddsJam Sports API
  slug: oddsjam-sports-api
- description: The Sportsbooks API from OddsJam — 3 operation(s) for sportsbooks.
  name: OddsJam Sportsbooks API
  slug: oddsjam-sportsbooks-api
- description: The Streaming API from OddsJam — 3 operation(s) for streaming.
  name: OddsJam Streaming API
  slug: oddsjam-streaming-api
- description: The Teams API from OddsJam — 3 operation(s) for teams.
  name: OddsJam Teams API
  slug: oddsjam-teams-api
- description: The Tournaments API from OddsJam — 2 operation(s) for tournaments.
  name: OddsJam Tournaments API
  slug: oddsjam-tournaments-api
artifact_total: 35
asyncapis:
- description: 'Real-time streaming surface for the OddsJam / OpticOdds Sports Betting API. Two delivery mechanisms are publicly documented: 1. Server-Sent Events (SSE) over long-lived HTTPS connections for odds, res'
  name: OddsJam (OpticOdds) Streaming API
  slug: oddsjam-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OddsJam Fixtures API
  slug: open-oddsjam-fixtures-api
- collection_type: open
  name: OddsJam Fixtures Futures API
  slug: open-oddsjam-futures-api
- collection_type: open
  name: OddsJam Fixtures Grader API
  slug: open-oddsjam-grader-api
- collection_type: open
  name: OddsJam Fixtures Injuries API
  slug: open-oddsjam-injuries-api
- collection_type: open
  name: OddsJam Fixtures Leagues API
  slug: open-oddsjam-leagues-api
- collection_type: open
  name: OddsJam Fixtures Markets API
  slug: open-oddsjam-markets-api
- collection_type: open
  name: OddsJam Fixtures Players API
  slug: open-oddsjam-players-api
- collection_type: open
  name: OddsJam Fixtures Sports API
  slug: open-oddsjam-sports-api
- collection_type: open
  name: OddsJam Fixtures Sportsbooks API
  slug: open-oddsjam-sportsbooks-api
- collection_type: open
  name: OddsJam Fixtures Streaming API
  slug: open-oddsjam-streaming-api
- collection_type: open
  name: OddsJam Fixtures Teams API
  slug: open-oddsjam-teams-api
- collection_type: open
  name: OddsJam Fixtures Tournaments API
  slug: open-oddsjam-tournaments-api
- collection_type: open
  name: OddsJam API
  slug: open-oddsjam
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oddsjam-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/oddsjam-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oddsjam-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oddsjam-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oddsjam
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/oddsjam-inc
- group: company
  title: ''
  type: Website
  url: https://oddsjam.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://oddsjam.com/llms.txt
created: '2025-02-08'
description: OddsJam's Sports Betting API offers real-time betting odds from 100+ sportsbooks including player props, alternate markets, injury data, schedules, rankings, and scores for sports betting applications.
finops:
- name: Oddsjam Finops
  service_category: API
  slug: oddsjam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oddsjam.png
layout: provider
modified: '2026-05-30'
name: OddsJam
nav: Providers
network: true
overview: 'OddsJam publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Fixtures API, Futures API, Grader API, and 9 more. Tagged areas include Odds, Sports Betting, and Sportsbooks.


  The OddsJam catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  OddsJam''s developer surface includes authentication and 7 more developer resources.'
plans:
- name: Oddsjam Plans Pricing
  plan_count: 3
  slug: oddsjam-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Oddsjam Rate Limits
  slug: oddsjam-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: OddsJam API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 8
  slug: oddsjam-asyncapi-spectral-rules
score:
  band: thin
  composite: 27.6
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 11.4
    contract_quality: 55.2
    developer_ergonomics: 11.9
    discoverability: 55.6
    governance: 11.4
    operational_transparency: 10.5
  previous_composite: 27.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oddsjam/refs/heads/main/screenshots/oddsjam-2026-06-20T190620.png
security:
- kind: authentication
  name: Oddsjam Authentication
  slug: oddsjam-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Oddsjam Domain Security
  slug: oddsjam-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Oddsjam Vulnerability Disclosure
  slug: oddsjam-vulnerability-disclosure
  summary_line: disclosure policy published
slug: oddsjam
tags:
- Odds
- Sports Betting
- Sportsbooks
website: https://oddsjam.com/
---
