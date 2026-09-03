---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Educative API is a platform that provides developers with access to a wide range of educational materials and resources through an easy-to-use interface. With Educative API, developers can access tuto
  name: Educative API
  slug: educative
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/educative-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.educative.io/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/educative-inc
- group: agent
  title: ''
  type: LlmsText
  url: https://www.educative.io/llms.txt
created: '2025-03-01'
description: Educative is an online learning platform that provides high-quality, interactive courses for developers of all skill levels. With a focus on practical, hands-on learning, Educative offers courses on a wide range of topics, from programming languages like Python and JavaScript to data structures and algorithms. Each course is created by expert instructors and includes quizzes, coding challenges, and real-world projects to help learners apply their knowledge.
finops:
- name: Educative Finops
  service_category: API
  slug: educative-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/educative.png
layout: provider
modified: '2026-04-28'
name: Educative
nav: Providers
network: true
overview: 'Educative publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Courses, Education, and Learning.


  Educative''s developer surface includes engineering blog and 3 more developer resources.'
plans:
- name: Educative Plans Pricing
  plan_count: 3
  slug: educative-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Educative Rate Limits
  slug: educative-rate-limits
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/educative/refs/heads/main/screenshots/educative-2026-06-20T180500.png
security:
- kind: domain-security
  name: Educative Domain Security
  slug: educative-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: educative
tags:
- Courses
- Education
- Learning
---
