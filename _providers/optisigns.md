---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 5
apis:
- description: Query and manage the devices (screens) paired to an OptiSigns account. List devices, look them up by name or ID, create and update device settings, reboot a device, push content, and delete devices. C
  name: OptiSigns Devices API
  slug: optisigns-devices-api
- description: Manage the content assets displayed on screens - upload file assets (images, video, documents), create website and app assets, modify asset settings, list and fetch assets by filename, and delete asse
  name: OptiSigns Assets API
  slug: optisigns-assets-api
- description: Create and manage playlists - ordered sequences of assets with per-item durations - and assign them to devices. Playlists are a documented OptiSigns resource type covered by the API cookbook; the spec
  name: OptiSigns Playlists API
  slug: optisigns-playlists-api
- description: Create and manage schedules that control when assets and playlists play on which devices across dates, times, and recurrence. Schedules are a documented OptiSigns resource type covered by the API cook
  name: OptiSigns Schedules API
  slug: optisigns-schedules-api
- description: Organize devices and assets into teams (sub-accounts) for multi-location and multi-tenant management. Teams are a documented OptiSigns resource type referenced by the API cookbook; the specific GraphQ
  name: OptiSigns Teams API
  slug: optisigns-teams-api
artifact_total: 13
collections:
- collection_type: open
  name: OptiSigns GraphQL API
  slug: open-optisigns
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/optisigns-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/optisigns-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optisigns-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/optisigns
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/optisigns
- group: company
  title: ''
  type: Website
  url: https://www.optisigns.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.optisigns.com
- group: commercial
  title: ''
  type: Plans
  url: plans/optisigns-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/optisigns-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/optisigns-finops.yml
- group: build
  title: ''
  type: SDK
  url: https://github.com/optisigns/optisigns-node
created: '2026-07-05'
description: OptiSigns is a cloud digital signage platform that turns any TV or display into a digital sign using low-cost media players (Android, Amazon Fire TV, Raspberry Pi, ProDVX, and others). Screens, media assets, playlists, and schedules are managed centrally from the OptiSigns dashboard. Developers manage the same resources programmatically through the OptiSigns GraphQL API, which is served from a single endpoint at https://graphql-gateway.optisigns.com/graphql and authenticated with a Bearer API key. API access is a paid capability available on the Pro Plus plan and higher; the API covers devices (screens), assets (content), playlists, schedules, and team management. Official TypeScript/JavaScript and Python SDKs plus an API cookbook are published on GitHub.
finops:
- name: Optisigns Finops
  service_category: Digital Signage
  slug: optisigns-finops
graphqls:
- description: OptiSigns is a cloud digital signage platform. Its public developer API is **GraphQL only** - there is no REST API. All operations run against a single endpoint, and the same URL serves an interactive
  name: OptiSigns GraphQL API
  slug: optisigns-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optisigns.png
layout: provider
modified: '2026-07-05'
name: OptiSigns
nav: Providers
network: true
overview: 'OptiSigns publishes 2 APIs on the [APIs.io](https://apis.io/) network: Devices API and Assets API. Tagged areas include Digital Signage, Screens, Content Management, GraphQL, and Displays.


  OptiSigns'' developer surface includes documentation, SDKs, and 9 more developer resources.'
plans:
- name: Optisigns Plans Pricing
  plan_count: 6
  slug: optisigns-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 3
  name: Optisigns Rate Limits
  slug: optisigns-rate-limits
score:
  band: thin
  composite: 35.5
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 43.2
    developer_ergonomics: 15.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optisigns/refs/heads/main/screenshots/optisigns-2026-08-07T190813.png
security:
- kind: domain-security
  name: Optisigns Domain Security
  slug: optisigns-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Optisigns Vulnerability Disclosure
  slug: optisigns-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Optisigns Trust Center
  slug: optisigns-trust-center
  summary_line: SOC 2
slug: optisigns
tags:
- Digital Signage
- Screens
- Content Management
- GraphQL
- Displays
- Playlists
website: https://www.optisigns.com
---
