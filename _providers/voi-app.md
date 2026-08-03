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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: Voi's read-only open mobility API surface, exposing GBFS v2/v3 auto-discovery, system information, free bike status (with optional battery extension), and service areas, plus MDS 0.4 trips, status_cha
  name: Voi MaaS Light API
  slug: voi-maas-light-api
- description: Voi's commercial Partner API enabling MaaS partners to embed full ride journeys in their apps — register users, start and end rentals, look up active and historical rentals for a user, discover availa
  name: Voi MaaS Pro API
  slug: voi-maas-pro-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voi-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.voi.com
- group: start
  title: ''
  type: Portal
  url: https://docs.voiscooters.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/voiapp/partner-api-docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/voiapp
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/voiapp/mobility-data-specification
- group: other
  title: ''
  type: Company
  url: https://www.voi.com/about
- group: company
  title: ''
  type: About
  url: https://careers.voi.com/pages/our-voiage-so-far
- group: company
  title: ''
  type: Careers
  url: https://careers.voi.com/
- group: company
  title: ''
  type: PressRoom
  url: https://www.voi.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.voi.com/blog
- group: operate
  title: ''
  type: Help
  url: https://www.voi.com/support
- group: operate
  title: ''
  type: Contact
  url: https://www.voi.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.voi.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.voi.com/legal/privacy-notice
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/voi-technology
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voi-technology/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/voiscooters
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/voiscooters/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@VoiTechnology
created: '2026-05-25'
description: Voi Technology is a Stockholm-based shared micromobility operator founded in August 2018 by Fredrik Hjelm, Adam Jafer, Filip Lindvall, and Douglas Stark. The company runs Europe's largest shared e-scooter and e-bike fleet, with 150,000+ vehicles deployed across 110+ towns and cities in 13 European countries, serving 8+ million riders who have completed 400+ million trips. Voi has been EBIT-profitable since 2024 and in 2026 unveiled a refreshed vehicle family including a new e-scooter model and two upgraded e-bikes, with first deployments in Stockholm. Voi exposes a public Partner API surface (MaaS Light and MaaS Pro) and standards-based open mobility feeds — GBFS v2/v3 for vehicle locations and system information, and MDS 0.4 for trips, status changes, and events — used by cities and MaaS aggregators across Europe. The Partner API also covers user registration, rental lifecycle (start/end), vehicle and zone discovery, pricing, payments, deeplinks, asset access, and customer
  support flows. Voi additionally publishes a GitHub organization (github.com/voiapp) hosting partner API docs, an iOS networking layer, a VIPER framework, an MDS fork, and internal tooling.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/voi-app.png
layout: provider
modified: '2026-05-25'
name: Voi
nav: Providers
network: true
overview: 'Voi publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Micromobility, Shared Mobility, E-Scooters, E-Bikes, and Transportation.


  Voi''s developer surface includes developer portal, documentation, engineering blog, YouTube channel, and 16 more developer resources.'
random_paper: 35
score:
  band: emerging
  composite: 14.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/voi-app/refs/heads/main/screenshots/voi-app-2026-06-20T201128.png
security:
- kind: domain-security
  name: Voi App Domain Security
  slug: voi-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voi-app
tags:
- Micromobility
- Shared Mobility
- E-Scooters
- E-Bikes
- Transportation
- MaaS
- Mobility As A Service
- GBFS
- MDS
- Open Mobility
- Smart Cities
- Sweden
- Europe
website: https://www.voi.com
---
