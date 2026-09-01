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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.2
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Medusa's GraphQL surface over the store data core. The schema in this repo was derived from the OAS output schemas published in the medusajs/medusa repository; Medusa does not publish a hosted, intros
  name: Medusa GraphQL API
  slug: medusa-graphql-api
- description: Medusa hosts a Streamable HTTP Model Context Protocol server at https://docs.medusajs.com/mcp. It exposes the Medusa documentation to coding agents plus curated implementation-guide tools for data mig
  name: Medusa MCP Remote Server
  slug: medusa-mcp-server
- description: API keys can be used for authentication or resource-scoping. A secret API key can be used to authenticate admin users. A publishable API key can be used to scope client requests to one or more sales c
  name: Medusa Api Keys API
  slug: medusa-api-keys-api
- description: Auth API routes allow you to manage an admin user's authentication.
  name: Medusa Auth API
  slug: medusa-auth-api
- description: The [auth_provider] API from Medusa — 1 operation(s) for [auth_provider].
  name: Medusa [auth Provider] API
  slug: medusa-auth-provider-api
- description: 'A campaign is a group of promotions that have the same conditions, such as start and end dates. These API routes allow admin users to manage campaigns, their conditions, and promotions that belong to '
  name: Medusa Campaigns API
  slug: medusa-campaigns-api
- description: A cart is a virtual shopping bag that customers can use to add items they want to purchase. A cart is then used to checkout and place an order. These API routes allow customers to create and manage th
  name: Medusa Carts API
  slug: medusa-carts-api
- description: An admin creates a claim for an order when a customer reports that an item is defective or incorrect. Using these API routes, admin users manage order claims, their items, and more.
  name: Medusa Claims API
  slug: medusa-claims-api
- description: A product collection organizes products into a collection for marketing purposes. For example, a summer collection. These API routes allow admin users to manage collections and the products in them.
  name: Medusa Collections API
  slug: medusa-collections-api
- description: 'A store can use unlimited currencies, and each region must be associated with at least one currency. Currencies are defined by the Currency Module. Currency API Routes allow admins to list and update '
  name: Medusa Currencies API
  slug: medusa-currencies-api
- description: Customers can be organized into groups. These groups are useful for segregation and marketing purposes. For example, you can provide different prices for specific customers by creating a price list co
  name: Medusa Customer Groups API
  slug: medusa-customer-groups-api
- description: Customers can either be created when they register through the Store APIs, or created by the admin using the Admin APIs. These API routes allow admin users to manage customers in their store.
  name: Medusa Customers API
  slug: medusa-customers-api
- description: 'A draft order is an order created by the admin user. This is useful for orders created offline or from clients other than a storefront, such as a third-party integration. These API routes allow admin '
  name: Medusa Draft Orders API
  slug: medusa-draft-orders-api
- description: An exchange is the replacement of an item that the customer ordered with another. These API routes allow admin users to create and manage exchanges.
  name: Medusa Exchanges API
  slug: medusa-exchanges-api
- description: Feature flags are used to enable or disable certain features in your Medusa application. These API routes allow admin users to view feature flags.
  name: Medusa Feature Flags API
  slug: medusa-feature-flags-api
- description: A fulfillment provider is a third-party integration or custom logic used to fulfill an order's items. Fulfillment providers are installed as module providers.
  name: Medusa Fulfillment Providers API
  slug: medusa-fulfillment-providers-api
- description: A fulfillment set is a general form or way of fulfillment, such as "shipping" or "pick up". All fulfillment-related configurations in a store are related to a fulfillment set. These API routes allow a
  name: Medusa Fulfillment Sets API
  slug: medusa-fulfillment-sets-api
- description: A fulfillment is created for items in an order, return, exchanges, or claims to deliver items to/from the customer. These API routes allow admin users to manage fulfillments.
  name: Medusa Fulfillments API
  slug: medusa-fulfillments-api
- description: 'A gift card is a prepaid card that can be used to pay for items during checkout. Gift cards can be purchased by customers, or created by admin users. When a gift card is redeemed, its amount is added '
  name: Medusa Gift Cards API
  slug: medusa-gift-cards-api
- description: The Index Module is a tool to perform high-performance queries across modules, for example, to filter linked modules. The Index Module is currently experimental and is hidden behind a feature flag. Le
  name: Medusa Index API
  slug: medusa-index-api
- description: An inventory item is a stock-kept product whose inventory is managed. These API routes allow admin users to manage inventory items.
  name: Medusa Inventory Items API
  slug: medusa-inventory-items-api
- description: An admin can invite new users to manage their team. This allows new users to authenticate as admins and perform admin functionalities. These API routes allow admin users to manage invites.
  name: Medusa Invites API
  slug: medusa-invites-api
- description: An admin can modify the layout of their admin dashboard. This allows admins to customize their dashboard to their preferences and needs. These API routes allow admin users to manage layouts.
  name: Medusa Layouts API
  slug: medusa-layouts-api
- description: A locale is a language that content is translated into for customers to view in a storefront. Medusa installs locales by default. These API routes allow admin users to retrieve and view locales.
  name: Medusa Locales API
  slug: medusa-locales-api
- description: 'Multi-factor authentication (MFA) adds an extra layer of security to admin accounts by requiring additional verification factors during login, such as a TOTP code or a recovery code. These API routes '
  name: Medusa Multi-Factor Authentication API
  slug: medusa-multi-factor-authentication-api
- description: Multi-factor authentication (MFA) factors are additional ways to verify a customer's identity during login, in addition to their password. Examples of MFA factors include authenticator apps, SMS messa
  name: Medusa Multi-Factor Authentication (MFA) Factors API
  slug: medusa-multi-factor-authentication-mfa-factors-api
- description: A notification informs an admin user of store changes or status changes of background tasks. These API routes allow admin users to view and manage notifications.
  name: Medusa Notifications API
  slug: medusa-notifications-api
- description: An order change is a proposed change to an order, such as adding or removing items, changing shipping methods, and more. They can be associated with order edits, claims, or exchanges. These API routes
  name: Medusa Order Changes API
  slug: medusa-order-changes-api
- description: An order edit is a change to an order's details, such as items, shipping methods, and more. Changes made by an order edit are only applied on the order once they're confirmed. The order's previous ver
  name: Medusa Order Edits API
  slug: medusa-order-edits-api
- description: An order is a purchase made by a customer through a storefront. Orders can also originally be created as draft orders. These API routes allow admin users to view and manage orders.
  name: Medusa Orders API
  slug: medusa-orders-api
- description: A payment collection is one or more payments of an order. They're also used for outstanding payments due to order exchanges or claims. Every purchase or request for payment starts with a payment colle
  name: Medusa Payment Collections API
  slug: medusa-payment-collections-api
- description: Each region has a set of payment providers enabled. During checkout, you retrieve the available payment providers in the customer's region to show them to the customer. Customers then choose their pre
  name: Medusa Payment Providers API
  slug: medusa-payment-providers-api
- description: A payment is created when a payment amount is authorized. The payment can then be captured or refunded. A payment is created from the payment session that was authorized, and it belongs to the payment
  name: Medusa Payments API
  slug: medusa-payments-api
- description: A plugin is a package of reusable Medusa customizations that you can install in any Medusa application. Plugins can be used to add new functionality, such as wishlists, or integrate third-party servic
  name: Medusa Plugins API
  slug: medusa-plugins-api
- description: 'A price list is a group of prices applied if the specified conditions and rules are satisfied. Price lists are useful for sales or special prices for special conditions, such as applying prices for a '
  name: Medusa Price Lists API
  slug: medusa-price-lists-api
- description: A price preference is used to specify whether tax-inclusiveness is enabled for a context, such as a region or currency code. These API routes allow admin users to manage whether a region or currency i
  name: Medusa Price Preferences API
  slug: medusa-price-preferences-api
- description: Products can be categorized into categories. Categories are nested and their heirarchy can be managed, giving admin users flexibility in how they categorize their products. These API routes allow admi
  name: Medusa Product Categories API
  slug: medusa-product-categories-api
- description: A product option is a way to define different options for a product, such as "Size" or "Color". Product options can be created globally and used by multiple products, or they can be exclusive to a spe
  name: Medusa Product Options API
  slug: medusa-product-options-api
- description: A tag is another way of organizing a product. Each tag has a name and a value. Products are organized into the same tag if they have the same value. These API routes allow admin users to manage produc
  name: Medusa Product Tags API
  slug: medusa-product-tags-api
- description: Products can be organized into types. Each type has a name and a value. Products are organized into the same type if they have the same value. These API routes allow admin users to manage product type
  name: Medusa Product Types API
  slug: medusa-product-types-api
- description: A product variant is a saleable form of the product. Each variant has different option values. For example, a "Shirt" product may have a "Blue" variant and a "Green" variant. Customers choose from the
  name: Medusa Product Variants API
  slug: medusa-product-variants-api
- description: 'A product is a set of variants that the customer chooses from when making a purchase. A product can be organized into categories or collections. A product can have many options, and variants for each '
  name: Medusa Products API
  slug: medusa-products-api
- description: 'A promotion discounts an amount or percentage off a cart''s items, shipping methods, or the entire order. Promotions have different types, such as a `standard` promotion that just discounts an amount, '
  name: Medusa Promotions API
  slug: medusa-promotions-api
- description: The Property Labels API from Medusa — 3 operation(s) for property labels.
  name: Medusa Property Labels API
  slug: medusa-property-labels-api
- description: A refund reason is a possible reason used when issuing a refund to the customer, such as when returning an item and refunding the customer. These API routes allow admin users to manage refund reasons.
  name: Medusa Refund Reasons API
  slug: medusa-refund-reasons-api
- description: Regions are different countries or geographical regions that the commerce store serves customers in. These API routes allow admin users to manage regions, their providers, and more.
  name: Medusa Regions API
  slug: medusa-regions-api
- description: A reservation is unavailable quantity of an inventory item in a location. A reservation is created automatically for variants in an order whose `manage_inventory` is enabled. Admin users can also crea
  name: Medusa Reservations API
  slug: medusa-reservations-api
- description: A return reason is a possible reason that an item is returned from the customer, such as when returning an item. These API routes allow admin users to manage return reasons.
  name: Medusa Return Reasons API
  slug: medusa-return-reasons-api
- description: Admin users create a return when a customer returns an item to them. Returns can also be created by customers through the storefront, and admins will be able to manage them and make refunds, if necess
  name: Medusa Returns API
  slug: medusa-returns-api
- description: A sales channel indicates a channel where products can be sold in. For example, a webshop or a mobile app. These API routes allow admins to manage sales channels and the products available in them.
  name: Medusa Sales Channels API
  slug: medusa-sales-channels-api
- description: The Search API from Medusa — 1 operation(s) for search.
  name: Medusa Search API
  slug: medusa-search-api
- description: Shipping option types define a group of shipping options with shared shipping characterstics. For example, you may have "Standard" and "Express" shipping option types. These API routes allow admins to
  name: Medusa Shipping Option Types API
  slug: medusa-shipping-option-types-api
- description: A shipping option is a way of shipping an item to or from the customer. Shipping options are associated with the fulfillment provider used to handle their fulfillment. Shipping options can be restrict
  name: Medusa Shipping Options API
  slug: medusa-shipping-options-api
- description: A shipping profile defines a type of items that are shipping in a similar manner. For example, digital products may have a `digital` shipping profile. These API routes allow admin users to manage ship
  name: Medusa Shipping Profiles API
  slug: medusa-shipping-profiles-api
- description: A stock location is where stock-kept items (products) are kept. Stock locations are linked to fulfillment providers used to fulfill items from this location. A stock location is also link to a fulfill
  name: Medusa Stock Locations API
  slug: medusa-stock-locations-api
- description: A store credit account is a ledger of store credit transactions for a customer. They hold the customer's store credit balance, including their credit and debit amounts. Store credit accounts allow you
  name: Medusa Store Credit Accounts API
  slug: medusa-store-credit-accounts-api
- description: 'A store holds the main configuration and information of your commerce store, such as supported currencies or default sales channel. By default, the Medusa application has one default store. There are '
  name: Medusa Stores API
  slug: medusa-stores-api
- description: A tax provider is a third-party integration or custom logic used to calculate taxes for a cart or an order. These API routes allow admin users to manage tax providers installed in their Medusa applica
  name: Medusa Tax Providers API
  slug: medusa-tax-providers-api
- description: A tax rate is a percentage amount used to calculate the tax amount of each taxable item's price, such as line items or shipping methods. Each tax region has a default tax rate. You can create tax rate
  name: Medusa Tax Rates API
  slug: medusa-tax-rates-api
- description: A tax region is a region's tax settings. It has tax rates and rules. So, after you create a region, you must create a tax region for it. A tax region can extend settings from a parent tax region. Thes
  name: Medusa Tax Regions API
  slug: medusa-tax-regions-api
- description: 'A translation is a localized version of content in a specific locale. For example, a product description in French. These API routes allow admin users to manage translations for different locales and '
  name: Medusa Translations API
  slug: medusa-translations-api
- description: 'Use these API routes to upload files to your Medusa application using the installed file module provider. You can upload public files, such as product images, or private files, such as CSV files used '
  name: Medusa Uploads API
  slug: medusa-uploads-api
- description: A user is an admin user that can authenticate and perform functionalities as an admin user. An admin user can invite other users to join their team. Once they accept the invite, they'll become admin u
  name: Medusa Users API
  slug: medusa-users-api
- description: A view configuration is a saved data-table view for an entity, such as products or orders. It lets admin users customize how a table shows its data, then save that customization as a reusable view. Th
  name: Medusa Views API
  slug: medusa-views-api
- description: These API routes allow you to track workflow executions in your Medusa application. Depending on the workflow engine you use, executions may only be retained for a short while, or only until the Medus
  name: Medusa Workflows Executions API
  slug: medusa-workflows-executions-api
artifact_total: 74
asyncapis:
- description: ''
  name: Medusa Events
  slug: medusa-events
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/medusa-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/medusa-store-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/medusa-admin-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://medusajs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.medusajs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.medusajs.com/learn
- group: docs
  title: ''
  type: APIReference
  url: https://docs.medusajs.com/api/store
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.medusajs.com/learn/installation
- group: operate
  title: ''
  type: Support
  url: https://medusajs.com/contact/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/medusajs
- group: company
  title: ''
  type: Blog
  url: https://medusajs.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/medusajs
- group: commercial
  title: ''
  type: Pricing
  url: https://medusajs.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.medusajs.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://medusajs.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://medusajs.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.medusajs.com
- group: auth
  title: ''
  type: Security
  url: https://github.com/medusajs/medusa/security/policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medusa-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/medusa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/medusa-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/medusa-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/medusa-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/medusa-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/medusa-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/medusa-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/medusa-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/medusa-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/medusa-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/medusa-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medusa-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/medusa-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/medusa-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/medusa-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/medusa-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/medusa-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/medusa-cli.yml
- group: design
  title: ''
  type: Components
  url: components/medusa-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/medusa-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/medusa-events.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/medusa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/medusa-rate-limits.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/medusa-graphql.md
created: '2026-07-22'
description: 'Medusa is an open-source, MIT-licensed digital commerce platform built around a modular architecture: a suite of Commerce Modules (cart, products, orders, pricing, promotions, tax, inventory, fulfillment, payment), a Framework for building custom API routes, data models, workflows and integrations, and a customizable Medusa Admin dashboard. Medusa ships two first-party REST APIs — a Store API for storefronts and an Admin API for merchant operations — both documented with published OpenAPI 3.0 specifications generated from the codebase. Medusa is self-hosted by default; MedusaJS, Inc. also operates Medusa Cloud, a managed PaaS, and a remote MCP server plus published Claude Code agent skills for agentic development.'
graphqls:
- description: Medusa is an open-source headless commerce platform with a modular architecture that enables developers to build custom commerce applications. The GraphQL API exposes the full store surface for buildi
  name: Medusa GraphQL API
  slug: medusa-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medusa.png
layout: provider
mcp_servers:
- description: 'Medusa operates one official MCP server. It is REMOTE ONLY — a Streamable HTTP endpoint at https://docs.medusajs.com/mcp. There is no npm/stdio package: @medusajs/mcp does not exist on npm (404, check'
  name: Medusa MCP Server
  slug: medusa-mcp-server
modified: '2026-08-26'
name: Medusa
nav: Providers
network: true
overview: 'Medusa publishes 63 APIs on the [APIs.io](https://apis.io/) network, including Api Keys API, Auth API, [auth Provider] API, and 60 more. Tagged areas include E-Commerce, Headless Commerce, Open-Source, Commerce, and Storefront.


  The Medusa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Medusa''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Medusa Plans Pricing
  plan_count: 4
  slug: medusa-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Medusa Rate Limits
  slug: medusa-rate-limits
scopes:
- name: Medusa Scopes
  scope_count: 0
  slug: medusa-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.0
  coverage:
    artifact_dirs: 26
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 59.2
    developer_ergonomics: 85.7
    discoverability: 70.4
    governance: 4.5
    operational_transparency: 60.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 60.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medusa/refs/heads/main/screenshots/medusa-2026-08-07T172412.png
security:
- kind: authentication
  name: Medusa Authentication
  slug: medusa-authentication
  summary_line: http/apiKey · 4 schemes
- kind: domain-security
  name: Medusa Domain Security
  slug: medusa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Medusa Vulnerability Disclosure
  slug: medusa-vulnerability-disclosure
  summary_line: disclosure policy published
slug: medusa
tags:
- E-Commerce
- Headless Commerce
- Open-Source
- Commerce
- Storefront
- Order Management
- Node.js
- GraphQL
- Agentic Commerce
- MCP
website: https://medusajs.com/
---
