---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: REST API returning structured JSON search results across 100+ engines (Google, Bing, Maps, News, Scholar, Images, Shopping, Trends, Jobs, YouTube, Amazon, Walmart, eBay). Single /api/v1/search endpoin
  name: SearchApi SERP API
  slug: searchapi-serp-api
artifact_total: 4
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
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/searchapi-llms.txt
created: '2026-07-23'
description: SearchApi is a real-time SERP and search-data API that gives applications and AI agents structured access to results from 100+ search engines — Google Search, Google Maps, Google News, Google Scholar, Google Images, Google Shopping, Google Trends, Google Jobs, YouTube, Bing, Baidu, and marketplace engines like Amazon, Walmart, and eBay — returning clean JSON instead of scraped HTML. It handles proxy rotation, CAPTCHA solving, and geographic/locale targeting server-side, and ships an MCP server plus "use-case bundles" that group selected endpoints around a job so agents can be handed a capability rather than a whole catalog. Used for SEO/rank tracking, market and price intelligence, RAG grounding, and agentic research workflows.
image: https://www.searchapi.io/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: SearchApi hosted MCP server
  slug: searchapi-hosted-mcp-server
modified: '2026-07-24'
name: SearchApi
nav: Providers
network: true
overview: 'SearchApi publishes 1 API on the [APIs.io](https://apis.io/) network: SERP API. Tagged areas include search, serp-api, google-search, web-scraping, and search-data.


  SearchApi''s developer surface includes documentation, API reference, pricing, signup flow, support, changelog, authentication, and 17 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 38.6
  delta: -0.2
  facets:
    commercial_clarity: 52.6
    contract_quality: 15.1
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 38.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Searchapi Authentication
  slug: searchapi-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Searchapi Domain Security
  slug: searchapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: searchapi
tags:
- search
- serp-api
- google-search
- web-scraping
- search-data
- market-intelligence
- seo
- mcp
- agent-native
website: https://www.searchapi.io/
---
