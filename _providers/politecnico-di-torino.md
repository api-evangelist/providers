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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Politecnico Di Torino Agentic Access
  operation_count: 132
  slug: politecnico-di-torino-agentic-access
  summary_line: 132 operations · 44 acting
api_count: 17
apis:
- description: Politecnico di Torino's official React Native mobile application for students, open-sourced under EUPL 1.2. It is a reference consumer of the PoliTO REST API; its configuration points at the https://a
  name: PoliTO Students App (mobile backend client)
  slug: students-app
- description: Institutional open-data portal publishing freely reusable academic datasets (study programs and courses, student enrollment, international students, graduates, mobility, and doctoral programs) under a
  name: PoliTO Open Data
  slug: open-data
- description: The Announcements API from Politecnico di Torino — 2 operation(s) for announcements.
  name: Politecnico di Torino Announcements API
  slug: politecnico-di-torino-announcements-api
- description: The Auth API from Politecnico di Torino — 11 operation(s) for auth.
  name: Politecnico di Torino Auth API
  slug: politecnico-di-torino-auth-api
- description: The Bookings API from Politecnico di Torino — 5 operation(s) for bookings.
  name: Politecnico di Torino Bookings API
  slug: politecnico-di-torino-bookings-api
- description: The Courses API from Politecnico di Torino — 12 operation(s) for courses.
  name: Politecnico di Torino Courses API
  slug: politecnico-di-torino-courses-api
- description: The Esc API from Politecnico di Torino — 2 operation(s) for esc.
  name: Politecnico di Torino Esc API
  slug: politecnico-di-torino-esc-api
- description: The Exams API from Politecnico di Torino — 3 operation(s) for exams.
  name: Politecnico di Torino Exams API
  slug: politecnico-di-torino-exams-api
- description: The Job offers API from Politecnico di Torino — 2 operation(s) for job offers.
  name: Politecnico di Torino Job offers API
  slug: politecnico-di-torino-job-offers-api
- description: The Lectures API from Politecnico di Torino — 1 operation(s) for lectures.
  name: Politecnico di Torino Lectures API
  slug: politecnico-di-torino-lectures-api
- description: The News API from Politecnico di Torino — 2 operation(s) for news.
  name: Politecnico di Torino News API
  slug: politecnico-di-torino-news-api
- description: The Offering API from Politecnico di Torino — 4 operation(s) for offering.
  name: Politecnico di Torino Offering API
  slug: politecnico-di-torino-offering-api
- description: The People API from Politecnico di Torino — 2 operation(s) for people.
  name: Politecnico di Torino People API
  slug: politecnico-di-torino-people-api
- description: The Places API from Politecnico di Torino — 7 operation(s) for places.
  name: Politecnico di Torino Places API
  slug: politecnico-di-torino-places-api
- description: The Student API from Politecnico di Torino — 16 operation(s) for student.
  name: Politecnico di Torino Student API
  slug: politecnico-di-torino-student-api
- description: The Surveys API from Politecnico di Torino — 1 operation(s) for surveys.
  name: Politecnico di Torino Surveys API
  slug: politecnico-di-torino-surveys-api
- description: The Tickets API from Politecnico di Torino — 10 operation(s) for tickets.
  name: Politecnico di Torino Tickets API
  slug: politecnico-di-torino-tickets-api
artifact_total: 35
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/polito/rn-apps/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/politecnico-di-torino-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/politecnico-di-torino-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/politecnico-di-torino-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.polito.it/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/polito
- group: company
  title: ''
  type: LinkedIn
  url: https://it.linkedin.com/school/politecnico-di-torino/
- group: other
  title: ''
  type: OpenData
  url: https://www.polito.it/open-data
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/polito/api-spec
- group: commercial
  title: ''
  type: Plans
  url: plans/politecnico-di-torino-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/politecnico-di-torino-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/politecnico-di-torino-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Politecnico di Torino (PoliTO) is Italy''s oldest technical university, founded in 1859 in Turin, and a leading European institution for engineering, architecture, and design, ranked #241 in the QS World University Rankings 2025. Its public developer footprint centers on an official OpenAPI specification (polito/api-spec) for the REST API that powers the official students mobile application, plus an institutional open-data portal publishing academic datasets. Code is published openly under the verified @polito GitHub organization, while the production API itself is consumed by official first-party apps and is not offered as a self-service public developer program.'
examples:
- key_count: 5
  name: Politecnico Di Torino Getannouncements Example
  slug: politecnico-di-torino-getAnnouncements-example
- key_count: 5
  name: Politecnico Di Torino Getexams Example
  slug: politecnico-di-torino-getExams-example
- key_count: 5
  name: Politecnico Di Torino Getstudent Example
  slug: politecnico-di-torino-getStudent-example
finops:
- name: Politecnico Di Torino Finops
  service_category: Education
  slug: politecnico-di-torino-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/politecnico-di-torino.png
json_schemas:
- name: Announcement
  property_count: 8
  slug: politecnico-di-torino-announcement
- name: Booking
  property_count: 9
  slug: politecnico-di-torino-booking
- name: Exam
  property_count: 17
  slug: politecnico-di-torino-exam
- name: Student
  property_count: 20
  slug: politecnico-di-torino-student
json_structures:
- name: Politecnico Di Torino Exam Structure
  property_count: 17
  slug: politecnico-di-torino-exam-structure
- name: Politecnico Di Torino Student Structure
  property_count: 20
  slug: politecnico-di-torino-student-structure
jsonld:
- class_count: 33
  name: Politecnico Di Torino Context
  property_count: 5
  slug: politecnico-di-torino-context
layout: provider
modified: '2026-06-03'
name: Politecnico di Torino
nav: Providers
network: true
overview: 'Politecnico di Torino publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Announcements API, Auth API, Bookings API, and 12 more. Tagged areas include Education, Higher Education, University, Italy, and Open Data.


  The Politecnico di Torino catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Politecnico di Torino''s developer surface includes authentication, GitHub presence, and 11 more developer resources.'
plans:
- name: Politecnico Di Torino Plans Pricing
  plan_count: 2
  slug: politecnico-di-torino-plans-pricing
random_paper: 99
rate_limits:
- limit_count: 1
  name: Politecnico Di Torino Rate Limits
  slug: politecnico-di-torino-rate-limits
rules:
- name: Politecnico di Torino API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: politecnico-di-torino-jsonschema-spectral-rules
- name: Politecnico di Torino API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: politecnico-di-torino-rules
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.3
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/politecnico-di-torino/refs/heads/main/screenshots/politecnico-di-torino-2026-06-20T191855.png
security:
- kind: authentication
  name: Politecnico Di Torino Authentication
  slug: politecnico-di-torino-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Politecnico Di Torino Domain Security
  slug: politecnico-di-torino-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: politecnico-di-torino
tags:
- Education
- Higher Education
- University
- Italy
- Open Data
- Mobile
- OpenAPI
website: https://www.polito.it/en
---
