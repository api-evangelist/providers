---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Bloomberg Agentic Access
  operation_count: 9
  slug: bloomberg-agentic-access
  summary_line: 9 operations · 9 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Provides real-time and historical market data, including stock prices, indices, commodities, and currencies.
  name: Bloomberg Market Data API
  slug: bloomberg-market-data-api
- description: Delivers real-time market data, historical data, reference data, and calculation engine capabilities from the Bloomberg Terminal for server applications.
  name: Bloomberg Server API (SAPI)
  slug: bloomberg-server-api
- description: Provides programmatic access to Bloomberg Data License content including reference, pricing, regulatory, ESG, corporate actions, fundamentals, and alternative data.
  name: Bloomberg Data License API
  slug: bloomberg-data-license-api
- description: Enables programmatic management and automation of equities, futures, and options trading through the Bloomberg Execution Management System.
  name: Bloomberg EMSX API
  slug: bloomberg-emsx-api
- baseURL: tcp://localhost:8194
  baseurl_source: spec
  description: The Bloomberg Open API (BLPAPI) Core — the foundational service-oriented, socket-based API used by the Desktop API, Server API (SAPI), B-PIPE, and Bloomberg Platform products. Provides Request/Respons
  name: Bloomberg BLPAPI Core
  slug: bloomberg-blpapi-core
artifact_total: 74
asyncapis:
- description: Event surface of the Bloomberg Open API (BLPAPI) Subscription paradigm. Clients call Session.subscribe(SubscriptionList) over a BLPAPI SDK session (Desktop API localhost:8194 or SAPI/B-PIPE host); str
  name: Bloomberg BLPAPI Market Data Subscriptions
  slug: bloomberg-market-data-asyncapi
collections:
- collection_type: postman
  name: Bloomberg BLPAPI Core Field Discovery API
  slug: postman-bloomberg-field-discovery-api
- collection_type: postman
  name: Bloomberg BLPAPI Core Field Discovery Historical Data API
  slug: postman-bloomberg-historical-data-api
- collection_type: postman
  name: Bloomberg BLPAPI Core Field Discovery Intraday Bars API
  slug: postman-bloomberg-intraday-bars-api
- collection_type: postman
  name: Bloomberg BLPAPI Core Field Discovery Intraday Ticks API
  slug: postman-bloomberg-intraday-ticks-api
- collection_type: postman
  name: Bloomberg BLPAPI Core Field Discovery Real-Time Bars API
  slug: postman-bloomberg-real-time-bars-api
- collection_type: postman
  name: Bloomberg BLPAPI Core Field Discovery Real-Time Market Data API
  slug: postman-bloomberg-real-time-market-data-api
- collection_type: postman
  name: Bloomberg BLPAPI Core Field Discovery Reference Data API
  slug: postman-bloomberg-reference-data-api
- collection_type: postman
  name: Bloomberg BLPAPI Core Field Discovery Request/Response API
  slug: postman-bloomberg-request-response-api
- collection_type: postman
  name: Bloomberg BLPAPI Core Field Discovery Subscriptions API
  slug: postman-bloomberg-subscriptions-api
- collection_type: postman
  name: Bloomberg BLPAPI Core Field Discovery VWAP API
  slug: postman-bloomberg-vwap-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bloomberg BLPAPI Core Field Discovery API
  slug: open-bloomberg-field-discovery-api
- collection_type: open
  name: Bloomberg BLPAPI Core Field Discovery Historical Data API
  slug: open-bloomberg-historical-data-api
- collection_type: open
  name: Bloomberg BLPAPI Core Field Discovery Intraday Bars API
  slug: open-bloomberg-intraday-bars-api
- collection_type: open
  name: Bloomberg BLPAPI Core Field Discovery Intraday Ticks API
  slug: open-bloomberg-intraday-ticks-api
- collection_type: open
  name: Bloomberg BLPAPI Core Field Discovery Real-Time Bars API
  slug: open-bloomberg-real-time-bars-api
- collection_type: open
  name: Bloomberg BLPAPI Core Field Discovery Real-Time Market Data API
  slug: open-bloomberg-real-time-market-data-api
- collection_type: open
  name: Bloomberg BLPAPI Core Field Discovery Reference Data API
  slug: open-bloomberg-reference-data-api
- collection_type: open
  name: Bloomberg BLPAPI Core Field Discovery Request/Response API
  slug: open-bloomberg-request-response-api
- collection_type: open
  name: Bloomberg BLPAPI Core Field Discovery Subscriptions API
  slug: open-bloomberg-subscriptions-api
- collection_type: open
  name: Bloomberg BLPAPI Core Field Discovery VWAP API
  slug: open-bloomberg-vwap-api
- collection_type: open
  name: Bloomberg BLPAPI Core
  slug: open-blpapi-core
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bloomberg/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bloomberg-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloomberg-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bloomberg
- group: start
  title: ''
  type: Portal
  url: https://developer.bloomberg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomberg.com/professional/support/api-library/
- group: build
  title: ''
  type: SDKs
  url: https://bloomberg.github.io/blpapi-docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bloomberg.com/professional/solutions/asset-management/developer/
- group: start
  title: ''
  type: Login
  url: https://console.bloomberg.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
- group: design
  title: ''
  type: SpectralRules
  url: rules/bloomberg-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bloomberg-vocabulary.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://bloomberg.github.io/blpapi-docs/
- group: company
  title: ''
  type: Blog
  url: https://www.techatbloomberg.com/blog/
- group: auth
  title: ''
  type: Security
  url: https://www.bloomberg.com/responsible-disclosure
- group: build
  title: ''
  type: Packages
  url: packages/bloomberg-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bloomberg-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bloomberg-security.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bloomberg-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bloomberg-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/bloomberg-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bloomberg-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bloomberg-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bloomberg-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bloomberg-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bloomberg-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bloomberg-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bloomberg-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/bloomberg-market-data-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-aim/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-apis/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-applications/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-buyside-enterprise-solutions/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-data/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-data-sets/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-data-workflows/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-emsx/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-enterprise/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-esg-products/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-excel-plug-ins/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-financial-solutions/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-government-bgov/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-index-solutions-limited-bisl/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-indices/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-instant-messaging/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-intelligence/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-media-platforms/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-message/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-news/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-platform/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-product-suite/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-products-and-platforms/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-professional-service/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-proprietary-technologies/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-query-language-bql/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-sustainable-finance-products/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-tax-btax/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-tax-research/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-television-and-radio/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-terminal/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-terminals/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-tradebook/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-tv/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/bloomberg-valuation-service-bval/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/second-measure/
created: '2024-01-20'
description: Bloomberg delivers business and markets news, data, analysis, and video to the world, featuring stories from Businessweek and Bloomberg News. Bloomberg provides a suite of developer APIs including BLPAPI, Server API, and the Hypermedia API for programmatic access to market data, analytics, and enterprise services.
examples:
- key_count: 0
  name: Blpapi Core Error Message Example
  slug: blpapi-core-error-message-example
- key_count: 0
  name: Blpapi Core Market Data Event Example
  slug: blpapi-core-market-data-event-example
- key_count: 0
  name: Blpapi Core Subscription Example
  slug: blpapi-core-subscription-example
- key_count: 0
  name: Blpapi Core Subscription List Example
  slug: blpapi-core-subscription-list-example
features:
- description: Stream live market data for equities, fixed income, commodities, and currencies via subscription.
  name: Real-Time Market Data
- description: Access end-of-day historical time series with periodicity, currency, and corporate-action adjustments.
  name: Historical Data
- description: Retrieve raw tick-by-tick trade and quote data for granular intraday analysis.
  name: Intraday Tick Data
- description: Query current reference, descriptive, fundamental, and pricing field values for securities.
  name: Reference Data
- description: Search and discover Bloomberg field mnemonics and metadata via the API Data Dictionary.
  name: Field Discovery
- description: Access BLPAPI through C, C++, Java, .NET, Python, Perl, and COM Excel SDKs.
  name: Multi-Language SDK
finops:
- name: Bloomberg Finops
  service_category: Market Data / Financial Services
  slug: bloomberg-finops
image: /assets/icons/bloomberg.png
integrations:
- description: Extend Bloomberg Terminal capabilities through the Desktop API integration.
  name: Bloomberg Terminal
- description: Access BLPAPI data directly from Excel spreadsheets using the COM Excel SDK.
  name: Excel
- description: Build data analytics and machine learning pipelines with the Python BLPAPI SDK.
  name: Python
- description: Distribute Bloomberg data across enterprise infrastructure using the B-PIPE product.
  name: B-PIPE
json_schemas:
- name: ErrorMessage
  property_count: 0
  slug: bloomberg-errormessage
- name: Bloomberg Market Data
  property_count: 0
  slug: bloomberg-market-data
- name: MarketDataEvent
  property_count: 0
  slug: bloomberg-marketdataevent
- name: Bloomberg Security
  property_count: 27
  slug: bloomberg-security
- name: Subscription
  property_count: 0
  slug: bloomberg-subscription
- name: SubscriptionList
  property_count: 0
  slug: bloomberg-subscriptionlist
- name: ErrorMessage
  property_count: 0
  slug: blpapi-core-error-message
- name: MarketDataEvent
  property_count: 0
  slug: blpapi-core-market-data-event
- name: Bloomberg BLPAPI Core Message Types
  property_count: 0
  slug: blpapi-core-messages
- name: SubscriptionList
  property_count: 0
  slug: blpapi-core-subscription-list
- name: Subscription
  property_count: 0
  slug: blpapi-core-subscription
json_structures:
- name: Bloomberg Structure
  property_count: 0
  slug: bloomberg-structure
- name: Blpapi Core Error Message Structure
  property_count: 0
  slug: blpapi-core-error-message-structure
- name: Blpapi Core Market Data Event Structure
  property_count: 0
  slug: blpapi-core-market-data-event-structure
- name: Blpapi Core Subscription List Structure
  property_count: 0
  slug: blpapi-core-subscription-list-structure
- name: Blpapi Core Subscription Structure
  property_count: 0
  slug: blpapi-core-subscription-structure
jsonld:
- class_count: 0
  name: Bloomberg Context
  property_count: 17
  slug: bloomberg-context
- class_count: 0
  name: Blpapi Core Context
  property_count: 0
  slug: blpapi-core-context
layout: provider
modified: '2026-08-27'
name: Bloomberg
nav: Providers
network: true
overview: 'Bloomberg publishes 1 API on the [APIs.io](https://apis.io/) network: BLPAPI Core. Tagged areas include Analytics, Business Intelligence, Data License, Enterprise, and Execution Management.


  The Bloomberg catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 2 Spectral governance rulesets.


  Bloomberg''s developer surface includes developer portal, documentation, getting-started guide, support, API reference, engineering blog, authentication, and 63 more developer resources.'
plans:
- name: Bloomberg Plans Pricing
  plan_count: 2
  slug: bloomberg-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Bloomberg Rate Limits
  slug: bloomberg-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Bloomberg API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: bloomberg-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Bloomberg API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 3
  slug: bloomberg-spectral-rules
scopes:
- name: Bloomberg Scopes
  scope_count: 3
  slug: bloomberg-scopes
  summary_line: 3 scopes · authorizationCode/refreshToken
score:
  band: strong
  composite: 59.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 67.5
    catalog_earned_first_party: 0.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 47.0
    contract_quality: 66.4
    developer_ergonomics: 67.3
    discoverability: 59.3
    governance: 47.0
    operational_transparency: 36.8
  previous_composite: 60.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 78.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg/refs/heads/main/screenshots/bloomberg-2026-06-20T173403.png
security:
- kind: authentication
  name: Bloomberg Authentication
  slug: bloomberg-authentication
  summary_line: session-identity/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Bloomberg Domain Security
  slug: bloomberg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bloomberg Vulnerability Disclosure
  slug: bloomberg-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bloomberg
tags:
- Analytics
- Business Intelligence
- Data License
- Enterprise
- Execution Management
- Financial-Services
- Market Data
- News
- Quantitative Analysis
- Trading
- Transaction Cost Analysis
use_cases:
- description: Build quantitative models using historical and real-time market data for alpha generation.
  name: Quantitative Research
- description: Monitor portfolio risk exposure using real-time pricing and reference data feeds.
  name: Risk Management
- description: Feed market data into trading algorithms via EMSX for automated order execution.
  name: Algorithmic Trading
- description: Access regulatory and compliance data through Data License for reporting requirements.
  name: Regulatory Reporting
website: https://developer.bloomberg.com/
---
