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
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 5
apis:
- description: The core Bloomberg API providing real-time market data, reference data, historical data, and intraday tick data. SDKs available for C++, Java, Python, C#/.NET, and Perl. Connects to Bloomberg Terminal
  name: Bloomberg Open API (BLPAPI)
  slug: blpapi
- description: A powerful query language for requesting Bloomberg data with flexible filtering, aggregation, and calculation capabilities. Enables custom data requests beyond standard API fields.
  name: Bloomberg Query Language (BQL)
  slug: bql
- description: Enterprise data delivery platform providing bulk financial data via SFTP and SOAP API. Supports requesting reference data, pricing data, corporate actions, and derived data for specified securities an
  name: Bloomberg Data License API
  slug: data-license
- description: High-performance server-side API for distributing Bloomberg data within enterprise environments. Supports B-PIPE for managed data distribution with authentication, authorization, and entitlement manag
  name: Bloomberg Server API (SAPI)
  slug: server-api
- description: Access to Bloomberg Intelligence research reports, analyst insights, industry analysis, and company research across equities, credit, government, and ESG.
  name: Bloomberg Intelligence Research API
  slug: research-api
artifact_total: 32
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bloomberg/blpapi-node/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/bloomberg/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/bloomberg/.github/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-intelligence-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/bloomberg-intelligence
- group: start
  title: ''
  type: Portal
  url: https://developer.bloomberg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomberg.com/professional/support/api-library/
- group: start
  title: ''
  type: GettingStarted
  url: https://bloomberg.github.io/blpapi-docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- group: build
  title: Python SDK (blpapi)
  type: SDKs
  url: https://pypi.org/project/blpapi/
- group: build
  title: Node.js SDK
  type: SDKs
  url: https://www.npmjs.com/package/blpapi
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
description: Bloomberg Intelligence provides research, data, and analytics on companies, industries, credit, government, litigation, and ESG. The Bloomberg developer platform offers BLPAPI (Bloomberg Open API) for real-time and reference data, BQL (Bloomberg Query Language) for flexible data queries, Data License for enterprise data delivery, and Server API / B-PIPE for high-performance data distribution.
features:
- description: Streaming real-time prices, quotes, and market activity across global markets.
  name: Real-Time Market Data
- description: Static and semi-static security attributes, corporate actions, and fundamentals.
  name: Reference Data
- description: End-of-day and intraday historical pricing, volume, and analytics data.
  name: Historical Data
- description: Tick-by-tick trade and quote data for detailed market microstructure analysis.
  name: Intraday Tick Data
- description: Flexible query language for custom data requests with filtering and aggregation.
  name: Bloomberg Query Language (BQL)
- description: Bulk enterprise data delivery via SFTP and SOAP for reference data, pricing, and analytics.
  name: Data License
- description: Managed high-performance data distribution with entitlement management for enterprise.
  name: B-PIPE Data Distribution
- description: Analyst research reports, industry analysis, and ESG insights from Bloomberg Intelligence.
  name: Intelligence Research
- description: Official SDKs for Python, Java, C++, C#/.NET, Node.js, and Perl.
  name: Multi-Language SDKs
- description: Authentication, authorization, and permissioning for enterprise data distribution.
  name: Enterprise Authentication
finops:
- name: Bloomberg Intelligence Finops
  service_category: API
  slug: bloomberg-intelligence-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-intelligence.png
layout: provider
modified: '2026-04-17'
name: Bloomberg Intelligence
nav: Providers
network: true
overview: 'Bloomberg Intelligence publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company Analysis, Credit Research, ESG Data, Financial Data, and Financial Research.


  The Bloomberg Intelligence catalog on APIs.io includes 1 Spectral governance ruleset.


  Bloomberg Intelligence''s developer surface includes developer portal, documentation, getting-started guide, support, and 10 more developer resources.'
plans:
- name: Bloomberg Intelligence Plans Pricing
  plan_count: 3
  slug: bloomberg-intelligence-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Bloomberg Intelligence Rate Limits
  slug: bloomberg-intelligence-rate-limits
rules:
- effective_rule_count: 17
  extends: []
  name: Bloomberg Intelligence API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: bloomberg-intelligence-spectral-rules
score:
  band: thin
  composite: 28.2
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 39.4
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 64.8
    governance: 39.4
    operational_transparency: 10.5
  previous_composite: 28.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-intelligence/refs/heads/main/screenshots/bloomberg-intelligence-2026-06-20T173440.png
security:
- kind: domain-security
  name: Bloomberg Intelligence Domain Security
  slug: bloomberg-intelligence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloomberg-intelligence
solutions:
- description: Professional terminal with integrated BLPAPI for desktop application development.
  name: Bloomberg Terminal
- description: Server API and B-PIPE for enterprise-wide data distribution.
  name: Bloomberg Enterprise
- description: Bulk data delivery platform for enterprise data management.
  name: Bloomberg Data License
- description: Research and analysis platform with proprietary data and expert insights.
  name: Bloomberg Intelligence
tags:
- Company Analysis
- Credit Research
- ESG Data
- Financial Data
- Financial Research
- Market Data
- Market Intelligence
use_cases:
- description: Feed real-time market data into trading and execution management systems.
  name: Trading Systems
- description: Source pricing and reference data for portfolio risk calculations.
  name: Risk Management
- description: Access historical data and BQL for quantitative analysis and backtesting.
  name: Quantitative Research
- description: Retrieve security attributes and pricing for portfolio valuation and attribution.
  name: Portfolio Analytics
- description: Source reference data for regulatory reporting and compliance.
  name: Compliance and Reporting
- description: Bulk load financial data via Data License for enterprise data warehouses.
  name: Data Warehousing
- description: Access Bloomberg Intelligence ESG scores and research for sustainable investing.
  name: ESG Analysis
- description: Access credit analysis, ratings data, and fixed income research.
  name: Credit Research
website: https://developer.bloomberg.com/
---
