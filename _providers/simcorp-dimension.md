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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 6
apis:
- description: RESTful API for accessing portfolio data, positions, transactions, and market data from SimCorp Dimension.
  name: SimCorp Dimension Data API
  slug: simcorp-dimension-data-api
- description: API for integrating third-party systems with SimCorp Dimension for data synchronization and workflow automation.
  name: SimCorp Dimension Integration API
  slug: simcorp-dimension-integration-api
- description: API for accessing analytics, performance metrics, risk calculations, and reporting data.
  name: SimCorp Dimension Analytics API
  slug: simcorp-dimension-analytics-api
- description: Web API providing HTTP-based interfaces for accessing and manipulating SimCorp Dimension data in real-time, supporting stateless RESTful operations across the investment management lifecycle.
  name: SimCorp Dimension Web API
  slug: simcorp-dimension-web-api
- description: API for distributing and sharing investment data across integrated systems, supporting event streaming channels and direct data access from SimCorp Dimension.
  name: SimCorp Dimension Data Distribution API
  slug: simcorp-dimension-data-distribution-api
- description: Real-time streaming API for delivering live investment data, market updates, and event-driven notifications from SimCorp Dimension.
  name: SimCorp Dimension Streaming API
  slug: simcorp-dimension-streaming-api
artifact_total: 28
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simcorp-dimension-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SimCorp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/simcorp-dimension
- group: start
  title: ''
  type: Portal
  url: https://www.simcorp.com/solutions/simcorp-one
- group: docs
  title: ''
  type: Documentation
  url: https://thesim.dev/
- group: other
  title: ''
  type: Portfolio Management
  url: https://www.simcorp.com/solutions/simcorp-one/portfolio-management
- group: auth
  title: ''
  type: Trading and Compliance
  url: https://www.simcorp.com/solutions/simcorp-one/trading-and-compliance
- group: other
  title: ''
  type: Risk and Performance
  url: https://www.simcorp.com/solutions/simcorp-one/risk-and-performance
- group: other
  title: ''
  type: Operations
  url: https://www.simcorp.com/solutions/simcorp-one/operations
- group: other
  title: ''
  type: Accounting
  url: https://www.simcorp.com/solutions/simcorp-one/accounting
- group: other
  title: ''
  type: Data Management
  url: https://www.simcorp.com/solutions/simcorp-one/data-management
- group: other
  title: ''
  type: Reporting
  url: https://www.simcorp.com/solutions/simcorp-one/reporting
- group: build
  title: ''
  type: Client Communications
  url: https://www.simcorp.com/solutions/simcorp-one/Client-Communications-and-Regulatory-Reporting
- group: company
  title: ''
  type: Partners
  url: https://www.simcorp.com/partners/open-platform-partners
- group: other
  title: ''
  type: Resources
  url: https://en.wikipedia.org/wiki/SimCorp
- group: other
  title: ''
  type: Resources
  url: https://www.simcorp.com/about-us/news/2024/simcorp-introduces-new-flagship-platform-simcorp-one
- group: operate
  title: ''
  type: Support
  url: https://www.dimensionalcommunity.com/insights
- group: design
  title: ''
  type: JSONLD
  url: json-ld/simcorp-dimension-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/simcorp-dimension-portfolio-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/simcorp-dimension-instrument-schema.json
created: '2024'
description: Investment management software solution providing APIs for portfolio management, accounting, risk management, and investment operations. SimCorp Dimension is part of the SimCorp One integrated platform, offering Web APIs, Data Distribution APIs, and Streaming APIs through the SimCorp Integration Model (SIM) for front-to-back office investment management.
features:
- Front-to-back investment management
- Real-time portfolio data and analytics
- Event-driven streaming data distribution
- Risk and performance measurement
- Accounting and operations management
- Trading and compliance monitoring
- Client communications and regulatory reporting
- Open platform integration model
finops:
- name: Simcorp Dimension Finops
  service_category: API
  slug: simcorp-dimension-finops
image: https://www.simcorp.com/logo.png
json_schemas:
- name: SimCorp Dimension Instrument
  property_count: 23
  slug: simcorp-dimension-instrument
- name: SimCorp Dimension Portfolio
  property_count: 24
  slug: simcorp-dimension-portfolio
jsonld:
- class_count: 0
  name: Simcorp Dimension Context
  property_count: 8
  slug: simcorp-dimension-context
layout: provider
modified: '2026-04-18'
name: SimCorp Dimension
nav: Providers
network: true
overview: 'SimCorp Dimension publishes 3 APIs on the [APIs.io](https://apis.io/) network: Data API, Integration API, and Analytics API. Tagged areas include Accounting, Asset Management, Compliance, Data Distribution, and Enterprise Software.


  The SimCorp Dimension catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SimCorp Dimension''s developer surface includes developer portal, documentation, support, and 17 more developer resources.'
plans:
- name: Simcorp Dimension Plans Pricing
  plan_count: 3
  slug: simcorp-dimension-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Simcorp Dimension Rate Limits
  slug: simcorp-dimension-rate-limits
rules:
- name: SimCorp Dimension API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: simcorp-dimension-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 40.3
    developer_ergonomics: 21.7
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 40.2
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simcorp-dimension/refs/heads/main/screenshots/simcorp-dimension-2026-06-20T193926.png
security:
- kind: domain-security
  name: Simcorp Dimension Domain Security
  slug: simcorp-dimension-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: simcorp-dimension
tags:
- Accounting
- Asset Management
- Compliance
- Data Distribution
- Enterprise Software
- Financial Data
- Financial Technology
- Investment Management
- Portfolio Management
- Risk Management
- SimCorp One
- Streaming
- Trading
use_cases:
- Portfolio management and analysis
- Investment data integration and distribution
- Risk and performance reporting
- Regulatory compliance and reporting
- Real-time market data streaming
- Multi-asset investment operations
website: https://www.simcorp.com/solutions/simcorp-one
---
