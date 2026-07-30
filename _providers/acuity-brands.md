---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Acuity Brands Agentic Access
  operation_count: 9
  slug: acuity-brands-agentic-access
  summary_line: 9 operations
api_count: 4
apis:
- description: Product catalog and item details
  name: acuity-brands Catalog API
  slug: acuity-brands-catalog-api
- description: Product inventory and availability
  name: acuity-brands Inventory API
  slug: acuity-brands-inventory-api
- description: Order status and shipment tracking
  name: acuity-brands Orders API
  slug: acuity-brands-orders-api
- description: Web content and product page data
  name: acuity-brands Webpages API
  slug: acuity-brands-webpages-api
artifact_total: 44
collections:
- collection_type: open
  name: Acuity Brands API
  slug: open-acuity-brands
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/acuity-brands-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acuity-brands-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acuity-brands-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acuitybrands
- group: company
  title: ''
  type: Website
  url: https://www.acuity-brands.com
- group: start
  title: ''
  type: Portal
  url: https://api-docs.acuitybrands.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.acuitybrands.com/docs/intro/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acuitybrands
- group: design
  title: ''
  type: SpectralRules
  url: rules/acuity-brands-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/acuity-brands-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/acuity-brands-context.jsonld
description: Acuity Brands is a provider of lighting, lighting controls, building management systems, and location-aware applications for commercial, industrial, institutional, and residential markets.
examples:
- key_count: 12
  name: Acuity Brands Catalog Item Example
  slug: acuity-brands-catalog-item-example
- key_count: 3
  name: Acuity Brands Catalog Item List Example
  slug: acuity-brands-catalog-item-list-example
- key_count: 6
  name: Acuity Brands Inventory Item Example
  slug: acuity-brands-inventory-item-example
- key_count: 3
  name: Acuity Brands Inventory List Example
  slug: acuity-brands-inventory-list-example
- key_count: 9
  name: Acuity Brands Order Example
  slug: acuity-brands-order-example
- key_count: 3
  name: Acuity Brands Order List Example
  slug: acuity-brands-order-list-example
- key_count: 9
  name: Acuity Brands Shipment Example
  slug: acuity-brands-shipment-example
- key_count: 2
  name: Acuity Brands Shipment List Example
  slug: acuity-brands-shipment-list-example
- key_count: 8
  name: Acuity Brands Webpage Example
  slug: acuity-brands-webpage-example
- key_count: 3
  name: Acuity Brands Webpage List Example
  slug: acuity-brands-webpage-list-example
finops:
- name: Acuity Brands Finops
  service_category: Lighting / Building Controls
  slug: acuity-brands-finops
image: /assets/icons/acuity-brands.png
json_schemas:
- name: CatalogItemList
  property_count: 3
  slug: acuity-brands-catalog-item-list
- name: CatalogItem
  property_count: 12
  slug: acuity-brands-catalog-item
- name: InventoryItem
  property_count: 6
  slug: acuity-brands-inventory-item
- name: InventoryList
  property_count: 3
  slug: acuity-brands-inventory-list
- name: OrderList
  property_count: 3
  slug: acuity-brands-order-list
- name: Order
  property_count: 9
  slug: acuity-brands-order
- name: ShipmentList
  property_count: 2
  slug: acuity-brands-shipment-list
- name: Shipment
  property_count: 9
  slug: acuity-brands-shipment
- name: WebpageList
  property_count: 3
  slug: acuity-brands-webpage-list
- name: Webpage
  property_count: 8
  slug: acuity-brands-webpage
json_structures:
- name: Acuity Brands Catalog Item List Structure
  property_count: 3
  slug: acuity-brands-catalog-item-list-structure
- name: Acuity Brands Catalog Item Structure
  property_count: 12
  slug: acuity-brands-catalog-item-structure
- name: Acuity Brands Inventory Item Structure
  property_count: 6
  slug: acuity-brands-inventory-item-structure
- name: Acuity Brands Inventory List Structure
  property_count: 3
  slug: acuity-brands-inventory-list-structure
- name: Acuity Brands Order List Structure
  property_count: 3
  slug: acuity-brands-order-list-structure
- name: Acuity Brands Order Structure
  property_count: 9
  slug: acuity-brands-order-structure
- name: Acuity Brands Shipment List Structure
  property_count: 2
  slug: acuity-brands-shipment-list-structure
- name: Acuity Brands Shipment Structure
  property_count: 9
  slug: acuity-brands-shipment-structure
- name: Acuity Brands Webpage List Structure
  property_count: 3
  slug: acuity-brands-webpage-list-structure
- name: Acuity Brands Webpage Structure
  property_count: 8
  slug: acuity-brands-webpage-structure
jsonld:
- class_count: 50
  name: Acuity Brands Context
  property_count: 7
  slug: acuity-brands-context
layout: provider
modified: '2026-05-19'
name: acuity-brands
nav: Providers
network: true
overview: 'acuity-brands publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Inventory API, Orders API, and 1 more. Tagged areas include Fortune 1000.


  The acuity-brands catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  acuity-brands'' developer surface includes authentication, developer portal, documentation, and 8 more developer resources.'
plans:
- name: Acuity Brands Plans Pricing
  plan_count: 1
  slug: acuity-brands-plans-pricing
press:
- date: '2026-05-25'
  title: Distech Controls Collaborates with École de Technologie ...
  url: https://insights.acuitybrands.com/news-releases-blog/distech-controls-collaborates-with-%C3%A9cole-de-technologie-sup%C3%A9rieure-to-develop-machine-learning-solutions-in-connected-buildings
- date: '2026-05-25'
  title: Acuity Brands Names Peter Han President of Intelligent ...
  url: https://www.investors.acuitybrands.com/news-releases/news-release-details/acuity-brands-names-peter-han-president-intelligent-spaces-group
- date: '2026-05-25'
  title: Acuity Brands Names Peter Han President of Intelligent ...
  url: https://www.nasdaq.com/press-release/acuity-brands-names-peter-han-president-of-intelligent-spaces-group-isg-and-acquires
- date: '2026-05-25'
  title: Acuity Brands Snaps Up AI Accelerator Rockpile Ventures
  url: https://www.mdm.com/news/mergers-acquisitions/acuity-buys-rockpile/
- date: '2026-05-25'
  title: 6 Nuanced Takeaways from Acuity's Boldest Year Yet
  url: https://inside.lighting/news/25-10/6-nuanced-takeaways-acuitys-boldest-year-yet
random_paper: 22
rate_limits:
- limit_count: 0
  name: Acuity Brands Rate Limits
  slug: acuity-brands-rate-limits
rules:
- name: acuity-brands API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: acuity-brands-jsonschema-spectral-rules
- name: acuity-brands API Rules
  rule_count: 29
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 17
  slug: acuity-brands-spectral-rules
score:
  band: developing
  composite: 42.0
  delta: -3.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 73.7
    developer_ergonomics: 28.3
    discoverability: 31.5
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acuity-brands/refs/heads/main/screenshots/acuity-brands-2026-06-20T164408.png
security:
- kind: authentication
  name: Acuity Brands Authentication
  slug: acuity-brands-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Acuity Brands Domain Security
  slug: acuity-brands-domain-security
  summary_line: TLSv1.3 · DMARC
slug: acuity-brands
tags:
- Fortune 1000
website: https://www.acuity-brands.com
---
