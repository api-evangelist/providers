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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The University of Macau Data and Open Data API Platform provides JSON APIs to data published by UM, organized into categories including About UM (organizational units and public holidays), Academic (c
  name: UM Data and Open Data API Platform
  slug: data-platform
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-macau-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.um.edu.mo/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.um.edu.mo/
- group: auth
  title: ''
  type: Authentication
  url: https://data.um.edu.mo/quickstart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://data.um.edu.mo/terms-and-conditions-of-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universityofmacau/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-macau-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-macau-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-macau-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Macau (UM), founded in 1981, is the leading public comprehensive research university of the Macao Special Administrative Region and is ranked #245 in the QS World University Rankings 2025. English is its main medium of instruction and around 80 percent of its faculty are recruited internationally. UM operates a public-facing Data and Open Data API Platform at data.um.edu.mo, managed by its Information and Communication Technology Office (ICTO), exposing JSON APIs across categories such as About UM, Academic, Facilities, Media, and Student data. Access requires registration and an API key via UMPASS, and the platform is primarily oriented toward UM staff and students.'
finops:
- name: University Of Macau Finops
  service_category: Education
  slug: university-of-macau-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-macau.png
jsonld:
- class_count: 15
  name: University Of Macau Context
  property_count: 5
  slug: university-of-macau-context
layout: provider
modified: '2026-06-03'
name: University of Macau
nav: Providers
network: true
overview: 'University of Macau publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Open Data, and Macau.


  The University of Macau catalog on APIs.io includes 1 JSON-LD context.


  University of Macau''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: University Of Macau Plans Pricing
  plan_count: 2
  slug: university-of-macau-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 1
  name: University Of Macau Rate Limits
  slug: university-of-macau-rate-limits
score:
  band: emerging
  composite: 26.0
  delta: -3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 19.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-macau/refs/heads/main/screenshots/university-of-macau-2026-06-20T200211.png
security:
- kind: domain-security
  name: University Of Macau Domain Security
  slug: university-of-macau-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-macau
tags:
- Education
- Higher Education
- University
- Open Data
- Macau
- China
website: https://www.um.edu.mo/
---
