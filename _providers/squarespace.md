---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 45
  human_in_the_loop: 0
  name: Squarespace Agentic Access
  operation_count: 83
  slug: squarespace-agentic-access
  summary_line: 83 operations · 45 acting
api_count: 2
apis:
- baseURL: https://api.squarespace.com
  baseurl_source: spec
  description: The Squarespace Orders API provides access to order history for a Squarespace merchant site, supporting both one-time purchases and subscription orders. Developers can retrieve, create, and manage ord
  name: Squarespace Orders API
  phrasing_intents:
  - id: getOrders
    intent: List and filter orders (1.0)
    question: How do I list orders for one customer with the versioned 1.0 orders API?
  - id: createOrder
    intent: Import a third-party channel order (1.0)
    question: How do I import an order placed on another sales channel into my store through the 1.0 API?
  - id: getOrder
    intent: Get one order (1.0)
    question: How do I look up a single order by ID on the versioned 1.0 API?
  - id: fulfillOrder
    intent: Mark an order fulfilled (1.0)
    question: How do I mark an order as shipped with the 1.0 fulfillment endpoint?
  - id: listOrders
    intent: List orders (unversioned)
    question: Which orders were updated recently, via the unversioned orders path?
  - id: postCommerceOrders
    intent: Import an order (unversioned)
    question: Does importing an order through the unversioned path charge the customer's card?
  - id: getCommerceOrdersByOrderId
    intent: Get one order (unversioned)
    question: Can I see the line items, addresses and payment details of an order via the unversioned path?
  - id: postCommerceOrdersByOrderIdFulfillments
    intent: Fulfill line items with tracking (unversioned)
    question: How do I add tracking numbers when fulfilling an order via the unversioned path?
  phrasing_ops: 8
  slug: squarespace-orders-api
- baseURL: https://api.squarespace.com
  baseurl_source: spec
  description: The Squarespace Products API allows developers to manage the product catalog of a Squarespace merchant site. It supports physical products, service products, gift cards, and digital downloads, along w
  name: Squarespace Products API
  phrasing_intents:
  - id: getProducts
    intent: List and search products (v2)
    question: How do I list all products of one type with the v2 products API?
  - id: createProduct
    intent: Create a product (v2)
    question: How do I add a new product to my store with the v2 products API?
  - id: getSpecificProducts
    intent: Get specific products by ID (v2)
    question: How do I fetch a handful of products, with variants and images, by ID on v2?
  - id: deleteProduct
    intent: Delete a product (v2)
    question: How do I delete a product with the v2 products API?
  - id: updateProduct
    intent: Update a product's details (v2)
    question: How do I hide a product from my storefront with the v2 API?
  - id: uploadProductImage
    intent: Upload a product image (v2)
    question: How do I upload a photo for a product with the v2 API?
  - id: deleteProductImage
    intent: Delete a product image (v2)
    question: How do I delete one image from a product with the v2 API?
  - id: updateProductImage
    intent: Update a product image's alt text (v2)
    question: How do I change the alt text on a product image with v2?
  phrasing_ops: 25
  slug: squarespace-products-api
- baseURL: https://api.squarespace.com
  baseurl_source: spec
  description: The Squarespace Inventory API enables developers to retrieve and update inventory quantities for product variants on a Squarespace merchant site. It supports bulk inventory queries and individual vari
  name: Squarespace Inventory API
  phrasing_intents:
  - id: getInventoryItems
    intent: List stock levels via the 1.0 inventory endpoint
    question: How do I pull current stock levels for every variant using the versioned 1.0 inventory API?
  - id: adjustInventoryStockLevels
    intent: Add, subtract, set or unlimit stock (1.0)
    question: How do I set an exact stock count for a variant rather than adjusting it up or down?
  - id: getSpecificInventoryItems
    intent: Get stock for specific variants (1.0)
    question: How do I check stock for just a few variant IDs on the versioned 1.0 endpoint?
  - id: listInventory
    intent: List stock for all variants (unversioned)
    question: What stock does every product variant in my shop have right now, via the unversioned inventory path?
  - id: getInventoryByVariants
    intent: Get stock for specific variants (unversioned)
    question: Can I check stock for up to 50 variants without paging, via the unversioned path?
  - id: adjustInventory
    intent: Apply relative stock increments (unversioned)
    question: How do I bump stock up or down by a relative amount for several variants at once?
  phrasing_ops: 6
  slug: squarespace-inventory-api
- baseURL: https://api.squarespace.com
  baseurl_source: spec
  description: The Squarespace Profiles API allows reading customer profiles, mailing list subscribers, and donors for a Squarespace site. It supports filtering by profile type and retrieving individual profile deta
  name: Squarespace Profiles API
  phrasing_intents:
  - id: getProfiles
    intent: List and sort profiles (1.0)
    question: How do I list customer profiles sorted by last name using the versioned 1.0 API?
  - id: getSpecificProfiles
    intent: Get specific profiles by ID (1.0)
    question: How do I fetch several profiles at once by their IDs on the 1.0 endpoint?
  - id: listProfiles
    intent: List customers, subscribers and donors (unversioned)
    question: Which of my site's profiles are customers, via the unversioned profiles path?
  - id: getProfilesByProfileIds
    intent: Get specific profiles by ID (unversioned)
    question: How do I retrieve particular profiles by ID without the 1.0 prefix?
  phrasing_ops: 4
  slug: squarespace-profiles-api
- baseURL: https://api.squarespace.com
  baseurl_source: spec
  description: The Squarespace Transactions API provides access to financial transaction records for a Squarespace merchant site. Developers can retrieve transaction history, including payment amounts, fees, and ass
  name: Squarespace Transactions API
  phrasing_intents:
  - id: getDocumentsByUpdatedOn
    intent: List transaction documents (1.0)
    question: How do I list payment transactions for orders and donations on the versioned 1.0 API?
  - id: getDocumentsById
    intent: Get transaction documents by ID (1.0)
    question: How do I fetch specific transaction documents by ID with the 1.0 endpoint?
  - id: listTransactions
    intent: List transaction documents (unversioned)
    question: What financial transactions happened on my site in a date range, via the unversioned path?
  - id: getTransactions
    intent: Get transaction documents by ID (unversioned)
    question: What gateway data and totals are on a specific transaction document, via the unversioned path?
  phrasing_ops: 4
  slug: squarespace-transactions-api
- baseURL: https://api.squarespace.com/1.0
  baseurl_source: spec
  description: The Squarespace Webhook Subscriptions API allows developers to manage webhook endpoint subscriptions for a merchant site. It supports creating, listing, updating, and deleting subscriptions that trigg
  name: Squarespace Webhook Subscriptions API
  phrasing_intents:
  - id: listWebhookSubscriptions
    intent: List webhook subscriptions
    question: Which webhook endpoints are currently subscribed on my site?
  - id: createWebhookSubscription
    intent: Subscribe an endpoint to webhook events
    question: How do I get notified at my own URL when store events happen on Squarespace?
  - id: getWebhookSubscription
    intent: Get one webhook subscription
    question: What endpoint URL and topics does a specific webhook subscription use?
  - id: updateWebhookSubscription
    intent: Change a webhook's endpoint or topics
    question: How do I point an existing webhook subscription at a new URL?
  - id: deleteWebhookSubscription
    intent: Delete a webhook subscription
    question: How do I stop receiving webhook notifications at an endpoint?
  - id: sendTestNotification
    intent: Send a test webhook notification
    question: How can I check that my webhook endpoint is reachable before live events arrive?
  - id: rotateWebhookSecret
    intent: Rotate a webhook subscription's secret
    question: How do I generate a new signing secret if my webhook secret may have leaked?
  - id: getWebhookSubscriptions
    intent: List webhook subscriptions (1.0)
    question: Which webhook subscriptions exist on my site through the 1.0 API?
  phrasing_ops: 14
  slug: squarespace-webhook-subscriptions-api
- baseURL: https://api.squarespace.com/1.0
  baseurl_source: spec
  description: Basic site information and metadata
  name: Squarespace Site API
  phrasing_intents:
  - id: retrieveSiteInfo
    intent: Look up the site behind my credentials
    question: Which Squarespace website is my API key connected to?
  phrasing_ops: 1
  slug: squarespace-site-api
- description: Squarespace operates a first-party remote MCP server at https://mcp.squarespace.com/mcp. It answers an unauthenticated JSON-RPC tools/list with HTTP 200 and exposes two tools with full JSON Schema inp
  name: Squarespace MCP Server
  slug: squarespace-mcp
- baseURL: https://api.squarespace.com
  baseurl_source: spec
  description: Query analytics for a website
  name: Squarespace Analytics API
  phrasing_intents:
  - id: getTransactionsSummaries
    intent: Summarize transactions for a set of contacts
    question: How much has each of my Squarespace contacts spent in total?
  phrasing_ops: 1
  slug: squarespace-analytics-api
- baseURL: https://api.squarespace.com
  baseurl_source: spec
  description: 'Manage customer contacts and address book entries for a website: create, read, update, delete, and query contacts; maintain addresses for shipping and fulfillment.'
  name: Squarespace Contacts API
  phrasing_intents:
  - id: getContacts
    intent: List the contacts on my website
    question: How do I list every contact stored for my Squarespace site?
  - id: createContact
    intent: Add a new contact
    question: How do I add a new person to my site's contact list?
  - id: queryContacts
    intent: Search and filter contacts
    question: Which contacts have placed more than a certain number of orders?
  - id: deleteContact
    intent: Delete a contact
    question: How do I remove a contact from my site entirely?
  - id: getContact
    intent: Get one contact's details
    question: How can I pull up the full record for a single contact by ID?
  - id: patchContact
    intent: Update a contact's name, email or locale
    question: How do I change the email address on an existing contact?
  - id: getAddressBook
    intent: List a contact's saved addresses
    question: Which addresses are saved in a contact's address book?
  - id: createAddressBookEntry
    intent: Add an address to a contact's address book
    question: How do I save a new shipping address for a contact?
  phrasing_ops: 11
  slug: squarespace-contacts-api
- baseURL: https://api.squarespace.com
  baseurl_source: spec
  description: Manage discounts for a website.
  name: Squarespace Discounts API
  phrasing_intents:
  - id: listDiscounts
    intent: List and filter discounts
    question: Which discounts are currently active on my store?
  - id: createDiscount
    intent: Create a discount or promo code
    question: How do I set up a new promo code for my Squarespace store?
  - id: deleteDiscount
    intent: Delete a discount
    question: How do I get rid of a discount I no longer want?
  - id: getDiscount
    intent: Get one discount's details
    question: How do I look up the settings of a single discount by its ID?
  - id: updateDiscount
    intent: Replace an existing discount's settings
    question: How do I extend the expiry date on a discount I already created?
  - id: getFulfillmentOptions
    intent: List fulfillment options usable with discounts
    question: Which shipping options and carrier services can a discount apply to?
  phrasing_ops: 6
  slug: squarespace-discounts-api
- baseURL: https://api.squarespace.com
  baseurl_source: spec
  description: The Websites API from Squarespace — 3 operation(s) for websites.
  name: Squarespace Websites API
  phrasing_intents:
  - id: getMemberProfile
    intent: Look up the member who owns my OAuth token
    question: Which Squarespace member account does my OAuth token belong to?
  - id: getWebsiteProfile
    intent: Look up the website that owns my key or token
    question: What website is my API key or OAuth token issued for?
  - id: getStorePages
    intent: List the store pages on my website
    question: Which store pages exist on my website?
  phrasing_ops: 3
  slug: squarespace-websites-api
artifact_total: 47
asyncapis:
- description: The Squarespace webhook system delivers real-time event notifications to registered endpoint URLs when commerce activity occurs on a merchant site. Supported events include order creation, order updat
  name: Squarespace Webhook Events
  slug: squarespace-webhooks-asyncapi
collections:
- collection_type: open
  name: Squarespace Commerce API
  slug: open-squarespace-commerce-api
- collection_type: open
  name: Squarespace Commerce Inventory API
  slug: open-squarespace-inventory-api
- collection_type: open
  name: Squarespace Commerce Inventory Orders API
  slug: open-squarespace-orders-api
- collection_type: open
  name: Squarespace Commerce Inventory Products API
  slug: open-squarespace-products-api
- collection_type: open
  name: Squarespace Commerce Inventory Profiles API
  slug: open-squarespace-profiles-api
- collection_type: open
  name: Squarespace Commerce Inventory Site API
  slug: open-squarespace-site-api
- collection_type: open
  name: Squarespace Commerce Inventory Transactions API
  slug: open-squarespace-transactions-api
- collection_type: open
  name: Squarespace Commerce Inventory Webhook Subscriptions API
  slug: open-squarespace-webhook-subscriptions-api
common:
- group: other
  href: https://artifacts.apis.io/squarespace/vendor-facets/squarespace-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/squarespace-vendor-facets.yml
- group: other
  href: https://artifacts.apis.io/squarespace/capabilities/squarespace-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/squarespace-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/squarespace/overlays/squarespace-commerce-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/squarespace-commerce-api-v2-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/squarespace/agentic-access/squarespace-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/squarespace-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/squarespace/security/squarespace-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/squarespace-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/squarespace/security/squarespace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/squarespace-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/squarespace/authentication/squarespace-authentication.yml
  title: ''
  type: Authentication
  url: authentication/squarespace-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/squarespace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/squarespace
- group: company
  title: ''
  type: Website
  url: https://www.squarespace.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.squarespace.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.squarespace.com/commerce-apis/overview
- group: auth
  title: ''
  type: APIKeys
  url: https://support.squarespace.com/hc/en-us/articles/236297987-Squarespace-API-keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.squarespace.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.squarespace.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.squarespace.com
- group: company
  title: ''
  type: Blog
  url: https://www.squarespace.com/blog
- group: auth
  href: https://artifacts.apis.io/squarespace/security/squarespace-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/squarespace-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/squarespace/security/squarespace-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/squarespace-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/squarespace/well-known/squarespace-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/squarespace-well-known.yml
- group: auth
  href: https://artifacts.apis.io/squarespace/well-known/squarespace-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/squarespace-security.txt
- group: agent
  href: https://artifacts.apis.io/squarespace/llms/squarespace-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/squarespace-llms.txt
- group: agent
  href: https://artifacts.apis.io/squarespace/mcp/squarespace-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/squarespace-mcp.yml
- group: build
  href: https://artifacts.apis.io/squarespace/mcp/squarespace-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/squarespace-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/squarespace/packages/squarespace-packages.yml
  title: ''
  type: Packages
  url: packages/squarespace-packages.yml
- group: design
  href: https://artifacts.apis.io/squarespace/conventions/squarespace-conventions.yml
  title: ''
  type: Conventions
  url: conventions/squarespace-conventions.yml
- group: design
  href: https://artifacts.apis.io/squarespace/conventions/squarespace-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/squarespace-conventions.yml
- group: design
  href: https://artifacts.apis.io/squarespace/errors/squarespace-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/squarespace-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/squarespace/scopes/squarespace-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/squarespace-scopes.yml
- group: design
  href: https://artifacts.apis.io/squarespace/conformance/squarespace-conformance.yml
  title: ''
  type: Conformance
  url: conformance/squarespace-conformance.yml
- group: design
  href: https://artifacts.apis.io/squarespace/lifecycle/squarespace-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/squarespace-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/squarespace/lifecycle/squarespace-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/squarespace-lifecycle.yml
- group: design
  title: ''
  type: Versioning
  url: https://developers.squarespace.com/commerce-apis/versioning
- group: design
  href: https://artifacts.apis.io/squarespace/data-model/squarespace-data-model.yml
  title: ''
  type: DataModel
  url: data-model/squarespace-data-model.yml
- group: operate
  href: https://artifacts.apis.io/squarespace/changelog/squarespace-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/squarespace-changelog.yml
- group: agent
  href: https://artifacts.apis.io/squarespace/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/squarespace/plans/squarespace-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/squarespace-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/squarespace/rate-limits/squarespace-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/squarespace-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/squarespace/finops/squarespace-finops.yml
  title: ''
  type: FinOps
  url: finops/squarespace-finops.yml
- group: docs
  href: https://artifacts.apis.io/squarespace/asyncapi/squarespace-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/squarespace-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/squarespace/asyncapi/squarespace-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/squarespace-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developers.squarespace.com/commerce-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.squarespace.com/quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.squarespace.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.squarespace.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://login.squarespace.com
- group: auth
  title: ''
  type: OAuth
  url: https://developers.squarespace.com/oauth
- group: operate
  title: ''
  type: FAQ
  url: https://developers.squarespace.com/commerce-apis/faq
- group: other
  title: ''
  type: Glossary
  url: https://developers.squarespace.com/commerce-apis/glossary
created: '2026-05-02'
description: Squarespace is an all-in-one website building and e-commerce platform that enables individuals and businesses to create, manage, and scale their online presence. Squarespace provides a suite of Commerce APIs for developers to build integrations managing products, orders, inventory, customer profiles, transactions, and webhook notifications. All APIs use HTTPS REST conventions with API key or OAuth authentication.
examples:
- key_count: 4
  name: Squarespace List Orders Example
  slug: squarespace-list-orders-example
- key_count: 4
  name: Squarespace List Products Example
  slug: squarespace-list-products-example
finops:
- has_sources: true
  method: derived
  name: Squarespace Finops
  primary_unit: site
  service_category: ''
  slug: squarespace-finops
  template: false
image: https://static1.squarespace.com/static/ta/5134cbefe4b0c6fb04df8065/10007/assets/logomark.svg
json_schemas:
- name: Squarespace Order
  property_count: 17
  slug: squarespace-order
- name: Squarespace Product
  property_count: 13
  slug: squarespace-product
- name: Squarespace Webhook Notification
  property_count: 6
  slug: squarespace-webhook-notification
json_structures:
- name: Squarespace Order Structure
  property_count: 0
  slug: squarespace-order-structure
- name: Squarespace Product Structure
  property_count: 0
  slug: squarespace-product-structure
jsonld:
- class_count: 0
  name: Squarespace Context
  property_count: 12
  slug: squarespace-context
layout: provider
mcp_servers:
- description: Squarespace operates a first-party REMOTE MCP server at https://mcp.squarespace.com/mcp. It answers an unauthenticated JSON-RPC tools/list with HTTP 200 and returns two real tools with full JSON Schem
  name: Squarespace MCP Server
  slug: squarespace-mcp-server
modified: '2026-08-13'
name: Squarespace
nav: Providers
network: true
overview: 'Squarespace publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Orders API, Products API, Inventory API, and 9 more. Tagged areas include Commerce, E-Commerce, Marketing, Payments, and Retail.


  The Squarespace catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Squarespace''s developer surface includes authentication, documentation, engineering blog, changelog, API reference, getting-started guide, support, and 42 more developer resources.'
plans:
- name: Squarespace Plans Pricing
  plan_count: 4
  slug: squarespace-plans-pricing
- name: Squarespace Price Estimates
  plan_count: 0
  slug: squarespace-price-estimates
random_paper: 5
rate_limits:
- limit_count: 2
  name: Squarespace Rate Limits
  slug: squarespace-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Squarespace — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: squarespace-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Squarespace — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: squarespace-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Squarespace API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 7
  slug: squarespace-rules
scopes:
- name: Squarespace Scopes
  scope_count: 11
  slug: squarespace-scopes
  summary_line: 11 scopes · authorization_code
score:
  band: exemplar
  composite: 69.9
  coverage:
    artifact_dirs: 36
    catalog_earned: 64.0
    catalog_earned_first_party: 20.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 67.0
    developer_ergonomics: 58.9
    discoverability: 60.0
    operational_transparency: 81.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 69.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 41.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/squarespace/squarespace-2026-06-20T194430.png
security:
- kind: authentication
  name: Squarespace Authentication
  slug: squarespace-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Squarespace Domain Security
  slug: squarespace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Squarespace Vulnerability Disclosure
  slug: squarespace-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Squarespace Trust Center
  slug: squarespace-trust-center
  summary_line: named, note
skill_count: 4
skills:
- name: squarespace-import-order
  slug: squarespace-import-order
- name: squarespace-migrate-profiles-to-contacts
  slug: squarespace-migrate-profiles-to-contacts
- name: squarespace-subscribe-webhooks
  slug: squarespace-subscribe-webhooks
- name: squarespace-sync-inventory
  slug: squarespace-sync-inventory
slug: squarespace
tags:
- Commerce
- E-Commerce
- Marketing
- Payments
- Retail
- Website Builder
- Webhook
website: https://www.squarespace.com
---
