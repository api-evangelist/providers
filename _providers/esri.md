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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Esri Agentic Access
  operation_count: 6
  slug: esri-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 4
apis:
- description: The Esri ArcGIS Platform API is a set of REST APIs and SDKs from Esri, provider of the ArcGIS GIS suite. It enables developers to integrate Esri's mapping, geocoding, routing, and spatial analysis ser
  name: Esri ArcGIS Platform API
  slug: esri-arcgis-platform-api
- description: The Auth API from Esri — 1 operation(s) for auth.
  name: Esri Auth API
  slug: esri-auth-api
- description: The Geocoding API from Esri — 4 operation(s) for geocoding.
  name: Esri Geocoding API
  slug: esri-geocoding-api
- description: The Routing API from Esri — 1 operation(s) for routing.
  name: Esri Routing API
  slug: esri-routing-api
artifact_total: 12
collections:
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
random_paper: 27
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
  composite: 35.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.5
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.8
  schema_version: 0.5
  scored_at: '2026-07-23'
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
