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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Single GraphQL endpoint delivering Spire's satellite AIS maritime data - vessel positions, voyages, port calls, and predicted ETAs - with flexible querying for analytics and integration use cases. Now
  name: Spire Maritime 2.0 API (GraphQL)
  slug: maritime-graphql
- description: REST APIs and real-time event and tracking streams for global flight data, including space-based ADS-B positions, flight metadata, historic flights, and delayed tracking streams.
  name: Spire Aviation API
  slug: aviation
- description: RESTful weather and climate APIs covering global numerical weather prediction outputs, ocean currents, salinity, and 30 years of maritime weather history.
  name: Spire Weather and Climate API
  slug: weather
- description: Developer portal and APIs for Spire Space Services, exposing managed satellite operations, hosted payloads, and on-orbit asset interactions.
  name: Spire Space Services Developer API
  slug: space-services
- description: Radio-frequency geolocation data products delivering detected emitter positions for maritime domain awareness, security, and dark-vessel detection use cases. Delivered through enterprise data feeds.
  name: Spire RF Geolocation
  slug: rf-geolocation
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spire-global-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spire.com/
- group: other
  title: ''
  type: DeveloperResources
  url: https://spire.com/developers/
- group: docs
  title: ''
  type: MaritimeDocs
  url: https://documentation.spire.com/
- group: docs
  title: ''
  type: AviationDocs
  url: https://aviation-docs.spire.com/
- group: docs
  title: ''
  type: WeatherDocs
  url: https://developers.wx.spire.com/
- group: docs
  title: ''
  type: SpaceServicesDocs
  url: https://developers.spire.com/
- group: other
  title: ''
  type: Products
  url: https://www.spire.com/products/
- group: company
  title: ''
  type: Newsroom
  url: https://spire.com/newsroom/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spire-global
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spire-global/
- group: other
  title: ''
  type: X
  url: https://x.com/SpireGlobal
- group: company
  title: ''
  type: BlogRSS
  url: https://spire.com/feed/
created: '2026-05-23'
description: 'Spire Global operates a constellation of more than 100 LEMUR nanosatellites collecting maritime AIS, aviation ADS-B, GNSS-RO weather profiles, and RF geolocation data, and offers Space Services for hosted payloads and managed satellite missions. Its data products are exposed as developer-friendly APIs: Spire Maritime 2.0 (now operated by Kpler) delivers vessel-tracking AIS through a GraphQL endpoint; Spire Aviation publishes REST APIs and real-time streams for flight metadata, live ADS-B tracking, historic positions, and event feeds; Spire Weather and Climate provides RESTful weather and ocean data APIs including 30 years of maritime weather history; and Spire Space Services exposes a developer portal for managed satellite operations. Spire''s APIs are documented at product-specific subdomains and authenticated with API keys.'
finops:
- name: Spire Global Finops
  service_category: API
  slug: spire-global-finops
graphqls:
- description: Single GraphQL endpoint delivering Spire's satellite AIS maritime data - vessel positions, voyages, port calls, and predicted ETAs - with flexible querying for analytics and integration use cases. Now
  name: Spire Global GraphQL API
  slug: spire-global-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spire-global.png
layout: provider
modified: '2026-05-23'
name: Spire Global
nav: Providers
network: true
overview: Spire Global publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Satellites, Earth Observation, AIS, Maritime, and ADS-B.
plans:
- name: Spire Global Plans Pricing
  plan_count: 1
  slug: spire-global-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Spire Global Rate Limits
  slug: spire-global-rate-limits
score:
  band: emerging
  composite: 16.6
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spire-global/refs/heads/main/screenshots/spire-global-2026-06-20T194320.png
security:
- kind: domain-security
  name: Spire Global Domain Security
  slug: spire-global-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spire-global
tags:
- Satellites
- Earth Observation
- AIS
- Maritime
- ADS-B
- Aviation
- Weather
- RF Geolocation
- GraphQL
- LEMUR
- GNSS-RO
website: https://spire.com/
---
