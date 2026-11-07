---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Digi Key Agentic Access
  operation_count: 58
  slug: digi-key-agentic-access
  summary_line: 58 operations · 12 acting
api_count: 22
apis:
- baseURL: https://api.digikey.com/OrderManagement/v1
  baseurl_source: declared
  description: The Barcoding API from Digi-Key — 4 operation(s) for barcoding.
  name: Digi-Key Barcoding API
  slug: digi-key-barcoding-api
- baseURL: https://api.digikey.com/OrderManagement/v1
  baseurl_source: declared
  description: The BondedInventory API from Digi-Key — 5 operation(s) for bondedinventory.
  name: Digi-Key Bonded Inventory API
  slug: digi-key-bondedinventory-api
- baseURL: https://api.digikey.com/OrderManagement/v1
  baseurl_source: declared
  description: The CustomerResource API from Digi-Key — 1 operation(s) for customerresource.
  name: Digi-Key Customer Resource API
  slug: digi-key-customerresource-api
- baseURL: https://api.digikey.com/OrderManagement/v1
  baseurl_source: declared
  description: The Lists API from Digi-Key — 5 operation(s) for lists.
  name: Digi-Key Lists API
  slug: digi-key-lists-api
- baseURL: https://api.digikey.com/OrderManagement/v1
  baseurl_source: declared
  description: The OrderHistory API from Digi-Key — 2 operation(s) for orderhistory.
  name: Digi-Key Order History API
  slug: digi-key-orderhistory-api
- baseURL: https://api.digikey.com/OrderManagement/v1
  baseurl_source: declared
  description: The OrderManagement API from Digi-Key — 8 operation(s) for ordermanagement.
  name: Digi-Key Order Management API
  slug: digi-key-ordermanagement-api
- baseURL: https://api.digikey.com/OrderManagement/v1
  baseurl_source: declared
  description: The Orders API from Digi-Key — 1 operation(s) for orders.
  name: Digi-Key Orders API
  slug: digi-key-orders-api
- baseURL: https://api.digikey.com/OrderManagement/v1
  baseurl_source: declared
  description: The PackList API from Digi-Key — 3 operation(s) for packlist.
  name: Digi-Key Pack List API
  slug: digi-key-packlist-api
- baseURL: https://api.digikey.com/OrderManagement/v1
  baseurl_source: declared
  description: The Parts API from Digi-Key — 2 operation(s) for parts.
  name: Digi-Key Parts API
  slug: digi-key-parts-api
- baseURL: https://api.digikey.com/OrderManagement/v1
  baseurl_source: declared
  description: The Pcn API from Digi-Key — 1 operation(s) for pcn.
  name: Digi-Key Pcn API
  slug: digi-key-pcn-api
- baseURL: https://api.digikey.com/OrderManagement/v1
  baseurl_source: declared
  description: The Quotes API from Digi-Key — 3 operation(s) for quotes.
  name: Digi-Key Quotes API
  slug: digi-key-quotes-api
- baseURL: https://api.digikey.com/OrderManagement/v1
  baseurl_source: declared
  description: The Product Search API from Digi-Key — 14 operation(s) for product search.
  name: Digi-Key Product Search API
  slug: digi-key-product-search-api
artifact_total: 58
common:
- group: other
  href: https://artifacts.apis.io/digi-key/capabilities/digi-key-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/digi-key-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/digi-key/json-ld/digi-key-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/digi-key-context.jsonld
- group: other
  href: https://artifacts.apis.io/digi-key/overlays/digi-key-b2bapi-order-management-api-ordermanagement-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/digi-key-b2bapi-order-management-api-ordermanagement-v1-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/digi-key/agentic-access/digi-key-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/digi-key-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/digi-key/rate-limits/digi-key-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/digi-key-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/digi-key/rules/digi-key-rules.yml
  title: ''
  type: Spectral
  url: rules/digi-key-rules.yml
- group: design
  href: https://artifacts.apis.io/digi-key/vocabulary/digi-key-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/digi-key-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/digi-key/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/digi-key/data-model/digi-key-data-model.yml
  title: ''
  type: DataModel
  url: data-model/digi-key-data-model.yml
- group: operate
  href: https://artifacts.apis.io/digi-key/changelog/digi-key-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/digi-key-changelog.yml
- group: design
  href: https://artifacts.apis.io/digi-key/conventions/digi-key-conventions.yml
  title: ''
  type: Conventions
  url: conventions/digi-key-conventions.yml
- group: start
  href: https://artifacts.apis.io/digi-key/sandbox/digi-key-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/digi-key-sandbox.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.digikey.com/changelog
- group: design
  href: https://artifacts.apis.io/digi-key/lifecycle/digi-key-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/digi-key-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/digi-key/errors/digi-key-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/digi-key-problem-types.yml
- group: design
  href: https://artifacts.apis.io/digi-key/conformance/digi-key-conformance.yml
  title: ''
  type: Conformance
  url: conformance/digi-key-conformance.yml
- group: other
  href: https://artifacts.apis.io/digi-key/hosts/digi-key-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digi-key-hosts.yml
- group: other
  href: https://artifacts.apis.io/digi-key/vendors/digi-key-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digi-key-vendors.yml
- group: build
  href: https://artifacts.apis.io/digi-key/packages/digi-key-packages.yml
  title: ''
  type: SDKs
  url: packages/digi-key-packages.yml
- group: build
  href: https://artifacts.apis.io/digi-key/packages/digi-key-packages.yml
  title: ''
  type: Packages
  url: packages/digi-key-packages.yml
- group: auth
  href: https://artifacts.apis.io/digi-key/authentication/digi-key-authentication.yml
  title: ''
  type: Authentication
  url: authentication/digi-key-authentication.yml
- group: auth
  href: https://artifacts.apis.io/digi-key/scopes/digi-key-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/digi-key-scopes.yml
- group: auth
  href: https://artifacts.apis.io/digi-key/security/digi-key-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digi-key-domain-security.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Website
  url: https://www.digikey.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.digikey.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.digikey.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://developer.digikey.com/products
- group: operate
  title: ''
  type: Support
  url: https://developer.digikey.com/support
- group: operate
  title: ''
  type: FAQ
  url: https://developer.digikey.com/faq
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.digikey.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Digi-Key
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.digikey.com/api-user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digikey.com/en/help/Privacy
created: '2026-05-28'
description: DigiKey is a global distributor of electronic components. Its developer portal (developer.digikey.com) publishes OAuth 2.0 REST APIs on api.digikey.com for product search, pricing and inventory (Product Information V4), product change notifications, quoting, ordering, order status and order management, MyLists, supply chain (consigned inventory locations), barcode decoding and packing lists, with a sandbox at sandbox-api.digikey.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digi-key.png
json_schemas:
- name: AccountAssociationResponse
  property_count: 2
  slug: digi-key-account-association-response
- name: AddProductToQuote
  property_count: 3
  slug: digi-key-add-product-to-quote
- name: AddProductsToQuoteResponse
  property_count: 3
  slug: digi-key-add-products-to-quote-response
- name: BondedInventoryProductResponse
  property_count: 18
  slug: digi-key-bonded-inventory-product-response
- name: CreateListRequest
  property_count: 6
  slug: digi-key-create-list-request
- name: CreateQuoteRequest
  property_count: 1
  slug: digi-key-create-quote-request
- name: CustomerLocationResponse
  property_count: 4
  slug: digi-key-customer-location-response
- name: DigiReelPricing
  property_count: 7
  slug: digi-key-digi-reel-pricing
- name: InvoicePackingList
  property_count: 5
  slug: digi-key-invoice-packing-list
- name: KeywordRequest
  property_count: 5
  slug: digi-key-keyword-request
- name: KeywordResponse
  property_count: 6
  slug: digi-key-keyword-response
- name: ListData
  property_count: 19
  slug: digi-key-list-data
- name: ListPart
  property_count: 41
  slug: digi-key-list-part
- name: OrderRequest
  property_count: 14
  slug: digi-key-order-request
- name: OrderResponse
  property_count: 2
  slug: digi-key-order-response
- name: PackListBarcodeResponse
  property_count: 4
  slug: digi-key-pack-list-barcode-response
- name: PackageTypeByQuantityResponse
  property_count: 3
  slug: digi-key-package-type-by-quantity-response
- name: PartsByListIdResponse
  property_count: 2
  slug: digi-key-parts-by-list-id-response
- name: PcnResponse
  property_count: 2
  slug: digi-key-pcn-response
- name: PoNumberPackList
  property_count: 2
  slug: digi-key-po-number-pack-list
- name: PricingOptionsForQuantityResponse
  property_count: 11
  slug: digi-key-pricing-options-for-quantity-response
- name: ProductBarcodeResponse
  property_count: 5
  slug: digi-key-product-barcode-response
- name: ProductPricingResponse
  property_count: 5
  slug: digi-key-product-pricing-response
- name: Product2DBarcodeResponse
  property_count: 11
  slug: digi-key-product2-dbarcode-response
- name: ProductsFromQuoteResponse
  property_count: 2
  slug: digi-key-products-from-quote-response
- name: QuoteResponse
  property_count: 1
  slug: digi-key-quote-response
- name: QuotesResponse
  property_count: 2
  slug: digi-key-quotes-response
- name: RequestedPart
  property_count: 12
  slug: digi-key-requested-part
- name: SalesOrderDetailView
  property_count: 11
  slug: digi-key-sales-order-detail-view
- name: SalesOrderEligibilityView
  property_count: 3
  slug: digi-key-sales-order-eligibility-view
- name: SalesOrderPackList
  property_count: 2
  slug: digi-key-sales-order-pack-list
- name: SalesOrderScheduleForUpdate
  property_count: 2
  slug: digi-key-sales-order-schedule-for-update
- name: SalesOrderSchedulesView
  property_count: 5
  slug: digi-key-sales-order-schedules-view
- name: SalesOrder
  property_count: 12
  slug: digi-key-sales-order
- name: SalesOrderView
  property_count: 6
  slug: digi-key-sales-order-view
- name: SchedulePatchView
  property_count: 2
  slug: digi-key-schedule-patch-view
jsonld:
- class_count: 115
  name: Digi Key Context
  property_count: 374
  slug: digi-key-context
layout: provider
modified: '2026-10-19'
name: Digi-Key
nav: Providers
network: true
overview: 'Digi-Key publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Barcoding API, Bonded Inventory API, Customer Resource API, and 9 more. Tagged areas include Shopping, Public APIs, Electronic Components, Distribution, and Ordering.


  The Digi-Key catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Digi-Key''s developer surface includes changelog, sandbox, authentication, documentation, API reference, support, FAQ, and 27 more developer resources.'
plans:
- name: Digi Key Plans Pricing
  plan_count: 0
  slug: digi-key-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 9
  name: Digi Key Rate Limits
  slug: digi-key-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Digi-Key API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: digi-key-rules
scopes:
- name: Digi Key Scopes
  scope_count: 1
  slug: digi-key-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 32
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 57.8
    developer_ergonomics: 51.8
    discoverability: 78.6
    operational_transparency: 46.1
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/digi-key/digi-key-2026-07-25T212002.png
security:
- kind: authentication
  name: Digi Key Authentication
  slug: digi-key-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Digi Key Domain Security
  slug: digi-key-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: digi-key-find-part-pricing
  slug: digi-key-find-part-pricing
- name: digi-key-quote-and-order
  slug: digi-key-quote-and-order
slug: digi-key
tags:
- Shopping
- Public APIs
- Electronic Components
- Distribution
- Ordering
- Product Search
- Pricing
- Inventory
- Supply Chain
website: https://www.digikey.com/
---
