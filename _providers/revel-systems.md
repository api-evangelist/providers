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
  - '{''url'': ''https://revelsystems.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.shift4.com/food-beverage — a different registrable domain (revelsystems.com -> shift4.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Revel Systems Agentic Access
  operation_count: 13
  slug: revel-systems-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 7
apis:
- description: Event-driven webhook channel that delivers POS events (order finalized, customer created/updated, stock changes, menu updates, timesheet changes, integration changes, reward cards, and ping) to partne
  name: Revel Webhooks
  slug: webhooks
- baseURL: https://yoursubdomain.revelup.com/resources
  baseurl_source: declared
  description: Customer records and addresses.
  name: Revel Systems Customers API
  slug: revel-systems-customers-api
- baseURL: https://yoursubdomain.revelup.com/resources
  baseurl_source: declared
  description: Establishment (location) resources.
  name: Revel Systems Establishments API
  slug: revel-systems-establishments-api
- baseURL: https://yoursubdomain.revelup.com/resources
  baseurl_source: declared
  description: Order and order-item resources.
  name: Revel Systems Orders API
  slug: revel-systems-orders-api
- baseURL: https://yoursubdomain.revelup.com/resources
  baseurl_source: declared
  description: Product catalog and modifier resources.
  name: Revel Systems Products API
  slug: revel-systems-products-api
- baseURL: https://yoursubdomain.revelup.com/resources
  baseurl_source: declared
  description: Labor scheduling and timesheet resources.
  name: Revel Systems Scheduling API
  slug: revel-systems-scheduling-api
- description: REST API for the Revel Systems iPad POS platform, covering orders, payments, products, inventory, customers, employees, scheduling, cash management, discounts, tax, tables, purchase orders, house acco
  name: Revel Systems API
  slug: revel-api
artifact_total: 93
asyncapis:
- description: 'Revel Systems delivers event notifications to partner-registered HTTPS endpoints via webhooks. Each event type is delivered by HTTP POST with a JSON body. Requests carry an HMAC-SHA1 signature in the '
  name: Revel Webhooks
  slug: revel-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Revel Open API
  slug: open-revel-open-api
- collection_type: open
  name: Revel Open Customers API
  slug: open-revel-systems-customers-api
- collection_type: open
  name: Revel Open Customers Establishments API
  slug: open-revel-systems-establishments-api
- collection_type: open
  name: Revel Open Customers Orders API
  slug: open-revel-systems-orders-api
- collection_type: open
  name: Revel Open Customers Products API
  slug: open-revel-systems-products-api
- collection_type: open
  name: Revel Open Customers Scheduling API
  slug: open-revel-systems-scheduling-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/revel-systems-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revel-systems-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revel-systems-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RevelSystems
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revel-systems
- group: company
  title: ''
  type: Website
  url: https://revelsystems.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.revelsystems.com/
- group: operate
  title: ''
  type: FAQ
  url: https://developer.revelsystems.com/revelsystems/docs/frequently-asked-questions
- group: design
  title: ''
  type: SpectralRules
  url: rules/revel-systems-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/revel-systems-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/revel-systems-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/revel-systems-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/revel-systems-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://revelsystems.com/blog/
created: '2026-05-08'
description: Revel Systems is a cloud iPad-based POS for restaurants and retailers. The Revel Open API exposes products, orders, customers, employees, inventory, schedules, and reporting via a REST interface for partner integrations. The API follows Django Tastypie conventions (objects/meta list envelope, field-lookup filtering) and is complemented by an HMAC-signed webhook channel.
examples:
- key_count: 13
  name: Revel Open Api Customer Example
  slug: revel-open-api-customer-example
- key_count: 2
  name: Revel Open Api Customer List Example
  slug: revel-open-api-customer-list-example
- key_count: 7
  name: Revel Open Api Establishment Example
  slug: revel-open-api-establishment-example
- key_count: 2
  name: Revel Open Api Establishment List Example
  slug: revel-open-api-establishment-list-example
- key_count: 22
  name: Revel Open Api Order Example
  slug: revel-open-api-order-example
- key_count: 2
  name: Revel Open Api Order List Example
  slug: revel-open-api-order-list-example
- key_count: 19
  name: Revel Open Api Product Example
  slug: revel-open-api-product-example
- key_count: 2
  name: Revel Open Api Product List Example
  slug: revel-open-api-product-list-example
- key_count: 10
  name: Revel Open Api Time Schedule Example
  slug: revel-open-api-time-schedule-example
- key_count: 2
  name: Revel Open Api Time Schedule List Example
  slug: revel-open-api-time-schedule-list-example
- key_count: 4
  name: Revel Webhooks Customer Event Payload Example
  slug: revel-webhooks-customer-event-payload-example
- key_count: 1
  name: Revel Webhooks Integration Changed Payload Example
  slug: revel-webhooks-integration-changed-payload-example
- key_count: 1
  name: Revel Webhooks Menu Updated Payload Example
  slug: revel-webhooks-menu-updated-payload-example
- key_count: 2
  name: Revel Webhooks Order Finalized Payload Example
  slug: revel-webhooks-order-finalized-payload-example
- key_count: 1
  name: Revel Webhooks Ping Payload Example
  slug: revel-webhooks-ping-payload-example
- key_count: 2
  name: Revel Webhooks Reward Card Event Payload Example
  slug: revel-webhooks-reward-card-event-payload-example
- key_count: 4
  name: Revel Webhooks Stock Status Payload Example
  slug: revel-webhooks-stock-status-payload-example
- key_count: 4
  name: Revel Webhooks Timesheet Event Payload Example
  slug: revel-webhooks-timesheet-event-payload-example
features:
- description: List endpoints return an objects array with a meta pagination envelope (total_count, limit, offset, next, previous).
  name: Tastypie REST Conventions
- description: Filter resources with Django-style lookups (e.g. id__lt, created_date__range, name__icontains).
  name: Field-Lookup Filtering
- description: Use the fields parameter to limit returned attributes and expand to inline one level of foreign-key relationships.
  name: Field Selection and Expansion
- description: Retrieve multiple records by ID in a single call using the set/id1;id2;id3 path form.
  name: Batch Retrieval
- description: Real-time event delivery secured with HMAC-SHA1 signatures and per-event-type endpoint registration.
  name: Signed Webhooks
finops:
- name: Revel Systems Finops
  service_category: Payments & POS
  slug: revel-systems-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revel-systems.png
integrations:
- description: Push order and sales data into accounting and ERP systems.
  name: Accounting and ERP
- description: Establishment-level payment configuration including ACH for US establishments.
  name: Payments
- description: Sync customer and loyalty data with marketing platforms.
  name: Marketing and CRM
json_schemas:
- name: CustomerList
  property_count: 2
  slug: revel-open-api-customer-list
- name: Customer
  property_count: 13
  slug: revel-open-api-customer
- name: EstablishmentList
  property_count: 2
  slug: revel-open-api-establishment-list
- name: Establishment
  property_count: 7
  slug: revel-open-api-establishment
- name: OrderList
  property_count: 2
  slug: revel-open-api-order-list
- name: Order
  property_count: 22
  slug: revel-open-api-order
- name: ProductList
  property_count: 2
  slug: revel-open-api-product-list
- name: Product
  property_count: 19
  slug: revel-open-api-product
- name: TimeScheduleList
  property_count: 2
  slug: revel-open-api-time-schedule-list
- name: TimeSchedule
  property_count: 10
  slug: revel-open-api-time-schedule
- name: CustomerEventPayload
  property_count: 4
  slug: revel-webhooks-customer-event-payload
- name: IntegrationChangedPayload
  property_count: 1
  slug: revel-webhooks-integration-changed-payload
- name: MenuUpdatedPayload
  property_count: 1
  slug: revel-webhooks-menu-updated-payload
- name: OrderFinalizedPayload
  property_count: 2
  slug: revel-webhooks-order-finalized-payload
- name: PingPayload
  property_count: 1
  slug: revel-webhooks-ping-payload
- name: RewardCardEventPayload
  property_count: 2
  slug: revel-webhooks-reward-card-event-payload
- name: StockStatusPayload
  property_count: 4
  slug: revel-webhooks-stock-status-payload
- name: TimesheetEventPayload
  property_count: 4
  slug: revel-webhooks-timesheet-event-payload
json_structures:
- name: Revel Open Api Customer List Structure
  property_count: 2
  slug: revel-open-api-customer-list-structure
- name: Revel Open Api Customer Structure
  property_count: 13
  slug: revel-open-api-customer-structure
- name: Revel Open Api Establishment List Structure
  property_count: 2
  slug: revel-open-api-establishment-list-structure
- name: Revel Open Api Establishment Structure
  property_count: 7
  slug: revel-open-api-establishment-structure
- name: Revel Open Api Order List Structure
  property_count: 2
  slug: revel-open-api-order-list-structure
- name: Revel Open Api Order Structure
  property_count: 22
  slug: revel-open-api-order-structure
- name: Revel Open Api Product List Structure
  property_count: 2
  slug: revel-open-api-product-list-structure
- name: Revel Open Api Product Structure
  property_count: 19
  slug: revel-open-api-product-structure
- name: Revel Open Api Time Schedule List Structure
  property_count: 2
  slug: revel-open-api-time-schedule-list-structure
- name: Revel Open Api Time Schedule Structure
  property_count: 10
  slug: revel-open-api-time-schedule-structure
- name: Revel Webhooks Customer Event Payload Structure
  property_count: 4
  slug: revel-webhooks-customer-event-payload-structure
- name: Revel Webhooks Integration Changed Payload Structure
  property_count: 1
  slug: revel-webhooks-integration-changed-payload-structure
- name: Revel Webhooks Menu Updated Payload Structure
  property_count: 1
  slug: revel-webhooks-menu-updated-payload-structure
- name: Revel Webhooks Order Finalized Payload Structure
  property_count: 2
  slug: revel-webhooks-order-finalized-payload-structure
- name: Revel Webhooks Ping Payload Structure
  property_count: 1
  slug: revel-webhooks-ping-payload-structure
- name: Revel Webhooks Reward Card Event Payload Structure
  property_count: 2
  slug: revel-webhooks-reward-card-event-payload-structure
- name: Revel Webhooks Stock Status Payload Structure
  property_count: 4
  slug: revel-webhooks-stock-status-payload-structure
- name: Revel Webhooks Timesheet Event Payload Structure
  property_count: 4
  slug: revel-webhooks-timesheet-event-payload-structure
jsonld:
- class_count: 10
  name: Revel Open Api Context
  property_count: 50
  slug: revel-open-api-context
- class_count: 8
  name: Revel Webhooks Context
  property_count: 12
  slug: revel-webhooks-context
layout: provider
modified: '2026-06-03'
name: Revel Systems
nav: Providers
network: true
overview: 'Revel Systems publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Revel Webhooks, Customers API, Establishments API, and 3 more. Tagged areas include Point-of-Sale, Restaurant, Retail, and iPad.


  The Revel Systems catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Revel Systems'' developer surface includes authentication, FAQ, engineering blog, and 11 more developer resources.'
plans:
- name: Revel Systems Plans Pricing
  plan_count: 1
  slug: revel-systems-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Revel Systems Rate Limits
  slug: revel-systems-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Revel Systems API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: revel-systems-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Revel Systems API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: revel-systems-jsonschema-spectral-rules
- effective_rule_count: 75
  extends:
  - spectral:oas
  name: Revel Systems API Rules
  rule_count: 34
  severity_counts:
    error: 8
    hint: 0
    info: 8
    warn: 18
  slug: revel-systems-rules
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 47.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.5
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 40.5
    developer_ergonomics: 2.4
    discoverability: 55.6
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 22.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revel-systems/refs/heads/main/screenshots/revel-systems-2026-06-20T193052.png
security:
- kind: authentication
  name: Revel Systems Authentication
  slug: revel-systems-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Revel Systems Domain Security
  slug: revel-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: revel-systems
tags:
- Point-of-Sale
- Restaurant
- Retail
- iPad
use_cases:
- description: Sync finalized orders into accounting, ERP, or analytics systems via the Order resource and order.finalized webhook.
  name: Order Synchronization
- description: Create and maintain products, modifiers, and combo sets across establishments.
  name: Catalog Management
- description: Sync customer profiles and loyalty/reward data with marketing and CRM platforms.
  name: Customer and Loyalty
- description: Read and write employee shifts and timesheets via TimeSchedule, TimeScheduleRule, and TimeSheetEntry.
  name: Labor and Scheduling
- description: React to stock-status changes in real time via the inout.stock webhook.
  name: Inventory Monitoring
website: https://revelsystems.com/
---
