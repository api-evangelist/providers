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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Serper Agentic Access
  operation_count: 10
  slug: serper-agentic-access
  summary_line: 10 operations · 10 acting
api_count: 2
apis:
- baseURL: https://google.serper.dev
  baseurl_source: declared
  description: Search autocomplete suggestions
  name: Serper Autocomplete API
  slug: serper-autocomplete-api
- baseURL: https://google.serper.dev
  baseurl_source: declared
  description: Image search results
  name: Serper Images API
  slug: serper-images-api
- baseURL: https://google.serper.dev
  baseurl_source: declared
  description: Google Lens reverse image search from an image URL. Exposed to every playground user; costs 3 credits per query.
  name: Serper Lens API
  slug: serper-lens-api
- baseURL: https://api.serper.dev
  baseurl_source: declared
  description: Canonical Google geo-target lookup for the location parameter used by every Serper search endpoint, plus a service health check. The only Serper surface that answers unauthenticated.
  name: Serper Locations API
  slug: serper-locations-api
- baseURL: https://google.serper.dev
  baseurl_source: declared
  description: Maps and location search
  name: Serper Maps API
  slug: serper-maps-api
- baseURL: https://google.serper.dev
  baseurl_source: declared
  description: News search results
  name: Serper News API
  slug: serper-news-api
- baseURL: https://google.serper.dev
  baseurl_source: declared
  description: Patent search results
  name: Serper Patents API
  slug: serper-patents-api
- baseURL: https://google.serper.dev
  baseurl_source: declared
  description: Local business and place search
  name: Serper Places API
  slug: serper-places-api
- baseURL: https://google.serper.dev
  baseurl_source: declared
  description: Google place reviews by cid, fid or placeId, cursor-paginated with nextPageToken. The only Serper endpoint that uses cursor pagination and the only one where mini-batch is unsupported.
  name: Serper Reviews API
  slug: serper-reviews-api
- baseURL: https://google.serper.dev
  baseurl_source: declared
  description: Academic publication search
  name: Serper Scholar API
  slug: serper-scholar-api
- baseURL: https://google.serper.dev
  baseurl_source: declared
  description: Web search results
  name: Serper Search API
  slug: serper-search-api
- baseURL: https://google.serper.dev
  baseurl_source: declared
  description: Product and shopping search results
  name: Serper Shopping API
  slug: serper-shopping-api
- baseURL: https://google.serper.dev
  baseurl_source: declared
  description: Video search results
  name: Serper Videos API
  slug: serper-videos-api
- baseURL: https://google.serper.dev
  baseurl_source: declared
  description: Webpage content extraction
  name: Serper Scrape API
  slug: serper-scrape-api
artifact_total: 41
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
- group: other
  title: ''
  type: Overlay
  url: overlays/serper-webpage-scrape-api-overlay.yaml
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
  type: X-MCPServerCandidate
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
modified: '2026-08-13'
name: Serper
nav: Providers
network: true
overview: 'Serper publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Images API, Lens API, and 11 more. Tagged areas include Search, SERP, Google Search, Artificial Intelligence, and LLM.


  The Serper catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Serper''s developer surface includes authentication, documentation, pricing, API reference, getting-started guide, signup flow, support, and 27 more developer resources.'
plans:
- name: Serper Plans Pricing
  plan_count: 5
  slug: serper-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Serper Rate Limits
  slug: serper-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Serper API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: serper-jsonschema-spectral-rules
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 78.3
    catalog_earned_first_party: 24.0
    catalog_gap: 36.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 14.4
    contract_quality: 57.2
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 14.4
    operational_transparency: 36.8
  previous_composite: 57.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 28.6
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
- Artificial Intelligence
- LLM
- SEO
- Image
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
