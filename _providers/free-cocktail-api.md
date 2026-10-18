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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Free Cocktail Api Agentic Access
  operation_count: 5
  slug: free-cocktail-api-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://www.thecocktaildb.com/api/json/v1
  baseurl_source: declared
  description: Filter cocktails by ingredient, alcohol, category, or glass.
  name: Free Cocktail API Filter API
  slug: free-cocktail-api-filter-api
- baseURL: https://www.thecocktaildb.com/api/json/v1
  baseurl_source: declared
  description: List available categories, glasses, ingredients, and alcohol filters.
  name: Free Cocktail API List API
  slug: free-cocktail-api-list-api
- baseURL: https://www.thecocktaildb.com/api/json/v1
  baseurl_source: declared
  description: Look up full details by ID.
  name: Free Cocktail API Lookup API
  slug: free-cocktail-api-lookup-api
- baseURL: https://www.thecocktaildb.com/api/json/v1
  baseurl_source: declared
  description: Fetch random cocktails.
  name: Free Cocktail API Random API
  slug: free-cocktail-api-random-api
- baseURL: https://www.thecocktaildb.com/api/json/v1
  baseurl_source: declared
  description: Search cocktails and ingredients.
  name: Free Cocktail API Search API
  slug: free-cocktail-api-search-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Free Cocktail Filter API
  slug: open-free-cocktail-api-filter-api
- collection_type: open
  name: Free Cocktail Filter List API
  slug: open-free-cocktail-api-list-api
- collection_type: open
  name: Free Cocktail Filter Lookup API
  slug: open-free-cocktail-api-lookup-api
- collection_type: open
  name: Free Cocktail Filter Random API
  slug: open-free-cocktail-api-random-api
- collection_type: open
  name: Free Cocktail Filter Search API
  slug: open-free-cocktail-api-search-api
- collection_type: open
  name: Free Cocktail API
  slug: open-free-cocktail-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/free-cocktail-api/refs/heads/main/plans/free-cocktail-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/free-cocktail-api-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/free-cocktail-api/refs/heads/main/rate-limits/free-cocktail-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/free-cocktail-api-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/free-cocktail-api/refs/heads/main/finops/free-cocktail-api-finops.yml
  title: ''
  type: FinOps
  url: finops/free-cocktail-api-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/free-cocktail-api/refs/heads/main/agentic-access/free-cocktail-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/free-cocktail-api-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/free-cocktail-api/refs/heads/main/security/free-cocktail-api-domain-security.yml
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
- has_sources: false
  method: generated
  name: Free Cocktail Api Finops
  primary_unit: ''
  service_category: API
  slug: free-cocktail-api-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/free-cocktail-api.png
layout: provider
modified: '2026-05-19'
name: Free Cocktail API
nav: Providers
network: true
overview: 'Free Cocktail API publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Filter API, List API, Lookup API, and 2 more. Tagged areas include Beverages, Cocktails, Drinks, Ingredients, and Recipes.


  Free Cocktail API''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Free Cocktail Api Plans Pricing
  plan_count: 3
  slug: free-cocktail-api-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Free Cocktail Api Rate Limits
  slug: free-cocktail-api-rate-limits
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 44.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 18.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
