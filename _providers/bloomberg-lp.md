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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bloomberg Lp Agentic Access
  operation_count: 4
  slug: bloomberg-lp-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 9
apis:
- description: 'BLPAPI is Bloomberg''s core programming interface for the Bloomberg Terminal Desktop API, Server API (SAPI), B-PIPE, and Platform products. It exposes a unified asynchronous session/event/subscription '
  name: Bloomberg BLPAPI (Desktop API)
  slug: blpapi
- description: Server-side variant of BLPAPI that lets a single Bloomberg Terminal user serve real-time market data, historical data, reference data, and calculation-engine output to multiple in-house applications a
  name: Bloomberg Server API (SAPI)
  slug: server-api
- description: Bloomberg's flagship enterprise market data feed, delivering normalized, consolidated, real-time and reference data across all asset classes with Bloomberg's entitlement and identifier infrastructure.
  name: Bloomberg B-PIPE
  slug: b-pipe
- description: Bulk reference, pricing, regulatory, and alternative-data delivery service covering over 50 million securities and 30,000+ fields. Accessed via REST API (HAPI / Bloomberg Enterprise Access Point), SFT
  name: Bloomberg Data License (DL / BEAP)
  slug: data-license
- description: 'Bloomberg''s flagship subscription product — a desktop application delivering real-time market data, news, analytics, trading, messaging, and research to financial professionals globally. The Terminal '
  name: Bloomberg Terminal
  slug: terminal
- description: Filtered, paginated search across the FIGI universe.
  name: Bloomberg L.P. Filter API
  slug: bloomberg-lp-filter-api
- description: Map third-party identifiers to FIGIs.
  name: Bloomberg L.P. Mapping API
  slug: bloomberg-lp-mapping-api
- description: Enumerated values for request and response fields.
  name: Bloomberg L.P. Reference API
  slug: bloomberg-lp-reference-api
- description: Keyword search across the FIGI universe.
  name: Bloomberg L.P. Search API
  slug: bloomberg-lp-search-api
artifact_total: 50
collections:
- collection_type: postman
  name: OpenFIGI Filter API
  slug: postman-bloomberg-lp-filter-api
- collection_type: postman
  name: OpenFIGI Filter Mapping API
  slug: postman-bloomberg-lp-mapping-api
- collection_type: postman
  name: OpenFIGI Filter Reference API
  slug: postman-bloomberg-lp-reference-api
- collection_type: postman
  name: OpenFIGI Filter Search API
  slug: postman-bloomberg-lp-search-api
- collection_type: open
  name: OpenFIGI API
  slug: open-openfigi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bloomberg-lp/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bloomberg-lp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-lp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bloomberg-lp-authentication.yml
- group: other
  title: ''
  type: LandingPage
  url: https://www.bloomberg.com/
- group: other
  title: ''
  type: Company
  url: https://www.bloomberg.com/company/
- group: start
  title: ''
  type: ProfessionalPortal
  url: https://www.bloomberg.com/professional/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bloomberg.com/
- group: start
  title: ''
  type: OpenFIGIPortal
  url: https://www.openfigi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bloomberg.github.io/blpapi-docs/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
- group: operate
  title: ''
  type: Contact
  url: https://www.bloomberg.com/professional/contact-menu/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bloomberg.com/professional/pricing/
- group: start
  title: ''
  type: Login
  url: https://bba.bloomberg.net/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/notices/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- group: build
  title: ''
  type: OpenFIGIGitHubOrganization
  url: https://github.com/OpenFIGI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bloomberg/
- group: company
  title: ''
  type: XTwitter
  url: https://twitter.com/business
- group: company
  title: ''
  type: Blog
  url: https://www.bloomberg.com/company/stories/
- group: company
  title: ''
  type: TechBlog
  url: https://www.bloomberg.com/company/stories/category/tech-at-bloomberg/
- group: company
  title: ''
  type: News
  url: https://www.bloomberg.com/news/
- group: commercial
  title: ''
  type: Plans
  url: plans/bloomberg-lp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bloomberg-lp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bloomberg-lp-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bloomberg-lp-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/bloomberg-lp-context.jsonld
created: '2024-01-01'
description: Bloomberg L.P. is a privately held financial, software, data, and media company founded by Michael Bloomberg in 1981 and headquartered in New York City. The company is best known for the Bloomberg Terminal, which delivers real-time market data, news, analytics, and trading tools to roughly 325,000 subscribers worldwide, and for Bloomberg News, Bloomberg.com, Bloomberg Television, and Bloomberg Industry Group (formerly Bloomberg BNA). On the developer side, Bloomberg exposes the BLPAPI (Bloomberg API) family across the Desktop API, Server API, B-PIPE, and Data License products via SDKs in C++, Java, Python and .NET, and operates OpenFIGI — the free, public Financial Instrument Global Identifier (FIGI) symbology API and the most openly accessible Bloomberg API surface for the general developer audience.
examples:
- key_count: 3
  name: Openfigi Filter Request Example
  slug: openfigi-filter-request-example
- key_count: 2
  name: Openfigi Filter Response Example
  slug: openfigi-filter-response-example
- key_count: 1
  name: Openfigi Mapping Values Idtype Response Example
  slug: openfigi-mapping-values-idtype-response-example
- key_count: 3
  name: Openfigi Search Request Example
  slug: openfigi-search-request-example
- key_count: 2
  name: Openfigi Search Response Example
  slug: openfigi-search-response-example
features:
- description: OpenFIGI maps tickers, ISINs, CUSIPs, SEDOLs, and other identifiers to FIGIs at no cost, with optional API key for higher throughput.
  name: Free FIGI Symbology
- description: BLPAPI ships official SDKs in C++, Java, Python, and .NET, plus community/legacy wrappers in Node.js and Haskell.
  name: Multi-Language SDK Coverage
- description: One BLPAPI session/event/subscription model spans Desktop API, Server API, B-PIPE, and Platform.
  name: Unified Programming Model
- description: BLPAPI exposes reference data, historical data, intraday bar/tick data, and real-time market data subscriptions via //blp/refdata and //blp/mktdata.
  name: Real-Time and Historical Data
- description: Bloomberg Data License delivers 50M+ securities and 30,000+ fields over REST, SFTP, and cloud channels.
  name: Bulk Enterprise Delivery
- description: Bloomberg News powers bloomberg.com, Bloomberg Television, and licensed enterprise news feeds (Event-Driven Feeds, Machine Readable News).
  name: News and Editorial Content
finops:
- name: Bloomberg Lp Finops
  service_category: API
  slug: bloomberg-lp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-lp.png
integrations:
- description: Bloomberg Excel Add-In for spreadsheet-based analysis on top of Terminal entitlements.
  name: Microsoft Excel
- description: blpapi Python SDK (3.26.x) for data science and quantitative finance workflows.
  name: Python
- description: BLPAPI Java SDK for enterprise JVM applications.
  name: Java
- description: BLPAPI .NET SDK for C# and F# applications.
  name: .NET
- description: BLPAPI C++ SDK for low-latency trading and market data applications.
  name: C++
- description: Bloomberg Datafeed Toolbox connects MATLAB analytics to Bloomberg.
  name: MATLAB
- description: Community Rblpapi package binds R to BLPAPI.
  name: R
- description: Bloomberg Data License supports cloud delivery to all three major hyperscalers.
  name: AWS / Azure / GCP
json_schemas:
- name: FIGI Record
  property_count: 13
  slug: openfigi-figi-record
- name: OpenFIGI Mapping Job
  property_count: 16
  slug: openfigi-mapping-job
json_structures:
- name: Openfigi Figi Record Structure
  property_count: 12
  slug: openfigi-figi-record-structure
jsonld:
- class_count: 26
  name: Bloomberg Lp Context
  property_count: 3
  slug: bloomberg-lp-context
layout: provider
modified: '2026-05-23'
name: Bloomberg L.P.
nav: Providers
network: true
overview: 'Bloomberg L.P. publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Filter API, Mapping API, Reference API, and 1 more. Tagged areas include Financial Services, Market Data, News, Reference Data, and Symbology.


  The Bloomberg L.P. catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Bloomberg L.P.''s developer surface includes authentication, documentation, support, pricing, engineering blog, product news, and 22 more developer resources.'
plans:
- name: Bloomberg Lp Plans Pricing
  plan_count: 6
  slug: bloomberg-lp-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 6
  name: Bloomberg Lp Rate Limits
  slug: bloomberg-lp-rate-limits
rules:
- name: Bloomberg L.P. API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bloomberg-lp-jsonschema-spectral-rules
- name: Bloomberg L.P. API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: openfigi-rules
score:
  band: strong
  composite: 60.7
  delta: -0.6
  facets:
    commercial_clarity: 84.2
    contract_quality: 72.4
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 61.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-lp/refs/heads/main/screenshots/bloomberg-lp-2026-06-20T173441.png
security:
- kind: authentication
  name: Bloomberg Lp Authentication
  slug: bloomberg-lp-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bloomberg Lp Domain Security
  slug: bloomberg-lp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloomberg-lp
tags:
- Financial Services
- Market Data
- News
- Reference Data
- Symbology
- Terminal
use_cases:
- description: Use OpenFIGI to resolve broker, exchange, and vendor identifiers to a stable, permanent FIGI for downstream joins.
  name: Cross-Provider Symbology
- description: Build algorithmic trading strategies using BLPAPI real-time and historical market data subscriptions.
  name: Quantitative Trading
- description: Pull reference, pricing, and regulatory data from Bloomberg Data License into risk and regulatory pipelines.
  name: Risk and Compliance Reporting
- description: Combine Bloomberg historical data with news and event-driven feeds for sell-side, buy-side, and academic research.
  name: Research and Analytics
- description: Embed Bloomberg market data and reference data into OMS/EMS and portfolio analytics platforms via the Server API.
  name: Portfolio and Order Management
website: https://www.bloomberg.com/company/
---
