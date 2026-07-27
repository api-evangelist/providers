---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Capella Space Agentic Access
  operation_count: 16
  slug: capella-space-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 9
apis:
- description: The Capella Tasking API lets customers submit imagery tasking requests against the Capella SAR constellation, configure collect parameters (geometry, resolution, polarization, look direction, off-nadi
  name: Capella Space Tasking API
  slug: capella-tasking-api
- description: The Capella Catalog API is a STAC-compliant search interface over the archive of SAR collects. Clients query the catalog by geometry, time, product type, resolution, and polarization to discover scene
  name: Capella Space Catalog API
  slug: capella-catalog-api
- description: The Capella Orders API submits and tracks orders for SAR products, manages order lifecycle, and returns signed download URLs for completed imagery via endpoints such as GET /orders/{orderId}/download.
  name: Capella Space Orders API
  slug: capella-orders-api
- description: The Collects API from Capella Space — 1 operation(s) for collects.
  name: Capella Space Collects API
  slug: capella-space-collects-api
- description: The Keys API from Capella Space — 1 operation(s) for keys.
  name: Capella Space Keys API
  slug: capella-space-keys-api
- description: The Orders API from Capella Space — 3 operation(s) for orders.
  name: Capella Space Orders API
  slug: capella-space-orders-api
- description: The RepeatRequests API from Capella Space — 4 operation(s) for repeatrequests.
  name: Capella Space RepeatRequests API
  slug: capella-space-repeatrequests-api
- description: The Tasking API from Capella Space — 4 operation(s) for tasking.
  name: Capella Space Tasking API
  slug: capella-space-tasking-api
- description: The Tiles API from Capella Space — 1 operation(s) for tiles.
  name: Capella Space Tiles API
  slug: capella-space-tiles-api
artifact_total: 31
collections:
- collection_type: open
  name: Capella Space API
  slug: open-capella-space
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/capella-space-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capella-space-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/capella-space-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.capellaspace.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.capellaspace.com/
- group: docs
  title: ''
  type: APIReference
  url: https://support.capellaspace.com/api-reference-and-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.capellaspace.com/
- group: start
  title: ''
  type: Console
  url: https://console.capellaspace.com/
- group: start
  title: ''
  type: Signup
  url: https://console.capellaspace.com/
- group: start
  title: ''
  type: Login
  url: https://console.capellaspace.com/
- group: operate
  title: ''
  type: Support
  url: https://support.capellaspace.com/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://support.capellaspace.com/
- group: company
  title: ''
  type: Blog
  url: https://www.capellaspace.com/insights
- group: company
  title: ''
  type: Newsroom
  url: https://www.capellaspace.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/capellaspace
- group: build
  title: ''
  type: SDKs
  url: https://github.com/capellaspace/console-client
- group: build
  title: ''
  type: SDKs
  url: https://capella-console-client.readthedocs.io/en/main/pages/api_reference.html
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/capellaspace/jupyter-notebooks
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/capellaspace/postman_collections
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/capellaspace/capella-reader
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/capella-space
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/capellaspace
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/CapellaSpace
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-23'
description: Capella Space operates a constellation of synthetic aperture radar (SAR) satellites and provides on-demand, high-resolution Earth-observation imagery through a self-service Console and public API. Customers can task the constellation with 15-minute scheduling cycles, search a STAC-based catalog of archive collects, place orders, and download imagery products for defense, intelligence, maritime, energy, insurance, and analytics use cases.
features:
- description: Self-service tasking of the SAR constellation with 15-minute scheduling cycles and multiple collection tiers.
  name: On-Demand SAR Tasking
- description: Spatio-Temporal Asset Catalog (STAC) compliant search interface for discovering archive collects.
  name: STAC Catalog
- description: Order management API for placing, tracking, and downloading SAR imagery products.
  name: Orders and Downloads
- description: SAR sensors collect through clouds and at night, providing reliable revisit for monitoring use cases.
  name: All-Weather, Day-Night Imaging
- description: Spotlight, stripmap, and sliding-spotlight products with sub-meter resolution options.
  name: Sub-0.5m Resolution Products
- description: Analytics products built on top of SAR collects for maritime domain awareness.
  name: Vessel Classification Analytics
- description: Subset of Capella imagery is available via the AWS Open Data registry.
  name: AWS Open Data
finops:
- name: Capella Space Finops
  service_category: API
  slug: capella-space-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/capella-space.png
integrations:
- description: Capella distributes imagery via AWS infrastructure and contributes to the AWS Open Data program.
  name: AWS
- description: Capella imagery is available through Esri's geospatial ecosystem.
  name: Esri ArcGIS
- description: Catalog conforms to the STAC specification, integrating with broader STAC tooling.
  name: STAC Ecosystem
layout: provider
modified: '2026-05-23'
name: Capella Space
nav: Providers
network: true
overview: 'Capella Space publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Collects API, Keys API, Orders API, and 3 more. Tagged areas include Synthetic Aperture Radar, SAR, Earth Observation, Satellite Imagery, and Geospatial.


  Capella Space''s developer surface includes authentication, documentation, API reference, getting-started guide, developer console, signup flow, support, and 16 more developer resources.'
plans:
- name: Capella Space Plans Pricing
  plan_count: 1
  slug: capella-space-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 2
  name: Capella Space Rate Limits
  slug: capella-space-rate-limits
score:
  band: developing
  composite: 46.7
  delta: 3.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 47.8
    developer_ergonomics: 56.5
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 43.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/capella-space/refs/heads/main/screenshots/capella-space-2026-06-20T173938.png
security:
- kind: authentication
  name: Capella Space Authentication
  slug: capella-space-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Capella Space Domain Security
  slug: capella-space-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: capella-space
tags:
- Synthetic Aperture Radar
- SAR
- Earth Observation
- Satellite Imagery
- Geospatial
- STAC
- Remote Sensing
- Tasking
- Catalog
use_cases:
- description: Persistent monitoring of areas of interest for defense and intelligence customers.
  name: Defense and Intelligence
- description: Vessel detection, classification, and dark-ship monitoring.
  name: Maritime Domain Awareness
- description: Monitoring of pipelines, refineries, and energy assets through cloud and darkness.
  name: Energy Infrastructure
- description: Rapid imagery tasking and delivery for floods, earthquakes, and wildfires.
  name: Disaster Response
- description: Pre- and post-event imagery for insurance underwriting and claims adjudication.
  name: Insurance and Claims
website: https://www.capellaspace.com
---
