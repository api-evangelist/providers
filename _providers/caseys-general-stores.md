---
access_model:
  confidence: high
  label: Key requested through a sign-in-gated developer portal
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - portal
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-09-05'
api_count: 21
apis:
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: Stores POS Activity Report documents from Casey's point-of-sale estate, implementing the Conexxus POS Back Office Interface / POS Activity Reporting API standard. Publishes report and journal document
  name: Casey's CasApi
  slug: caseys-casapi
- baseURL: https://esl.caseys.io/casgatewayapi
  baseurl_source: declared
  description: Gateway for POS POSJournal document management, implementing the Conexxus POS Back Office Interface standard. Accepts journal, report and journal-reconciliation postings and serves individual CPJR doc
  name: Casey's CasGatewayApi
  slug: caseys-casgatewayapi
- baseURL: https://esl.caseys.io/devopsmetricsapi
  baseurl_source: declared
  description: Internal DevOps metrics API. The publicly exported contract exposes only a v1 heartbeat health check and the OpenAPI document; the metrics operations themselves are not present in the published defini
  name: Casey's DevOpsMetricsApi
  slug: caseys-devopsmetricsapi
- baseURL: https://esl.caseys.io/digitalproductionplannerapi
  baseurl_source: declared
  description: GraphQL surface for digital production-planner data used by Casey's kitchen and prepared-food production planning. The published REST contract exposes a single POST /graphql operation plus the OpenAPI
  name: Casey's DigitalProductionPlannerApi
  slug: caseys-digitalproductionplannerapi
- baseURL: https://esl.caseys.io/fuelpriceapi
  baseurl_source: declared
  description: Returns fuel price data for Casey's stores. POST a list of store numbers to /fuelprices to retrieve current fuel pricing per store, with a heartbeat health check.
  name: Casey's FuelPriceApi
  slug: caseys-fuelpriceapi
- baseURL: https://esl.caseys.io/itemapi
  baseurl_source: declared
  description: Item Master (Pricebook) API. Returns up-to-date item data for a store, related items by UPC, and an unbuffered variant of the store-items read, alongside a GraphQL endpoint for item data.
  name: Casey's ItemApi
  slug: caseys-itemapi
- baseURL: https://esl.caseys.io/itsmapi
  baseurl_source: declared
  description: Creates, updates and attaches files to incidents in Casey's IT service management tool, with a v1 heartbeat health check.
  name: Casey's ItsmApi
  slug: caseys-itsmapi
- baseURL: https://esl.caseys.io/kitchensupplyorderingapi
  baseurl_source: declared
  description: GraphQL surface for kitchen supply ordering data used by Casey's prepared-food kitchens, plus a v1 heartbeat health check.
  name: Casey's KitchenSupplyOrderingapi
  slug: caseys-kitchensupplyorderingapi
- baseURL: https://esl.caseys.io/oldstoreapi
  baseurl_source: declared
  description: Legacy store-information API. Twenty-eight operations cover stores, brands, regions, hours and the organization hierarchy; the v0 surface is explicitly tagged deprecated in the published contract in f
  name: Casey's OldStoreApi
  slug: caseys-oldstoreapi
- baseURL: https://esl.caseys.io/powerinventoryapi
  baseurl_source: declared
  description: GraphQL surface for power inventory data, plus a v1 heartbeat health check.
  name: Casey's PowerInventoryApi
  slug: caseys-powerinventoryapi
- baseURL: https://esl.caseys.io/productionplannerapi
  baseurl_source: declared
  description: GraphQL surface for production-planner data driving prepared-food production schedules. The published REST contract exposes POST /graphql and the OpenAPI document only.
  name: Casey's ProductionPlannerApi
  slug: caseys-productionplannerapi
- baseURL: https://esl.caseys.io/shelflabelprintapi
  baseurl_source: declared
  description: GraphQL surface for shelf-label print data used to drive in-store shelf label printing, plus a v1 heartbeat health check.
  name: Casey's ShelfLabelPrintApi
  slug: caseys-shelflabelprintapi
- baseURL: https://esl.caseys.io/storeapi
  baseurl_source: declared
  description: The Store API represents key points of information about Casey's stores. Thirty-seven operations cover stores, store hours, amenities, brands, locations, districts, divisions, regions and the wider or
  name: Casey's StoreApi
  slug: caseys-storeapi
- baseURL: https://esl.caseys.io/storedetailsapi
  baseurl_source: declared
  description: Store detail reads across the Casey's estate — stores, brands, regions, hours and the all-stores organization hierarchy — as a twenty-three operation successor surface to the legacy store API.
  name: Casey's StoreDetailsApi
  slug: caseys-storedetailsapi
- baseURL: https://esl.caseys.io/storemessagingapi
  baseurl_source: declared
  description: Allows services running in a Casey's store to receive messages from external sources. Registers store agents (v1 and v2 registration), lists registered services, sends messages to a store, and carries
  name: Casey's StoreMessagingApi
  slug: caseys-storemessagingapi
- baseURL: https://esl.caseys.io/storenumberapi
  baseurl_source: declared
  description: The Store Number Generator API returns available store numbers and version/health information for Casey's store-numbering system.
  name: Casey's StoreNumberApi
  slug: caseys-storenumberapi
- baseURL: https://esl.caseys.io/supplierapi
  baseurl_source: declared
  description: Returns the list of suppliers for a given store and exposes a GraphQL endpoint for supplier data, plus a v1 heartbeat health check.
  name: Casey's SupplierApi
  slug: caseys-supplierapi
- baseURL: https://esl.caseys.io/tanklevelapi
  baseurl_source: declared
  description: Fuel tank telemetry. Reads the most recent tank level readings and accepts new tank level readings for Casey's fuel sites, with a v1 heartbeat health check.
  name: Casey's TankLevelApi
  slug: caseys-tanklevelapi
- baseURL: https://esl.caseys.io/taxapi
  baseurl_source: declared
  description: 'Tax calculation and configuration for Casey''s stores: POST /Taxes for tax calculation, plus per-store tax strategies, tax levels and compound taxes.'
  name: Casey's TaxApi
  slug: caseys-taxapi
- baseURL: https://esl.caseys.io/teammemberapi
  baseurl_source: declared
  description: Team member information API. The publicly exported contract exposes only the heartbeat health check and the OpenAPI document; the team member reads themselves are not present in the published definiti
  name: Casey's TeamMemberApi
  slug: caseys-teammemberapi
- baseURL: https://esl.caseys.io/vendorcheckinapi
  baseurl_source: declared
  description: GraphQL surface for vendor check-in data covering deliveries and vendor visits to Casey's stores, plus a v1 heartbeat health check.
  name: Casey's VendorCheckinApi
  slug: caseys-vendorcheckinapi
artifact_total: 25
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caseys-general-stores-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/caseys
- group: company
  title: ''
  type: Website
  url: https://www.caseys.com
- group: company
  title: ''
  type: About
  url: https://www.caseys.com/about-caseys
- group: company
  title: ''
  type: Careers
  url: https://www.caseys.com/careers
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.caseys.com/
- group: other
  title: ''
  type: Rewards
  url: https://www.caseys.com/rewards
- group: other
  title: ''
  type: Mobile
  url: https://www.caseys.com/mobile-app
- group: operate
  title: ''
  type: Contact
  url: https://www.caseys.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.caseys.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caseys.com/privacy-policy
- group: other
  title: ''
  type: Accessibility
  url: https://www.caseys.com/accessibility
- group: other
  title: ''
  type: Sitemap
  url: https://www.caseys.com/sitemap
- group: operate
  title: ''
  type: PressReleases
  url: https://investor.caseys.com/press-releases
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.esl.caseys.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.esl.caseys.io/
- group: start
  title: ''
  type: Login
  url: https://developer.esl.caseys.io/signin
- group: auth
  title: ''
  type: Authentication
  url: authentication/caseys-general-stores-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/caseys-general-stores-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/caseys-general-stores-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/caseys-general-stores-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/caseys-general-stores-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/caseys-general-stores-data-model.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/caseys-general-stores-tool-crosswalk.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/caseys-general-stores-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/caseys-general-stores-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/caseys-general-stores-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/caseys-general-stores-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/caseys-general-stores-rate-limits.yml
created: '2026-03-21'
description: 'Casey''s General Stores (NASDAQ: CASY) is one of the largest convenience-store chains in the United States, operating more than 2,900 stores selling fuel, made-from-scratch pizza, prepared food and convenience items, primarily in small midwestern communities. Behind the consumer brand Casey''s runs a B2B API estate on Azure API Management at esl.caseys.io: 21 published OpenAPI 3.0.1 contracts and 158 operations covering stores and the division/region/district hierarchy, the Item Master (Pricebook), fuel pricing, per-store tax configuration, fuel tank telemetry, suppliers, vendor check-in, kitchen production planning, shelf-label printing, in-store messaging and IT service-management incidents — plus Conexxus POS Back Office Interface document ingestion carrying Conexxus Open Retailing identifiers. Access is by Azure APIM subscription key requested through the developer portal at developer.esl.caseys.io; a UAT environment mirrors the estate. No pricing, rate limits, SDKs, status
  page, changelog, deprecation policy or MCP server are published.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/caseys-general-stores.png
layout: provider
modified: '2026-09-05'
name: Casey's General Stores
nav: Providers
network: true
overview: 'Casey''s General Stores publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Casey''s CasApi, Casey''s CasGatewayApi, Casey''s DevOpsMetricsApi, and 18 more. Tagged areas include APIs, Azure API Management, Conexxus, Convenience Stores, and Food Service.


  Casey''s General Stores'' developer surface includes getting-started guide, authentication, sandbox, and 27 more developer resources.'
plans:
- name: Caseys General Stores Plans Pricing
  plan_count: 0
  slug: caseys-general-stores-plans-pricing
press:
- date: '2026-05-25'
  title: Casey's General Stores announced Thursday that it was ...
  url: https://www.facebook.com/DakotaNewsNow/posts/caseys-general-stores-announced-thursday-that-it-was-added-to-the-sp-500-one-of-/1355783423246321/
- date: '2026-05-25'
  title: Nielsen broadens convenience channel coverage with ...
  url: https://nielseniq.com/global/en/news-center/2019/nielsen-broadens-convenience-channel-coverage-with-caseys-general-stores-inc/
- date: '2026-05-25'
  title: Casey's expands AI-powered ordering agents to more than ...
  url: https://cspdailynews.com/technologyservices/caseys-expands-ai-powered-ordering-agents-more-2600-stores
- date: '2026-05-25'
  title: Casey's, Pizza and the Quiet Power of AI
  url: https://www.wisdomtree.com/us/insights/blog/caseys-pizza-and-the-quiet-power-of-ai
- date: '2026-05-25'
  title: 'Q&A: The mind behind Casey''s digital transformation efforts'
  url: https://www.cstoredive.com/news/caseys-digital-transformation-art-sebastian-interview/636695/
random_paper: 2
rate_limits:
- limit_count: 0
  name: Caseys General Stores Rate Limits
  slug: caseys-general-stores-rate-limits
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 26.6
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 49.1
    developer_ergonomics: 42.3
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 9.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/screenshots/caseys-general-stores-2026-06-20T174033.png
security:
- kind: authentication
  name: Caseys General Stores Authentication
  slug: caseys-general-stores-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Caseys General Stores Domain Security
  slug: caseys-general-stores-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: caseys-general-stores
tags:
- APIs
- Azure API Management
- Conexxus
- Convenience Stores
- Food Service
- Fortune 500
- Fuel Pricing
- Fuel Retail
- GraphQL
- Item Data
- Loyalty
- OpenAPI
- Pizza
- Point of Sale
- Retail
- Store Locations
- Supply Chain
- Tax
website: https://www.caseys.com
---
