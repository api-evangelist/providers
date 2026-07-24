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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 84.6
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Bloomberg Agentic Access
  operation_count: 9
  slug: bloomberg-agentic-access
  summary_line: 9 operations · 9 acting · 1 human-in-the-loop
api_count: 5
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
- description: The Bloomberg Open API (BLPAPI) Core — the foundational service-oriented, socket-based API used by the Desktop API, Server API (SAPI), B-PIPE, and Bloomberg Platform products. Provides Request/Respons
  name: Bloomberg BLPAPI Core
  slug: bloomberg-blpapi-core
artifact_total: 53
asyncapis:
- description: Event surface of the Bloomberg Open API (BLPAPI) Subscription paradigm. Clients call Session.subscribe(SubscriptionList) over a BLPAPI SDK session (Desktop API localhost:8194 or SAPI/B-PIPE host); str
  name: Bloomberg BLPAPI Market Data Subscriptions
  slug: bloomberg-market-data-asyncapi
collections:
- collection_type: open
  name: Bloomberg BLPAPI Core
  slug: open-blpapi-core
common:
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
  type: MCPServer
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
modified: '2026-06-20'
name: Bloomberg
nav: Providers
network: true
overview: 'Bloomberg publishes 1 API on the [APIs.io](https://apis.io/) network: BLPAPI Core. Tagged areas include Analytics, Business Intelligence, Data License, Enterprise, and Execution Management.


  The Bloomberg catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 2 Spectral governance rulesets.


  Bloomberg''s developer surface includes developer portal, documentation, getting-started guide, support, API reference, engineering blog, authentication, and 26 more developer resources.'
plans:
- name: Bloomberg Plans Pricing
  plan_count: 2
  slug: bloomberg-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 3
  name: Bloomberg Rate Limits
  slug: bloomberg-rate-limits
rules:
- name: Bloomberg API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: bloomberg-jsonschema-spectral-rules
- name: Bloomberg API Rules
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
  band: exemplar
  composite: 72.9
  delta: 2.8
  facets:
    commercial_clarity: 63.2
    contract_quality: 69.0
    developer_ergonomics: 73.9
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 63.2
  previous_composite: 70.1
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 89.1
  schema_version: 0.5
  scored_at: '2026-07-23'
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
- Financial Services
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
