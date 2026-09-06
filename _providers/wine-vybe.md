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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: 'The Wine Vybe Wine API provides access to thousands of wines with data including wine regions, grape varieties, tasting notes, food pairing recommendations, awards, producer details, and custom taste '
  name: Wine Vybe Wine API
  slug: wine-vybe-api
- description: The Wine Vybe Beer API provides access to brewery details, ABV data, beer descriptions, food pairing recommendations, awards, packaging specifications, and tasting profiles for thousands of popular be
  name: Wine Vybe Beer API
  slug: wine-vybe-beer-api
- description: The Wine Vybe Liquor API provides access to spirits and liquor data including distillery information, tasting notes, food pairing, and product details for whisky, cognac, tequila, vodka, rum, gin, bra
  name: Wine Vybe Liquor API
  slug: wine-vybe-liquor-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wine-vybe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://winevybe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://winevybe.com/wine-api/
- group: docs
  title: ''
  type: Documentation
  url: https://winevybe.com/beer-api/
- group: start
  title: ''
  type: Portal
  url: https://winevybe.com/apis/
- group: other
  title: ''
  type: RapidAPI
  url: https://rapidapi.com/user/winevybe
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/wine-vybe/refs/heads/main/json-ld/wine-vybe-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/wine-vybe/refs/heads/main/vocabulary/wine-vybe-vocabulary.yml
created: '2026-03-16'
description: Wine Vybe is a wine, beer, and liquor database API platform that provides access to comprehensive beverage data including wine regions, grape varieties, tasting notes, food pairing recommendations, awards, producer information, brewery and distillery details, and custom taste profiles. The platform serves app developers and businesses through RESTful APIs hosted on RapidAPI.
examples:
- key_count: 13
  name: Wine Vybe Beer Example
  slug: wine-vybe-beer-example
- key_count: 15
  name: Wine Vybe Wine Example
  slug: wine-vybe-wine-example
finops:
- name: Wine Vybe Finops
  service_category: API
  slug: wine-vybe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wine-vybe.png
json_schemas:
- name: Beer
  property_count: 13
  slug: wine-vybe-beer
- name: Wine
  property_count: 15
  slug: wine-vybe-wine
json_structures:
- name: Wine Vybe Beer Structure
  property_count: 0
  slug: wine-vybe-beer-structure
- name: Wine Vybe Wine Structure
  property_count: 0
  slug: wine-vybe-wine-structure
jsonld:
- class_count: 24
  name: Wine Vybe Context
  property_count: 0
  slug: wine-vybe-context
layout: provider
modified: '2026-05-03'
name: Wine Vybe
nav: Providers
network: true
overview: 'Wine Vybe publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Beverages, Beer, Database, Food Pairing, and Liquor.


  The Wine Vybe catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wine Vybe''s developer surface includes documentation, developer portal, and 6 more developer resources.'
plans:
- name: Wine Vybe Plans Pricing
  plan_count: 3
  slug: wine-vybe-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Wine Vybe Rate Limits
  slug: wine-vybe-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Wine Vybe API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wine-vybe-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 71.3
    catalog_earned_first_party: 0.0
    catalog_gap: 43.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 25.3
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 24.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wine-vybe/refs/heads/main/screenshots/wine-vybe-2026-06-20T201513.png
security:
- kind: domain-security
  name: Wine Vybe Domain Security
  slug: wine-vybe-domain-security
  summary_line: TLSv1.3 · HSTS
slug: wine-vybe
tags:
- Beverages
- Beer
- Database
- Food Pairing
- Liquor
- Recommendations
- Wine
website: https://winevybe.com/
---
