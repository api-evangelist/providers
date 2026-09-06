---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Teachable Agentic Access
  operation_count: 28
  slug: teachable-agentic-access
  summary_line: 28 operations · 6 acting
api_count: 2
apis:
- baseURL: https://developers.teachable.com/v1
  baseurl_source: declared
  description: Course management endpoints
  name: Teachable Courses API
  slug: teachable-courses-api
- baseURL: https://developers.teachable.com/v1
  baseurl_source: declared
  description: Endpoints for the authenticated current user
  name: Teachable CurrentUser API
  slug: teachable-currentuser-api
- baseURL: https://developers.teachable.com/v1
  baseurl_source: declared
  description: Enrollment management endpoints
  name: Teachable Enrollments API
  slug: teachable-enrollments-api
- baseURL: https://developers.teachable.com/v1
  baseurl_source: declared
  description: Lecture management endpoints
  name: Teachable Lectures API
  slug: teachable-lectures-api
- baseURL: https://developers.teachable.com/v1
  baseurl_source: declared
  description: Pricing plan endpoints
  name: Teachable PricingPlans API
  slug: teachable-pricingplans-api
- baseURL: https://developers.teachable.com/v1
  baseurl_source: declared
  description: Quiz and quiz response endpoints
  name: Teachable Quizzes API
  slug: teachable-quizzes-api
- baseURL: https://developers.teachable.com/v1
  baseurl_source: declared
  description: Transaction and sales endpoints
  name: Teachable Transactions API
  slug: teachable-transactions-api
- baseURL: https://developers.teachable.com/v1
  baseurl_source: declared
  description: User management endpoints
  name: Teachable Users API
  slug: teachable-users-api
- baseURL: https://developers.teachable.com/v1
  baseurl_source: declared
  description: Video access endpoints for current user
  name: Teachable Videos API
  slug: teachable-videos-api
- baseURL: https://developers.teachable.com/v1
  baseurl_source: declared
  description: Webhook configuration and event endpoints
  name: Teachable Webhooks API
  slug: teachable-webhooks-api
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Teachable Admin Courses API
  slug: open-teachable-courses-api
- collection_type: open
  name: Teachable Admin Courses CurrentUser API
  slug: open-teachable-currentuser-api
- collection_type: open
  name: Teachable Admin Courses Enrollments API
  slug: open-teachable-enrollments-api
- collection_type: open
  name: Teachable Admin Courses Lectures API
  slug: open-teachable-lectures-api
- collection_type: open
  name: Teachable Admin Courses PricingPlans API
  slug: open-teachable-pricingplans-api
- collection_type: open
  name: Teachable Admin Courses Quizzes API
  slug: open-teachable-quizzes-api
- collection_type: open
  name: Teachable Admin Courses Transactions API
  slug: open-teachable-transactions-api
- collection_type: open
  name: Teachable Admin Courses Users API
  slug: open-teachable-users-api
- collection_type: open
  name: Teachable Admin Courses Videos API
  slug: open-teachable-videos-api
- collection_type: open
  name: Teachable Admin Courses Webhooks API
  slug: open-teachable-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/teachable-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/teachable-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/teachable-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/teachable-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teachable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/teachable-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/teachable-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://teachable.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.teachable.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usefedora
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teachable
- group: other
  title: ''
  type: X
  url: https://x.com/teachable
- group: company
  title: ''
  type: Blog
  url: https://www.teachable.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.teachable.com
- group: commercial
  title: ''
  type: Pricing
  url: https://teachable.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://www.teachablestatus.com
- group: operate
  title: ''
  type: Support
  url: https://support.teachable.com
- group: commercial
  title: ''
  type: Plans
  url: plans/teachable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/teachable-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/teachable-finops.yml
created: '2026-06-12'
description: 'Teachable is an online course and coaching platform that empowers creators to build and sell educational content without technical expertise. The Teachable REST API provides programmatic access to school management capabilities including course management, user enrollment, quiz responses, and sales transaction data. The API supports two authentication patterns: a server-side Admin API using API keys and an OAuth API for third-party application integrations. API access is available on Growth and Advanced plans, with webhook support for event-driven workflows covering enrollment, lecture completion, sales, and user lifecycle events.'
examples:
- key_count: 4
  name: Teachable Create User Request
  slug: teachable-create-user-request
- key_count: 2
  name: Teachable Enroll User Request
  slug: teachable-enroll-user-request
- key_count: 1
  name: Teachable Get Course Response
  slug: teachable-get-course-response
- key_count: 2
  name: Teachable List Courses Response
  slug: teachable-list-courses-response
- key_count: 2
  name: Teachable List Transactions Response
  slug: teachable-list-transactions-response
finops:
- name: Teachable Finops
  service_category: ''
  slug: teachable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teachable.png
json_schemas:
- name: TeachableCourse
  property_count: 8
  slug: teachable-course
- name: TeachableEnrollment
  property_count: 5
  slug: teachable-enrollment
- name: TeachableTransaction
  property_count: 21
  slug: teachable-transaction
- name: TeachableUser
  property_count: 8
  slug: teachable-user
- name: TeachableWebhook
  property_count: 5
  slug: teachable-webhook
jsonld:
- class_count: 98
  name: Teachable Context
  property_count: 17
  slug: teachable-context
layout: provider
modified: '2026-06-12'
name: Teachable
nav: Providers
network: true
overview: 'Teachable publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Courses API, CurrentUser API, Enrollments API, and 7 more. Tagged areas include Online Courses, E-Learning, Education, Course Management, and Enrollments.


  The Teachable catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Teachable''s developer surface includes authentication, documentation, engineering blog, changelog, pricing, support, and 14 more developer resources.'
plans:
- name: Teachable Plans Pricing
  plan_count: 5
  slug: teachable-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Teachable Rate Limits
  slug: teachable-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Teachable API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: teachable-jsonschema-spectral-rules
scopes:
- name: Teachable Scopes
  scope_count: 4
  slug: teachable-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 56.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 74.3
    catalog_earned_first_party: 0.0
    catalog_gap: 40.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 63.9
    developer_ergonomics: 36.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 55.3
  previous_composite: 56.6
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
    regime: Education & Research
    regime_id: education
    score: 70.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/teachable/refs/heads/main/screenshots/teachable-2026-06-20T194953.png
security:
- kind: authentication
  name: Teachable Authentication
  slug: teachable-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Teachable Domain Security
  slug: teachable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Teachable Vulnerability Disclosure
  slug: teachable-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Teachable Trust Center
  slug: teachable-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: teachable
tags:
- Online Courses
- E-Learning
- Education
- Course Management
- Enrollments
- Coaching
- Memberships
- Transaction
website: https://teachable.com
---
