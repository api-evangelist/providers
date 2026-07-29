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
- acting_count: 0
  human_in_the_loop: 0
  name: Particle Space Agentic Access
  operation_count: 7
  slug: particle-space-agentic-access
  summary_line: 7 operations
api_count: 5
apis:
- description: Address and property search / lookup.
  name: Particle Space Address Search API
  slug: particle-space-address-search-api
- description: Comparable properties for a subject property.
  name: Particle Space Comparables API
  slug: particle-space-comparables-api
- description: For-sale, for-rent, and off-market property listings.
  name: Particle Space Listings API
  slug: particle-space-listings-api
- description: Property records and detailed attributes.
  name: Particle Space Property Records API
  slug: particle-space-property-records-api
- description: Automated valuation model (AVM) value and rent estimates.
  name: Particle Space Valuations API
  slug: particle-space-valuations-api
artifact_total: 11
collections:
- collection_type: open
  name: Particle Space API
  slug: open-particle-space
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/particle-space-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/particle-space-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/particlespace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/particle-space
- group: company
  title: ''
  type: Website
  url: https://particlespace.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.particlespace.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/particle-space-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/particle-space-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/particle-space-finops.yml
created: '2026-06-21'
description: Particle Space is proptech infrastructure that exposes real-estate and property data through a REST API, Dashboard, SDKs, and white-labeled UIs. The platform provides real-time access to millions of properties for sale, rent, and off-market - property records, address and property search, valuations, comparables, and listings - using publishable and secret API keys with live and test modes.
finops:
- name: Particle Space Finops
  service_category: Real Estate and Property Data
  slug: particle-space-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/particle-space.png
layout: provider
modified: '2026-06-21'
name: Particle Space
nav: Providers
network: true
overview: 'Particle Space publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Address Search API, Comparables API, Listings API, and 2 more. Tagged areas include Real Estate, Property Data, PropTech, Listings, and Valuations.


  Particle Space''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Particle Space Plans Pricing
  plan_count: 3
  slug: particle-space-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 2
  name: Particle Space Rate Limits
  slug: particle-space-rate-limits
score:
  band: thin
  composite: 36.9
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.1
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Particle Space Authentication
  slug: particle-space-authentication
  summary_line: http · 1 scheme
slug: particle-space
tags:
- Real Estate
- Property Data
- PropTech
- Listings
- Valuations
website: https://particlespace.com/
---
