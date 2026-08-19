---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agify Agentic Access
  operation_count: 1
  slug: agify-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Endpoints for predicting age from first names using statistical data.
  name: Agify.io Age Prediction API
  slug: agify-age-prediction-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Agify Age Prediction API
  slug: open-agify-age-prediction-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agify-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://agify.io
- group: docs
  title: ''
  type: Documentation
  url: https://agify.io/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://agify.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/agify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agify-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/agify-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: https://agify.io/register
- group: operate
  title: ''
  type: FAQ
  url: https://agify.io/faq
- group: build
  title: ''
  type: Libraries
  url: https://agify.io/libraries
- group: other
  title: ''
  type: DataCoverage
  url: https://agify.io/our-data
- group: other
  title: ''
  type: CaseStudies
  url: https://agify.io/case-studies
created: '2026-06-13'
description: Agify.io is a free REST API that predicts the age of a person based on their first name using statistical data from over one billion records spanning 195+ countries. The service is provided by Demografix ApS and shares a single API key with the companion Genderize.io and Nationalize.io APIs. The free tier allows 2,500 name lookups per month with no credit card required; paid plans scale up to 250,000+ names per month. Requests support batch processing of up to 10 names and optional country scoping via ISO 3166-1 alpha-2 codes. The API is stateless, cookieless, and GDPR compliant — submitted names are discarded immediately and never stored.
examples:
- key_count: 4
  name: Batch Name Lookup
  slug: batch-name-lookup
- key_count: 4
  name: Name Not Found
  slug: name-not-found
- key_count: 4
  name: Rate Limit Exceeded
  slug: rate-limit-exceeded
- key_count: 4
  name: Single Name Country Scoped
  slug: single-name-country-scoped
- key_count: 4
  name: Single Name Lookup
  slug: single-name-lookup
finops:
- name: Agify Finops
  service_category: ''
  slug: agify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agify.png
json_schemas:
- name: AgePrediction
  property_count: 4
  slug: age-prediction-response
- name: ErrorResponse
  property_count: 1
  slug: error-response
layout: provider
modified: '2026-06-13'
name: Agify.io
nav: Providers
network: true
overview: 'Agify.io publishes 1 API on the [APIs.io](https://apis.io/) network: Age Prediction API. Tagged areas include Age Prediction, Name Analysis, Demographics, Statistical API, and Free API.


  The Agify.io catalog on APIs.io includes 1 Spectral governance ruleset.


  Agify.io''s developer surface includes authentication, documentation, pricing, FAQ, and 10 more developer resources.'
plans:
- name: Agify Plans Pricing
  plan_count: 3
  slug: agify-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 1
  name: Agify Rate Limits
  slug: agify-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Agify.io API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: agify-jsonschema-spectral-rules
score:
  band: developing
  composite: 39.9
  delta: -6.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 59.4
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/agify/refs/heads/main/screenshots/agify-2026-06-20T170124.png
security:
- kind: authentication
  name: Agify Authentication
  slug: agify-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Agify Domain Security
  slug: agify-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: agify
tags:
- Age Prediction
- Name Analysis
- Demographics
- Statistical API
- Free API
website: https://agify.io
---
