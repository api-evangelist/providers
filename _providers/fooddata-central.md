---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Fooddata Central Agentic Access
  operation_count: 9
  slug: fooddata-central-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- description: National Nutrient Database for Standard Reference
  name: FoodData Central
  slug: fooddata-central
- description: endpoints to retrieve nutrient data
  name: FoodData Central FDC API
  slug: fooddata-fdc-api
artifact_total: 17
collections:
- collection_type: open
  name: Food Data Central FDC API
  slug: open-fooddata-central-fdc-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fooddata-central-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fdc.nal.usda.gov/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fooddata-central-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fooddata-central-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fooddata-central-authentication.yml
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
  url: plans/fooddata-central-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fooddata-central-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fooddata-central-finops.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fooddata-central-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fooddata-central-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fooddata-central-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fooddata-central-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fooddata-central-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fooddata-central-finops.yml
created: '2026-05-28'
description: National Nutrient Database for Standard Reference
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
- name: Fooddata Central Finops
  service_category: ''
  slug: fooddata-central-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fooddata-central.png
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
  name: Fooddata Central Context
  property_count: 39
  slug: fooddata-central-context
layout: provider
modified: '2026-05-28'
name: FoodData Central
nav: Providers
network: true
overview: 'FoodData Central publishes 1 API on the [APIs.io](https://apis.io/) network: FDC API. Tagged areas include Health and Public APIs.


  The FoodData Central catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FoodData Central''s developer surface includes authentication, documentation, developer portal, signup flow, FAQ, changelog, and 18 more developer resources.'
plans:
- name: Fooddata Central Plans Pricing
  plan_count: 3
  slug: fooddata-central-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 6
  name: Fooddata Central Rate Limits
  slug: fooddata-central-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: FoodData Central API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: fooddata-central-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 46.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 9.8
    contract_quality: 60.5
    developer_ergonomics: 31.0
    discoverability: 57.4
    governance: 9.8
    operational_transparency: 47.4
  previous_composite: 45.3
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fooddata-central/refs/heads/main/screenshots/fooddata-central-2026-06-20T181402.png
security:
- kind: authentication
  name: Fooddata Central Authentication
  slug: fooddata-central-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fooddata Central Domain Security
  slug: fooddata-central-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: fooddata-central
tags:
- Health
- Public APIs
website: https://fdc.nal.usda.gov/
---
