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
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Advance Auto Parts Agentic Access
  operation_count: 14
  slug: advance-auto-parts-agentic-access
  summary_line: 14 operations · 2 acting
api_count: 2
apis:
- baseURL: https://api.advanceautoparts.com/v1
  baseurl_source: declared
  description: Shopping cart management
  name: Advance Auto Parts Cart API
  slug: advance-auto-parts-cart-api
- baseURL: https://api.advanceautoparts.com/v1
  baseurl_source: declared
  description: Store and warehouse inventory
  name: Advance Auto Parts Inventory API
  slug: advance-auto-parts-inventory-api
- baseURL: https://api.advanceautoparts.com/v1
  baseurl_source: declared
  description: Speed Perks loyalty program
  name: Advance Auto Parts Loyalty API
  slug: advance-auto-parts-loyalty-api
- baseURL: https://api.advanceautoparts.com/v1
  baseurl_source: declared
  description: Order placement and management
  name: Advance Auto Parts Orders API
  slug: advance-auto-parts-orders-api
- baseURL: https://api.advanceautoparts.com/v1
  baseurl_source: declared
  description: Parts and product catalog
  name: Advance Auto Parts Products API
  slug: advance-auto-parts-products-api
- baseURL: https://api.advanceautoparts.com/v1
  baseurl_source: declared
  description: Store locations and availability
  name: Advance Auto Parts Stores API
  slug: advance-auto-parts-stores-api
- baseURL: https://api.advanceautoparts.com/v1
  baseurl_source: declared
  description: Vehicle year/make/model lookup and fitment
  name: Advance Auto Parts Vehicles API
  slug: advance-auto-parts-vehicles-api
artifact_total: 112
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Advance Auto Parts Catalog Cart API
  slug: open-advance-auto-parts-cart-api
- collection_type: open
  name: Advance Auto Parts Catalog API
  slug: open-advance-auto-parts-catalog-api
- collection_type: open
  name: Advance Auto Parts Commerce API
  slug: open-advance-auto-parts-commerce-api
- collection_type: open
  name: Advance Auto Parts Catalog Cart Inventory API
  slug: open-advance-auto-parts-inventory-api
- collection_type: open
  name: Advance Auto Parts Catalog Cart Loyalty API
  slug: open-advance-auto-parts-loyalty-api
- collection_type: open
  name: Advance Auto Parts Catalog Cart Orders API
  slug: open-advance-auto-parts-orders-api
- collection_type: open
  name: Advance Auto Parts Catalog Cart Products API
  slug: open-advance-auto-parts-products-api
- collection_type: open
  name: Advance Auto Parts Catalog Cart Stores API
  slug: open-advance-auto-parts-stores-api
- collection_type: open
  name: Advance Auto Parts Catalog Cart Vehicles API
  slug: open-advance-auto-parts-vehicles-api
common:
- group: build
  title: ''
  type: Packages
  url: packages/advance-auto-parts-packages.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/advance-auto-parts-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/advance-auto-parts-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/advance-auto-parts-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/advance-auto-parts-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advance-auto-parts-llms.txt
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/advance-auto-parts-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/advance-auto-parts-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advance-auto-parts-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/advance-auto-parts-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/advance-auto-parts-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdvanceAutoParts
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/advance-auto-parts
- group: company
  title: ''
  type: Website
  url: https://www.advanceautoparts.com
- group: start
  title: ''
  type: Portal
  url: https://www.advanceautoparts.com/i/help
- group: operate
  title: ''
  type: Support
  url: https://www.advanceautoparts.com/i/help/customer-service
- group: company
  title: ''
  type: Blog
  url: https://www.advanceautoparts.com/gearhead
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.advanceautoparts.com/i/policies/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.advanceautoparts.com/i/policies/privacy
- group: start
  title: ''
  type: Login
  url: https://www.advanceautoparts.com/myaccount/login
- group: start
  title: ''
  type: Signup
  url: https://www.advanceautoparts.com/myaccount/register
coverage:
  checked: '2026-08-30'
  detail: 'Every Advance Auto Parts integration surface sits behind an account: the supplier portal at supplier.advanceautoparts.com/ords redirects all data paths to a login, the Advance Professional shop-management-system order integration page at my.advancepro.com renders client-side inside a Salesforce community with no public API reference, and the declared API host api.advanceautoparts.com answers HTTP 503 "DNS failure" from the Akamai edge with no origin behind it.'
  evidence:
  - status: 503
    url: https://api.advanceautoparts.com/openapi.json
  - status: 302
    url: https://supplier.advanceautoparts.com/ords/_/db-api/stable/apex/workspaces/
  - status: 200
    url: https://my.advancepro.com/service/s/apro-sms-order-integration-page?language=en_US
  - status: 200
    url: https://www.advanceautoparts.com/llms.txt
  reason: partner-login
  state: gated
created: '2024-01-01'
description: Advance Auto Parts is a leading automotive aftermarket parts retailer offering a comprehensive catalog of automotive parts, accessories, batteries, and maintenance items. The company serves both professional automotive technicians and do-it-yourself customers across North America through retail stores, online, and commercial delivery programs.
examples:
- key_count: 2
  name: Catalog Api Errorresponse Example
  slug: catalog-api-errorresponse-example
- key_count: 2
  name: Catalog Api Inventoryresult Example
  slug: catalog-api-inventoryresult-example
- key_count: 2
  name: Catalog Api Make Example
  slug: catalog-api-make-example
- key_count: 1
  name: Catalog Api Makelist Example
  slug: catalog-api-makelist-example
- key_count: 1
  name: Catalog Api Modellist Example
  slug: catalog-api-modellist-example
- key_count: 8
  name: Catalog Api Product Example
  slug: catalog-api-product-example
- key_count: 2
  name: Catalog Api Productlist Example
  slug: catalog-api-productlist-example
- key_count: 6
  name: Catalog Api Store Example
  slug: catalog-api-store-example
- key_count: 4
  name: Catalog Api Storeinventory Example
  slug: catalog-api-storeinventory-example
- key_count: 1
  name: Catalog Api Storelist Example
  slug: catalog-api-storelist-example
- key_count: 2
  name: Catalog Api Vehiclemodel Example
  slug: catalog-api-vehiclemodel-example
- key_count: 1
  name: Catalog Api Yearlist Example
  slug: catalog-api-yearlist-example
- key_count: 3
  name: Commerce Api Cart Example
  slug: commerce-api-cart-example
- key_count: 3
  name: Commerce Api Cartitem Example
  slug: commerce-api-cartitem-example
- key_count: 2
  name: Commerce Api Cartiteminput Example
  slug: commerce-api-cartiteminput-example
- key_count: 5
  name: Commerce Api Loyaltyaccount Example
  slug: commerce-api-loyaltyaccount-example
- key_count: 5
  name: Commerce Api Loyaltytransaction Example
  slug: commerce-api-loyaltytransaction-example
- key_count: 1
  name: Commerce Api Loyaltytransactionlist Example
  slug: commerce-api-loyaltytransactionlist-example
- key_count: 5
  name: Commerce Api Order Example
  slug: commerce-api-order-example
- key_count: 4
  name: Commerce Api Orderinput Example
  slug: commerce-api-orderinput-example
- key_count: 2
  name: Commerce Api Orderlist Example
  slug: commerce-api-orderlist-example
features:
- description: Look up compatible parts by year, make, model, engine, and trim for accurate fitment verification.
  name: Vehicle Fitment Search
- description: Check part availability and quantity at nearby stores and distribution centers in real time.
  name: Real-Time Inventory
- description: Access a comprehensive catalog of millions of SKUs including OEM and aftermarket parts, accessories, and fluids.
  name: Parts Catalog Access
- description: Manage commercial accounts, purchase orders, net terms, and invoice history for professional installers.
  name: Commercial Account Management
- description: Query and apply Speed Perks loyalty points for purchases and track reward status.
  name: Speed Perks Loyalty Integration
- description: Order parts for same-day delivery or in-store pickup with real-time availability confirmation.
  name: Same-Day Delivery and Store Pickup
- description: Retrieve current pricing, promotional discounts, and sale prices for catalog items.
  name: Price and Promo Queries
- description: Track shipment status and estimated delivery for online and commercial orders.
  name: Order Tracking
finops:
- name: Advance Auto Parts Finops
  service_category: Automotive Retail
  slug: advance-auto-parts-finops
image: /assets/icons/advance-auto-parts.png
integrations:
- description: Integration with Mitchell 1 shop management and repair information software for parts ordering.
  name: Mitchell 1 ProDemand
- description: Integration with ALLDATA repair information and shop management platform for professional technicians.
  name: ALLDATA
- description: Parts available through Amazon marketplace for broader consumer reach.
  name: Amazon
- description: ACES/PIES automotive data standard compatibility for parts catalog interchange.
  name: AutoZone MOTOR Data
- description: Dealer management system integration for automotive dealership parts departments.
  name: DealerSocket
- description: Storefront integration for resellers using Shopify to list Advance Auto Parts products.
  name: Shopify
json_schemas:
- name: ErrorResponse
  property_count: 2
  slug: catalog-api-errorresponse
- name: InventoryResult
  property_count: 2
  slug: catalog-api-inventoryresult
- name: Make
  property_count: 2
  slug: catalog-api-make
- name: MakeList
  property_count: 1
  slug: catalog-api-makelist
- name: ModelList
  property_count: 1
  slug: catalog-api-modellist
- name: Product
  property_count: 8
  slug: catalog-api-product
- name: ProductList
  property_count: 2
  slug: catalog-api-productlist
- name: Store
  property_count: 6
  slug: catalog-api-store
- name: StoreInventory
  property_count: 4
  slug: catalog-api-storeinventory
- name: StoreList
  property_count: 1
  slug: catalog-api-storelist
- name: VehicleModel
  property_count: 2
  slug: catalog-api-vehiclemodel
- name: YearList
  property_count: 1
  slug: catalog-api-yearlist
- name: Cart
  property_count: 3
  slug: commerce-api-cart
- name: CartItem
  property_count: 3
  slug: commerce-api-cartitem
- name: CartItemInput
  property_count: 2
  slug: commerce-api-cartiteminput
- name: LoyaltyAccount
  property_count: 5
  slug: commerce-api-loyaltyaccount
- name: LoyaltyTransaction
  property_count: 5
  slug: commerce-api-loyaltytransaction
- name: LoyaltyTransactionList
  property_count: 1
  slug: commerce-api-loyaltytransactionlist
- name: Order
  property_count: 5
  slug: commerce-api-order
- name: OrderInput
  property_count: 4
  slug: commerce-api-orderinput
- name: OrderList
  property_count: 2
  slug: commerce-api-orderlist
json_structures:
- name: Catalog Api Errorresponse Structure
  property_count: 2
  slug: catalog-api-errorresponse-structure
- name: Catalog Api Inventoryresult Structure
  property_count: 2
  slug: catalog-api-inventoryresult-structure
- name: Catalog Api Make Structure
  property_count: 2
  slug: catalog-api-make-structure
- name: Catalog Api Makelist Structure
  property_count: 1
  slug: catalog-api-makelist-structure
- name: Catalog Api Modellist Structure
  property_count: 1
  slug: catalog-api-modellist-structure
- name: Catalog Api Product Structure
  property_count: 8
  slug: catalog-api-product-structure
- name: Catalog Api Productlist Structure
  property_count: 2
  slug: catalog-api-productlist-structure
- name: Catalog Api Store Structure
  property_count: 6
  slug: catalog-api-store-structure
- name: Catalog Api Storeinventory Structure
  property_count: 4
  slug: catalog-api-storeinventory-structure
- name: Catalog Api Storelist Structure
  property_count: 1
  slug: catalog-api-storelist-structure
- name: Catalog Api Vehiclemodel Structure
  property_count: 2
  slug: catalog-api-vehiclemodel-structure
- name: Catalog Api Yearlist Structure
  property_count: 1
  slug: catalog-api-yearlist-structure
- name: Commerce Api Cart Structure
  property_count: 3
  slug: commerce-api-cart-structure
- name: Commerce Api Cartitem Structure
  property_count: 3
  slug: commerce-api-cartitem-structure
- name: Commerce Api Cartiteminput Structure
  property_count: 2
  slug: commerce-api-cartiteminput-structure
- name: Commerce Api Loyaltyaccount Structure
  property_count: 5
  slug: commerce-api-loyaltyaccount-structure
- name: Commerce Api Loyaltytransaction Structure
  property_count: 5
  slug: commerce-api-loyaltytransaction-structure
- name: Commerce Api Loyaltytransactionlist Structure
  property_count: 1
  slug: commerce-api-loyaltytransactionlist-structure
- name: Commerce Api Order Structure
  property_count: 5
  slug: commerce-api-order-structure
- name: Commerce Api Orderinput Structure
  property_count: 4
  slug: commerce-api-orderinput-structure
- name: Commerce Api Orderlist Structure
  property_count: 2
  slug: commerce-api-orderlist-structure
jsonld:
- class_count: 34
  name: Advance Auto Parts Catalog Api Context
  property_count: 1
  slug: advance-auto-parts-catalog-api-context
- class_count: 30
  name: Advance Auto Parts Commerce Api Context
  property_count: 6
  slug: advance-auto-parts-commerce-api-context
layout: provider
modified: '2026-04-19'
name: Advance Auto Parts
nav: Providers
network: true
overview: 'Advance Auto Parts publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Cart API, Inventory API, Loyalty API, and 4 more. Tagged areas include Automotive, E-Commerce, Parts Catalog, Retail, and Supply Chain.


  The Advance Auto Parts catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Advance Auto Parts'' developer surface includes authentication, developer portal, support, engineering blog, signup flow, and 16 more developer resources.'
plans:
- name: Advance Auto Parts Plans Pricing
  plan_count: 1
  slug: advance-auto-parts-plans-pricing
press:
- date: '2026-05-25'
  title: Premium Guard Inc. Named 2025 E-Commerce Vendor of ...
  url: https://www.prnewswire.com/news-releases/premium-guard-inc-named-2025-e-commerce-vendor-of-the-year-by-advance-auto-parts-302658791.html
- date: '2026-05-25'
  title: Advance Auto Parts Cuts 2025 Outlook As Sales Fall
  url: https://www.wsj.com/business/earnings/advance-auto-parts-cuts-2025-outlook-amid-weaker-results-4dbf7195
- date: '2026-05-25'
  title: Advance Auto Parts Vendor Portal | Alloy.ai Integrations
  url: https://alloy.ai/integrations/advance-auto-parts
- date: '2026-05-25'
  title: Shweta Bhatia - Advance Auto Parts
  url: https://www.linkedin.com/in/shweta-bhatia25
- date: '2026-05-25'
  title: Advance Auto Parts reshapes footprint and 2025 results
  url: https://www.stocktitan.net/sec-filings/AAP/10-k-advance-auto-parts-inc-files-annual-report-a1f015e6e77e.html
random_paper: 1
rate_limits:
- limit_count: 1
  name: Advance Auto Parts Rate Limits
  slug: advance-auto-parts-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Advance Auto Parts API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: advance-auto-parts-jsonschema-spectral-rules
- effective_rule_count: 79
  extends:
  - spectral:oas
  name: Advance Auto Parts API Rules
  rule_count: 38
  severity_counts:
    error: 16
    hint: 0
    info: 6
    warn: 16
  slug: advance-auto-parts-spectral-rules
scopes:
- name: Advance Auto Parts Scopes
  scope_count: 4
  slug: advance-auto-parts-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 26
    catalog_gap: 47.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 30.3
    commercial_clarity: 30.3
    contract_governance: 28.8
    contract_quality: 68.6
    developer_ergonomics: 29.8
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 18.4
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/advance-auto-parts/refs/heads/main/screenshots/advance-auto-parts-2026-06-20T165218.png
security:
- kind: authentication
  name: Advance Auto Parts Authentication
  slug: advance-auto-parts-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Advance Auto Parts Domain Security
  slug: advance-auto-parts-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Advance Auto Parts Vulnerability Disclosure
  slug: advance-auto-parts-vulnerability-disclosure
  summary_line: Hackerone
slug: advance-auto-parts
tags:
- Automotive
- E-Commerce
- Parts Catalog
- Retail
- Supply Chain
- Fortune 500
use_cases:
- description: Integrate parts ordering directly into auto repair shop management software for seamless procurement.
  name: Shop Management Software Integration
- description: Automate parts procurement for fleet vehicles based on maintenance schedules and repair orders.
  name: Fleet Maintenance Automation
- description: Build mobile applications that allow technicians to look up and order parts from their smartphones.
  name: Mobile Parts Lookup App
- description: Embed parts catalog and ordering in vehicle repair estimation and diagnostic platforms.
  name: Vehicle Repair Platforms
- description: Build custom loyalty dashboards showing Speed Perks points, rewards, and purchase history.
  name: Loyalty Program Portals
- description: Sync Advance Auto Parts catalog data with shop or warehouse inventory management systems.
  name: Inventory Management Systems
website: https://www.advanceautoparts.com
---
