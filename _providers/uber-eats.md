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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Uber Eats Agentic Access
  operation_count: 17
  slug: uber-eats-agentic-access
  summary_line: 17 operations · 10 acting
api_count: 15
apis:
- description: The Integration Activation API suite onboards merchant stores onto a partner's Uber Eats integration, connecting Uber store identifiers to a partner platform and enabling subsequent menu, order, and s
  name: Uber Eats Integration Activation API
  slug: integration-activation
- description: The Menu API suite lets integrations retrieve and upsert full menus for a store and update individual menu items, modifier groups, prices, suspensions, and availability windows.
  name: Uber Eats Menu API
  slug: menu-api
- description: The Order API suite handles inbound Uber Eats orders, including order accept/deny, status updates, item-level adjustments, and cancellation flows. Orders are typically delivered to integrations via we
  name: Uber Eats Order API
  slug: order-api
- description: The Delivery Partner API suite handles delivery fulfillment by Uber couriers for Uber Eats orders, including courier assignment, tracking, and status updates surfaced back to the merchant integration.
  name: Uber Eats Delivery Partner API
  slug: delivery-partner
- description: The Delivery BYOC ("Bring Your Own Courier") API suite supports merchants and marketplace partners that use their own delivery fleet, exchanging assignment, status, and proof-of-delivery information w
  name: Uber Eats Delivery BYOC API
  slug: delivery-byoc
- description: The Promotions API suite creates and manages marketing campaigns and discounts on Uber Eats stores, including campaign lifecycle, targeting, and reporting.
  name: Uber Eats Promotions API
  slug: promotions
- description: The Reporting API suite returns transactional, financial, and performance reports for Uber Eats stores, used by merchants and marketplace partners for reconciliation and analytics.
  name: Uber Eats Reporting API
  slug: reporting
- description: The Organizations API lets Uber Direct partners manage parent organizations and child accounts (e.g. multi-tenant merchants), including provisioning of API credentials and store-level access.
  name: Uber Direct Organizations API
  slug: uber-direct-organizations
- description: The Courier Pick & Pack API supports shop-and-pay style deliveries where the courier shops on behalf of the customer, including item lists, substitutions, and shopping progress events.
  name: Uber Direct Courier Pick & Pack API
  slug: uber-direct-pick-and-pack
- description: The Refund API supports refund requests on completed Uber Direct deliveries, including the corresponding webhook events that notify merchants of refund outcomes.
  name: Uber Direct Refund API
  slug: uber-direct-refund
- description: The Business Location Management API administers physical pickup locations associated with Uber Direct accounts, used for routing and dispatch.
  name: Uber Direct Business Location Management API
  slug: uber-direct-business-locations
- description: Both Uber Eats and Uber Direct send webhook events for order lifecycle, courier updates, refunds, shopping progress, and delivery status. Partners register webhook URLs in the Uber Developer Portal an
  name: Uber Eats & Direct Webhooks
  slug: webhooks
- description: Uber APIs are authenticated using OAuth 2.0. Server-to-server integrations use the client_credentials grant; user-facing integrations use the authorization_code grant with PKCE. Tokens are obtained fr
  name: Uber OAuth 2.0
  slug: oauth
- description: The Customers API from Uber Eats — 5 operation(s) for customers.
  name: Uber Eats Customers API
  slug: uber-eats-customers-api
- description: The Eats API from Uber Eats — 9 operation(s) for eats.
  name: Uber Eats Eats API
  slug: uber-eats-eats-api
artifact_total: 68
collections:
- collection_type: open
  name: Uber Direct (DaaS) API
  slug: open-uber-direct
- collection_type: open
  name: Uber Eats Marketplace API
  slug: open-uber-eats
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uber-eats-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uber-eats-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uber-eats-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/uber-eats-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.uber.com/us/en/business/products/eats/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uber
- group: build
  title: Uber Direct JavaScript/TypeScript SDK
  type: SDKs
  url: https://github.com/uber/uber-direct-sdk
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.uber.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uber.com/docs
- group: docs
  title: ''
  type: UberEatsDocs
  url: https://developer.uber.com/docs/eats/introduction
- group: docs
  title: ''
  type: UberDirectDocs
  url: https://developer.uber.com/docs/deliveries/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developer.uber.com/docs/eats/guides/authentication
- group: design
  title: ''
  type: Webhooks
  url: https://developer.uber.com/docs/eats/guides/webhooks
- group: other
  title: ''
  type: Dashboard
  url: https://developer.uber.com/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.uber.com/docs/riders/policies/legal
- group: company
  title: ''
  type: Blog
  url: https://www.uber.com/newsroom/
- group: operate
  title: ''
  type: Status
  url: https://status.uber.com/
- group: design
  title: ''
  type: SpectralRules
  url: rules/uber-eats-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/uber-eats-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uber-eats-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uber-eats-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uber-eats-finops.yml
created: '2026-05-23'
description: Uber Eats exposes a family of developer APIs through the Uber Developer Portal that let restaurants, marketplace platforms, POS providers, and logistics partners integrate directly with Uber Eats and Uber Direct. The Uber Eats Marketplace APIs cover store onboarding, store status and hours, menu management, order ingestion and fulfillment, delivery fulfillment (Uber-courier and BYOC), promotions, and reporting. Uber Direct (Deliveries) exposes Uber's courier network for on-demand same-day delivery — quotes, deliveries, courier tracking, proof of delivery, refunds, pick-and-pack, and webhook notifications. All APIs are RESTful, JSON, and gated by OAuth 2.0 client credentials issued from the Uber Developer Portal.
examples:
- key_count: 4
  name: Eats Menu Example
  slug: eats-menu-example
- key_count: 5
  name: Eats Menu Item Example
  slug: eats-menu-item-example
- key_count: 9
  name: Eats Order Example
  slug: eats-order-example
- key_count: 7
  name: Eats Store Example
  slug: eats-store-example
- key_count: 3
  name: Eats Store Status Example
  slug: eats-store-status-example
- key_count: 14
  name: Uber Direct Delivery Quote Req Example
  slug: uber-direct-delivery-quote-req-example
- key_count: 10
  name: Uber Direct Delivery Quote Resp Example
  slug: uber-direct-delivery-quote-resp-example
- key_count: 18
  name: Uber Direct Delivery Req Example
  slug: uber-direct-delivery-req-example
- key_count: 19
  name: Uber Direct Delivery Resp Example
  slug: uber-direct-delivery-resp-example
- key_count: 7
  name: Uber Direct Manifest Item Example
  slug: uber-direct-manifest-item-example
- key_count: 2
  name: Uber Direct Podreq Example
  slug: uber-direct-podreq-example
- key_count: 1
  name: Uber Direct Podresp Example
  slug: uber-direct-podresp-example
- key_count: 8
  name: Uber Direct Update Delivery Req Example
  slug: uber-direct-update-delivery-req-example
finops:
- name: Uber Eats Finops
  service_category: API
  slug: uber-eats-finops
graphqls:
- description: This conceptual GraphQL schema represents the Uber Eats platform API domain, covering restaurant and store management, menus, orders, delivery fulfillment, promotions, customer data, and reporting. Ub
  name: Uber Eats GraphQL Schema
  slug: uber-eats-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uber-eats.png
json_schemas:
- name: MenuItem
  property_count: 5
  slug: eats-menu-item
- name: Menu
  property_count: 4
  slug: eats-menu
- name: Order
  property_count: 9
  slug: eats-order
- name: Store
  property_count: 7
  slug: eats-store
- name: StoreStatus
  property_count: 3
  slug: eats-store-status
- name: DeliveryQuoteReq
  property_count: 14
  slug: uber-direct-delivery-quote-req
- name: DeliveryQuoteResp
  property_count: 10
  slug: uber-direct-delivery-quote-resp
- name: DeliveryReq
  property_count: 18
  slug: uber-direct-delivery-req
- name: DeliveryResp
  property_count: 19
  slug: uber-direct-delivery-resp
- name: ManifestItem
  property_count: 7
  slug: uber-direct-manifest-item
- name: PODReq
  property_count: 2
  slug: uber-direct-podreq
- name: PODResp
  property_count: 1
  slug: uber-direct-podresp
- name: UpdateDeliveryReq
  property_count: 8
  slug: uber-direct-update-delivery-req
json_structures:
- name: Eats Menu Item Structure
  property_count: 5
  slug: eats-menu-item-structure
- name: Eats Menu Structure
  property_count: 4
  slug: eats-menu-structure
- name: Eats Order Structure
  property_count: 9
  slug: eats-order-structure
- name: Eats Store Status Structure
  property_count: 3
  slug: eats-store-status-structure
- name: Eats Store Structure
  property_count: 7
  slug: eats-store-structure
- name: Uber Direct Delivery Quote Req Structure
  property_count: 14
  slug: uber-direct-delivery-quote-req-structure
- name: Uber Direct Delivery Quote Resp Structure
  property_count: 10
  slug: uber-direct-delivery-quote-resp-structure
- name: Uber Direct Delivery Req Structure
  property_count: 18
  slug: uber-direct-delivery-req-structure
- name: Uber Direct Delivery Resp Structure
  property_count: 19
  slug: uber-direct-delivery-resp-structure
- name: Uber Direct Manifest Item Structure
  property_count: 7
  slug: uber-direct-manifest-item-structure
- name: Uber Direct Podreq Structure
  property_count: 2
  slug: uber-direct-podreq-structure
- name: Uber Direct Podresp Structure
  property_count: 1
  slug: uber-direct-podresp-structure
- name: Uber Direct Update Delivery Req Structure
  property_count: 8
  slug: uber-direct-update-delivery-req-structure
jsonld:
- class_count: 5
  name: Uber Eats Eats Context
  property_count: 26
  slug: uber-eats-eats-context
- class_count: 8
  name: Uber Eats Uber Direct Context
  property_count: 58
  slug: uber-eats-uber-direct-context
layout: provider
modified: '2026-06-03'
name: Uber Eats
nav: Providers
network: true
overview: 'Uber Eats publishes 2 APIs on the [APIs.io](https://apis.io/) network: Customers API and Eats API. Tagged areas include Uber Eats, Uber Direct, Food Delivery, Last-Mile Logistics, and Restaurants.


  The Uber Eats catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Uber Eats'' developer surface includes authentication, documentation, engineering blog, status page, and 18 more developer resources.'
plans:
- name: Uber Eats Plans Pricing
  plan_count: 6
  slug: uber-eats-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Uber Eats Rate Limits
  slug: uber-eats-rate-limits
rules:
- name: Uber Eats API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: uber-eats-jsonschema-spectral-rules
- name: Uber Eats API Rules
  rule_count: 27
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 16
  slug: uber-eats-rules
scopes:
- name: Uber Eats Scopes
  scope_count: 8
  slug: uber-eats-scopes
  summary_line: 8 scopes · clientCredentials
score:
  band: developing
  composite: 55.0
  delta: -4.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.1
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 34.2
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uber-eats/refs/heads/main/screenshots/uber-eats-2026-06-20T195931.png
security:
- kind: authentication
  name: Uber Eats Authentication
  slug: uber-eats-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Uber Eats Domain Security
  slug: uber-eats-domain-security
  summary_line: TLSv1.3 · DMARC
slug: uber-eats
tags:
- Uber Eats
- Uber Direct
- Food Delivery
- Last-Mile Logistics
- Restaurants
- Menus
- Orders
- Fulfillment
- Courier
- OAuth2
website: https://www.uber.com/us/en/business/products/eats/
---
