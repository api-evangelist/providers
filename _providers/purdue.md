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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Purdue Agentic Access
  operation_count: 20
  slug: purdue-agentic-access
  summary_line: 20 operations
api_count: 11
apis:
- description: The Purdue University Research Repository (PURR) exposes an OAI-PMH endpoint for harvesting research dataset metadata, supporting standard verbs (Identify, ListSets, ListMetadataFormats, ListIdentifie
  name: PURR OAI-PMH Metadata API
  slug: purr-oaipmh
- description: The Buildings API from Purdue University — 2 operation(s) for buildings.
  name: Purdue University Buildings API
  slug: purdue-buildings-api
- description: The Campuses API from Purdue University — 2 operation(s) for campuses.
  name: Purdue University Campuses API
  slug: purdue-campuses-api
- description: The Classes API from Purdue University — 2 operation(s) for classes.
  name: Purdue University Classes API
  slug: purdue-classes-api
- description: The Courses API from Purdue University — 2 operation(s) for courses.
  name: Purdue University Courses API
  slug: purdue-courses-api
- description: The Instructors API from Purdue University — 2 operation(s) for instructors.
  name: Purdue University Instructors API
  slug: purdue-instructors-api
- description: The Meetings API from Purdue University — 2 operation(s) for meetings.
  name: Purdue University Meetings API
  slug: purdue-meetings-api
- description: The Rooms API from Purdue University — 2 operation(s) for rooms.
  name: Purdue University Rooms API
  slug: purdue-rooms-api
- description: The Sections API from Purdue University — 2 operation(s) for sections.
  name: Purdue University Sections API
  slug: purdue-sections-api
- description: The Subjects API from Purdue University — 2 operation(s) for subjects.
  name: Purdue University Subjects API
  slug: purdue-subjects-api
- description: The Terms API from Purdue University — 2 operation(s) for terms.
  name: Purdue University Terms API
  slug: purdue-terms-api
artifact_total: 28
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/purdue-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/purdue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.purdue.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Purdue
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/purdue-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/purdue-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/purdue-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/purdue-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/purdue-context.jsonld
created: '2026-06-03'
description: 'Purdue University is a public land-grant research university in West Lafayette, Indiana, United States, ranked #99 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is limited and largely community- or service-specific rather than a single centralized developer portal. Confirmed public interfaces include the community-built Purdue.io OData course-catalog API and the Purdue University Research Repository (PURR) OAI-PMH metadata endpoint. A Purdue Libraries API host exists but currently serves only a placeholder page.'
examples:
- key_count: 2
  name: Purdue Listcampuses Example
  slug: purdue-listCampuses-example
- key_count: 2
  name: Purdue Listcourses Example
  slug: purdue-listCourses-example
- key_count: 2
  name: Purdue Listsubjects Example
  slug: purdue-listSubjects-example
finops:
- name: Purdue Finops
  service_category: Education
  slug: purdue-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/purdue.png
json_schemas:
- name: Course
  property_count: 6
  slug: purdue-course
- name: Meeting
  property_count: 9
  slug: purdue-meeting
- name: Section
  property_count: 6
  slug: purdue-section
- name: Subject
  property_count: 3
  slug: purdue-subject
json_structures:
- name: Purdue Course Structure
  property_count: 6
  slug: purdue-course-structure
- name: Purdue Section Structure
  property_count: 6
  slug: purdue-section-structure
jsonld:
- class_count: 34
  name: Purdue Context
  property_count: 3
  slug: purdue-context
layout: provider
modified: '2026-06-03'
name: Purdue University
nav: Providers
network: true
overview: 'Purdue University publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Buildings API, Campuses API, Classes API, and 7 more. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Purdue University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Purdue University''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Purdue Plans Pricing
  plan_count: 2
  slug: purdue-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 1
  name: Purdue Rate Limits
  slug: purdue-rate-limits
rules:
- name: Purdue University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: purdue-jsonschema-spectral-rules
- name: Purdue University API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: purdue-rules
score:
  band: thin
  composite: 36.9
  delta: -0.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.9
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/purdue/refs/heads/main/screenshots/purdue-2026-06-20T192313.png
security:
- kind: domain-security
  name: Purdue Domain Security
  slug: purdue-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: purdue
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- United States
website: https://www.purdue.edu/
---
