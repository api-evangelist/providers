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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Numbers Api Agentic Access
  operation_count: 9
  slug: numbers-api-agentic-access
  summary_line: 9 operations
api_count: 1
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
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Numbers Date API
  slug: open-numbers-api-date-api
- collection_type: open
  name: Numbers Date Math API
  slug: open-numbers-api-math-api
- collection_type: open
  name: Numbers Date Numbers API API
  slug: open-numbers-api-numbers-api-api
- collection_type: open
  name: Numbers Date Random API
  slug: open-numbers-api-random-api
- collection_type: open
  name: Numbers Date Trivia API
  slug: open-numbers-api-trivia-api
- collection_type: open
  name: Numbers Date Year API
  slug: open-numbers-api-year-api
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
random_paper: 10
rate_limits:
- limit_count: 0
  name: Numbers Api Rate Limits
  slug: numbers-api-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Numbers API API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: numbers-api-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 55.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 9.8
    contract_quality: 56.0
    developer_ergonomics: 6.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 30.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
