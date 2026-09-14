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
  title: ''
  type: DomainSecurity
  url: security/playerdata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.playerdata.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/playerdata-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/playerdata-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/playerdata-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/playerdata-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/playerdata-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/playerdata-events-asyncapi.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/playerdata-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/playerdata-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/playerdata-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/playerdata-well-known.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/PlayerData/playerdatapy/blob/main/docs/auth.md
- group: docs
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
random_paper: 13
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
website: https://www.playerdata.com/
---
