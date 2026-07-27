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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Vehicle Api Agentic Access
  operation_count: 7
  slug: vehicle-api-agentic-access
  summary_line: 7 operations
api_count: 7
apis:
- description: Dealer vehicle inventory
  name: Vehicle API Inventory API
  slug: vehicle-api-inventory-api
- description: Vehicle manufacturer make data
  name: Vehicle API Makes API
  slug: vehicle-api-makes-api
- description: Vehicle photos and videos
  name: Vehicle API Media API
  slug: vehicle-api-media-api
- description: Vehicle model information
  name: Vehicle API Models API
  slug: vehicle-api-models-api
- description: True Market Value pricing data
  name: Vehicle API Pricing API
  slug: vehicle-api-pricing-api
- description: Vehicle technical specifications
  name: Vehicle API Specs API
  slug: vehicle-api-specs-api
- description: Vehicle trim and style configurations
  name: Vehicle API Styles API
  slug: vehicle-api-styles-api
artifact_total: 53
collections:
- collection_type: open
  name: Vehicle API (Edmunds)
  slug: open-vehicle-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vehicle-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vehicle-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vehicle-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://developer.edmunds.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.edmunds.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.edmunds.com/api-documentation/vehicle/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.edmunds.com/api-documentation/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.edmunds.com/api-documentation/overview/
- group: operate
  title: ''
  type: Support
  url: https://developer.edmunds.com/support/
- group: design
  title: Vehicle API Spectral Rules
  type: SpectralRules
  url: rules/vehicle-api-spectral-rules.yml
- group: design
  title: Vehicle API Vocabulary
  type: Vocabulary
  url: vocabulary/vehicle-api-vocabulary.yml
created: '2025-01-07'
description: The Vehicle API by Edmunds provides comprehensive access to automotive datasets covering vehicle makes, models, trims, specs, media, pricing (TMV), incentives, dealer information, and reviews. Enables developers to build automotive shopping tools, vehicle configurators, and consumer research applications.
examples:
- key_count: 12
  name: Vehicle Api Inventory Item Example
  slug: vehicle-api-inventory-item-example
- key_count: 4
  name: Vehicle Api Make Example
  slug: vehicle-api-make-example
- key_count: 5
  name: Vehicle Api Model Example
  slug: vehicle-api-model-example
- key_count: 4
  name: Vehicle Api Model Year Example
  slug: vehicle-api-model-year-example
- key_count: 5
  name: Vehicle Api Photo Example
  slug: vehicle-api-photo-example
- key_count: 3
  name: Vehicle Api Price Response Example
  slug: vehicle-api-price-response-example
- key_count: 8
  name: Vehicle Api Style Example
  slug: vehicle-api-style-example
- key_count: 4
  name: Vehicle Api Style Price Example
  slug: vehicle-api-style-price-example
features:
- description: Comprehensive database of vehicle makes, models, and trim levels with OEM specifications, features, and configuration options.
  name: Vehicle Make and Model Data
- description: Edmunds TMV pricing data including new vehicle suggested retail, invoice prices, and used vehicle values by condition and mileage.
  name: True Market Value Pricing
- description: Photo and video assets for vehicle makes, models, and trims including exterior, interior, color swatch, and 360-degree images.
  name: Vehicle Media
- description: Real-time dealer inventory search with make, model, year, zip code, radius, and price range filtering.
  name: Dealer Inventory
- description: Manufacturer incentives, rebates, financing offers, and lease programs by vehicle, region, and customer type.
  name: Incentives and Rebates
- description: Edmunds editorial reviews and consumer ratings for vehicle models including performance, comfort, value, and reliability scores.
  name: Vehicle Reviews and Ratings
finops:
- name: Vehicle Api Finops
  service_category: API
  slug: vehicle-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vehicle-api.png
integrations:
- description: Cross-reference vehicle listings with AutoTrader inventory using Edmunds vehicle identifiers and specs for consistent data.
  name: AutoTrader
- description: Combine Edmunds vehicle data with Cars.com listings for enriched consumer shopping experiences.
  name: Cars.com
- description: Integrate vehicle specs and pricing into Salesforce, CDK, and Reynolds and Reynolds dealer management systems.
  name: Dealer CRM Systems
json_schemas:
- name: InventoryItem
  property_count: 12
  slug: vehicle-api-inventory-item
- name: Make
  property_count: 4
  slug: vehicle-api-make
- name: Model
  property_count: 5
  slug: vehicle-api-model
- name: ModelYear
  property_count: 4
  slug: vehicle-api-model-year
- name: Photo
  property_count: 5
  slug: vehicle-api-photo
- name: PriceResponse
  property_count: 3
  slug: vehicle-api-price-response
- name: StylePrice
  property_count: 4
  slug: vehicle-api-style-price
- name: Style
  property_count: 8
  slug: vehicle-api-style
json_structures:
- name: Vehicle Api Inventory Item Structure
  property_count: 12
  slug: vehicle-api-inventory-item-structure
- name: Vehicle Api Make Structure
  property_count: 4
  slug: vehicle-api-make-structure
- name: Vehicle Api Model Structure
  property_count: 5
  slug: vehicle-api-model-structure
- name: Vehicle Api Model Year Structure
  property_count: 4
  slug: vehicle-api-model-year-structure
- name: Vehicle Api Photo Structure
  property_count: 5
  slug: vehicle-api-photo-structure
- name: Vehicle Api Price Response Structure
  property_count: 3
  slug: vehicle-api-price-response-structure
- name: Vehicle Api Style Price Structure
  property_count: 4
  slug: vehicle-api-style-price-structure
- name: Vehicle Api Style Structure
  property_count: 8
  slug: vehicle-api-style-structure
layout: provider
modified: '2026-05-19'
name: Vehicle API
nav: Providers
network: true
overview: 'Vehicle API publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Inventory API, Makes API, Media API, and 4 more. Tagged areas include Automotive, Cars, Edmunds, Pricing, and Vehicles.


  The Vehicle API catalog on APIs.io includes 2 Spectral governance rulesets.


  Vehicle API''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, and 6 more developer resources.'
plans:
- name: Vehicle Api Plans Pricing
  plan_count: 3
  slug: vehicle-api-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Vehicle Api Rate Limits
  slug: vehicle-api-rate-limits
rules:
- name: Vehicle API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vehicle-api-jsonschema-spectral-rules
- name: Vehicle API API Rules
  rule_count: 30
  severity_counts:
    error: 11
    hint: 0
    info: 5
    warn: 14
  slug: vehicle-api-spectral-rules
score:
  band: developing
  composite: 58.0
  delta: 4.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 72.6
    developer_ergonomics: 43.5
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 31.6
  previous_composite: 53.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vehicle-api/refs/heads/main/screenshots/vehicle-api-2026-06-20T200854.png
security:
- kind: authentication
  name: Vehicle Api Authentication
  slug: vehicle-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vehicle Api Domain Security
  slug: vehicle-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vehicle-api
tags:
- Automotive
- Cars
- Edmunds
- Pricing
- Vehicles
use_cases:
- description: Build vehicle search and comparison tools that let consumers filter by make, model, year, price, and features with TMV pricing guidance.
  name: Automotive Shopping Tools
- description: Power dealer websites and CRM systems with accurate vehicle specs, pricing, and inventory data synced from Edmunds.
  name: Dealer Management Systems
- description: Enable consumers to build and price vehicles with available trims, packages, options, and colors with live pricing calculations.
  name: Vehicle Configurator
- description: Integrate used vehicle pricing into trade-in calculators, appraisal tools, and consumer value estimators using TMV data.
  name: Used Car Valuation
website: https://developer.edmunds.com/
---
