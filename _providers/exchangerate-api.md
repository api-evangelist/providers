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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Exchangerate Api Agentic Access
  operation_count: 9
  slug: exchangerate-api-agentic-access
  summary_line: 9 operations
api_count: 7
apis:
- description: Pair conversion enriched with target currency locale, name, symbol, and flag (Business / Volume plans only).
  name: ExchangeRate-API Enriched Data API
  slug: exchangerate-api-enriched-data-api
- description: Historical exchange rates for a specific date back to 1990 (Pro / Business / Volume plans only).
  name: ExchangeRate-API Historical Rates API
  slug: exchangerate-api-historical-rates-api
- description: Standard endpoint returning latest exchange rates from a base currency to all supported currencies.
  name: ExchangeRate-API Latest Rates API
  slug: exchangerate-api-latest-rates-api
- description: Free no-key endpoint with once-daily rates and attribution requirement.
  name: ExchangeRate-API Open Access API
  slug: exchangerate-api-open-access-api
- description: Direct currency-to-currency exchange rate and optional amount conversion.
  name: ExchangeRate-API Pair Conversion API
  slug: exchangerate-api-pair-conversion-api
- description: Inspect the remaining request quota for the API key.
  name: ExchangeRate-API Quota API
  slug: exchangerate-api-quota-api
- description: List of all supported ISO 4217 currency codes with their full names.
  name: ExchangeRate-API Supported Codes API
  slug: exchangerate-api-supported-codes-api
arazzos:
- description: Discover supported currencies, pull latest rates, then convert a specific pair.
  name: ExchangeRate-API Codes to Conversion
  slug: exchangerate-api-codes-to-conversion-workflow
- description: Build a display-ready conversion with currency name, symbol, and flag.
  name: ExchangeRate-API Enriched Pair Display
  slug: exchangerate-api-enriched-pair-display-workflow
- description: Convert an amount as it would have valued on a specific past date.
  name: ExchangeRate-API Historical Amount Conversion
  slug: exchangerate-api-historical-amount-conversion-workflow
- description: Compare a base currency's latest rates against its rates on a past date.
  name: ExchangeRate-API Latest vs Historical
  slug: exchangerate-api-latest-vs-historical-workflow
- description: Validate currencies against supported codes, then convert a specific amount.
  name: ExchangeRate-API Pair Amount Conversion
  slug: exchangerate-api-pair-amount-conversion-workflow
- description: Check remaining quota, then use the keyed endpoint or fall back to open access.
  name: ExchangeRate-API Quota Guarded Rates
  slug: exchangerate-api-quota-guarded-rates-workflow
artifact_total: 75
collections:
- collection_type: postman
  name: ExchangeRate-API
  slug: postman-exchangerate-api
- collection_type: open
  name: ExchangeRate-API
  slug: open-exchangerate-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/exchangerate-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exchangerate-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/exchangerate-api-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/exchangerate-api/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exchangerate-api-codes-to-conversion-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exchangerate-api-enriched-pair-display-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exchangerate-api-historical-amount-conversion-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exchangerate-api-latest-vs-historical-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exchangerate-api-pair-amount-conversion-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exchangerate-api-quota-guarded-rates-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.exchangerate-api.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.exchangerate-api.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://www.exchangerate-api.com/docs/overview
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/exchangerate-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/exchangerate-api-error-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/exchangerate-api-error-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/exchangerate-api-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/exchangerate-api-error-example.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/exchangerate-api-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/exchangerate-api-rules.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/exchangerate-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/exchangerate-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/exchangerate-api-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: https://www.exchangerate-api.com/docs/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.exchangerate-api.com/#pricing
- group: start
  title: ''
  type: Signup
  url: https://app.exchangerate-api.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.exchangerate-api.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.exchangerate-api.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exchangerate-api.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.exchangerate-api.com/contact
- group: operate
  title: ''
  type: Contact
  url: https://www.exchangerate-api.com/contact
- group: build
  title: Python Documentation
  type: SDKs
  url: https://www.exchangerate-api.com/docs/python-currency-api
- group: build
  title: Node.js Community SDK
  type: SDKs
  url: https://github.com/EloquentStudio/exchangerate-api-node
- group: agent
  title: Community ExchangeRate MCP Server
  type: MCPServer
  url: https://lobehub.com/mcp/mazezen-mcp-exchange-rate
created: '2026-05-28'
description: ExchangeRate-API is a currency exchange rates API providing authoritative daily and intraday foreign exchange rates for 161 currencies. The v6 surface includes Latest, Pair, Enriched, Historical, Supported Codes, and Quota endpoints, plus a no-API-key Open Access endpoint at open.er-api.com that requires attribution.
examples:
- key_count: 4
  name: Exchangerate Api Error Example
  slug: exchangerate-api-error-example
- key_count: 2
  name: Exchangerate Api Get Enriched Pair Example
  slug: exchangerate-api-get-enriched-pair-example
- key_count: 2
  name: Exchangerate Api Get Historical Rates Example
  slug: exchangerate-api-get-historical-rates-example
- key_count: 2
  name: Exchangerate Api Get Historical Rates With Amount Example
  slug: exchangerate-api-get-historical-rates-with-amount-example
- key_count: 2
  name: Exchangerate Api Get Latest Rates Example
  slug: exchangerate-api-get-latest-rates-example
- key_count: 2
  name: Exchangerate Api Get Open Access Latest Example
  slug: exchangerate-api-get-open-access-latest-example
- key_count: 2
  name: Exchangerate Api Get Pair Conversion Example
  slug: exchangerate-api-get-pair-conversion-example
- key_count: 2
  name: Exchangerate Api Get Pair Conversion With Amount Example
  slug: exchangerate-api-get-pair-conversion-with-amount-example
- key_count: 2
  name: Exchangerate Api Get Quota Example
  slug: exchangerate-api-get-quota-example
- key_count: 2
  name: Exchangerate Api Get Supported Codes Example
  slug: exchangerate-api-get-supported-codes-example
features:
- description: Get latest exchange rates from a base currency to all 161 supported currencies.
  name: Latest Rates
- description: Direct currency-to-currency rate lookup with optional amount conversion.
  name: Pair Conversion
- description: Pair conversion plus target currency locale, name, symbol, and flag.
  name: Enriched Data
- description: Exchange rates for any date back to 1990 (with full coverage from 2021).
  name: Historical Rates
- description: Full ISO 4217 currency code listing with names.
  name: Supported Codes
- description: No-API-key endpoint at open.er-api.com with once-daily updates and attribution.
  name: Open Access Endpoint
- description: Pingdom-measured uptime exceeded 99.99% during 2024.
  name: 99.99% Uptime SLA
- description: Comprehensive coverage of world fiat currencies.
  name: 161 Supported Currencies
finops:
- name: Exchangerate Api Finops
  service_category: Financial Data
  slug: exchangerate-api-finops
image: https://www.exchangerate-api.com/img/logo.svg
integrations:
- description: Use ExchangeRate-API from Python applications via the documented HTTP API.
  name: Python
- description: Community Node.js SDK published by EloquentStudio for first-class JavaScript integration.
  name: Node.js
- description: Documented sample code for major server-side languages on the ExchangeRate-API docs site.
  name: PHP / Java / Ruby / C# / Perl / Objective-C
- description: Pull rates into Google Sheets and Excel via HTTP request functions.
  name: Spreadsheets
- description: Community-built Model Context Protocol servers expose ExchangeRate-API as a tool for LLM agents such as Claude.
  name: MCP Servers
json_schemas:
- name: EnrichedPairResponse
  property_count: 11
  slug: exchangerate-api-enriched
- name: ErrorResponse
  property_count: 4
  slug: exchangerate-api-error
- name: HistoricalRatesResponse
  property_count: 10
  slug: exchangerate-api-historical
- name: LatestRatesResponse
  property_count: 9
  slug: exchangerate-api-latest-rates
- name: OpenAccessResponse
  property_count: 11
  slug: exchangerate-api-open-access
- name: PairResponse
  property_count: 11
  slug: exchangerate-api-pair
- name: QuotaResponse
  property_count: 6
  slug: exchangerate-api-quota
- name: SupportedCodesResponse
  property_count: 4
  slug: exchangerate-api-supported-codes
json_structures:
- name: Exchangerate Api Enriched Structure
  property_count: 11
  slug: exchangerate-api-enriched-structure
- name: Exchangerate Api Error Structure
  property_count: 4
  slug: exchangerate-api-error-structure
- name: Exchangerate Api Historical Structure
  property_count: 10
  slug: exchangerate-api-historical-structure
- name: Exchangerate Api Latest Rates Structure
  property_count: 9
  slug: exchangerate-api-latest-rates-structure
- name: Exchangerate Api Open Access Structure
  property_count: 11
  slug: exchangerate-api-open-access-structure
- name: Exchangerate Api Pair Structure
  property_count: 11
  slug: exchangerate-api-pair-structure
- name: Exchangerate Api Quota Structure
  property_count: 6
  slug: exchangerate-api-quota-structure
- name: Exchangerate Api Supported Codes Structure
  property_count: 4
  slug: exchangerate-api-supported-codes-structure
jsonld:
- class_count: 0
  name: Exchangerate Api Context
  property_count: 32
  slug: exchangerate-api-context
layout: provider
mcp_servers:
- description: ''
  name: Community ExchangeRate MCP Server
  slug: community-exchangerate-mcp-server
modified: '2026-05-29'
name: ExchangeRate-API
nav: Providers
network: true
overview: 'ExchangeRate-API publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Enriched Data API, Historical Rates API, Latest Rates API, and 4 more. Tagged areas include Currency Exchange, Foreign Exchange, Financial Data, Forex, and Currency Conversion.


  The ExchangeRate-API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ExchangeRate-API''s developer surface includes authentication, documentation, API reference, code examples, pricing, signup flow, support, and 27 more developer resources.'
plans:
- name: Exchangerate Api Plans Pricing
  plan_count: 5
  slug: exchangerate-api-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Exchangerate Api Rate Limits
  slug: exchangerate-api-rate-limits
rules:
- name: ExchangeRate-API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: exchangerate-api-jsonschema-spectral-rules
- name: ExchangeRate-API API Rules
  rule_count: 8
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 1
  slug: exchangerate-api-rules
score:
  band: exemplar
  composite: 66.4
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 79.1
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 66.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exchangerate-api/refs/heads/main/screenshots/exchangerate-api-2026-06-20T180923.png
security:
- kind: authentication
  name: Exchangerate Api Authentication
  slug: exchangerate-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Exchangerate Api Domain Security
  slug: exchangerate-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: exchangerate-api
solutions:
- description: Self-serve evaluation with 1,500 requests/month and daily updates.
  name: Free Tier
- description: Production-grade tier with 30,000 requests/month and hourly updates.
  name: Pro Tier
- description: Higher-volume tier with 125,000 requests/month, 5-minute updates, and Enriched Data access.
  name: Business Tier
- description: Highest-volume tier for high-traffic applications and aggregators.
  name: Volume Tier
tags:
- Currency Exchange
- Foreign Exchange
- Financial Data
- Forex
- Currency Conversion
- Public APIs
use_cases:
- description: Show product prices in the visitor's local currency on storefronts and checkout pages.
  name: E-commerce Multi-currency Display
- description: Convert invoice totals to the customer's billing currency at the time of invoice issuance.
  name: Cross-border Invoicing
- description: Translate revenues, costs, and balances across currencies for consolidated reporting.
  name: Financial Reporting
- description: Show flights, hotels, and packages in the user's home currency.
  name: Travel & Booking Platforms
- description: Convert account balances and transactions across currencies for travel and expense tracking.
  name: Personal Finance Apps
- description: Expose currency conversion to AI agents via MCP servers and tool-use frameworks.
  name: AI / LLM Agent Currency Tools
- description: Use 30+ years of historical rates to backtest trading strategies and FX exposure scenarios.
  name: Historical Backtesting
website: https://www.exchangerate-api.com
---
