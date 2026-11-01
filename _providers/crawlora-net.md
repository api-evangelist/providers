---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Crawlora provides structured web data via a REST API; endpoints require an API key and are documented in the public docs.
  name: Crawlora API
  slug: api
- baseURL: https://api.crawlora.net
  baseurl_source: declared
  description: 'crawlora-net API as documented publicly: 178 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: crawlora-net API
  slug: crawlora-net-api
artifact_total: 17
common:
- group: operate
  href: https://artifacts.apis.io/crawlora-net/rate-limits/crawlora-net-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crawlora-net-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/crawlora-net/plans/crawlora-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crawlora-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/crawlora-net/rules/crawlora-net-rules.yml
  title: ''
  type: Spectral
  url: rules/crawlora-net-rules.yml
- group: design
  href: https://artifacts.apis.io/crawlora-net/json-ld/crawlora-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crawlora-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/crawlora-net/vocabulary/crawlora-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crawlora-net-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/crawlora-net/data-model/crawlora-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crawlora-net-data-model.yml
- group: auth
  href: https://artifacts.apis.io/crawlora-net/security/crawlora-net-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/crawlora-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/crawlora-net/authentication/crawlora-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crawlora-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/crawlora-net/conformance/crawlora-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crawlora-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crawlora-net/llms/crawlora-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crawlora-net-llms.txt
- group: other
  href: https://artifacts.apis.io/crawlora-net/a2a/crawlora-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/crawlora-net-a2a.yml
- group: agent
  href: https://artifacts.apis.io/crawlora-net/mcp/crawlora-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crawlora-net-mcp.yml
- group: auth
  href: https://artifacts.apis.io/crawlora-net/well-known/crawlora-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crawlora-net-security.txt
- group: agent
  href: https://artifacts.apis.io/crawlora-net/well-known/crawlora-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crawlora-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/crawlora-net/hosts/crawlora-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crawlora-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/crawlora-net/vendors/crawlora-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crawlora-net-vendors.yml
- group: build
  href: https://artifacts.apis.io/crawlora-net/packages/crawlora-net-packages.yml
  title: ''
  type: Packages
  url: packages/crawlora-net-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://crawlora.net/playground
- group: build
  title: ''
  type: SDKs
  url: https://crawlora.net/sdk
- group: operate
  title: ''
  type: ChangeLog
  url: https://crawlora.net/changelog
- group: auth
  href: https://artifacts.apis.io/crawlora-net/security/crawlora-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crawlora-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/crawlora-net/security/crawlora-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crawlora-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crawlora.net/
- group: docs
  title: ''
  type: Documentation
  url: https://crawlora.net/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://crawlora.net/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://crawlora.net/contact
- group: company
  title: ''
  type: Blog
  url: https://crawlora.net/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Crawlora-org
- group: commercial
  title: ''
  type: Pricing
  url: https://crawlora.net/pricing
- group: start
  title: ''
  type: Login
  url: https://crawlora.net/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crawlora.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crawlora.net/privacy
coverage:
  checked: '2026-10-30'
  detail: API endpoints require an API key; no public OpenAPI spec is provided.
  evidence:
  - status: 401
    url: https://api.crawlora.net/api/v1/amazon/product/B0CHXH39GN?currency=USD&language=en_US
  reason: auth-required
  state: gated
created: '2026-10-30'
description: Crawlora provides web scraping APIs and MCP tools for AI agents, offering over 4,112 endpoints covering search, maps, commerce, finance, and more. Users pay only on successful data retrieval, even for sites that block bots. The platform includes a wide range of datasets, free tools, comprehensive documentation, SDKs, and flexible pricing plans, supporting use cases such as SERP monitoring, property market intelligence, crypto market research, and AI-driven web data workflows.
image: https://crawlora.net/favicon.ico
json_schemas:
- name: GetAljazeeraArticleResponse
  property_count: 9
  slug: crawlora-net-get-aljazeera-article-response
- name: GetAppleBooksSearchResponse
  property_count: 19
  slug: crawlora-net-get-apple-books-search-response
- name: GetBenzingaArticleResponse
  property_count: 9
  slug: crawlora-net-get-benzinga-article-response
- name: GetBrisbanetimesArticleResponse
  property_count: 10
  slug: crawlora-net-get-brisbanetimes-article-response
- name: GetBrisbanetimesAuthorResponse
  property_count: 11
  slug: crawlora-net-get-brisbanetimes-author-response
- name: GetCnbcArticleResponse
  property_count: 9
  slug: crawlora-net-get-cnbc-article-response
jsonld:
- class_count: 120
  name: Crawlora Net Context
  property_count: 116
  slug: crawlora-net-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.crawlora.net requiring an API key.
  name: crawlora-net MCP Server
  slug: crawlora-net-mcp-yml
modified: '2026-10-30'
name: crawlora-net
nav: Providers
network: true
overview: 'crawlora-net is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Web Scraping, AI, Data, and MCP.


  The crawlora-net catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  crawlora-net''s developer surface includes authentication, sandbox, changelog, documentation, getting-started guide, support, engineering blog, and 25 more developer resources.'
plans:
- name: Crawlora Net Plans Pricing
  plan_count: 5
  slug: crawlora-net-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Crawlora Net Rate Limits
  slug: crawlora-net-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: crawlora-net API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: crawlora-net-rules
scopes:
- name: Crawlora Net Scopes
  scope_count: 0
  slug: crawlora-net-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 64.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 99.3
    catalog_earned_first_party: 0.0
    catalog_gap: 15.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 45.6
    developer_ergonomics: 54.8
    discoverability: 65.0
    operational_transparency: 60.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Crawlora Net Authentication
  slug: crawlora-net-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Crawlora Net Domain Security
  slug: crawlora-net-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Crawlora Net Vulnerability Disclosure
  slug: crawlora-net-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crawlora-net
tags:
- Company
- Web Scraping
- AI
- Data
- MCP
website: https://crawlora.net/
---
