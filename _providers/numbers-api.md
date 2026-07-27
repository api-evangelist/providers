---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Numbers Api Agentic Access
  operation_count: 9
  slug: numbers-api-agentic-access
  summary_line: 9 operations
api_count: 6
apis:
- description: The Date API from Numbers API — 1 operation(s) for date.
  name: Numbers API Date API
  slug: numbers-api-date-api
- description: The Math API from Numbers API — 1 operation(s) for math.
  name: Numbers API Math API
  slug: numbers-api-math-api
- description: The Numbers API API from Numbers API — 1 operation(s) for numbers api.
  name: Numbers API Numbers API API
  slug: numbers-api-numbers-api-api
- description: The Random API from Numbers API — 4 operation(s) for random.
  name: Numbers API Random API
  slug: numbers-api-random-api
- description: The Trivia API from Numbers API — 1 operation(s) for trivia.
  name: Numbers API Trivia API
  slug: numbers-api-trivia-api
- description: The Year API from Numbers API — 1 operation(s) for year.
  name: Numbers API Year API
  slug: numbers-api-year-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/numbers-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/numbers-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://numbersapi.com
- group: docs
  title: ''
  type: Documentation
  url: http://numbersapi.com/#42
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/divad12
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/in/davidhu2000/
- group: company
  title: ''
  type: Blog
  url: http://numbersapi.com
- group: commercial
  title: ''
  type: Pricing
  url: http://numbersapi.com
- group: operate
  title: ''
  type: StatusPage
  url: http://numbersapi.com
- group: other
  title: ''
  type: X
  url: https://x.com/numbersapi
- group: commercial
  title: ''
  type: Plans
  url: plans/numbers-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/numbers-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/numbers-api-finops.yml
created: '2026-06-13'
description: 'Free REST API providing interesting mathematical facts, trivia, dates, and year facts about numbers for educational and fun applications. Returns short, readable facts about any number or date across four categories: trivia, mathematical properties, notable years, and day-of-year historical events. No authentication or API key required.'
examples:
- key_count: 4
  name: Batch Facts Json
  slug: batch-facts-json
- key_count: 5
  name: Date Fact Json
  slug: date-fact-json
- key_count: 4
  name: Math Fact Json
  slug: math-fact-json
- key_count: 4
  name: Trivia Fact Json
  slug: trivia-fact-json
- key_count: 5
  name: Year Fact Json
  slug: year-fact-json
finops:
- name: Numbers Api Finops
  service_category: ''
  slug: numbers-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/numbers-api.png
json_schemas:
- name: NumberFact
  property_count: 6
  slug: number-fact
jsonld:
- class_count: 5
  name: Numbers Api Context
  property_count: 6
  slug: numbers-api-context
layout: provider
modified: '2026-06-13'
name: Numbers API
nav: Providers
network: true
overview: 'Numbers API publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Date API, Math API, Numbers API API, and 3 more. Tagged areas include Numbers, Trivia, Math, Facts, and Education.


  The Numbers API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Numbers API''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Numbers Api Plans Pricing
  plan_count: 1
  slug: numbers-api-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 0
  name: Numbers Api Rate Limits
  slug: numbers-api-rate-limits
rules:
- name: Numbers API API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: numbers-api-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.3
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 46.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/numbers-api/refs/heads/main/screenshots/numbers-api-2026-06-20T190517.png
security:
- kind: domain-security
  name: Numbers Api Domain Security
  slug: numbers-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: numbers-api
tags:
- Numbers
- Trivia
- Math
- Facts
- Education
- Free
- No Auth
website: http://numbersapi.com
---
