---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: Atlas is the Abios REST and WebSocket data API delivering fixtures, live match state, historical stats, players, teams, tournaments, and series across covered esports titles. Designed as a developer-f
  name: Abios Atlas API
  slug: atlas-api
- description: Pre-match and live esports odds feed including player props and live betting markets, packaged for sportsbook integration alongside the Atlas data feed.
  name: Abios Esports Odds
  slug: odds-api
- description: Embeddable esports widgets (live scoreboards, event feeds, statistics displays) backed by the Atlas data feed for media and sportsbook front-ends.
  name: Abios Esports Widgets
  slug: widgets-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abios-gaming-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abiosgaming.com/
- group: docs
  title: ''
  type: Documentation
  url: https://abiosgaming.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://abiosgaming.com/api-reference/atlas
- group: build
  title: ''
  type: GitHub
  url: https://github.com/AbiosGaming
- group: company
  title: ''
  type: Careers
  url: https://jobs.abiosgaming.com/
- group: other
  title: Sportradar (parent company)
  type: Parent
  url: https://sportradar.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abiosgaming.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abiosgaming.com/terms
- group: operate
  title: ''
  type: Contact
  url: https://abiosgaming.com/contact
- group: agent
  title: ''
  type: LlmsText
  url: https://jobs.abiosgaming.com/llms.txt
created: '2026-05-23'
description: Abios, a Sportradar company headquartered in Stockholm, provides enterprise-scale esports data, odds, and engagement products for sportsbooks and media platforms. The Abios Atlas API delivers REST and WebSocket access to fixtures, live statistics, odds, and player props across 60,000+ yearly matches and 50 billion+ data points spanning major esports titles plus traditional sports coverage via Sportradar integration.
finops:
- name: Abios Gaming Finops
  service_category: API
  slug: abios-gaming-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/abios-gaming.png
layout: provider
modified: '2026-05-23'
name: Abios (Sportradar)
nav: Providers
network: true
overview: 'Abios (Sportradar) publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Esports, Sports Data, Odds, Widgets, and Live Data.


  Abios (Sportradar)''s developer surface includes documentation, API reference, GitHub presence, and 8 more developer resources.'
plans:
- name: Abios Gaming Plans Pricing
  plan_count: 1
  slug: abios-gaming-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 2
  name: Abios Gaming Rate Limits
  slug: abios-gaming-rate-limits
score:
  band: emerging
  composite: 23.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abios-gaming/refs/heads/main/screenshots/abios-gaming-2026-06-20T163209.png
security:
- kind: domain-security
  name: Abios Gaming Domain Security
  slug: abios-gaming-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: abios-gaming
tags:
- Esports
- Sports Data
- Odds
- Widgets
- Live Data
- WebSocket
- REST
- Sportradar
website: https://abiosgaming.com/
---
