---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
  name: Attom Data Agentic Access
  operation_count: 37
  slug: attom-data-agentic-access
  summary_line: 37 operations
api_count: 1
apis:
- description: Area geography, geoId lookups, and boundaries (v2/v4).
  name: ATTOM Area API
  slug: attom-data-area-api
- description: County tax assessment data.
  name: ATTOM Assessment API
  slug: attom-data-assessment-api
- description: Neighborhood and community context (v4).
  name: ATTOM Community API
  slug: attom-data-community-api
- description: Consolidated all-event property history.
  name: ATTOM Events API
  slug: attom-data-events-api
- description: Estimated home equity and loan-to-value.
  name: ATTOM Home Equity API
  slug: attom-data-home-equity-api
- description: Property records enriched with mortgage and owner data.
  name: ATTOM Mortgage API
  slug: attom-data-mortgage-api
- description: Points of interest (v4).
  name: ATTOM POI API
  slug: attom-data-poi-api
- description: Core property characteristics packages.
  name: ATTOM Property API
  slug: attom-data-property-api
- description: Recorded sale, deed, sales history, and sales trend data.
  name: ATTOM Sales API
  slug: attom-data-sales-api
- description: Schools, school districts, and attendance zones.
  name: ATTOM School API
  slug: attom-data-school-api
- description: Modeled transportation-noise scores.
  name: ATTOM Transportation Noise API
  slug: attom-data-transportation-noise-api
- description: Automated Valuation Model (AVM) and rental value.
  name: ATTOM Valuation API
  slug: attom-data-valuation-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ATTOM Area API
  slug: open-attom-data-area-api
- collection_type: open
  name: ATTOM Area Assessment API
  slug: open-attom-data-assessment-api
- collection_type: open
  name: ATTOM Area Community API
  slug: open-attom-data-community-api
- collection_type: open
  name: ATTOM Area Events API
  slug: open-attom-data-events-api
- collection_type: open
  name: ATTOM Area Home Equity API
  slug: open-attom-data-home-equity-api
- collection_type: open
  name: ATTOM Area Mortgage API
  slug: open-attom-data-mortgage-api
- collection_type: open
  name: ATTOM Area POI API
  slug: open-attom-data-poi-api
- collection_type: open
  name: ATTOM Area Property API
  slug: open-attom-data-property-api
- collection_type: open
  name: ATTOM Area Sales API
  slug: open-attom-data-sales-api
- collection_type: open
  name: ATTOM Area School API
  slug: open-attom-data-school-api
- collection_type: open
  name: ATTOM Area Transportation Noise API
  slug: open-attom-data-transportation-noise-api
- collection_type: open
  name: ATTOM Area Valuation API
  slug: open-attom-data-valuation-api
- collection_type: open
  name: ATTOM API
  slug: open-attom-data
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/attom-data-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/attom-data-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/attom-data-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/attom-data-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/attom-data-solutions
- group: company
  title: ''
  type: Website
  url: https://www.attomdata.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.developer.attomdata.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/attom-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/attom-data-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.attomdata.com/feed/
- group: commercial
  title: ''
  type: FinOps
  url: finops/attom-data-finops.yml
created: '2026-07-03'
description: ATTOM Data Solutions is a national property, real estate, and location data provider that curates a multi-sourced warehouse of data on 158+ million U.S. properties. The ATTOM API (also delivered as ATTOM Cloud) exposes that data over REST as a family of logical resources - property characteristics, tax assessments, automated valuations (AVM), sales and deed history, mortgage records, area and boundary geographies, schools, community and neighborhood data, points of interest, transportation noise, all-event snapshots, and home equity - queried by address, APN/FIPS, ATTOM ID, radius, or geoIdV4 and authenticated with an API key.
finops:
- name: Attom Data Finops
  service_category: Data and Analytics
  slug: attom-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/attom-data.png
layout: provider
modified: '2026-07-03'
name: ATTOM
nav: Providers
network: true
overview: 'ATTOM publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Area API, Assessment API, Community API, and 9 more. Tagged areas include Property Data, Real-Estate, Location Data, Valuation, and AVM.


  ATTOM''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Attom Data Plans Pricing
  plan_count: 3
  slug: attom-data-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Attom Data Rate Limits
  slug: attom-data-rate-limits
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.1
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/attom-data/refs/heads/main/screenshots/attom-data-2026-07-25T201637.png
security:
- kind: authentication
  name: Attom Data Authentication
  slug: attom-data-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Attom Data Domain Security
  slug: attom-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: attom-data
tags:
- Property Data
- Real-Estate
- Location Data
- Valuation
- AVM
- Assessment
- Mortgage
- Neighborhood
website: https://www.attomdata.com
---
