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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Fooddata Agentic Access
  operation_count: 9
  slug: fooddata-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- description: endpoints to retrieve nutrient data
  name: FoodData Central FDC API
  slug: fooddata-fdc-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fooddata-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fooddata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fooddata-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://fdc.nal.usda.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://fdc.nal.usda.gov/api-guide
- group: start
  title: ''
  type: Portal
  url: https://fdc.nal.usda.gov/
- group: start
  title: ''
  type: Signup
  url: https://fdc.nal.usda.gov/api-key-signup
- group: company
  title: ''
  type: About
  url: https://fdc.nal.usda.gov/about-us
- group: operate
  title: ''
  type: Contact
  url: https://fdc.nal.usda.gov/contact
- group: operate
  title: ''
  type: FAQ
  url: https://fdc.nal.usda.gov/faq
- group: other
  title: ''
  type: DataDownload
  url: https://fdc.nal.usda.gov/download-datasets
- group: operate
  title: ''
  type: ChangeLog
  url: https://fdc.nal.usda.gov/log
- group: other
  title: ''
  type: X
  url: https://twitter.com/usda_ars
- group: commercial
  title: ''
  type: Plans
  url: plans/fooddata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fooddata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fooddata-finops.yml
created: '2026-06-13'
description: USDA FoodData Central is a comprehensive food composition database and REST API providing nutritional data for over 600,000 foods. The service covers multiple distinct data types including Foundation Foods, SR Legacy, Survey Foods (FNDDS), Branded Foods, and Experimental Foods. All data is released under CC0 1.0 Universal (public domain) and the API is free to use with a data.gov API key. FoodData Central is operated by the USDA Agricultural Research Service (ARS) and receives twice-annual updates for Foundation Foods and monthly updates for Branded Foods.
examples:
- key_count: 4
  name: Get Food By Fdc Id
  slug: get-food-by-fdc-id
- key_count: 4
  name: Get Foods Batch
  slug: get-foods-batch
- key_count: 4
  name: Search Foods
  slug: search-foods
finops:
- name: Fooddata Finops
  service_category: ''
  slug: fooddata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fooddata.png
json_schemas:
- name: FoodItem
  property_count: 0
  slug: food-item
- name: FoodSearchCriteria
  property_count: 7
  slug: search-criteria
- name: SearchResult
  property_count: 5
  slug: search-result
jsonld:
- class_count: 14
  name: Fooddata Context
  property_count: 39
  slug: fooddata-context
layout: provider
modified: '2026-06-13'
name: FoodData Central
nav: Providers
network: true
overview: 'FoodData Central publishes 1 API on the [APIs.io](https://apis.io/) network: FDC API. Tagged areas include Food, Nutrition, USDA, Government, and Health.


  The FoodData Central catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FoodData Central''s developer surface includes authentication, documentation, developer portal, signup flow, FAQ, changelog, and 10 more developer resources.'
plans:
- name: Fooddata Plans Pricing
  plan_count: 3
  slug: fooddata-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 6
  name: Fooddata Rate Limits
  slug: fooddata-rate-limits
rules:
- name: FoodData Central API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: fooddata-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.6
    developer_ergonomics: 28.3
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 47.4
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fooddata/refs/heads/main/screenshots/fooddata-2026-06-20T181400.png
security:
- kind: authentication
  name: Fooddata Authentication
  slug: fooddata-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fooddata Domain Security
  slug: fooddata-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: fooddata
tags:
- Food
- Nutrition
- USDA
- Government
- Health
- Diet
- Nutrients
- Public Domain
website: https://fdc.nal.usda.gov/
---
