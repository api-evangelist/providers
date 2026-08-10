---
access_model:
  confidence: medium
  label: Free · Requires approval
  onboarding: approval
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
api_count: 7
apis:
- description: Central campus API developer portal for discovering, subscribing to, requesting elevated access for, and consuming UCSB web service APIs. Registration is required and new accounts are reviewed and app
  name: UCSB API Developer Portal
  slug: developer-portal
- description: APIs covering the life-cycle of campus, departments, and students, including Academic Curriculums, Academic Graduate Programs, Academic Quarter Calendar, BARC Quarter Calendar, CLAS Schedules, and Eve
  name: UCSB Academics APIs
  slug: academics
- description: APIs providing access to student rosters and individual student information including demographic, registration, academic program, and schedule data. Includes Student Courses, Student Registrations, S
  name: UCSB Students APIs
  slug: students
- description: Administrative APIs pertaining to financials, accounts receivable, and related campus systems, including ClassCode Lookup Service, Department Chartfield, PeopleSoft FAU Combination Service, COA/CCOA c
  name: UCSB Administration APIs
  slug: administration
- description: APIs providing campus dining venue information used by students, faculty, and staff, including Dining Cams, Dining Commons, Dining Menu, Dining Patrons, and Meal Plan Rates.
  name: UCSB Dining APIs
  slug: dining
- description: APIs delivering student housing data, including Contract Status and Housing Assignments.
  name: UCSB Housing APIs
  slug: housing
- description: APIs offering faculty and staff details such as the Employee Job API and related identity mapping services.
  name: UCSB Employees APIs
  slug: employees
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucsb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ucsb.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ucsb.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ucsb
- group: operate
  title: ''
  type: Status
  url: https://status.library.ucsb.edu/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uc-santa-barbara/
- group: commercial
  title: ''
  type: Plans
  url: plans/ucsb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucsb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucsb-finops.yml
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
  url: json-ld/ucsb-context.jsonld
- group: company
  title: ''
  type: About
  url: https://alexandria.ucsb.edu/
created: '2026-06-03'
description: 'University of California, Santa Barbara (UCSB) is a public land-grant research university and a member of the University of California system, ranked #79 in the QS World University Rankings 2025. UCSB operates a formal, well-structured API Developer Portal at developer.ucsb.edu that exposes campus enterprise APIs across Academics, Administration, Dining, Employees, Housing, and Students categories. Most APIs are gated behind registration and manual account approval (security classifications include Auto-Approved, Access Approval Required, and Private). The UCSB Library also runs the Alexandria Digital Research Library (ADRL), a Samvera/Fedora-based institutional repository, and maintains an official GitHub organization at github.com/ucsb.'
finops:
- name: Ucsb Finops
  service_category: Education
  slug: ucsb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucsb.png
jsonld:
- class_count: 17
  name: Ucsb Context
  property_count: 6
  slug: ucsb-context
layout: provider
modified: '2026-07-25'
name: University of California, Santa Barbara
nav: Providers
network: true
overview: 'University of California, Santa Barbara publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Student Information System, and Campus.


  The University of California, Santa Barbara catalog on APIs.io includes 1 JSON-LD context.


  University of California, Santa Barbara''s developer surface includes GitHub presence, status page, engineering blog, and 10 more developer resources.'
plans:
- name: Ucsb Plans Pricing
  plan_count: 2
  slug: ucsb-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 1
  name: Ucsb Rate Limits
  slug: ucsb-rate-limits
score:
  band: emerging
  composite: 21.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ucsb/refs/heads/main/screenshots/ucsb-2026-06-20T195943.png
security:
- kind: domain-security
  name: Ucsb Domain Security
  slug: ucsb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ucsb
tags:
- Education
- Higher Education
- University
- Student Information System
- Campus
- California
- United States
website: https://www.ucsb.edu/
---
