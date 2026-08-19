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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Opticodds Agentic Access
  operation_count: 16
  slug: opticodds-agentic-access
  summary_line: 16 operations
api_count: 6
apis:
- description: OpticOdds Sports Betting API offers real-time betting odds for main lines, player props, alternate markets, injury data, schedules, ranking, scores and more for sports betting applications.
  name: OpticOdds
  slug: opticodds
- description: Fixtures and odds.
  name: OpticOdds Fixtures API
  slug: opticodds-fixtures-api
- description: Futures markets and odds.
  name: OpticOdds Futures API
  slug: opticodds-futures-api
- description: Injuries and injury predictions.
  name: OpticOdds Injuries API
  slug: opticodds-injuries-api
- description: Sports, leagues, sportsbooks, market types.
  name: OpticOdds Reference API
  slug: opticodds-reference-api
- description: Game and player results.
  name: OpticOdds Results API
  slug: opticodds-results-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opticodds-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opticodds-domain-security.yml
- group: auth
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
- group: company
  title: ''
  type: Blog
  url: https://opticodds.com/blog
created: '2025-02-08'
description: OpticOdds Sports Betting API offers real-time betting odds for main lines, player props, alternate markets, injury data, schedules, ranking, scores and more for sports betting applications.
finops:
- name: Opticodds Finops
  service_category: API
  slug: opticodds-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opticodds.png
layout: provider
modified: '2026-03-16'
name: OpticOdds
nav: Providers
network: true
overview: 'OpticOdds publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Fixtures API, Futures API, Injuries API, and 2 more. Tagged areas include Odds, Sports Betting, and Sports Data.


  OpticOdds'' developer surface includes authentication, engineering blog, and 5 more developer resources.'
plans:
- name: Opticodds Plans Pricing
  plan_count: 3
  slug: opticodds-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 5
  name: Opticodds Rate Limits
  slug: opticodds-rate-limits
score:
  band: emerging
  composite: 25.2
  delta: -0.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 14.3
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 26.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opticodds/refs/heads/main/screenshots/opticodds-2026-06-20T191108.png
security:
- kind: authentication
  name: Opticodds Authentication
  slug: opticodds-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Opticodds Domain Security
  slug: opticodds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opticodds
tags:
- Odds
- Sports Betting
- Sports Data
---
