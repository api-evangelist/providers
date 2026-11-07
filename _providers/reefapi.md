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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Hosted MCP server over streamable-HTTP with 5 discovery-first tools (search_engines, get_catalog, get_engine_schema, get_action_schema, call_engine). Auth via Authorization: Bearer ak_live_ key. Compa'
  name: ReefAPI MCP Server
  slug: reefapi-mcp-server
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: The Classifieds & Second-hand API from ReefAPI — 29 operation(s) for classifieds & second-hand.
  name: ReefAPI Classifieds & Second-hand API
  slug: reefapi-classifieds-second-hand-api
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: The Developer Tools API from ReefAPI — 263 operation(s) for developer tools.
  name: ReefAPI Developer Tools API
  slug: reefapi-developer-tools-api
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: The E-commerce & Marketplaces API from ReefAPI — 264 operation(s) for e-commerce & marketplaces.
  name: ReefAPI E-commerce & Marketplaces API
  slug: reefapi-e-commerce-marketplaces-api
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: The Finance & Data API from ReefAPI — 103 operation(s) for finance & data.
  name: ReefAPI Finance & Data API
  slug: reefapi-finance-data-api
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: The Government & Tenders API from ReefAPI — 5 operation(s) for government & tenders.
  name: ReefAPI Government & Tenders API
  slug: reefapi-government-tenders-api
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: The Jobs & Hiring API from ReefAPI — 69 operation(s) for jobs & hiring.
  name: ReefAPI Jobs & Hiring API
  slug: reefapi-jobs-hiring-api
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: The Media, Film & Knowledge API from ReefAPI — 274 operation(s) for media, film & knowledge.
  name: ReefAPI Media, Film & Knowledge API
  slug: reefapi-media-film-knowledge-api
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: The Other API from ReefAPI — 57 operation(s) for other.
  name: ReefAPI Other API
  slug: reefapi-other-api
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: The Real Estate API from ReefAPI — 57 operation(s) for real estate.
  name: ReefAPI Real Estate API
  slug: reefapi-real-estate-api
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: The Reputation & Reviews API from ReefAPI — 76 operation(s) for reputation & reviews.
  name: ReefAPI Reputation & Reviews API
  slug: reefapi-reputation-reviews-api
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: The Search & SEO API from ReefAPI — 8 operation(s) for search & seo.
  name: ReefAPI Search & SEO API
  slug: reefapi-search-seo-api
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: The Social Media API from ReefAPI — 117 operation(s) for social media.
  name: ReefAPI Social Media API
  slug: reefapi-social-media-api
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: The Travel & Lodging API from ReefAPI — 43 operation(s) for travel & lodging.
  name: ReefAPI Travel & Lodging API
  slug: reefapi-travel-lodging-api
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: The Utilities & AI API from ReefAPI — 163 operation(s) for utilities & ai.
  name: ReefAPI Utilities & AI API
  slug: reefapi-utilities-ai-api
artifact_total: 26
common:
- group: other
  href: https://artifacts.apis.io/reefapi/capabilities/reefapi-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/reefapi-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/reefapi/overlays/reefapi-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/reefapi-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.reefapi.com/
- group: commercial
  title: ''
  type: License
  url: https://github.com/reefapi/reefapi-mcp/blob/main/LICENSE
- group: auth
  href: https://artifacts.apis.io/reefapi/security/reefapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reefapi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/reefapi/authentication/reefapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/reefapi-authentication.yml
- group: agent
  href: https://artifacts.apis.io/reefapi/well-known/reefapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/reefapi-well-known.yml
- group: other
  href: https://artifacts.apis.io/reefapi/well-known/reefapi-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/reefapi-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/reefapi/llms/reefapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reefapi-llms.txt
- group: build
  href: https://artifacts.apis.io/reefapi/packages/reefapi-packages.yml
  title: ''
  type: Packages
  url: packages/reefapi-packages.yml
- group: design
  href: https://artifacts.apis.io/reefapi/conformance/reefapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reefapi-conformance.yml
- group: design
  href: https://artifacts.apis.io/reefapi/lifecycle/reefapi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/reefapi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://reefapi.com/status
- group: start
  href: https://artifacts.apis.io/reefapi/sandbox/reefapi-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/reefapi-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/reefapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/reefapi/plans/reefapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/reefapi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/reefapi/rate-limits/reefapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/reefapi-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://reefapi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://reefapi.com/signup
- group: start
  title: ''
  type: Login
  url: https://reefapi.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reefapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reefapi.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://reefapi.com/about
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reefapi
- group: start
  title: ''
  type: Console
  url: https://reefapi.com/playground
- group: start
  title: ''
  type: GettingStarted
  url: https://reefapi.com/guides
created: '2026-08-30'
description: 'ReefAPI is a unified web-data gateway that fronts 183 production data engines - Amazon, Zillow, Reddit, Trustpilot, LinkedIn Jobs, Indeed, Google Maps, Booking.com, StockX, YouTube and more - behind ONE JSON contract, ONE API key and ONE shared credit pool. Every one of its 1,528 operations is POST https://api.reefapi.com/{engine}/v1/{action} with an x-api-key header, and every response - success or failure - is the same { ok, data, meta, error } envelope with a stable error code and a machine-readable `retryable` flag. The company handles proxies, headless browsers, logins and anti-bot walls server-side, so a caller gets parsed JSON from sites that block scrapers, with no per-site plan to buy and no scraper to maintain. Credits never expire, failed or blocked calls cost zero, and a 1,000-credit free tier needs no card. The agent surface is unusually complete: a live hosted MCP server at https://api.reefapi.com/mcp with five discovery-first tools whose manifest is anonymously
  introspectable, an RFC 9727 /.well-known/api-catalog linkset, a published OpenAPI 3.0.3 on the API host root, llms.txt plus a per-engine markdown twin at /docs/{engine}.md, and a robots.txt that explicitly allow-lists fifteen named AI crawlers.'
finops:
- has_sources: true
  method: derived
  name: Reefapi Finops
  primary_unit: credits
  service_category: ''
  slug: reefapi-finops
  template: false
image: https://reefapi.com/icon.svg
layout: provider
mcp_servers:
- description: 'LIVE remote MCP over streamable-HTTP. PROBED 2026-08-31: initialize returned protocolVersion 2025-06-18, serverInfo {name reefapi, version 1.27.2}; tools/list returned 5 tools ANONYMOUSLY (no key). A '
  name: ReefAPI MCP Server
  slug: mcp
modified: '2026-08-31'
name: ReefAPI
nav: Providers
network: true
overview: 'ReefAPI publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Classifieds & Second-hand API, Developer Tools API, E-commerce & Marketplaces API, and 12 more. Tagged areas include Web Data, Data Aggregation, Web Scraping, SERP, and E-Commerce.


  The ReefAPI catalog on APIs.io includes 1 Spectral governance ruleset.


  ReefAPI''s developer surface includes authentication, sandbox, pricing, signup flow, support, developer console, getting-started guide, and 19 more developer resources.'
plans:
- name: Reefapi Plans Pricing
  plan_count: 5
  slug: reefapi-plans-pricing
- name: Reefapi Price Estimates
  plan_count: 0
  slug: reefapi-price-estimates
random_paper: 12
rate_limits:
- limit_count: 2
  name: Reefapi Rate Limits
  slug: reefapi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: ReefAPI API Rules
  rule_count: 47
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 3
  slug: reefapi-rules
score:
  band: strong
  composite: 61.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 31.8
    contract_quality: 46.0
    developer_ergonomics: 63.7
    discoverability: 75.0
    operational_transparency: 39.5
  previous_composite: 61.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/reefapi/reefapi-2026-09-02T153219.png
security:
- kind: authentication
  name: Reefapi Authentication
  slug: reefapi-authentication
  summary_line: apiKey/http-bearer · 2 schemes
- kind: domain-security
  name: Reefapi Domain Security
  slug: reefapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: reefapi-engine-discovery
  slug: reefapi-engine-discovery
- name: reefapi-market-research-sweep
  slug: reefapi-market-research-sweep
- name: reefapi-product-intelligence
  slug: reefapi-product-intelligence
slug: reefapi
tags:
- Web Data
- Data Aggregation
- Web Scraping
- SERP
- E-Commerce
- Social Media
- Real Estate
- Job
- Travel
- News
- Finance
- Reviews
- Company Intelligence
- MCP
- Agent-Native
- REST
- OpenAPI
- Llms.txt
- API Catalog
- Free Tier
- Credit
- Gateways
website: https://www.reefapi.com/
---
