---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Federal Reserve Agentic Access
  operation_count: 13
  slug: federal-reserve-agentic-access
  summary_line: 13 operations
api_count: 1
apis:
- baseURL: https://api.stlouisfed.org/fred
  baseurl_source: declared
  description: The Category API from Federal Reserve — 3 operation(s) for category.
  name: Federal Reserve Category API
  slug: federal-reserve-category-api
- baseURL: https://api.stlouisfed.org/fred
  baseurl_source: declared
  description: The Related Tags API from Federal Reserve — 1 operation(s) for related tags.
  name: Federal Reserve Related Tags API
  slug: federal-reserve-related-tags-api
- baseURL: https://api.stlouisfed.org/fred
  baseurl_source: declared
  description: The Release API from Federal Reserve — 2 operation(s) for release.
  name: Federal Reserve Release API
  slug: federal-reserve-release-api
- baseURL: https://api.stlouisfed.org/fred
  baseurl_source: declared
  description: The Releases API from Federal Reserve — 1 operation(s) for releases.
  name: Federal Reserve Releases API
  slug: federal-reserve-releases-api
- baseURL: https://api.stlouisfed.org/fred
  baseurl_source: declared
  description: The Series API from Federal Reserve — 3 operation(s) for series.
  name: Federal Reserve Series API
  slug: federal-reserve-series-api
- baseURL: https://api.stlouisfed.org/fred
  baseurl_source: declared
  description: The Source API from Federal Reserve — 1 operation(s) for source.
  name: Federal Reserve Source API
  slug: federal-reserve-source-api
- baseURL: https://api.stlouisfed.org/fred
  baseurl_source: declared
  description: The Sources API from Federal Reserve — 1 operation(s) for sources.
  name: Federal Reserve Sources API
  slug: federal-reserve-sources-api
- baseURL: https://api.stlouisfed.org/fred
  baseurl_source: declared
  description: The Tags API from Federal Reserve — 1 operation(s) for tags.
  name: Federal Reserve Tags API
  slug: federal-reserve-tags-api
artifact_total: 24
collections:
- collection_type: open
  name: Federal Reserve FRED Category API
  slug: open-federal-reserve-category-api
- collection_type: open
  name: Federal Reserve FRED API
  slug: open-federal-reserve-fred
- collection_type: open
  name: Federal Reserve FRED Category Related Tags API
  slug: open-federal-reserve-related-tags-api
- collection_type: open
  name: Federal Reserve FRED Category Release API
  slug: open-federal-reserve-release-api
- collection_type: open
  name: Federal Reserve FRED Category Releases API
  slug: open-federal-reserve-releases-api
- collection_type: open
  name: Federal Reserve FRED Category Series API
  slug: open-federal-reserve-series-api
- collection_type: open
  name: Federal Reserve FRED Category Source API
  slug: open-federal-reserve-source-api
- collection_type: open
  name: Federal Reserve FRED Category Sources API
  slug: open-federal-reserve-sources-api
- collection_type: open
  name: Federal Reserve FRED Category Tags API
  slug: open-federal-reserve-tags-api
common:
- group: commercial
  href: https://artifacts.apis.io/federal-reserve/plans/federal-reserve-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/federal-reserve-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/federal-reserve/rate-limits/federal-reserve-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/federal-reserve-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/federal-reserve/finops/federal-reserve-finops.yml
  title: ''
  type: FinOps
  url: finops/federal-reserve-finops.yml
- group: agent
  href: https://artifacts.apis.io/federal-reserve/agentic-access/federal-reserve-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/federal-reserve-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/federal-reserve/security/federal-reserve-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/federal-reserve-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/federal-reserve/authentication/federal-reserve-authentication.yml
  title: ''
  type: Authentication
  url: authentication/federal-reserve-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-reserve-board
- group: company
  title: ''
  type: Website
  url: https://www.federalreserve.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://fred.stlouisfed.org/docs/api/fred
- group: company
  title: ''
  type: Blog
  url: https://www.federalreserve.gov/feeds/press_all.xml
created: '2024-12-03'
description: The FRED API is a web service that allows developers to write programs and build applications that retrieve economic data from the FRED and ALFRED websites hosted by the Economic Research Division of the Federal Reserve Bank of St. Louis.
finops:
- has_sources: false
  method: generated
  name: Federal Reserve Finops
  primary_unit: request
  service_category: API
  slug: federal-reserve-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-reserve.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.stlouisfed.org over HTTP.
  name: Federal Reserve MCP Server
  slug: federal-reserve
modified: '2026-05-19'
name: Federal Reserve
nav: Providers
network: true
overview: 'Federal Reserve publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Category API, Related Tags API, Release API, and 5 more. Tagged areas include Economics, Federal Government, and Finance.


  Federal Reserve''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Federal Reserve Plans Pricing
  plan_count: 3
  slug: federal-reserve-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Federal Reserve Rate Limits
  slug: federal-reserve-rate-limits
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 42.2
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 23.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/federal-reserve/federal-reserve-2026-06-20T181129.png
security:
- kind: authentication
  name: Federal Reserve Authentication
  slug: federal-reserve-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Federal Reserve Domain Security
  slug: federal-reserve-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federal-reserve
tags:
- Economics
- Federal Government
- Finance
website: https://www.federalreserve.gov/
---
