---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Stockdata Agentic Access
  operation_count: 16
  slug: stockdata-agentic-access
  summary_line: 16 operations
api_count: 3
apis:
- description: Entity search and metadata
  name: StockData Entities API
  slug: stockdata-entities-api
- description: Global financial news with sentiment analysis
  name: StockData News API
  slug: stockdata-news-api
- description: Real-time and historical stock market price data
  name: StockData Stock Data API
  slug: stockdata-stock-data-api
artifact_total: 22
collections:
- collection_type: postman
  name: StockData Entities API
  slug: postman-stockdata-entities-api
- collection_type: postman
  name: StockData Entities News API
  slug: postman-stockdata-news-api
- collection_type: postman
  name: StockData Entities Stock Data API
  slug: postman-stockdata-stock-data-api
- collection_type: open
  name: StockData API
  slug: open-stockdata
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/stockdata/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stockdata-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stockdata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stockdata-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stockdata-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stockdata-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/stockdata-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stockdata-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stockdata-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stockdata-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stockdata-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/stockdata-vocabulary.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stockdata-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stockdata-plans-pricing.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/stockdata-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stockdata-quote-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stockdata-news-article-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/stockdata-quote-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/stockdata-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/stockdata-get-stock-quote-example.json
- group: build
  title: ''
  type: Examples
  url: examples/stockdata-get-financial-news-example.json
- group: build
  title: ''
  type: PostmanCollection
  url: collections/stockdata.postman_collection.json
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stockdata-org
- group: start
  title: ''
  type: Portal
  url: https://www.stockdata.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.stockdata.org/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.stockdata.org/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.stockdata.org/documentation#introduction
- group: operate
  title: ''
  type: Support
  url: https://www.stockdata.org/contact
- group: start
  title: ''
  type: Signup
  url: https://www.stockdata.org/register
- group: start
  title: ''
  type: Login
  url: https://www.stockdata.org/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stockdata.org/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stockdata.org/privacy
- group: company
  title: ''
  type: Website
  url: https://www.stockdata.org/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stockdata.org/pricing
created: '2025-02-24'
description: StockData.org provides real-time, intraday, and historical stock, forex, and cryptocurrency data along with global financial news and sentiment analysis. The REST API delivers market data for US-listed stocks including OHLCV data, splits, dividends, and entity-level news sentiment from 5,000+ sources in 30+ languages.
examples:
- key_count: 2
  name: Stockdata Get Financial News Example
  slug: stockdata-get-financial-news-example
- key_count: 2
  name: Stockdata Get Stock Quote Example
  slug: stockdata-get-stock-quote-example
finops:
- name: Stockdata Finops
  service_category: API
  slug: stockdata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stockdata.png
json_schemas:
- name: StockData News Article
  property_count: 12
  slug: stockdata-news-article
- name: StockData Quote
  property_count: 16
  slug: stockdata-quote
json_structures:
- name: Stockdata Quote Structure
  property_count: 0
  slug: stockdata-quote-structure
jsonld:
- class_count: 39
  name: Stockdata Context
  property_count: 0
  slug: stockdata-context
layout: provider
mcp_servers:
- description: ''
  name: stockdata-mcp.yml
  slug: stockdata-mcpyml
modified: '2026-07-22'
name: StockData
nav: Providers
network: true
overview: 'StockData publishes 3 APIs on the [APIs.io](https://apis.io/) network: Entities API, News API, and Stock Data API. Tagged areas include Finance, Financial Data, Stock Market, Market Data, and News.


  The StockData catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  StockData''s developer surface includes authentication, code examples, developer portal, documentation, API reference, getting-started guide, support, and 28 more developer resources.'
plans:
- name: Stockdata Plans Pricing
  plan_count: 5
  slug: stockdata-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 6
  name: Stockdata Rate Limits
  slug: stockdata-rate-limits
rules:
- name: StockData API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stockdata-jsonschema-spectral-rules
- name: StockData API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 3
  slug: stockdata-rules
score:
  band: strong
  composite: 65.7
  delta: -3.4
  facets:
    commercial_clarity: 84.2
    contract_quality: 66.9
    developer_ergonomics: 58.2
    discoverability: 92.6
    governance: 80.2
    operational_transparency: 31.6
  previous_composite: 69.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stockdata/refs/heads/main/screenshots/stockdata-2026-06-20T194552.png
security:
- kind: authentication
  name: Stockdata Authentication
  slug: stockdata-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Stockdata Domain Security
  slug: stockdata-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: stockdata
tags:
- Finance
- Financial Data
- Stock Market
- Market Data
- News
- Sentiment Analysis
website: https://www.stockdata.org/
---
