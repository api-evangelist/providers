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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Schoology Agentic Access
  operation_count: 28
  slug: schoology-agentic-access
  summary_line: 28 operations · 8 acting
api_count: 2
apis:
- description: REST API for the Schoology K-12 LMS. Authenticated via OAuth. Supports realm resources (districts, schools, buildings, users, groups, courses, sections), realm objects (enrollments, events, blog posts
  name: Schoology REST API v1
  slug: rest-api-v1
- baseURL: https://api.schoology.com/v1/
  baseurl_source: declared
  description: The Assignments API from Schoology — 2 operation(s) for assignments.
  name: Schoology Assignments API
  slug: schoology-assignments-api
- baseURL: https://api.schoology.com/v1/
  baseurl_source: declared
  description: The Courses API from Schoology — 2 operation(s) for courses.
  name: Schoology Courses API
  slug: schoology-courses-api
- baseURL: https://api.schoology.com/v1/
  baseurl_source: declared
  description: The Enrollments API from Schoology — 2 operation(s) for enrollments.
  name: Schoology Enrollments API
  slug: schoology-enrollments-api
- baseURL: https://api.schoology.com/v1/
  baseurl_source: declared
  description: The Grades API from Schoology — 2 operation(s) for grades.
  name: Schoology Grades API
  slug: schoology-grades-api
- baseURL: https://api.schoology.com/v1/
  baseurl_source: declared
  description: The Groups API from Schoology — 2 operation(s) for groups.
  name: Schoology Groups API
  slug: schoology-groups-api
- baseURL: https://api.schoology.com/v1/
  baseurl_source: declared
  description: The Multi-Call API from Schoology — 2 operation(s) for multi-call.
  name: Schoology Multi-Call API
  slug: schoology-multi-call-api
- baseURL: https://api.schoology.com/v1/
  baseurl_source: declared
  description: The Sections API from Schoology — 4 operation(s) for sections.
  name: Schoology Sections API
  slug: schoology-sections-api
- baseURL: https://api.schoology.com/v1/
  baseurl_source: declared
  description: The Submissions API from Schoology — 2 operation(s) for submissions.
  name: Schoology Submissions API
  slug: schoology-submissions-api
- baseURL: https://api.schoology.com/v1/
  baseurl_source: declared
  description: The Subscriptions API from Schoology — 1 operation(s) for subscriptions.
  name: Schoology Subscriptions API
  slug: schoology-subscriptions-api
- baseURL: https://api.schoology.com/v1/
  baseurl_source: declared
  description: The Targets API from Schoology — 2 operation(s) for targets.
  name: Schoology Targets API
  slug: schoology-targets-api
- baseURL: https://api.schoology.com/v1/
  baseurl_source: declared
  description: The Users API from Schoology — 6 operation(s) for users.
  name: Schoology Users API
  slug: schoology-users-api
- baseURL: https://api.schoology.com/v1/
  baseurl_source: declared
  description: The Events API from Schoology — 0 operation(s) for events.
  name: Schoology Events API
  slug: schoology-events-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Schoology REST API v1 Assignments API
  slug: open-schoology-assignments-api
- collection_type: open
  name: Schoology REST API v1 Assignments Courses API
  slug: open-schoology-courses-api
- collection_type: open
  name: Schoology REST API v1 Assignments Enrollments API
  slug: open-schoology-enrollments-api
- collection_type: open
  name: Schoology REST API v1 Assignments Grades API
  slug: open-schoology-grades-api
- collection_type: open
  name: Schoology REST API v1 Assignments Groups API
  slug: open-schoology-groups-api
- collection_type: open
  name: Schoology REST API v1 Assignments Multi-Call API
  slug: open-schoology-multi-call-api
- collection_type: open
  name: Schoology REST API v1 Assignments Sections API
  slug: open-schoology-sections-api
- collection_type: open
  name: Schoology REST API v1 Assignments Submissions API
  slug: open-schoology-submissions-api
- collection_type: open
  name: Schoology REST API v1 Assignments Subscriptions API
  slug: open-schoology-subscriptions-api
- collection_type: open
  name: Schoology REST API v1 Assignments Targets API
  slug: open-schoology-targets-api
- collection_type: open
  name: Schoology REST API v1 Assignments Users API
  slug: open-schoology-users-api
- collection_type: open
  name: Schoology Event Triggers (Webhooks) API
  slug: open-schoology-webhooks
- collection_type: open
  name: Schoology REST API v1
  slug: open-schoology
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/schoology-capability-edges.yml
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
overview: 'Schoology publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Assignments API, Courses API, Enrollments API, and 9 more. Tagged areas include EdTech, LMS, and K-12.


  Schoology''s developer surface includes authentication and 11 more developer resources.'
plans:
- name: Schoology Plans Pricing
  plan_count: 1
  slug: schoology-plans-pricing
random_paper: 17
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
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 48.0
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.8
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
    regime: Education & Research
    regime_id: education
    score: 40.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
