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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Acuity Brands Agentic Access
  operation_count: 9
  slug: acuity-brands-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: https://api.acuitybrands.com/v1
  baseurl_source: spec
  description: Product catalog and item details
  name: acuity-brands Catalog API
  slug: acuity-brands-catalog-api
- baseURL: https://api.acuitybrands.com/v1
  baseurl_source: spec
  description: Product inventory and availability
  name: acuity-brands Inventory API
  slug: acuity-brands-inventory-api
- baseURL: https://api.acuitybrands.com/v1
  baseurl_source: spec
  description: Order status and shipment tracking
  name: acuity-brands Orders API
  slug: acuity-brands-orders-api
- baseURL: https://api.acuitybrands.com/v1
  baseurl_source: spec
  description: Web content and product page data
  name: acuity-brands Webpages API
  slug: acuity-brands-webpages-api
artifact_total: 49
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Acuity Brands Catalog API
  slug: open-acuity-brands-catalog-api
- collection_type: open
  name: Acuity Brands Catalog Inventory API
  slug: open-acuity-brands-inventory-api
- collection_type: open
  name: Acuity Brands Catalog Orders API
  slug: open-acuity-brands-orders-api
- collection_type: open
  name: Acuity Brands Catalog Webpages API
  slug: open-acuity-brands-webpages-api
- collection_type: open
  name: Acuity Brands API
  slug: open-acuity-brands
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/acuity-brands-capability-edges.yml
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
name: Acuity Brands
nav: Providers
network: true
overview: 'Acuity Brands publishes 4 APIs on the [APIs.io](https://apis.io/) network, including acuity-brands Catalog API, acuity-brands Inventory API, acuity-brands Orders API, and 1 more. Tagged areas include Fortune 1000.


  The Acuity Brands catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Acuity Brands'' developer surface includes authentication, developer portal, documentation, and 9 more developer resources.'
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
random_paper: 11
rate_limits:
- limit_count: 0
  name: Acuity Brands Rate Limits
  slug: acuity-brands-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Acuity Brands API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: acuity-brands-jsonschema-spectral-rules
- effective_rule_count: 70
  extends:
  - spectral:oas
  name: Acuity Brands API Rules
  rule_count: 29
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 17
  slug: acuity-brands-spectral-rules
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 66.7
    developer_ergonomics: 31.0
    discoverability: 25.9
    governance: 28.8
    operational_transparency: 2.6
  previous_composite: 31.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
