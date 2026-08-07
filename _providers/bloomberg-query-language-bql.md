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
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: Execute BQL queries programmatically via the Bloomberg API to retrieve custom computed financial data, filtered security sets, and time series expressions from Bloomberg's data universe. Accessible vi
  name: Bloomberg Query Language (BQL) API
  slug: bql-api
- description: Use Bloomberg Query Language directly in Microsoft Excel to execute complex data queries and retrieve computed results in spreadsheet cells. Supports multi-row outputs, time series, and calculated fie
  name: BQL in Bloomberg Excel Add-in
  slug: bql-excel
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-query-language-bql-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomberg.com/professional/support/api-library/
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
description: Bloomberg Query Language (BQL) is a proprietary query language for accessing, filtering, aggregating, and computing on Bloomberg's financial data universe. BQL enables users to write flexible data requests that go beyond standard API fields, supporting derived calculations, time series expressions, and complex filtering of securities and data points. Available in the Bloomberg Terminal, Excel Add-in, and via API.
features:
- description: Filter securities using complex logical and conditional expressions.
  name: Security Universe Filtering
- description: Compute derived financial metrics and ratios in BQL expressions.
  name: Derived Calculations
- description: Build time series queries for historical data analysis.
  name: Time Series Expressions
- description: Aggregate data with sum, average, rank, and other functions.
  name: Aggregation Functions
- description: Query Bloomberg data across equities, fixed income, FX, and commodities.
  name: Cross-Asset Data Access
- description: Execute BQL queries directly in Excel cells for spreadsheet analysis.
  name: BQL in Excel
finops:
- name: Bloomberg Query Language Bql Finops
  service_category: API
  slug: bloomberg-query-language-bql-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-query-language-bql.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Query Language (BQL)
nav: Providers
network: true
overview: 'Bloomberg Query Language (BQL) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include BQL, Query Language, Financial Data, Analytics, and Data Query.


  Bloomberg Query Language (BQL)''s developer surface includes developer portal, documentation, support, and 3 more developer resources.'
plans:
- name: Bloomberg Query Language Bql Plans Pricing
  plan_count: 3
  slug: bloomberg-query-language-bql-plans-pricing
random_paper: 97
rate_limits:
- limit_count: 5
  name: Bloomberg Query Language Bql Rate Limits
  slug: bloomberg-query-language-bql-rate-limits
score:
  band: emerging
  composite: 26.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 26.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-query-language-bql/refs/heads/main/screenshots/bloomberg-query-language-bql-2026-07-25T203403.png
security:
- kind: domain-security
  name: Bloomberg Query Language Bql Domain Security
  slug: bloomberg-query-language-bql-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-query-language-bql
tags:
- BQL
- Query Language
- Financial Data
- Analytics
- Data Query
- Bloomberg
use_cases:
- description: Screen securities using complex fundamental and technical criteria.
  name: Quantitative Screening
- description: Create custom financial metrics not available as standard data fields.
  name: Custom Analytics
- description: Analyze portfolio characteristics using flexible BQL expressions.
  name: Portfolio Analysis
- description: Access historical data via BQL time series for strategy backtesting.
  name: Backtesting
- description: Compute and aggregate risk metrics across portfolios using BQL.
  name: Risk Reporting
website: https://www.bloomberg.com/professional/
---
