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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Realtymole Agentic Access
  operation_count: 5
  slug: realtymole-agentic-access
  summary_line: 5 operations
api_count: 4
apis:
- description: Active for-sale and for-rent listings near a location.
  name: RealtyMole Listings API
  slug: realtymole-listings-api
- description: Property record lookups by address or coordinates.
  name: RealtyMole Property Records API
  slug: realtymole-property-records-api
- description: AVM long-term rent estimate with comparable properties.
  name: RealtyMole Rental Estimate API
  slug: realtymole-rental-estimate-api
- description: AVM sale-price (value) estimate with comparable sales.
  name: RealtyMole Sale Estimate API
  slug: realtymole-sale-estimate-api
artifact_total: 11
collections:
- collection_type: open
  name: Realty Mole Property API
  slug: open-realtymole
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/realtymole-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/realtymole-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/realtymole-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rentcast
- group: company
  title: ''
  type: Website
  url: https://www.realtymole.com
- group: docs
  title: ''
  type: Documentation
  url: https://rapidapi.com/realtymole/api/realty-mole-property-api
- group: commercial
  title: ''
  type: Plans
  url: plans/realtymole-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/realtymole-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/realtymole-finops.yml
created: '2026-06-21'
description: RealtyMole (Realty Mole Property API) is a US real-estate and property data API distributed primarily through RapidAPI. It returns property records, AVM-based rental estimates and sale-price (value) estimates with comparable properties, and active for-sale and for-rent listings by address or latitude/longitude. RealtyMole is the predecessor product to RentCast (rentcast.io); the standalone Realty Mole Property API on RapidAPI is legacy and superseded by the RentCast API.
finops:
- name: Realtymole Finops
  service_category: Real Estate and Property Data
  slug: realtymole-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/realtymole.png
layout: provider
modified: '2026-06-21'
name: RealtyMole
nav: Providers
network: true
overview: 'RealtyMole publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Listings API, Property Records API, Rental Estimate API, and 1 more. Tagged areas include Real Estate, Property Data, Rental Estimate, Valuation, and Listings.


  RealtyMole''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Realtymole Plans Pricing
  plan_count: 5
  slug: realtymole-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 3
  name: Realtymole Rate Limits
  slug: realtymole-rate-limits
score:
  band: thin
  composite: 40.5
  delta: 3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Realtymole Authentication
  slug: realtymole-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Realtymole Domain Security
  slug: realtymole-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: realtymole
tags:
- Real Estate
- Property Data
- Rental Estimate
- Valuation
- Listings
website: https://www.realtymole.com
---
