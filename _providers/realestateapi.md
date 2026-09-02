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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Realestateapi Agentic Access
  operation_count: 9
  slug: realestateapi-agentic-access
  summary_line: 9 operations · 9 acting
api_count: 1
apis:
- description: Automated valuation model
  name: RealEstateAPI AVM API
  slug: realestateapi-avm-api
- description: Comparable property analytics
  name: RealEstateAPI Comparables API
  slug: realestateapi-comparables-api
- description: Involuntary lien records
  name: RealEstateAPI Liens API
  slug: realestateapi-liens-api
- description: MLS listing data
  name: RealEstateAPI MLS API
  slug: realestateapi-mls-api
- description: Parcel boundary and GIS data
  name: RealEstateAPI Parcel API
  slug: realestateapi-parcel-api
- description: Detailed property records
  name: RealEstateAPI Property Detail API
  slug: realestateapi-property-detail-api
- description: Search and filter properties
  name: RealEstateAPI Property Search API
  slug: realestateapi-property-search-api
- description: Owner contact tracing
  name: RealEstateAPI Skip Trace API
  slug: realestateapi-skip-trace-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RealEstate AVM API
  slug: open-realestateapi-avm-api
- collection_type: open
  name: RealEstate AVM Comparables API
  slug: open-realestateapi-comparables-api
- collection_type: open
  name: RealEstate AVM Liens API
  slug: open-realestateapi-liens-api
- collection_type: open
  name: RealEstate AVM MLS API
  slug: open-realestateapi-mls-api
- collection_type: open
  name: RealEstate AVM Parcel API
  slug: open-realestateapi-parcel-api
- collection_type: open
  name: RealEstate AVM Property Detail API
  slug: open-realestateapi-property-detail-api
- collection_type: open
  name: RealEstate AVM Property Search API
  slug: open-realestateapi-property-search-api
- collection_type: open
  name: RealEstate AVM Skip Trace API
  slug: open-realestateapi-skip-trace-api
- collection_type: open
  name: RealEstateAPI
  slug: open-realestateapi
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/realestateapi-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/realestateapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/realestateapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/realestateapi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/realestateapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/realestateapi
- group: start
  title: ''
  type: Portal
  url: https://www.realestateapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.realestateapi.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.realestateapi.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://app.realestateapi.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.realestateapi.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.realestateapi.com/blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.realestateapi.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.realestateapi.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.realestateapi.com/privacy-policy/
created: '2026-03-16'
description: RealEstateAPI.com offers expressive property data APIs designed for building prop-tech applications. The platform exposes nationwide US property records including ownership, valuations, MLS listings, comparables, parcel boundary data, skip tracing, and involuntary liens through a unified JSON REST API.
finops:
- name: Realestateapi Finops
  service_category: API
  slug: realestateapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/realestateapi.png
layout: provider
modified: '2026-05-19'
name: RealEstateAPI
nav: Providers
network: true
overview: 'RealEstateAPI publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AVM API, Comparables API, Liens API, and 5 more. Tagged areas include Real-Estate, Property Data, MLS, Valuation, and Geospatial.


  RealEstateAPI''s developer surface includes authentication, developer portal, documentation, pricing, signup flow, engineering blog, and 9 more developer resources.'
plans:
- name: Realestateapi Plans Pricing
  plan_count: 3
  slug: realestateapi-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Realestateapi Rate Limits
  slug: realestateapi-rate-limits
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 50.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/realestateapi/refs/heads/main/screenshots/realestateapi-2026-06-20T192646.png
security:
- kind: authentication
  name: Realestateapi Authentication
  slug: realestateapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Realestateapi Domain Security
  slug: realestateapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: realestateapi
tags:
- Real-Estate
- Property Data
- MLS
- Valuation
- Geospatial
- Skip Tracing
- PropTech
website: https://www.realestateapi.com/
---
