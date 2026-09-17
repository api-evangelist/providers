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
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-09-16'
api_count: 21
apis:
- baseURL: https://esl.caseys.io/itemapi
  baseurl_source: declared
  description: Item Master (Pricebook) API. Returns up-to-date item data for a store, related items by UPC, and an unbuffered variant of the store-items read, alongside a GraphQL endpoint for item data.
  name: Casey's ItemApi
  slug: caseys-itemapi
- baseURL: https://esl.caseys.io/storeapi
  baseurl_source: declared
  description: The Store API represents key points of information about Casey's stores. Thirty-seven operations cover stores, store hours, amenities, brands, locations, districts, divisions, regions and the wider or
  name: Casey's StoreApi
  slug: caseys-storeapi
- baseURL: https://esl.caseys.io/supplierapi
  baseurl_source: declared
  description: Returns the list of suppliers for a given store and exposes a GraphQL endpoint for supplier data, plus a v1 heartbeat health check.
  name: Casey's SupplierApi
  slug: caseys-supplierapi
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The brands API from Casey's General Stores — 2 operation(s) for brands.
  name: Casey's General Stores Brands API
  slug: caseys-general-stores-brands-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Caseys.StoreApi API from Casey's General Stores — 1 operation(s) for caseys.storeapi.
  name: Casey's General Stores Caseys.Store API
  slug: caseys-general-stores-caseys-storeapi-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Caseys.StoreNumberGenerator.Api API from Casey's General Stores — 2 operation(s) for caseys.storenumbergenerator.api.
  name: Casey's General Stores Caseys.Store Number Generator.Api API
  slug: caseys-general-stores-caseys-storenumbergenerator-api-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Districts API from Casey's General Stores — 2 operation(s) for districts.
  name: Casey's General Stores Districts API
  slug: caseys-general-stores-districts-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Divisions API from Casey's General Stores — 2 operation(s) for divisions.
  name: Casey's General Stores Divisions API
  slug: caseys-general-stores-divisions-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Health API from Casey's General Stores — 1 operation(s) for health.
  name: Casey's General Stores Health API
  slug: caseys-general-stores-health-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The heartbeat API from Casey's General Stores — 2 operation(s) for heartbeat.
  name: Casey's General Stores Heartbeat API
  slug: caseys-general-stores-heartbeat-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The hours API from Casey's General Stores — 4 operation(s) for hours.
  name: Casey's General Stores Hours API
  slug: caseys-general-stores-hours-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The incident API from Casey's General Stores — 2 operation(s) for incident.
  name: Casey's General Stores Incident API
  slug: caseys-general-stores-incident-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Location API from Casey's General Stores — 2 operation(s) for location.
  name: Casey's General Stores Location API
  slug: caseys-general-stores-location-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The organization hierarchy API from Casey's General Stores — 12 operation(s) for organization hierarchy.
  name: Casey's General Stores organization hierarchy API
  slug: caseys-general-stores-organization-hierarchy-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Organizational API from Casey's General Stores — 3 operation(s) for organizational.
  name: Casey's General Stores Organizational API
  slug: caseys-general-stores-organizational-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Print API from Casey's General Stores — 1 operation(s) for print.
  name: Casey's General Stores Print API
  slug: caseys-general-stores-print-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The pull API from Casey's General Stores — 2 operation(s) for pull.
  name: Casey's General Stores Pull API
  slug: caseys-general-stores-pull-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The push API from Casey's General Stores — 3 operation(s) for push.
  name: Casey's General Stores Push API
  slug: caseys-general-stores-push-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Regions API from Casey's General Stores — 2 operation(s) for regions.
  name: Casey's General Stores Regions API
  slug: caseys-general-stores-regions-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Register API from Casey's General Stores — 2 operation(s) for register.
  name: Casey's General Stores Register API
  slug: caseys-general-stores-register-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Registrations API from Casey's General Stores — 1 operation(s) for registrations.
  name: Casey's General Stores Registrations API
  slug: caseys-general-stores-registrations-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The StoreAmenities API from Casey's General Stores — 1 operation(s) for storeamenities.
  name: Casey's General Stores Store Amenities API
  slug: caseys-general-stores-storeamenities-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The StoreOrganizational API from Casey's General Stores — 2 operation(s) for storeorganizational.
  name: Casey's General Stores Store Organizational API
  slug: caseys-general-stores-storeorganizational-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Stores API from Casey's General Stores — 6 operation(s) for stores.
  name: Casey's General Stores Stores API
  slug: caseys-general-stores-stores-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Swagger API from Casey's General Stores — 1 operation(s) for swagger.
  name: Casey's General Stores Swagger API
  slug: caseys-general-stores-swagger-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The tankLevels API from Casey's General Stores — 2 operation(s) for tanklevels.
  name: Casey's General Stores Tank Levels API
  slug: caseys-general-stores-tanklevels-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Taxes API from Casey's General Stores — 1 operation(s) for taxes.
  name: Casey's General Stores Taxes API
  slug: caseys-general-stores-taxes-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Unbuffered Store Items API from Casey's General Stores — 1 operation(s) for unbuffered store items.
  name: Casey's General Stores Unbuffered Store Items API
  slug: caseys-general-stores-unbuffered-store-items-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The v0 API from Casey's General Stores — 1 operation(s) for v0.
  name: Casey's General Stores V0 API
  slug: caseys-general-stores-v0-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The v1 API from Casey's General Stores — 1 operation(s) for v1.
  name: Casey's General Stores V1 API
  slug: caseys-general-stores-v1-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The V1StoreById API from Casey's General Stores — 1 operation(s) for v1storebyid.
  name: Casey's General Stores V1 Store By ID API
  slug: caseys-general-stores-v1storebyid-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The V1StoreHours API from Casey's General Stores — 1 operation(s) for v1storehours.
  name: Casey's General Stores V1 Store Hours API
  slug: caseys-general-stores-v1storehours-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The V1StoreHoursByStoreNumber API from Casey's General Stores — 1 operation(s) for v1storehoursbystorenumber.
  name: Casey's General Stores V1 Store Hours By Store Number API
  slug: caseys-general-stores-v1storehoursbystorenumber-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The V1Stores API from Casey's General Stores — 1 operation(s) for v1stores.
  name: Casey's General Stores V1 Stores API
  slug: caseys-general-stores-v1stores-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The v2 API from Casey's General Stores — 1 operation(s) for v2.
  name: Casey's General Stores V2 API
  slug: caseys-general-stores-v2-api
- baseURL: https://esl.caseys.io/casapi
  baseurl_source: declared
  description: The Version API from Casey's General Stores — 1 operation(s) for version.
  name: Casey's General Stores Version API
  slug: caseys-general-stores-version-api
- baseURL: https://esl.caseys.io/itemapi
  baseurl_source: declared
  description: The Fuel Prices API from Casey's General Stores — 1 operation(s) for fuel prices.
  name: Casey's General Stores Fuel Prices API
  slug: caseys-general-stores-fuel-prices-api
- baseURL: https://esl.caseys.io/itemapi
  baseurl_source: declared
  description: The Graph QL API from Casey's General Stores — 1 operation(s) for graph ql.
  name: Casey's General Stores Graph QL API
  slug: caseys-general-stores-graph-ql-api
- baseURL: https://esl.caseys.io/itemapi
  baseurl_source: declared
  description: The Open API API from Casey's General Stores — 2 operation(s) for open api.
  name: Casey's General Stores Open API
  slug: caseys-general-stores-open-api-api
artifact_total: 43
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-cas-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-cas-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-cas-gateway-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-cas-gateway-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-devops-metrics-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-devops-metrics-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-digital-production-planner-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-digital-production-planner-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-fuel-price-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-fuel-price-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-itsm-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-itsm-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-kitchen-supply-ordering-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-kitchen-supply-ordering-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-old-store-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-old-store-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-power-inventory-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-power-inventory-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-production-planner-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-production-planner-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-shelf-label-print-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-shelf-label-print-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-store-details-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-store-details-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-store-messaging-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-store-messaging-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-store-number-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-store-number-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-tank-level-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-tank-level-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-tax-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-tax-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-team-member-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-team-member-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/overlays/caseys-general-stores-vendor-checkin-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/caseys-general-stores-vendor-checkin-api-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/security/caseys-general-stores-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/authentication/caseys-general-stores-authentication.yml
  title: ''
  type: Authentication
  url: authentication/caseys-general-stores-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/conventions/caseys-general-stores-conventions.yml
  title: ''
  type: Conventions
  url: conventions/caseys-general-stores-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/errors/caseys-general-stores-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/caseys-general-stores-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/lifecycle/caseys-general-stores-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/caseys-general-stores-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/conformance/caseys-general-stores-conformance.yml
  title: ''
  type: Conformance
  url: conformance/caseys-general-stores-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/data-model/caseys-general-stores-data-model.yml
  title: ''
  type: DataModel
  url: data-model/caseys-general-stores-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/mcp/caseys-general-stores-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/caseys-general-stores-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/mcp/caseys-general-stores-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/caseys-general-stores-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/llms/caseys-general-stores-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caseys-general-stores-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/sandbox/caseys-general-stores-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/caseys-general-stores-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/plans/caseys-general-stores-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/caseys-general-stores-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/caseys-general-stores/refs/heads/main/rate-limits/caseys-general-stores-rate-limits.yml
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
overview: 'Casey''s General Stores publishes 39 APIs on the [APIs.io](https://apis.io/) network, including Casey''s ItemApi, Casey''s StoreApi, Casey''s SupplierApi, and 36 more. Tagged areas include Azure API Management, Conexxus, Convenience Stores, Food Service, and Fortune 500.


  Casey''s General Stores'' developer surface includes getting-started guide, authentication, sandbox, and 45 more developer resources.'
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
random_paper: 10
rate_limits:
- limit_count: 0
  name: Caseys General Stores Rate Limits
  slug: caseys-general-stores-rate-limits
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 49.5
    developer_ergonomics: 42.3
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 37.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 39
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 27.8
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
- Point-of-Sale
- Retail
- Store Locations
- Supply Chain
- Tax
website: https://www.caseys.com
---
