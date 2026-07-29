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
- acting_count: 8
  human_in_the_loop: 0
  name: Learnworlds Agentic Access
  operation_count: 18
  slug: learnworlds-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 7
apis:
- description: Read the school's courses and their contents.
  name: LearnWorlds Courses API
  slug: learnworlds-courses-api
- description: Enroll and unenroll users on courses, bundles, and subscriptions.
  name: LearnWorlds Enrollments API
  slug: learnworlds-enrollments-api
- description: Read payments, subscriptions, and transactions.
  name: LearnWorlds Payments API
  slug: learnworlds-payments-api
- description: Read per-user course progress and completion.
  name: LearnWorlds Progress API
  slug: learnworlds-progress-api
- description: List tags and attach / detach them from users.
  name: LearnWorlds Tags API
  slug: learnworlds-tags-api
- description: Manage school users (students / members) and their profiles.
  name: LearnWorlds Users API
  slug: learnworlds-users-api
- description: Manage webhook subscriptions for school events.
  name: LearnWorlds Webhooks API
  slug: learnworlds-webhooks-api
artifact_total: 15
collections:
- collection_type: open
  name: LearnWorlds API
  slug: open-learnworlds
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/learnworlds-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/learnworlds-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/learnworlds-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/learnworlds-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/learnworlds
- group: company
  title: ''
  type: Website
  url: https://www.learnworlds.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.learnworlds.dev/docs/api
- group: commercial
  title: ''
  type: Plans
  url: plans/learnworlds-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/learnworlds-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/learnworlds-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.learnworlds.com/blog/
created: '2026-07-05'
description: LearnWorlds is an online course and learning management (LMS) platform that lets creators, trainers, and businesses build, sell, and run branded online schools. Its REST API (v2) is served per-school from https://{school}.learnworlds.com/admin/api/v2 and exposes school entities - users, courses, enrollments, subscriptions, payments, course progress, tags, bundles, and certificates - plus webhooks for real-time events. Requests are authenticated with OAuth2 client credentials (a bearer access token) together with an Lw-Client header identifying the client application. API and webhook access is a plan-gated feature available on the Learning Center and High Volume & Corporate plans.
finops:
- name: Learnworlds Finops
  service_category: Education and Learning Management
  slug: learnworlds-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/learnworlds.png
layout: provider
modified: '2026-07-05'
name: LearnWorlds
nav: Providers
network: true
overview: 'LearnWorlds publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Courses API, Enrollments API, Payments API, and 4 more. Tagged areas include Online Courses, LMS, eLearning, Education, and Course Platform.


  LearnWorlds'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Learnworlds Plans Pricing
  plan_count: 4
  slug: learnworlds-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Learnworlds Rate Limits
  slug: learnworlds-rate-limits
scopes:
- name: Learnworlds Scopes
  scope_count: 0
  slug: learnworlds-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.4
  delta: -3.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/learnworlds/refs/heads/main/screenshots/learnworlds-2026-07-25T224802.png
security:
- kind: authentication
  name: Learnworlds Authentication
  slug: learnworlds-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Learnworlds Domain Security
  slug: learnworlds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: learnworlds
tags:
- Online Courses
- LMS
- eLearning
- Education
- Course Platform
- Creator Economy
website: https://www.learnworlds.com
---
