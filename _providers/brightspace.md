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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Brightspace Agentic Access
  operation_count: 55
  slug: brightspace-agentic-access
  summary_line: 55 operations · 18 acting
api_count: 1
apis:
- baseURL: https://{host}/d2l/api/lp
  baseurl_source: declared
  description: Assignment (Dropbox) folders, submissions, and feedback.
  name: D2L Brightspace Assignments API
  slug: brightspace-assignments-api
- baseURL: https://{host}/d2l/api/lp
  baseurl_source: declared
  description: Course calendar events.
  name: D2L Brightspace Calendar API
  slug: brightspace-calendar-api
- baseURL: https://{host}/d2l/api/lp
  baseurl_source: declared
  description: Course content - modules and topics.
  name: D2L Brightspace Content API
  slug: brightspace-content-api
- baseURL: https://{host}/d2l/api/lp
  baseurl_source: declared
  description: Data Export Framework and Brightspace Data Sets.
  name: D2L Brightspace Data Hub API
  slug: brightspace-data-hub-api
- baseURL: https://{host}/d2l/api/lp
  baseurl_source: declared
  description: Discussion forums, topics, and posts.
  name: D2L Brightspace Discussions API
  slug: brightspace-discussions-api
- baseURL: https://{host}/d2l/api/lp
  baseurl_source: declared
  description: Membership of users in org units.
  name: D2L Brightspace Enrollments API
  slug: brightspace-enrollments-api
- baseURL: https://{host}/d2l/api/lp
  baseurl_source: declared
  description: Course gradebook - grade objects, values, categories, and schemes.
  name: D2L Brightspace Grades API
  slug: brightspace-grades-api
- baseURL: https://{host}/d2l/api/lp
  baseurl_source: declared
  description: Learning outcome sets, outcomes, and alignments.
  name: D2L Brightspace Learning Outcomes API
  slug: brightspace-learning-outcomes-api
- baseURL: https://{host}/d2l/api/lp
  baseurl_source: declared
  description: News (announcement) items.
  name: D2L Brightspace News API
  slug: brightspace-news-api
- baseURL: https://{host}/d2l/api/lp
  baseurl_source: declared
  description: Organization structure, course offerings, departments, and semesters.
  name: D2L Brightspace Org Units API
  slug: brightspace-org-units-api
- baseURL: https://{host}/d2l/api/lp
  baseurl_source: declared
  description: Quizzes, attempts, questions, and special access.
  name: D2L Brightspace Quizzes API
  slug: brightspace-quizzes-api
- baseURL: https://{host}/d2l/api/lp
  baseurl_source: declared
  description: User accounts and roles on the Learning Platform.
  name: D2L Brightspace Users API
  slug: brightspace-users-api
- baseURL: https://{host}/d2l/api/lp
  baseurl_source: declared
  description: Product component version discovery.
  name: D2L Brightspace Versions API
  slug: brightspace-versions-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: D2L Brightspace Valence Learning Framework Assignments API
  slug: open-brightspace-assignments-api
- collection_type: open
  name: D2L Brightspace Valence Learning Framework Assignments Calendar API
  slug: open-brightspace-calendar-api
- collection_type: open
  name: D2L Brightspace Valence Learning Framework Assignments Content API
  slug: open-brightspace-content-api
- collection_type: open
  name: D2L Brightspace Valence Learning Framework Assignments Data Hub API
  slug: open-brightspace-data-hub-api
- collection_type: open
  name: D2L Brightspace Valence Learning Framework Assignments Discussions API
  slug: open-brightspace-discussions-api
- collection_type: open
  name: D2L Brightspace Valence Learning Framework Assignments Enrollments API
  slug: open-brightspace-enrollments-api
- collection_type: open
  name: D2L Brightspace Valence Learning Framework Assignments Grades API
  slug: open-brightspace-grades-api
- collection_type: open
  name: D2L Brightspace Valence Learning Framework Assignments Learning Outcomes API
  slug: open-brightspace-learning-outcomes-api
- collection_type: open
  name: D2L Brightspace Valence Learning Framework Assignments News API
  slug: open-brightspace-news-api
- collection_type: open
  name: D2L Brightspace Valence Learning Framework Assignments Org Units API
  slug: open-brightspace-org-units-api
- collection_type: open
  name: D2L Brightspace Valence Learning Framework Assignments Quizzes API
  slug: open-brightspace-quizzes-api
- collection_type: open
  name: D2L Brightspace Valence Learning Framework Assignments Users API
  slug: open-brightspace-users-api
- collection_type: open
  name: D2L Brightspace Valence Learning Framework Assignments Versions API
  slug: open-brightspace-versions-api
- collection_type: open
  name: D2L Brightspace Valence API
  slug: open-brightspace
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/brightspace-capability-edges.yml
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


  D2L Brightspace''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Brightspace Plans Pricing
  plan_count: 3
  slug: brightspace-plans-pricing
random_paper: 9
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
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.6
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 40.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
