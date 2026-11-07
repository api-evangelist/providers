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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://crustapi.com
  baseurl_source: spec
  description: The Demo API from CrustAPI — 1 operation(s) for demo.
  name: CrustAPI Demo API
  slug: crustapi-demo-api
- baseURL: https://crustapi.com
  baseurl_source: spec
  description: The Search API from CrustAPI — 1 operation(s) for search.
  name: CrustAPI Search API
  slug: crustapi-search-api
- baseURL: https://crustapi.com
  baseurl_source: spec
  description: The Linked In API from CrustAPI — 2 operation(s) for linked in.
  name: CrustAPI Linked In API
  slug: crustapi-linked-in-api
artifact_total: 17
asyncapis:
- description: ''
  name: Crustapi Webhooks
  slug: crustapi-webhooks
common:
- group: other
  href: https://artifacts.apis.io/crustapi/capabilities/crustapi-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/crustapi-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/crustapi/plans/crustapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crustapi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/crustapi/rate-limits/crustapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crustapi-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://crustapi.com/pricing
- group: agent
  href: https://artifacts.apis.io/crustapi/mcp/crustapi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crustapi-mcp.yml
- group: agent
  href: https://artifacts.apis.io/crustapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/crustapi/overlays/crustapi-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/crustapi-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://crustapi.com
- group: auth
  href: https://artifacts.apis.io/crustapi/security/crustapi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/crustapi-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/crustapi/security/crustapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crustapi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/crustapi/authentication/crustapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crustapi-authentication.yml
- group: build
  href: https://artifacts.apis.io/crustapi/packages/crustapi-packages.yml
  title: ''
  type: SDKs
  url: packages/crustapi-packages.yml
- group: build
  href: https://artifacts.apis.io/crustapi/packages/crustapi-packages.yml
  title: ''
  type: Packages
  url: packages/crustapi-packages.yml
- group: auth
  href: https://artifacts.apis.io/crustapi/security/crustapi-trust-center.yml
  title: ''
  type: Compliance
  url: security/crustapi-trust-center.yml
created: '2026-09-10'
description: Hosted API delivering structured Google (Search/Maps/etc.) and public LinkedIn data as JSON for developers, data teams, and AI agents. Pay-per-successful-result billing with an OpenAPI spec, an llms.txt, an x402 agent-payment endpoint, and a local MCP server.
finops:
- has_sources: true
  method: derived
  name: Crustapi Finops
  primary_unit: credit
  service_category: ''
  slug: crustapi-finops
  template: false
image: https://crustapi.com/uploads/crustapi-12-handdrawn-continents-amber-accent.svg
layout: provider
mcp_servers:
- description: First-party MCP server giving MCP clients (Claude Desktop, Cursor, Cline, etc.) live Google (Search/Maps/News/Images/Reviews/webpage) and public LinkedIn data. Distributed as an npm package run locall
  name: CrustAPI MCP Server
  slug: crustapi
modified: '2026-09-10'
name: CrustAPI
nav: Providers
network: true
overview: 'CrustAPI publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Demo API, Search API, and Linked In API. Tagged areas include Search, Google Maps, LinkedIn, SERP / Web Scraping, and Business & Lead Data.


  The CrustAPI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  CrustAPI''s developer surface includes pricing, authentication, and 12 more developer resources.'
plans:
- name: Crustapi Plans Pricing
  plan_count: 1
  slug: crustapi-plans-pricing
- name: Crustapi Price Estimates
  plan_count: 0
  slug: crustapi-price-estimates
random_paper: 11
rate_limits:
- limit_count: 3
  name: Crustapi Rate Limits
  slug: crustapi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: CrustAPI API Rules
  rule_count: 57
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 3
  slug: crustapi-rules
score:
  band: strong
  composite: 59.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 20.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 89.5
    contract_governance: 31.8
    contract_quality: 58.2
    developer_ergonomics: 44.6
    discoverability: 58.3
    operational_transparency: 50.0
  previous_composite: 58.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 40.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/crustapi/crustapi-2026-10-11T103410.png
security:
- kind: authentication
  name: Crustapi Authentication
  slug: crustapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Crustapi Domain Security
  slug: crustapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Crustapi Trust Center
  slug: crustapi-trust-center
  summary_line: trust center published
skill_count: 4
skills:
- name: Build a local-business lead list
  slug: crustapi-google-lead-list
- name: Refresh a contact database in bulk with webhook delivery
  slug: crustapi-linkedin-batch-refresh
- name: Look up a public LinkedIn profile or people search
  slug: crustapi-linkedin-profile-lookup
- name: Pull web search + page content for RAG
  slug: crustapi-web-search-rag
slug: crustapi
tags:
- Search
- Google Maps
- LinkedIn
- SERP / Web Scraping
- Business & Lead Data
- People / Recruiting Data
- Data Enrichment
- AI Agents / MCP
- RAG
- Data
website: https://crustapi.com
---
