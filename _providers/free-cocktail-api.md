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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Free Cocktail Api Agentic Access
  operation_count: 5
  slug: free-cocktail-api-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: Filter cocktails by ingredient, alcohol, category, or glass.
  name: Free Cocktail API Filter API
  slug: free-cocktail-api-filter-api
- description: List available categories, glasses, ingredients, and alcohol filters.
  name: Free Cocktail API List API
  slug: free-cocktail-api-list-api
- description: Look up full details by ID.
  name: Free Cocktail API Lookup API
  slug: free-cocktail-api-lookup-api
- description: Fetch random cocktails.
  name: Free Cocktail API Random API
  slug: free-cocktail-api-random-api
- description: Search cocktails and ingredients.
  name: Free Cocktail API Search API
  slug: free-cocktail-api-search-api
artifact_total: 11
collections:
- collection_type: open
  name: Free Cocktail API
  slug: open-free-cocktail-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/free-cocktail-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/free-cocktail-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thecocktaildb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.thecocktaildb.com/api.php
created: '2025-01-07'
description: The Free Cocktail API is a resource that provides access to a vast database of cocktail recipes, ingredients, and images.
finops:
- name: Free Cocktail Api Finops
  service_category: API
  slug: free-cocktail-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/free-cocktail-api.png
layout: provider
modified: '2026-05-19'
name: Free Cocktail API
nav: Providers
network: true
overview: 'Free Cocktail API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Filter API, List API, Lookup API, and 2 more. Tagged areas include Beverages, Cocktails, Drinks, Ingredients, and Recipes.


  Free Cocktail API''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Free Cocktail Api Plans Pricing
  plan_count: 3
  slug: free-cocktail-api-plans-pricing
random_paper: 82
rate_limits:
- limit_count: 5
  name: Free Cocktail Api Rate Limits
  slug: free-cocktail-api-rate-limits
score:
  band: thin
  composite: 34.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.7
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/free-cocktail-api/refs/heads/main/screenshots/free-cocktail-api-2026-06-20T181517.png
security:
- kind: domain-security
  name: Free Cocktail Api Domain Security
  slug: free-cocktail-api-domain-security
  summary_line: TLSv1.3
slug: free-cocktail-api
tags:
- Beverages
- Cocktails
- Drinks
- Ingredients
- Recipes
website: https://www.thecocktaildb.com/
---
