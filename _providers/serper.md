---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Serper Agentic Access
  operation_count: 10
  slug: serper-agentic-access
  summary_line: 10 operations · 10 acting
api_count: 14
apis:
- description: Search autocomplete suggestions
  name: Serper Autocomplete API
  slug: serper-autocomplete-api
- description: Image search results
  name: Serper Images API
  slug: serper-images-api
- description: Google Lens reverse image search from an image URL. Exposed to every playground user; costs 3 credits per query.
  name: Serper Lens API
  slug: serper-lens-api
- description: Canonical Google geo-target lookup for the location parameter used by every Serper search endpoint, plus a service health check. The only Serper surface that answers unauthenticated.
  name: Serper Locations API
  slug: serper-locations-api
- description: Maps and location search
  name: Serper Maps API
  slug: serper-maps-api
- description: News search results
  name: Serper News API
  slug: serper-news-api
- description: Patent search results
  name: Serper Patents API
  slug: serper-patents-api
- description: Local business and place search
  name: Serper Places API
  slug: serper-places-api
- description: Google place reviews by cid, fid or placeId, cursor-paginated with nextPageToken. The only Serper endpoint that uses cursor pagination and the only one where mini-batch is unsupported.
  name: Serper Reviews API
  slug: serper-reviews-api
- description: Academic publication search
  name: Serper Scholar API
  slug: serper-scholar-api
- description: Web search results
  name: Serper Search API
  slug: serper-search-api
- description: Product and shopping search results
  name: Serper Shopping API
  slug: serper-shopping-api
- description: Video search results
  name: Serper Videos API
  slug: serper-videos-api
- description: Fetch and extract the contents of a URL, optionally as markdown with images, links and videos. Served from a separate host and priced per difficulty at 2, 6 or 10 credits, with the credits consumed re
  name: Serper Webpage Scrape API
  slug: serper-webpage-scrape-api
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Serper Google Search Autocomplete API
  slug: open-serper-autocomplete-api
- collection_type: open
  name: Serper Google Search Autocomplete Images API
  slug: open-serper-images-api
- collection_type: open
  name: Serper Google Search Autocomplete Maps API
  slug: open-serper-maps-api
- collection_type: open
  name: Serper Google Search Autocomplete News API
  slug: open-serper-news-api
- collection_type: open
  name: Serper Google Search Autocomplete Patents API
  slug: open-serper-patents-api
- collection_type: open
  name: Serper Google Search Autocomplete Places API
  slug: open-serper-places-api
- collection_type: open
  name: Serper Google Search Autocomplete Scholar API
  slug: open-serper-scholar-api
- collection_type: open
  name: Serper Google Autocomplete Search API
  slug: open-serper-search-api
- collection_type: open
  name: Serper Google Search Autocomplete Shopping API
  slug: open-serper-shopping-api
- collection_type: open
  name: Serper Google Search Autocomplete Videos API
  slug: open-serper-videos-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/serper-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/serper-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/serper-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://serper.dev
- group: docs
  title: ''
  type: Documentation
  url: https://serper.dev
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Serper-API
- group: other
  title: ''
  type: X
  url: https://x.com/serperapi
- group: commercial
  title: ''
  type: Pricing
  url: https://serper.dev/#pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/serper-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/serper-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/serper-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/serper-packages.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/serper-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/serper-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/serper-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/serper-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/serper-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/serper-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://serper.betteruptime.com
- group: design
  title: ''
  type: Conventions
  url: conventions/serper-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/serper-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://serper.dev/playground
- group: docs
  title: ''
  type: APIReference
  url: https://serper.dev/playground
- group: other
  title: ''
  type: Playground
  url: https://serper.dev/playground
- group: start
  title: ''
  type: GettingStarted
  url: https://serper.dev/signup
- group: start
  title: ''
  type: SignUp
  url: https://serper.dev/signup
- group: start
  title: ''
  type: Login
  url: https://serper.dev/login
- group: operate
  title: ''
  type: Support
  url: mailto:support@serper.dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://serper.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://serper.dev/privacy
- group: other
  title: ''
  type: CookiePolicy
  url: https://serper.dev/cookies
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@serper/list/articles-3f700b49cbc4
created: '2026-06-13'
description: Serper is the world's fastest and most affordable Google Search API, delivering real-time SERP data in 1-2 seconds via a simple REST interface. It supports web search, images, news, maps, places, videos, shopping, scholar, patents, and autocomplete — all returned as structured JSON. Widely used in AI agents, LLM pipelines, and SEO tooling, Serper uses a credit-based model with 2,500 free queries and volume pricing down to $0.30 per 1,000 requests.
examples:
- key_count: 2
  name: Serper Autocomplete Example
  slug: serper-autocomplete-example
- key_count: 2
  name: Serper Image Search Example
  slug: serper-image-search-example
- key_count: 2
  name: Serper News Search Example
  slug: serper-news-search-example
- key_count: 2
  name: Serper Scholar Search Example
  slug: serper-scholar-search-example
- key_count: 2
  name: Serper Shopping Search Example
  slug: serper-shopping-search-example
- key_count: 2
  name: Serper Web Search Example
  slug: serper-web-search-example
finops:
- name: Serper Finops
  service_category: ''
  slug: serper-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/serper.png
json_schemas:
- name: Serper Search Request
  property_count: 8
  slug: serper-search-request
- name: Serper Search Response
  property_count: 6
  slug: serper-search-response
jsonld:
- class_count: 53
  name: Serper Context
  property_count: 30
  slug: serper-context
layout: provider
mcp_servers:
- description: ''
  name: serper-mcp.yml
  slug: serper-mcpyml
modified: '2026-08-13'
name: Serper
nav: Providers
network: true
overview: 'Serper publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Images API, Lens API, and 11 more. Tagged areas include Search, SERP, Google Search, AI, and LLM.


  The Serper catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Serper''s developer surface includes authentication, documentation, pricing, API reference, getting-started guide, signup flow, support, and 26 more developer resources.'
plans:
- name: Serper Plans Pricing
  plan_count: 5
  slug: serper-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 4
  name: Serper Rate Limits
  slug: serper-rate-limits
rules:
- name: Serper API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: serper-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 74.0
  delta: 22.8
  facets:
    commercial_clarity: 84.2
    contract_quality: 71.7
    developer_ergonomics: 73.9
    discoverability: 81.5
    governance: 79.2
    operational_transparency: 52.6
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/serper/refs/heads/main/screenshots/serper-2026-06-20T193723.png
security:
- kind: authentication
  name: Serper Authentication
  slug: serper-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Serper Domain Security
  slug: serper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: serper
tags:
- Search
- SERP
- Google Search
- AI
- LLM
- SEO
- Images
- News
- Maps
- Shopping
- Reviews
- Lens
- Scraping
- Locations
- SERP API
- Web Search
- Agents
- Patents
- Scholar
- Autocomplete
- Places
- Videos
website: https://serper.dev
---
