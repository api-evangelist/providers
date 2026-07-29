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
    asyncapi_events: true
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
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Refinitiv Agentic Access
  operation_count: 47
  slug: refinitiv-agentic-access
  summary_line: 47 operations · 16 acting
api_count: 45
apis:
- description: Python library providing uniform access to the breadth and depth of financial data and services available on the LSEG Data Platform. It offers ease-of-use interfaces for streaming and non-streaming da
  name: Refinitiv Data Library for Python
  slug: refinitiv-data-library-for-python
- description: .NET library providing uniform access to financial data and services available on the LSEG Data Platform. It supports streaming and non-streaming data retrieval and integrates with LSEG Workspace, the
  name: Refinitiv Data Library for .NET
  slug: refinitiv-data-library-for-net
- description: Suite of ease-of-use libraries and interfaces for Python, TypeScript and JavaScript providing access to streaming and non-streaming data services on the LSEG Data Platform. These libraries have been s
  name: Refinitiv Data Platform Libraries
  slug: refinitiv-data-platform-libraries
- description: Python library providing access to financial data, news, and symbology from within the Refinitiv Eikon or LSEG Workspace desktop application. It enables Eikon end users to access data programmatically
  name: Eikon Data API
  slug: eikon-data-api
- description: Low-latency streaming API for real-time market data using WebSocket connections. It supports the Open Message Model (OMM) and allows applications to connect directly to Refinitiv Real-Time distributio
  name: Refinitiv Real-Time WebSocket API
  slug: refinitiv-real-time-websocket-api
- description: Open source Java SDK for the Refinitiv Real-Time platform, containing the Enterprise Message API (EMA) for ease-of-use rapid development and the Enterprise Transport API (ETA) for low-level, high-perf
  name: Refinitiv Real-Time SDK - Java
  slug: refinitiv-real-time-sdk-java
- description: Open source C/C++ SDK for the Refinitiv Real-Time platform, providing the Enterprise Message API (EMA) and Enterprise Transport API (ETA) for building high-performance, low-latency applications that c
  name: Refinitiv Real-Time SDK - C/C++
  slug: refinitiv-real-time-sdk-cc
- description: Access to comprehensive news content from Refinitiv including real-time and historical news articles, Machine Readable News (MRN), and news analytics delivered through the Refinitiv Data Platform.
  name: Refinitiv News API
  slug: refinitiv-news-api
- description: 'Access to environmental, social, and governance (ESG) data, scores, and analytics for sustainable investing. The API provides ESG scores, carbon emissions data, green revenue metrics, and controversy '
  name: Refinitiv ESG API
  slug: refinitiv-esg-api
- description: SOAP-based web service API for DataScope Select, providing extraction functionality for global pricing, reference, and historical data. Clients are encouraged to migrate to the REST API for new develo
  name: LSEG DataScope Select - SOAP API
  slug: lseg-datascope-select-soap-api
- description: REST API providing access to historical high-frequency timestamped tick data across all global asset classes dating back to 1996. It supports custom reporting and Venue by Day standard reporting for c
  name: LSEG Tick History REST API
  slug: lseg-tick-history-rest-api
- description: API providing access to Datastream, the world's leading time series database with histories back to the 1900s and over 48 million individual instruments or indicators. Available via SOAP, REST (JSON/X
  name: Datastream Web Service API
  slug: datastream-web-service-api
- description: REST API enabling clients to place orders for LSEG Due Diligence Reports from within their own internal systems and onboarding platforms. It uses OAuth2 for security and follows the OpenAPI 3 standard
  name: LSEG Due Diligence Portal API
  slug: lseg-due-diligence-portal-api
- description: API for wealth management that provides access to Refinitiv hosted content and capabilities. It integrates into advisor solutions, customer-facing investment portals, and online trading platforms thro
  name: Refinitiv Knowledge Direct API (RKD)
  slug: refinitiv-knowledge-direct-api-rkd
- description: Natural language processing API that identifies and tags entities such as companies, people, deals, geographical locations, industries, and events within unstructured text. It maps recognized entities
  name: Intelligent Tagging RESTful API
  slug: intelligent-tagging-restful-api
- description: End-to-end financial application development kit that allows developers to design a GUI, power it with market data, and integrate logic into workflows. It enables creation of web-based financial appli
  name: Workspace SDK
  slug: workspace-sdk
- description: Interoperability API that connects client web applications to LSEG Workspace Web. It allows applications to authenticate, connect to a running Workspace instance in the same browser, and exchange meta
  name: Workspace Web Side by Side API
  slug: workspace-web-side-by-side-api
- description: FIX protocol-based API for electronic FX trading on LSEG Matching venues, supporting spot and forwards currency trading. It uses FIX 5.0 SP2 with a specific set of FIX messages, tags, and workflows fo
  name: FX Trading - Spot and Forwards Matching API
  slug: fx-trading-spot-and-forwards-matching-api
- description: FIX protocol-based API for electronic trading of non-deliverable forwards (NDFs) on LSEG Matching venues. It provides connectivity for trading participants to submit and manage NDF orders.
  name: FX Trading - NDF Matching API
  slug: fx-trading-ndf-matching-api
- description: Point-to-point market data service based on FIX SBE technology, allowing trading participants to receive real-time information for each instrument traded on Primary CLOBs for NDF Matching venues.
  name: FX Market Data - NDF Matching API
  slug: fx-market-data-ndf-matching-api
- description: Service providing reference data for LSEG FX venues, offering instrument and venue configuration data to support FX trading operations on the replatformed spot and forward Matching venues.
  name: FX Reference Data API
  slug: fx-reference-data-api
- description: API providing reporting and analytics for FX trading participants on LSEG venues, enabling access to execution quality metrics and participant insight data.
  name: FX Participant Insight Reporting API
  slug: fx-participant-insight-reporting-api
- description: OAuth 2.0 token management for obtaining and refreshing access tokens required by all other API endpoints.
  name: Refinitiv Authentication API
  slug: refinitiv-authentication-api
- description: Case creation, screening, retrieval, update, and deletion operations for entity screening against the World-Check database.
  name: Refinitiv Cases API
  slug: refinitiv-cases-api
- description: Configuration retrieval for country codes, fields, consents, and test entities required for verification requests.
  name: Refinitiv Configuration API
  slug: refinitiv-configuration-api
- description: Connectivity and authentication testing endpoints.
  name: Refinitiv Connection API
  slug: refinitiv-connection-api
- description: Search for organizations, equity instruments, and equity quotes using various identifier types including name, ticker, RIC, LEI, and PermID.
  name: Refinitiv Entity Search API
  slug: refinitiv-entity-search-api
- description: Environmental, Social, and Governance data including scores, measures, carbon emissions, and controversy tracking across thousands of companies.
  name: Refinitiv ESG API
  slug: refinitiv-esg-api
- description: On-demand and scheduled data extraction operations for retrieving pricing, reference, corporate actions, and historical data.
  name: Refinitiv Extractions API
  slug: refinitiv-extractions-api
- description: Group management operations for organizing cases and configuring screening parameters per group.
  name: Refinitiv Groups API
  slug: refinitiv-groups-api
- description: Access to historical interday and intraday pricing data for financial instruments including summaries, events, and time series.
  name: Refinitiv Historical Pricing API
  slug: refinitiv-historical-pricing-api
- description: Instrument search, validation, and instrument list management operations.
  name: Refinitiv Instruments API
  slug: refinitiv-instruments-api
- description: Access to real-time and historical news headlines and stories from Reuters and other sources.
  name: Refinitiv News API
  slug: refinitiv-news-api
- description: Ongoing screening monitoring for cases that have been flagged for continuous surveillance against the World-Check database.
  name: Refinitiv Ongoing Screening API
  slug: refinitiv-ongoing-screening-api
- description: Real-time and delayed snapshot pricing data for financial instruments and pricing chains.
  name: Refinitiv Pricing API
  slug: refinitiv-pricing-api
- description: Instrument Pricing Analytics (IPA) service for pricing financial contracts, calculating risk measures, and running quantitative models.
  name: Refinitiv Quantitative Analytics API
  slug: refinitiv-quantitative-analytics-api
- description: Match unstructured entity records to PermID identifiers for concordance and entity resolution.
  name: Refinitiv Record Matching API
  slug: refinitiv-record-matching-api
- description: Reference data operations for retrieving profile details and resolution toolkit configurations.
  name: Refinitiv Reference API
  slug: refinitiv-reference-api
- description: Schedule management for recurring extraction jobs.
  name: Refinitiv Schedules API
  slug: refinitiv-schedules-api
- description: Operations for retrieving and managing screening results including matched profiles and resolution workflows.
  name: Refinitiv Screening Results API
  slug: refinitiv-screening-results-api
- description: Discovery and search across organizations, instruments, quotes, and economic indicators.
  name: Refinitiv Search API
  slug: refinitiv-search-api
- description: Service discovery for streaming connections to real-time pricing and data services.
  name: Refinitiv Streaming API
  slug: refinitiv-streaming-api
- description: Symbol lookup and conversion between different identifier types including RIC, ISIN, CUSIP, SEDOL, and PermID.
  name: Refinitiv Symbology API
  slug: refinitiv-symbology-api
- description: User account information and preferences management.
  name: Refinitiv Users API
  slug: refinitiv-users-api
- description: Identity and document verification submission and transaction record retrieval.
  name: Refinitiv Verification API
  slug: refinitiv-verification-api
artifact_total: 69
asyncapis:
- description: Low-latency streaming API for real-time market data using WebSocket connections. It supports the Open Message Model (OMM) and allows applications to connect directly to Refinitiv Real-Time distributio
  name: Refinitiv Real-Time WebSocket API
  slug: refinitiv-real-time-websocket-asyncapi
collections:
- collection_type: open
  name: Refinitiv Data Platform (RDP) APIs
  slug: open-refinitiv-data-platform
- collection_type: open
  name: Refinitiv LSEG DataScope Select REST API
  slug: open-refinitiv-datascope-select
- collection_type: open
  name: Refinitiv PermID Entity Search API
  slug: open-refinitiv-permid-entity-search
- collection_type: open
  name: Refinitiv Qual-ID API
  slug: open-refinitiv-qual-id
- collection_type: open
  name: Refinitiv World-Check One API
  slug: open-refinitiv-world-check-one
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/refinitiv-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/refinitiv-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/refinitiv-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/refinitiv
- group: design
  title: ''
  type: JSONLD
  url: json-ld/refinitiv-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/refinitiv-instrument-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/refinitiv-esg-score-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/refinitiv-screening-case-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/refinitiv-news-article-schema.json
- group: start
  title: ''
  type: Portal
  url: https://developers.lseg.com/en
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.lseg.com/en/api-catalog
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lseg.com/en/api-catalog
- group: operate
  title: ''
  type: Support
  url: https://developers.lseg.com/en/support
- group: company
  title: ''
  type: Blog
  url: https://developers.lseg.com/en/article-catalog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LSEG-API-Samples
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Refinitiv-API-Samples
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.lseg.com/en/terms-and-conditions
- group: operate
  title: ''
  type: Contact
  url: https://developers.lseg.com/en/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lseg.com/en/policies/privacy-statement
- group: operate
  title: ''
  type: Community
  url: https://community.developers.refinitiv.com/
- group: company
  title: ''
  type: Website
  url: https://www.lseg.com/en
- group: start
  title: ''
  type: Login
  url: https://www.lseg.com/en/product-logins
- group: build
  title: ''
  type: Developer Tools
  url: https://developers.lseg.com/en/tools-catalog
- group: other
  title: ''
  type: Medium
  url: https://medium.com/lseg-developer-community
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/refinitiv-data-platform-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/refinitiv-datascope-select-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/refinitiv-permid-entity-search-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/refinitiv-qual-id-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/refinitiv-world-check-one-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/refinitiv-real-time-websocket-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/refinitiv-instrument-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/refinitiv-esg-score-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/refinitiv-news-article-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/refinitiv-screening-case-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/refinitiv-data-platform-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/refinitiv-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/refinitiv-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/refinitiv-vocabulary.yml
created: '2024-01-01'
description: Refinitiv, an LSEG (London Stock Exchange Group) business, provides financial market data, infrastructure, and analytics to businesses and financial professionals worldwide.
examples:
- key_count: 2
  name: Refinitiv Get Pricing Snapshots Example
  slug: refinitiv-get-pricing-snapshots-example
- key_count: 2
  name: Refinitiv World Check Screen Entity Example
  slug: refinitiv-world-check-screen-entity-example
finops:
- name: Refinitiv Finops
  service_category: Market Data
  slug: refinitiv-finops
graphqls:
- description: Refinitiv (now LSEG Data & Analytics) provides financial data, trading infrastructure, and analytics. The API covers real-time market data, historical prices, reference data, news, ESG scores, and fin
  name: Refinitiv GraphQL API
  slug: refinitiv-graphql
image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
json_schemas:
- name: Refinitiv ESG Score
  property_count: 15
  slug: refinitiv-esg-score
- name: Refinitiv Financial Instrument
  property_count: 14
  slug: refinitiv-instrument
- name: Refinitiv News Article
  property_count: 13
  slug: refinitiv-news-article
- name: Refinitiv World-Check Screening Case
  property_count: 11
  slug: refinitiv-screening-case
json_structures:
- name: Refinitiv Data Platform Structure
  property_count: 0
  slug: refinitiv-data-platform-structure
jsonld:
- class_count: 0
  name: Refinitiv Context
  property_count: 7
  slug: refinitiv-context
layout: provider
modified: '2026-05-19'
name: Refinitiv
nav: Providers
network: true
overview: 'Refinitiv publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Real-Time WebSocket API, News API, ESG API, and 23 more.


  The Refinitiv catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Refinitiv''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, engineering blog, and 32 more developer resources.'
plans:
- name: Refinitiv Plans Pricing
  plan_count: 1
  slug: refinitiv-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Refinitiv Rate Limits
  slug: refinitiv-rate-limits
rules:
- name: Refinitiv API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 5
  slug: refinitiv-asyncapi-spectral-rules
- name: Refinitiv API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: refinitiv-jsonschema-spectral-rules
- name: Refinitiv API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 4
  slug: refinitiv-rules
score:
  band: developing
  composite: 55.9
  delta: -3.3
  facets:
    commercial_clarity: 63.2
    contract_quality: 75.0
    developer_ergonomics: 45.7
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 59.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/refinitiv/refs/heads/main/screenshots/refinitiv-2026-06-20T192746.png
security:
- kind: authentication
  name: Refinitiv Authentication
  slug: refinitiv-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Refinitiv Domain Security
  slug: refinitiv-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: refinitiv
website: https://www.lseg.com/en
---
