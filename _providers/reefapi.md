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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://api.reefapi.com
  baseurl_source: declared
  description: POST-based REST/JSON API fronting a catalog of web-data engines. Auth via x-api-key header; uniform {ok,data,meta,error} response envelope with stable error codes. Declared OpenAPI contract and RFC 97
  name: ReefAPI REST API
  slug: reefapi-rest-api
- description: 'Hosted MCP server over streamable-HTTP with 5 discovery-first tools (search_engines, get_catalog, get_engine_schema, get_action_schema, call_engine). Auth via Authorization: Bearer ak_live_ key. Compa'
  name: ReefAPI MCP Server
  slug: reefapi-mcp-server
artifact_total: 8
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/reefapi/reefapi-mcp/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reefapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reefapi-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/reefapi-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/reefapi-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reefapi-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/reefapi-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reefapi-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reefapi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://reefapi.com/status
- group: start
  title: ''
  type: Sandbox
  url: sandbox/reefapi-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/reefapi-plans-pricing.yml
- group: operate
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
image: https://reefapi.com/icon.svg
layout: provider
mcp_servers:
- description: 'LIVE remote MCP over streamable-HTTP. PROBED 2026-08-31: initialize returned protocolVersion 2025-06-18, serverInfo {name reefapi, version 1.27.2}; tools/list returned 5 tools ANONYMOUSLY (no key). A '
  name: ReefAPI MCP Server
  slug: reefapi-mcp-server
- description: Local manifest with the deployment block, probe notes and the verbatim tool set.
  name: ReefAPI MCP Server
  slug: reefapi-mcp-server-2
modified: '2026-08-31'
name: ReefAPI
nav: Providers
network: true
overview: 'ReefAPI publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Web Data, Data Aggregation, Web Scraping, SERP, and E-Commerce.


  ReefAPI''s developer surface includes authentication, sandbox, pricing, signup flow, support, developer console, getting-started guide, and 16 more developer resources.'
plans:
- name: Reefapi Plans Pricing
  plan_count: 6
  slug: reefapi-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Reefapi Rate Limits
  slug: reefapi-rate-limits
score:
  band: strong
  composite: 54.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 47.6
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 54.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reefapi/refs/heads/main/screenshots/reefapi-2026-09-02T153219.png
security:
- kind: authentication
  name: Reefapi Authentication
  slug: reefapi-authentication
  summary_line: apiKey/http-bearer · 2 schemes
- kind: domain-security
  name: Reefapi Domain Security
  slug: reefapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reefapi
tags:
- Web Data
- Data Aggregation
- Web Scraping
- SERP
- E-Commerce
- Social-Media
- Real-Estate
- Job
- Travel
- News
- Finance
- Reviews
- Company Intelligence
- MCP
- agent-native
- REST
- OpenAPI
- llms-txt
- API Catalog
- Free Tier
- Credits
- Gateway
---
