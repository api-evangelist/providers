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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: A web service for integrating USC Schedule of Classes content (terms, departments, courses, and sections) into other web sites and applications. The online USC Schedule of Classes is itself a consumer
  name: USC Schedule of Classes (SOC) Web Services API
  slug: schedule-of-classes
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usc.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uscdatascience
- group: build
  title: ''
  type: GitHub
  url: https://github.com/isi-usc-edu
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-southern-california/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/USC
- group: commercial
  title: ''
  type: Plans
  url: plans/usc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/usc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/usc-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/usc-context.jsonld
created: '2026-06-03'
description: 'The University of Southern California (USC) is a private research university in Los Angeles, California, ranked #59 in the QS World University Rankings 2025. USC does not operate a single, centralized public API developer portal. Its most concretely documented public web service is the Schedule of Classes (SOC) Web Services API, which exposes course, department, and term data used to power the online schedule of classes. Beyond that, USC''s programmatic and data footprint is distributed across departmental and research GitHub organizations (such as the USC Information Retrieval & Data Science group and the USC Information Sciences Institute) and library/digital-collection systems, rather than a unified API catalog.'
finops:
- name: Usc Finops
  service_category: Education
  slug: usc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usc.png
jsonld:
- class_count: 9
  name: Usc Context
  property_count: 4
  slug: usc-context
layout: provider
modified: '2026-06-03'
name: University of Southern California
nav: Providers
network: true
overview: 'University of Southern California publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and United States.


  The University of Southern California catalog on APIs.io includes 1 JSON-LD context.


  University of Southern California''s developer surface includes GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Usc Plans Pricing
  plan_count: 2
  slug: usc-plans-pricing
random_paper: 91
rate_limits:
- limit_count: 1
  name: Usc Rate Limits
  slug: usc-rate-limits
score:
  band: emerging
  composite: 18.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 2.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usc/refs/heads/main/screenshots/usc-2026-06-20T200656.png
security:
- kind: domain-security
  name: Usc Domain Security
  slug: usc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: usc
tags:
- Education
- Higher Education
- University
- Research
- United States
- California
- Courses
website: https://www.usc.edu/
---
