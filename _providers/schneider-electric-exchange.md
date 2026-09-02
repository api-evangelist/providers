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
  scored_at: '2026-09-01'
api_count: 11
apis:
- description: The EcoStruxure IT Expert API provides programmatic access to data center infrastructure management data. It enables integrations to query locations, devices, alarms, sensors, and measurements from th
  name: EcoStruxure IT Expert API
  slug: ecostruxure-it-expert-api
- description: API providing time series data and alarms access for buildings and equipment monitored by EcoStruxure Facility Expert. Enables facility managers and integrators to retrieve energy measurements, equipm
  name: EcoStruxure Facility Expert Data API
  slug: ecostruxure-facility-expert-api
- description: Provides contextualized energy data from EcoStruxure Energy hubs, including consumption metrics, load profiles, and energy optimization data for buildings and industrial sites.
  name: EcoStruxure Energy Contextualized Data API
  slug: ecostruxure-energy-contextualized-data-api
- description: API providing transformer health analytics and monitoring data. Enables integration of transformer assets into enterprise applications, delivering condition monitoring, diagnostics, and predictive mai
  name: EcoStruxure Transformer Expert Data API
  slug: ecostruxure-transformer-expert-api
- description: Provides access to comprehensive technical data for Schneider Electric products from a single source, including product specifications, technical documentation, and ETIM 10.0 classification data.
  name: Partner Product Catalog API
  slug: partner-product-catalog-api
- description: Provides the date when a required quantity of a product can be delivered to a defined address. Queries Schneider Electric's supply chain for delivery lead times by product reference and delivery locat
  name: Partner Product Availability API
  slug: partner-product-availability-api
- description: Provides real-time access to both public list price and personalized net price for Schneider Electric products based on the partner account and standard commercial discounts.
  name: Partner Net Price API
  slug: partner-net-price-api
- description: Provides current order status, shipment schedule, and list of items for orders associated with a registered buying account. Enables distributors to track order fulfillment in real time.
  name: Partner Order Status API
  slug: partner-order-status-api
- description: A read-only service allowing distributors to retrieve quote-lines based on quotes associated with their accounts. Supports the conversion workflow from quote to order in the partner sales process.
  name: Partner Distributor Quote API
  slug: partner-distributor-quote-api
- description: Retrieves public information about installed product warranty start and end dates by providing a product serial number. Supports asset lifecycle management and warranty tracking for field-installed eq
  name: Partner Installed Product API
  slug: partner-installed-product-api
- description: Provides access to product-related digital assets and visualization services including 360-degree image sets and 3D models for Schneider Electric products.
  name: Partner Product Digital Asset API
  slug: partner-digital-asset-api
artifact_total: 22
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/schneider-electric-exchange-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://devportal.exchange.se.com/
- group: company
  title: ''
  type: Website
  url: https://exchange.se.com/develop
- group: start
  title: ''
  type: Partner Portal
  url: https://api-explorer.se.com/en
- group: operate
  title: ''
  type: Community
  url: https://community.se.com/t5/EcoStruxure-IT-Expert-API/tkb-p/ecostruxure-it-expert-api
- group: docs
  title: ''
  type: Documentation
  url: https://exchange.se.com/develop
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/schneider-electric-exchange/
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/schneider-electric-exchange/refs/heads/main/json-structure/schneider-electric-exchange-api-structure.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/schneider-electric-exchange/refs/heads/main/json-ld/schneider-electric-exchange-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/schneider-electric-exchange/refs/heads/main/vocabulary/schneider-electric-exchange-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/schneider-electric-exchange/refs/heads/main/examples/ecostruxure-it-get-devices-example.json
created: '2026-03-16'
description: Schneider Electric Exchange is a developer platform providing APIs for EcoStruxure energy management, building automation, industrial IoT, and commerce partner integrations. The Exchange platform enables partners and developers to build integrations with Schneider Electric products and services. APIs span EcoStruxure data services (IT Expert, Facility Expert, Transformer Expert, Energy Contextualized Data) and Partner Commerce APIs for product catalog, inventory, pricing, orders, quotes, and marketplace integrations. Authentication uses OAuth 2.0 with client credentials for Partner APIs and subscription-based API keys for EcoStruxure data APIs.
examples:
- key_count: 7
  name: Ecostruxure It Get Devices Example
  slug: ecostruxure-it-get-devices-example
- key_count: 7
  name: Partner Get Product Availability Example
  slug: partner-get-product-availability-example
finops:
- name: Schneider Electric Exchange Finops
  service_category: API
  slug: schneider-electric-exchange-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/schneider-electric-exchange.png
json_schemas:
- name: EcoStruxure IT Device
  property_count: 13
  slug: ecostruxure-it-device
- name: Schneider Electric Partner Product
  property_count: 10
  slug: partner-product
json_structures:
- name: Schneider Electric Exchange Api Structure
  property_count: 0
  slug: schneider-electric-exchange-api-structure
jsonld:
- class_count: 32
  name: Schneider Electric Exchange Context
  property_count: 3
  slug: schneider-electric-exchange-context
layout: provider
modified: '2026-05-02'
name: Schneider Electric Exchange
nav: Providers
network: true
overview: 'Schneider Electric Exchange publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Building Automation, Commerce APIs, EcoStruxure, Energy Management, and Industrial IoT.


  The Schneider Electric Exchange catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Schneider Electric Exchange''s developer surface includes developer portal, documentation, code examples, and 8 more developer resources.'
plans:
- name: Schneider Electric Exchange Plans Pricing
  plan_count: 3
  slug: schneider-electric-exchange-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Schneider Electric Exchange Rate Limits
  slug: schneider-electric-exchange-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Schneider Electric Exchange API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: schneider-electric-exchange-jsonschema-spectral-rules
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 48.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 25.3
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 25.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 14.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/schneider-electric-exchange/refs/heads/main/screenshots/schneider-electric-exchange-2026-06-20T193528.png
security:
- kind: domain-security
  name: Schneider Electric Exchange Domain Security
  slug: schneider-electric-exchange-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: schneider-electric-exchange
tags:
- Building Automation
- Commerce APIs
- EcoStruxure
- Energy Management
- Industrial IoT
- Schneider Electric
website: https://exchange.se.com/develop
---
