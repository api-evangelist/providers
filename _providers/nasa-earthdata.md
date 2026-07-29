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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Nasa Earthdata Agentic Access
  operation_count: 13
  slug: nasa-earthdata-agentic-access
  summary_line: 13 operations · 1 acting
api_count: 7
apis:
- description: The CMR SpatioTemporal Asset Catalog (STAC) API provides a STAC-compliant interface over NASA's Common Metadata Repository, enabling discovery and access to Earth science data collections and items us
  name: CMR STAC API
  slug: cmr-stac-api
- description: The Earthdata Login API provides free and immediate access to thousands of EOSDIS data products covering all Earth science disciplines. It manages user authentication and profile management using OAut
  name: Earthdata Login API
  slug: earthdata-login-api
- description: The Application for Extracting and Exploring Analysis Ready Samples (AppEEARS) API offers a RESTful interface for submitting and managing area or point-based data extraction tasks from NASA Earth scie
  name: AppEEARS API
  slug: appeears-api
- description: The Global Imagery Browse Services (GIBS) API delivers quick access to over 1,000 satellite imagery products through standards-compliant web services including WMTS, WMS, and Tiled Web Map Service (TW
  name: Global Imagery Browse Services (GIBS) API
  slug: global-imagery-browse-services-gibs-api
- description: Essential characteristics of this API including information about the data.
  name: NASA Earthdata Capabilities API
  slug: nasa-earthdata-capabilities-api
- description: Access to data (coverage).
  name: NASA Earthdata Coverage API
  slug: nasa-earthdata-coverage-api
- description: The OpenAPI API from NASA Earthdata — 1 operation(s) for openapi.
  name: NASA Earthdata OpenAPI API
  slug: nasa-earthdata-openapi-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nasa-earthdata-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nasa-earthdata-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.earthdata.nasa.gov/engage/open-data-services-software/earthdata-developer-portal
- group: auth
  title: ''
  type: Authentication
  url: https://www.earthdata.nasa.gov/engage/open-data-services-software/earthdata-developer-portal/earthdata-login-api
- group: operate
  title: ''
  type: Forums
  url: https://forum.earthdata.nasa.gov/
- group: operate
  title: ''
  type: Status
  url: https://status.earthdata.nasa.gov/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.earthdata.nasa.gov/learn/use-data/data-use-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nasa.gov/about/highlights/HP_Privacy.html
- group: company
  title: ''
  type: Blog
  url: https://www.earthdata.nasa.gov/news/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/nasa
created: '2026-06-13'
description: NASA Earthdata is the Earth Observing System Data and Information System (EOSDIS) portal providing access to NASA's Earth observation data holdings. It offers REST APIs for searching, discovering, and downloading satellite imagery, climate data, and Earth science datasets from NASA missions including the Common Metadata Repository, Harmony data transformation services, Global Imagery Browse Services, and the Application for Extracting and Exploring Analysis Ready Samples.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nasa-earthdata.png
layout: provider
modified: '2026-06-13'
name: NASA Earthdata
nav: Providers
network: true
overview: 'NASA Earthdata publishes 3 APIs on the [APIs.io](https://apis.io/) network: Capabilities API, Coverage API, and OpenAPI API. Tagged areas include Earth Observation, Satellite Data, Climate Data, Remote Sensing, and Geospatial.


  NASA Earthdata''s developer surface includes developer portal, authentication, status page, engineering blog, GitHub presence, and 5 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 20
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 32.8
  delta: -3.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 41.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nasa-earthdata/refs/heads/main/screenshots/nasa-earthdata-2026-06-20T185948.png
security:
- kind: domain-security
  name: Nasa Earthdata Domain Security
  slug: nasa-earthdata-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nasa-earthdata
tags:
- Earth Observation
- Satellite Data
- Climate Data
- Remote Sensing
- Geospatial
- NASA
- Science Data
website: https://www.earthdata.nasa.gov/engage/open-data-services-software/earthdata-developer-portal
---
