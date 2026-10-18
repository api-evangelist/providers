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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Cdc Agentic Access
  operation_count: 33
  slug: cdc-agentic-access
  summary_line: 33 operations · 20 acting
api_count: 12
apis:
- description: The CDC WONDER (Wide-ranging Online Data for Epidemiologic Research) API enables automated data queries in XML format over HTTP. Supports access to online databases covering mortality, natality, cance
  name: CDC WONDER API
  slug: cdc-wonder-api
- description: Allows querying of data from the CDC National Environmental Public Health Tracking Network. Returns JSON-formatted responses covering environmental health indicators such as air quality, water quality
  name: CDC Environmental Public Health Tracking Network API
  slug: cdc-environmental-public-health-tracking-network-api
- description: Enables CDC to offer web content to other sites and applications. Provides structured access to CDC health content including articles, health topics, media, and tools in JSON and XML formats for syndi
  name: CDC Content Syndication API
  slug: cdc-content-syndication-api
- description: 'The Public Health Information Network Vocabulary Access and Distribution System (PHIN VADS) is a web-based enterprise vocabulary system for accessing, searching, and distributing vocabularies used in '
  name: PHIN VADS API
  slug: phin-vads-api
- description: PLACES (Population Level Analysis and Community Estimates) provides model-based small-area estimates for chronic disease risk factors, health outcomes, and prevention practices for counties, ZCTAs, ce
  name: CDC PLACES / 500 Cities API
  slug: cdc-places-api
- description: 'The National Notifiable Diseases Surveillance System (NNDSS) and Morbidity and Mortality Weekly Report (MMWR) tables are published as Socrata datasets on data.cdc.gov, providing weekly and historical '
  name: CDC NNDSS / MMWR Socrata Data
  slug: cdc-tb-nndss-socrata
- baseURL: https://wonder.cdc.gov/controller/datarequest
  baseurl_source: declared
  description: The app-notifications API from CDC — 1 operation(s) for app-notifications.
  name: CDC App Notifications API
  slug: cdc-gov-app-notifications-api
- baseURL: https://wonder.cdc.gov/controller/datarequest
  baseurl_source: declared
  description: The code-systems API from CDC — 1 operation(s) for code-systems.
  name: CDC Code Systems API
  slug: cdc-gov-code-systems-api
- baseURL: https://wonder.cdc.gov/controller/datarequest
  baseurl_source: declared
  description: The conditions API from CDC — 2 operation(s) for conditions.
  name: CDC Conditions API
  slug: cdc-gov-conditions-api
- baseURL: https://wonder.cdc.gov/controller/datarequest
  baseurl_source: declared
  description: The configurations API from CDC — 15 operation(s) for configurations.
  name: CDC Configurations API
  slug: cdc-gov-configurations-api
- baseURL: https://wonder.cdc.gov/controller/datarequest
  baseurl_source: declared
  description: The events API from CDC — 2 operation(s) for events.
  name: CDC Events API
  slug: cdc-gov-events-api
- baseURL: https://wonder.cdc.gov/controller/datarequest
  baseurl_source: declared
  description: The Query API from CDC — 1 operation(s) for query.
  name: CDC Query API
  slug: cdc-gov-query-api
- baseURL: https://wonder.cdc.gov/controller/datarequest
  baseurl_source: declared
  description: The Query Connector API OpenAPI 3.0 API from CDC — 1 operation(s) for query connector api openapi 3.0.
  name: CDC Query Connector API OpenAPI 3.0 API
  slug: cdc-gov-query-connector-api-openapi-3-0-api
- baseURL: https://wonder.cdc.gov/controller/datarequest
  baseurl_source: declared
  description: The releases API from CDC — 1 operation(s) for releases.
  name: CDC Releases API
  slug: cdc-gov-releases-api
- baseURL: https://wonder.cdc.gov/controller/datarequest
  baseurl_source: declared
  description: The simulator API from CDC — 3 operation(s) for simulator.
  name: CDC Simulator API
  slug: cdc-gov-simulator-api
- baseURL: https://wonder.cdc.gov/controller/datarequest
  baseurl_source: declared
  description: The user API from CDC — 1 operation(s) for user.
  name: CDC User API
  slug: cdc-gov-user-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DIBBs eCR Refiner app-notifications API
  slug: open-cdc-app-notifications-api
- collection_type: open
  name: DIBBs eCR Refiner app-notifications code-systems API
  slug: open-cdc-code-systems-api
- collection_type: open
  name: DIBBs eCR Refiner app-notifications conditions API
  slug: open-cdc-conditions-api
- collection_type: open
  name: DIBBs eCR Refiner app-notifications configurations API
  slug: open-cdc-configurations-api
- collection_type: open
  name: DIBBs eCR Refiner app-notifications events API
  slug: open-cdc-events-api
- collection_type: open
  name: DIBBs eCR Refiner app-notifications Query API
  slug: open-cdc-query-api
- collection_type: open
  name: DIBBs eCR Refiner app-notifications Query Connector API OpenAPI 3.0 API
  slug: open-cdc-query-connector-api-openapi-3-0-api
- collection_type: open
  name: DIBBs eCR Refiner app-notifications releases API
  slug: open-cdc-releases-api
- collection_type: open
  name: DIBBs eCR Refiner app-notifications simulator API
  slug: open-cdc-simulator-api
- collection_type: open
  name: DIBBs eCR Refiner app-notifications user API
  slug: open-cdc-user-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cdc-gov/refs/heads/main/plans/plans.yml
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cdc-gov/refs/heads/main/rate-limits/rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cdc-gov/refs/heads/main/finops/finops.yml
  title: ''
  type: FinOps
  url: finops/finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.cdc.gov/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cdc-gov/refs/heads/main/agentic-access/cdc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cdc-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cdc-gov/refs/heads/main/security/cdc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cdc-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://open.cdc.gov/apis.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/CDCgov
- group: auth
  title: ''
  type: Authentication
  url: https://dev.socrata.com/docs/app-tokens.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cdc.gov/other/policies.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cdc.gov/other/privacy.html
- group: other
  title: ''
  type: Licensing
  url: https://www.cdc.gov/other/policies.html#linking
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/cdc-gov/refs/heads/main/json-ld/apis-jsonld.json
- group: docs
  title: ''
  type: Documentation
  url: https://tools.cdc.gov/api/docs/info.aspx
- group: docs
  title: ''
  type: APIReference
  url: https://wonder.cdc.gov/wonder/help/wonder-api.html
created: '2026-06-13'
description: The US Centers for Disease Control and Prevention (CDC) provides a suite of public APIs for accessing disease surveillance data, vaccination rates, health statistics, environmental public health tracking, and public health datasets. Key offerings include the CDC WONDER API for querying mortality and disease databases, the Open Data API powered by Socrata for thousands of datasets across categories such as flu vaccinations, STDs, injury, and NCHS statistics, the Environmental Public Health Tracking Network API for environmental health data, and the PHIN VADS vocabulary service for public health terminology.
finops:
- has_sources: false
  method: generated
  name: Finops
  primary_unit: ''
  service_category: ''
  slug: finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cdc.png
layout: provider
modified: '2026-06-13'
name: CDC
nav: Providers
network: true
overview: 'CDC publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including App Notifications API, Code Systems API, Conditions API, and 13 more. Tagged areas include Public Health, Disease Surveillance, Vaccination, Health Statistics, and Government.


  CDC''s developer surface includes developer portal, GitHub presence, authentication, documentation, API reference, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 15
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 44.8
    developer_ergonomics: 38.1
    discoverability: 62.5
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/cdc-gov/refs/heads/main/screenshots/cdc-2026-06-20T174105.png
security:
- kind: domain-security
  name: Cdc Domain Security
  slug: cdc-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: cdc-gov
tags:
- Public Health
- Disease Surveillance
- Vaccination
- Health Statistics
- Government
- Open Data
- Environmental Health
- Mortality
- CDC WONDER
- Epidemiology
- Federal Government
- Healthcare
- Socrata
- WONDER
website: https://www.cdc.gov/
---
