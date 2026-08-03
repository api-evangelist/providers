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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 5
apis:
- description: Provides access to real-time and historical market data including stocks, bonds, commodities, and currencies through the Bloomberg Terminal and enterprise data feeds.
  name: Bloomberg Market Data API
  slug: market-data-api
- description: Access to Bloomberg's breaking news, articles, and multimedia content covering global markets and business through the Bloomberg Professional platform.
  name: Bloomberg News API
  slug: news-api
- description: 'Lightweight server-side API that delivers real-time market, historical, and key reference data as well as calculation engine capabilities for proprietary and third-party applications. Available in C, '
  name: Bloomberg Server API (SAPI)
  slug: server-api
- description: Provides programmatic access to Data License content via REST API, SFTP, or cloud providers, with available content including reference, pricing, regulatory, and alternative data for over 50 million s
  name: Bloomberg Data License API
  slug: data-license-api
- description: Core Bloomberg API providing a unified programming interface for Desktop API, Server API, B-PIPE, and Platform products. Available as SDKs for C++, C# (.NET), Java, and Python.
  name: Bloomberg BLPAPI
  slug: blpapi
artifact_total: 29
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-news-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bloomberg-news
- group: start
  title: ''
  type: Portal
  url: https://developer.bloomberg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bloomberg.github.io/blpapi-docs/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
- group: company
  title: ''
  type: Blog
  url: https://www.bloomberg.com/company/stories/category/tech-at-bloomberg/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/notices/
- group: operate
  title: ''
  type: Contact
  url: https://www.bloomberg.com/professional/contact-menu/
- group: start
  title: ''
  type: Login
  url: https://bba.bloomberg.net/
created: '2024-01-01'
description: Bloomberg News is a leading global provider of financial news, data, and analysis, delivering breaking news and insights on markets, economics, politics, and business. Bloomberg provides APIs through the Bloomberg Professional Services platform including BLPAPI, Server API, Data License, and market data services.
features:
- description: Access streaming real-time market data for equities, fixed income, commodities, and currencies.
  name: Real-Time Market Data
- description: Query historical pricing, volume, and fundamental data for backtesting and analysis.
  name: Historical Data Services
- description: Access comprehensive reference data for securities identification, corporate actions, and classifications.
  name: Reference Data
- description: Programmatic access to Bloomberg breaking news, articles, and research content.
  name: News and Research
- description: Server-side APIs for distributing Bloomberg data to internal applications and trading systems.
  name: Enterprise Data Distribution
- description: SDKs available in Python, Java, C++, C#, and C for cross-platform integration.
  name: Multi-Language SDK Support
finops:
- name: Bloomberg News Finops
  service_category: API
  slug: bloomberg-news-finops
image: /assets/icons/bloomberg-news.png
integrations:
- description: Bloomberg Excel Add-In for spreadsheet-based data analysis and modeling.
  name: Excel
- description: Python SDK (blpapi) for data science and quantitative finance applications.
  name: Python
- description: Bloomberg Datafeed Toolbox for MATLAB for financial modeling and analysis.
  name: MATLAB
- description: Rblpapi package for accessing Bloomberg data in R statistical computing.
  name: R
- description: Integration with order management and execution management systems.
  name: Trading Platforms
json_schemas:
- name: Bloomberg News Article
  property_count: 22
  slug: bloomberg-news-article
- name: Bloomberg Market Data
  property_count: 9
  slug: bloomberg-news-market-data
jsonld:
- class_count: 0
  name: Bloomberg News Context
  property_count: 10
  slug: bloomberg-news-context
layout: provider
modified: '2026-04-18'
name: Bloomberg News
nav: Providers
network: true
overview: 'Bloomberg News publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Business Intelligence, Financial Services, Market Data, and News.


  The Bloomberg News catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bloomberg News'' developer surface includes developer portal, documentation, support, engineering blog, and 7 more developer resources.'
plans:
- name: Bloomberg News Plans Pricing
  plan_count: 3
  slug: bloomberg-news-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Bloomberg News Rate Limits
  slug: bloomberg-news-rate-limits
rules:
- name: Bloomberg News API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: bloomberg-news-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.1
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 12.9
    developer_ergonomics: 23.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 41.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-news/refs/heads/main/screenshots/bloomberg-news-2026-06-20T173445.png
security:
- kind: domain-security
  name: Bloomberg News Domain Security
  slug: bloomberg-news-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloomberg-news
tags:
- Analytics
- Business Intelligence
- Financial Services
- Market Data
- News
use_cases:
- description: Build algorithmic trading strategies using real-time and historical market data feeds.
  name: Quantitative Trading
- description: Calculate portfolio risk metrics using Bloomberg's pricing and analytics data.
  name: Risk Management
- description: Automate financial research workflows with news, fundamental data, and analytics.
  name: Financial Research
- description: Generate regulatory compliance reports using reference data and pricing services.
  name: Regulatory Reporting
- description: Integrate Bloomberg data into portfolio management systems for real-time monitoring.
  name: Portfolio Management
website: https://developer.bloomberg.com/
---
