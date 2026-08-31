---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-08-30'
api_count: 10
apis:
- description: REST APIs for MSCI index data including index levels and performance, constituents, security master, dividends, and corporate events for MSCI indexes across supported variants and currencies.
  name: MSCI Index API
  slug: msci-index-api
- description: Real-time index and factor data API delivering intraday index levels for MSCI indexes.
  name: MSCI Real Time Index API
  slug: msci-real-time-index-api
- description: Retrieve current day and historical ESG data for entitled issuers, providing access to thousands of ESG data points including MSCI ESG Ratings and underlying raw data.
  name: MSCI ESG Data API
  slug: msci-esg-data-api
- description: Access ESG documents and reports for companies, funds, and industries as PDF and HTML documents.
  name: MSCI ESG Report API
  slug: msci-esg-report-api
- description: On-demand access to MSCI sustainability and climate datasets, including climate metrics for portfolio and issuer analysis.
  name: MSCI Sustainability and Climate On-Demand API
  slug: msci-sustainability-and-climate-on-demand-api
- description: RiskMetrics RiskManager-based analytics APIs for risk measurement, stress testing, and exposure analysis across portfolios.
  name: MSCI Risk Analytics API
  slug: msci-risk-analytics-api
- description: Instrument-level analytics API for pricing and risk measures across asset classes using MSCI models.
  name: MSCI Instrument Analytics API
  slug: msci-instrument-analytics-api
- description: Portfolio optimization service from MSCI Quantitative Investment Solutions supporting portfolio and tax-lot upload in JSON and tax-aware optimizations; accessible through the official MSCI Python SDK.
  name: MSCI Optimization Service API
  slug: msci-optimization-service-api
- description: Real estate index and market data API covering property fund and asset performance and risk data across global markets.
  name: MSCI Real Estate Performance and Risk Data API
  slug: msci-real-estate-performance-and-risk-data-api
- description: Private capital data API providing asset and deal-level metrics for private asset funds and portfolios.
  name: MSCI Private Asset and Deal Metrics API
  slug: msci-private-asset-and-deal-metrics-api
artifact_total: 13
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/msci-inc
- group: company
  title: ''
  type: Website
  url: https://www.msci.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.msci.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.msci.com/apis
- group: docs
  title: ''
  type: APIReference
  url: https://developer.msci.com/apis
- group: operate
  title: ''
  type: Support
  url: https://support.msci.com
- group: start
  title: ''
  type: Login
  url: https://one.msci.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.msci.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.msci.com/privacy-pledge
- group: build
  title: ''
  type: Packages
  url: packages/msci-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/msci-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/msci-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/msci-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/msci-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/msci-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/msci-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/msci-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/msci-domain-security.yml
created: '2026-05-05'
description: MSCI is a leading provider of critical decision support tools and services for the global investment community, publishing indexes, ESG and climate ratings, risk analytics, and real estate and private asset data. The MSCI Developer Community at developer.msci.com catalogs thirty-plus REST APIs spanning index performance and constituents, ESG data and reports, sustainability and climate on-demand data, risk and instrument analytics, portfolio optimization, real estate performance, and private capital metrics, alongside an official Python SDK and the MSCI Connector, a Model Context Protocol server listed in the Claude connector directory.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/msci.png
layout: provider
mcp_servers:
- description: ''
  name: MSCI Connector
  slug: msci-connector
modified: '2026-07-22'
name: MSCI
nav: Providers
network: true
overview: 'MSCI publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Data, Indexes, ESG, Climate, and Risk Analytics.


  MSCI''s developer surface includes documentation, API reference, support, authentication, and 14 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 20.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/msci/refs/heads/main/screenshots/msci-2026-06-20T185849.png
security:
- kind: authentication
  name: Msci Authentication
  slug: msci-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Msci Domain Security
  slug: msci-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: msci
tags:
- Financial Data
- Indexes
- ESG
- Climate
- Risk Analytics
- Real-Estate
- Private Assets
- Investing
website: https://www.msci.com
---
