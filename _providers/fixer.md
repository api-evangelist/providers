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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fixer Agentic Access
  operation_count: 6
  slug: fixer-agentic-access
  summary_line: 6 operations
api_count: 5
apis:
- description: On-demand currency amount conversion.
  name: Fixer Conversion API
  slug: fixer-conversion-api
- description: Currency fluctuation analysis between two dates.
  name: Fixer Fluctuation API
  slug: fixer-fluctuation-api
- description: Real-time and historical foreign exchange rate operations.
  name: Fixer Rates API
  slug: fixer-rates-api
- description: Discovery of supported currency symbols.
  name: Fixer Symbols API
  slug: fixer-symbols-api
- description: Daily historical rates between two dates.
  name: Fixer Time Series API
  slug: fixer-time-series-api
artifact_total: 58
collections:
- collection_type: open
  name: Fixer API
  slug: open-fixer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fixer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fixer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fixer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://fixer.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apilayer.com/fixer/docs/api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://apilayer.com/marketplace/fixer-api
- group: commercial
  title: ''
  type: Pricing
  url: https://fixer.io/product
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
  url: https://fixer.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fixer.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://fixer.io/contact
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
  url: https://github.com/apilayer/fixer
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: rules/fixer-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/fixer-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fixer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fixer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fixer-finops.yml
created: '2026-05-28'
description: Fixer is a lightweight JSON API for real-time and historical foreign exchange rates and currency conversion. Built on top of European Central Bank reference rates and 15+ additional data sources, Fixer supports 170+ world currencies and is delivered through the APILayer marketplace under a freemium subscription model.
examples:
- key_count: 2
  name: Fixer Convertcurrency Example
  slug: fixer-convertcurrency-example
- key_count: 2
  name: Fixer Getfluctuation Example
  slug: fixer-getfluctuation-example
- key_count: 2
  name: Fixer Gethistorical Example
  slug: fixer-gethistorical-example
- key_count: 2
  name: Fixer Getlatest Example
  slug: fixer-getlatest-example
- key_count: 2
  name: Fixer Getsymbols Example
  slug: fixer-getsymbols-example
- key_count: 2
  name: Fixer Gettimeseries Example
  slug: fixer-gettimeseries-example
features:
- description: Coverage of fiat currencies, sourced from the European Central Bank and 15+ additional providers.
  name: 170+ World Currencies
- description: Latest rates with refresh cadence ranging from hourly (Free) to 60 seconds (Professional Plus, Enterprise).
  name: Real-Time Exchange Rates
- description: End-of-day rates for any working day since 1999-01-04, available on every plan including Free.
  name: Historical Exchange Rates
- description: On-demand conversion between any two currencies at real-time or historical rates.
  name: Currency Conversion Endpoint
- description: Daily rates between two arbitrary dates (max 365 days) for trend analysis.
  name: Time Series Endpoint
- description: Start rate, end rate, absolute change, and percentage change for a chosen window.
  name: Fluctuation Endpoint
- description: SSL-secured transport on Basic plan and above; Free is HTTP only.
  name: HTTPS Encryption
- description: Choose any of the 170+ symbols as the base currency on Basic plan and above.
  name: Source Currency Switching
- description: One APILayer `apikey` works across Fixer and other APILayer marketplace APIs.
  name: APILayer Unified Auth
finops:
- name: Fixer Finops
  service_category: ''
  slug: fixer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fixer.png
integrations:
- description: Fixer is distributed via the APILayer hub; signup, billing, and key management share the marketplace.
  name: APILayer Marketplace
- description: Primary upstream data source for daily reference exchange rates.
  name: European Central Bank
- description: Client-side JavaScript library historically paired with Fixer for browser-side conversion.
  name: money.js
- description: Sister APILayer product with similar FX surface; often used interchangeably or for redundancy.
  name: Currencylayer
- description: Cryptocurrency exchange rate API on the same APILayer platform.
  name: Coinlayer
- description: Competing FX APIs that consumers benchmark Fixer against.
  name: Currencyfreaks / Open Exchange Rates
json_schemas:
- name: Fixer Convert Response
  property_count: 6
  slug: fixer-convert
- name: Fixer Error Response
  property_count: 2
  slug: fixer-error
- name: Fixer Fluctuation Response
  property_count: 6
  slug: fixer-fluctuation
- name: Fixer Rates Response
  property_count: 6
  slug: fixer-rates
- name: Fixer Symbols Response
  property_count: 2
  slug: fixer-symbols
- name: Fixer Time Series Response
  property_count: 6
  slug: fixer-timeseries
json_structures:
- name: Fixer Convert Structure
  property_count: 6
  slug: fixer-convert-structure
- name: Fixer Fluctuation Structure
  property_count: 6
  slug: fixer-fluctuation-structure
- name: Fixer Rates Structure
  property_count: 6
  slug: fixer-rates-structure
- name: Fixer Symbols Structure
  property_count: 2
  slug: fixer-symbols-structure
- name: Fixer Timeseries Structure
  property_count: 6
  slug: fixer-timeseries-structure
jsonld:
- class_count: 9
  name: Fixer Context
  property_count: 20
  slug: fixer-context
layout: provider
modified: '2026-05-29'
name: Fixer
nav: Providers
network: true
overview: 'Fixer publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Conversion API, Fluctuation API, Rates API, and 2 more. Tagged areas include Currency Exchange, Foreign Exchange, FX, Forex, and ECB.


  The Fixer catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Fixer''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, engineering blog, and 14 more developer resources.'
plans:
- name: Fixer Plans Pricing
  plan_count: 5
  slug: fixer-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 0
  name: Fixer Rate Limits
  slug: fixer-rate-limits
rules:
- name: Fixer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fixer-jsonschema-spectral-rules
- name: Fixer API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 8
  slug: fixer-rules
score:
  band: strong
  composite: 64.6
  delta: 5.5
  facets:
    commercial_clarity: 84.2
    contract_quality: 80.5
    developer_ergonomics: 32.6
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 5.3
  previous_composite: 59.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/fixer/refs/heads/main/screenshots/fixer-2026-06-20T181258.png
security:
- kind: authentication
  name: Fixer Authentication
  slug: fixer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fixer Domain Security
  slug: fixer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fixer
solutions:
- description: 100 requests/month, hourly refresh, EUR base only, HTTP only. Best for prototyping.
  name: Free Plan
- description: 10,000 requests/month at $14.99/mo, HTTPS, source currency switching, /convert endpoint.
  name: Basic Plan
- description: 100,000 requests/month at $59.99/mo, 10-minute refresh, /timeseries endpoint.
  name: Professional Plan
- description: 500,000 requests/month at $99.99/mo, 60-second refresh, /fluctuation endpoint.
  name: Professional Plus Plan
- description: Custom volume, 60-second refresh, dedicated account team and priority support.
  name: Enterprise Plan
tags:
- Currency Exchange
- Foreign Exchange
- FX
- Forex
- ECB
- Conversion
- Historical Rates
- Time Series
- Fluctuation
- APILayer
- Public APIs
use_cases:
- description: Convert prices into the shopper's local currency at checkout using /convert.
  name: E-Commerce Multi-Currency Pricing
- description: Daily mark-to-market of multi-currency balances using /timeseries and /fluctuation.
  name: Treasury and Cash Reporting
- description: Power in-app FX widgets, traveler wallets, and remittance quotes with /latest.
  name: Travel and Fintech Apps
- description: Look up the official end-of-day rate for any historical transaction with /{date}.
  name: Accounting and Ledger Reconciliation
- description: Pull windowed rate history with /timeseries to feed quant or BI models.
  name: Backtesting and Analytics
- description: Reference an immutable ECB-sourced rate when auditing cross-border payments.
  name: Compliance and Audit Trails
website: https://fixer.io
---
