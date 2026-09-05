---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Esri Agentic Access
  operation_count: 6
  slug: esri-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- description: The Esri ArcGIS Platform API is a set of REST APIs and SDKs from Esri, provider of the ArcGIS GIS suite. It enables developers to integrate Esri's mapping, geocoding, routing, and spatial analysis ser
  name: Esri ArcGIS Platform API
  slug: esri-arcgis-platform-api
- baseURL: https://www.arcgis.com/sharing/rest
  baseurl_source: declared
  description: The Auth API from Esri — 1 operation(s) for auth.
  name: Esri Auth API
  slug: esri-auth-api
- baseURL: https://www.arcgis.com/sharing/rest
  baseurl_source: declared
  description: The Geocoding API from Esri — 4 operation(s) for geocoding.
  name: Esri Geocoding API
  slug: esri-geocoding-api
- baseURL: https://www.arcgis.com/sharing/rest
  baseurl_source: declared
  description: The Routing API from Esri — 1 operation(s) for routing.
  name: Esri Routing API
  slug: esri-routing-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Esri ArcGIS Location Services Auth API
  slug: open-esri-auth-api
- collection_type: open
  name: Esri ArcGIS Location Services Auth Geocoding API
  slug: open-esri-geocoding-api
- collection_type: open
  name: Esri ArcGIS Location Services Auth Routing API
  slug: open-esri-routing-api
- collection_type: open
  name: Esri ArcGIS Location Services API
  slug: open-esri
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/esri-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/esri-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/esri-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/esri-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/esri
- group: company
  title: ''
  type: Website
  url: https://www.esri.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.arcgis.com/
- group: other
  title: ''
  type: Alias
  url: https://github.com/api-evangelist/esri-arcgis
created: '2025-01-14'
description: 'Esri is a global leader in geographic information system (GIS) technology, offering innovative solutions for mapping and spatial analysis. The company provides software, data, and services to help organizations make better decisions based on location intelligence. Esri''s technology is used across a wide range of industries, including government, natural resources, utilities, and public safety. NOTE: This repository is an alias for the canonical Esri ArcGIS profile maintained at api-evangelist/esri-arcgis, which contains the full set of API definitions, OpenAPI artifacts, and developer resources.'
finops:
- name: Esri Finops
  service_category: API
  slug: esri-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/esri.png
layout: provider
modified: '2026-04-28'
name: Esri
nav: Providers
network: true
overview: 'Esri publishes 3 APIs on the [APIs.io](https://apis.io/) network: Auth API, Geocoding API, and Routing API. Tagged areas include Geographic, Geospatial, GIS, Location, and Mapping.


  Esri''s developer surface includes authentication and 7 more developer resources.'
plans:
- name: Esri Plans Pricing
  plan_count: 3
  slug: esri-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Esri Rate Limits
  slug: esri-rate-limits
scopes:
- name: Esri Scopes
  scope_count: 0
  slug: esri-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/esri/refs/heads/main/screenshots/esri-2026-06-20T180822.png
security:
- kind: authentication
  name: Esri Authentication
  slug: esri-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Esri Domain Security
  slug: esri-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: esri
tags:
- Geographic
- Geospatial
- GIS
- Location
- Mapping
- Maps
- Spatial Analysis
website: https://www.esri.com/
---
