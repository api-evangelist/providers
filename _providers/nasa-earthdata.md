---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nasa Earthdata Agentic Access
  operation_count: 13
  slug: nasa-earthdata-agentic-access
  summary_line: 13 operations
api_count: 1
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
- baseURL: https://cmr.earthdata.nasa.gov
  baseurl_source: declared
  description: Essential characteristics of this API including information about the data.
  name: NASA Earthdata Capabilities API
  slug: nasa-earthdata-capabilities-api
- baseURL: https://cmr.earthdata.nasa.gov
  baseurl_source: declared
  description: Access to data (coverage).
  name: NASA Earthdata Coverage API
  slug: nasa-earthdata-coverage-api
- baseURL: https://cmr.earthdata.nasa.gov/stac
  baseurl_source: declared
  description: The Open API API from NASA Earthdata — 1 operation(s) for open api.
  name: NASA Earthdata Open API
  slug: nasa-earthdata-open-api-api
artifact_total: 16
collections:
- collection_type: open
  name: Harmony API conforming to OGC API - Coverages Capabilities API
  slug: open-nasa-earthdata-capabilities-api
- collection_type: open
  name: Harmony API conforming to OGC API - Coverages Capabilities Coverage API
  slug: open-nasa-earthdata-coverage-api
- collection_type: open
  name: Harmony API conforming to OGC API - Coverages Capabilities OpenAPI API
  slug: open-nasa-earthdata-openapi-api
common:
- group: commercial
  href: https://artifacts.apis.io/nasa-earthdata/plans/plans.yml
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  href: https://artifacts.apis.io/nasa-earthdata/rate-limits/rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nasa-earthdata/finops/finops.yml
  title: ''
  type: FinOps
  url: finops/finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasa.gov/
- group: agent
  href: https://artifacts.apis.io/nasa-earthdata/agentic-access/nasa-earthdata-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nasa-earthdata-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/nasa-earthdata/security/nasa-earthdata-domain-security.yml
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
- has_sources: false
  method: generated
  name: Finops
  primary_unit: ''
  service_category: ''
  slug: finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nasa-earthdata.png
layout: provider
modified: '2026-06-13'
name: NASA Earthdata
nav: Providers
network: true
overview: 'NASA Earthdata publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Capabilities API, Coverage API, Open API, and 4 more. Tagged areas include Earth Observation, Satellite Data, Climate Data, Remote Sensing, and Geospatial.


  The NASA Earthdata catalog on APIs.io includes 1 Spectral governance ruleset.


  NASA Earthdata''s developer surface includes developer portal, authentication, status page, engineering blog, GitHub presence, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 14
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: NASA Earthdata API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: nasa-earthdata-rules
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 43.5
    catalog_earned_first_party: 0.0
    catalog_gap: 71.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 40.7
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 32.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/nasa-earthdata/nasa-earthdata-2026-06-20T185948.png
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
website: https://www.nasa.gov/
---
