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
  scored_at: '2026-09-06'
api_count: 1
apis:
- description: Educative API is a platform that provides developers with access to a wide range of educational materials and resources through an easy-to-use interface. With Educative API, developers can access tuto
  name: Educative API
  slug: educative
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.educative.io/
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
  type: LLMsTxt
  url: https://www.educative.io/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://www.educative.io/unlimited
- group: start
  title: ''
  type: SignUp
  url: https://www.educative.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.educative.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.educative.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.educative.io/faq/general-faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Educative-Inc
coverage:
  checked: '2026-09-06'
  detail: 'Educative ships an end-user learning product only — there is no developer program to profile: api., developers., developer., docs. and help.educative.io do not resolve in DNS, /developers, /docs and /api all 404 on the marketing site, the 318KB llms.txt the company itself publishes names every course and blog section but not one endpoint, and the /integrations page offers only Slack, Google Calendar and Figma "Connect" buttons with no API, webhook, SSO, SCIM or LTI surface behind them.'
  evidence:
  - status: 404
    url: https://www.educative.io/developers
  - status: 404
    url: https://www.educative.io/openapi.json
  - status: 404
    url: https://www.educative.io/.well-known/api-catalog
  - status: 200
    url: https://www.educative.io/llms.txt
  - status: 200
    url: https://www.educative.io/integrations
  reason: no-developer-program
  state: none
created: '2025-03-01'
description: Educative is an online learning platform that provides high-quality, interactive courses for developers of all skill levels. With a focus on practical, hands-on learning, Educative offers courses on a wide range of topics, from programming languages like Python and JavaScript to data structures and algorithms. Each course is created by expert instructors and includes quizzes, coding challenges, and real-world projects to help learners apply their knowledge.
finops:
- name: Educative Finops
  service_category: API
  slug: educative-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/educative.png
layout: provider
modified: '2026-09-06'
name: Educative
nav: Providers
network: true
overview: 'Educative publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Courses, Education, Learning, Online Learning, and Developer Training.


  Educative''s developer surface includes engineering blog, pricing, signup flow, support, and 7 more developer resources.'
plans:
- name: Educative Plans Pricing
  plan_count: 0
  slug: educative-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Educative Rate Limits
  slug: educative-rate-limits
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.9
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
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
- Online Learning
- Developer Training
- Interview Preparation
- EdTech
website: https://www.educative.io/
---
