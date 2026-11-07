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
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Fastcrw Com Agentic Access
  operation_count: 13
  slug: fastcrw-com-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.fastcrw.com
  baseurl_source: declared
  description: The batch API from fastcrw-com — 2 operation(s) for batch.
  name: fastcrw-com Batch API
  slug: fastcrw-com-batch-api
- baseURL: https://api.fastcrw.com
  baseurl_source: declared
  description: The capabilities API from fastcrw-com — 1 operation(s) for capabilities.
  name: fastcrw-com Capabilities API
  slug: fastcrw-com-capabilities-api
- baseURL: https://api.fastcrw.com
  baseurl_source: declared
  description: Stateless diff of a scrape against a caller-supplied previous snapshot (monitor primitive)
  name: fastcrw-com Change Tracking API
  slug: fastcrw-com-change-tracking-api
- baseURL: https://api.fastcrw.com
  baseurl_source: declared
  description: Async multi-page crawl jobs
  name: fastcrw-com Crawl API
  slug: fastcrw-com-crawl-api
- baseURL: https://api.fastcrw.com
  baseurl_source: declared
  description: Structured JSON extraction via scrape + jsonOptions
  name: fastcrw-com Extract API
  slug: fastcrw-com-extract-api
- baseURL: https://api.fastcrw.com
  baseurl_source: declared
  description: URL discovery without full scraping
  name: fastcrw-com Map API
  slug: fastcrw-com-map-api
- baseURL: https://api.fastcrw.com
  baseurl_source: declared
  description: Single-URL content extraction
  name: fastcrw-com Scrape API
  slug: fastcrw-com-scrape-api
- baseURL: https://api.fastcrw.com
  baseurl_source: declared
  description: Web search via our own search backend (self-hosted) or managed (hosted)
  name: fastcrw-com Search API
  slug: fastcrw-com-search-api
artifact_total: 35
common:
- group: agent
  href: https://artifacts.apis.io/fastcrw-com/agentic-access/fastcrw-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fastcrw-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/fastcrw-com/rate-limits/fastcrw-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fastcrw-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fastcrw-com/plans/fastcrw-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fastcrw-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fastcrw-com/rules/fastcrw-com-rules.yml
  title: ''
  type: Spectral
  url: rules/fastcrw-com-rules.yml
- group: design
  href: https://artifacts.apis.io/fastcrw-com/json-ld/fastcrw-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fastcrw-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/fastcrw-com/vocabulary/fastcrw-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fastcrw-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/fastcrw-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/fastcrw-com/data-model/fastcrw-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fastcrw-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/fastcrw-com/authentication/fastcrw-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fastcrw-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/fastcrw-com/lifecycle/fastcrw-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fastcrw-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/fastcrw-com/errors/fastcrw-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fastcrw-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fastcrw-com/conformance/fastcrw-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fastcrw-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fastcrw-com/llms/fastcrw-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fastcrw-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/fastcrw-com/well-known/fastcrw-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fastcrw-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/fastcrw-com/hosts/fastcrw-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fastcrw-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/fastcrw-com/vendors/fastcrw-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fastcrw-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/fastcrw-com/packages/fastcrw-com-packages.yml
  title: ''
  type: SDKs
  url: packages/fastcrw-com-packages.yml
- group: build
  href: https://artifacts.apis.io/fastcrw-com/packages/fastcrw-com-packages.yml
  title: ''
  type: Packages
  url: packages/fastcrw-com-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://fastcrw.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://fastcrw.com/status
- group: start
  title: ''
  type: Sandbox
  url: https://fastcrw.com/playground
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/fastcrw/crw/releases
- group: start
  title: ''
  type: SignUp
  url: https://fastcrw.com/register?ref=docs-quick-start-inline
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.fastcrw.com</code
- group: auth
  href: https://artifacts.apis.io/fastcrw-com/security/fastcrw-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fastcrw-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fastcrw.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fastcrw.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fastcrw.com/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://fastcrw.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fastcrw
- group: commercial
  title: ''
  type: Pricing
  url: https://fastcrw.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fastcrw.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fastcrw.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.fastcrw.com/openapi.json
  - status: null
    url: https://docs.fastcrw.com/openapi.json
  - status: 401
    url: https://fastcrw.com/mcp
  - status: 200
    url: https://fastcrw.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: fastCRW is an open-source Rust-based web scraping and search API designed for AI agents. It offers a self‑hostable single‑binary deployment, a free tier, and multiple paid plans. The service includes an MCP server for AI‑agent integration, benchmark‑backed performance, and full compatibility with Firecrawl workflows. Features include web crawling with robots.txt and sitemap support, structured LLM extraction, and fast, lightweight operation.
image: https://fastcrw.com/opengraph-image
json_schemas:
- name: BatchScrapeRequest
  property_count: 5
  slug: fastcrw-com-batch-scrape-request
- name: CrawlRequest
  property_count: 14
  slug: fastcrw-com-crawl-request
- name: ExtractRequest
  property_count: 7
  slug: fastcrw-com-extract-request
- name: ScrapeRequest
  property_count: 39
  slug: fastcrw-com-scrape-request
- name: ScrapeResponse
  property_count: 3
  slug: fastcrw-com-scrape-response
- name: SearchResponse
  property_count: 6
  slug: fastcrw-com-search-response
jsonld:
- class_count: 39
  name: Fastcrw Com Context
  property_count: 116
  slug: fastcrw-com-context
layout: provider
modified: '2026-10-30'
name: fastcrw-com
nav: Providers
network: true
overview: 'fastcrw-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batch API, Capabilities API, Change Tracking API, and 5 more. Tagged areas include Company, Web Scraping, AI Agents, Rust, and Open Source.


  The fastcrw-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  fastcrw-com''s developer surface includes authentication, support, sandbox, changelog, signup flow, documentation, API reference, and 26 more developer resources.'
plans:
- name: Fastcrw Com Plans Pricing
  plan_count: 5
  slug: fastcrw-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Fastcrw Com Rate Limits
  slug: fastcrw-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: fastcrw-com API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: fastcrw-com-rules
scopes:
- name: Fastcrw Com Scopes
  scope_count: 0
  slug: fastcrw-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 61.8
    developer_ergonomics: 45.7
    discoverability: 66.1
    operational_transparency: 50.0
  previous_composite: 64.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fastcrw-com/fastcrw-com-2026-11-03T131904.png
security:
- kind: authentication
  name: Fastcrw Com Authentication
  slug: fastcrw-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fastcrw Com Domain Security
  slug: fastcrw-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 13
skills:
- name: batch-scrape-cancel
  slug: fastcrw-com-batchScrapeCancel
- name: batch-scrape-start
  slug: fastcrw-com-batchScrapeStart
- name: batch-scrape-status
  slug: fastcrw-com-batchScrapeStatus
- name: capabilities
  slug: fastcrw-com-capabilities
- name: change-tracking-diff
  slug: fastcrw-com-changeTrackingDiff
- name: crawl-start
  slug: fastcrw-com-crawlStart
- name: crawl-status
  slug: fastcrw-com-crawlStatus
- name: extract-cancel
  slug: fastcrw-com-extractCancel
- name: extract-start
  slug: fastcrw-com-extractStart
- name: extract-status
  slug: fastcrw-com-extractStatus
- name: map
  slug: fastcrw-com-map
- name: scrape
  slug: fastcrw-com-scrape
- name: search
  slug: fastcrw-com-search
slug: fastcrw-com
tags:
- Company
- Web Scraping
- AI Agents
- Rust
- Open Source
- SERP
website: https://fastcrw.com/
---
