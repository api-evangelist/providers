---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nordic Financial News Agentic Access
  operation_count: 30
  slug: nordic-financial-news-agentic-access
  summary_line: 30 operations
api_count: 2
apis:
- description: Remote Streamable HTTP MCP server exposing 19 read tools over the same data as the REST API, with OAuth 2.1 or static Bearer API keys.
  name: Nordic Financial News MCP Server
  slug: nordic-financial-news-mcp
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Articles API from Nordic Financial News — 2 operation(s) for articles.
  name: Nordic Financial News Articles API
  slug: nordic-financial-news-articles-api
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Calendar Events API from Nordic Financial News — 2 operation(s) for calendar events.
  name: Nordic Financial News Calendar Events API
  slug: nordic-financial-news-calendar-events-api
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Categories API from Nordic Financial News — 1 operation(s) for categories.
  name: Nordic Financial News Categories API
  slug: nordic-financial-news-categories-api
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Companies API from Nordic Financial News — 6 operation(s) for companies.
  name: Nordic Financial News Companies API
  slug: nordic-financial-news-companies-api
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Countries API from Nordic Financial News — 2 operation(s) for countries.
  name: Nordic Financial News Countries API
  slug: nordic-financial-news-countries-api
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Event Types API from Nordic Financial News — 1 operation(s) for event types.
  name: Nordic Financial News Event Types API
  slug: nordic-financial-news-event-types-api
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Events API from Nordic Financial News — 2 operation(s) for events.
  name: Nordic Financial News Events API
  slug: nordic-financial-news-events-api
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Exchanges API from Nordic Financial News — 3 operation(s) for exchanges.
  name: Nordic Financial News Exchanges API
  slug: nordic-financial-news-exchanges-api
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Health API from Nordic Financial News — 1 operation(s) for health.
  name: Nordic Financial News Health API
  slug: nordic-financial-news-health-api
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Indices API from Nordic Financial News — 3 operation(s) for indices.
  name: Nordic Financial News Indices API
  slug: nordic-financial-news-indices-api
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Meta API from Nordic Financial News — 1 operation(s) for meta.
  name: Nordic Financial News Meta API
  slug: nordic-financial-news-meta-api
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Search API from Nordic Financial News — 1 operation(s) for search.
  name: Nordic Financial News Search API
  slug: nordic-financial-news-search-api
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Sources API from Nordic Financial News — 1 operation(s) for sources.
  name: Nordic Financial News Sources API
  slug: nordic-financial-news-sources-api
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Stories API from Nordic Financial News — 2 operation(s) for stories.
  name: Nordic Financial News Stories API
  slug: nordic-financial-news-stories-api
- baseURL: https://nordicfinancialnews.com/api/v1
  baseurl_source: declared
  description: The Watchlists API from Nordic Financial News — 2 operation(s) for watchlists.
  name: Nordic Financial News Watchlists API
  slug: nordic-financial-news-watchlists-api
artifact_total: 31
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/agentic-access/nordic-financial-news-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nordic-financial-news-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/rate-limits/nordic-financial-news-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nordic-financial-news-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/plans/nordic-financial-news-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nordic-financial-news-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/rules/nordic-financial-news-rules.yml
  title: ''
  type: Spectral
  url: rules/nordic-financial-news-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/json-ld/nordic-financial-news-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nordic-financial-news-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/vocabulary/nordic-financial-news-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nordic-financial-news-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/data-model/nordic-financial-news-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nordic-financial-news-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/cli/nordic-financial-news-cli.yml
  title: ''
  type: CLI
  url: cli/nordic-financial-news-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/changelog/nordic-financial-news-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/nordic-financial-news-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/conventions/nordic-financial-news-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nordic-financial-news-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/scopes/nordic-financial-news-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/nordic-financial-news-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/lifecycle/nordic-financial-news-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nordic-financial-news-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/errors/nordic-financial-news-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nordic-financial-news-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/conformance/nordic-financial-news-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nordic-financial-news-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/llms/nordic-financial-news-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nordic-financial-news-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/a2a/nordic-financial-news-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/nordic-financial-news-a2a.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/mcp/nordic-financial-news-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/nordic-financial-news-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/mcp/nordic-financial-news-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/nordic-financial-news-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/well-known/nordic-financial-news-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nordic-financial-news-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/hosts/nordic-financial-news-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nordic-financial-news-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/vendors/nordic-financial-news-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nordic-financial-news-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://nordicfinancialnews.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/authentication/nordic-financial-news-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nordic-financial-news-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/security/nordic-financial-news-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nordic-financial-news-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nordicfinancialnews.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nordicfinancialnews.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nordicfinancialnews.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nordicfinancialnews.com/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://nordicfinancialnews.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://nordicfinancialnews.com/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://nordicfinancialnews.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nordicfinancialnews.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nordicfinancialnews.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nordic-financial-news
- group: company
  title: ''
  type: Blog
  url: https://nordicfinancialnews.com/blog
- group: operate
  title: ''
  type: Support
  url: https://nordicfinancialnews.com/contact
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.nordicfinancialnews.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nordicfinancialnews.com/
- group: other
  title: ''
  type: X
  url: https://x.com/nordicfinnews
created: '2026-10-09'
description: Nordic Financial News delivers structured, English-translated financial news from 70+ Nordic-language sources across Sweden, Norway, Denmark, Finland and Iceland, with synthesized stories, company and exchange reference data, and a financial calendar of earnings, dividends and AGMs, through a REST API, a remote OAuth MCP server and the nfn CLI.
image: https://nordicfinancialnews.com/assets/nfn-og-c4be56ba.jpg
json_schemas:
- name: ArticleDetail
  property_count: 0
  slug: nordic-financial-news-article-detail
- name: ArticleSummary
  property_count: 11
  slug: nordic-financial-news-article-summary
- name: CalendarEventSummary
  property_count: 18
  slug: nordic-financial-news-calendar-event-summary
- name: CompanyDetail
  property_count: 0
  slug: nordic-financial-news-company-detail
- name: EventDetail
  property_count: 0
  slug: nordic-financial-news-event-detail
- name: EventSummary
  property_count: 13
  slug: nordic-financial-news-event-summary
jsonld:
- class_count: 14
  name: Nordic Financial News Context
  property_count: 56
  slug: nordic-financial-news-context
layout: provider
mcp_servers:
- description: Remote MCP server at nordicfinancialnews.com requiring OAuth; 19 tools listed.
  name: Nordic Financial News MCP server
  slug: nordic-financial-news-mcp-server
modified: '2026-10-09'
name: Nordic Financial News
nav: Providers
network: true
overview: 'Nordic Financial News publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Articles API, Calendar Events API, Categories API, and 13 more. Tagged areas include Company, Financial News, Nordic, Market Data, and Financial Calendar.


  The Nordic Financial News catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nordic Financial News'' developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, pricing, and 32 more developer resources.'
plans:
- name: Nordic Financial News Plans Pricing
  plan_count: 3
  slug: nordic-financial-news-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Nordic Financial News Rate Limits
  slug: nordic-financial-news-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Nordic Financial News API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: nordic-financial-news-rules
scopes:
- name: Nordic Financial News Scopes
  scope_count: 2
  slug: nordic-financial-news-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 63.6
    developer_ergonomics: 54.8
    discoverability: 76.7
    operational_transparency: 68.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 63.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/nordic-financial-news/refs/heads/main/screenshots/nordic-financial-news-2026-10-11T111624.png
security:
- kind: authentication
  name: Nordic Financial News Authentication
  slug: nordic-financial-news-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nordic Financial News Domain Security
  slug: nordic-financial-news-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nordic-financial-news
tags:
- Company
- Financial News
- Nordic
- Market Data
- Financial Calendar
- MCP
- News API
website: https://nordicfinancialnews.com/
---
