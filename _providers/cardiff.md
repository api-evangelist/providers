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
  name: Cardiff Agentic Access
  operation_count: 26
  slug: cardiff-agentic-access
  summary_line: 26 operations
api_count: 16
apis:
- description: The Assessments API from Cardiff University — 1 operation(s) for assessments.
  name: Cardiff University Assessments API
  slug: cardiff-assessments-api
- description: The Clearing Adjustments API from Cardiff University — 1 operation(s) for clearing adjustments.
  name: Cardiff University Clearing Adjustments API
  slug: cardiff-clearing-adjustments-api
- description: The Courses API from Cardiff University — 4 operation(s) for courses.
  name: Cardiff University Courses API
  slug: cardiff-courses-api
- description: The * API from Cardiff University — 1 operation(s) for *.
  name: Cardiff University * API
  slug: cardiff-default-api
- description: The Groups API from Cardiff University — 1 operation(s) for groups.
  name: Cardiff University Groups API
  slug: cardiff-groups-api
- description: The Levels API from Cardiff University — 1 operation(s) for levels.
  name: Cardiff University Levels API
  slug: cardiff-levels-api
- description: The Modules API from Cardiff University — 5 operation(s) for modules.
  name: Cardiff University Modules API
  slug: cardiff-modules-api
- description: The Occurrences API from Cardiff University — 4 operation(s) for occurrences.
  name: Cardiff University Occurrences API
  slug: cardiff-occurrences-api
- description: The Publications API from Cardiff University — 2 operation(s) for publications.
  name: Cardiff University Publications API
  slug: cardiff-publications-api
- description: The Qualifications API from Cardiff University — 1 operation(s) for qualifications.
  name: Cardiff University Qualifications API
  slug: cardiff-qualifications-api
- description: The Rollover API from Cardiff University — 2 operation(s) for rollover.
  name: Cardiff University Rollover API
  slug: cardiff-rollover-api
- description: The Schools API from Cardiff University — 1 operation(s) for schools.
  name: Cardiff University Schools API
  slug: cardiff-schools-api
- description: The Semesters API from Cardiff University — 1 operation(s) for semesters.
  name: Cardiff University Semesters API
  slug: cardiff-semesters-api
- description: The Subjects API from Cardiff University — 1 operation(s) for subjects.
  name: Cardiff University Subjects API
  slug: cardiff-subjects-api
- description: The Test API from Cardiff University — 1 operation(s) for test.
  name: Cardiff University Test API
  slug: cardiff-test-api
- description: The Years API from Cardiff University — 1 operation(s) for years.
  name: Cardiff University Years API
  slug: cardiff-years-api
artifact_total: 37
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cardiff-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cardiff-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cardiff-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cardiff-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.cardiff.ac.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.cardiff.ac.uk/devportal/
- group: auth
  title: ''
  type: Authentication
  url: https://data.cardiff.ac.uk/devportal/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/cardiff-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/cardiff-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cardiff-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cardiff-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Cardiff University is a public research university in Cardiff, Wales, United Kingdom, ranked #186 in the QS World University Rankings 2025. The university operates a public developer portal at data.cardiff.ac.uk (powered by WSO2 API Manager) exposing a small set of RESTful institutional APIs covering courses, modules, lookups, and research publications. The APIs are OAuth2-secured: integration requires creating an application and generating consumer keys and access tokens, with external developer access granted on request by emailing integration@cardiff.ac.uk. The gateway is hosted at api.data.cardiff.ac.uk.'
examples:
- key_count: 2
  name: Cardiff Courses List Example
  slug: cardiff-courses-list-example
- key_count: 2
  name: Cardiff Lookups Schools Example
  slug: cardiff-lookups-schools-example
- key_count: 2
  name: Cardiff Modules List Example
  slug: cardiff-modules-list-example
- key_count: 2
  name: Cardiff Publications List Example
  slug: cardiff-publications-list-example
finops:
- name: Cardiff Finops
  service_category: Education
  slug: cardiff-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cardiff.png
json_schemas:
- name: Course
  property_count: 19
  slug: cardiff-course
- name: Meta
  property_count: 5
  slug: cardiff-meta
- name: Module
  property_count: 10
  slug: cardiff-module
- name: Publication
  property_count: 31
  slug: cardiff-publication
json_structures:
- name: Cardiff Course Structure
  property_count: 13
  slug: cardiff-course-structure
- name: Cardiff Module Structure
  property_count: 10
  slug: cardiff-module-structure
- name: Cardiff Publication Structure
  property_count: 16
  slug: cardiff-publication-structure
jsonld:
- class_count: 5
  name: Cardiff Context
  property_count: 4
  slug: cardiff-context
layout: provider
modified: '2026-06-03'
name: Cardiff University
nav: Providers
network: true
overview: 'Cardiff University publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Assessments API, Clearing Adjustments API, Courses API, and 13 more. Tagged areas include Education, Higher Education, University, United Kingdom, and Wales.


  The Cardiff University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cardiff University''s developer surface includes authentication and 11 more developer resources.'
plans:
- name: Cardiff Plans Pricing
  plan_count: 2
  slug: cardiff-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 1
  name: Cardiff Rate Limits
  slug: cardiff-rate-limits
rules:
- name: Cardiff University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cardiff-jsonschema-spectral-rules
- name: Cardiff University API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: cardiff-rules
scopes:
- name: Cardiff Scopes
  scope_count: 2
  slug: cardiff-scopes
  summary_line: 2 scopes · implicit
score:
  band: developing
  composite: 42.4
  delta: -4.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 57.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cardiff/refs/heads/main/screenshots/cardiff-2026-06-20T173956.png
security:
- kind: authentication
  name: Cardiff Authentication
  slug: cardiff-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cardiff Domain Security
  slug: cardiff-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cardiff
tags:
- Education
- Higher Education
- University
- United Kingdom
- Wales
- Open Data
- Courses
- Research
website: https://www.cardiff.ac.uk/
---
