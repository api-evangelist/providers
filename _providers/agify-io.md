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
    agentic_commerce: false
    auth_clarity: false
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
  score: 32.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agify Io Agentic Access
  operation_count: 1
  slug: agify-io-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- description: Predict the age of a person based on their first name. Returns an estimated age, data count used for the prediction, and optionally a country-localized estimate. Supports single name and batch request
  name: Agify.io Predict Age API
  slug: predict-age-api
- description: Predict a person's age from their first name
  name: Agify.io Age Prediction API
  slug: agify-io-age-prediction-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Agify.io Age Prediction API
  slug: open-agify-io-age-prediction-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agify-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agify-io-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://agify.io/
- group: docs
  title: ''
  type: Documentation
  url: https://agify.io/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://agify.io/#pricing
- group: operate
  title: ''
  type: RateLimits
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://agify.io/llms.txt
created: '2025-01-07'
description: Agify.io is a simple REST API that predicts the age of a person based on their first name. Using a large dataset of name-age associations, it returns an estimated age along with a count of how many data points were used and the name's country-localized variant when a country code is provided. Supports batch requests for up to 10 names per call. Used for demographics research, content personalization, and marketing segmentation.
examples:
- key_count: 4
  name: Agify Io Age Prediction Example
  slug: agify-io-age-prediction-example
features:
- description: Estimates a person's age from their first name using a large statistical dataset of name-age associations.
  name: Name-Based Age Prediction
- description: Accepts an optional ISO 3166-1 country code to return country-specific age predictions for the given name.
  name: Country Localization
- description: Supports up to 10 names per API request using array parameter syntax for efficient bulk predictions.
  name: Batch Processing
- description: Returns X-Rate-Limit-Limit, X-Rate-Limit-Remaining, and X-Rate-Limit-Reset headers to track API usage and quota.
  name: Rate Limit Headers
- description: Free access for up to 100 requests per day without an API key, making it easy to evaluate the service.
  name: Free Tier
finops:
- name: Agify Io Finops
  service_category: API
  slug: agify-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agify-io.png
integrations:
- description: Sibling API that predicts gender based on first name — commonly used alongside Agify for demographic profiling.
  name: Genderize.io
- description: Sibling API that predicts nationality from first name, completing a demographic analysis trifecta with Agify and Genderize.
  name: Nationalize.io
json_schemas:
- name: AgePrediction
  property_count: 4
  slug: agify-io-age-prediction
json_structures:
- name: Agify Io Age Prediction Structure
  property_count: 4
  slug: agify-io-age-prediction-structure
jsonld:
- class_count: 2
  name: Agify Io Context
  property_count: 3
  slug: agify-io-context
layout: provider
modified: '2026-05-19'
name: Agify.io
nav: Providers
network: true
overview: 'Agify.io publishes 1 API on the [APIs.io](https://apis.io/) network: Age Prediction API. Tagged areas include Age Prediction, Name Analysis, Demographics, and REST API.


  The Agify.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agify.io''s developer surface includes developer portal, documentation, pricing, and 3 more developer resources.'
plans:
- name: Agify Io Plans Pricing
  plan_count: 3
  slug: agify-io-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Agify Io Rate Limits
  slug: agify-io-rate-limits
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
  slug: agify-io-jsonschema-spectral-rules
score:
  band: emerging
  composite: 22.0
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 16.2
    developer_ergonomics: 19.0
    discoverability: 66.7
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 22.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agify-io/refs/heads/main/screenshots/agify-io-2026-06-20T170134.png
security:
- kind: domain-security
  name: Agify Io Domain Security
  slug: agify-io-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: agify-io
tags:
- Age Prediction
- Name Analysis
- Demographics
- REST API
use_cases:
- description: Analyze name datasets to estimate age distributions across a user base for research and analytics purposes.
  name: Demographics Research
- description: Tailor content or product recommendations based on estimated age derived from a user's provided first name.
  name: Content Personalization
- description: Segment leads and customers by estimated age group for targeted marketing campaigns without requiring date-of-birth collection.
  name: Marketing Segmentation
- description: Provide age-range hints during user registration to improve form completion rates and data accuracy.
  name: Form Pre-Fill Assistance
website: https://agify.io/
---
