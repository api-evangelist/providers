---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Johns Hopkins University Agentic Access
  operation_count: 7
  slug: johns-hopkins-university-agentic-access
  summary_line: 7 operations
api_count: 4
apis:
- description: REST API exposing data from the Hub database, a central repository of news articles, announcements, photo galleries, faculty experts, and events. Built to power the Hub website and reused across JHU s
  name: JHU Hub API
  slug: hub
- description: Central API management platform built on MuleSoft Anypoint, where JHU developers and consumers view and request access to integration APIs. Gated to Johns Hopkins affiliates rather than open to the pu
  name: JHU API Portal (MuleSoft Anypoint)
  slug: api-portal
- description: Course and section lookup and advanced search.
  name: Johns Hopkins University Classes API
  slug: johns-hopkins-university-classes-api
- description: Reference code lists (schools, terms, departments).
  name: Johns Hopkins University Codes API
  slug: johns-hopkins-university-codes-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/johns-hopkins-university-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/johns-hopkins-university-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/johns-hopkins-university-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.jhu.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.jh.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/jhu-sheridan-libraries
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/johns-hopkins-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/johns-hopkins-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/johns-hopkins-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/johns-hopkins-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Johns Hopkins University is a private research university in Baltimore, Maryland, ranked #22 in the QS World University Rankings 2025. It maintains a real public developer footprint: the Hub API serves news, announcements, events, photo galleries, and faculty experts from the university Hub database, and the Self-Service Public Course Search API (SIS) returns course catalog data in JSON. A central MuleSoft-based API Portal (api.jh.edu) governs integration APIs but is gated to JHU affiliates. The university also operates numerous public GitHub organizations across its libraries, data services, and research centers.'
examples:
- key_count: 2
  name: Johns Hopkins University Advanced Search Example
  slug: johns-hopkins-university-advanced-search-example
- key_count: 2
  name: Johns Hopkins University Schools Example
  slug: johns-hopkins-university-schools-example
finops:
- name: Johns Hopkins University Finops
  service_category: Education
  slug: johns-hopkins-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/johns-hopkins-university.png
json_schemas:
- name: Course
  property_count: 36
  slug: johns-hopkins-university-course
json_structures:
- name: Johns Hopkins University Course Structure
  property_count: 36
  slug: johns-hopkins-university-course-structure
jsonld:
- class_count: 19
  name: Johns Hopkins University Context
  property_count: 4
  slug: johns-hopkins-university-context
layout: provider
modified: '2026-06-03'
name: Johns Hopkins University
nav: Providers
network: true
overview: 'Johns Hopkins University publishes 2 APIs on the [APIs.io](https://apis.io/) network: Classes API and Codes API. Tagged areas include Education, Higher Education, University, Research, and Course Catalog.


  The Johns Hopkins University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Johns Hopkins University''s developer surface includes authentication, GitHub presence, and 9 more developer resources.'
plans:
- name: Johns Hopkins University Plans Pricing
  plan_count: 2
  slug: johns-hopkins-university-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 1
  name: Johns Hopkins University Rate Limits
  slug: johns-hopkins-university-rate-limits
rules:
- name: Johns Hopkins University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: johns-hopkins-university-jsonschema-spectral-rules
- name: Johns Hopkins University API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 2
  slug: johns-hopkins-university-rules
score:
  band: developing
  composite: 44.0
  delta: -4.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 69.5
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/johns-hopkins-university/refs/heads/main/screenshots/johns-hopkins-university-2026-06-20T183755.png
security:
- kind: authentication
  name: Johns Hopkins University Authentication
  slug: johns-hopkins-university-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Johns Hopkins University Domain Security
  slug: johns-hopkins-university-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: johns-hopkins-university
tags:
- Education
- Higher Education
- University
- Research
- Course Catalog
- News
- United States
website: https://www.jhu.edu/
---
