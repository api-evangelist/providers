---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: 'JSON over HTTPS Web API for the NSE Request-for-Quote (RFQ) platform for corporate bonds and debt securities. Documented in the "RFQ - Protocol for Web API" PDF published on the NSE trading protocols '
  name: NSE RFQ Web API
  slug: nse-rfq-web-api
- description: JSON over HTTPS Web API for CBRICS (Corporate Bond Reporting and Integrated Clearing System), NSE's reporting and settlement platform for corporate bond trades. Documented in the "WEB CBRICS PROTOCOL"
  name: NSE CBRICS Web API
  slug: nse-cbrics-web-api
- description: JSON over HTTPS Web API for the NSE Offer-For-Sale platform, used by members to place, modify, cancel and query OFS orders and to stream market messages. Bearer access-token authentication with a refr
  name: NSE Offer For Sale (OFS) Web API
  slug: nse-offer-for-sale-ofs-web-api
artifact_total: 6
asyncapis:
- description: ''
  name: National Stock Exchange Of India Webhooks
  slug: national-stock-exchange-of-india-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-stock-exchange-of-india-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nseindia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nseindia.com/static/trade/platform-services-neat-trading-system-protocols
- group: docs
  title: ''
  type: APIReference
  url: https://www.nseindia.com/static/trade/platform-services-neat-trading-system-protocols
- group: operate
  title: ''
  type: Support
  url: https://www.nseindia.com/static/list-contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nseindia.com/static/nse-data-and-analytics/data-information-vending
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nseindia.com/static/nse-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nseindia.com/static/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.nseindia.com/resources/exchange-communication-circulars
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/national-stock-exchange-of-india-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/national-stock-exchange-of-india-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/national-stock-exchange-of-india-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/national-stock-exchange-of-india-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/national-stock-exchange-of-india-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/national-stock-exchange-of-india-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/national-stock-exchange-of-india-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/national-stock-exchange-of-india-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/national-stock-exchange-of-india-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/national-stock-exchange-of-india-llms.txt
created: '2026-08-04'
description: 'National Stock Exchange of India Ltd (NSE) is India''s largest stock exchange, operating the Capital Market, Futures & Options, Currency Derivatives, Commodity Derivatives, Debt and Electronic Gold Receipts segments, together with NSE Clearing, NSE Indices and NSE Data & Analytics Ltd (formerly DotEx International). NSE exposes its trading and post-trade systems to members and empanelled vendors through a published protocol surface rather than a public developer portal: binary Non-NEAT Front-End (NNF) and multicast tick-by-tick (MTBT) trading protocols, a Drop Copy facility, an Extranet API, a FIX 5.0 (SP2) interface for the RFQ platform, and JSON/HTTPS Web APIs for the RFQ, CBRICS bond, e-IPO/ASBA, Offer-For-Sale and MFSS platforms. Every one of those interfaces is documented only as a PDF or ZIP protocol document — NSE publishes no OpenAPI, AsyncAPI, SDK, Postman collection or machine-readable contract of any kind. Market data itself is vended commercially by NSE Data & Analytics
  under a subscription and data-vending agreement.'
image: https://www.nseindia.com/assets/images/NSE_Logo.svg
layout: provider
modified: '2026-08-04'
name: National Stock Exchange of India
nav: Providers
network: true
overview: 'National Stock Exchange of India publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Stock Exchange, Capital Markets, Market Data, and Trading.


  The National Stock Exchange of India catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  National Stock Exchange of India''s developer surface includes documentation, API reference, support, pricing, changelog, authentication, sandbox, and 12 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 29.8
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 31.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 35.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-stock-exchange-of-india/refs/heads/main/screenshots/national-stock-exchange-of-india-2026-08-07T184648.png
security:
- kind: authentication
  name: National Stock Exchange Of India Authentication
  slug: national-stock-exchange-of-india-authentication
  summary_line: http/apiKey/mutualTLS · 5 schemes
- kind: domain-security
  name: National Stock Exchange Of India Domain Security
  slug: national-stock-exchange-of-india-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-stock-exchange-of-india
tags:
- Company
- Stock Exchange
- Capital Markets
- Market Data
- Trading
- Financial-Services
- Securities
- India
- FIX Protocol
- Bonds
website: https://www.nseindia.com/
---
