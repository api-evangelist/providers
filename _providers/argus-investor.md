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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Argus Research API provides programmatic access to equity research reports, stock ratings, analyst recommendations, earnings estimates, target prices, and sector analysis. Used by institutional cl
  name: Argus Research API
  slug: argus-research-api
artifact_total: 24
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/argus-investor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.argusresearch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.argusresearch.com/
- group: start
  title: ''
  type: Portal
  url: https://www.argusresearch.com/
- group: operate
  title: ''
  type: Support
  url: https://www.argusresearch.com/
- group: company
  title: ''
  type: Blog
  url: https://www.argusresearch.com/
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
modified: '2026-04-19'
name: Argus Investor
nav: Providers
network: true
overview: 'Argus Investor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Equity Analysis, Financial Data, Financial Services, Investment Ratings, and Stock Research.


  Argus Investor''s developer surface includes documentation, developer portal, support, engineering blog, and 2 more developer resources.'
plans:
- name: Argus Investor Plans Pricing
  plan_count: 3
  slug: argus-investor-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Argus Investor Rate Limits
  slug: argus-investor-rate-limits
score:
  band: emerging
  composite: 15.4
  delta: 0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
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
- Financial Services
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
