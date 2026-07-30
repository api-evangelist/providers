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
- acting_count: 2
  human_in_the_loop: 0
  name: University Of Waterloo Agentic Access
  operation_count: 48
  slug: university-of-waterloo-agentic-access
  summary_line: 48 operations · 2 acting
api_count: 12
apis:
- description: The AcademicOrganizations API from University of Waterloo — 2 operation(s) for academicorganizations.
  name: University of Waterloo AcademicOrganizations API
  slug: university-of-waterloo-academicorganizations-api
- description: The Account API from University of Waterloo — 5 operation(s) for account.
  name: University of Waterloo Account API
  slug: university-of-waterloo-account-api
- description: The ClassSchedules API from University of Waterloo — 3 operation(s) for classschedules.
  name: University of Waterloo ClassSchedules API
  slug: university-of-waterloo-classschedules-api
- description: The Courses API from University of Waterloo — 5 operation(s) for courses.
  name: University of Waterloo Courses API
  slug: university-of-waterloo-courses-api
- description: The ExamSchedules API from University of Waterloo — 2 operation(s) for examschedules.
  name: University of Waterloo ExamSchedules API
  slug: university-of-waterloo-examschedules-api
- description: The FoodServices API from University of Waterloo — 6 operation(s) for foodservices.
  name: University of Waterloo FoodServices API
  slug: university-of-waterloo-foodservices-api
- description: The HolidayDates API from University of Waterloo — 3 operation(s) for holidaydates.
  name: University of Waterloo HolidayDates API
  slug: university-of-waterloo-holidaydates-api
- description: The ImportantDates API from University of Waterloo — 2 operation(s) for importantdates.
  name: University of Waterloo ImportantDates API
  slug: university-of-waterloo-importantdates-api
- description: The Locations API from University of Waterloo — 6 operation(s) for locations.
  name: University of Waterloo Locations API
  slug: university-of-waterloo-locations-api
- description: The Subjects API from University of Waterloo — 3 operation(s) for subjects.
  name: University of Waterloo Subjects API
  slug: university-of-waterloo-subjects-api
- description: The Terms API from University of Waterloo — 3 operation(s) for terms.
  name: University of Waterloo Terms API
  slug: university-of-waterloo-terms-api
- description: The Wcms API from University of Waterloo — 8 operation(s) for wcms.
  name: University of Waterloo Wcms API
  slug: university-of-waterloo-wcms-api
artifact_total: 35
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-waterloo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-waterloo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-waterloo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-waterloo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://uwaterloo.ca/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://uwaterloo.ca/api/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uWaterloo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-waterloo/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/uWaterloo/Datasets
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-waterloo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-waterloo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-waterloo-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://uwaterloo.ca/news/rss.xml
created: '2026-06-03'
description: 'The University of Waterloo is a public research university in Waterloo, Ontario, Canada, ranked #115 in the QS World University Rankings 2025 and known for its cooperative education programs and strength in mathematics, engineering, and computer science. Its developer footprint is centered on the University of Waterloo Open Data API (the Open Data Initiative), a public, key-authenticated REST API exposing authoritative academic, campus, and student-information datasets. Official code, documentation, and datasets are published under the verified uWaterloo GitHub organization.'
examples:
- key_count: 5
  name: University Of Waterloo Academicorganization Detail Example
  slug: university-of-waterloo-academicorganization-detail-example
- key_count: 19
  name: University Of Waterloo Course Detail Example
  slug: university-of-waterloo-course-detail-example
- key_count: 7
  name: University Of Waterloo Location Detail Example
  slug: university-of-waterloo-location-detail-example
- key_count: 7
  name: University Of Waterloo Term Current Example
  slug: university-of-waterloo-term-current-example
finops:
- name: University Of Waterloo Finops
  service_category: Education
  slug: university-of-waterloo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-waterloo.png
json_schemas:
- name: AcademicOrganization
  property_count: 5
  slug: university-of-waterloo-academicorganization
- name: Course
  property_count: 19
  slug: university-of-waterloo-course
- name: Location
  property_count: 7
  slug: university-of-waterloo-location
- name: Subject
  property_count: 5
  slug: university-of-waterloo-subject
- name: Term
  property_count: 7
  slug: university-of-waterloo-term
json_structures:
- name: University Of Waterloo Course Structure
  property_count: 11
  slug: university-of-waterloo-course-structure
- name: University Of Waterloo Location Structure
  property_count: 6
  slug: university-of-waterloo-location-structure
- name: University Of Waterloo Subject Structure
  property_count: 5
  slug: university-of-waterloo-subject-structure
- name: University Of Waterloo Term Structure
  property_count: 7
  slug: university-of-waterloo-term-structure
jsonld:
- class_count: 28
  name: University Of Waterloo Context
  property_count: 0
  slug: university-of-waterloo-context
layout: provider
modified: '2026-06-03'
name: University of Waterloo
nav: Providers
network: true
overview: 'University of Waterloo publishes 12 APIs on the [APIs.io](https://apis.io/) network, including AcademicOrganizations API, Account API, ClassSchedules API, and 9 more. Tagged areas include Education, Higher Education, University, Open Data, and Canada.


  The University of Waterloo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Waterloo''s developer surface includes authentication, GitHub presence, engineering blog, and 11 more developer resources.'
plans:
- name: University Of Waterloo Plans Pricing
  plan_count: 2
  slug: university-of-waterloo-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: University Of Waterloo Rate Limits
  slug: university-of-waterloo-rate-limits
rules:
- name: University of Waterloo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-waterloo-jsonschema-spectral-rules
- name: University of Waterloo API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 2
  slug: university-of-waterloo-rules
score:
  band: developing
  composite: 42.2
  delta: -4.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 42.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-waterloo/refs/heads/main/screenshots/university-of-waterloo-2026-06-20T200326.png
security:
- kind: authentication
  name: University Of Waterloo Authentication
  slug: university-of-waterloo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: University Of Waterloo Domain Security
  slug: university-of-waterloo-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of Waterloo Vulnerability Disclosure
  slug: university-of-waterloo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-waterloo
tags:
- Education
- Higher Education
- University
- Open Data
- Canada
- Research
website: https://uwaterloo.ca/
---
