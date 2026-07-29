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
- acting_count: 0
  human_in_the_loop: 0
  name: Currencylayer Agentic Access
  operation_count: 6
  slug: currencylayer-agentic-access
  summary_line: 6 operations
api_count: 5
apis:
- description: Currency change (margin and percentage) analysis between two dates.
  name: Currencylayer Change API
  slug: currencylayer-change-api
- description: On-demand currency amount conversion.
  name: Currencylayer Conversion API
  slug: currencylayer-conversion-api
- description: Real-time and historical foreign exchange rate operations.
  name: Currencylayer Rates API
  slug: currencylayer-rates-api
- description: Discovery of supported currency symbols.
  name: Currencylayer Symbols API
  slug: currencylayer-symbols-api
- description: Daily historical rates between two dates.
  name: Currencylayer Time Frame API
  slug: currencylayer-time-frame-api
artifact_total: 66
collections:
- collection_type: postman
  name: Currencylayer Change API
  slug: postman-currencylayer-change-api
- collection_type: postman
  name: Currencylayer Change Conversion API
  slug: postman-currencylayer-conversion-api
- collection_type: postman
  name: Currencylayer Change Rates API
  slug: postman-currencylayer-rates-api
- collection_type: postman
  name: Currencylayer Change Symbols API
  slug: postman-currencylayer-symbols-api
- collection_type: postman
  name: Currencylayer Change Time Frame API
  slug: postman-currencylayer-time-frame-api
- collection_type: open
  name: Currencylayer API
  slug: open-currencylayer
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/currencylayer/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/currencylayer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/currencylayer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/currencylayer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://currencylayer.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apilayer.com/currencylayer/docs/api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://apilayer.com/marketplace/currency_data-api
- group: commercial
  title: ''
  type: Pricing
  url: https://currencylayer.com/product
- group: start
  title: ''
  type: Signup
  url: https://apilayer.com/signup
- group: start
  title: ''
  type: Login
  url: https://apilayer.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://currencylayer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://currencylayer.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://currencylayer.com/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.apilayer.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apilayer
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apilayer/currencylayer-API
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: rules/currencylayer-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/currencylayer-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/currencylayer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/currencylayer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/currencylayer-finops.yml
- group: build
  title: APILayer MCP Server Pattern (currencylayer example)
  type: Tools
  url: https://blog.apilayer.com/how-to-turn-any-rest-api-into-an-mcp-server-for-claude-complete-2026-pillar-guide/
created: '2026-05-28'
description: Currencylayer is a real-time and historical foreign exchange rate JSON API delivering bank-grade exchange rate data for 168 world currencies and precious metals, sourced from 15+ commercial-grade providers. The service is delivered through the APILayer marketplace under a freemium subscription model with refresh cadence ranging from hourly on Free up to 60 seconds on Enterprise tiers.
examples:
- key_count: 2
  name: Currencylayer Convertcurrency Example
  slug: currencylayer-convertcurrency-example
- key_count: 2
  name: Currencylayer Getchange Example
  slug: currencylayer-getchange-example
- key_count: 2
  name: Currencylayer Gethistorical Example
  slug: currencylayer-gethistorical-example
- key_count: 2
  name: Currencylayer Getlive Example
  slug: currencylayer-getlive-example
- key_count: 2
  name: Currencylayer Gettimeframe Example
  slug: currencylayer-gettimeframe-example
- key_count: 2
  name: Currencylayer Listcurrencies Example
  slug: currencylayer-listcurrencies-example
features:
- description: Coverage of fiat currencies plus precious metals, sourced from 15+ commercial-grade providers.
  name: 168 World Currencies
- description: Latest rates with refresh cadence ranging from hourly (Free) to 60 seconds (Enterprise and above).
  name: Real-Time Exchange Rates
- description: End-of-day rates for any day since 1999, available on every plan including Free.
  name: Historical Exchange Rates
- description: On-demand conversion between any two currencies at real-time or historical rates.
  name: Currency Conversion Endpoint
- description: Daily rates between two arbitrary dates (max 365 days) for trend analysis.
  name: Time-Frame Endpoint
- description: Start rate, end rate, absolute change, and percentage change for a chosen window.
  name: Change Endpoint
- description: SSL-secured transport on Basic plan and above; Free is HTTP only.
  name: HTTPS Encryption
- description: Choose any of the 168 codes as the base currency on Basic plan and above.
  name: Source Currency Switching
- description: One APILayer `apikey` works across Currencylayer and other APILayer marketplace APIs.
  name: APILayer Unified Auth
- description: Aggregated from 15+ commercial-grade providers, suitable for finance and treasury workloads.
  name: Bank-Grade Data Sourcing
finops:
- name: Currencylayer Finops
  service_category: ''
  slug: currencylayer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/currencylayer.png
integrations:
- description: Currencylayer is distributed via the APILayer hub; signup, billing, and key management share the marketplace.
  name: APILayer Marketplace
- description: Sister APILayer FX product with overlapping surface; commonly used interchangeably or for redundancy.
  name: Fixer
- description: Cryptocurrency exchange rate API on the same APILayer platform.
  name: Coinlayer
- description: Competing FX API that consumers benchmark Currencylayer against.
  name: Open Exchange Rates
- description: Free/community FX alternatives often evaluated alongside Currencylayer.
  name: Frankfurter / ExchangeRate.host
- description: Server- and browser-side libraries paired with Currencylayer for conversion math.
  name: Money / money.js
json_schemas:
- name: Currencylayer Change Response
  property_count: 8
  slug: currencylayer-change
- name: Currencylayer Convert Response
  property_count: 8
  slug: currencylayer-convert
- name: Currencylayer Currencies Response
  property_count: 4
  slug: currencylayer-currencies
- name: Currencylayer Error Response
  property_count: 2
  slug: currencylayer-error
- name: Currencylayer Quotes Response
  property_count: 8
  slug: currencylayer-quotes
- name: Currencylayer Time-Frame Response
  property_count: 8
  slug: currencylayer-timeframe
json_structures:
- name: Currencylayer Change Structure
  property_count: 6
  slug: currencylayer-change-structure
- name: Currencylayer Convert Structure
  property_count: 6
  slug: currencylayer-convert-structure
- name: Currencylayer Currencies Structure
  property_count: 2
  slug: currencylayer-currencies-structure
- name: Currencylayer Quotes Structure
  property_count: 6
  slug: currencylayer-quotes-structure
- name: Currencylayer Timeframe Structure
  property_count: 6
  slug: currencylayer-timeframe-structure
jsonld:
- class_count: 8
  name: Currencylayer Context
  property_count: 21
  slug: currencylayer-context
layout: provider
modified: '2026-05-29'
name: Currencylayer
nav: Providers
network: true
overview: 'Currencylayer publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Change API, Conversion API, Rates API, and 2 more. Tagged areas include Currency Exchange, Foreign Exchange, FX, Forex, and Conversion.


  The Currencylayer catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Currencylayer''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, engineering blog, and 16 more developer resources.'
plans:
- name: Currencylayer Plans Pricing
  plan_count: 6
  slug: currencylayer-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 0
  name: Currencylayer Rate Limits
  slug: currencylayer-rate-limits
rules:
- name: Currencylayer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: currencylayer-jsonschema-spectral-rules
- name: Currencylayer API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 8
  slug: currencylayer-rules
score:
  band: strong
  composite: 60.8
  delta: -3.8
  facets:
    commercial_clarity: 84.2
    contract_quality: 78.0
    developer_ergonomics: 37.0
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 64.6
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
screenshot: https://raw.githubusercontent.com/api-evangelist/currencylayer/refs/heads/main/screenshots/currencylayer-2026-06-20T175338.png
security:
- kind: authentication
  name: Currencylayer Authentication
  slug: currencylayer-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Currencylayer Domain Security
  slug: currencylayer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: currencylayer
solutions:
- description: 100 requests/month, hourly refresh, USD base only, HTTP only. Best for prototyping.
  name: Free Plan
- description: 10,000 requests/month at $14.99/mo, HTTPS, source-currency switching, /convert endpoint.
  name: Basic Plan
- description: 100,000 requests/month at $39.99/mo, 10-minute refresh, /convert endpoint.
  name: Professional Plan
- description: 100,000 requests/month at $59.99/mo, 60-second refresh, /timeframe endpoint.
  name: Enterprise Plan
- description: 500,000 requests/month at $99.99/mo, 60-second refresh, /timeframe and /change endpoints.
  name: Enterprise Plus Plan
- description: Volume-based pricing, 60-second refresh, dedicated account team and priority support.
  name: Custom Plan
tags:
- Currency Exchange
- Foreign Exchange
- FX
- Forex
- Conversion
- Historical Rates
- Time Frame
- Change Report
- Precious Metals
- APILayer
- Public APIs
use_cases:
- description: Convert prices into the shopper's local currency at checkout using /convert and /live.
  name: E-Commerce Multi-Currency Pricing
- description: Daily mark-to-market of multi-currency balances using /timeframe and /change.
  name: Treasury and Cash Reporting
- description: Power in-app FX widgets, traveler wallets, and remittance quotes with /live.
  name: Travel and Fintech Apps
- description: Look up the official end-of-day rate for any historical transaction with /historical.
  name: Accounting and Ledger Reconciliation
- description: Pull windowed rate history with /timeframe to feed quant or BI models.
  name: Backtesting and Analytics
- description: Reference an immutable end-of-day rate when auditing cross-border payments.
  name: Compliance and Audit Trails
- description: Expose live and historical rates to LLM agents via APILayer's MCP server pattern.
  name: AI Agents and MCP Tools
website: https://currencylayer.com
---
