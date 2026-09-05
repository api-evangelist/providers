---
access_model:
  confidence: medium
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
  score: 29.9
  scored_at: '2026-09-04'
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
  baseurl_source: declared
  description: Endpoints that require no authentication
  name: QuizAPI Discovery API
  slug: quiz-api-discovery-api
- baseURL: https://quizapi.io
  baseurl_source: declared
  description: Retrieve questions for quizzes or browse across all quizzes
  name: QuizAPI Questions API
  slug: quiz-api-questions-api
- baseURL: https://quizapi.io
  baseurl_source: declared
  description: Browse and search published quizzes
  name: QuizAPI Quizzes API
  slug: quiz-api-quizzes-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
random_paper: 18
rate_limits:
- limit_count: 5
  name: Quiz Api Rate Limits
  slug: quiz-api-rate-limits
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 55.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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
