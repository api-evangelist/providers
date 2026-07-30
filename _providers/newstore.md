---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 79
  human_in_the_loop: 0
  name: Newstore Agentic Access
  operation_count: 150
  slug: newstore-agentic-access
  summary_line: 150 operations · 79 acting
api_count: 42
apis:
- description: Customer Profile Addresses
  name: Newstore address API
  slug: newstore-address-api
- description: Audit event operations.
  name: Newstore audit-events API
  slug: newstore-audit-events-api
- description: Operations on carts
  name: Newstore cart API
  slug: newstore-cart-api
- description: Fiscal cashboxes
  name: Newstore cashboxes API
  slug: newstore-cashboxes-api
- description: Customer API Configurations
  name: Newstore customer-configuration API
  slug: newstore-customer-configuration-api
- description: Customer Profiles
  name: Newstore customer-profile API
  slug: newstore-customer-profile-api
- description: Customer Profiles
  name: Newstore customerProfile API
  slug: newstore-customerprofile-api
- description: PII Data
  name: Newstore data API
  slug: newstore-data-api
- description: Easypost Adapter Configuration
  name: Newstore EasypostAdapterConfig API
  slug: newstore-easypostadapterconfig-api
- description: The external-public API from Newstore — 89 operation(s) for external-public.
  name: Newstore external-public API
  slug: newstore-external-public-api
- description: Fulfillment Requests
  name: Newstore fulfillment-requests API
  slug: newstore-fulfillment-requests-api
- description: Identity Providers
  name: Newstore identity-providers API
  slug: newstore-identity-providers-api
- description: Import Schemas
  name: Newstore Import Schemas API
  slug: newstore-import-schemas-api
- description: Inventory Configuration
  name: Newstore Inventory Configuration API
  slug: newstore-inventory-configuration-api
- description: Order Injection
  name: Newstore order-injection API
  slug: newstore-order-injection-api
- description: Order Injection Configuration
  name: Newstore order-injection-config API
  slug: newstore-order-injection-config-api
- description: Fiscal orders
  name: Newstore orders API
  slug: newstore-orders-api
- description: Package Types
  name: Newstore package-types API
  slug: newstore-package-types-api
- description: Pricebook Export
  name: Newstore Pricebook export API
  slug: newstore-pricebook-export-api
- description: Product Export
  name: Newstore Product export API
  slug: newstore-product-export-api
- description: Clienteling Profiles
  name: Newstore profiles API
  slug: newstore-profiles-api
- description: Provider Rates
  name: Newstore provider-rates API
  slug: newstore-provider-rates-api
- description: Payment provider operations
  name: Newstore providers API
  slug: newstore-providers-api
- description: Reason Codes API.
  name: Newstore Reason Codes API
  slug: newstore-reason-codes-api
- description: Reservations
  name: Newstore reservations API
  slug: newstore-reservations-api
- description: Roles
  name: Newstore roles API
  slug: newstore-roles-api
- description: Routing
  name: Newstore routing API
  slug: newstore-routing-api
- description: Routing Configuration
  name: Newstore routing-config API
  slug: newstore-routing-config-api
- description: Routing Ruleset
  name: Newstore routing-ruleset API
  slug: newstore-routing-ruleset-api
- description: Operations related to sales order management.
  name: Newstore sales-orders API
  slug: newstore-sales-orders-api
- description: Shipment Configurations
  name: Newstore shipment-configurations API
  slug: newstore-shipment-configurations-api
- description: Shipping Labels
  name: Newstore shipping-labels API
  slug: newstore-shipping-labels-api
- description: Shipping Option Audits
  name: Newstore shipping-option-audits API
  slug: newstore-shipping-option-audits-api
- description: Stock Operations
  name: Newstore stock API
  slug: newstore-stock-api
- description: Tax configuration - Store
  name: Newstore store-tax-configuration API
  slug: newstore-store-tax-configuration-api
- description: Fiscal stores
  name: Newstore stores API
  slug: newstore-stores-api
- description: Tax transactions
  name: Newstore tax-transactions API
  slug: newstore-tax-transactions-api
- description: Tenant configuration
  name: Newstore tenant-config API
  slug: newstore-tenant-config-api
- description: Tax configuration - Tenant
  name: Newstore tenant-tax-configuration API
  slug: newstore-tenant-tax-configuration-api
- description: Tokens
  name: Newstore token-operations API
  slug: newstore-token-operations-api
- description: Third Party Promotions Engine
  name: Newstore tppe API
  slug: newstore-tppe-api
- description: Users
  name: Newstore users API
  slug: newstore-users-api
artifact_total: 48
asyncapis:
- description: ''
  name: Newstore Webhooks
  slug: newstore-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newstore-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/newstore-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/newstore-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/newstore-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.newstore.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.newstore.net/api/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.newstore.com
- group: design
  title: ''
  type: Webhooks
  url: https://docs.newstore.net/api/webhooks/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NewStore
- group: operate
  title: ''
  type: StatusPage
  url: https://status.newstore.net/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.newstore.net/release-notes/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.newstore.net/release-notes/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.newstore.com/company/roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.newstore.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.newstore.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.newstore.com/legal/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: mailto:support@newstore.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/newstore-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/newstore-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/newstore-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/newstore-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/newstore-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/newstore-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/newstore-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/newstore-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/newstore-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/newstore-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/newstore-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/newstore-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: NewStore is a mobile-first omnichannel order management system (OMS) and point-of-service platform for retail brands. Its cloud platform unifies order management, mobile POS and checkout, clienteling, inventory and availability, fulfillment and order routing, returns, tax, fiscalization, and store operations into a single system, exposed through the NewStore Omnichannel REST API. The public API covers carts and checkout, customer profiles, orders and sales orders, in-store pickup and shipments, stock and reservations, fulfillment routing, catalog/pricebook/product export, identity and access management (users, roles, providers), and tenant/store configuration. Integrations are delivered through a documented webhook/adapter surface (payment, tax, shipping, fulfillment, gift card, availability, and an event stream). Authentication is OAuth 2.0 client-credentials against a per-tenant Keycloak identity server. NewStore was founded by Stephan Schambach.
image: https://developer.newstore.com/static/images/logo.png
layout: provider
mcp_servers:
- description: ''
  name: newstore-mcp.yml
  slug: newstore-mcpyml
modified: '2026-07-20'
name: Newstore
nav: Providers
network: true
overview: 'Newstore publishes 42 APIs on the [APIs.io](https://apis.io/) network, including address API, audit-events API, cart API, and 39 more. Tagged areas include Company, Retail, Omnichannel, Order Management, and Point of Sale.


  The Newstore catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Newstore''s developer surface includes authentication, documentation, API reference, changelog, pricing, support, sandbox, and 23 more developer resources.'
random_paper: 67
scopes:
- name: Newstore Scopes
  scope_count: 29
  slug: newstore-scopes
  summary_line: 29 scopes · clientCredentials
score:
  band: developing
  composite: 47.3
  delta: -3.8
  facets:
    commercial_clarity: 31.6
    contract_quality: 51.6
    developer_ergonomics: 49.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 57.9
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Newstore Authentication
  slug: newstore-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Newstore Domain Security
  slug: newstore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: newstore
tags:
- Company
- Retail
- Omnichannel
- Order Management
- Point of Sale
- Ecommerce
- Fulfillment
- Inventory
- Store Operations
- REST
website: https://developer.newstore.com
---
