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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: A suite of APIs published by the OIT Integrations Team providing access to frequently used and requested University data sourced from the Common Data Layer (CDL). Includes Person Basic Information, Cl
  name: Common Good APIs
  slug: common-good-apis
- description: University of Minnesota Libraries APIs for programmatically downloading items, text, and metadata from the UMedia digital collections. Includes a JSON API for metadata/text and an IIIF API for still i
  name: UMedia Digital Collection APIs
  slug: umedia-digital-collections
- description: A collection of agricultural and geospatial data APIs from GEMS Informatics at the University of Minnesota, including Climate, Weather, Soils, Hydro, Elevation, Land Cover, Crop Calendar, Market acces
  name: GEMS Informatics Exchange APIs
  slug: gems-exchange-apis
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-minnesota-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://twin-cities.umn.edu
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UMNLibraries
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-minnesota/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sites.google.com/umn.edu/integration-apis/home
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/GEMS-UMN
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-minnesota-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-minnesota-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-minnesota-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Minnesota is a public land-grant research university with its flagship campus in the Twin Cities (Minneapolis-Saint Paul), ranked #203 in the QS World University Rankings 2025. Its developer/API footprint is led by the OIT Integrations Team, which publishes a suite of "Common Good APIs" sourced from the University''s Common Data Layer (CDL) covering person, HR, student, class, and organization data; access requires request and data-custodian approval. Additional public-facing APIs include the University Libraries digital collection APIs (UMedia JSON and IIIF) and GEMS Informatics agricultural/geospatial data APIs. Most data APIs are gated behind access requests and institutional authentication.'
finops:
- name: University Of Minnesota Finops
  service_category: Education
  slug: university-of-minnesota-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-minnesota.png
jsonld:
- class_count: 24
  name: University Of Minnesota Context
  property_count: 6
  slug: university-of-minnesota-context
layout: provider
modified: '2026-06-03'
name: University of Minnesota
nav: Providers
network: true
overview: 'University of Minnesota publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The University of Minnesota catalog on APIs.io includes 1 JSON-LD context.


  University of Minnesota''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: University Of Minnesota Plans Pricing
  plan_count: 2
  slug: university-of-minnesota-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: University Of Minnesota Rate Limits
  slug: university-of-minnesota-rate-limits
score:
  band: emerging
  composite: 19.3
  delta: -1.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-minnesota/refs/heads/main/screenshots/university-of-minnesota-2026-06-20T200207.png
security:
- kind: domain-security
  name: University Of Minnesota Domain Security
  slug: university-of-minnesota-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-minnesota
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Geospatial
- United States
- Minnesota
website: https://twin-cities.umn.edu
---
