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
  trial: false
  try_now: false
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
  score: 28.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 54
  human_in_the_loop: 0
  name: Crunchtime Agentic Access
  operation_count: 168
  slug: crunchtime-agentic-access
  summary_line: 168 operations · 54 acting
api_count: 4
apis:
- description: The Crunchtime Inventory & Labor API is a REST/JSON web-services API for integrating restaurant back-office data with the Crunchtime platform. It exposes 150+ operations organized by functional area —
  name: Crunchtime Inventory & Labor API
  slug: crunchtime-inventory-labor-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Application User service is used to create and retrieve user profiles where each user is assigned a unique User ID and password for logging in to Enterprise Manager, Net-Chef, or the Teamworx Mana
  name: Crunchtime Application User Service API
  slug: crunchtime-application-user-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Authentication Service is allowing to validate user access to a franchisee site using a username and password.
  name: Crunchtime Authentication Service API
  slug: crunchtime-authentication-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: 'The Budgets Service allows you to create and retrieve budgets for each post period at each location. Budget figures for each General Ledger can be entered either as currency values or as percentages. '
  name: Crunchtime Budget Service API
  slug: crunchtime-budget-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Category Service allows you to create and retrieve product categories.
  name: Crunchtime Category Service API
  slug: crunchtime-category-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Check Menu Mix Service allows for the import of Check and Item based data from the POS system in order to deplete inventory according to the Recipe configuration in Enterprise Manager. The get cal
  name: Crunchtime Check Menu Mix Service API
  slug: crunchtime-check-menu-mix-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Commissary Order Service allows you to retrieve commissary orders.
  name: Crunchtime Commissary Order Service API
  slug: crunchtime-commissary-order-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Company Product Service allows you to create and retrieve the global, above store list of products that can be used elsewhere in the application, including recipe components (see the Recipe Enhanc
  name: Crunchtime Company Product Enhanced Service API
  slug: crunchtime-company-product-enhanced-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Confirm Receipt Standard Service allows you to create and retrieve confirmation receipts.
  name: Crunchtime Confirm Receipt Standard Service API
  slug: crunchtime-confirm-receipt-standard-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Currency Ratios Service is used to enter the exchange rates that will to convert monetary values from one currency to another. The "toCurrencyCode" is equal to the base currency in Enterprise Mana
  name: Crunchtime Currency Ratio Service API
  slug: crunchtime-currency-ratio-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Customer Order Enhanced service allows you to create and retrieve customer orders.
  name: Crunchtime Customer Order Enhanced Service API
  slug: crunchtime-customer-order-enhanced-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Customer Service can be used to create a “Customer” that is an establishment or outlet to which a Crunchtime Location sells or distributes products and/or produced Recipe items. It may be an outle
  name: Crunchtime Customer Service API
  slug: crunchtime-customer-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Daily Prep Service allows you to create, update, finalize, cancel, or retrieve daily prep transactions.
  name: Crunchtime Daily Prep Service API
  slug: crunchtime-daily-prep-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Electronic Invoice service enables you to upload e-invoice data into Crunchtime.
  name: Crunchtime Electronic Invoice Service API
  slug: crunchtime-electronic-invoice-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Employee Service combines what used to be three Crunchtime Data Pump (CDP) imports into one API call with multiple arrays. The Employee Service is used to create or review an employee in Crunchtim
  name: Crunchtime Employee Service API
  slug: crunchtime-employee-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The General Ledger services allows the Crunchtime applications to be aligned with the company’s accounting and bookkeeping systems. General Ledger codes and descriptions are associated with P&L groupi
  name: Crunchtime General Ledger Service API
  slug: crunchtime-general-ledger-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Hierarchy Service is used to group locations together for reporting purposes. For example, if the company is a national restaurant chain divided into six regions, setting up the hierarchy configur
  name: Crunchtime Hierarchy Service API
  slug: crunchtime-hierarchy-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: 'The Inventory Service combines a series of get and post calls used to update and review the quantity and value of a location stock on hand including: -Inventory Adjustments (Waste) -Value Adjustments '
  name: Crunchtime Inventory Service API
  slug: crunchtime-inventory-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Location Product Pricing Service API from Crunchtime — 6 operation(s) for location product pricing service.
  name: Crunchtime Location Product Pricing Service API
  slug: crunchtime-location-product-pricing-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: 'The Locations Service allows you to review and configure general information about each location (restaurant, venue etc.) such as the address and phone number, as well as detailed preference settings '
  name: Crunchtime Location Service API
  slug: crunchtime-location-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Nutrition Service is used to create and retrieve data for Nutrition Product records.
  name: Crunchtime Nutrition Service API
  slug: crunchtime-nutrition-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Package Type Service offers a way to create, update, and retrieve package type entries.
  name: Crunchtime Package Type Service API
  slug: crunchtime-package-type-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Purchase by Invoice Service is used to create and retrieve purchasing data that is not directly associated with products. Typically this Service is used to record expenses for services, like month
  name: Crunchtime Pbi Service API
  slug: crunchtime-pbi-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Projected Consumption service is used to get Consumption data that has been systematically calculated based on a Location's Suggested Order configuration, or post Projected Consumption, overriding
  name: Crunchtime Projected Consumption Service API
  slug: crunchtime-projected-consumption-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Purchase Order Service allows you to create and retrieve vendor order records.
  name: Crunchtime Purchase Order Service API
  slug: crunchtime-purchase-order-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Recipe Service is used to create or extract recipe data including the header and component details. Recipes are created in Crunchtime for the purpose of inventory depletion. They are used to deple
  name: Crunchtime Recipe Enhanced Service API
  slug: crunchtime-recipe-enhanced-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Recipe Location Service allows you to create and retrieve location specific recipes.
  name: Crunchtime Recipe Location Service API
  slug: crunchtime-recipe-location-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Sales Forecasts Service can be used to ensure that Sales Forecasting data aligns between Crunchtime and other systems. You can use the service to get Forecast data that has been systematically cal
  name: Crunchtime Sales Forecast Service API
  slug: crunchtime-sales-forecast-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: 'The Sales Mix Service is used to align Crunchtime with Daily Sales Information generated in a PointofSale system. The data includes: Sales, Sales Tax, Paid Outs, Non Cash Media, Comps and Discounts an'
  name: Crunchtime Sales Mix Service API
  slug: crunchtime-sales-mix-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Scheduled Export service is an API that Crunchtime customers can use to download export files that have been generated via Scheduled Events in Enterprise Manager and convert the file content to JS
  name: Crunchtime Scheduled Export Service API
  slug: crunchtime-scheduled-export-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Storage Location service offers viewing and managing data associated with primary and secondary storage locations.
  name: Crunchtime Storage Location Service API
  slug: crunchtime-storage-location-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Supplemental Wage Service allows you to get or post Lump Sum or Hourly values to individual employees/positions for various supplemental earnings, such as tip sharing, vacation pay, sick pay, jury
  name: Crunchtime Supplemental Wage Service API
  slug: crunchtime-supplemental-wage-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Time Clock Enhanced service allows you to get or post employee time clock records that typically come from an external payroll or POS system. The post call will contain the original time punch dat
  name: Crunchtime Time Clock Enhanced Service API
  slug: crunchtime-time-clock-enhanced-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The User Defined Attributes (UDA) Service allows for the retrieval of the location and vendor User-Defined Attributes (UDAs). Location UDAs can be configured at the corporate level or specific to a pa
  name: Crunchtime Uda Service API
  slug: crunchtime-uda-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Vendor Location Service enables for quick setup of vendor locations for companies with large amounts of locationspecific information per vendor, such as payment terms, order minimums, email addres
  name: Crunchtime Vendor Location Service API
  slug: crunchtime-vendor-location-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Vendor Payment service allows you to create and retrieve payment information that typically comes from an Accounts Payable system. The Post call will update reconciled Vendor Orders and Purchase b
  name: Crunchtime Vendor Payment Service API
  slug: crunchtime-vendor-payment-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: Project Read Me - API Descriptions (SOURCE OF TRUTH) Project Read Me - API Descriptions (SOURCE OF TRUTH) 100% 10 Vendor Product Pricing Service 1 of 2 B22 Vendor Product Pricing Service [<<glossary:B
  name: Crunchtime Vendor Product Pricing Service API
  slug: crunchtime-vendor-product-pricing-service-api
- baseURL: https://webservices.net-chef.com
  baseurl_source: declared
  description: The Vendor Service is used to create/review records of all Vendors that can be used to record expenses in Crunchtime. Typically, a third-party system is the system of record for Vendors and vendor dat
  name: Crunchtime Vendor Service API
  slug: crunchtime-vendor-service-api
artifact_total: 53
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/agentic-access/crunchtime-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crunchtime-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/rules/crunchtime-rules.yml
  title: ''
  type: Spectral
  url: rules/crunchtime-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/json-ld/crunchtime-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crunchtime-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/vocabulary/crunchtime-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crunchtime-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/data-model/crunchtime-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crunchtime-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/hosts/crunchtime-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crunchtime-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/vendors/crunchtime-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crunchtime-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crunchtime.com/
- group: auth
  title: ''
  type: Security
  url: https://www.crunchtime.com/security
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
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crunchtime.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crunchtime.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.crunchtime.com/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/llms/crunchtime-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crunchtime-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/authentication/crunchtime-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crunchtime-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/conventions/crunchtime-conventions.yml
  title: ''
  type: Conventions
  url: conventions/crunchtime-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/errors/crunchtime-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crunchtime-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/rate-limits/crunchtime-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crunchtime-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/lifecycle/crunchtime-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/crunchtime-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/lifecycle/crunchtime-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/crunchtime-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/changelog/crunchtime-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/crunchtime-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/conformance/crunchtime-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crunchtime-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/security/crunchtime-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crunchtime-domain-security.yml
created: '2026-07-17'
description: Crunchtime (CrunchTime! Information Systems) is an AI-powered restaurant operations management platform used by 850+ multi-unit restaurant brands across 150,000+ locations to run inventory and food-cost control, labor and scheduling, operations execution (tasks, audits, temperature and food-prep labeling), kitchen display (KDS), guest/host-stand management, learning & development, and operational intelligence (Crunchtime Insights and Data Streaming). For integrators, Crunchtime publishes the Inventory & Labor developer hub — a REST/JSON API of 150+ operations (employees, locations, budgets, recipes, purchase orders, inventory counts, schedules, sales/menu-mix and more) served from the net-chef.com web services, authenticated with per-environment API tokens plus a site name and application user. The company merged with QSR Automations to cover the full restaurant food lifecycle and is a Battery Ventures portfolio company.
image: https://www.crunchtime.com/hubfs/2026-Crunchtime-Suite-ftr_@2x.jpg
json_schemas:
- name: ApplicationUserDetailsGet
  property_count: 13
  slug: crunchtime-application-user-details-get
- name: ApplicationUserDetails
  property_count: 13
  slug: crunchtime-application-user-details
- name: DailyPrepDto
  property_count: 16
  slug: crunchtime-daily-prep-dto
- name: EmployeeGet
  property_count: 129
  slug: crunchtime-employee-get
- name: GeneralLedgerDto
  property_count: 13
  slug: crunchtime-general-ledger-dto
- name: LocationDetailsGet
  property_count: 12
  slug: crunchtime-location-details-get
- name: PurchaseOrderHeaderDto
  property_count: 89
  slug: crunchtime-purchase-order-header-dto
- name: ScheduledBatchExportFiles
  property_count: 9
  slug: crunchtime-scheduled-batch-export-files
- name: VendorGetDto
  property_count: 58
  slug: crunchtime-vendor-get-dto
jsonld:
- class_count: 120
  name: Crunchtime Context
  property_count: 575
  slug: crunchtime-context
layout: provider
modified: '2026-07-18'
name: Crunchtime
nav: Providers
network: true
overview: 'Crunchtime publishes 38 API contracts indexed on the [APIs.io](https://apis.io/) network, including Application User Service API, Authentication Service API, Budget Service API, and 35 more. Tagged areas include Company, Restaurant Operations, Inventory, Labor & Scheduling, and Food Cost.


  The Crunchtime catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Crunchtime''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 4
  name: Crunchtime Rate Limits
  slug: crunchtime-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Crunchtime API Rules
  rule_count: 18
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 4
  slug: crunchtime-rules
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 21.0
  facets:
    access_clarity: 42.1
    contract_governance: 35.6
    contract_quality: 61.6
    developer_ergonomics: 57.1
    discoverability: 80.4
    operational_transparency: 81.6
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 37
    mcp: derived
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
screenshot: https://raw.githubusercontent.com/api-evangelist/crunchtime/refs/heads/main/screenshots/crunchtime-2026-07-25T210820.png
security:
- kind: authentication
  name: Crunchtime Authentication
  slug: crunchtime-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Crunchtime Domain Security
  slug: crunchtime-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crunchtime
tags:
- Company
- Restaurant Operations
- Inventory
- Labor & Scheduling
- Food Cost
- Kitchen Display
- Point-of-Sale
- Supply Chain
- Hospitality
- REST API
- Food and Beverage
website: https://www.crunchtime.com/
---
