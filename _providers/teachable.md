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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Teachable Agentic Access
  operation_count: 28
  slug: teachable-agentic-access
  summary_line: 28 operations · 6 acting
api_count: 10
apis:
- description: Course management endpoints
  name: Teachable Courses API
  slug: teachable-courses-api
- description: Endpoints for the authenticated current user
  name: Teachable CurrentUser API
  slug: teachable-currentuser-api
- description: Enrollment management endpoints
  name: Teachable Enrollments API
  slug: teachable-enrollments-api
- description: Lecture management endpoints
  name: Teachable Lectures API
  slug: teachable-lectures-api
- description: Pricing plan endpoints
  name: Teachable PricingPlans API
  slug: teachable-pricingplans-api
- description: Quiz and quiz response endpoints
  name: Teachable Quizzes API
  slug: teachable-quizzes-api
- description: Transaction and sales endpoints
  name: Teachable Transactions API
  slug: teachable-transactions-api
- description: User management endpoints
  name: Teachable Users API
  slug: teachable-users-api
- description: Video access endpoints for current user
  name: Teachable Videos API
  slug: teachable-videos-api
- description: Webhook configuration and event endpoints
  name: Teachable Webhooks API
  slug: teachable-webhooks-api
artifact_total: 31
common:
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


  Teachable''s developer surface includes authentication, documentation, engineering blog, changelog, pricing, support, and 13 more developer resources.'
plans:
- name: Teachable Plans Pricing
  plan_count: 5
  slug: teachable-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Teachable Rate Limits
  slug: teachable-rate-limits
rules:
- name: Teachable API Rules
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
  band: developing
  composite: 57.3
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 67.4
    developer_ergonomics: 26.1
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 57.3
  schema_version: 0.5
  scored_at: '2026-07-23'
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
- Transactions
website: https://teachable.com
---
