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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 35.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nationalize Agentic Access
  operation_count: 1
  slug: nationalize-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Operations for predicting nationality from names
  name: Nationalize.io Nationality API
  slug: nationalize-nationality-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nationalize.io Nationality API
  slug: open-nationalize-nationality-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nationalize-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nationalize-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nationalize-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://nationalize.io
- group: docs
  title: ''
  type: Documentation
  url: https://nationalize.io/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://nationalize.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/nationalize/refs/heads/main/plans/nationalize-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/nationalize/refs/heads/main/rate-limits/nationalize-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/nationalize/refs/heads/main/finops/nationalize-finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nationalize.io/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nationalize.io/legal/privacy-policy
- group: operate
  title: ''
  type: FAQ
  url: https://nationalize.io/faq
- group: start
  title: ''
  type: Login
  url: https://nationalize.io/login
- group: start
  title: ''
  type: Signup
  url: https://nationalize.io/register
created: '2026-06-13'
description: Free REST API that predicts the nationality of a person based on their first name using probabilistic models derived from a dataset of approximately one billion people spanning 250 countries and territories. Accepts single or batched names, handles diacritics and non-Latin alphabets, and returns ranked country probabilities as JSON. The same API key works across all three Demografix services (Genderize, Agify, Nationalize).
examples:
- key_count: 3
  name: Batch Name Lookup
  slug: batch-name-lookup
- key_count: 3
  name: Name Not Found
  slug: name-not-found
- key_count: 3
  name: Single Name Lookup
  slug: single-name-lookup
finops:
- name: Nationalize Finops
  service_category: ''
  slug: nationalize-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nationalize.png
json_schemas:
- name: NationalityResult
  property_count: 3
  slug: nationalize-result
jsonld:
- class_count: 2
  name: Nationalize Context
  property_count: 5
  slug: nationalize-context
layout: provider
modified: '2026-06-13'
name: Nationalize.io
nav: Providers
network: true
overview: 'Nationalize.io publishes 1 API on the [APIs.io](https://apis.io/) network: Nationality API. Tagged areas include Nationality, Name Prediction, Demographics, Probabilistic Models, and People.


  The Nationalize.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nationalize.io''s developer surface includes authentication, documentation, pricing, FAQ, signup flow, and 9 more developer resources.'
plans:
- name: Nationalize Plans Pricing
  plan_count: 4
  slug: nationalize-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Nationalize Rate Limits
  slug: nationalize-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Nationalize.io API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: nationalize-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 42.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 9.8
    contract_quality: 59.2
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 31.6
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nationalize/refs/heads/main/screenshots/nationalize-2026-06-20T190047.png
security:
- kind: authentication
  name: Nationalize Authentication
  slug: nationalize-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nationalize Domain Security
  slug: nationalize-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: nationalize
tags:
- Nationality
- Name Prediction
- Demographics
- Probabilistic Models
- People
website: https://nationalize.io
---
