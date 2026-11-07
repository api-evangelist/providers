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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Bigdata Agentic Access
  operation_count: 31
  slug: bigdata-agentic-access
  summary_line: 31 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.bigdata.com/
  baseurl_source: declared
  description: Analyst estimates and ratings including analyst ratings, estimates, target prices, and earnings surprises
  name: RavenPack Analyst Estimates API
  slug: bigdata-analyst-estimates-api
- baseURL: https://api.bigdata.com/
  baseurl_source: declared
  description: Company information and events including company profile and events calendar
  name: RavenPack Company & Events API
  slug: bigdata-company-events-api
- baseURL: https://api.bigdata.com/
  baseurl_source: declared
  description: Financial statements and ratios including balance sheet, income statement, cash flow statement, key metrics TTM, and company ratios TTM
  name: RavenPack Financials & Ratios API
  slug: bigdata-financials-ratios-api
- baseURL: https://api.bigdata.com/
  baseurl_source: declared
  description: 'Bond reference data: the bonds a company has issued and their terms'
  name: RavenPack Fixed Income API
  slug: bigdata-fixed-income-api
- baseURL: https://api.bigdata.com/
  baseurl_source: declared
  description: Institutional fund holdings from SEC 13F filings including fund holdings and stock fund holdings
  name: RavenPack Fund Holdings API
  slug: bigdata-fund-holdings-api
- baseURL: https://api.bigdata.com/
  baseurl_source: declared
  description: Market data endpoints including intraday prices, daily prices, price changes, and real-time quotes
  name: RavenPack Market Data API
  slug: bigdata-market-data-api
- baseURL: https://api.bigdata.com/
  baseurl_source: declared
  description: Private company data including profile, headquarters, funding totals and valuation
  name: RavenPack Private Markets API
  slug: bigdata-private-markets-api
artifact_total: 23
common:
- group: auth
  href: https://artifacts.apis.io/bigdata/well-known/bigdata-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bigdata-status-security.txt
- group: start
  title: ''
  type: Login
  url: https://app.bigdata.com/login
- group: agent
  href: https://artifacts.apis.io/bigdata/agentic-access/bigdata-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bigdata-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/bigdata/rate-limits/bigdata-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bigdata-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bigdata/plans/bigdata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bigdata-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bigdata/rules/bigdata-rules.yml
  title: ''
  type: Spectral
  url: rules/bigdata-rules.yml
- group: design
  href: https://artifacts.apis.io/bigdata/json-ld/bigdata-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bigdata-context.jsonld
- group: design
  href: https://artifacts.apis.io/bigdata/vocabulary/bigdata-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bigdata-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bigdata/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bigdata/data-model/bigdata-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bigdata-data-model.yml
- group: operate
  href: https://artifacts.apis.io/bigdata/changelog/bigdata-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bigdata-changelog.yml
- group: design
  href: https://artifacts.apis.io/bigdata/errors/bigdata-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bigdata-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bigdata/conformance/bigdata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bigdata-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bigdata/llms/bigdata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bigdata-llms.txt
- group: other
  href: https://artifacts.apis.io/bigdata/a2a/bigdata-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bigdata-a2a.yml
- group: agent
  href: https://artifacts.apis.io/bigdata/well-known/bigdata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bigdata-well-known.yml
- group: other
  href: https://artifacts.apis.io/bigdata/hosts/bigdata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bigdata-hosts.yml
- group: other
  href: https://artifacts.apis.io/bigdata/vendors/bigdata-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bigdata-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bigdata.com/terms-and-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bigdata.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bigdata.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.bigdata.com/release-notes/api_changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bigdata.com\
- group: auth
  href: https://artifacts.apis.io/bigdata/authentication/bigdata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bigdata-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bigdata/security/bigdata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bigdata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bigdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bigdata.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://bigdata.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://bigdata.com/how-it-works
- group: commercial
  title: ''
  type: Pricing
  url: https://bigdata.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://bigdata.com/blog
created: '2026-10-19'
description: RavenPack provides AI-driven analytics and data solutions for finance, delivering real-time insights, sentiment analysis, and predictive modeling to help firms make data‑driven decisions across markets, risk, and strategy. The platform aggregates news, social media, and alternative data, transforming it into structured, searchable signals for investors, traders, and analysts.
image: https://framerusercontent.com/images/VrOQfwdVdsAIUHQ1aYd2eKd1ICM.webp
json_schemas:
- name: EconomicCalendarQuery
  property_count: 5
  slug: bigdata-economic-calendar-query
- name: EconomicCalendarResponse
  property_count: 5
  slug: bigdata-economic-calendar-response
- name: EventsCalendarQuery
  property_count: 8
  slug: bigdata-events-calendar-query
- name: EventsCalendarResponse
  property_count: 7
  slug: bigdata-events-calendar-response
- name: PublicCompanyProfileResponse
  property_count: 4
  slug: bigdata-public-company-profile-response
- name: PublicGetHoldingsOverviewResponse
  property_count: 5
  slug: bigdata-public-get-holdings-overview-response
jsonld:
- class_count: 120
  name: Bigdata Context
  property_count: 298
  slug: bigdata-context
layout: provider
modified: '2026-10-19'
name: RavenPack
nav: Providers
network: true
overview: 'RavenPack publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analyst Estimates API, Company & Events API, Financials & Ratios API, and 4 more. Tagged areas include Company, Finance, Artificial Intelligence, Data Analytics, and Market Insights.


  The RavenPack catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RavenPack''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 24 more developer resources.'
plans:
- name: Bigdata Plans Pricing
  plan_count: 2
  slug: bigdata-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Bigdata Rate Limits
  slug: bigdata-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: RavenPack API Rules
  rule_count: 49
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 7
  slug: bigdata-rules
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 50.0
    contract_governance: 22.0
    contract_quality: 62.8
    developer_ergonomics: 33.9
    discoverability: 73.2
    operational_transparency: 47.4
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bigdata/bigdata-2026-11-03T121713.png
security:
- kind: authentication
  name: Bigdata Authentication
  slug: bigdata-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bigdata Domain Security
  slug: bigdata-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: bigdata-company-profile-and-events
  slug: bigdata-company-profile-and-events
- name: bigdata-fetch-financial-statements
  slug: bigdata-fetch-financial-statements
- name: bigdata-fetch-market-data
  slug: bigdata-fetch-market-data
slug: bigdata
tags:
- Company
- Finance
- Artificial Intelligence
- Data Analytics
- Market Insights
website: https://bigdata.com/
---
