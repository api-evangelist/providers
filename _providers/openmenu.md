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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Openmenu Agentic Access
  operation_count: 7
  slug: openmenu-agentic-access
  summary_line: 7 operations
api_count: 6
apis:
- description: The OpenMenu Enhanced API is an enterprise tier powered by DishDNA machine learning, offering analysis_search, analysis, trends, heatmap, menu and menu_items taxonomy searches, and gap_analysis for co
  name: OpenMenu Enhanced API
  slug: enhanced-api
- description: DishDNA machine-learning trends, heatmaps, and gap analysis (Enhanced tier).
  name: OpenMenu Analytics API
  slug: openmenu-analytics-api
- description: Coupons, specials, and daily deals for a restaurant.
  name: OpenMenu Deals API
  slug: openmenu-deals-api
- description: Ingredient database with nutrition labels, claims, and food groups.
  name: OpenMenu Ingredients API
  slug: openmenu-ingredients-api
- description: Full restaurant profiles and geographic listings.
  name: OpenMenu Restaurants API
  slug: openmenu-restaurants-api
- description: Find restaurants, menu items, and sample menus by location and term.
  name: OpenMenu Search API
  slug: openmenu-search-api
artifact_total: 22
collections:
- collection_type: open
  name: OpenMenu API
  slug: open-openmenu
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openmenu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openmenu-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openmenu-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://openmenu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.openmenu.com/api/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://openmenu.com/api/
- group: start
  title: ''
  type: Signup
  url: https://www.openmenu.com/signup.php?at=developer
- group: auth
  title: ''
  type: Authentication
  url: https://www.openmenu.com/api/docs/authentication.php
- group: operate
  title: ''
  type: RateLimits
  url: https://www.openmenu.com/api/docs/rate-limiting.php
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openmenu.com/tos-api.php
created: '2026-06-02'
description: OpenMenu provides structured menu data and menu publishing for restaurants, built on the open OpenMenu Format specification. Its public REST API helps developers locate restaurants, menus, and menu items, returning structured data including names, descriptions, prices, locations, and dietary attributes such as vegan, vegetarian, halal, kosher, and gluten-free. The standard API covers search, restaurant, location, deals, and ingredients endpoints, while an Enhanced enterprise tier adds DishDNA machine-learning analysis, trends, heatmaps, and gap analysis. The API offers a sandbox mode (s=sample / id=sample), API key authentication via the key query parameter, and tiered pricing from a free plan up to enterprise on a daily/monthly credit model.
examples:
- key_count: 2
  name: Openmenu Restaurant Example
  slug: openmenu-restaurant-example
- key_count: 2
  name: Openmenu Search Example
  slug: openmenu-search-example
finops:
- name: Openmenu Finops
  service_category: ''
  slug: openmenu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openmenu.png
json_schemas:
- name: OpenMenu Menu Item
  property_count: 15
  slug: openmenu-menu-item
- name: OpenMenu Menu
  property_count: 9
  slug: openmenu-menu
- name: OpenMenu Restaurant
  property_count: 7
  slug: openmenu-restaurant
json_structures:
- name: Openmenu Menu Item Structure
  property_count: 12
  slug: openmenu-menu-item-structure
jsonld:
- class_count: 30
  name: Openmenu Context
  property_count: 7
  slug: openmenu-context
layout: provider
modified: '2026-06-03'
name: OpenMenu
nav: Providers
network: true
overview: 'OpenMenu publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Deals API, Ingredients API, and 2 more. Tagged areas include Restaurant, Menus, Menu Data, Search, and Nutrition.


  The OpenMenu catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  OpenMenu''s developer surface includes authentication, documentation, API reference, signup flow, and 6 more developer resources.'
plans:
- name: Openmenu Plans Pricing
  plan_count: 4
  slug: openmenu-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 0
  name: Openmenu Rate Limits
  slug: openmenu-rate-limits
rules:
- name: OpenMenu API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openmenu-jsonschema-spectral-rules
- name: OpenMenu API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: openmenu-rules
score:
  band: developing
  composite: 50.7
  delta: 1.9
  facets:
    commercial_clarity: 63.2
    contract_quality: 73.9
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openmenu/refs/heads/main/screenshots/openmenu-2026-06-20T191015.png
security:
- kind: authentication
  name: Openmenu Authentication
  slug: openmenu-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Openmenu Domain Security
  slug: openmenu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: openmenu
tags:
- Restaurant
- Menus
- Menu Data
- Search
- Nutrition
- Structured Data
website: https://openmenu.com/
---
