---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Schoology Agentic Access
  operation_count: 28
  slug: schoology-agentic-access
  summary_line: 28 operations · 8 acting
api_count: 12
apis:
- description: REST API for the Schoology K-12 LMS. Authenticated via OAuth. Supports realm resources (districts, schools, buildings, users, groups, courses, sections), realm objects (enrollments, events, blog posts
  name: Schoology REST API v1
  slug: rest-api-v1
- description: The Assignments API from Schoology — 2 operation(s) for assignments.
  name: Schoology Assignments API
  slug: schoology-assignments-api
- description: The Courses API from Schoology — 2 operation(s) for courses.
  name: Schoology Courses API
  slug: schoology-courses-api
- description: The Enrollments API from Schoology — 2 operation(s) for enrollments.
  name: Schoology Enrollments API
  slug: schoology-enrollments-api
- description: The Grades API from Schoology — 2 operation(s) for grades.
  name: Schoology Grades API
  slug: schoology-grades-api
- description: The Groups API from Schoology — 2 operation(s) for groups.
  name: Schoology Groups API
  slug: schoology-groups-api
- description: The Multi-Call API from Schoology — 2 operation(s) for multi-call.
  name: Schoology Multi-Call API
  slug: schoology-multi-call-api
- description: The Sections API from Schoology — 4 operation(s) for sections.
  name: Schoology Sections API
  slug: schoology-sections-api
- description: The Submissions API from Schoology — 2 operation(s) for submissions.
  name: Schoology Submissions API
  slug: schoology-submissions-api
- description: The Subscriptions API from Schoology — 1 operation(s) for subscriptions.
  name: Schoology Subscriptions API
  slug: schoology-subscriptions-api
- description: The Targets API from Schoology — 2 operation(s) for targets.
  name: Schoology Targets API
  slug: schoology-targets-api
- description: The Users API from Schoology — 6 operation(s) for users.
  name: Schoology Users API
  slug: schoology-users-api
artifact_total: 21
collections:
- collection_type: open
  name: Schoology Event Triggers (Webhooks) API
  slug: open-schoology-webhooks
- collection_type: open
  name: Schoology REST API v1
  slug: open-schoology
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/schoology-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/schoology-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/schoology-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/schoology-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/schoology
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/schoology
- group: company
  title: ''
  type: Website
  url: https://www.schoology.com/
- group: other
  title: ''
  type: Developer
  url: https://developers.schoology.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/schoology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/schoology-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/schoology-finops.yml
created: '2026-05-08'
description: Schoology (a PowerSchool company) is a K-12 LMS. The Schoology REST API exposes districts, schools, buildings, users, groups, courses, sections, enrollments, events, blog posts, discussions, updates, media albums, documents, assignments, grades, grading scales, rubrics, attendance, submissions, pages, SCORM packages, friend requests, invites, networks, grading periods, roles, private messaging, search, and resource collections.
finops:
- name: Schoology Finops
  service_category: Education & Training
  slug: schoology-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/schoology.png
layout: provider
modified: '2026-05-30'
name: Schoology
nav: Providers
network: true
overview: 'Schoology publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Assignments API, Courses API, Enrollments API, and 8 more. Tagged areas include EdTech, LMS, and K-12.


  Schoology''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Schoology Plans Pricing
  plan_count: 1
  slug: schoology-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 1
  name: Schoology Rate Limits
  slug: schoology-rate-limits
scopes:
- name: Schoology Scopes
  scope_count: 0
  slug: schoology-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.2
  delta: -5.7
  facets:
    commercial_clarity: 13.2
    contract_quality: 50.1
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
security:
- kind: authentication
  name: Schoology Authentication
  slug: schoology-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Schoology Domain Security
  slug: schoology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: schoology
tags:
- EdTech
- LMS
- K-12
website: https://www.schoology.com/
---
