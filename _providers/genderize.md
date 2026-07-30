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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Genderize Agentic Access
  operation_count: 1
  slug: genderize-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Predict the gender of one or more first names.
  name: Genderize.io Gender Prediction API
  slug: genderize-gender-prediction-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/genderize-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genderize-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://genderize.io
- group: docs
  title: ''
  type: Documentation
  url: https://genderize.io/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://genderize.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/genderize-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/genderize-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/genderize-finops.yml
- group: start
  title: ''
  type: Login
  url: https://genderize.io/login
- group: operate
  title: ''
  type: FAQ
  url: https://genderize.io/faq
- group: company
  title: ''
  type: Blog
  url: https://genderize.io/blog
- group: other
  title: ''
  type: X
  url: https://x.com/genderizeio
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/genderize
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/demografix
- group: operate
  title: ''
  type: StatusPage
  url: https://status.genderize.io
created: '2026-06-13'
description: Free REST API that predicts the gender of a first name with probability scores based on name statistics from millions of users worldwide. Part of the Demografix suite alongside Agify (age prediction) and Nationalize (nationality prediction), sharing a single API key across all three services.
examples:
- key_count: 3
  name: Authenticated Request
  slug: authenticated-request
- key_count: 3
  name: Batch Names Request
  slug: batch-names-request
- key_count: 3
  name: Country Scoped Request
  slug: country-scoped-request
- key_count: 3
  name: Single Name Request
  slug: single-name-request
- key_count: 3
  name: Unknown Gender Response
  slug: unknown-gender-response
finops:
- name: Genderize Finops
  service_category: ''
  slug: genderize-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/genderize.png
json_schemas:
- name: ErrorResponse
  property_count: 1
  slug: error-response
- name: GenderPrediction
  property_count: 4
  slug: gender-prediction
jsonld:
- class_count: 2
  name: context Context
  property_count: 6
  slug: context
layout: provider
modified: '2026-06-13'
name: Genderize.io
nav: Providers
network: true
overview: 'Genderize.io publishes 1 API on the [APIs.io](https://apis.io/) network: Gender Prediction API. Tagged areas include Gender, Names, Prediction, Demographics, and Machine Learning.


  The Genderize.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Genderize.io''s developer surface includes documentation, pricing, FAQ, engineering blog, and 11 more developer resources.'
plans:
- name: Genderize Plans Pricing
  plan_count: 3
  slug: genderize-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 4
  name: Genderize Rate Limits
  slug: genderize-rate-limits
rules:
- name: Genderize.io API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: genderize-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.0
  delta: -3.8
  facets:
    commercial_clarity: 63.2
    contract_quality: 61.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/genderize/refs/heads/main/screenshots/genderize-2026-06-20T181721.png
security:
- kind: domain-security
  name: Genderize Domain Security
  slug: genderize-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: genderize
tags:
- Gender
- Names
- Prediction
- Demographics
- Machine Learning
- Statistics
website: https://genderize.io
---
