---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 69.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Hydrafetch Com Agentic Access
  operation_count: 25
  slug: hydrafetch-com-agentic-access
  summary_line: 25 operations · 12 acting
api_count: 1
apis:
- baseURL: https://api.hydrafetch.com
  baseurl_source: declared
  description: 'Resolve a domain into the company ready to render: logos for light and dark, the palette ranked by how the site uses it, fonts, socials, and the design system behind them.'
  name: hydrafetch-com Brand API
  slug: hydrafetch-com-brand-api
- baseURL: https://api.hydrafetch.com
  baseurl_source: declared
  description: Whole sites rather than single pages. Map every URL, crawl with depth and path rules, batch a list you already have, and read the webhook deliveries for either.
  name: hydrafetch-com Crawl & batch API
  slug: hydrafetch-com-crawl-batch-api
- baseURL: https://api.hydrafetch.com
  baseurl_source: declared
  description: Pull schema-shaped JSON out of one or many pages, with optional per-field confidence and the source passage behind each value.
  name: hydrafetch-com Extract API
  slug: hydrafetch-com-extract-api
- baseURL: https://api.hydrafetch.com
  baseurl_source: declared
  description: The Feedback API from hydrafetch-com — 1 operation(s) for feedback.
  name: hydrafetch-com Feedback API
  slug: hydrafetch-com-feedback-api
- baseURL: https://api.hydrafetch.com
  baseurl_source: declared
  description: The Logo API from hydrafetch-com — 1 operation(s) for logo.
  name: hydrafetch-com Logo API
  slug: hydrafetch-com-logo-api
- baseURL: https://api.hydrafetch.com
  baseurl_source: declared
  description: Images and screenshots from a page, with source and alt text, or a rendered capture of the page as it appears.
  name: hydrafetch-com Media API
  slug: hydrafetch-com-media-api
- baseURL: https://api.hydrafetch.com
  baseurl_source: declared
  description: Turn one URL into clean, LLM-ready content. Ask for Markdown, HTML, links, or the page’s own structured data, and poll a job id when a fetch runs long.
  name: hydrafetch-com Scrape API
  slug: hydrafetch-com-scrape-api
- baseURL: https://api.hydrafetch.com
  baseurl_source: declared
  description: Search the web and get the ranked results back already scraped, so an agent has content to cite rather than links to fetch.
  name: hydrafetch-com Search API
  slug: hydrafetch-com-search-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/hydrafetch-com/agentic-access/hydrafetch-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hydrafetch-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/hydrafetch-com/plans/hydrafetch-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hydrafetch-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/hydrafetch-com/rules/hydrafetch-com-rules.yml
  title: ''
  type: Spectral
  url: rules/hydrafetch-com-rules.yml
- group: design
  href: https://artifacts.apis.io/hydrafetch-com/json-ld/hydrafetch-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hydrafetch-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/hydrafetch-com/vocabulary/hydrafetch-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hydrafetch-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/hydrafetch-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hydrafetch-com/data-model/hydrafetch-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hydrafetch-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/hydrafetch-com/changelog/hydrafetch-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hydrafetch-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/hydrafetch-com/authentication/hydrafetch-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hydrafetch-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/hydrafetch-com/errors/hydrafetch-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hydrafetch-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hydrafetch-com/conformance/hydrafetch-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hydrafetch-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hydrafetch-com/llms/hydrafetch-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hydrafetch-com-llms.txt
- group: other
  href: https://artifacts.apis.io/hydrafetch-com/a2a/hydrafetch-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hydrafetch-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/hydrafetch-com/mcp/hydrafetch-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hydrafetch-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/hydrafetch-com/well-known/hydrafetch-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hydrafetch-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/hydrafetch-com/hosts/hydrafetch-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hydrafetch-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/hydrafetch-com/vendors/hydrafetch-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hydrafetch-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hydrafetch.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hydrafetch.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://hydrafetch.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://hydrafetch.com/blog/
- group: auth
  href: https://artifacts.apis.io/hydrafetch-com/security/hydrafetch-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hydrafetch-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hydrafetch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hydrafetch.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hydrafetch.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hydrafetch.com/quickstart
- group: operate
  title: ''
  type: Changelog
  url: https://docs.hydrafetch.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hydrafetch
- group: start
  title: ''
  type: SignUp
  url: https://app.hydrafetch.com/
created: '2026-10-30'
description: Hydrafetch provides a web‑scraping API that converts any URL into clean Markdown and structured data for AI models. It offers endpoints for crawling, searching, extracting page content, and handling pagination, all with a simple credit‑per‑page pricing model. The service aims to simplify data acquisition for developers building LLM‑powered applications.
image: https://mintcdn.com/hydrafetch/koPVMLXM3S4OTC3p/logo/lockup-light.svg
json_schemas:
- name: CrawlRequestDto
  property_count: 11
  slug: hydrafetch-com-crawl-request-dto
- name: ExtractRequestDto
  property_count: 11
  slug: hydrafetch-com-extract-request-dto
- name: MapRequestDto
  property_count: 12
  slug: hydrafetch-com-map-request-dto
- name: ScrapeFormatRequestDto
  property_count: 18
  slug: hydrafetch-com-scrape-format-request-dto
- name: ScrapeRequestDto
  property_count: 20
  slug: hydrafetch-com-scrape-request-dto
- name: ScreenshotRequestDto
  property_count: 8
  slug: hydrafetch-com-screenshot-request-dto
jsonld:
- class_count: 92
  name: Hydrafetch Com Context
  property_count: 237
  slug: hydrafetch-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.hydrafetch.com requiring OAuth.
  name: hydrafetch-com MCP Server
  slug: hydrafetch-com-mcp-yml
modified: '2026-10-30'
name: hydrafetch-com
nav: Providers
network: true
overview: 'hydrafetch-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Brand API, Crawl & batch API, Extract API, and 5 more. Tagged areas include Web Scraping, Data Extraction, API, Automation, and Markdown.


  The hydrafetch-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  hydrafetch-com''s developer surface includes changelog, authentication, pricing, engineering blog, documentation, API reference, getting-started guide, and 22 more developer resources.'
plans:
- name: Hydrafetch Com Plans Pricing
  plan_count: 5
  slug: hydrafetch-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Hydrafetch Com Rate Limits
  slug: hydrafetch-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: hydrafetch-com API Rules
  rule_count: 19
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 0
  slug: hydrafetch-com-rules
scopes:
- name: Hydrafetch Com Scopes
  scope_count: 0
  slug: hydrafetch-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 85.8
    catalog_earned_first_party: 0.0
    catalog_gap: 29.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 70.9
    contract_quality: 64.8
    developer_ergonomics: 49.3
    discoverability: 65.0
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hydrafetch Com Authentication
  slug: hydrafetch-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hydrafetch Com Domain Security
  slug: hydrafetch-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: resolve-brand
  slug: hydrafetch-com-resolve-brand
slug: hydrafetch-com
tags:
- Web Scraping
- Data Extraction
- API
- Automation
- Markdown
website: https://hydrafetch.com/
---
