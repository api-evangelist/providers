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
  band: agent-ready
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 54
  human_in_the_loop: 0
  name: Crunchtime Information Systems Agentic Access
  operation_count: 168
  slug: crunchtime-information-systems-agentic-access
  summary_line: 168 operations · 54 acting
api_count: 4
apis:
- description: REST data-integration API for Crunchtime's Inventory Management, Labor & Scheduling, and Cruise products. GET and POST operations move employees, locations, budgets, categories, products, recipes, sal
  name: Crunchtime Inventory & Labor APIs
  slug: crunchtime-inventory-labor-apis
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Application User service is used to create and retrieve user profiles where each user is assigned a unique User ID and password for logging in to Enterprise Manager, Net-Chef, or the Teamworx Mana
  name: Crunchtime Information Systems Application User Service API
  slug: crunchtime-information-systems-application-user-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Authentication Service is allowing to validate user access to a franchisee site using a username and password.
  name: Crunchtime Information Systems Authentication Service API
  slug: crunchtime-information-systems-authentication-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: 'The Budgets Service allows you to create and retrieve budgets for each post period at each location. Budget figures for each General Ledger can be entered either as currency values or as percentages. '
  name: Crunchtime Information Systems Budget Service API
  slug: crunchtime-information-systems-budget-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Category Service allows you to create and retrieve product categories.
  name: Crunchtime Information Systems Category Service API
  slug: crunchtime-information-systems-category-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Check Menu Mix Service allows for the import of Check and Item based data from the POS system in order to deplete inventory according to the Recipe configuration in Enterprise Manager. The get cal
  name: Crunchtime Information Systems Check Menu Mix Service API
  slug: crunchtime-information-systems-check-menu-mix-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Commissary Order Service allows you to retrieve commissary orders.
  name: Crunchtime Information Systems Commissary Order Service API
  slug: crunchtime-information-systems-commissary-order-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Company Product Service allows you to create and retrieve the global, above store list of products that can be used elsewhere in the application, including recipe components (see the Recipe Enhanc
  name: Crunchtime Information Systems Company Product Enhanced Service API
  slug: crunchtime-information-systems-company-product-enhanced-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Confirm Receipt Standard Service allows you to create and retrieve confirmation receipts.
  name: Crunchtime Information Systems Confirm Receipt Standard Service API
  slug: crunchtime-information-systems-confirm-receipt-standard-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Currency Ratios Service is used to enter the exchange rates that will to convert monetary values from one currency to another. The "toCurrencyCode" is equal to the base currency in Enterprise Mana
  name: Crunchtime Information Systems Currency Ratio Service API
  slug: crunchtime-information-systems-currency-ratio-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Customer Order Enhanced service allows you to create and retrieve customer orders.
  name: Crunchtime Information Systems Customer Order Enhanced Service API
  slug: crunchtime-information-systems-customer-order-enhanced-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Customer Service can be used to create a “Customer” that is an establishment or outlet to which a Crunchtime Location sells or distributes products and/or produced Recipe items. It may be an outle
  name: Crunchtime Information Systems Customer Service API
  slug: crunchtime-information-systems-customer-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Daily Prep Service allows you to create, update, finalize, cancel, or retrieve daily prep transactions.
  name: Crunchtime Information Systems Daily Prep Service API
  slug: crunchtime-information-systems-daily-prep-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Electronic Invoice service enables you to upload e-invoice data into Crunchtime.
  name: Crunchtime Information Systems Electronic Invoice Service API
  slug: crunchtime-information-systems-electronic-invoice-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Employee Service combines what used to be three Crunchtime Data Pump (CDP) imports into one API call with multiple arrays. The Employee Service is used to create or review an employee in Crunchtim
  name: Crunchtime Information Systems Employee Service API
  slug: crunchtime-information-systems-employee-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The General Ledger services allows the Crunchtime applications to be aligned with the company’s accounting and bookkeeping systems. General Ledger codes and descriptions are associated with P&L groupi
  name: Crunchtime Information Systems General Ledger Service API
  slug: crunchtime-information-systems-general-ledger-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Hierarchy Service is used to group locations together for reporting purposes. For example, if the company is a national restaurant chain divided into six regions, setting up the hierarchy configur
  name: Crunchtime Information Systems Hierarchy Service API
  slug: crunchtime-information-systems-hierarchy-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: 'The Inventory Service combines a series of get and post calls used to update and review the quantity and value of a location stock on hand including: -Inventory Adjustments (Waste) -Value Adjustments '
  name: Crunchtime Information Systems Inventory Service API
  slug: crunchtime-information-systems-inventory-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Location Product Pricing Service API from Crunchtime Information Systems — 6 operation(s) for location product pricing service.
  name: Crunchtime Information Systems Location Product Pricing Service API
  slug: crunchtime-information-systems-location-product-pricing-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: 'The Locations Service allows you to review and configure general information about each location (restaurant, venue etc.) such as the address and phone number, as well as detailed preference settings '
  name: Crunchtime Information Systems Location Service API
  slug: crunchtime-information-systems-location-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Nutrition Service is used to create and retrieve data for Nutrition Product records.
  name: Crunchtime Information Systems Nutrition Service API
  slug: crunchtime-information-systems-nutrition-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Package Type Service offers a way to create, update, and retrieve package type entries.
  name: Crunchtime Information Systems Package Type Service API
  slug: crunchtime-information-systems-package-type-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Purchase by Invoice Service is used to create and retrieve purchasing data that is not directly associated with products. Typically this Service is used to record expenses for services, like month
  name: Crunchtime Information Systems Pbi Service API
  slug: crunchtime-information-systems-pbi-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Projected Consumption service is used to get Consumption data that has been systematically calculated based on a Location's Suggested Order configuration, or post Projected Consumption, overriding
  name: Crunchtime Information Systems Projected Consumption Service API
  slug: crunchtime-information-systems-projected-consumption-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Purchase Order Service allows you to create and retrieve vendor order records.
  name: Crunchtime Information Systems Purchase Order Service API
  slug: crunchtime-information-systems-purchase-order-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Recipe Service is used to create or extract recipe data including the header and component details. Recipes are created in Crunchtime for the purpose of inventory depletion. They are used to deple
  name: Crunchtime Information Systems Recipe Enhanced Service API
  slug: crunchtime-information-systems-recipe-enhanced-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Recipe Location Service allows you to create and retrieve location specific recipes.
  name: Crunchtime Information Systems Recipe Location Service API
  slug: crunchtime-information-systems-recipe-location-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Sales Forecasts Service can be used to ensure that Sales Forecasting data aligns between Crunchtime and other systems. You can use the service to get Forecast data that has been systematically cal
  name: Crunchtime Information Systems Sales Forecast Service API
  slug: crunchtime-information-systems-sales-forecast-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: 'The Sales Mix Service is used to align Crunchtime with Daily Sales Information generated in a PointofSale system. The data includes: Sales, Sales Tax, Paid Outs, Non Cash Media, Comps and Discounts an'
  name: Crunchtime Information Systems Sales Mix Service API
  slug: crunchtime-information-systems-sales-mix-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Scheduled Export service is an API that Crunchtime customers can use to download export files that have been generated via Scheduled Events in Enterprise Manager and convert the file content to JS
  name: Crunchtime Information Systems Scheduled Export Service API
  slug: crunchtime-information-systems-scheduled-export-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Storage Location service offers viewing and managing data associated with primary and secondary storage locations.
  name: Crunchtime Information Systems Storage Location Service API
  slug: crunchtime-information-systems-storage-location-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Supplemental Wage Service allows you to get or post Lump Sum or Hourly values to individual employees/positions for various supplemental earnings, such as tip sharing, vacation pay, sick pay, jury
  name: Crunchtime Information Systems Supplemental Wage Service API
  slug: crunchtime-information-systems-supplemental-wage-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Time Clock Enhanced service allows you to get or post employee time clock records that typically come from an external payroll or POS system. The post call will contain the original time punch dat
  name: Crunchtime Information Systems Time Clock Enhanced Service API
  slug: crunchtime-information-systems-time-clock-enhanced-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The User Defined Attributes (UDA) Service allows for the retrieval of the location and vendor User-Defined Attributes (UDAs). Location UDAs can be configured at the corporate level or specific to a pa
  name: Crunchtime Information Systems Uda Service API
  slug: crunchtime-information-systems-uda-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Vendor Location Service enables for quick setup of vendor locations for companies with large amounts of locationspecific information per vendor, such as payment terms, order minimums, email addres
  name: Crunchtime Information Systems Vendor Location Service API
  slug: crunchtime-information-systems-vendor-location-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Vendor Payment service allows you to create and retrieve payment information that typically comes from an Accounts Payable system. The Post call will update reconciled Vendor Orders and Purchase b
  name: Crunchtime Information Systems Vendor Payment Service API
  slug: crunchtime-information-systems-vendor-payment-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: Project Read Me - API Descriptions (SOURCE OF TRUTH) Project Read Me - API Descriptions (SOURCE OF TRUTH) 100% 10 Vendor Product Pricing Service 1 of 2 B22 Vendor Product Pricing Service [<<glossary:B
  name: Crunchtime Information Systems Vendor Product Pricing Service API
  slug: crunchtime-information-systems-vendor-product-pricing-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Vendor Service is used to create/review records of all Vendors that can be used to record expenses in Crunchtime. Typically, a third-party system is the system of record for Vendors and vendor dat
  name: Crunchtime Information Systems Vendor Service API
  slug: crunchtime-information-systems-vendor-service-api
artifact_total: 54
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/agentic-access/crunchtime-information-systems-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crunchtime-information-systems-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/rules/crunchtime-information-systems-rules.yml
  title: ''
  type: Spectral
  url: rules/crunchtime-information-systems-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/json-ld/crunchtime-information-systems-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crunchtime-information-systems-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/vocabulary/crunchtime-information-systems-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crunchtime-information-systems-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/data-model/crunchtime-information-systems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crunchtime-information-systems-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/errors/crunchtime-information-systems-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crunchtime-information-systems-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/conformance/crunchtime-information-systems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crunchtime-information-systems-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/hosts/crunchtime-information-systems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crunchtime-information-systems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/vendors/crunchtime-information-systems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crunchtime-information-systems-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crunchtime.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crunchtime.com/
- group: auth
  title: ''
  type: Security
  url: https://www.crunchtime.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crunchtime.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.crunchtime.com/press
- group: company
  title: ''
  type: Website
  url: https://www.crunchtime.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.crunchtime.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.crunchtime.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.crunchtime.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.crunchtime.com/docs/getting-started-with-apis
- group: operate
  title: ''
  type: Support
  url: https://crunchtime.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.crunchtime.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.crunchtime.com/request-demo
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.crunchtime.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.crunchtime.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/llms/crunchtime-information-systems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crunchtime-information-systems-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/authentication/crunchtime-information-systems-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crunchtime-information-systems-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/conventions/crunchtime-information-systems-conventions.yml
  title: ''
  type: Conventions
  url: conventions/crunchtime-information-systems-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/rate-limits/crunchtime-information-systems-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crunchtime-information-systems-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/changelog/crunchtime-information-systems-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/crunchtime-information-systems-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/sandbox/crunchtime-information-systems-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/crunchtime-information-systems-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/mcp/crunchtime-information-systems-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/crunchtime-information-systems-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/security/crunchtime-information-systems-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/crunchtime-information-systems-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/security/crunchtime-information-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crunchtime-information-systems-domain-security.yml
created: '2026-07-17'
description: Crunchtime (Crunchtime Information Systems) is a Boston-based provider of AI-powered operations-management software for multi-unit restaurants, founded in 1995 and serving 850+ restaurant brands across 150,000+ locations. Its platform unifies inventory management, labor scheduling, kitchen/operations execution, and analytics. Crunchtime publishes a public developer hub for its Inventory & Labor and Cruise data-integration REST APIs, letting partners and customers push and pull employees, locations, budgets, products, recipes, sales/menu mix, purchase orders, inventory counts, time clock, and forecasting data. Backed by Battery Ventures.
image: https://logo.clearbit.com/crunchtime.com
json_schemas:
- name: ApplicationUserDetailsGet
  property_count: 13
  slug: crunchtime-information-systems-application-user-details-get
- name: ApplicationUserDetails
  property_count: 13
  slug: crunchtime-information-systems-application-user-details
- name: DailyPrepDto
  property_count: 16
  slug: crunchtime-information-systems-daily-prep-dto
- name: EmployeeGet
  property_count: 129
  slug: crunchtime-information-systems-employee-get
- name: GeneralLedgerDto
  property_count: 13
  slug: crunchtime-information-systems-general-ledger-dto
- name: LocationDetailsGet
  property_count: 12
  slug: crunchtime-information-systems-location-details-get
- name: PurchaseOrderHeaderDto
  property_count: 89
  slug: crunchtime-information-systems-purchase-order-header-dto
- name: ScheduledBatchExportFiles
  property_count: 9
  slug: crunchtime-information-systems-scheduled-batch-export-files
- name: VendorGetDto
  property_count: 58
  slug: crunchtime-information-systems-vendor-get-dto
jsonld:
- class_count: 120
  name: Crunchtime Information Systems Context
  property_count: 575
  slug: crunchtime-information-systems-context
layout: provider
modified: '2026-07-18'
name: Crunchtime Information Systems
nav: Providers
network: true
overview: 'Crunchtime Information Systems publishes 38 API contracts indexed on the [APIs.io](https://apis.io/) network, including Application User Service API, Authentication Service API, Budget Service API, and 35 more. Tagged areas include Company, Restaurant, Food Service, Hospitality, and Inventory.


  The Crunchtime Information Systems catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Crunchtime Information Systems'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 27 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 1
  name: Crunchtime Information Systems Rate Limits
  slug: crunchtime-information-systems-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Crunchtime Information Systems API Rules
  rule_count: 18
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 4
  slug: crunchtime-information-systems-rules
score:
  band: strong
  composite: 56.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 27.7
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 61.6
    developer_ergonomics: 53.0
    discoverability: 80.4
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 28.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 37
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/screenshots/crunchtime-information-systems-2026-07-25T210822.png
security:
- kind: authentication
  name: Crunchtime Information Systems Authentication
  slug: crunchtime-information-systems-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Crunchtime Information Systems Domain Security
  slug: crunchtime-information-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Crunchtime Information Systems Trust Center
  slug: crunchtime-information-systems-trust-center
  summary_line: SOC 2, ISO 27001
slug: crunchtime-information-systems
tags:
- Company
- Restaurant
- Food Service
- Hospitality
- Inventory
- Labor Scheduling
- Operations Management
- Back Office
- Supply Chain
website: https://www.crunchtime.com/
---
