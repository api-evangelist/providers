---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Quiz Api Agentic Access
  operation_count: 7
  slug: quiz-api-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 3
apis:
- description: Endpoints that require no authentication
  name: QuizAPI Discovery API
  slug: quiz-api-discovery-api
- description: Retrieve questions for quizzes or browse across all quizzes
  name: QuizAPI Questions API
  slug: quiz-api-questions-api
- description: Browse and search published quizzes
  name: QuizAPI Quizzes API
  slug: quiz-api-quizzes-api
artifact_total: 10
collections:
- collection_type: open
  name: QuizAPI
  slug: open-quiz-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quiz-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quiz-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quiz-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://quizapi.io/
- group: docs
  title: ''
  type: Documentation
  url: https://quizapi.io/docs
- group: start
  title: ''
  type: Signup
  url: https://quizapi.io/signup
- group: operate
  title: ''
  type: Support
  url: https://github.com/QuizAPI/support/issues
- group: agent
  title: ''
  type: LlmsText
  url: https://quizapi.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://quizapi.io/blog
created: '2025-02-12'
description: QuizAPI provides programmatic access to thousands of quiz questions across topics such as programming, science, mathematics, and general knowledge. Developers can use the API to power trivia apps, online assessments, learning platforms, and embedded quizzes on their own websites. Questions can be filtered by category, difficulty, and tags, and quizzes can be created and managed through a JSON REST API.
finops:
- name: Quiz Api Finops
  service_category: API
  slug: quiz-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quiz-api.png
layout: provider
modified: '2026-05-19'
name: QuizAPI
nav: Providers
network: true
overview: 'QuizAPI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Discovery API, Questions API, and Quizzes API. Tagged areas include Quizzes, Trivia, Education, Assessment, and Content.


  QuizAPI''s developer surface includes authentication, documentation, signup flow, support, engineering blog, and 4 more developer resources.'
plans:
- name: Quiz Api Plans Pricing
  plan_count: 3
  slug: quiz-api-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Quiz Api Rate Limits
  slug: quiz-api-rate-limits
score:
  band: thin
  composite: 34.9
  delta: -5.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 59.0
    developer_ergonomics: 26.1
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/quiz-api/refs/heads/main/screenshots/quiz-api-2026-06-20T192440.png
security:
- kind: authentication
  name: Quiz Api Authentication
  slug: quiz-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Quiz Api Domain Security
  slug: quiz-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: quiz-api
tags:
- Quizzes
- Trivia
- Education
- Assessment
- Content
website: https://quizapi.io/
---
