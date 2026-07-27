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
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 81.7
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 49
  human_in_the_loop: 0
  name: Boxc Agentic Access
  operation_count: 83
  slug: boxc-agentic-access
  summary_line: 83 operations · 49 acting
api_count: 22
apis:
- description: Calculate the landed cost of a shipment. This is a quick way to calculate the duties and taxes owed for a shipment without having to create one.
  name: Boxc CalculateDuty API
  slug: boxc-calculateduty-api
- description: The Classify resource permits a user to retrieve the <em>most likely</em> HS code and description for one or more products. Each successful request costs $0.05 (USD) regardless of the number of produc
  name: Boxc Classify API
  slug: boxc-classify-api
- description: The Credentials resource allows users to store their own carrier account secrets securely. This gives users the ability to reuse their credentials without providing actual secret values in every singl
  name: Boxc Credentials API
  slug: boxc-credentials-api
- description: Not to be confused with Fulfillment [Products](/#tag/Products), Customs Products are for clearing shipments containing regulated items like Food and Cosmetics (PGA). Customs Products contain informati
  name: Boxc CustomsProducts API
  slug: boxc-customsproducts-api
- description: An entry point is the drop off location / origin for your shipments which affects your rates and the routes available. The `entry_point.id` is required when creating a shipment. You must query this en
  name: Boxc EntryPoints API
  slug: boxc-entrypoints-api
- description: 'The Estimate resource allows a user to retrieve the estimated cost of shipping a package based on weight, dimensions, entry point, destination, and other parameters. No services will be returned if a '
  name: Boxc Estimate API
  slug: boxc-estimate-api
- description: The Inbound resource is part of the fulfillment component and allows customers to restock their products at warehouses operated by BoxC. An inbound shipment's products can't be modified after creation
  name: Boxc Inbound API
  slug: boxc-inbound-api
- description: Invoices and statements are generated weekly and include a summary of all transactions between the invoice's `start_date` and `end_date`. Users can export an itemized list of all transactions for a bi
  name: Boxc Invoices API
  slug: boxc-invoices-api
- description: The Labels resource allows a user to create, cancel, retrieve, and track labels for shipments. A label can't be created if there is already an uncancelled or processed label for the shipment. Labels t
  name: Boxc Labels API
  slug: boxc-labels-api
- description: The Manifests resource is used for generating the paperwork required for dropping off Overpacks at a [collection center](/#tag/EntryPoints) or carrier facility at the end of the day. It also transmits
  name: Boxc Manifests API
  slug: boxc-manifests-api
- description: The Orders resource allows you to create, read, update, and delete orders that are meant to be fulfilled by BoxC. If you wish to manually create an order for a third party shop you must provide the `s
  name: Boxc Orders API
  slug: boxc-orders-api
- description: The Overpacks resource allows a user to combine many Shipments into one object for faster clearance with BoxC and Customs. An overpack can be a carton, container, pallet, or bag. Regardless, it must c
  name: Boxc Overpacks API
  slug: boxc-overpacks-api
- description: The Products resource allows users to add their products to the BoxC system. A product can have one or more Stock Keeping Units (SKUs). This gives users the ability to link their different shops' SKUs
  name: Boxc Products API
  slug: boxc-products-api
- description: The Reshipments resource allows you to reship one or more returned packages at a time from a BoxC warehouse. When a reshipment is created the `status` of all included returns will change to "Reshippin
  name: Boxc Reshipments API
  slug: boxc-reshipments-api
- description: 'The Returns resource allows a user to retrieve a list of returned shipments processed at a BoxC warehouse. Users may verify, [reship](/#tag/Reshipments), or discard their returns. Discarding a return '
  name: Boxc Returns API
  slug: boxc-returns-api
- description: 'The Shipments resource allows a user to create, update, retrieve, and delete shipments. Only test shipments and shipments without labels can be deleted. Shipments with uncancelled or processed labels '
  name: Boxc Shipments API
  slug: boxc-shipments-api
- description: 'The Shops resource allows a user to manage their fulfillment shop. A shop with orders or SKUs cannot be deleted. Clients should use a third party platform for integrating their ecommerce marketplaces '
  name: Boxc Shops API
  slug: boxc-shops-api
- description: The Track resource allows clients to retrieve tracking events for shipments by their tracking number. You may only track one shipment per request. This endpoint is rate limited. Some shipments may hav
  name: Boxc Track API
  slug: boxc-track-api
- description: The Users resources allows an application to retrieve information about the tokenized user such as balances, personal/company address, and subscriptions. Only the addresses can be updated by applicati
  name: Boxc Users API
  slug: boxc-users-api
- description: The Validate Address resource permits a user to validate and retrieve the most likely matches of provided postal addresses. Each successful validation costs $0.03 (USD).
  name: Boxc ValidateAddress API
  slug: boxc-validateaddress-api
- description: The Warehouses resource allows you to retrieve location and identity information for a single warehouse or all warehouses. You should query this endpoint to retrieve an active list of fulfillment ware
  name: Boxc Warehouses API
  slug: boxc-warehouses-api
- description: The Webhooks resource allows applications to subscribe to topics and receive events for users. Events are pushed to the webhook's `address` with a payload by issuing an HTTP POST request each time. **
  name: Boxc Webhooks API
  slug: boxc-webhooks-api
artifact_total: 28
asyncapis:
- description: ''
  name: Boxc Webhooks
  slug: boxc-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://boxc.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.boxc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.boxc.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.boxc.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.boxc.com/#tag/Introduction
- group: operate
  title: ''
  type: Support
  url: https://support.boxc.com/support/solutions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boxc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boxc.com/terms-and-conditions
- group: start
  title: ''
  type: Login
  url: https://accounts.boxc.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/boxc-openapi-original.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/boxc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/boxc-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/boxc-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/boxc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/boxc-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/boxc-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/boxc-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/boxc-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/boxc-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/boxc-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/boxc-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/boxc-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/boxc-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/boxc-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/boxc-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/boxc-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boxc-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/boxc-agentic-access.yml
created: '2026-07-17'
description: BoxC (BoxC Logistics, Inc.) is an international e-commerce logistics management platform. Its single RESTful API drives cross-border ecommerce by integrating dozens of carriers, customs clearance, duties and taxes, warehousing and fulfillment, and returns through one integration. A routing engine can complete every leg of a shipment's journey or only selected steps on the merchant's behalf. The v1 API (currently 1.123) exposes 83 operations across 34 resources including Shipments, Labels, Orders, Products, Shops, Warehouses, Manifests, Overpacks, Inbound, Returns, Reshipments, Webhooks, Carrier Credentials, Customs Products, Entry Points, Tracking, Calculate Duty, Validate Address, and Classify. Authentication is OAuth 2.0 / OpenID Connect with RS256 JWT bearer tokens.
image: https://storage.googleapis.com/boxc_cdn/public/boxc-logo.png
layout: provider
mcp_servers:
- description: ''
  name: boxc-mcp.yml
  slug: boxc-mcpyml
modified: '2026-07-18'
name: Boxc
nav: Providers
network: true
overview: 'Boxc publishes 22 APIs on the [APIs.io](https://apis.io/) network, including CalculateDuty API, Classify API, Credentials API, and 19 more. Tagged areas include Company, Logistics, Shipping, Ecommerce, and Cross-Border.


  The Boxc catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Boxc''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, sandbox, and 22 more developer resources.'
random_paper: 20
scopes:
- name: Boxc Scopes
  scope_count: 19
  slug: boxc-scopes
  summary_line: 19 scopes · authorizationCode
score:
  band: thin
  composite: 44.7
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 60.4
    developer_ergonomics: 71.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 44.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boxc/refs/heads/main/screenshots/boxc-2026-07-25T203656.png
security:
- kind: authentication
  name: Boxc Authentication
  slug: boxc-authentication
  summary_line: oauth2/openIdConnect/http · 2 schemes
- kind: domain-security
  name: Boxc Domain Security
  slug: boxc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: boxc
tags:
- Company
- Logistics
- Shipping
- Ecommerce
- Cross-Border
- Fulfillment
- Customs
- Tracking
- Webhooks
website: https://boxc.com
---
