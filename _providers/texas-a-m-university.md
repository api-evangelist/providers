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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: Free geocoding, address normalization/standardization, and GIS data capture REST and SOAP API from TAMU GeoServices. Version 5 returns up to 172 output fields; an API key (from the account profile) is
  name: TAMU GeoServices Geocoding API
  slug: geoservices-geocode
- description: 'Texas A&M University System enterprise API to search/verify, create, and update Universal Identification Numbers (UIN). Access is gated: it requires registering an application, subscribing to UIN Prox'
  name: UIN Services API
  slug: uin-services
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/texas-a-m-university-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/texas-a-m-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tamu.edu
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-doc.sea.system.tamus.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/tamu-edu
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TAMULib
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/texas-a-m-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/texas-a-m-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/texas-a-m-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/texas-a-m-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Texas A&M University is a public land-grant research university in College Station, Texas, and the flagship of the Texas A&M University System. It is ranked #154 in the QS World University Rankings 2025. Its public developer footprint is led by the Texas A&M University System API Developer Portal (api-doc.sea.system.tamus.edu), which exposes gated enterprise services such as the UIN Services API behind subscription approval, alongside the publicly documented TAMU GeoServices geocoding/address API and an active library open-source ecosystem on GitHub (TAMULib) covering IIIF, DSpace, and Vireo ETD systems.'
finops:
- name: Texas A M University Finops
  service_category: Education
  slug: texas-a-m-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/texas-a-m-university.png
jsonld:
- class_count: 11
  name: Texas A M University Context
  property_count: 0
  slug: texas-a-m-university-context
layout: provider
modified: '2026-06-03'
name: Texas A&M University
nav: Providers
network: true
overview: 'Texas A&M University publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Geocoding.


  The Texas A&M University catalog on APIs.io includes 1 JSON-LD context.


  Texas A&M University''s developer surface includes GitHub presence and 10 more developer resources.'
plans:
- name: Texas A M University Plans Pricing
  plan_count: 2
  slug: texas-a-m-university-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Texas A M University Rate Limits
  slug: texas-a-m-university-rate-limits
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 28.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/texas-a-m-university/refs/heads/main/screenshots/texas-a-m-university-2026-06-20T195203.png
security:
- kind: domain-security
  name: Texas A M University Domain Security
  slug: texas-a-m-university-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Texas A M University Vulnerability Disclosure
  slug: texas-a-m-university-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: texas-a-m-university
tags:
- Education
- Higher Education
- University
- Research
- Geocoding
- Library
- United States
website: https://www.tamu.edu
---
