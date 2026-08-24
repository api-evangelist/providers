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
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: The Bloomberg Add-in for Microsoft Excel provides formula functions including BDP (Bloomberg Data Point), BDH (Bloomberg Data History), BDS (Bloomberg Data Set), and BQL for accessing Bloomberg data d
  name: Bloomberg Excel Add-in
  slug: bloomberg-excel-addin
- description: Access Bloomberg Query Language (BQL) directly within Excel to run flexible, custom queries for financial data, analytics, and derived metrics using the Bloomberg BQL Add-in.
  name: Bloomberg BQL in Excel
  slug: bloomberg-bql-excel
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-excel-plug-ins-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bloomberg.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
created: '2024-01-01'
description: Bloomberg Excel Plug-ins integrate Bloomberg market data, analytics, and functions directly into Microsoft Excel. The Bloomberg Add-in for Excel provides the BDH, BDP, BDS, and other Bloomberg formula functions to pull real-time and historical data, enabling quantitative analysis, financial modeling, and reporting without leaving the spreadsheet environment.
features:
- description: Bloomberg Data Point formula for real-time and static data retrieval in Excel.
  name: BDP Formula
- description: Bloomberg Data History formula for historical time series data retrieval.
  name: BDH Formula
- description: Bloomberg Data Set formula for multi-cell data retrieval and tables.
  name: BDS Formula
- description: Bloomberg Query Language support directly in Excel for advanced custom queries.
  name: BQL Integration
- description: Automatic data refresh for real-time market data in Excel cells.
  name: Real-Time Updates
- description: Pre-built Excel templates for portfolio analysis, risk, and reporting.
  name: Portfolio Analysis Templates
finops:
- name: Bloomberg Excel Plug Ins Finops
  service_category: API
  slug: bloomberg-excel-plug-ins-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-excel-plug-ins.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Excel Plug-ins
nav: Providers
network: true
overview: 'Bloomberg Excel Plug-ins publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Excel, Spreadsheet, Financial Modeling, Market Data, and Bloomberg.


  Bloomberg Excel Plug-ins'' developer surface includes developer portal, documentation, support, and 3 more developer resources.'
plans:
- name: Bloomberg Excel Plug Ins Plans Pricing
  plan_count: 3
  slug: bloomberg-excel-plug-ins-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Bloomberg Excel Plug Ins Rate Limits
  slug: bloomberg-excel-plug-ins-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 19.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-excel-plug-ins/refs/heads/main/screenshots/bloomberg-excel-plug-ins-2026-06-20T173424.png
security:
- kind: domain-security
  name: Bloomberg Excel Plug Ins Domain Security
  slug: bloomberg-excel-plug-ins-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-excel-plug-ins
tags:
- Excel
- Spreadsheet
- Financial Modeling
- Market Data
- Bloomberg
- Add-in
use_cases:
- description: Build discounted cash flow models and valuation models with live Bloomberg data.
  name: Financial Modeling
- description: Create automated portfolio reports with real-time and historical data.
  name: Portfolio Reporting
- description: Pull pricing, volatility, and correlation data for risk calculations.
  name: Risk Analysis
- description: Analyze market trends and securities data without leaving Excel.
  name: Market Research
- description: Run quantitative screens and backtests using Bloomberg historical data in Excel.
  name: Quantitative Analysis
website: https://www.bloomberg.com/professional/
---
