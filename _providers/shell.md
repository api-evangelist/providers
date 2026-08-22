---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Shell Agentic Access
  operation_count: 28
  slug: shell-agentic-access
  summary_line: 28 operations · 9 acting
api_count: 12
apis:
- description: The Shell Aviation Fuel Reseller API enables aviation fuel resellers and operators to manage fuel procurement, pricing queries, order placement, and delivery logistics for Shell Aviation fuel products
  name: Shell Aviation Fuel Reseller API
  slug: aviation-fuel-reseller
- description: Manage loyalty accounts
  name: Shell Accounts API
  slug: shell-accounts-api
- description: Manage B2B fuel cards
  name: Shell Cards API
  slug: shell-cards-api
- description: Browse loyalty rewards catalogue
  name: Shell Catalogue API
  slug: shell-catalogue-api
- description: Manage fuel card invoices
  name: Shell Invoices API
  slug: shell-invoices-api
- description: Manage card spending limits and restrictions
  name: Shell Limits API
  slug: shell-limits-api
- description: Manage loyalty offers
  name: Shell Offers API
  slug: shell-offers-api
- description: Manage lubricants orders
  name: Shell Orders API
  slug: shell-orders-api
- description: Query and manage loyalty points
  name: Shell Points API
  slug: shell-points-api
- description: Browse lubricants product catalogue
  name: Shell Products API
  slug: shell-products-api
- description: Query Shell fuel and EV charging sites
  name: Shell Sites API
  slug: shell-sites-api
- description: Retrieve fuel card transaction data
  name: Shell Transactions API
  slug: shell-transactions-api
artifact_total: 82
collections:
- collection_type: postman
  name: Shell B2B Mobility Accounts API
  slug: postman-shell-accounts-api
- collection_type: postman
  name: Shell B2B Mobility Accounts Cards API
  slug: postman-shell-cards-api
- collection_type: postman
  name: Shell B2B Mobility Accounts Catalogue API
  slug: postman-shell-catalogue-api
- collection_type: postman
  name: Shell B2B Mobility Accounts Invoices API
  slug: postman-shell-invoices-api
- collection_type: postman
  name: Shell B2B Mobility Accounts Limits API
  slug: postman-shell-limits-api
- collection_type: postman
  name: Shell B2B Mobility Accounts Offers API
  slug: postman-shell-offers-api
- collection_type: postman
  name: Shell B2B Mobility Accounts Orders API
  slug: postman-shell-orders-api
- collection_type: postman
  name: Shell B2B Mobility Accounts Points API
  slug: postman-shell-points-api
- collection_type: postman
  name: Shell B2B Mobility Accounts Products API
  slug: postman-shell-products-api
- collection_type: postman
  name: Shell B2B Mobility Accounts Sites API
  slug: postman-shell-sites-api
- collection_type: postman
  name: Shell B2B Mobility Accounts Transactions API
  slug: postman-shell-transactions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shell B2B Mobility Accounts API
  slug: open-shell-accounts-api
- collection_type: open
  name: Shell B2B Mobility API
  slug: open-shell-b2b-mobility
- collection_type: open
  name: Shell B2B Mobility Accounts Cards API
  slug: open-shell-cards-api
- collection_type: open
  name: Shell B2B Mobility Accounts Catalogue API
  slug: open-shell-catalogue-api
- collection_type: open
  name: Shell B2B Mobility Accounts Invoices API
  slug: open-shell-invoices-api
- collection_type: open
  name: Shell B2B Mobility Accounts Limits API
  slug: open-shell-limits-api
- collection_type: open
  name: Shell Loyalty API
  slug: open-shell-loyalty
- collection_type: open
  name: Shell Lubricants API
  slug: open-shell-lubricants
- collection_type: open
  name: Shell B2B Mobility Accounts Offers API
  slug: open-shell-offers-api
- collection_type: open
  name: Shell B2B Mobility Accounts Orders API
  slug: open-shell-orders-api
- collection_type: open
  name: Shell B2B Mobility Accounts Points API
  slug: open-shell-points-api
- collection_type: open
  name: Shell B2B Mobility Accounts Products API
  slug: open-shell-products-api
- collection_type: open
  name: Shell B2B Mobility Accounts Sites API
  slug: open-shell-sites-api
- collection_type: open
  name: Shell B2B Mobility Accounts Transactions API
  slug: open-shell-transactions-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/shell/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shell-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shell-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shell-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shell-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shell
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.shell.com
- group: other
  title: ''
  type: API Catalog
  url: https://developer.shell.com/api-catalog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.shell.com/docs/welcome-shell-developer-portal
- group: auth
  title: ''
  type: API Key Registration
  url: https://developer.shell.com/signup
- group: auth
  title: ''
  type: Authentication
  url: https://developer.shell.com/docs/authentication
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shell.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shell.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://developer.shell.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.shell.com/support/api-status
- group: company
  title: ''
  type: Blog
  url: https://developer.shell.com/latest-updates
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shell
- group: company
  title: ''
  type: Website
  url: https://www.shell.com
- group: design
  title: ''
  type: JSONLD
  url: json-ld/shell-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/shell-vocabulary.yml
created: '2025-03-01'
description: Royal Dutch Shell plc is a global energy company operating across oil, gas, renewable energy, lubricants, aviation fuel, and mobility sectors. The Shell Developer Portal provides APIs for B2B mobility card management, loyalty programs, lubricants ordering, aviation fuel reselling, and fleet management. SDKs are available in Java, .NET, TypeScript, PHP, Python, and Ruby.
examples:
- key_count: 4
  name: Shell List Transactions Example
  slug: shell-list-transactions-example
finops:
- name: Shell Finops
  service_category: Energy / Mobility B2B
  slug: shell-finops
image: https://www.shell.com/etc/designs/shell/clientlib-main/img/shell-logo.png
json_schemas:
- name: AccountEnrollRequest
  property_count: 8
  slug: shell-accountenrollrequest
- name: AccountUpdateRequest
  property_count: 5
  slug: shell-accountupdaterequest
- name: Card
  property_count: 12
  slug: shell-card
- name: CardLimit
  property_count: 4
  slug: shell-cardlimit
- name: CardLimitUpdateRequest
  property_count: 5
  slug: shell-cardlimitupdaterequest
- name: CardListResponse
  property_count: 4
  slug: shell-cardlistresponse
- name: CardOrderRequest
  property_count: 7
  slug: shell-cardorderrequest
- name: CardOrderResponse
  property_count: 3
  slug: shell-cardorderresponse
- name: CatalogueItem
  property_count: 10
  slug: shell-catalogueitem
- name: CatalogueListResponse
  property_count: 4
  slug: shell-cataloguelistresponse
- name: Shell Fuel Card
  property_count: 12
  slug: shell-fuel-card
- name: Invoice
  property_count: 9
  slug: shell-invoice
- name: InvoiceListResponse
  property_count: 4
  slug: shell-invoicelistresponse
- name: LoyaltyAccount
  property_count: 11
  slug: shell-loyaltyaccount
- name: LoyaltyTransaction
  property_count: 8
  slug: shell-loyaltytransaction
- name: LubricantsAccount
  property_count: 8
  slug: shell-lubricantsaccount
- name: Offer
  property_count: 7
  slug: shell-offer
- name: OfferListResponse
  property_count: 2
  slug: shell-offerlistresponse
- name: Order
  property_count: 10
  slug: shell-order
- name: OrderCreateRequest
  property_count: 6
  slug: shell-ordercreaterequest
- name: OrderItem
  property_count: 6
  slug: shell-orderitem
- name: OrderListResponse
  property_count: 4
  slug: shell-orderlistresponse
- name: PointsBalance
  property_count: 8
  slug: shell-pointsbalance
- name: Product
  property_count: 10
  slug: shell-product
- name: ProductListResponse
  property_count: 4
  slug: shell-productlistresponse
- name: RedemptionRequest
  property_count: 4
  slug: shell-redemptionrequest
- name: RedemptionResponse
  property_count: 5
  slug: shell-redemptionresponse
- name: Site
  property_count: 10
  slug: shell-site
- name: SiteListResponse
  property_count: 4
  slug: shell-sitelistresponse
- name: Shell Fuel Card Transaction
  property_count: 19
  slug: shell-transaction
- name: TransactionListResponse
  property_count: 4
  slug: shell-transactionlistresponse
json_structures:
- name: Shell Fuel Card Structure
  property_count: 0
  slug: shell-fuel-card-structure
- name: Shell Structure
  property_count: 0
  slug: shell-structure
jsonld:
- class_count: 42
  name: Shell Context
  property_count: 14
  slug: shell-context
layout: provider
modified: '2026-05-19'
name: Shell
nav: Providers
network: true
overview: 'Shell publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Cards API, Catalogue API, and 8 more. Tagged areas include Aviation, Electric Vehicle Charging, Energy, Fleet Management, and Fuel.


  The Shell catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Shell''s developer surface includes authentication, getting-started guide, support, engineering blog, and 16 more developer resources.'
plans:
- name: Shell Plans Pricing
  plan_count: 1
  slug: shell-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Shell Rate Limits
  slug: shell-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Shell API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: shell-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Shell API Rules
  rule_count: 13
  severity_counts:
    error: 3
    hint: 0
    info: 5
    warn: 5
  slug: shell-rules
scopes:
- name: Shell Scopes
  scope_count: 9
  slug: shell-scopes
  summary_line: 9 scopes · clientCredentials
score:
  band: developing
  composite: 52.0
  delta: -0.7
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 25.0
    contract_quality: 70.6
    developer_ergonomics: 45.2
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shell/refs/heads/main/screenshots/shell-2026-06-20T193753.png
security:
- kind: authentication
  name: Shell Authentication
  slug: shell-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Shell Domain Security
  slug: shell-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: shell
tags:
- Aviation
- Electric Vehicle Charging
- Energy
- Fleet Management
- Fuel
- Gas
- Loyalty
- Lubricants
- Mobility
- Oil and Gas
- Renewable Energy
website: https://www.shell.com
---
