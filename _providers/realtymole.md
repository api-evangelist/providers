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
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Realtymole Agentic Access
  operation_count: 5
  slug: realtymole-agentic-access
  summary_line: 5 operations
api_count: 1
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
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Realty Mole Property Listings API
  slug: open-realtymole-listings-api
- collection_type: open
  name: Realty Mole Property Listings Property Records API
  slug: open-realtymole-property-records-api
- collection_type: open
  name: Realty Mole Property Listings Rental Estimate API
  slug: open-realtymole-rental-estimate-api
- collection_type: open
  name: Realty Mole Property Listings Sale Estimate API
  slug: open-realtymole-sale-estimate-api
- collection_type: open
  name: Realty Mole Property API
  slug: open-realtymole
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/realtymole-capability-edges.yml
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
overview: 'RealtyMole publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Listings API, Property Records API, Rental Estimate API, and 1 more. Tagged areas include Real-Estate, Property Data, Rental Estimate, Valuation, and Listings.


  RealtyMole''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Realtymole Plans Pricing
  plan_count: 5
  slug: realtymole-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Realtymole Rate Limits
  slug: realtymole-rate-limits
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Real-Estate
- Property Data
- Rental Estimate
- Valuation
- Listings
website: https://www.realtymole.com
---
