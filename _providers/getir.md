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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 39
  human_in_the_loop: 1
  name: Getir Agentic Access
  operation_count: 62
  slug: getir-agentic-access
  summary_line: 62 operations · 39 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://food-external-api-gateway.getirapi.com
  baseurl_source: declared
  description: 'Secret keys provided to your company will be used for login. After successful login, you must use the token returned to your company in other endpoints. The validity period of the token is 1 hour, at '
  name: Getir Auth API
  slug: getir-auth-api
- baseURL: https://food-external-api-gateway.getirapi.com
  baseurl_source: declared
  description: The chain-menus API from Getir — 4 operation(s) for chain-menus.
  name: Getir Chain Menus API
  slug: getir-chain-menus-api
- baseURL: https://food-external-api-gateway.getirapi.com
  baseurl_source: declared
  description: The changelog API from Getir — 1 operation(s) for changelog.
  name: Getir Changelog API
  slug: getir-changelog-api
- baseURL: https://food-external-api-gateway.getirapi.com
  baseurl_source: declared
  description: Endpoints about food orders
  name: Getir Food Orders API
  slug: getir-food-orders-api
- baseURL: https://food-external-api-gateway.getirapi.com
  baseurl_source: declared
  description: This endpoint can be used to check the health of the application
  name: Getir Health API
  slug: getir-health-api
- baseURL: https://food-external-api-gateway.getirapi.com
  baseurl_source: declared
  description: The payment-methods API from Getir — 1 operation(s) for payment-methods.
  name: Getir Payment Methods API
  slug: getir-payment-methods-api
- baseURL: https://food-external-api-gateway.getirapi.com
  baseurl_source: declared
  description: Endpoints in the products section can be used with product information obtained from restaurant endpoints.
  name: Getir Products API
  slug: getir-products-api
- baseURL: https://food-external-api-gateway.getirapi.com
  baseurl_source: declared
  description: Endpoints about restaurant and courier opening and closing features can be seen in the restaurants section.
  name: Getir Restaurants API
  slug: getir-restaurants-api
artifact_total: 15
asyncapis:
- description: ''
  name: Getir Food Webhooks
  slug: getir-food-webhooks
collections:
- collection_type: open
  name: GetirFood API Documentation
  slug: open-getir-food
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/getir-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://getir.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.getir.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.getir.com/food/documentation/giris
- group: docs
  title: ''
  type: APIReference
  url: https://developers.getir.com/food/api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.getir.com/food/documentation/giris
- group: operate
  title: ''
  type: Support
  url: mailto:getiryemekapi@getir.com
- group: operate
  title: ''
  type: StatusPage
  url: https://getir-food-integration.instatus.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getir
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getir.com/yardim/gizlilik-politikasi/
- group: auth
  title: ''
  type: Authentication
  url: authentication/getir-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/getir-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/getir-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/getir-food-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/getir-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/getir-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/getir-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/getir-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/getir-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/getir-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/getir-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/getir-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/getir-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getir-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/getir-food-overlay.yaml
created: '2026-07-31'
description: 'Getir is an Istanbul-based on-demand delivery company, founded in 2015, that pioneered the ultrafast "groceries in minutes" model and grew into a super-app spanning rapid grocery (Getir), large-basket grocery (GetirBüyük), water (GetirSu), restaurant food delivery (GetirYemek / GetirFood) and local-merchant commerce (GetirÇarşı / GetirLocals). Its developer-facing surface is a partner-integration platform rather than a public product API: Getir publishes the GetirFood API — a Swagger 2.0 contract at food-external-api-gateway.getirapi.com covering restaurant onboarding, menu and product status, working hours, delivery zones, payment methods and the full food-order lifecycle (verify, prepare, handover, deliver, cancel, transfer) — for POS and integrator companies that connect restaurant point-of-sale systems to GetirFood. Orders are pushed to partners over webhooks, with a documented rate limiter, a 99-entry service error registry, published test cards and a dedicated test environment.
  In February 2026 Uber agreed to acquire Getir''s Türkiye delivery business, cleared by the Turkish Competition Authority in June 2026.'
image: https://developers.getir.com/assets/getir-developers-logo-BbJf7m5Z.svg
layout: provider
mcp_servers:
- description: Getir publishes NO official MCP server. Searched the developer portal, the docs content API, the GitHub org (0 public repos), npm under @modelcontextprotocol and the MCP registries — no first-party ho
  name: Getir MCP Server
  slug: getir-mcp-server
modified: '2026-07-31'
name: Getir
nav: Providers
network: true
overview: 'Getir publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Chain Menus API, Changelog API, and 5 more. Tagged areas include Company, Food Delivery, Grocery Delivery, On-Demand Delivery, and Logistics.


  The Getir catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Getir''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, changelog, and 19 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 3
  name: Getir Rate Limits
  slug: getir-rate-limits
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 47.1
    developer_ergonomics: 25.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 57.9
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getir/refs/heads/main/screenshots/getir-2026-08-07T165703.png
security:
- kind: authentication
  name: Getir Authentication
  slug: getir-authentication
  summary_line: custom-token · 1 scheme
- kind: domain-security
  name: Getir Domain Security
  slug: getir-domain-security
  summary_line: TLSv1.3 · DMARC
slug: getir
tags:
- Company
- Food Delivery
- Grocery Delivery
- On-Demand Delivery
- Logistics
- Restaurant
- Point-of-Sale
- Marketplace
- Turkey
- Partner Integration
website: https://getir.com/
---
