---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Serpapi Agentic Access
  operation_count: 3
  slug: serpapi-agentic-access
  summary_line: 3 operations
api_count: 10
apis:
- description: 'SerpApi Google Jobs results (engine=google_jobs) as structured JSON: job titles, companies, locations, descriptions, related links and apply options. Real-time scraping with proxies and CAPTCHA solvin'
  name: SerpApi Google Jobs API
  slug: serpapi-google-jobs-api
- description: 'SerpApi Google Local results (engine=google_local): local pack businesses with ratings, reviews, addresses, GPS coordinates and place ids. Real-time scraping with proxies and CAPTCHA solving handled b'
  name: SerpApi Google Local API
  slug: serpapi-google-local-api
- description: 'SerpApi Google Maps results (engine=google_maps): place search, place details, reviews, photos and directions as JSON. Real-time scraping with proxies and CAPTCHA solving handled by SerpApi; one GET h'
  name: SerpApi Google Maps API
  slug: serpapi-google-maps-api
- description: 'SerpApi Google Search results (engine=google) parsed into JSON: organic results, knowledge graph, answer box, ads, AI overview, related questions, local pack and more; output as JSON, raw HTML or Mark'
  name: SerpApi Google Search API
  slug: serpapi-google-search-api
- description: 'SerpApi Google Trends data (engine=google_trends): interest over time, interest by region, related topics and related queries. Real-time scraping with proxies and CAPTCHA solving handled by SerpApi; o'
  name: SerpApi Google Trends API
  slug: serpapi-google-trends-api
- baseURL: https://serpapi.com
  baseurl_source: declared
  description: 'SerpApi Account API: GET https://serpapi.com/account.json returns plan, searches left, extra credits, this/last hour usage and account_rate_limit_per_hour for the API key. Free; does not count as a se'
  name: SerpApi Account API
  slug: serpapi-account-api
- baseURL: https://serpapi.com
  baseurl_source: declared
  description: 'SerpApi Search API: GET https://serpapi.com/search with engine=<google|bing|baidu|yahoo|duckduckgo|youtube|amazon|ebay|...> returns parsed search engine results as JSON (or HTML / Markdown), and GET h'
  name: SerpApi Search API
  slug: serpapi-search-api
- description: 'SerpApi Extract API (engine=extract): GET https://serpapi.com/search?engine=extract&url=<page> returns the page as Markdown plus page information, meta tags, Open Graph, JSON-LD, inline links, images,'
  name: SerpApi Extract API
  slug: serpapi-extract-api
- description: 'SerpApi Locations API: GET https://serpapi.com/locations.json?q=<text>&limit=<n> (max 10) returns Google geo-targets with id, google_id, canonical_name, country_code, target_type, reach and gps, for u'
  name: SerpApi Locations API
  slug: serpapi-locations-api
- description: 'SerpApi Image API: multipart/form-data POST https://serpapi.com/image uploads a JPG/PNG/WebP image (max 500 KB) and returns an image_id, valid for 10 minutes, for reverse-image engines such as the Goo'
  name: SerpApi Image API
  slug: serpapi-image-api
artifact_total: 28
collections:
- collection_type: open
  name: SerpApi Search Account API
  slug: open-serpapi-account-api
- collection_type: open
  name: SerpApi Account Search API
  slug: open-serpapi-search-api
- collection_type: open
  name: SerpApi Search API
  slug: open-serpapi
common:
- group: other
  href: https://artifacts.apis.io/serpapi/capabilities/serpapi-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/serpapi-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/serpapi/rules/serpapi-rules.yml
  title: ''
  type: Spectral
  url: rules/serpapi-rules.yml
- group: design
  href: https://artifacts.apis.io/serpapi/json-ld/serpapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/serpapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/serpapi/vocabulary/serpapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/serpapi-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/serpapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/serpapi/data-model/serpapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/serpapi-data-model.yml
- group: build
  href: https://artifacts.apis.io/serpapi/cli/serpapi-cli.yml
  title: ''
  type: CLI
  url: cli/serpapi-cli.yml
- group: operate
  href: https://artifacts.apis.io/serpapi/changelog/serpapi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/serpapi-changelog.yml
- group: design
  href: https://artifacts.apis.io/serpapi/conventions/serpapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/serpapi-conventions.yml
- group: start
  href: https://artifacts.apis.io/serpapi/sandbox/serpapi-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/serpapi-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://serpapi.com/security
- group: operate
  href: https://artifacts.apis.io/serpapi/lifecycle/serpapi-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/serpapi-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/serpapi/lifecycle/serpapi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/serpapi-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/serpapi/errors/serpapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/serpapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/serpapi/conformance/serpapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/serpapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/serpapi/llms/serpapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/serpapi-llms.txt
- group: build
  href: https://artifacts.apis.io/serpapi/mcp/serpapi-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/serpapi-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/serpapi/well-known/serpapi-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/serpapi-www-security.txt
- group: auth
  href: https://artifacts.apis.io/serpapi/well-known/serpapi-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/serpapi-status-security.txt
- group: auth
  href: https://artifacts.apis.io/serpapi/well-known/serpapi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/serpapi-security.txt
- group: agent
  href: https://artifacts.apis.io/serpapi/well-known/serpapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/serpapi-well-known.yml
- group: other
  href: https://artifacts.apis.io/serpapi/hosts/serpapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/serpapi-hosts.yml
- group: build
  href: https://artifacts.apis.io/serpapi/integrations/serpapi-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/serpapi-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/serpapi/vendors/serpapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/serpapi-vendors.yml
- group: build
  href: https://artifacts.apis.io/serpapi/packages/serpapi-packages.yml
  title: ''
  type: SDKs
  url: packages/serpapi-packages.yml
- group: build
  href: https://artifacts.apis.io/serpapi/packages/serpapi-packages.yml
  title: ''
  type: Packages
  url: packages/serpapi-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.serpapi.com/
- group: commercial
  href: https://artifacts.apis.io/serpapi/plans/serpapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/serpapi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/serpapi/rate-limits/serpapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/serpapi-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/serpapi/finops/serpapi-finops.yml
  title: ''
  type: FinOps
  url: finops/serpapi-finops.yml
- group: company
  title: ''
  type: Website
  url: https://serpapi.com/
- group: agent
  href: https://artifacts.apis.io/serpapi/agentic-access/serpapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/serpapi-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/serpapi/security/serpapi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/serpapi-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/serpapi/security/serpapi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/serpapi-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/serpapi/security/serpapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/serpapi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/serpapi/authentication/serpapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/serpapi-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/serpapi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/serpapi
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/serpapi/serpapi/overview
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/serpapi/serpapi-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/serpapi/skills
- group: agent
  title: ''
  type: LlmsText
  url: https://serpapi.com/llms.txt
- group: company
  title: ''
  type: BlogRSS
  url: https://serpapi.com/blog/feed
- group: company
  title: ''
  type: Blog
  url: https://serpapi.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://serpapi.com/search-api
- group: docs
  title: ''
  type: APIReference
  url: https://serpapi.com/search-api
- group: start
  title: ''
  type: GettingStarted
  url: https://serpapi.com/integrations
- group: commercial
  title: ''
  type: Pricing
  url: https://serpapi.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://serpapi.com/release-notes
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/serpapi/public-roadmap
- group: start
  title: ''
  type: SignUp
  url: https://serpapi.com/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://serpapi.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://serpapi.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://serpapi.com/legal
- group: auth
  title: ''
  type: Security
  url: https://serpapi.com/security
- group: start
  title: ''
  type: Sandbox
  url: https://serpapi.com/playground
- group: company
  title: ''
  type: About
  url: https://serpapi.com/team
- group: company
  title: ''
  type: Newsroom
  url: https://serpapi.com/media
- group: operate
  title: ''
  type: Support
  url: mailto:support@serpapi.com
- group: operate
  title: ''
  type: FAQ
  url: https://serpapi.com/faq
created: '2024-11-07'
description: SerpApi is a real-time API for scraping and parsing search engine results. One GET https://serpapi.com/search request, selected by the engine parameter, returns structured JSON (or raw HTML or Markdown for LLMs) from Google (search, maps, jobs, trends, shopping, scholar, flights, hotels, news, images, AI Mode and AI Overview), Bing, Baidu, Yahoo, DuckDuckGo, Yandex, Naver, YouTube, Amazon, eBay, Walmart, Apple, TikTok and more; SerpApi handles proxies, CAPTCHAs and parsing. Extras cover the Search Archive, Account, Locations, Image upload and the Extract API; a hosted MCP server at mcp.serpapi.com and 12 client libraries (Ruby, Python, JavaScript, Go, PHP, Java, Rust, .NET, Swift, C++, CLI, MCP) are maintained by SerpApi, LLC (Austin, Texas).
finops:
- has_sources: false
  method: generated
  name: Serpapi Finops
  primary_unit: request
  service_category: API
  slug: serpapi-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/serpapi.png
json_schemas:
- name: GenericResponse
  property_count: 0
  slug: serpapi-generic-response
jsonld:
- class_count: 1
  name: Serpapi Context
  property_count: 1
  slug: serpapi-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: Remote MCP server at mcp.serpapi.com over streamable HTTP requiring an API key; 4 tools listed.
  name: SerpApi MCP Server
  slug: serpapi-mcp-server
modified: '2026-11-05'
name: SerpApi
nav: Providers
network: true
overview: 'SerpApi is listed with 10 APIs on the [APIs.io](https://apis.io/) network, including Account API, Search API, and 8 more. Tagged areas include Bing, Google, Search, Search Engines, and SERP.


  The SerpApi catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SerpApi''s developer surface includes CLI, changelog, sandbox, authentication, engineering blog, documentation, API reference, and 53 more developer resources.'
plans:
- name: Serpapi Plans Pricing
  plan_count: 63
  slug: serpapi-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 124
  name: Serpapi Rate Limits
  slug: serpapi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: SerpApi API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: serpapi-rules
score:
  band: exemplar
  composite: 75.0
  coverage:
    artifact_dirs: 36
    catalog_earned: 80.2
    catalog_earned_first_party: 24.0
    catalog_gap: 34.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 41.5
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 51.8
    developer_ergonomics: 81.0
    discoverability: 81.7
    operational_transparency: 92.1
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/serpapi/serpapi-2026-06-20T193722.png
security:
- kind: authentication
  name: Serpapi Authentication
  slug: serpapi-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Serpapi Domain Security
  slug: serpapi-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Serpapi Vulnerability Disclosure
  slug: serpapi-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Serpapi Trust Center
  slug: serpapi-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 2
skills:
- name: serpapi-web-search
  slug: serpapi-web-search-2
- name: serpapi-web-search
  slug: serpapi-web-search
slug: serpapi
tags:
- Bing
- Google
- Search
- Search Engines
- SERP
- Web Scraping
- AI Agents
- MCP
- Markdown
- Baidu
- DuckDuckGo
- YouTube
- Amazon
website: https://serpapi.com/
---
