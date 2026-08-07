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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Carapi Agentic Access
  operation_count: 4
  slug: carapi-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 2
apis:
- description: Endpoints for obtaining a JWT token for API access.
  name: CarAPI Authentication API
  slug: carapi-authentication-api
- description: Operations for retrieving vehicle models, trims, and attributes.
  name: CarAPI Vehicles API
  slug: carapi-vehicles-api
artifact_total: 9
collections:
- collection_type: open
  name: CarAPI
  slug: open-carapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/carapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/carapi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/car-api-team
- group: company
  title: ''
  type: Website
  url: https://carapi.app/
- group: docs
  title: ''
  type: Documentation
  url: https://carapi.app/docs/
- group: auth
  title: ''
  type: Authentication
  url: https://carapi.app/docs/#authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://carapi.app/docs/rate_limits/
- group: commercial
  title: ''
  type: Pricing
  url: https://carapi.app/pricing
created: '2025-01-07'
description: CarAPI is an innovative platform that provides detailed information about a wide range of vehicles including car specifications, pricing, availability, and more. With CarAPI, users can search for specific makes and models, compare different vehicles, and make informed decisions when purchasing a new car.
finops:
- name: Carapi Finops
  service_category: API
  slug: carapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carapi.png
layout: provider
modified: '2026-05-19'
name: CarAPI
nav: Providers
network: true
overview: 'CarAPI publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Vehicles API. Tagged areas include Automobiles and Vehicles.


  CarAPI''s developer surface includes authentication, documentation, pricing, and 6 more developer resources.'
plans:
- name: Carapi Plans Pricing
  plan_count: 3
  slug: carapi-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 5
  name: Carapi Rate Limits
  slug: carapi-rate-limits
score:
  band: thin
  composite: 40.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 65.1
    developer_ergonomics: 19.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carapi/refs/heads/main/screenshots/carapi-2026-06-20T173946.png
security:
- kind: authentication
  name: Carapi Authentication
  slug: carapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Carapi Domain Security
  slug: carapi-domain-security
  summary_line: TLSv1.3
slug: carapi
tags:
- Automobiles
- Vehicles
website: https://carapi.app/
---
