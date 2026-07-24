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
- acting_count: 0
  human_in_the_loop: 0
  name: Attomdata Agentic Access
  operation_count: 47
  slug: attomdata-agentic-access
  summary_line: 47 operations
api_count: 18
apis:
- description: Combined assessment, AVM, and sales-transaction events.
  name: ATTOM All Events API
  slug: attomdata-all-events-api
- description: Assessed value, tax liability, and assessment history.
  name: ATTOM Assessment API
  slug: attomdata-assessment-api
- description: Automated Valuation Model — current AVM, AVM history, and rental AVM.
  name: ATTOM AVM API
  slug: attomdata-avm-api
- description: GeoJSON boundary polygons by geography identifier.
  name: ATTOM Boundary API
  slug: attomdata-boundary-api
- description: Building permit records associated with a property.
  name: ATTOM Building Permits API
  slug: attomdata-building-permits-api
- description: Neighborhood community profile (demographics, crime, weather, commute).
  name: ATTOM Community API
  slug: attomdata-community-api
- description: Geographic hierarchy lookup from coordinates.
  name: ATTOM Hierarchy API
  slug: attomdata-hierarchy-api
- description: Estimated home equity calculations.
  name: ATTOM Home Equity API
  slug: attomdata-home-equity-api
- description: Resolve a location by geoIdV4.
  name: ATTOM Location API
  slug: attomdata-location-api
- description: Lookup of state, county, CBSA, and geoID metadata.
  name: ATTOM Lookup API
  slug: attomdata-lookup-api
- description: Vector parcel boundary tiles.
  name: ATTOM Parcel Tiles API
  slug: attomdata-parcel-tiles-api
- description: Lookup of POI categories, lines of business, and industries.
  name: ATTOM POI Categories API
  slug: attomdata-poi-categories-api
- description: Search points of interest by point or address.
  name: ATTOM POI Search API
  slug: attomdata-poi-search-api
- description: Pre-foreclosure status and notice records.
  name: ATTOM Pre-Foreclosure API
  slug: attomdata-pre-foreclosure-api
- description: Property characteristics, ownership, mortgage, and address resolution.
  name: ATTOM Property API
  slug: attomdata-property-api
- description: Sales transactions, sales history, and comparable sales.
  name: ATTOM Sale API
  slug: attomdata-sale-api
- description: Aggregated sales trends for a geography.
  name: ATTOM Sales Trends API
  slug: attomdata-sales-trends-api
- description: School assignments and attendance-zone associations.
  name: ATTOM School API
  slug: attomdata-school-api
artifact_total: 43
collections:
- collection_type: open
  name: ATTOM Area API
  slug: open-attom-area-api
- collection_type: open
  name: ATTOM Community API
  slug: open-attom-community-api
- collection_type: open
  name: ATTOM Parcel Tiles API
  slug: open-attom-parcel-tiles-api
- collection_type: open
  name: ATTOM POI API
  slug: open-attom-poi-api
- collection_type: open
  name: ATTOM Property API
  slug: open-attom-property-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/attomdata-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/attomdata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/attomdata-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.attomdata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.developer.attomdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.developer.attomdata.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.developer.attomdata.com/docs/guides
- group: start
  title: ''
  type: Signup
  url: https://api.developer.attomdata.com/signup
- group: start
  title: ''
  type: Login
  url: https://api.developer.attomdata.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.attomdata.com/solutions/property-data-api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.attomdata.com/solutions/bulk-data-licensing/
- group: docs
  title: ''
  type: Documentation
  url: https://www.attomdata.com/solutions/cloud-delivery/
- group: docs
  title: ''
  type: Documentation
  url: https://www.attomdata.com/data/
- group: company
  title: ''
  type: Blog
  url: https://www.attomdata.com/news/most-recent/
- group: docs
  title: ''
  type: Documentation
  url: https://www.attomdata.com/insights/white-papers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.attomdata.com/webinars/
- group: docs
  title: ''
  type: Documentation
  url: https://www.attomdata.com/glossary/
- group: operate
  title: ''
  type: Support
  url: https://www.attomdata.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/attomdata
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/attomdata
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/attomdata
- group: build
  title: ''
  type: GitHub
  url: https://github.com/AttomDataSolutions
- group: build
  title: ''
  type: Postman
  url: https://github.com/AttomDataSolutions/postman-collections
- group: build
  title: ''
  type: SDKs
  url: https://github.com/AttomDataSolutions/Sample_Code
- group: build
  title: ''
  type: SDKs
  url: https://github.com/AttomDataSolutions/School_Sample_Code
- group: build
  title: ''
  type: SDKs
  url: https://github.com/AttomDataSolutions/POI_Sample_Code
- group: build
  title: ''
  type: SDKs
  url: https://github.com/AttomDataSolutions/Community_Sample_Code
- group: operate
  title: ''
  type: ContactEmail
  url: mailto:datacustomercare@attomdata.com
- group: operate
  title: ''
  type: ContactPhone
  url: tel:+18004625125
- group: commercial
  title: ''
  type: Plans
  url: plans/attomdata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/attomdata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/attomdata-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/attomdata-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/attomdata-rules.yml
created: '2026-05-25'
examples:
- key_count: 3
  name: Attom Area Hierarchy Example
  slug: attom-area-hierarchy-example
- key_count: 3
  name: Attom Community Neighborhood Example
  slug: attom-community-neighborhood-example
- key_count: 3
  name: Attom Poi Search Example
  slug: attom-poi-search-example
- key_count: 3
  name: Attom Property Detail Example
  slug: attom-property-detail-example
finops:
- name: Attomdata Finops
  service_category: ''
  slug: attomdata-finops
graphqls:
- description: Conceptual GraphQL schema for the ATTOM Property Intelligence API suite, covering
  name: ATTOM Data GraphQL Schema
  slug: attomdata-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/attomdata.png
json_schemas:
- name: ATTOM Area
  property_count: 8
  slug: attom-area
- name: ATTOM Assessment
  property_count: 5
  slug: attom-assessment
- name: ATTOM AVM
  property_count: 3
  slug: attom-avm
- name: ATTOM Community
  property_count: 6
  slug: attom-community
- name: ATTOM Property
  property_count: 8
  slug: attom-property
- name: ATTOM Sale
  property_count: 5
  slug: attom-sale
jsonld:
- class_count: 0
  name: Attomdata Context
  property_count: 10
  slug: attomdata-context
layout: provider
modified: '2026-05-25'
name: ATTOM
nav: Providers
network: true
overview: 'ATTOM publishes 18 APIs on the [APIs.io](https://apis.io/) network, including All Events API, Assessment API, AVM API, and 15 more. Tagged areas include Real Estate, Property Data, Property Intelligence, Mortgage, and Assessment.


  The ATTOM catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ATTOM''s developer surface includes authentication, developer portal, documentation, signup flow, engineering blog, support, GitHub presence, and 27 more developer resources.'
plans:
- name: Attomdata Plans Pricing
  plan_count: 4
  slug: attomdata-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 0
  name: Attomdata Rate Limits
  slug: attomdata-rate-limits
rules:
- name: ATTOM API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: attomdata-jsonschema-spectral-rules
- name: ATTOM API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 3
  slug: attomdata-rules
score:
  band: developing
  composite: 51.9
  delta: -2.7
  facets:
    commercial_clarity: 52.6
    contract_quality: 66.3
    developer_ergonomics: 54.3
    discoverability: 55.0
    governance: 86.8
    operational_transparency: 5.3
  previous_composite: 54.6
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/attomdata/refs/heads/main/screenshots/attomdata-2026-06-20T172541.png
security:
- kind: authentication
  name: Attomdata Authentication
  slug: attomdata-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Attomdata Domain Security
  slug: attomdata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: attomdata
tags:
- Real Estate
- Property Data
- Property Intelligence
- Mortgage
- Assessment
- AVM
- Foreclosure
- Transactions
- Owner Data
- Building Permits
- Geospatial
- Boundaries
- Demographics
- Neighborhood
- POI
- Insurance
- Mortgage Technology
- PropTech
website: https://api.developer.attomdata.com/
---
