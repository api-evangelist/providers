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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
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
random_paper: 23
rate_limits:
- limit_count: 1
  name: Texas A M University Rate Limits
  slug: texas-a-m-university-rate-limits
score:
  band: emerging
  composite: 22.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 8.7
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.7
  schema_version: 0.5
  scored_at: '2026-07-23'
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
