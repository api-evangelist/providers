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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.6
  scored_at: '2026-08-06'
api_count: 21
apis:
- description: The Applications API from Ankorstore — 1 operation(s) for applications.
  name: Ankorstore Applications API
  slug: ankorstore-applications-api
- description: The Brands API from Ankorstore — 8 operation(s) for brands.
  name: Ankorstore Brands API
  slug: ankorstore-brands-api
- description: 'ℹ️ This section describes the API endpoints that you can use to manage your catalog resources, such as products, product variants etc. ## 💡 Working with Products Here you will find information about t'
  name: Ankorstore Catalog API
  slug: ankorstore-catalog-api
- description: The Catalog Exchange API from Ankorstore — 3 operation(s) for catalog exchange.
  name: Ankorstore Catalog Exchange API
  slug: ankorstore-catalog-exchange-api
- description: '## 👋 Getting Started The catalogue integration process relies on the concept of operations. An operation is a batch of records representing the products to create, update or delete. The completion sta'
  name: Ankorstore Catalog Integrations API
  slug: ankorstore-catalog-integrations-api
- description: ℹ️ Here you can find the endpoints which are currently deprecated and will be removed in the future versions of the API. We strongly encourage you to migrate away from these endpoints in order to prev
  name: Ankorstore Deprecated API
  slug: ankorstore-deprecated-api
- description: 'ℹ️ Here you can find the information and endpoint specification related to fulfillment of the orders. ## 💡 About Fulfillment _Fulfillment_ is the process of preparing and shipping orders to customers '
  name: Ankorstore Fulfillment API
  slug: ankorstore-fulfillment-api
- description: 'ℹ️ This section contains general-purpose endpoints that are transversal to the system. These endpoints provide reference data useful across different integration scenarios. ## 💡 Currency Rates The cur'
  name: Ankorstore General API
  slug: ankorstore-general-api
- description: The Integration API from Ankorstore — 1 operation(s) for integration.
  name: Ankorstore Integration API
  slug: ankorstore-integration-api
- description: The Locations API from Ankorstore — 1 operation(s) for locations.
  name: Ankorstore Locations API
  slug: ankorstore-locations-api
- description: Operations for documents linked to fulfillment requests
  name: Ankorstore Media API
  slug: ankorstore-media-api
- description: The Movements API from Ankorstore — 2 operation(s) for movements.
  name: Ankorstore Movements API
  slug: ankorstore-movements-api
- description: ℹ️ This section of API allows to manage different types of orders in the system. Depending on the order type, there are different endpoints available to manage them. Before starting to work with the A
  name: Ankorstore Ordering API
  slug: ankorstore-ordering-api
- description: ℹ️ This section describes the API endpoints for managing _OrderPay_ orders and customers. OrderPay allows brands to create and manage orders for their own customers, handle payments, and track order l
  name: Ankorstore OrderPay API
  slug: ankorstore-orderpay-api
- description: ℹ️ Here your can find endpoints related to different types of shipping, available on the platform. <div class="warning"> Please note, that shipping information described here is only available for _In
  name: Ankorstore Shipping API
  slug: ankorstore-shipping-api
- description: The State API from Ankorstore — 1 operation(s) for state.
  name: Ankorstore State API
  slug: ankorstore-state-api
- description: The Stock Management API from Ankorstore — 1 operation(s) for stock management.
  name: Ankorstore Stock Management API
  slug: ankorstore-stock-management-api
- description: 'ℹ️ This section is dedicated to the testing API during development process. The listed endpoints are **not available** on production environment. ### Creating Test Orders When using the public sandbox'
  name: Ankorstore Testing API
  slug: ankorstore-testing-api
- description: 'ℹ️ This section describes the API endpoints for retrieving user and platform configuration. ## 💡 User Configuration The user configuration endpoints return locale and currency settings for the authent'
  name: Ankorstore User API
  slug: ankorstore-user-api
- description: The Users API from Ankorstore — 1 operation(s) for users.
  name: Ankorstore Users API
  slug: ankorstore-users-api
- description: 'ℹ️ This section describes the API endpoints which can be used for managing webhook subscriptions. ## 💡 Overview In order to be able to manage Webhook Subscriptions via API you should understand the re'
  name: Ankorstore Webhooks API
  slug: ankorstore-webhooks-api
artifact_total: 25
asyncapis:
- description: ''
  name: Ankorstore Webhooks
  slug: ankorstore-webhooks
common:
- group: docs
  title: ''
  type: Documentation
  url: https://ankorstore.github.io/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://ankorstore.github.io/api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://ankorstore.github.io/api-docs/#section/Getting-Started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ankorstore
- group: start
  title: ''
  type: SignUp
  url: https://www.ankorstore.com/register
- group: operate
  title: ''
  type: Support
  url: mailto:api@ankorstore.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/ankorstore-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ankorstore-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ankorstore-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ankorstore-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/ankorstore-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ankorstore-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/ankorstore-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ankorstore-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/ankorstore-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ankorstore-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ankorstore-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ankorstore-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ankorstore-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ankorstore-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/ankorstore-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ankorstore-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ankorstore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ankorstore.com
created: '2026-07-17'
description: 'Ankorstore is a European B2B wholesale marketplace that connects independent brands with independent retailers across Europe. Its public developer platform lets brands and their technical partners programmatically manage their presence on the marketplace: sync product catalogs and stock, update prices, process and transition orders, request shipping quotes and schedule pickups, manage Ankorstore Fulfillment Center replenishments, run OrderPay flows for a brand''s own customers, and subscribe to real-time webhook notifications. The API is built on the JSON:API specification, secured with OAuth2 client credentials, and ships alongside the ASTRAL stock-tracking/logistics API and a fulfillment media service, with a public sandbox environment and a downloadable mock server for testing.'
image: https://cdn.ankorstore.com/images/logo/logo-black.svg
layout: provider
mcp_servers:
- description: ''
  name: ankorstore-mcp.yml
  slug: ankorstore-mcpyml
modified: '2026-07-17'
name: Ankorstore
nav: Providers
network: true
overview: 'Ankorstore publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Brands API, Catalog API, and 18 more. Tagged areas include Company, Retail, Wholesale, Marketplace, and E-commerce.


  The Ankorstore catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ankorstore''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, changelog, and 18 more developer resources.'
random_paper: 79
score:
  band: developing
  composite: 44.0
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 74.3
    developer_ergonomics: 51.6
    discoverability: 63.0
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 44.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ankorstore/refs/heads/main/screenshots/ankorstore-2026-07-25T200257.png
security:
- kind: authentication
  name: Ankorstore Authentication
  slug: ankorstore-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Ankorstore Domain Security
  slug: ankorstore-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: ankorstore
tags:
- Company
- Retail
- Wholesale
- Marketplace
- E-commerce
- Ordering
- Fulfillment
- Catalog
- Webhooks
- JSON:API
website: https://www.ankorstore.com
---
