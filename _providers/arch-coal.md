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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Arch Coal Agentic Access
  operation_count: 3
  slug: arch-coal-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: SEC and regulatory filings
  name: Arch Coal Filings API
  slug: arch-coal-filings-api
- description: Financial performance metrics
  name: Arch Coal Financial API
  slug: arch-coal-financial-api
- description: Coal production and sales volume data
  name: Arch Coal Production API
  slug: arch-coal-production-api
artifact_total: 39
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arch-coal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arch-coal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arch-coal-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.arch-coal.com/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/arch-coal/refs/heads/main/rules/arch-coal-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/arch-coal/refs/heads/main/vocabulary/arch-coal-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/arch-coal/refs/heads/main/json-ld/arch-coal-investor-relations-api-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://archresources.com/llms.txt
created: '2026-03-23'
description: Arch Coal (now Arch Resources) is a Fortune 500 producer and marketer of metallurgical and thermal coal from mines in the United States, supplying steel manufacturers, electric utilities, and industrial customers worldwide.
examples:
- key_count: 6
  name: Arch Coal Investor Relations Api Earnings Report Example
  slug: arch-coal-investor-relations-api-earnings-report-example
- key_count: 2
  name: Arch Coal Investor Relations Api Error Response Example
  slug: arch-coal-investor-relations-api-error-response-example
- key_count: 4
  name: Arch Coal Investor Relations Api Filing Example
  slug: arch-coal-investor-relations-api-filing-example
- key_count: 2
  name: Arch Coal Investor Relations Api Filing List Example
  slug: arch-coal-investor-relations-api-filing-list-example
- key_count: 6
  name: Arch Coal Investor Relations Api Production Report Example
  slug: arch-coal-investor-relations-api-production-report-example
features:
- description: High-quality metallurgical coal for steelmaking from mines in West Virginia and Virginia.
  name: Metallurgical Coal
- description: Thermal coal for electricity generation from mines in Wyoming's Powder River Basin.
  name: Thermal Coal
- description: Publicly reported mine safety and environmental performance metrics.
  name: Safety Performance Data
- description: Quarterly coal production and sales volume reporting for investors and analysts.
  name: Production Reporting
- description: Annual reports, 10-K, 10-Q, and 8-K filings available through SEC EDGAR.
  name: SEC Filings
finops:
- name: Arch Coal Finops
  service_category: Industrial / Mining
  slug: arch-coal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arch-coal.png
integrations:
- description: All SEC filings available through the EDGAR electronic filing system at sec.gov.
  name: SEC EDGAR
- description: Financial data integrated with Bloomberg terminal for market analysis.
  name: Bloomberg
- description: Production and financial data available through Refinitiv (formerly Thomson Reuters) data services.
  name: Refinitiv
json_schemas:
- name: EarningsReport
  property_count: 6
  slug: arch-coal-investor-relations-api-earnings-report
- name: ErrorResponse
  property_count: 2
  slug: arch-coal-investor-relations-api-error-response
- name: FilingList
  property_count: 2
  slug: arch-coal-investor-relations-api-filing-list
- name: Filing
  property_count: 4
  slug: arch-coal-investor-relations-api-filing
- name: ProductionReport
  property_count: 6
  slug: arch-coal-investor-relations-api-production-report
json_structures:
- name: Arch Coal Investor Relations Api Earnings Report Structure
  property_count: 6
  slug: arch-coal-investor-relations-api-earnings-report-structure
- name: Arch Coal Investor Relations Api Error Response Structure
  property_count: 2
  slug: arch-coal-investor-relations-api-error-response-structure
- name: Arch Coal Investor Relations Api Filing List Structure
  property_count: 2
  slug: arch-coal-investor-relations-api-filing-list-structure
- name: Arch Coal Investor Relations Api Filing Structure
  property_count: 4
  slug: arch-coal-investor-relations-api-filing-structure
- name: Arch Coal Investor Relations Api Production Report Structure
  property_count: 6
  slug: arch-coal-investor-relations-api-production-report-structure
jsonld:
- class_count: 5
  name: Arch Coal Investor Relations Api Context
  property_count: 18
  slug: arch-coal-investor-relations-api-context
layout: provider
modified: '2026-05-19'
name: Arch Coal
nav: Providers
network: true
overview: 'Arch Coal publishes 3 APIs on the [APIs.io](https://apis.io/) network: Filings API, Financial API, and Production API. Tagged areas include Mining, Coal, Metallurgical Coal, Thermal Coal, and Energy.


  The Arch Coal catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Arch Coal''s developer surface includes authentication, developer portal, and 6 more developer resources.'
plans:
- name: Arch Coal Plans Pricing
  plan_count: 1
  slug: arch-coal-plans-pricing
press:
- date: '2026-05-25'
  title: About Core Natural Resources
  url: https://corenaturalresources.com/about-core/
- date: '2026-05-25'
  title: Press Releases
  url: https://www.ftc.gov/news-events/news/press-releases?initialSessionID=144-1670540-8490742&page=379
- date: '2026-05-25'
  title: Arch Resources winding down massive US coal mine as ...
  url: https://www.spglobal.com/market-intelligence/en/news-insights/articles/2021/2/arch-resources-winding-down-massive-us-coal-mine-as-customer-base-dwindles-62788531
- date: '2026-05-25'
  title: Q4 2018 Arch Coal Inc Earnings Call Transcript
  url: https://www.gurufocus.com/news/2231894/q4-2018-arch-coal-inc-earnings-call-transcript?mobile=true
- date: '2026-05-25'
  title: Despite a strong quarter for its Powder River Basin ...
  url: https://www.facebook.com/cowboystatedaily/posts/despite-a-strong-quarter-for-its-powder-river-basin-operations-arch-resources-in/500718778737496/
random_paper: 7
rate_limits:
- limit_count: 1
  name: Arch Coal Rate Limits
  slug: arch-coal-rate-limits
rules:
- name: Arch Coal API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: arch-coal-jsonschema-spectral-rules
- name: Arch Coal API Rules
  rule_count: 21
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 10
  slug: arch-coal-spectral-rules
score:
  band: developing
  composite: 49.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 71.7
    developer_ergonomics: 19.6
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 21.1
  previous_composite: 49.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Arch Coal Authentication
  slug: arch-coal-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Arch Coal Domain Security
  slug: arch-coal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arch-coal
tags:
- Mining
- Coal
- Metallurgical Coal
- Thermal Coal
- Energy
- Fortune 500
use_cases:
- description: Analyze Arch Coal financial performance, production data, and market position for investment decisions.
  name: Investment Research
- description: Access environmental, safety, and governance data for ESG analysis and reporting.
  name: ESG Reporting
- description: Steel manufacturers and utilities use production data for supply chain planning and procurement.
  name: Supply Chain Planning
- description: Track coal pricing, production volumes, and export data for commodity market research.
  name: Commodity Market Analysis
website: https://www.arch-coal.com/
---
