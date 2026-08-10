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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 6
apis:
- description: Information on all classes offered in a selected term, including title, description, notes and final exam details, as well as class sections with meeting times, locations, enrollment details, units an
  name: Classes API
  slug: classes
- description: Information on all approved courses (currently and historically offered) at UCLA, including course title, description, General Education and diversity attributes, and course requisites, with the abili
  name: Courses API
  slug: courses
- description: Access to general data dictionary information and descriptions from the UCLA Registrar's Office, used to interpret coded values across the student information system APIs. Access is gated by the porta
  name: Dictionary API
  slug: dictionary
- description: Returns the information needed to build the MyUCLA megamenu navigation, published through the UCLA API Developer Portal. Access is gated by the portal's approval workflow.
  name: MyUCLA Menu Data API
  slug: myucla-menu
- description: Endpoints for obtaining information about production calendar operations and scheduled jobs, published through the UCLA API Developer Portal. Access is gated by the portal's approval workflow.
  name: Production Calendar Jobs API
  slug: production-calendar-jobs
- description: UCLA Library Digital Collections comply with the International Image Interoperability Framework (IIIF). Each item page exposes a IIIF JSON manifest that can be opened in IIIF-compatible viewers and to
  name: UCLA Library Digital Collections IIIF
  slug: library-iiif
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucla-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ucla.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.api.ucla.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ucla
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ucla/
- group: commercial
  title: ''
  type: Plans
  url: plans/ucla-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucla-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucla-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of California, Los Angeles (UCLA) is a public land-grant research university in Los Angeles, California, ranked #30 in the QS World University Rankings 2025. UCLA operates a centralized API Developer Portal (developer.api.ucla.edu) that publishes a catalog of campus APIs covering student information systems, course and class data, the Registrar data dictionary, MyUCLA menu data, and enterprise integration services. Most products are interactive-documented but gated behind an access request and approval workflow with App Key/secret credentials. UCLA Library additionally exposes IIIF-compliant digital collections manifests for image interoperability.'
finops:
- name: Ucla Finops
  service_category: Education
  slug: ucla-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucla.png
jsonld:
- class_count: 13
  name: Ucla Context
  property_count: 3
  slug: ucla-context
layout: provider
modified: '2026-06-03'
name: University of California, Los Angeles
nav: Providers
network: true
overview: 'University of California, Los Angeles publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Student Information, and Course Catalog.


  The University of California, Los Angeles catalog on APIs.io includes 1 JSON-LD context.


  University of California, Los Angeles'' developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Ucla Plans Pricing
  plan_count: 2
  slug: ucla-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 1
  name: Ucla Rate Limits
  slug: ucla-rate-limits
score:
  band: emerging
  composite: 20.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ucla/refs/heads/main/screenshots/ucla-2026-06-20T195941.png
security:
- kind: domain-security
  name: Ucla Domain Security
  slug: ucla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ucla
tags:
- Education
- Higher Education
- University
- Student Information
- Course Catalog
- Library
- IIIF
- United States
- California
website: https://www.ucla.edu/
---
