---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: The Logiwa Integration API is an RPC-over-HTTP interface with 81 documented operations covering products and kits, shipment orders and order details, purchase orders, receipt orders and receiving, inv
  name: Logiwa Integration API
  slug: logiwa-integration-api
- description: Logiwa's outbound event surface. Eleven documented topics deliver order status, receipt and purchase order status, inventory change, location update, movement, receipt, shipment tracking and consolida
  name: Logiwa Webhooks
  slug: logiwa-webhooks
artifact_total: 10
asyncapis:
- description: ''
  name: Logiwa Webhooks
  slug: logiwa-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.logiwa.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.logiwa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.logiwa.com/?id=5df0d8bfe6466c2eec992f31
- group: docs
  title: ''
  type: APIReference
  url: https://developer.logiwa.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.logiwa.com/?id=5df0d8bfe6466c2eec992f31
- group: company
  title: ''
  type: Blog
  url: https://www.logiwa.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.logiwa.com/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.logiwa.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.logiwa.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/logiwa-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/logiwa-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/logiwa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/logiwa-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/logiwa-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/logiwa-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/logiwa-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/logiwa-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/logiwa-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/logiwa-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/logiwa-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/logiwa-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/logiwa-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/logiwa-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/logiwa-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/logiwa-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-25'
description: 'Logiwa is a Chicago-based cloud fulfillment software company whose flagship product, Logiwa IO, is a warehouse management and fulfillment management system (WMS/FMS) built for high-volume B2C and DTC brands, wholesalers and third-party logistics providers (3PLs). Logiwa exposes a documented Integration API covering products, shipment orders, purchase orders, receipt orders, inventory, locations, count plans, documents, warehouse tasks, transaction history and 3PL billing, plus an eleven-topic webhook surface for order, inventory, movement and shipment tracking events. The API is an RPC-over-POST design: 81 documented operations, all reached by POST to /en/api/IntegrationApi/{Method} on a per-tenant host, authenticated with an OAuth 2.0 password grant that yields a bearer token. Logiwa publishes no OpenAPI, AsyncAPI or other machine-readable contract, and no first-party SDKs; the reference is a JavaScript-rendered developer portal and API credentials are provisioned by sales
  rather than self-service.'
image: https://developer.logiwa.com/Content/img/logiwa_new_logo.png
layout: provider
modified: '2026-08-25'
name: Logiwa
nav: Providers
network: true
overview: 'Logiwa publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Warehouse Management, Fulfillment, Logistics, and Supply Chain.


  The Logiwa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Logiwa''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, authentication, and 19 more developer resources.'
plans:
- name: Logiwa Plans Pricing
  plan_count: 0
  slug: logiwa-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 6
  name: Logiwa Rate Limits
  slug: logiwa-rate-limits
scopes:
- name: Logiwa Scopes
  scope_count: 0
  slug: logiwa-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.8
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 39.5
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Logiwa Authentication
  slug: logiwa-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Logiwa Domain Security
  slug: logiwa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Logiwa Vulnerability Disclosure
  slug: logiwa-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Logiwa Trust Center
  slug: logiwa-trust-center
  summary_line: SOC 2 Type II
slug: logiwa
tags:
- Company
- Warehouse Management
- Fulfillment
- Logistics
- Supply Chain
- Inventory Management
- Order Management
- Third Party Logistics
- Ecommerce
- Shipping
- Webhooks
- SaaS
website: https://www.logiwa.com/
---
