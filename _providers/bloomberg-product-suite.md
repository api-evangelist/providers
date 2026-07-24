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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: The core API providing programmatic access to the Bloomberg data ecosystem including real-time prices, reference data, news, analytics, and Terminal functions.
  name: Bloomberg Open API (BLPAPI)
  slug: blpapi
- description: Enterprise bulk data delivery platform for acquiring Bloomberg reference data, pricing, corporate actions, and analytics at scale for data management and downstream applications.
  name: Bloomberg Data License
  slug: data-license
- description: Remote access service extending Bloomberg Terminal capabilities to any internet-connected device, enabling mobile and remote access to Bloomberg data, analytics, and messaging.
  name: Bloomberg Anywhere
  slug: bloomberg-anywhere
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-product-suite-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bloomberg.com/
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
  url: https://www.bloomberg.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
created: '2024-01-01'
description: Bloomberg's Product Suite encompasses the complete portfolio of Bloomberg professional products including the Bloomberg Terminal, data products, analytics solutions, trading platforms, media, and technology infrastructure. The suite serves financial professionals across asset management, banking, insurance, government, and corporate sectors with integrated data, analytics, and workflow tools.
features:
- description: Professional financial workstation with data, analytics, and messaging.
  name: Bloomberg Terminal
- description: B-PIPE and Data License for enterprise-wide data distribution.
  name: Enterprise Data
- description: PORT and multi-asset analytics for portfolio management.
  name: Portfolio Analytics
- description: EMSX and Tradebook for electronic order routing and execution.
  name: Trading Solutions
- description: Credit and market risk analytics across asset classes.
  name: Risk Solutions
- description: Bloomberg Intelligence research and analytics.
  name: Research Solutions
finops:
- name: Bloomberg Product Suite Finops
  service_category: API
  slug: bloomberg-product-suite-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-product-suite.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Product Suite
nav: Providers
network: true
overview: 'Bloomberg Product Suite publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Product Suite, Terminal, Data, Analytics, and Trading.


  Bloomberg Product Suite''s developer surface includes developer portal, documentation, support, and 4 more developer resources.'
plans:
- name: Bloomberg Product Suite Plans Pricing
  plan_count: 3
  slug: bloomberg-product-suite-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Bloomberg Product Suite Rate Limits
  slug: bloomberg-product-suite-rate-limits
score:
  band: thin
  composite: 30.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 30.0
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-product-suite/refs/heads/main/screenshots/bloomberg-product-suite-2026-06-20T173456.png
security:
- kind: domain-security
  name: Bloomberg Product Suite Domain Security
  slug: bloomberg-product-suite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloomberg-product-suite
tags:
- Product Suite
- Terminal
- Data
- Analytics
- Trading
- Financial Technology
- Bloomberg
use_cases:
- description: Full-lifecycle investment data and analytics for portfolio managers.
  name: Investment Management
- description: Order management and execution across equities, fixed income, FX, and derivatives.
  name: Trading and Execution
- description: Integrated risk analytics and regulatory compliance solutions.
  name: Risk and Compliance
- description: M&A, capital markets, and corporate treasury data and analytics.
  name: Corporate Finance
website: https://www.bloomberg.com/professional/
---
