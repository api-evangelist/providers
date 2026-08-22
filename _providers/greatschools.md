---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
api_count: 2
apis:
- description: Retrieve key information about schools across the United States based on proximity to a location or filtered by name, type, and more. Returns school names, addresses, grades offered, type, and website
  name: GreatSchools School Essentials API
  slug: school-essentials
- description: Builds on School Essentials by adding GreatSchools School Rating Bands (below average, average, above average) to assess school quality.
  name: GreatSchools School Quality API
  slug: school-quality
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/greatschools-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/greatschools
- group: company
  title: ''
  type: Website
  url: https://www.greatschools.org
- group: other
  title: ''
  type: Developer Hub
  url: https://www.greatschools.org/api
created: '2026-03-16'
description: GreatSchools provides school information, ratings, and quality data via its Developer Hub APIs, including the School Essentials API for school details and the School Quality API for GreatSchools rating bands.
finops:
- name: Greatschools Finops
  service_category: API
  slug: greatschools-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/greatschools.png
layout: provider
modified: '2026-04-28'
name: GreatSchools
nav: Providers
network: true
overview: GreatSchools publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Schools, Education, Ratings, and Geolocation.
plans:
- name: Greatschools Plans Pricing
  plan_count: 3
  slug: greatschools-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Greatschools Rate Limits
  slug: greatschools-rate-limits
score:
  band: minimal
  composite: 6.7
  delta: -2.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/greatschools/refs/heads/main/screenshots/greatschools-2026-06-20T182349.png
security:
- kind: domain-security
  name: Greatschools Domain Security
  slug: greatschools-domain-security
  summary_line: TLSv1.2 · DMARC
slug: greatschools
tags:
- Schools
- Education
- Ratings
- Geolocation
website: https://www.greatschools.org
---
