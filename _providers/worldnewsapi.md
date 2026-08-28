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
  trial: false
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
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Worldnewsapi Agentic Access
  operation_count: 8
  slug: worldnewsapi-agentic-access
  summary_line: 8 operations
api_count: 7
apis:
- description: Extract article content and links from arbitrary news URLs.
  name: World News API Extract News API
  slug: worldnewsapi-extract-news-api
- description: Retrieve newspaper front-page images by country and date.
  name: World News API Front Pages API
  slug: worldnewsapi-front-pages-api
- description: Resolve a place name to latitude/longitude for local news search.
  name: World News API Geo Coordinates API
  slug: worldnewsapi-geo-coordinates-api
- description: Discover and inspect available news sources.
  name: World News API News Sources API
  slug: worldnewsapi-news-sources-api
- description: Retrieve full article records by id.
  name: World News API Retrieve News API
  slug: worldnewsapi-retrieve-news-api
- description: Full-text, semantic, and geo/local news search.
  name: World News API Search News API
  slug: worldnewsapi-search-news-api
- description: Country-level top news clustered by coverage.
  name: World News API Top News API
  slug: worldnewsapi-top-news-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: World News Extract News API
  slug: open-worldnewsapi-extract-news-api
- collection_type: open
  name: World News Extract News Front Pages API
  slug: open-worldnewsapi-front-pages-api
- collection_type: open
  name: World News Extract News Geo Coordinates API
  slug: open-worldnewsapi-geo-coordinates-api
- collection_type: open
  name: World News Extract News News Sources API
  slug: open-worldnewsapi-news-sources-api
- collection_type: open
  name: World News Extract News Retrieve News API
  slug: open-worldnewsapi-retrieve-news-api
- collection_type: open
  name: World News Extract News Search News API
  slug: open-worldnewsapi-search-news-api
- collection_type: open
  name: World News Extract News Top News API
  slug: open-worldnewsapi-top-news-api
- collection_type: open
  name: World News API
  slug: open-worldnewsapi
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/worldnewsapi-openapi-original.json
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/worldnewsapi-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/worldnewsapi-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/worldnewsapi-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/worldnewsapi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/worldnewsapi-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/worldnewsapi-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/worldnewsapi-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/worldnewsapi-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/worldnewsapi-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/worldnewsapi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/worldnewsapi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.worldnewsapi.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://worldnewsapi.com/docs/api-changelog/
- group: design
  title: ''
  type: Conventions
  url: conventions/worldnewsapi-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/worldnewsapi-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/worldnewsapi-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/worldnewsapi-search-news-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/worldnewsapi-top-news-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/worldnewsapi-extract-news-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/worldnewsapi-retrieve-news-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/worldnewsapi-front-pages-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/worldnewsapi-news-sources-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/worldnewsapi-geo-coordinates-api-overlay.yaml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ddsky
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/world-news-api
- group: company
  title: ''
  type: Website
  url: https://worldnewsapi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://worldnewsapi.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://worldnewsapi.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://worldnewsapi.com/docs/search-news/
- group: start
  title: ''
  type: GettingStarted
  url: https://worldnewsapi.com/docs/quick-start-tutorial/
- group: start
  title: ''
  type: Console
  url: https://worldnewsapi.com/newsroom/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/spoonacular-api/workspace/world-news-api/collection/7431899-9288f331-3732-4328-baad-1d1e53001875
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/GrmNknKHYD
- group: commercial
  title: ''
  type: Pricing
  url: https://worldnewsapi.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://worldnewsapi.com/console/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://worldnewsapi.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://worldnewsapi.com/terms/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ddsky/world-news-api-clients
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ddsky/world-news-api-mcp
- group: commercial
  title: ''
  type: Plans
  url: plans/worldnewsapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/worldnewsapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/worldnewsapi-finops.yml
created: '2026-07-11'
description: World News API is a real-time and historical news data API covering thousands of sources across 210+ countries and 86+ languages. It provides full-text and semantic news search, geo-targeted local news search (a radius filter around a latitude/longitude point), article content and link extraction from arbitrary URLs, country-level top news clustering, newspaper front-page images, and news-source discovery. Local news search is a first-class feature - resolve a place name to coordinates with the Geo Coordinates endpoint, then pass those coordinates to Search News via the location-filter parameter to find news published or mentioned near that place. Requests are authenticated with an API key (api-key query parameter or x-api-key header) and metered in points against a daily plan allowance, with X-API-Quota-* headers returning cost and remaining budget on every response. The provider publishes its own OpenAPI 3 document, generated client libraries for two dozen languages, and a
  first-party local-stdio MCP server exposing eight news tools to AI agents.
finops:
- name: Worldnewsapi Finops
  service_category: News and Media Data
  slug: worldnewsapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/worldnewsapi.png
layout: provider
mcp_servers:
- description: World News API publishes a first-party MCP server that exposes eight news tools over stdio. It is a locally installed npm package - there is no hosted remote MCP endpoint - so a human installs and run
  name: World News API MCP Server
  slug: world-news-api-mcp-server
modified: '2026-08-13'
name: World News API
nav: Providers
network: true
overview: 'World News API publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Extract News API, Front Pages API, Geo Coordinates API, and 4 more. Tagged areas include News, Local News, News Search, Media Monitoring, and Geo Search.


  World News API''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, developer console, support, and 37 more developer resources.'
plans:
- name: Worldnewsapi Plans Pricing
  plan_count: 4
  slug: worldnewsapi-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 6
  name: Worldnewsapi Rate Limits
  slug: worldnewsapi-rate-limits
score:
  band: strong
  composite: 64.4
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 16.7
    contract_quality: 53.7
    developer_ergonomics: 75.6
    discoverability: 74.1
    governance: 16.7
    operational_transparency: 73.7
  previous_composite: 64.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/worldnewsapi/refs/heads/main/screenshots/worldnewsapi-2026-08-17T080439.png
security:
- kind: authentication
  name: Worldnewsapi Authentication
  slug: worldnewsapi-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Worldnewsapi Domain Security
  slug: worldnewsapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: worldnewsapi
tags:
- News
- Local News
- News Search
- Media Monitoring
- Geo Search
- News Data
- Sentiment Analysis
- Content Extraction
- Front Pages
- MCP
- RSS
- Semantic Search
website: https://worldnewsapi.com
---
