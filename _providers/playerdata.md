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
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.4
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: OAuth2-secured GraphQL API for PlayerData sports performance data — clubs, athletes, sessions, devices, metrics, reports and real-time subscription events.
  name: PlayerData GraphQL API
  slug: playerdata-graphql-api
artifact_total: 4
asyncapis:
- description: 'Server-emitted real-time events exposed by the PlayerData GraphQL API via RootSubscription. Derived from the published GraphQL schema; each channel maps to a GraphQL subscription field delivered over '
  name: PlayerData Real-Time Events (GraphQL Subscriptions)
  slug: playerdata-events-asyncapi
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/playerdata/refs/heads/main/security/playerdata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/playerdata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.playerdata.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/playerdata/refs/heads/main/authentication/playerdata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/playerdata-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/playerdata/refs/heads/main/packages/playerdata-packages.yml
  title: ''
  type: Packages
  url: packages/playerdata-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/playerdata/refs/heads/main/packages/playerdata-packages.yml
  title: ''
  type: SDKs
  url: packages/playerdata-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/playerdata/refs/heads/main/conventions/playerdata-conventions.yml
  title: ''
  type: Conventions
  url: conventions/playerdata-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/playerdata/refs/heads/main/data-model/playerdata-data-model.yml
  title: ''
  type: DataModel
  url: data-model/playerdata-data-model.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/playerdata/refs/heads/main/asyncapi/playerdata-events-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/playerdata-events-asyncapi.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/playerdata/refs/heads/main/mcp/playerdata-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/playerdata-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/playerdata/refs/heads/main/llms/playerdata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/playerdata-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/playerdata/refs/heads/main/conformance/playerdata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/playerdata-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/playerdata/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/playerdata/refs/heads/main/well-known/playerdata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/playerdata-well-known.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/PlayerData/playerdatapy/blob/main/docs/auth.md
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/playerdata/refs/heads/main/graphql/playerdata-schema.graphql
  title: ''
  type: APIReference
  url: graphql/playerdata-schema.graphql
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PlayerData
- group: operate
  title: ''
  type: Support
  url: https://support.playerdata.com/knowledge
- group: company
  title: ''
  type: Blog
  url: https://www.playerdata.com/blog
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.playerdata.com/
- group: start
  title: ''
  type: Login
  url: https://app.playerdata.co.uk/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.playerdata.com/en-gb/privacy-policy-iframe
created: '2026-07-17'
description: PlayerData provides GPS sports performance tracking technology for athletes and teams — FIFA Quality Certified EDGE wearable trackers, a GPS-enabled Connected Ball, and indoor IMU / local-positioning systems. Its platform captures distance, speed, sprints, acceleration/deceleration and workload, and exposes a GraphQL API secured with OAuth 2.0 covering clubs, athletes, sessions, devices, metrics and reports, plus real-time GraphQL subscription events. Official Python (playerdatapy) and R (playerdatar) client libraries wrap the API. PlayerData is a Techstars portfolio company.
image: https://www.playerdata.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: PlayerData
nav: Providers
network: true
overview: 'PlayerData publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Sports Performance, GPS Tracking, and Wearables.


  The PlayerData catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PlayerData''s developer surface includes authentication, documentation, API reference, support, engineering blog, and 16 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 25.0
    contract_governance: 4.5
    contract_quality: 51.0
    developer_ergonomics: 44.6
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 35.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/playerdata/refs/heads/main/screenshots/playerdata-2026-09-02T151456.png
security:
- kind: authentication
  name: Playerdata Authentication
  slug: playerdata-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: Playerdata Domain Security
  slug: playerdata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: playerdata
tags:
- Company
- Sports
- Sports Performance
- GPS Tracking
- Wearables
- Athlete Monitoring
- GraphQL
- Analytics
- Real-Time
website: https://www.playerdata.com/
---
