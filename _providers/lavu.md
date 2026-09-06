---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Lavu Agentic Access
  operation_count: 2
  slug: lavu-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 2
apis:
- baseURL: https://admin.poslavu.com/cp/reqserv
  baseurl_source: spec
  description: Menu groups, categories, and items.
  name: Lavu Menu API
  slug: lavu-menu-api
- baseURL: https://admin.poslavu.com/cp/reqserv
  baseurl_source: spec
  description: Orders, order contents, and payments.
  name: Lavu Orders API
  slug: lavu-orders-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lavu (POSLavu) Inventory API
  slug: open-lavu-inventory-api
- collection_type: open
  name: Lavu (POSLavu) Inventory Menu API
  slug: open-lavu-menu-api
- collection_type: open
  name: Lavu (POSLavu) Inventory Orders API
  slug: open-lavu-orders-api
- collection_type: open
  name: Lavu (POSLavu) API
  slug: open-lavu-poslavu-api
- collection_type: open
  name: Lavu (POSLavu) Inventory Tables API
  slug: open-lavu-tables-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lavu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lavu-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lavu-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://lavu.com
- group: company
  title: ''
  type: Blog
  url: https://lavu.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://lavu.com/pricing/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lavu-inc
- group: commercial
  title: ''
  type: Plans
  url: plans/lavu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lavu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lavu-finops.yml
- group: design
  title: ''
  type: Rules
  url: rules/lavu-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/lavu-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/lavu-poslavu-api-context.jsonld
created: '2026-06-02'
description: Lavu is a cloud-based iPad restaurant point-of-sale system, now positioned as an AI-powered restaurant intelligence platform, serving restaurants, bars, and hospitality businesses with POS, payments, inventory, and reporting. Lavu promotes an open API that lets developers and restaurants extend the point of sale, build peripheral components, and create tailored integrations without waiting on vendor roadmaps. The POSLavu API is a POST-based interface where a single request server accepts form-encoded credentials (dataname, key, token) plus a table selector and returns XML rows; documented tables include menu_groups, menu_categories, menu_items, tables, orders, order_contents, order_payments, ingredients, and ingredient_usage. Records can be written with cmd=insert and an XML contents payload. Credentials are retrieved from the API tab of the POSLavu Control Panel, and the developer documentation is published at admin.poslavu.com; API access comes with an active Lavu account.
examples:
- key_count: 16
  name: Poslavu Api Menu Category Example
  slug: poslavu-api-menu-category-example
- key_count: 4
  name: Poslavu Api Menu Group Example
  slug: poslavu-api-menu-group-example
- key_count: 32
  name: Poslavu Api Menu Item Example
  slug: poslavu-api-menu-item-example
- key_count: 41
  name: Poslavu Api Order Content Example
  slug: poslavu-api-order-content-example
- key_count: 58
  name: Poslavu Api Order Example
  slug: poslavu-api-order-example
- key_count: 47
  name: Poslavu Api Order Payment Example
  slug: poslavu-api-order-payment-example
- key_count: 8
  name: Poslavu Api Table Example
  slug: poslavu-api-table-example
finops:
- name: Lavu Finops
  service_category: Point of Sale
  slug: lavu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lavu.png
json_schemas:
- name: MenuCategory
  property_count: 16
  slug: poslavu-api-menu-category
- name: MenuGroup
  property_count: 4
  slug: poslavu-api-menu-group
- name: MenuItem
  property_count: 32
  slug: poslavu-api-menu-item
- name: OrderContent
  property_count: 41
  slug: poslavu-api-order-content
- name: OrderPayment
  property_count: 47
  slug: poslavu-api-order-payment
- name: Order
  property_count: 58
  slug: poslavu-api-order
- name: Table
  property_count: 8
  slug: poslavu-api-table
json_structures:
- name: Poslavu Api Menu Category Structure
  property_count: 16
  slug: poslavu-api-menu-category-structure
- name: Poslavu Api Menu Group Structure
  property_count: 4
  slug: poslavu-api-menu-group-structure
- name: Poslavu Api Menu Item Structure
  property_count: 32
  slug: poslavu-api-menu-item-structure
- name: Poslavu Api Order Content Structure
  property_count: 41
  slug: poslavu-api-order-content-structure
- name: Poslavu Api Order Payment Structure
  property_count: 47
  slug: poslavu-api-order-payment-structure
- name: Poslavu Api Order Structure
  property_count: 58
  slug: poslavu-api-order-structure
- name: Poslavu Api Table Structure
  property_count: 8
  slug: poslavu-api-table-structure
jsonld:
- class_count: 7
  name: Lavu Poslavu Api Context
  property_count: 161
  slug: lavu-poslavu-api-context
layout: provider
modified: '2026-06-02'
name: Lavu
nav: Providers
network: true
overview: 'Lavu publishes 2 APIs on the [APIs.io](https://apis.io/) network: Menu API and Orders API. Tagged areas include Restaurant, Point-of-Sale, Payments, Inventory, and Menu Management.


  The Lavu catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Lavu''s developer surface includes authentication, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Lavu Plans Pricing
  plan_count: 4
  slug: lavu-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Lavu Rate Limits
  slug: lavu-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Lavu API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lavu-jsonschema-spectral-rules
- effective_rule_count: 76
  extends:
  - spectral:oas
  name: Lavu API Rules
  rule_count: 35
  severity_counts:
    error: 4
    hint: 0
    info: 9
    warn: 22
  slug: lavu-spectral-rules
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 70.5
    catalog_earned_first_party: 0.0
    catalog_gap: 44.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 21.3
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 28.8
    operational_transparency: 21.1
  previous_composite: 27.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lavu/refs/heads/main/screenshots/lavu-2026-06-20T184344.png
security:
- kind: authentication
  name: Lavu Authentication
  slug: lavu-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lavu Domain Security
  slug: lavu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lavu
tags:
- Restaurant
- Point-of-Sale
- Payments
- Inventory
- Menu Management
website: https://lavu.com
---
