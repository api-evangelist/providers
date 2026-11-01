---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.7
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Web scraping API with AI and stealth features.
  name: ScrapingBot API
  slug: scrapingbot-api
- description: 'scrapingbot-io API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: scrapingbot-io API
  slug: scrapingbot-io-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/scrapingbot-io/rate-limits/scrapingbot-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/scrapingbot-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/scrapingbot-io/plans/scrapingbot-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scrapingbot-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/scrapingbot-io/rules/scrapingbot-io-rules.yml
  title: ''
  type: Spectral
  url: rules/scrapingbot-io-rules.yml
- group: design
  href: https://artifacts.apis.io/scrapingbot-io/json-ld/scrapingbot-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/scrapingbot-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/scrapingbot-io/vocabulary/scrapingbot-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/scrapingbot-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/scrapingbot-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/scrapingbot-io/data-model/scrapingbot-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scrapingbot-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/scrapingbot-io/conventions/scrapingbot-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/scrapingbot-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/scrapingbot-io/authentication/scrapingbot-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scrapingbot-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/scrapingbot-io/errors/scrapingbot-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scrapingbot-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/scrapingbot-io/conformance/scrapingbot-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scrapingbot-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/scrapingbot-io/mcp/scrapingbot-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/scrapingbot-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/scrapingbot-io/hosts/scrapingbot-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scrapingbot-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/scrapingbot-io/vendors/scrapingbot-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scrapingbot-io-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://scrapingbot.io/auth/login
- group: auth
  href: https://artifacts.apis.io/scrapingbot-io/security/scrapingbot-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scrapingbot-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scrapingbot.io/
- group: docs
  title: ''
  type: Documentation
  url: https://scrapingbot.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://scrapingbot.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://scrapingbot.io/docs
- group: company
  title: ''
  type: Blog
  url: https://scrapingbot.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://scrapingbot.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scrapingbot.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scrapingbot.io/privacy
coverage:
  checked: '2026-10-31'
  detail: MCP endpoint requires an API key and no OpenAPI spec is published.
  evidence:
  - status: 401
    url: https://scrapingbot.io/api/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: ScrapingBot provides a powerful web scraping API that combines JavaScript rendering, AI‑driven data extraction, rotating and stealth proxies, and specialized endpoints for platforms such as TikTok, Instagram, Google, Amazon, and ChatGPT. Developers can submit a URL and receive fully rendered HTML, screenshots, or structured data without being blocked, with built‑in rate‑limit handling, error reporting, and a free‑tier of 100 credits to get started.
image: https://scrapingbot.io/icon-512.png
json_schemas:
- name: GetApiV1JobJobidResponse
  property_count: 8
  slug: scrapingbot-io-get-api-v1-job-jobid-response
- name: GetJsResponse
  property_count: 7
  slug: scrapingbot-io-get-js-response
- name: GetScrapeResponse
  property_count: 7
  slug: scrapingbot-io-get-scrape-response
- name: PostApiV1GoogleRequest
  property_count: 2
  slug: scrapingbot-io-post-api-v1-google-request
- name: PostApiV1ScrapeRequest
  property_count: 2
  slug: scrapingbot-io-post-api-v1-scrape-request
- name: PostApiV1TiktokRequest
  property_count: 2
  slug: scrapingbot-io-post-api-v1-tiktok-request
jsonld:
- class_count: 17
  name: Scrapingbot Io Context
  property_count: 20
  slug: scrapingbot-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at scrapingbot.io requiring an API key.
  name: scrapingbot-io MCP Server
  slug: scrapingbot-io-mcp-yml
modified: '2026-10-31'
name: scrapingbot-io
nav: Providers
network: true
overview: 'scrapingbot-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Web Scraping, API, AI, and Data Extraction.


  The scrapingbot-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  scrapingbot-io''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Scrapingbot Io Plans Pricing
  plan_count: 6
  slug: scrapingbot-io-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 6
  name: Scrapingbot Io Rate Limits
  slug: scrapingbot-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: scrapingbot-io API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: scrapingbot-io-rules
scopes:
- name: Scrapingbot Io Scopes
  scope_count: 0
  slug: scrapingbot-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 94.3
    catalog_earned_first_party: 0.0
    catalog_gap: 20.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 55.0
    developer_ergonomics: 49.3
    discoverability: 56.7
    operational_transparency: 28.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Scrapingbot Io Authentication
  slug: scrapingbot-io-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Scrapingbot Io Domain Security
  slug: scrapingbot-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scrapingbot-io
tags:
- Company
- Web Scraping
- API
- AI
- Data Extraction
- Automation
website: https://scrapingbot.io/
---
