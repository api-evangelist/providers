---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
  scored_at: '2026-08-24'
api_count: 7
apis:
- description: FMX Futures Exchange launched September 23, 2024, initially listing SOFR futures (the largest notional futures contract in the world) and adding U.S. Treasury futures in Q1 2025. Equity partners inclu
  name: FMX Futures Exchange Connectivity
  slug: fmx-futures
- description: FMX UST (formerly Fenics UST) is BGC's electronic trading venue for U.S. Treasuries. Connectivity is a "point-to-point service based on industry standards TCP/IP and the FIX Protocol." Supports FIX 4.
  name: FMX UST
  slug: fmx-ust
- description: FMX FX (operating as Fenics FX) is BGC's electronic foreign exchange platform covering Spot, Forwards, NDFs and Options. Integration is offered via FIX (order entry) and ITCH/OUCH (market data and ord
  name: FMX FX (Fenics FX)
  slug: fmx-fx
- description: Fenics Market Data (FMD) is the exclusive data distributor of BGC Group, Inc. and its affiliates. FMD provides streaming, intra-day, end-of-day and historical market data across Foreign Exchange (350+
  name: Fenics Market Data
  slug: fenics-market-data
- description: 'Lucera is BGC''s financial technology subsidiary offering a "high-performance, low latency platform that provides a single API for aggregating and trading across multiple markets – FX, Rates, Futures, '
  name: Lucera LumeMarkets
  slug: lucera
- description: 'Capitalab is BGC''s post-trade compression, optimization and risk-mitigation arm. It executes initial margin optimization runs across interest rate, FX, inflation and credit derivatives portfolios for '
  name: Capitalab
  slug: capitalab
- description: GFI Group, Inc. is a wholly owned BGC subsidiary — "a leading intermediary and provider of trading technologies and support services to the global OTC and listed markets." GFI offers voice and electro
  name: GFI Group
  slug: gfi-group
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bgc-partners-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bgc-partners-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bgcg.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.bgcg.com
- group: operate
  title: ''
  type: PressReleases
  url: https://www.bgcg.com/press-releases/
- group: company
  title: ''
  type: News
  url: https://www.bgcg.com/news/
- group: company
  title: ''
  type: Careers
  url: https://www.bgcg.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.bgcg.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bgcg.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bgcg.com/terms-of-use/
- group: other
  title: ''
  type: SECFilings
  url: https://ir.bgcg.com/financials/sec-filings/
- group: other
  title: ''
  type: AnnualReports
  url: https://ir.bgcg.com/financials/annual-reports/
- group: other
  title: ''
  type: StockTicker
  url: https://ir.bgcg.com/stock-info/stock-quote/
- group: other
  title: ''
  type: SpinOff
  url: https://www.nmrk.com
- group: other
  title: ''
  type: Subsidiary
  url: https://www.fmx.com
- group: company
  title: ''
  type: ClearingPartner
  url: https://www.lch.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bgc-group/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bgc-partners-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bgc-partners-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/bgc-partners-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bgc-partners-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bgc-partners-finops.yml
created: '2026-05-05'
description: 'BGC Group, Inc. (NASDAQ: BGC), formerly BGC Partners, is a global brokerage and financial technology firm. Headquartered in New York and London, BGC operates electronic and voice broking across foreign exchange, interest rate derivatives, fixed income, energy and commodities, equity derivatives, credit, and futures. Its technology portfolio includes the FMX division (FMX UST, FMX FX, and FMX Futures Exchange — launched September 23, 2024 for SOFR futures), Fenics Market Data (the exclusive data distributor for BGC and its affiliates), Capitalab (post-trade optimization), Lucera (LumeMarkets cross-asset trading platform and Lucera Connect/Compute infrastructure), and GFI Group. BGC spun off Newmark Group (NASDAQ: NMRK) on November 30, 2018. Public developer documentation is generally gated behind sales engagement; protocol specifications (FIX, ITCH/SoupBinTCP, BIMP, BOP) exist for institutional clients.'
finops:
- name: Bgc Partners Finops
  service_category: ''
  slug: bgc-partners-finops
image: https://www.bgcg.com/wp-content/uploads/2023/06/BGC-Group-Logo.svg
jsonld:
- class_count: 42
  name: Bgc Partners Context
  property_count: 0
  slug: bgc-partners-context
layout: provider
modified: '2026-05-23'
name: BGC Group
nav: Providers
network: true
overview: 'BGC Group publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Brokerage, Inter-Dealer Broker, Financial-Services, Capital Markets, and Market Data.


  The BGC Group catalog on APIs.io includes 1 JSON-LD context.


  BGC Group''s developer surface includes developer portal, product news, and 20 more developer resources.'
plans:
- name: Bgc Partners Plans Pricing
  plan_count: 6
  slug: bgc-partners-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Bgc Partners Rate Limits
  slug: bgc-partners-rate-limits
score:
  band: emerging
  composite: 23.1
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 15.2
    contract_quality: 11.3
    developer_ergonomics: 9.5
    discoverability: 81.5
    governance: 15.2
    operational_transparency: 0.0
  previous_composite: 23.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Bgc Partners Domain Security
  slug: bgc-partners-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bgc Partners Vulnerability Disclosure
  slug: bgc-partners-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bgc-partners
tags:
- Brokerage
- Inter-Dealer Broker
- Financial-Services
- Capital Markets
- Market Data
- Foreign Exchange
- Fixed Income
- Interest Rate Derivatives
- Energy And Commodities
- Equity Derivatives
- Credit Derivatives
- Futures Exchange
- SOFR
- US Treasuries
- Post-Trade
- Trading Infrastructure
- Financial Technology
- Fortune 1000
website: https://www.bgcg.com
---
