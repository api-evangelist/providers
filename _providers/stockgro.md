---
access_model:
  confidence: medium
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.stockgro.club
  baseurl_source: declared
  description: Real-time scoring service for intraday trade predictions, published as an auto-generated FastAPI OpenAPI 3.1.0 document served without authentication at api.stockgro.club/openapi.json. Three operation
  name: TradeView Intraday Model API
  slug: stockgro-tradeview-intraday-model-api
artifact_total: 5
common:
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
  title: ''
  type: LLMsTxt
  url: llms/stockgro-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/stockgro-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/stockgro-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stockgro-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stockgro-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stockgro-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stockgro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stockgro-rate-limits.yml
- group: agent
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
overview: 'StockGro publishes 1 API on the [APIs.io](https://apis.io/) network: TradeView Intraday Model API. Tagged areas include Company, Financial-Services, Stock Market, Investing, and Market Data.


  StockGro''s developer surface includes engineering blog, support, signup flow, pricing, and 13 more developer resources.'
plans:
- name: Stockgro Plans Pricing
  plan_count: 0
  slug: stockgro-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Stockgro Rate Limits
  slug: stockgro-rate-limits
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 38.8
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 36.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 60.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stockgro/refs/heads/main/screenshots/stockgro-2026-09-02T160912.png
security:
- kind: authentication
  name: Stockgro Authentication
  slug: stockgro-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Stockgro Domain Security
  slug: stockgro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stockgro
tags:
- Company
- Financial-Services
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
