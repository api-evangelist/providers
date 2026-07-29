---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Sandp Global Agentic Access
  operation_count: 8
  slug: sandp-global-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 6
apis:
- description: The S&P Global Marketplace Catalog API provides programmatic access to the S&P Global data marketplace, enabling discovery and consumption of available data products, datasets, and API solutions acros
  name: S&P Global Marketplace Catalog API
  slug: sandp-global-marketplace-catalog-api
- description: Token generation and refresh operations
  name: S&P Global Authentication API
  slug: sandp-global-authentication-api
- description: Retrieve fundamental financial data for companies
  name: S&P Global Financial Data API
  slug: sandp-global-financial-data-api
- description: Real-time and historical market data
  name: S&P Global Market Data API
  slug: sandp-global-market-data-api
- description: Commodity price assessment data
  name: S&P Global Price Assessments API
  slug: sandp-global-price-assessments-api
- description: Commodity, location, and entity reference data
  name: S&P Global Reference Data API
  slug: sandp-global-reference-data-api
artifact_total: 22
collections:
- collection_type: open
  name: S&P Capital IQ API
  slug: open-sandp-global-capital-iq
- collection_type: open
  name: S&P Global Commodity Insights API
  slug: open-sandp-global-commodity-insights
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sandp-global-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sandp-global-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sandp-global-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spgi-ci
- group: company
  title: ''
  type: Website
  url: https://www.spglobal.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.spglobal.com
- group: other
  title: ''
  type: Marketplace
  url: https://www.marketplace.spglobal.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.support.marketplace.spglobal.com
- group: auth
  title: ''
  type: Authentication
  url: https://developer.spglobal.com/getting-started/Auth.html
- group: build
  title: ''
  type: Python SDK
  url: https://pypi.org/project/spgci/
- group: build
  title: ''
  type: Python SDK
  url: https://pypi.org/project/SPGMICIQ/
- group: operate
  title: ''
  type: FAQ
  url: https://developer.spglobal.com/support/faq
- group: operate
  title: ''
  type: Support
  url: https://commodityinsightssupport.spglobal.com
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sandp-global-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/sandp-global-rules.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/market-intelligence.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sandp-global-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.spglobal.com/llms.txt
created: '2026-05-02'
description: 'S&P Global is a leading provider of credit ratings, benchmarks, analytics, and workflow solutions in the global capital, commodity, and automotive markets. S&P Global offers multiple API product lines across its business divisions: the Capital IQ API provides comprehensive financial and market intelligence data; the Commodity Insights API provides price assessments, market data, and analytics for energy and commodities markets; and the Marketplace API enables programmatic access to the S&P Global data marketplace catalog.'
examples:
- key_count: 2
  name: Sandp Global Get Financial Data Example
  slug: sandp-global-get-financial-data-example
- key_count: 2
  name: Sandp Global Get Latest Prices Example
  slug: sandp-global-get-latest-prices-example
finops:
- name: Sandp Global Finops
  service_category: Financial Market Data
  slug: sandp-global-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sandp-global.png
json_schemas:
- name: S&P Capital IQ Financial Data Request
  property_count: 1
  slug: sandp-global-financial-data-request
- name: S&P Global Price Assessment
  property_count: 7
  slug: sandp-global-price-assessment
json_structures:
- name: Sandp Global Price Assessment Structure
  property_count: 0
  slug: sandp-global-price-assessment-structure
jsonld:
- class_count: 0
  name: Sandp Global Context
  property_count: 13
  slug: sandp-global-context
layout: provider
modified: '2026-05-19'
name: S&P Global
nav: Providers
network: true
overview: 'S&P Global publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Financial Data API, Market Data API, and 2 more. Tagged areas include Financial Data, Market Intelligence, Commodity Insights, Credit Ratings, and Analytics.


  The S&P Global catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  S&P Global''s developer surface includes authentication, documentation, FAQ, support, and 14 more developer resources.'
plans:
- name: Sandp Global Plans Pricing
  plan_count: 1
  slug: sandp-global-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Sandp Global Rate Limits
  slug: sandp-global-rate-limits
rules:
- name: S&P Global API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sandp-global-jsonschema-spectral-rules
- name: S&P Global API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: sandp-global-rules
score:
  band: developing
  composite: 50.1
  delta: -4.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 73.4
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sandp-global/refs/heads/main/screenshots/sandp-global-2026-06-20T193408.png
security:
- kind: authentication
  name: Sandp Global Authentication
  slug: sandp-global-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sandp Global Domain Security
  slug: sandp-global-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sandp-global
tags:
- Financial Data
- Market Intelligence
- Commodity Insights
- Credit Ratings
- Analytics
- Fortune 500
- Enterprise
website: https://www.spglobal.com
---
