---
access_model:
  confidence: high
  label: Paid plans · Self-serve signup · Free trial
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - sandbox
  trial: true
  try_now: true
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Serpwow Agentic Access
  operation_count: 6
  slug: serpwow-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: 'The SerpWow platform — a real-time SERP API covering Google, Bing, Yahoo, Baidu, Yandex, Naver, Amazon and eBay, plus a Batches API for scheduled bulk collection, a free Locations API, a Destinations '
  name: SerpWow
  slug: serpwow
- baseURL: https://api.serpwow.com/live
  baseurl_source: declared
  description: The real-time Search API from SerpWow — GET /search, /places, /shopping, /news, /product and /place_reviews against https://api.serpwow.com/live, authenticated with an api_key query parameter and mete
  name: SerpWow Search API
  slug: serpwow-search-api
artifact_total: 13
asyncapis:
- description: ''
  name: Serpwow Batches Webhooks
  slug: serpwow-batches-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SerpWow Search API
  slug: open-serpwow-search-api
- collection_type: open
  name: SerpWow API
  slug: open-serpwow
common:
- group: company
  title: ''
  type: Website
  url: https://serpwow.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.trajectdata.com/serpwow
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trajectdata.com/serpwow/search-api/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trajectdata.com/serpwow/search-api/searches/common
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trajectdata.com/serpwow/search-api/getting-started/send-requests
- group: operate
  title: ''
  type: Support
  url: https://trajectdata.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://trajectdata.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://trajectdata.com/serp/serp-wow-api/
- group: start
  title: ''
  type: SignUp
  url: https://app.serpwow.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trajectdata.com/traject-data-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trajectdata.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://trajectdata.com/gdpr/
- group: operate
  title: ''
  type: StatusPage
  url: https://serpwow.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/serpwow-changelog.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/cyfebytraject/traject-data-apis/collection/5cd4b562-7a19-47be-ad54-c0e7d38e6579/serpwow-api
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/serpwow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/serpwow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/serpwow-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/serpwow-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/serpwow-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/serpwow-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/serpwow-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/serpwow-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/serpwow-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/serpwow-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/serpwow-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/serpwow-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/serpwow-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/serpwow-batches-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/serpwow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/serpwow-rate-limits.yml
created: '2025-01-07'
description: SerpWow is a real-time SERP (search engine results page) API from Traject Data. A single GET request to https://api.serpwow.com/live returns clean, structured JSON, HTML or CSV results from Google, Bing, Yahoo, Baidu, Yandex, Naver, Amazon or eBay, with fine-grained control over location (down to ZIP/postal code), device (desktop, tablet, mobile), language, country and result type — organic search, Maps places and reviews, Shopping, Product, News, Images, Videos, Scholar, Trends, Autocomplete, Reverse Image and Google AI Overviews. Alongside the real-time Search API, SerpWow ships a Batches API for scheduling up to 15,000 searches at a time with webhook or object-storage delivery, a free Locations API, a Destinations API that pushes result sets to S3, Google Cloud Storage, Azure Blob or any S3-compatible store, an Error Logs API, and an Account API for credit and platform-status telemetry. Billing is metered in credits with published per-tier overage rates, and requests that
  do not return HTTP 200 are not charged.
finops:
- name: Serpwow Finops
  service_category: API
  slug: serpwow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/serpwow.png
layout: provider
mcp_servers:
- description: SerpWow publishes no MCP server. Candidate tool list derived one-per-operationId from the repo's OpenAPI. Nothing here is served by the provider — do not read this as an agent surface.
  name: SerpWow MCP Server
  slug: serpwow-mcp-server
modified: '2026-08-27'
name: SerpWow
nav: Providers
network: true
overview: 'SerpWow publishes 1 API on the [APIs.io](https://apis.io/) network: Search API. Tagged areas include Search, SERP, Web Data, Scraping, and SEO.


  The SerpWow catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SerpWow''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Serpwow Plans Pricing
  plan_count: 5
  slug: serpwow-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 6
  name: Serpwow Rate Limits
  slug: serpwow-rate-limits
score:
  band: strong
  composite: 61.0
  coverage:
    artifact_dirs: 24
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 4.5
    contract_quality: 53.0
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 71.1
  previous_composite: 61.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/serpwow/refs/heads/main/screenshots/serpwow-2026-06-20T193727.png
security:
- kind: authentication
  name: Serpwow Authentication
  slug: serpwow-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Serpwow Domain Security
  slug: serpwow-domain-security
  summary_line: TLSv1.3 · DMARC
slug: serpwow
tags:
- Search
- SERP
- Web Data
- Scraping
- SEO
- Search Engines
- Google
- E-Commerce
- Market Intelligence
- Data Extraction
website: https://serpwow.com/
---
