---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Quiz Api Agentic Access
  operation_count: 7
  slug: quiz-api-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- baseURL: https://quizapi.io
  baseurl_source: spec
  description: Endpoints that require no authentication
  name: QuizAPI Discovery API
  slug: quiz-api-discovery-api
- baseURL: https://quizapi.io
  baseurl_source: spec
  description: Retrieve questions for quizzes or browse across all quizzes
  name: QuizAPI Questions API
  slug: quiz-api-questions-api
- baseURL: https://quizapi.io
  baseurl_source: spec
  description: Browse and search published quizzes
  name: QuizAPI Quizzes API
  slug: quiz-api-quizzes-api
artifact_total: 14
collections:
- collection_type: open
  name: Quiz Discovery API
  slug: open-quiz-api-discovery-api
- collection_type: open
  name: Quiz Discovery Questions API
  slug: open-quiz-api-questions-api
- collection_type: open
  name: Quiz Discovery Quizzes API
  slug: open-quiz-api-quizzes-api
- collection_type: open
  name: QuizAPI
  slug: open-quiz-api
common:
- group: commercial
  href: https://artifacts.apis.io/quiz-api/plans/quiz-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quiz-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/quiz-api/rate-limits/quiz-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/quiz-api-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/quiz-api/finops/quiz-api-finops.yml
  title: ''
  type: FinOps
  url: finops/quiz-api-finops.yml
- group: agent
  href: https://artifacts.apis.io/quiz-api/agentic-access/quiz-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/quiz-api-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/quiz-api/security/quiz-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quiz-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/quiz-api/authentication/quiz-api-authentication.yml
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
- has_sources: false
  method: generated
  name: Quiz Api Finops
  primary_unit: request
  service_category: API
  slug: quiz-api-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quiz-api.png
layout: provider
modified: '2026-05-19'
name: QuizAPI
nav: Providers
network: true
overview: 'QuizAPI publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Discovery API, Questions API, and Quizzes API. Tagged areas include Quizzes, Trivia, Education, Assessment, and Content.


  The QuizAPI catalog on APIs.io includes 1 Spectral governance ruleset.


  QuizAPI''s developer surface includes authentication, documentation, signup flow, support, engineering blog, and 7 more developer resources.'
plans:
- name: Quiz Api Plans Pricing
  plan_count: 3
  slug: quiz-api-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Quiz Api Rate Limits
  slug: quiz-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: QuizAPI API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: quiz-api-rules
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 21.1
    contract_governance: 13.6
    contract_quality: 57.7
    developer_ergonomics: 35.7
    discoverability: 64.3
    operational_transparency: 15.8
  previous_composite: 32.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/quiz-api/quiz-api-2026-06-20T192440.png
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
