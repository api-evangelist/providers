---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Brightspace Agentic Access
  operation_count: 55
  slug: brightspace-agentic-access
  summary_line: 55 operations · 18 acting
api_count: 13
apis:
- description: Assignment (Dropbox) folders, submissions, and feedback.
  name: D2L Brightspace Assignments API
  slug: brightspace-assignments-api
- description: Course calendar events.
  name: D2L Brightspace Calendar API
  slug: brightspace-calendar-api
- description: Course content - modules and topics.
  name: D2L Brightspace Content API
  slug: brightspace-content-api
- description: Data Export Framework and Brightspace Data Sets.
  name: D2L Brightspace Data Hub API
  slug: brightspace-data-hub-api
- description: Discussion forums, topics, and posts.
  name: D2L Brightspace Discussions API
  slug: brightspace-discussions-api
- description: Membership of users in org units.
  name: D2L Brightspace Enrollments API
  slug: brightspace-enrollments-api
- description: Course gradebook - grade objects, values, categories, and schemes.
  name: D2L Brightspace Grades API
  slug: brightspace-grades-api
- description: Learning outcome sets, outcomes, and alignments.
  name: D2L Brightspace Learning Outcomes API
  slug: brightspace-learning-outcomes-api
- description: News (announcement) items.
  name: D2L Brightspace News API
  slug: brightspace-news-api
- description: Organization structure, course offerings, departments, and semesters.
  name: D2L Brightspace Org Units API
  slug: brightspace-org-units-api
- description: Quizzes, attempts, questions, and special access.
  name: D2L Brightspace Quizzes API
  slug: brightspace-quizzes-api
- description: User accounts and roles on the Learning Platform.
  name: D2L Brightspace Users API
  slug: brightspace-users-api
- description: Product component version discovery.
  name: D2L Brightspace Versions API
  slug: brightspace-versions-api
artifact_total: 21
collections:
- collection_type: open
  name: D2L Brightspace Valence API
  slug: open-brightspace
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brightspace-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brightspace-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brightspace-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/brightspace-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Brightspace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/d2l
- group: company
  title: ''
  type: Website
  url: https://www.d2l.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.valence.desire2learn.com
- group: commercial
  title: ''
  type: Plans
  url: plans/brightspace-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brightspace-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brightspace-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.d2l.com/blog/all/
created: '2026-07-03'
description: D2L Brightspace is an enterprise learning management system (LMS) used by higher education, K-12, and corporate organizations. Its public REST API is the Valence Learning Framework API, exposed under https://{host}/d2l/api/ and split into two product components - "lp" (Learning Platform - users, roles, enrollments, org units, data hub) and "le" (Learning Environment - content, grades, assignments/dropbox, quizzes, discussions, calendar, news, learning outcomes). Routes are versioned per component (for example lp 1.x and le 1.x) and authenticated with OAuth 2 bearer tokens issued by the D2L auth service; the older ID-Key (app-id/user-id) scheme is deprecated. D2L is the vendor; Valence is the historical name of the API framework.
finops:
- name: Brightspace Finops
  service_category: Education Technology and Learning Management
  slug: brightspace-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brightspace.png
layout: provider
modified: '2026-07-03'
name: D2L Brightspace
nav: Providers
network: true
overview: 'D2L Brightspace publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Assignments API, Calendar API, Content API, and 10 more. Tagged areas include LMS, Learning Management System, EdTech, Education, and Valence.


  D2L Brightspace''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Brightspace Plans Pricing
  plan_count: 3
  slug: brightspace-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Brightspace Rate Limits
  slug: brightspace-rate-limits
scopes:
- name: Brightspace Scopes
  scope_count: 4
  slug: brightspace-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 38.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brightspace/refs/heads/main/screenshots/brightspace-2026-07-25T203856.png
security:
- kind: authentication
  name: Brightspace Authentication
  slug: brightspace-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Brightspace Domain Security
  slug: brightspace-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: brightspace
tags:
- LMS
- Learning Management System
- EdTech
- Education
- Valence
- D2L
- Brightspace
website: https://www.d2l.com
---
