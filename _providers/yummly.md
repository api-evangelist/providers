---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: 'DEPRECATED / HISTORICAL. The Search Recipes endpoint (GET http://api.yummly.com/v1/api/recipes) returned recipe matches as JSON with optional filters combined via AND - free-text query (q), maxResult '
  name: Yummly Recipe Search API (Historical)
  slug: yummly-recipe-search-api
- description: DEPRECATED / HISTORICAL. The Get Recipe endpoint (GET http://api.yummly.com/v1/api/recipe/{recipe-id}) returned the full detail for a single recipe by its Yummly recipe id - ingredient lines, nutritio
  name: Yummly Recipe Details API (Historical)
  slug: yummly-recipe-details-api
- description: DEPRECATED / HISTORICAL. The Metadata endpoints (GET http://api.yummly.com/v1/api/metadata/{key}) returned the controlled vocabularies used to build search filters - keys included ingredient, allergy,
  name: Yummly Metadata API (Historical)
  slug: yummly-metadata-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yummly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.yummly.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yummly
- group: docs
  title: ''
  type: Documentation
  url: https://developer.yummly.com/documentation.html
- group: commercial
  title: ''
  type: Plans
  url: plans/yummly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yummly-rate-limits.yml
created: '2026-07-03'
description: Yummly is a recipe and food discovery platform (yummly.com) offering semantic and visual recipe search, personalized recommendations, shopping lists, and guided cooking. Founded in 2009 (Redwood City, CA), Yummly was acquired by Whirlpool Corporation in May 2017 and operated as a wholly owned subsidiary tied to Whirlpool's smart-kitchen strategy. Yummly historically ran a well-known public Recipe API (developer.yummly.com) exposing recipe search, recipe details, and metadata endpoints. That developer program was DEPRECATED - it stopped accepting new signups and was wound down (commonly cited end date of September 30, 2019), and the developer.yummly.com developer portal and api.yummly.com endpoints are no longer available. There is no public Yummly developer API accepting new registrations as of this cataloging (2026-07-03); the APIs below are documented as historical / modeled for archival and migration reference only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yummly.png
layout: provider
modified: '2026-07-03'
name: Yummly
nav: Providers
network: true
overview: 'Yummly publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Recipes, Food, Cooking, Recipe Search, and Food Discovery.


  Yummly''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Yummly Plans Pricing
  plan_count: 4
  slug: yummly-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 4
  name: Yummly Rate Limits
  slug: yummly-rate-limits
score:
  band: emerging
  composite: 19.6
  delta: -2.6
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 22.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Yummly Domain Security
  slug: yummly-domain-security
  summary_line: TLSv1.2
slug: yummly
tags:
- Recipes
- Food
- Cooking
- Recipe Search
- Food Discovery
- Deprecated
- Historical
website: https://www.yummly.com
---
