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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Zestful Agentic Access
  operation_count: 1
  slug: zestful-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://zestfuldata.com
  baseurl_source: declared
  description: Ingredient parsing operations
  name: Zestful Parse API
  slug: zestful-parse-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zestful Parse API
  slug: open-zestful-parse-api
- collection_type: open
  name: Zestful
  slug: open-zestful
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zestful-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zestful-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zestful-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zestful
- group: company
  title: ''
  type: Website
  url: https://zestfuldata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://zestfuldata.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://zestfuldata.com/pricing/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mtlynch/zestful-client
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/zestful-vocabulary.yml
created: '2024-11-14'
description: Zestful provides a machine-learning-powered ingredient parser API that turns plain recipe ingredient strings into structured JSON data. The API extracts quantity, unit, product name, preparation notes, and USDA FoodData Central database matches from free-form recipe text. Designed for recipe app developers building searchable recipes, shopping lists, and ingredient databases.
examples:
- key_count: 2
  name: Zestful Parse Ingredients Example
  slug: zestful-parse-ingredients-example
finops:
- name: Zestful Finops
  service_category: API
  slug: zestful-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zestful.png
json_schemas:
- name: Zestful Parsed Ingredient
  property_count: 4
  slug: zestful-ingredient
- name: Zestful Parse Ingredients Response
  property_count: 3
  slug: zestful-parse-response
json_structures:
- name: Zestful Ingredient Structure
  property_count: 0
  slug: zestful-ingredient-structure
jsonld:
- class_count: 0
  name: Zestful Context
  property_count: 15
  slug: zestful-context
layout: provider
modified: '2026-05-19'
name: Zestful
nav: Providers
network: true
overview: 'Zestful publishes 1 API on the [APIs.io](https://apis.io/) network: Parse API. Tagged areas include Food, Ingredients, Parsers, Recipes, and USDA.


  The Zestful catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Zestful''s developer surface includes authentication, documentation, pricing, and 6 more developer resources.'
plans:
- name: Zestful Plans Pricing
  plan_count: 3
  slug: zestful-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Zestful Rate Limits
  slug: zestful-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Zestful API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: zestful-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Zestful API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: zestful-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 73.5
    catalog_earned_first_party: 0.0
    catalog_gap: 41.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 69.4
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zestful/refs/heads/main/screenshots/zestful-2026-06-20T201840.png
security:
- kind: authentication
  name: Zestful Authentication
  slug: zestful-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zestful Domain Security
  slug: zestful-domain-security
  summary_line: TLSv1.3 · HSTS
slug: zestful
tags:
- Food
- Ingredients
- Parsers
- Recipes
- USDA
website: https://zestfuldata.com/
---
