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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.8
  scored_at: '2026-10-31'
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
artifact_total: 17
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
  type: Blog
  url: https://www.searchapi.io/press
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
  href: https://artifacts.apis.io/searchapi/mcp/searchapi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/searchapi-mcp.yml
- group: auth
  href: https://artifacts.apis.io/searchapi/authentication/searchapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/searchapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/searchapi/conventions/searchapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/searchapi-conventions.yml
- group: build
  href: https://artifacts.apis.io/searchapi/packages/searchapi-packages.yml
  title: ''
  type: Packages
  url: packages/searchapi-packages.yml
- group: operate
  href: https://artifacts.apis.io/searchapi/changelog/searchapi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/searchapi-changelog.yml
- group: design
  href: https://artifacts.apis.io/searchapi/lifecycle/searchapi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/searchapi-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/searchapi/conformance/searchapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/searchapi-conformance.yml
- group: auth
  href: https://artifacts.apis.io/searchapi/security/searchapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/searchapi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/searchapi/security/searchapi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/searchapi-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/searchapi/llms/searchapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/searchapi-llms.txt
- group: agent
  href: https://artifacts.apis.io/searchapi/well-known/searchapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/searchapi-well-known.yml
- group: auth
  href: https://artifacts.apis.io/searchapi/scopes/searchapi-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/searchapi-scopes.yml
- group: operate
  href: https://artifacts.apis.io/searchapi/rate-limits/searchapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/searchapi-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/searchapi/plans/searchapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/searchapi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/searchapi/errors/searchapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/searchapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/searchapi/data-model/searchapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/searchapi-data-model.yml
- group: build
  href: https://artifacts.apis.io/searchapi/mcp/searchapi-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/searchapi-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/searchapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/searchapi/overlays/searchapi-search-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/searchapi-search-api-overlay.yaml
- group: build
  href: https://artifacts.apis.io/searchapi/collections/searchapi-search-api.postman_collection.json
  title: ''
  type: PostmanCollection
  url: collections/searchapi-search-api.postman_collection.json
- group: build
  href: https://artifacts.apis.io/searchapi/collections/searchapi-search-api.opencollection.json
  title: ''
  type: OpenCollection
  url: collections/searchapi-search-api.opencollection.json
created: '2026-07-23'
description: SearchApi is a real-time SERP and search-data API that gives applications and AI agents structured access to results from 100+ search engines — Google Search, Google Maps, Google News, Google Scholar, Google Images, Google Shopping, Google Trends, Google Jobs, YouTube, Bing, Baidu, and marketplace engines like Amazon, Walmart, and eBay — returning clean JSON instead of scraped HTML. It handles proxy rotation, CAPTCHA solving, and geographic/locale targeting server-side, and ships an MCP server plus "use-case bundles" that group selected endpoints around a job so agents can be handed a capability rather than a whole catalog. Used for SEO/rank tracking, market and price intelligence, RAG grounding, and agentic research workflows.
finops:
- has_sources: true
  method: derived
  name: Searchapi Finops
  primary_unit: searches
  service_category: ''
  slug: searchapi-finops
  template: false
image: https://www.searchapi.io/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.searchapi.io over streamable HTTP; 19 tools listed.
  name: SearchApi hosted MCP server
  slug: searchapi
modified: '2026-10-06'
name: SearchApi
nav: Providers
network: true
overview: 'SearchApi is listed with 3 APIs on the [APIs.io](https://apis.io/) network: SERP API, Account & Analytics API, and Analytics API. Tagged areas include Search, SERP, Google Search, Web Scraping, and Search data.


  SearchApi''s developer surface includes engineering blog, documentation, API reference, pricing, signup flow, support, changelog, and 30 more developer resources.'
plans:
- name: Searchapi Plans Pricing
  plan_count: 9
  slug: searchapi-plans-pricing
- name: Searchapi Price Estimates
  plan_count: 0
  slug: searchapi-price-estimates
random_paper: 8
rate_limits:
- limit_count: 3
  name: Searchapi Rate Limits
  slug: searchapi-rate-limits
scopes:
- name: Searchapi Scopes
  scope_count: 1
  slug: searchapi-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 13.9
    developer_ergonomics: 51.8
    discoverability: 70.0
    operational_transparency: 68.4
  previous_composite: 53.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/searchapi/searchapi-2026-08-17T081744.png
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
skill_count: 3
skills:
- name: searchapi-grounded-web-research
  slug: searchapi-grounded-web-research
- name: searchapi-mcp-agent-connect
  slug: searchapi-mcp-agent-connect
- name: searchapi-quota-aware-batch
  slug: searchapi-quota-aware-batch
slug: searchapi
tags:
- Search
- SERP
- Google Search
- Web Scraping
- Search data
- Market Intelligence
- SEO
- MCP
- Agent-Native
website: https://www.searchapi.io/
---
