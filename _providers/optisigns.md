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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-25'
api_count: 5
apis:
- baseURL: https://graphql-gateway.optisigns.com/graphql
  baseurl_source: declared
  description: Query and manage the devices (screens) paired to an OptiSigns account. List devices, look them up by name or ID, create and update device settings, reboot a device, push content, and delete devices. C
  name: OptiSigns Devices API
  slug: optisigns-devices-api
- baseURL: https://graphql-gateway.optisigns.com/graphql
  baseurl_source: declared
  description: Manage the content assets displayed on screens - upload file assets (images, video, documents), create website and app assets, modify asset settings, list and fetch assets by filename, and delete asse
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
  href: https://raw.githubusercontent.com/api-evangelist/optisigns/refs/heads/main/security/optisigns-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/optisigns-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/optisigns/refs/heads/main/security/optisigns-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/optisigns-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/optisigns/refs/heads/main/security/optisigns-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/optisigns/refs/heads/main/plans/optisigns-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/optisigns-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/optisigns/refs/heads/main/rate-limits/optisigns-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/optisigns-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/optisigns/refs/heads/main/finops/optisigns-finops.yml
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
overview: 'OptiSigns publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Assets API, and 3 more. Tagged areas include Digital Signage, Screens, Content Management, GraphQL, and Displays.


  OptiSigns'' developer surface includes documentation, SDKs, and 9 more developer resources.'
plans:
- name: Optisigns Plans Pricing
  plan_count: 6
  slug: optisigns-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Optisigns Rate Limits
  slug: optisigns-rate-limits
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 64.6
    catalog_earned_first_party: 0.0
    catalog_gap: 50.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 44.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.1
    discoverability: 71.4
    operational_transparency: 31.1
  previous_composite: 27.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
