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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Unified Orders API in Aleph V2 that consolidates archive purchases and new-capture tasking into a single REST surface. Supports archive products, POI (point-of-interest) tasking, and AOI (area-of-inte
  name: Satellogic Aleph V2 Orders API
  slug: aleph-v2-orders-api
- description: Legacy Aleph V1 Tasking API for submitting and tracking imagery collection orders against the Satellogic NewSat constellation. Supports multiple tasking product types defined by geometry (point, polyg
  name: Satellogic Aleph V1 Tasking API
  slug: aleph-v1-tasking-api
- description: Search and order historical Satellogic imagery from the archive, including L1 Basic (L1B) multispectral products and hyperspectral products. Provides catalog discovery by AOI, date range, cloud cover,
  name: Satellogic Aleph V1 Archive API
  slug: aleph-v1-archive-api
- description: Feasibility analysis API that lets customers evaluate the likelihood and timing of a prospective tasking request — including pass opportunities, sun and look-angle constraints, and expected revisit ca
  name: Satellogic Aleph V1 Analysis API
  slug: aleph-v1-analysis-api
- description: Asset retrieval API for downloading processed imagery products and derived artifacts once a tasking or archive order is fulfilled. Provides scene listings, signed download URLs, and delivery status ac
  name: Satellogic Aleph V1 Delivery API
  slug: aleph-v1-delivery-api
- description: OAuth 2.0 Client Credentials flow used by all Aleph APIs. Customers generate API credentials inside the Aleph web platform (aleph.satellogic.com), exchange them at auth.platform.satellogic.com/oauth/t
  name: Satellogic Aleph Authentication API
  slug: aleph-authentication-api
artifact_total: 22
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/satellogic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://satellogic.com
- group: start
  title: ''
  type: Portal
  url: https://developers.satellogic.com/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://developers.satellogic.com/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://doc.api.satellogic.com/tasking-service/description.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.satellogic.com/getting-started/gettingstarted.html
- group: auth
  title: ''
  type: Authentication
  url: https://developers.satellogic.com/api-authentication/getting_started.html
- group: start
  title: ''
  type: Signup
  url: https://aleph.satellogic.com/
- group: other
  title: ''
  type: Product
  url: https://satellogic.com/products/
- group: other
  title: ''
  type: Product
  url: https://satellogic.com/products/aleph-observer/
- group: other
  title: ''
  type: Product
  url: https://satellogic.com/products/multispectral-imagery/
- group: other
  title: ''
  type: Product
  url: https://satellogic.com/products/constellation-as-a-service/
- group: other
  title: ''
  type: Product
  url: https://satellogic.com/products/space-systems/
- group: other
  title: ''
  type: Company
  url: https://satellogic.com/about/
- group: company
  title: ''
  type: Newsroom
  url: https://satellogic.com/news/
- group: company
  title: ''
  type: Blog
  url: https://satellogic.com/news/press-room/
- group: operate
  title: ''
  type: PressReleases
  url: https://satellogic.com/news/press-releases/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.satellogic.com/
- group: company
  title: ''
  type: Careers
  url: https://satellogic.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://satellogic.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/satellogic
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/satellogic/telluric
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/satellogic/orbit-predictor
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/satellogic/iquaflow
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/satellogic/satellogic-earthview
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/satellogic/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/satellogic
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@satellogic
- group: commercial
  title: ''
  type: TermsOfService
  url: https://satellogic.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://satellogic.com/privacy-policy/
created: '2026-05-24'
description: 'Satellogic is an Argentine-founded, U.S.-listed (NASDAQ: SATL) vertically integrated Earth observation company that designs, builds, and operates its own NewSat constellation to deliver sub-meter, high-frequency multispectral and hyperspectral satellite imagery. Its commercial platform Aleph unifies archive search, tasking, analysis, and delivery into a single web and API experience, available in both the legacy Aleph V1 (Tasking, Archive, Analysis, Delivery APIs) and the unified Aleph V2 Orders API. Satellogic also markets Aleph Observer for persistent daily monitoring of designated sites, Constellation-as-a-Service for priority and large-scale tasking, and Space Systems for customers who wish to purchase and operate their own Mark V class satellites. Imagery is delivered via API, FTP, and a reseller network, with OAuth 2.0 Client Credentials authentication against auth.platform.satellogic.com and product APIs under api.satellogic.com.'
features:
- Sub-meter high-resolution multispectral imagery from the NewSat constellation
- Hyperspectral imagery products for advanced spectral analysis
- Daily, high-frequency monitoring via Aleph Observer with up to 7 daily revisits
- Aleph V2 unified Orders API combining archive purchases and tasking
- Aleph V1 specialized APIs — Tasking, Archive, Analysis, Delivery
- POI (point-of-interest) and AOI (area-of-interest) tasking workflows
- Feasibility analysis API for pre-order pass and constraint evaluation
- OAuth 2.0 Client Credentials authentication via auth.platform.satellogic.com
- 24-hour access token lifetime with contract-ID-scoped requests
- Imagery delivery via API, FTP, and reseller network
- L1 Basic (L1B) and hyperspectral product tiers
- Constellation-as-a-Service for priority and large-scale tasking
- Space Systems — purchase and operate custom NewSat Mark V class satellites
- Open-source geospatial tooling (telluric, orbit-predictor, iquaflow, EarthView dataset)
- Vertically integrated — designs, builds, launches, and operates its own satellites
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/satellogic.png
layout: provider
modified: '2026-05-24'
name: Satellogic
nav: Providers
network: true
overview: 'Satellogic publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Earth Observation, Satellite Imagery, Geospatial, Remote Sensing, and High Resolution.


  Satellogic''s developer surface includes developer portal, documentation, getting-started guide, authentication, signup flow, engineering blog, YouTube channel, and 23 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 21.2
  delta: -4.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 25.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/satellogic/refs/heads/main/screenshots/satellogic-2026-06-20T193438.png
security:
- kind: domain-security
  name: Satellogic Domain Security
  slug: satellogic-domain-security
  summary_line: TLSv1.2 · DMARC
slug: satellogic
tags:
- Earth Observation
- Satellite Imagery
- Geospatial
- Remote Sensing
- High Resolution
- Sub-Meter Imagery
- Multispectral
- Hyperspectral
- Tasking
- Archive
- Aleph
- NewSat
- Constellation
- Defense and Intelligence
- Energy and Mining
- Insurance
- Climate
website: https://satellogic.com
---
