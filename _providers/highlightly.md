---
access_model:
  confidence: high
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Highlightly Agentic Access
  operation_count: 24
  slug: highlightly-agentic-access
  summary_line: 24 operations
api_count: 7
apis:
- description: The Catalog API from Highlightly — 4 operation(s) for catalog.
  name: Highlightly Catalog API
  slug: highlightly-catalog-api
- description: The Highlights API from Highlightly — 3 operation(s) for highlights.
  name: Highlightly Highlights API
  slug: highlightly-highlights-api
- description: The Matches API from Highlightly — 6 operation(s) for matches.
  name: Highlightly Matches API
  slug: highlightly-matches-api
- description: The Odds API from Highlightly — 3 operation(s) for odds.
  name: Highlightly Odds API
  slug: highlightly-odds-api
- description: The Standings API from Highlightly — 1 operation(s) for standings.
  name: Highlightly Standings API
  slug: highlightly-standings-api
- description: The Statistics API from Highlightly — 5 operation(s) for statistics.
  name: Highlightly Statistics API
  slug: highlightly-statistics-api
- description: The Teams API from Highlightly — 2 operation(s) for teams.
  name: Highlightly Teams API
  slug: highlightly-teams-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Highlightly Sports Catalog API
  slug: open-highlightly-catalog-api
- collection_type: open
  name: Highlightly Sports Catalog Highlights API
  slug: open-highlightly-highlights-api
- collection_type: open
  name: Highlightly Sports Catalog Matches API
  slug: open-highlightly-matches-api
- collection_type: open
  name: Highlightly Sports Catalog Odds API
  slug: open-highlightly-odds-api
- collection_type: open
  name: Highlightly Sports Catalog Standings API
  slug: open-highlightly-standings-api
- collection_type: open
  name: Highlightly Sports Catalog Statistics API
  slug: open-highlightly-statistics-api
- collection_type: open
  name: Highlightly Sports Catalog Teams API
  slug: open-highlightly-teams-api
- collection_type: open
  name: Highlightly
  slug: open-highlightly
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/highlightly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/highlightly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/highlightly-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/highlightly
- group: company
  title: ''
  type: Website
  url: https://highlightly.net/
- group: docs
  title: ''
  type: Documentation
  url: https://highlightly.net/sport-api/documentation/
- group: commercial
  title: ''
  type: Plans
  url: plans/highlightly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/highlightly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/highlightly-finops.yml
created: '2026-06-25'
description: Highlightly is a real-time sports data and highlights API covering football, basketball, American football, hockey, baseball, cricket, rugby, volleyball, and handball across 950+ leagues. Its REST APIs serve live scores, matches, standings, team and player statistics, head-to-head records, odds, and on-demand video highlight clips, available directly via highlightly.net hosts or through RapidAPI.
finops:
- name: Highlightly Finops
  service_category: Analytics and Data
  slug: highlightly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/highlightly.png
layout: provider
modified: '2026-06-25'
name: Highlightly
nav: Providers
network: true
overview: 'Highlightly publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Highlights API, Matches API, and 4 more. Tagged areas include Sports, Sports Data, Live Scores, Odds, and Highlights.


  Highlightly''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Highlightly Plans Pricing
  plan_count: 4
  slug: highlightly-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 7
  name: Highlightly Rate Limits
  slug: highlightly-rate-limits
score:
  band: thin
  composite: 36.7
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.1
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/highlightly/refs/heads/main/screenshots/highlightly-2026-07-25T221204.png
security:
- kind: authentication
  name: Highlightly Authentication
  slug: highlightly-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Highlightly Domain Security
  slug: highlightly-domain-security
  summary_line: TLSv1.3 · HSTS
slug: highlightly
tags:
- Sports
- Sports Data
- Live Scores
- Odds
- Highlights
website: https://highlightly.net/
---
