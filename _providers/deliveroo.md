---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Deliveroo Agentic Access
  operation_count: 15
  slug: deliveroo-agentic-access
  summary_line: 15 operations · 11 acting
api_count: 9
apis:
- description: The Deliveroo Catalogue API is part of the Retail Platform Suite and manages master grocery catalogues of up to 30,000 items per merchant. Retailers use it to publish product data, variations, and ava
  name: Deliveroo Catalogue API
  slug: catalogue-api
- description: The Deliveroo Picking API supports the Retail Platform Suite picking flow, letting grocery operators process incoming orders, remove unavailable items, propose substitutions, and accept or reject orde
  name: Deliveroo Picking API
  slug: picking-api
- description: The Deliveries API from Deliveroo — 1 operation(s) for deliveries.
  name: Deliveroo Deliveries API
  slug: deliveroo-deliveries-api
- description: The Menus API from Deliveroo — 1 operation(s) for menus.
  name: Deliveroo Menus API
  slug: deliveroo-menus-api
- description: The Opening Hours API from Deliveroo — 1 operation(s) for opening hours.
  name: Deliveroo Opening Hours API
  slug: deliveroo-opening-hours-api
- description: The Orders API from Deliveroo — 2 operation(s) for orders.
  name: Deliveroo Orders API
  slug: deliveroo-orders-api
- description: The Pricing API from Deliveroo — 1 operation(s) for pricing.
  name: Deliveroo Pricing API
  slug: deliveroo-pricing-api
- description: The Quotes API from Deliveroo — 1 operation(s) for quotes.
  name: Deliveroo Quotes API
  slug: deliveroo-quotes-api
- description: The Sync Status API from Deliveroo — 1 operation(s) for sync status.
  name: Deliveroo Sync Status API
  slug: deliveroo-sync-status-api
artifact_total: 93
asyncapis:
- description: Event-driven webhook callbacks delivered by the Deliveroo Developer Portal APIs. Integrators configure HTTPS webhook URLs for Order Events, Rider Events, and Menu (upload result) events. Each delivery
  name: Deliveroo Webhooks
  slug: deliveroo-webhooks-asyncapi
collections:
- collection_type: postman
  name: Deliveroo Catalogue API
  slug: postman-deliveroo-catalogue-api
- collection_type: postman
  name: Deliveroo Catalogue Deliveries API
  slug: postman-deliveroo-deliveries-api
- collection_type: postman
  name: Deliveroo Catalogue Menus API
  slug: postman-deliveroo-menus-api
- collection_type: postman
  name: Deliveroo Catalogue Opening Hours API
  slug: postman-deliveroo-opening-hours-api
- collection_type: postman
  name: Deliveroo Catalogue Orders API
  slug: postman-deliveroo-orders-api
- collection_type: postman
  name: Deliveroo Catalogue Picking API
  slug: postman-deliveroo-picking-api
- collection_type: postman
  name: Deliveroo Catalogue Pricing API
  slug: postman-deliveroo-pricing-api
- collection_type: postman
  name: Deliveroo Catalogue Quotes API
  slug: postman-deliveroo-quotes-api
- collection_type: postman
  name: Deliveroo Catalogue Sync Status API
  slug: postman-deliveroo-sync-status-api
- collection_type: open
  name: Deliveroo Catalogue API
  slug: open-deliveroo-catalogue-api
- collection_type: open
  name: Deliveroo Menu API
  slug: open-deliveroo-menu-api
- collection_type: open
  name: Deliveroo Order API
  slug: open-deliveroo-order-api
- collection_type: open
  name: Deliveroo Picking API
  slug: open-deliveroo-picking-api
- collection_type: open
  name: Deliveroo Signature API
  slug: open-deliveroo-signature-api
- collection_type: open
  name: Deliveroo Site API
  slug: open-deliveroo-site-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/deliveroo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deliveroo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deliveroo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deliveroo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deliveroo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deliveroo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deliveroo
- group: company
  title: ''
  type: Website
  url: https://deliveroo.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.deliveroo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.deliveroo.com/v2.0/docs
- group: start
  title: ''
  type: SignupURL
  url: https://developers.deliveroo.com/
- group: auth
  title: ''
  type: Authentication
  url: https://api-docs.deliveroo.com/v2.0/docs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deliveroo.co.uk/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deliveroo.co.uk/legal
- group: operate
  title: ''
  type: Support
  url: https://deliveroo.co.uk/help
- group: company
  title: ''
  type: Blog
  url: https://deliveroo.co.uk/blog
- group: design
  title: ''
  type: Spectral
  url: rules/deliveroo-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/deliveroo-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/deliveroo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deliveroo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/deliveroo-finops.yml
created: '2026-05-05'
description: A British online food delivery company operating across the United Kingdom, Europe, Asia, and the Middle East. Deliveroo's Developer Portal exposes three API suites — Partner Platform, Retail Platform, and Signature — that restaurants, grocers, and merchants use to integrate menus, orders, sites, and on-demand courier delivery.
examples:
- key_count: 3
  name: Catalogue Api Catalogue Example
  slug: catalogue-api-catalogue-example
- key_count: 1
  name: Catalogue Api Site Price Overrides Example
  slug: catalogue-api-site-price-overrides-example
- key_count: 3
  name: Menu Api Menu Upload Example
  slug: menu-api-menu-upload-example
- key_count: 3
  name: Order Api Order Status Update Example
  slug: order-api-order-status-update-example
- key_count: 4
  name: Order Api Sync Status Example
  slug: order-api-sync-status-example
- key_count: 1
  name: Picking Api Item Amendments Example
  slug: picking-api-item-amendments-example
- key_count: 1
  name: Picking Api Reject Order Example
  slug: picking-api-reject-order-example
- key_count: 2
  name: Signature Api Delivery Request Example
  slug: signature-api-delivery-request-example
- key_count: 3
  name: Signature Api Location Example
  slug: signature-api-location-example
- key_count: 2
  name: Signature Api Order Example
  slug: signature-api-order-example
- key_count: 3
  name: Signature Api Order Request Example
  slug: signature-api-order-request-example
- key_count: 2
  name: Signature Api Quote Example
  slug: signature-api-quote-example
- key_count: 2
  name: Signature Api Quote Request Example
  slug: signature-api-quote-request-example
- key_count: 1
  name: Site Api Opening Hours Example
  slug: site-api-opening-hours-example
- key_count: 2
  name: Webhooks Menu Event Payload Example
  slug: webhooks-menu-event-payload-example
- key_count: 2
  name: Webhooks Order Event Payload Example
  slug: webhooks-order-event-payload-example
- key_count: 2
  name: Webhooks Rider Event Payload Example
  slug: webhooks-rider-event-payload-example
finops:
- name: Deliveroo Finops
  service_category: Food Delivery + Grocery Marketplace
  slug: deliveroo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deliveroo.png
json_schemas:
- name: Catalogue
  property_count: 3
  slug: catalogue-api-catalogue
- name: SitePriceOverrides
  property_count: 1
  slug: catalogue-api-site-price-overrides
- name: MenuUpload
  property_count: 3
  slug: menu-api-menu-upload
- name: OrderStatusUpdate
  property_count: 3
  slug: order-api-order-status-update
- name: SyncStatus
  property_count: 4
  slug: order-api-sync-status
- name: ItemAmendments
  property_count: 1
  slug: picking-api-item-amendments
- name: RejectOrder
  property_count: 1
  slug: picking-api-reject-order
- name: DeliveryRequest
  property_count: 2
  slug: signature-api-delivery-request
- name: Location
  property_count: 3
  slug: signature-api-location
- name: OrderRequest
  property_count: 3
  slug: signature-api-order-request
- name: Order
  property_count: 2
  slug: signature-api-order
- name: QuoteRequest
  property_count: 2
  slug: signature-api-quote-request
- name: Quote
  property_count: 2
  slug: signature-api-quote
- name: OpeningHours
  property_count: 1
  slug: site-api-opening-hours
- name: MenuEventPayload
  property_count: 2
  slug: webhooks-menu-event-payload
- name: OrderEventPayload
  property_count: 2
  slug: webhooks-order-event-payload
- name: RiderEventPayload
  property_count: 2
  slug: webhooks-rider-event-payload
json_structures:
- name: Catalogue Api Catalogue Structure
  property_count: 3
  slug: catalogue-api-catalogue-structure
- name: Catalogue Api Site Price Overrides Structure
  property_count: 1
  slug: catalogue-api-site-price-overrides-structure
- name: Menu Api Menu Upload Structure
  property_count: 3
  slug: menu-api-menu-upload-structure
- name: Order Api Order Status Update Structure
  property_count: 3
  slug: order-api-order-status-update-structure
- name: Order Api Sync Status Structure
  property_count: 4
  slug: order-api-sync-status-structure
- name: Picking Api Item Amendments Structure
  property_count: 1
  slug: picking-api-item-amendments-structure
- name: Picking Api Reject Order Structure
  property_count: 1
  slug: picking-api-reject-order-structure
- name: Signature Api Delivery Request Structure
  property_count: 2
  slug: signature-api-delivery-request-structure
- name: Signature Api Location Structure
  property_count: 3
  slug: signature-api-location-structure
- name: Signature Api Order Request Structure
  property_count: 3
  slug: signature-api-order-request-structure
- name: Signature Api Order Structure
  property_count: 2
  slug: signature-api-order-structure
- name: Signature Api Quote Request Structure
  property_count: 2
  slug: signature-api-quote-request-structure
- name: Signature Api Quote Structure
  property_count: 2
  slug: signature-api-quote-structure
- name: Site Api Opening Hours Structure
  property_count: 1
  slug: site-api-opening-hours-structure
- name: Webhooks Menu Event Payload Structure
  property_count: 2
  slug: webhooks-menu-event-payload-structure
- name: Webhooks Order Event Payload Structure
  property_count: 2
  slug: webhooks-order-event-payload-structure
- name: Webhooks Rider Event Payload Structure
  property_count: 2
  slug: webhooks-rider-event-payload-structure
jsonld:
- class_count: 2
  name: Deliveroo Catalogue Api Context
  property_count: 7
  slug: deliveroo-catalogue-api-context
- class_count: 1
  name: Deliveroo Menu Api Context
  property_count: 3
  slug: deliveroo-menu-api-context
- class_count: 2
  name: Deliveroo Order Api Context
  property_count: 5
  slug: deliveroo-order-api-context
- class_count: 2
  name: Deliveroo Picking Api Context
  property_count: 4
  slug: deliveroo-picking-api-context
- class_count: 6
  name: Deliveroo Signature Api Context
  property_count: 9
  slug: deliveroo-signature-api-context
- class_count: 1
  name: Deliveroo Site Api Context
  property_count: 5
  slug: deliveroo-site-api-context
- class_count: 3
  name: Deliveroo Webhooks Context
  property_count: 2
  slug: deliveroo-webhooks-context
layout: provider
modified: '2026-06-02'
name: Deliveroo
nav: Providers
network: true
overview: 'Deliveroo publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Catalogue API, Picking API, Deliveries API, and 6 more. Tagged areas include Food Delivery, Grocery, Marketplace, Logistics, and Restaurants.


  The Deliveroo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 7 JSON-LD contexts, and 3 Spectral governance rulesets.


  Deliveroo''s developer surface includes authentication, documentation, support, engineering blog, and 17 more developer resources.'
plans:
- name: Deliveroo Plans Pricing
  plan_count: 5
  slug: deliveroo-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 6
  name: Deliveroo Rate Limits
  slug: deliveroo-rate-limits
rules:
- name: Deliveroo API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: deliveroo-asyncapi-spectral-rules
- name: Deliveroo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: deliveroo-jsonschema-spectral-rules
- name: Deliveroo API Rules
  rule_count: 36
  severity_counts:
    error: 6
    hint: 0
    info: 4
    warn: 26
  slug: deliveroo-spectral-rules
score:
  band: developing
  composite: 47.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 32.2
    developer_ergonomics: 39.1
    discoverability: 68.5
    governance: 62.5
    operational_transparency: 36.8
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deliveroo/refs/heads/main/screenshots/deliveroo-2026-06-20T175902.png
security:
- kind: authentication
  name: Deliveroo Authentication
  slug: deliveroo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Deliveroo Domain Security
  slug: deliveroo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deliveroo Vulnerability Disclosure
  slug: deliveroo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deliveroo
tags:
- Food Delivery
- Grocery
- Marketplace
- Logistics
- Restaurants
website: https://deliveroo.co.uk/
---
