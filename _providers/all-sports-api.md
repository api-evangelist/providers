---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: 'The All Sports Football (Soccer) API provides real-time and historical football data including livescores, fixtures, standings, team information, player statistics, and league data for major football '
  name: All Sports Football API
  slug: football-api
- description: 'The All Sports Basketball API provides real-time and historical basketball data including livescores, fixtures, standings, countries, and league information. The API supports major basketball leagues '
  name: All Sports Basketball API
  slug: basketball-api
- description: The All Sports Cricket API provides real-time and historical cricket data including livescores, fixtures, standings, and league information for major cricket competitions worldwide.
  name: All Sports Cricket API
  slug: cricket-api
- description: The All Sports Tennis API provides real-time and historical tennis data including livescores, fixtures, standings, and tournament information for major tennis competitions worldwide.
  name: All Sports Tennis API
  slug: tennis-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/all-sports-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allsportsapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://allsportsapi.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://allsportsapi.com/
- group: start
  title: ''
  type: SignUp
  url: https://allsportsapi.com/register
- group: build
  title: ''
  type: Packages
  url: packages/all-sports-api-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/all-sports-api-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/all-sports-api-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/all-sports-api-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/all-sports-api-lifecycle.yml
description: All Sports API is a fast, reliable, and comprehensive sports data API providing livescore feeds, fixtures, standings, and historical data for major sports worldwide. The platform offers JSON pull-based APIs for football (soccer), basketball, cricket, and tennis, with hockey, baseball, and American football available as additional sports. The API base URL is apiv2.allsportsapi.com and uses API key authentication with sport-specific endpoints accessed via the met query parameter. All Sports API also provides free embeddable widgets (results, fixtures, standings, livescore) and WordPress plugins. Plans include a 14-day free trial.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/all-sports-api.png
layout: provider
modified: '2026-06-20'
name: All Sports API
nav: Providers
network: true
overview: 'All Sports API publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Sports, Football, Soccer, Basketball, and Cricket.


  All Sports API''s developer surface includes documentation, pricing, signup flow, and 7 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 16.1
  delta: -0.4
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 16.5
  provenance:
    conformance: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/all-sports-api/refs/heads/main/screenshots/all-sports-api-2026-07-25T195637.png
security:
- kind: domain-security
  name: All Sports Api Domain Security
  slug: all-sports-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: all-sports-api
tags:
- Sports
- Football
- Soccer
- Basketball
- Cricket
- Tennis
- Livescore
- Sports Data
- Fixtures
- Standings
website: https://allsportsapi.com/
---
