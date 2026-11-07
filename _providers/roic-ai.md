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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Roic Ai Agentic Access
  operation_count: 79
  slug: roic-ai-agentic-access
  summary_line: 79 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: Pre-generated CSV datasets delivered through short-lived signed URLs.
  name: roic-ai Bulk Downloads API
  slug: roic-ai-bulk-downloads-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: Dated company event resources such as the earnings calendar.
  name: roic-ai Calendar API
  slug: roic-ai-calendar-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: The Company API from roic-ai — 6 operation(s) for company.
  name: roic-ai Company API
  slug: roic-ai-company-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: Earnings events with their transcripts, audio recordings, slide decks, and filings.
  name: roic-ai Company Events API
  slug: roic-ai-company-events-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: Company earnings-call and future editorial content resources.
  name: roic-ai Content API
  slug: roic-ai-content-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: The Countries API from roic-ai — 1 operation(s) for countries.
  name: roic-ai Countries API
  slug: roic-ai-countries-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: The Excel API from roic-ai — 2 operation(s) for excel.
  name: roic-ai Excel API
  slug: roic-ai-excel-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: The Exchanges API from roic-ai — 1 operation(s) for exchanges.
  name: roic-ai Exchanges API
  slug: roic-ai-exchanges-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: Currency pair reference data and foreign-exchange rate resources.
  name: roic-ai Forex API
  slug: roic-ai-forex-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: The Fundamental API from roic-ai — 11 operation(s) for fundamental.
  name: roic-ai Fundamental API
  slug: roic-ai-fundamental-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: Financial statements, ratios, and valuation resources.
  name: roic-ai Fundamentals API
  slug: roic-ai-fundamentals-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: The Industries API from roic-ai — 1 operation(s) for industries.
  name: roic-ai Industries API
  slug: roic-ai-industries-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: Historical and current market data resources.
  name: roic-ai Market Data API
  slug: roic-ai-market-data-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: Ticker identity and discovery resources.
  name: roic-ai Reference Data API
  slug: roic-ai-reference-data-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: The Sectors API from roic-ai — 1 operation(s) for sectors.
  name: roic-ai Sectors API
  slug: roic-ai-sectors-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: The Stock Prices API from roic-ai — 2 operation(s) for stock prices.
  name: roic-ai Stock Prices API
  slug: roic-ai-stock-prices-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: The Stock Splits API from roic-ai — 2 operation(s) for stock splits.
  name: roic-ai Stock Splits API
  slug: roic-ai-stock-splits-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: The Tickers API from roic-ai — 7 operation(s) for tickers.
  name: roic-ai Tickers API
  slug: roic-ai-tickers-api
- baseURL: https://api.roic.ai
  baseurl_source: declared
  description: The Usage API from roic-ai — 1 operation(s) for usage.
  name: roic-ai Usage API
  slug: roic-ai-usage-api
artifact_total: 34
common:
- group: agent
  href: https://artifacts.apis.io/roic-ai/agentic-access/roic-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/roic-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/roic-ai/rate-limits/roic-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/roic-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/roic-ai/plans/roic-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/roic-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/roic-ai/rules/roic-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/roic-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/roic-ai/json-ld/roic-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/roic-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/roic-ai/vocabulary/roic-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/roic-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/roic-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/roic-ai/data-model/roic-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/roic-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/roic-ai/authentication/roic-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/roic-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/roic-ai/errors/roic-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/roic-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/roic-ai/conformance/roic-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/roic-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/roic-ai/llms/roic-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/roic-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/roic-ai/mcp/roic-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/roic-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/roic-ai/mcp/roic-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/roic-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/roic-ai/well-known/roic-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/roic-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/roic-ai/hosts/roic-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/roic-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/roic-ai/vendors/roic-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/roic-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/roic-ai/packages/roic-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/roic-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/roic-ai/packages/roic-ai-packages.yml
  title: ''
  type: Packages
  url: packages/roic-ai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.roic.ai/tos
- group: operate
  title: ''
  type: StatusPage
  url: https://status.roic.ai
- group: start
  title: ''
  type: SignUp
  url: https://www.roic.ai/signup
- group: company
  title: ''
  type: Newsroom
  url: https://www.roic.ai/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.roic.ai/changelog
- group: auth
  href: https://artifacts.apis.io/roic-ai/security/roic-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/roic-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://roic.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.roic.ai/api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.roic.ai/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.roic.ai/api/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.roic.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.roic.ai/blog
created: '2026-10-31'
description: ROIC.ai provides a free financial data API delivering up to 40+ years of company financial statements, earnings call transcripts, and historical stock-price data. Users can access comprehensive financial metrics across multiple plans, including a free tier with no credit‑card required.
image: https://www.roic.ai/opengraph-image-xglmiy?f4f2a206cab2754f
json_schemas:
- name: v3.BalanceSheetFinancialPeriodList
  property_count: 3
  slug: roic-ai-v3-balance-sheet-financial-period-list
- name: v3.CashFlowFinancialPeriodList
  property_count: 3
  slug: roic-ai-v3-cash-flow-financial-period-list
- name: v3.CompanyEventList
  property_count: 3
  slug: roic-ai-v3-company-event-list
- name: v3.CompanyProfile
  property_count: 28
  slug: roic-ai-v3-company-profile
- name: v3.IncomeStatementFinancialPeriodList
  property_count: 3
  slug: roic-ai-v3-income-statement-financial-period-list
- name: v3.ValuationMultiplesFinancialPeriodList
  property_count: 3
  slug: roic-ai-v3-valuation-multiples-financial-period-list
jsonld:
- class_count: 120
  name: Roic Ai Context
  property_count: 436
  slug: roic-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.roic.ai requiring OAuth.
  name: roic-ai MCP Server
  slug: roic-ai-mcp-yml
modified: '2026-10-31'
name: roic-ai
nav: Providers
network: true
overview: 'roic-ai publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bulk Downloads API, Calendar API, Company API, and 16 more. Tagged areas include Company, Finance, Data, and Stocks.


  The roic-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  roic-ai''s developer surface includes authentication, signup flow, changelog, documentation, API reference, getting-started guide, pricing, and 24 more developer resources.'
plans:
- name: Roic Ai Plans Pricing
  plan_count: 4
  slug: roic-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Roic Ai Rate Limits
  slug: roic-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: roic-ai API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: roic-ai-rules
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 53.6
    developer_ergonomics: 41.0
    discoverability: 57.5
    operational_transparency: 47.4
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/roic-ai/roic-ai-2026-11-03T142401.png
security:
- kind: authentication
  name: Roic Ai Authentication
  slug: roic-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Roic Ai Domain Security
  slug: roic-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: get-income-statement
  slug: roic-ai-get-income-statement
slug: roic-ai
tags:
- Company
- Finance
- Data
- Stocks
website: https://roic.ai/
---
