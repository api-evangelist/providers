---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Ncr Agentic Access
  operation_count: 43
  slug: ncr-agentic-access
  summary_line: 43 operations · 26 acting
api_count: 7
apis:
- description: Item, item-price, and item-attribute management plus item-details search.
  name: NCR Catalog API
  slug: ncr-catalog-api
- description: Catalog category-node hierarchy and group management.
  name: NCR Category API
  slug: ncr-category-api
- description: Order creation, lookup, update, and search.
  name: NCR Order API
  slug: ncr-order-api
- description: Platform user creation and user profile management.
  name: NCR Provisioning API
  slug: ncr-provisioning-api
- description: Authentication, authorization, and user password management.
  name: NCR Security API
  slug: ncr-security-api
- description: Selling Service shopping carts and cart line items.
  name: NCR Selling API
  slug: ncr-selling-api
- description: Site (location) provisioning, lookup, and geospatial search.
  name: NCR Site API
  slug: ncr-site-api
artifact_total: 116
collections:
- collection_type: postman
  name: BSP HMAC Examples
  slug: postman-ncr-bsp-hmac-examples
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NCR Voyix Commerce Platform APIs Catalog API
  slug: open-ncr-catalog-api
- collection_type: open
  name: NCR Voyix Commerce Platform APIs Catalog Category API
  slug: open-ncr-category-api
- collection_type: open
  name: NCR Voyix Commerce Platform APIs Catalog Order API
  slug: open-ncr-order-api
- collection_type: open
  name: NCR Voyix Commerce Platform APIs Catalog Provisioning API
  slug: open-ncr-provisioning-api
- collection_type: open
  name: NCR Voyix Commerce Platform APIs Catalog Security API
  slug: open-ncr-security-api
- collection_type: open
  name: NCR Voyix Commerce Platform APIs Catalog Selling API
  slug: open-ncr-selling-api
- collection_type: open
  name: NCR Voyix Commerce Platform APIs Catalog Site API
  slug: open-ncr-site-api
- collection_type: open
  name: NCR Voyix Commerce Platform APIs
  slug: open-ncr-voyix-commerce-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ncr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ncr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ncr-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NCRVoyix-Corporation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ncr-corporation
- group: company
  title: ''
  type: Website
  url: https://www.ncr.com
- group: company
  title: ''
  type: Website
  url: https://www.ncrvoyix.com/
- group: company
  title: ''
  type: Website
  url: https://www.ncratleos.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ncrvoyix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.docs.ncr.com/
- group: auth
  title: AccessKey (HMAC SHA-512) Authentication
  type: Authentication
  url: https://github.com/NCRVoyix-Corporation/ncr-bsp-hmac
- group: design
  title: ''
  type: Rules
  url: rules/ncr-voyix-commerce-platform-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ncr-voyix-commerce-platform-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ncr-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ncr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ncr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ncr-finops.yml
created: '2026-03-24'
description: 'NCR Corporation separated in October 2023 into two independent public companies: NCR Voyix, a global provider of digital commerce solutions for retailers and restaurants, and NCR Atleos, a leader in expanding self-directed banking through ATM networks. NCR Voyix operates the Voyix Commerce Platform, an API-based cloud architecture (the Business Services Platform) that powers unified-commerce POS, ecommerce, and payments for retail and restaurants. Developers access it at developer.ncrvoyix.com using AccessKey (HMAC SHA-512) authentication against api.ncr.com.'
examples:
- key_count: 5
  name: Ncr Voyix Commerce Platform Address Example
  slug: ncr-voyix-commerce-platform-address-example
- key_count: 4
  name: Ncr Voyix Commerce Platform Cart Example
  slug: ncr-voyix-commerce-platform-cart-example
- key_count: 5
  name: Ncr Voyix Commerce Platform Cart Line Example
  slug: ncr-voyix-commerce-platform-cart-line-example
- key_count: 3
  name: Ncr Voyix Commerce Platform Cart Line Input Example
  slug: ncr-voyix-commerce-platform-cart-line-input-example
- key_count: 6
  name: Ncr Voyix Commerce Platform Category Node Example
  slug: ncr-voyix-commerce-platform-category-node-example
- key_count: 2
  name: Ncr Voyix Commerce Platform Coordinates Example
  slug: ncr-voyix-commerce-platform-coordinates-example
- key_count: 3
  name: Ncr Voyix Commerce Platform Customer Example
  slug: ncr-voyix-commerce-platform-customer-example
- key_count: 5
  name: Ncr Voyix Commerce Platform Group Example
  slug: ncr-voyix-commerce-platform-group-example
- key_count: 1
  name: Ncr Voyix Commerce Platform Item Code List Example
  slug: ncr-voyix-commerce-platform-item-code-list-example
- key_count: 7
  name: Ncr Voyix Commerce Platform Item Example
  slug: ncr-voyix-commerce-platform-item-example
- key_count: 7
  name: Ncr Voyix Commerce Platform Item Input Example
  slug: ncr-voyix-commerce-platform-item-input-example
- key_count: 1
  name: Ncr Voyix Commerce Platform Item Page Example
  slug: ncr-voyix-commerce-platform-item-page-example
- key_count: 6
  name: Ncr Voyix Commerce Platform Item Price Example
  slug: ncr-voyix-commerce-platform-item-price-example
- key_count: 5
  name: Ncr Voyix Commerce Platform Item Price Input Example
  slug: ncr-voyix-commerce-platform-item-price-input-example
- key_count: 1
  name: Ncr Voyix Commerce Platform Localized Text Example
  slug: ncr-voyix-commerce-platform-localized-text-example
- key_count: 2
  name: Ncr Voyix Commerce Platform Login Request Example
  slug: ncr-voyix-commerce-platform-login-request-example
- key_count: 6
  name: Ncr Voyix Commerce Platform Order Example
  slug: ncr-voyix-commerce-platform-order-example
- key_count: 4
  name: Ncr Voyix Commerce Platform Order Input Example
  slug: ncr-voyix-commerce-platform-order-input-example
- key_count: 3
  name: Ncr Voyix Commerce Platform Order Line Example
  slug: ncr-voyix-commerce-platform-order-line-example
- key_count: 2
  name: Ncr Voyix Commerce Platform Order Search Example
  slug: ncr-voyix-commerce-platform-order-search-example
- key_count: 2
  name: Ncr Voyix Commerce Platform Product Id Example
  slug: ncr-voyix-commerce-platform-product-id-example
- key_count: 3
  name: Ncr Voyix Commerce Platform Quantity Example
  slug: ncr-voyix-commerce-platform-quantity-example
- key_count: 9
  name: Ncr Voyix Commerce Platform Site Example
  slug: ncr-voyix-commerce-platform-site-example
- key_count: 8
  name: Ncr Voyix Commerce Platform Site Input Example
  slug: ncr-voyix-commerce-platform-site-input-example
- key_count: 2
  name: Ncr Voyix Commerce Platform Site Search Example
  slug: ncr-voyix-commerce-platform-site-search-example
- key_count: 2
  name: Ncr Voyix Commerce Platform Token Response Example
  slug: ncr-voyix-commerce-platform-token-response-example
- key_count: 5
  name: Ncr Voyix Commerce Platform User Example
  slug: ncr-voyix-commerce-platform-user-example
- key_count: 4
  name: Ncr Voyix Commerce Platform User Input Example
  slug: ncr-voyix-commerce-platform-user-input-example
- key_count: 5
  name: Ncr Voyix Commerce Platform User Profile Example
  slug: ncr-voyix-commerce-platform-user-profile-example
finops:
- name: Ncr Finops
  service_category: Commerce + Point of Sale + Payments
  slug: ncr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ncr.png
json_schemas:
- name: Address
  property_count: 5
  slug: ncr-voyix-commerce-platform-address
- name: CartLineInput
  property_count: 3
  slug: ncr-voyix-commerce-platform-cart-line-input
- name: CartLine
  property_count: 5
  slug: ncr-voyix-commerce-platform-cart-line
- name: Cart
  property_count: 4
  slug: ncr-voyix-commerce-platform-cart
- name: CategoryNode
  property_count: 6
  slug: ncr-voyix-commerce-platform-category-node
- name: Coordinates
  property_count: 2
  slug: ncr-voyix-commerce-platform-coordinates
- name: Customer
  property_count: 3
  slug: ncr-voyix-commerce-platform-customer
- name: Group
  property_count: 5
  slug: ncr-voyix-commerce-platform-group
- name: ItemCodeList
  property_count: 1
  slug: ncr-voyix-commerce-platform-item-code-list
- name: ItemInput
  property_count: 7
  slug: ncr-voyix-commerce-platform-item-input
- name: ItemPage
  property_count: 1
  slug: ncr-voyix-commerce-platform-item-page
- name: ItemPriceInput
  property_count: 5
  slug: ncr-voyix-commerce-platform-item-price-input
- name: ItemPrice
  property_count: 6
  slug: ncr-voyix-commerce-platform-item-price
- name: Item
  property_count: 7
  slug: ncr-voyix-commerce-platform-item
- name: LocalizedText
  property_count: 1
  slug: ncr-voyix-commerce-platform-localized-text
- name: LoginRequest
  property_count: 2
  slug: ncr-voyix-commerce-platform-login-request
- name: OrderInput
  property_count: 4
  slug: ncr-voyix-commerce-platform-order-input
- name: OrderLine
  property_count: 3
  slug: ncr-voyix-commerce-platform-order-line
- name: Order
  property_count: 6
  slug: ncr-voyix-commerce-platform-order
- name: OrderSearch
  property_count: 2
  slug: ncr-voyix-commerce-platform-order-search
- name: ProductId
  property_count: 2
  slug: ncr-voyix-commerce-platform-product-id
- name: Quantity
  property_count: 3
  slug: ncr-voyix-commerce-platform-quantity
- name: SiteInput
  property_count: 8
  slug: ncr-voyix-commerce-platform-site-input
- name: Site
  property_count: 9
  slug: ncr-voyix-commerce-platform-site
- name: SiteSearch
  property_count: 2
  slug: ncr-voyix-commerce-platform-site-search
- name: Status
  property_count: 0
  slug: ncr-voyix-commerce-platform-status
- name: TokenResponse
  property_count: 2
  slug: ncr-voyix-commerce-platform-token-response
- name: UserInput
  property_count: 4
  slug: ncr-voyix-commerce-platform-user-input
- name: UserProfile
  property_count: 5
  slug: ncr-voyix-commerce-platform-user-profile
- name: User
  property_count: 5
  slug: ncr-voyix-commerce-platform-user
json_structures:
- name: Ncr Voyix Commerce Platform Address Structure
  property_count: 5
  slug: ncr-voyix-commerce-platform-address-structure
- name: Ncr Voyix Commerce Platform Cart Line Input Structure
  property_count: 3
  slug: ncr-voyix-commerce-platform-cart-line-input-structure
- name: Ncr Voyix Commerce Platform Cart Line Structure
  property_count: 5
  slug: ncr-voyix-commerce-platform-cart-line-structure
- name: Ncr Voyix Commerce Platform Cart Structure
  property_count: 4
  slug: ncr-voyix-commerce-platform-cart-structure
- name: Ncr Voyix Commerce Platform Category Node Structure
  property_count: 6
  slug: ncr-voyix-commerce-platform-category-node-structure
- name: Ncr Voyix Commerce Platform Coordinates Structure
  property_count: 2
  slug: ncr-voyix-commerce-platform-coordinates-structure
- name: Ncr Voyix Commerce Platform Customer Structure
  property_count: 3
  slug: ncr-voyix-commerce-platform-customer-structure
- name: Ncr Voyix Commerce Platform Group Structure
  property_count: 5
  slug: ncr-voyix-commerce-platform-group-structure
- name: Ncr Voyix Commerce Platform Item Code List Structure
  property_count: 1
  slug: ncr-voyix-commerce-platform-item-code-list-structure
- name: Ncr Voyix Commerce Platform Item Input Structure
  property_count: 7
  slug: ncr-voyix-commerce-platform-item-input-structure
- name: Ncr Voyix Commerce Platform Item Page Structure
  property_count: 1
  slug: ncr-voyix-commerce-platform-item-page-structure
- name: Ncr Voyix Commerce Platform Item Price Input Structure
  property_count: 5
  slug: ncr-voyix-commerce-platform-item-price-input-structure
- name: Ncr Voyix Commerce Platform Item Price Structure
  property_count: 6
  slug: ncr-voyix-commerce-platform-item-price-structure
- name: Ncr Voyix Commerce Platform Item Structure
  property_count: 7
  slug: ncr-voyix-commerce-platform-item-structure
- name: Ncr Voyix Commerce Platform Localized Text Structure
  property_count: 1
  slug: ncr-voyix-commerce-platform-localized-text-structure
- name: Ncr Voyix Commerce Platform Login Request Structure
  property_count: 2
  slug: ncr-voyix-commerce-platform-login-request-structure
- name: Ncr Voyix Commerce Platform Order Input Structure
  property_count: 4
  slug: ncr-voyix-commerce-platform-order-input-structure
- name: Ncr Voyix Commerce Platform Order Line Structure
  property_count: 3
  slug: ncr-voyix-commerce-platform-order-line-structure
- name: Ncr Voyix Commerce Platform Order Search Structure
  property_count: 2
  slug: ncr-voyix-commerce-platform-order-search-structure
- name: Ncr Voyix Commerce Platform Order Structure
  property_count: 6
  slug: ncr-voyix-commerce-platform-order-structure
- name: Ncr Voyix Commerce Platform Product Id Structure
  property_count: 2
  slug: ncr-voyix-commerce-platform-product-id-structure
- name: Ncr Voyix Commerce Platform Quantity Structure
  property_count: 3
  slug: ncr-voyix-commerce-platform-quantity-structure
- name: Ncr Voyix Commerce Platform Site Input Structure
  property_count: 8
  slug: ncr-voyix-commerce-platform-site-input-structure
- name: Ncr Voyix Commerce Platform Site Search Structure
  property_count: 2
  slug: ncr-voyix-commerce-platform-site-search-structure
- name: Ncr Voyix Commerce Platform Site Structure
  property_count: 9
  slug: ncr-voyix-commerce-platform-site-structure
- name: Ncr Voyix Commerce Platform Status Structure
  property_count: 0
  slug: ncr-voyix-commerce-platform-status-structure
- name: Ncr Voyix Commerce Platform Token Response Structure
  property_count: 2
  slug: ncr-voyix-commerce-platform-token-response-structure
- name: Ncr Voyix Commerce Platform User Input Structure
  property_count: 4
  slug: ncr-voyix-commerce-platform-user-input-structure
- name: Ncr Voyix Commerce Platform User Profile Structure
  property_count: 5
  slug: ncr-voyix-commerce-platform-user-profile-structure
- name: Ncr Voyix Commerce Platform User Structure
  property_count: 5
  slug: ncr-voyix-commerce-platform-user-structure
jsonld:
- class_count: 29
  name: Ncr Voyix Commerce Platform Context
  property_count: 65
  slug: ncr-voyix-commerce-platform-context
layout: provider
modified: '2026-06-02'
name: NCR
nav: Providers
network: true
overview: 'NCR publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Category API, Order API, and 4 more. Tagged areas include Restaurant, Retail, Banking, ATM, and Point-of-Sale.


  The NCR catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  NCR''s developer surface includes authentication, documentation, and 17 more developer resources.'
plans:
- name: Ncr Plans Pricing
  plan_count: 2
  slug: ncr-plans-pricing
press:
- date: '2026-05-25'
  title: NCR Voyix Unveils AI-Accelerated Suite of Applications on ...
  url: https://investor.ncrvoyix.com/news-releases/news-release-details/ncr-voyix-unveils-ai-accelerated-suite-applications-voyix/
- date: '2026-05-25'
  title: NCR Atleos Appoints New Chief Information Officer to ...
  url: https://investor.ncratleos.com/news-events/press-releases/detail/167/ncr-atleos-appoints-new-chief-information-officer-to-drive-technology-strategy-digital-transformation-and-ai-led-automation
- date: '2026-05-25'
  title: NCR Atleos
  url: https://www.facebook.com/Atleos.NCR/posts/ncr-atleos-announced-an-advancement-in-the-dual-sided-atm-concept-leveraging-com/743595608814422/
- date: '2026-05-25'
  title: NCR Atleos Advances Dual-Sided ATM Concept with AI- ...
  url: https://www.businesswire.com/news/home/20260127016774/en/NCR-Atleos-Advances-Dual-Sided-ATM-Concept-with-AI-Assisted-Design-Sustainability-and-Operational-Efficiency
- date: '2026-05-25'
  title: 'NCR: Proactive defect management with AI'
  url: https://www.fabasoft.com/en/media-center/nonconformance-reports-proactive-defect-management-ai-and-cloud
- date: '2026-05-06'
  title: Pei Wei Expands NCR Voyix Relationship to Power POS Across Its Restaurants | NCR Voyix
  url: https://collections.ncrvoyix.com/newsroom/pei-wei-expands-ncr-voyix-relationship-to-power-pos-across-its-restaurants
- date: '2026-05-06'
  title: NCR Voyix Selected by Gyro Hut to Modernize and Strengthen its Technology Platform | NCR Voyix
  url: https://collections.ncrvoyix.com/newsroom/ncr-voyix-selected-by-gyro-hut-to-modernize-and-strengthen-its-technology-platform
- date: '2026-05-04'
  title: Stater Bros. Markets Signs New Agreement with NCR Voyix to Modernize POS and Payments on the Voyix Commerce Platform | NCR Voyix
  url: https://collections.ncrvoyix.com/newsroom/stater-bros-markets-signs-new-agreement-with-ncr-voyix-to-modernize-pos-and-payments-on-the-voyix-commerce-platform
random_paper: 8
rate_limits:
- limit_count: 2
  name: Ncr Rate Limits
  slug: ncr-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: NCR API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ncr-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: NCR API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: ncr-spectral-rules
- effective_rule_count: 37
  extends: []
  name: NCR API Rules
  rule_count: 37
  severity_counts:
    error: 11
    hint: 0
    info: 8
    warn: 18
  slug: ncr-voyix-commerce-platform-spectral-rules
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 35.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.8
    contract_quality: 25.9
    developer_ergonomics: 38.1
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 23.7
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ncr/refs/heads/main/screenshots/ncr-2026-06-20T190112.png
security:
- kind: authentication
  name: Ncr Authentication
  slug: ncr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ncr Domain Security
  slug: ncr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ncr
tags:
- Restaurant
- Retail
- Banking
- ATM
- Point-of-Sale
- Commerce
- Fortune 500
website: https://www.ncr.com
---
