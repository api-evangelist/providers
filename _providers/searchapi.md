---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.5
  scored_at: '2026-09-03'
api_count: 3
apis:
- baseURL: https://www.searchapi.io/api/v1/search
  baseurl_source: declared
  description: REST API returning structured JSON search results across 100+ engines (Google, Bing, Maps, News, Scholar, Images, Shopping, Trends, Jobs, YouTube, Amazon, Walmart, eBay). Single /api/v1/search endpoin
  name: SearchApi SERP API
  slug: searchapi-serp-api
- baseURL: https://www.searchapi.io/api/v1
  baseurl_source: declared
  description: The two account-management endpoints SearchApi documents alongside its SERP surface. GET /api/v1/me returns the calling key's monthly allowance, month-to-date usage, remaining credits, searches made i
  name: SearchApi Account & Analytics API
  slug: searchapi-account-analytics-api
- baseURL: https://www.searchapi.io/api/v1/search
  baseurl_source: declared
  description: Aggregated performance and error analytics for the account's own searches.
  name: SearchApi Analytics API
  slug: searchapi-analytics-api
artifact_total: 12
collections:
- collection_type: open
  name: SearchApi Account & Analytics API
  slug: open-searchapi-account-api
- collection_type: open
  name: SearchApi SERP API
  slug: open-searchapi-search-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.searchapi.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.searchapi.io/docs/google
- group: docs
  title: ''
  type: Documentation
  url: https://www.searchapi.io/docs/google
- group: docs
  title: ''
  type: APIReference
  url: https://www.searchapi.io/docs/google
- group: commercial
  title: ''
  type: Pricing
  url: https://www.searchapi.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.searchapi.io/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://www.searchapi.io/users/sign_in
- group: operate
  title: ''
  type: Support
  url: mailto:support@searchapi.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SearchApi
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.searchapi.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.searchapi.io/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.searchapi.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.searchapi.io/announcements
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/searchapiofficial/searchapi-official-postman-collection/
- group: auth
  title: ''
  type: Compliance
  url: https://www.searchapi.io/legal/dpa
- group: agent
  title: ''
  type: MCPServer
  url: mcp/searchapi-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/searchapi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/searchapi-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/searchapi-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/searchapi-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/searchapi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/searchapi-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/searchapi-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/searchapi-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/searchapi-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/searchapi-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/searchapi-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/searchapi-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/searchapi-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/searchapi-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/searchapi-data-model.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/searchapi-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/searchapi-search-api-overlay.yaml
- group: build
  title: ''
  type: PostmanCollection
  url: collections/searchapi-search-api.postman_collection.json
- group: build
  title: ''
  type: OpenCollection
  url: collections/searchapi-search-api.opencollection.json
created: '2026-07-23'
description: SearchApi is a real-time SERP and search-data API that gives applications and AI agents structured access to results from 100+ search engines — Google Search, Google Maps, Google News, Google Scholar, Google Images, Google Shopping, Google Trends, Google Jobs, YouTube, Bing, Baidu, and marketplace engines like Amazon, Walmart, and eBay — returning clean JSON instead of scraped HTML. It handles proxy rotation, CAPTCHA solving, and geographic/locale targeting server-side, and ships an MCP server plus "use-case bundles" that group selected endpoints around a job so agents can be handed a capability rather than a whole catalog. Used for SEO/rank tracking, market and price intelligence, RAG grounding, and agentic research workflows.
image: https://www.searchapi.io/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: SearchApi hosted MCP server
  slug: searchapi-hosted-mcp-server
modified: '2026-08-13'
name: SearchApi
nav: Providers
network: true
overview: 'SearchApi publishes 3 APIs on the [APIs.io](https://apis.io/) network: SERP API, Account & Analytics API, and Analytics API. Tagged areas include Search, SERP API, Google Search, Web Scraping, and Search data.


  SearchApi''s developer surface includes documentation, API reference, pricing, signup flow, support, changelog, authentication, and 29 more developer resources.'
plans:
- name: Searchapi Plans Pricing
  plan_count: 8
  slug: searchapi-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Searchapi Rate Limits
  slug: searchapi-rate-limits
scopes:
- name: Searchapi Scopes
  scope_count: 0
  slug: searchapi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 14.2
    developer_ergonomics: 49.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 50.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/searchapi/refs/heads/main/screenshots/searchapi-2026-08-17T081744.png
security:
- kind: authentication
  name: Searchapi Authentication
  slug: searchapi-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Searchapi Domain Security
  slug: searchapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Searchapi Trust Center
  slug: searchapi-trust-center
  summary_line: ISO/IEC 27001:2022, GDPR, SOC 2, PCI DSS, HIPAA, FedRAMP
slug: searchapi
tags:
- Search
- SERP API
- Google Search
- Web Scraping
- Search data
- Market Intelligence
- SEO
- MCP
- agent-native
website: https://www.searchapi.io/
---
