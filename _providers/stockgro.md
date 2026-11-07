---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.stockgro.club
  baseurl_source: declared
  description: The Health API from StockGro — 1 operation(s) for health.
  name: StockGro Health API
  slug: stockgro-health-api
- baseURL: https://api.stockgro.club
  baseurl_source: declared
  description: The Process API from StockGro — 1 operation(s) for process.
  name: StockGro Process API
  slug: stockgro-process-api
- baseURL: https://api.stockgro.club
  baseurl_source: declared
  description: The TradeView Intraday Model API API from StockGro — 1 operation(s) for tradeview intraday model api.
  name: StockGro TradeView Intraday Model API
  slug: stockgro-tradeview-intraday-model-api-api
artifact_total: 10
common:
- group: other
  href: https://artifacts.apis.io/stockgro/overlays/stockgro-tradeview-intraday-model-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stockgro-tradeview-intraday-model-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.stockgro.club/
- group: company
  title: ''
  type: Blog
  url: https://www.stockgro.club/blogs/
- group: operate
  title: ''
  type: Support
  url: https://www.stockgro.club/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stockgro.club/tandc/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stockgro.club/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://app.stockgro.club/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stockgro.club/subscription/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stockgro-india
- group: agent
  href: https://artifacts.apis.io/stockgro/llms/stockgro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stockgro-llms.txt
- group: design
  href: https://artifacts.apis.io/stockgro/conformance/stockgro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stockgro-conformance.yml
- group: auth
  href: https://artifacts.apis.io/stockgro/conformance/stockgro-conformance.yml
  title: ''
  type: Compliance
  url: conformance/stockgro-conformance.yml
- group: design
  href: https://artifacts.apis.io/stockgro/lifecycle/stockgro-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/stockgro-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/stockgro/conventions/stockgro-conventions.yml
  title: ''
  type: Conventions
  url: conventions/stockgro-conventions.yml
- group: auth
  href: https://artifacts.apis.io/stockgro/security/stockgro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stockgro-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/stockgro/plans/stockgro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stockgro-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/stockgro/rate-limits/stockgro-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stockgro-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/stockgro/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-29'
description: 'StockGro is an Indian stock market advisory, research and financial-education platform operated by Assetgro Fintech Private Limited and headquartered in Bengaluru. It is registered with SEBI as a Research Analyst (INH000018300) and delivers daily trade ideas with entry, exit and stop-loss levels authored by SEBI-registered research analysts, alongside a portfolio builder, live market data and stock pages, an advisors directory, and StockGro Academy courses used by 1,400+ educational institutions. Its AI assistant, Stoxo, answers market and research questions in conversational language. StockGro is an advisory and research platform connected to major Indian brokers for last-mile execution; it does not execute trades or hold client funds. StockGro publishes no public developer program: the company serves a substantive llms.txt for AI agents, and one internal FastAPI scoring service is publicly reachable at api.stockgro.club, but there is no documented API, portal, or SDK.'
image: https://www.stockgro.club/favicon.ico
layout: provider
modified: '2026-08-29'
name: StockGro
nav: Providers
network: true
overview: 'StockGro publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Health API, Process API, and TradeView Intraday Model API. Tagged areas include Company, Financial Services, Stock Market, Investing, and Market Data.


  The StockGro catalog on APIs.io includes 1 Spectral governance ruleset.


  StockGro''s developer surface includes engineering blog, support, signup flow, pricing, and 14 more developer resources.'
plans:
- name: Stockgro Plans Pricing
  plan_count: 0
  slug: stockgro-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Stockgro Rate Limits
  slug: stockgro-rate-limits
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: StockGro API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: stockgro-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 42.4
    developer_ergonomics: 37.5
    discoverability: 73.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 35.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/stockgro/stockgro-2026-09-02T160912.png
security:
- kind: authentication
  name: Stockgro Authentication
  slug: stockgro-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Stockgro Domain Security
  slug: stockgro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: stockgro-check-service-health
  slug: stockgro-check-service-health
- name: stockgro-process-trade-post
  slug: stockgro-process-trade-post
slug: stockgro
tags:
- Company
- Financial Services
- Stock Market
- Investing
- Market Data
- Financial Education
- Fintech
- India
- Advisory
- Social Investing
website: https://www.stockgro.club/
---
