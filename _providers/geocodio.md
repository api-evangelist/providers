---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Geocodio Agentic Access
  operation_count: 9
  slug: geocodio-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.geocod.io/v1.7
  baseurl_source: declared
  description: Asynchronous spreadsheet geocoding jobs.
  name: Geocodio Lists API
  slug: geocodio-lists-api
- description: Address geocoding / reverse geocoding in bulk
  name: Geocod.io
  slug: geocodio
- baseURL: https://api.geocod.io/v1.7
  baseurl_source: declared
  description: Calculate distances between one origin and one or more destinations
  name: Geocodio Distance API
  slug: geocodio-distance-api
- baseURL: https://api.geocod.io/v1.7
  baseurl_source: declared
  description: Async distance matrix and one-to-one pairs job management
  name: Geocodio Distance Jobs API
  slug: geocodio-distance-jobs-api
- baseURL: https://api.geocod.io/v1.7
  baseurl_source: declared
  description: Calculate distances between multiple origins and multiple destinations, either as a full matrix or as one-to-one pairs
  name: Geocodio Distance Matrix API
  slug: geocodio-distance-matrix-api
- baseURL: https://api.geocod.io/v1.7
  baseurl_source: declared
  description: Geocode addresses to coordinates
  name: Geocodio Geocode API
  slug: geocodio-geocode-api
- baseURL: https://api.geocod.io/v1.7
  baseurl_source: declared
  description: Reverse geocode coordinates to addresses
  name: Geocodio Reverse API
  slug: geocodio-reverse-api
artifact_total: 22
collections:
- collection_type: open
  name: Geocodio Batch API
  slug: open-geocodio-batch-api
- collection_type: open
  name: Geocodio Batch Forward Geocoding API
  slug: open-geocodio-forward-geocoding-api
- collection_type: open
  name: Geocodio Batch Lists API
  slug: open-geocodio-lists-api
- collection_type: open
  name: Geocodio Batch Reverse Geocoding API
  slug: open-geocodio-reverse-geocoding-api
- collection_type: open
  name: Geocodio API
  slug: open-geocodio
common:
- group: other
  href: https://artifacts.apis.io/geocodio/capabilities/geocodio-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/geocodio-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/geocodio/agentic-access/geocodio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/geocodio-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/geocodio/security/geocodio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/geocodio-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/geocodio/security/geocodio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/geocodio-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/geocodio/security/geocodio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geocodio-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/geocodio/authentication/geocodio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/geocodio-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Geocodio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geocodio
- group: company
  title: ''
  type: Website
  url: https://www.geocod.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.geocod.io/docs/
- group: commercial
  href: https://artifacts.apis.io/geocodio/plans/geocodio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/geocodio-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/geocodio/rate-limits/geocodio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/geocodio-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/geocodio/finops/geocodio-finops.yml
  title: ''
  type: FinOps
  url: finops/geocodio-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.geocod.io/updates/rss.xml
created: '2026-06-21'
description: Geocodio is a US and Canada geocoding API that converts addresses to coordinates (forward), coordinates to addresses (reverse), processes batches and spreadsheet lists, and enriches results with appended data such as congressional and state legislative districts, census geographies, ACS demographics, school districts, and timezones. Authentication is via an api_key query parameter and the first 2,500 lookups per day are free.
finops:
- has_sources: true
  method: generated
  name: Geocodio Finops
  primary_unit: ''
  service_category: Maps and Geospatial
  slug: geocodio-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geocodio.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.geocod.io over HTTP.
  name: Geocodio MCP Server
  slug: geocodio
modified: '2026-06-21'
name: Geocodio
nav: Providers
network: true
overview: 'Geocodio publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Lists API, Distance API, Distance Jobs API, and 4 more. Tagged areas include Geocoding, Reverse Geocoding, Addresses, Data Append, and Census.


  The Geocodio catalog on APIs.io includes 1 Spectral governance ruleset.


  Geocodio''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Geocodio Plans Pricing
  plan_count: 3
  slug: geocodio-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Geocodio Rate Limits
  slug: geocodio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Geocodio API Rules
  rule_count: 67
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 4
  slug: geocodio-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 51.6
    developer_ergonomics: 31.0
    discoverability: 60.0
    operational_transparency: 21.1
  previous_composite: 32.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 54.5
      total: 11
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/geocodio/geocodio-2026-07-25T215651.png
security:
- kind: authentication
  name: Geocodio Authentication
  slug: geocodio-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Geocodio Domain Security
  slug: geocodio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Geocodio Vulnerability Disclosure
  slug: geocodio-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Geocodio Trust Center
  slug: geocodio-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: geocodio
tags:
- Geocoding
- Reverse Geocoding
- Addresses
- Data Append
- Census
- Geospatial
website: https://www.geocod.io
---
