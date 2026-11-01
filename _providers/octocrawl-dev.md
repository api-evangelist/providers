---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Octocrawl REST API for scraping, mapping, crawling and batch jobs.
  name: Octocrawl API
  slug: octocrawl-api
- baseURL: https://api.octocrawl.dev
  baseurl_source: declared
  description: 'octocrawl-dev API as documented publicly: 31 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: octocrawl-dev API
  slug: octocrawl-dev-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/octocrawl-dev/rate-limits/octocrawl-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/octocrawl-dev-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/octocrawl-dev/rules/octocrawl-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/octocrawl-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/octocrawl-dev/json-ld/octocrawl-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/octocrawl-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/octocrawl-dev/vocabulary/octocrawl-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/octocrawl-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/octocrawl-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/octocrawl-dev/data-model/octocrawl-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/octocrawl-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/octocrawl-dev/cli/octocrawl-dev-cli.yml
  title: ''
  type: CLI
  url: cli/octocrawl-dev-cli.yml
- group: operate
  href: https://artifacts.apis.io/octocrawl-dev/changelog/octocrawl-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/octocrawl-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/octocrawl-dev/conventions/octocrawl-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/octocrawl-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/octocrawl-dev/conventions/octocrawl-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/octocrawl-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/octocrawl-dev/authentication/octocrawl-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/octocrawl-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/octocrawl-dev/errors/octocrawl-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/octocrawl-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/octocrawl-dev/conformance/octocrawl-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/octocrawl-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/octocrawl-dev/llms/octocrawl-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/octocrawl-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/octocrawl-dev/mcp/octocrawl-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/octocrawl-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/octocrawl-dev/well-known/octocrawl-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/octocrawl-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/octocrawl-dev/hosts/octocrawl-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/octocrawl-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/octocrawl-dev/vendors/octocrawl-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/octocrawl-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/octocrawl-dev/packages/octocrawl-dev-packages.yml
  title: ''
  type: Packages
  url: packages/octocrawl-dev-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://octocrawl.dev/docs/terms/
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@octocrawl/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://octocrawl.dev/docs/privacy/
- group: start
  title: ''
  type: Login
  url: https://octocrawl.dev/signin/
- group: docs
  title: ''
  type: Documentation
  url: https://octocrawl.dev/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://octocrawl.dev/changelog/
- group: company
  title: ''
  type: Blog
  url: https://octocrawl.dev/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://octocrawl.dev/docs/reference/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.octocrawl.dev`
- group: auth
  href: https://artifacts.apis.io/octocrawl-dev/security/octocrawl-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/octocrawl-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://octocrawl.dev/
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI or other machine-readable contract found despite probing known spec URLs on the API host.
  evidence:
  - status: 403
    url: https://api.octocrawl.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Octocrawl provides a web scraping API that extracts web pages as Markdown and structured data via REST, SDKs or MCP. It offers hosted scrape, map, crawl and batch jobs, or can run locally. The service delivers clean Markdown and structured data from public pages, each with a receipt, supporting JSON-LD, microdata, meta tags, tables and PDF label-value extraction.
image: https://octocrawl.dev/assets/octopus-ghost.webp
json_schemas:
- name: GetApiCapabilityResponse
  property_count: 2
  slug: octocrawl-dev-get-api-capability-response
- name: GetApiQuotaResponse
  property_count: 2
  slug: octocrawl-dev-get-api-quota-response
- name: PostCrawlRequest
  property_count: 3
  slug: octocrawl-dev-post-crawl-request
- name: PostV1LoginsImportRequest
  property_count: 2
  slug: octocrawl-dev-post-v1-logins-import-request
- name: PostV1LoginsImportResponse
  property_count: 6
  slug: octocrawl-dev-post-v1-logins-import-response
- name: PostV1ScrapeRequest
  property_count: 6
  slug: octocrawl-dev-post-v1-scrape-request
jsonld:
- class_count: 29
  name: Octocrawl Dev Context
  property_count: 40
  slug: octocrawl-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.octocrawl.dev.
  name: octocrawl-dev MCP Server
  slug: octocrawl-dev-mcp-yml
modified: '2026-10-30'
name: octocrawl-dev
nav: Providers
network: true
overview: 'octocrawl-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, WebScraping, DataExtraction, and SaaS.


  The octocrawl-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  octocrawl-dev''s developer surface includes CLI, changelog, authentication, documentation, engineering blog, API reference, and 24 more developer resources.'
plans:
- name: Octocrawl Dev Plans Pricing
  plan_count: 0
  slug: octocrawl-dev-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Octocrawl Dev Rate Limits
  slug: octocrawl-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: octocrawl-dev API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: octocrawl-dev-rules
scopes:
- name: Octocrawl Dev Scopes
  scope_count: 0
  slug: octocrawl-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 79.1
    contract_quality: 55.2
    developer_ergonomics: 61.2
    discoverability: 65.0
    operational_transparency: 44.2
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
  name: Octocrawl Dev Authentication
  slug: octocrawl-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Octocrawl Dev Domain Security
  slug: octocrawl-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: octocrawl-dev
tags:
- Company
- API
- WebScraping
- DataExtraction
- SaaS
- Automation
website: https://octocrawl.dev/
---
