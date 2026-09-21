---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: 'Argus Research Company''s coverage and ratings surface: analyst BUY/HOLD/SELL recommendations and target prices on 500+ US equities across 60+ industries, A6 quantitative ratings on 1,100+ companies, a'
  name: Argus Research Coverage and Ratings
  slug: argus-research-api
artifact_total: 24
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/argus-investor/refs/heads/main/security/argus-investor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/argus-investor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.argusresearch.com/
- group: operate
  title: ''
  type: Support
  url: https://www.argusresearch.com/ContactUs.aspx
- group: start
  title: ''
  type: Login
  url: https://www.argusresearch.com/Login/tabid/202/Default.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.argusresearch.com/terms.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.argusresearch.com/privacy.aspx
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/argus-investor/refs/heads/main/llms/argus-investor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/argus-investor-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.argusresearch.com/
coverage:
  checked: '2026-09-14'
  detail: 'argusresearch.com is a DotNetNuke marketing site with a subscriber Login and no developer section anywhere in its navigation: /openapi.json, /llms.txt, /robots.txt and all nine named /.well-known/ paths return a branded 404, api./developer./data./docs. are DNS wildcards serving the same marketing home page, and the fourteen Our Services pages describe report, platform and licensed-distribution products (Bloomberg, Fidelity, Schwab, Interactive Brokers) without naming an API, SDK, data feed or contract of any kind.'
  evidence:
  - status: 404
    url: https://www.argusresearch.com/openapi.json
  - status: 404
    url: https://www.argusresearch.com/llms.txt
  - status: 404
    url: https://www.argusresearch.com/.well-known/agent-card.json
  - status: 200
    url: https://www.argusresearch.com/AboutUs/OurServices.aspx
  - status: 200
    url: https://api.argusresearch.com/
  reason: no-developer-program
  state: none
created: '2024-01-15'
description: Argus Research Company is an independent equity research firm founded in 1934, providing institutional-quality investment research, stock ratings, and analyst recommendations for 500+ publicly traded companies. The firm publishes fundamental research, earnings estimates, target prices, and Buy/Hold/Sell ratings across all major sectors including healthcare, technology, financial services, and industrials. Research is distributed to institutional clients and through financial data platforms including Bloomberg, Fidelity, Schwab, and Interactive Brokers.
features:
- description: In-depth company analysis using a six-point system covering financials, management, competitive position, earnings quality, growth, and valuation.
  name: Fundamental Equity Research
- description: Clear investment recommendations with target prices and time horizon for 500+ publicly traded companies.
  name: Buy/Hold/Sell Ratings
- description: Quarterly and annual earnings per share estimates for covered securities with revision history.
  name: Earnings Estimates
- description: Regular sector-level commentary and relative weighting recommendations across major GICS sectors.
  name: Sector Analysis
- description: Weekly macro-economic analysis covering interest rates, GDP, employment, and market conditions.
  name: Economic Commentary
- description: Curated model portfolios across growth, income, and defensive strategies with performance tracking.
  name: Model Portfolios
- description: No investment banking conflicts — Argus does not underwrite IPOs, broker trades, or manage money.
  name: Institutional Independence
- description: Daily and weekly market analysis including Daily Spotlight, Market Watch, and analyst quick notes.
  name: Market Commentary
finops:
- name: Argus Investor Finops
  service_category: API
  slug: argus-investor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/argus-investor.png
integrations:
- description: Argus research distributed through Bloomberg Terminal for institutional clients.
  name: Bloomberg
- description: Argus ratings and reports available on Fidelity research platform for retail and institutional investors.
  name: Fidelity
- description: Argus content integrated into Schwab's research and planning tools.
  name: Charles Schwab
- description: Argus research available through Interactive Brokers research portal.
  name: Interactive Brokers
- description: Argus analyst commentary and ratings cited in Reuters financial news coverage.
  name: Reuters
- description: Argus ratings featured in Yahoo Finance analyst rating aggregations.
  name: Yahoo Finance
layout: provider
modified: '2026-09-14'
name: Argus Investor
nav: Providers
network: true
overview: 'Argus Investor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Equity Analysis, Financial Data, Financial-Services, Investment Ratings, and Stock Research.


  Argus Investor''s developer surface includes support, engineering blog, and 6 more developer resources.'
plans:
- name: Argus Investor Plans Pricing
  plan_count: 0
  slug: argus-investor-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Argus Investor Rate Limits
  slug: argus-investor-rate-limits
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 59.3
    operational_transparency: 0.0
  previous_composite: 14.5
  provenance:
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/argus-investor/refs/heads/main/screenshots/argus-investor-2026-06-20T172426.png
security:
- kind: domain-security
  name: Argus Investor Domain Security
  slug: argus-investor-domain-security
  summary_line: TLSv1.2 · DMARC
slug: argus-investor
tags:
- Equity Analysis
- Financial Data
- Financial-Services
- Investment Ratings
- Stock Research
use_cases:
- description: Integrate Argus ratings and estimates into portfolio management systems and research platforms.
  name: Portfolio Research Integration
- description: Screen securities by Argus rating, sector, market cap, and analyst confidence level.
  name: Stock Screening
- description: Access Argus estimates as an independent data point alongside consensus estimates.
  name: Earnings Estimate Consensus
- description: Distribute Argus research reports to brokerage clients via financial data platforms.
  name: Brokerage Research Distribution
- description: Track rating changes and analyst recommendations for investment committee compliance.
  name: Compliance Monitoring
website: https://www.argusresearch.com/
---
