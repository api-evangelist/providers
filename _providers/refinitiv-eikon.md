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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Refinitiv Eikon Agentic Access
  operation_count: 29
  slug: refinitiv-eikon-agentic-access
  summary_line: 29 operations · 12 acting
api_count: 47
apis:
- description: Python and R library that allows programmatic access to Refinitiv Eikon data. Provides access to instrument pricing, fundamentals, estimates, time series, news, and symbology. Requires the Eikon or LS
  name: Eikon Data API
  slug: eikon-data-api
- description: SDK for building intelligent, compliant messaging bots within the LSEG Messenger platform. Enables sending, receiving, and replying to messages in one-to-one and group chat contexts with full OAuth 2.
  name: LSEG Messenger Bot SDK
  slug: lseg-messenger-bot-sdk
- description: API allowing external applications to connect with and pass information into LSEG Messenger. Requires user interaction and enables integration of third-party applications alongside the messenger for c
  name: Messenger Side by Side API
  slug: messenger-side-by-side-api
- description: Python library providing uniform, ease-of-use interfaces for accessing the breadth and depth of financial data and services on the LSEG Data Platform. Returns data as Pandas DataFrames and supports bo
  name: Refinitiv Data Library for Python
  slug: refinitiv-data-library-for-python
- description: TypeScript and JavaScript library providing ease-of-use interfaces for accessing financial data and services on the Refinitiv Data Platform. Supports both streaming and non-streaming data services for
  name: Refinitiv Data Library for TypeScript
  slug: refinitiv-data-library-for-typescript
- description: '.NET library providing uniform interfaces for accessing the Refinitiv Data Platform. Supports streaming and non-streaming data services for C# and other .NET languages, rebranded as LSEG Data Library '
  name: Refinitiv Data Library for .NET
  slug: refinitiv-data-library-for-net
- description: API providing access to Datastream content, the world's leading time series database, via SOAP/XML and REST/JSON protocols. Enables strategists, economists, and research communities to access comprehe
  name: Datastream Web Service API
  slug: datastream-web-service-api
- description: Standards-based WebSocket API for real-time pricing streaming using JSON message formats. Connects to Real-Time Distribution Systems and Real-Time Optimized cloud solutions for data consumption, contr
  name: LSEG WebSocket API
  slug: lseg-websocket-api
- description: Java SDK encompassing the Enterprise Message API (EMA) and Enterprise Transport API (ETA) for building high-performance real-time data applications. Provides consumer, provider, and publisher features
  name: Real-Time Java SDK
  slug: real-time-java-sdk
- description: C and C++ SDK providing the Enterprise Message API (EMA) and Enterprise Transport API (ETA) for ultra-low-latency, high-throughput real-time data applications. The ETA foundation enables the highest p
  name: Real-Time C/C++ SDK
  slug: real-time-cc-sdk
- description: C# SDK providing the Enterprise Transport API (ETA) for building high-performance real-time data applications on .NET. Supports consuming, providing, and publishing real-time content using the Open Me
  name: Real-Time C# SDK
  slug: real-time-c-sdk
- description: Web API for integrating standalone desktop applications with Refinitiv Eikon to create dynamic custom workflows. Enables launching Eikon apps programmatically and exchanging context such as portfolios
  name: Eikon Side by Side Interoperability API
  slug: eikon-side-by-side-interoperability-api
- description: 'API enabling interoperability and context passing between LSEG Workspace Web and external web applications within the same browser instance. Supports authentication, metadata exchange, and navigation '
  name: Workspace Web Side by Side API
  slug: workspace-web-side-by-side-api
- description: End-to-end financial application development kit for designing GUI applications, powering them with market data, and integrating workflow logic into LSEG Workspace. Provides UI components, data integr
  name: Workspace SDK
  slug: workspace-sdk
- description: REST API providing programmatic access to the DataScope Select platform for extracting global prices, corporate actions, reference data, historical data, cross-reference data, and entity data. Support
  name: LSEG DataScope Select REST API
  slug: lseg-datascope-select-rest-api
- description: REST API providing programmatic access to historical tick-level market data through the DataScope Select platform. Supports on-demand and scheduled extractions of tick data, intraday bars, and end-of-
  name: LSEG Tick History REST API
  slug: lseg-tick-history-rest-api
- description: RESTful API for searching and discovering organizations, equity instruments, and equity quotes using PermID identifiers. Supports searching by name, ticker, RIC, LEI, and other standard identifiers ac
  name: PermID Entity Search API
  slug: permid-entity-search-api
- description: RESTful API for matching unstructured entity records to PermID identifiers. Enables concordance by mapping external entity data to LSEG permanent identifiers for organizations and instruments.
  name: PermID Record Matching API
  slug: permid-record-matching-api
- description: RESTful API for extracting entities, topics, and metadata from unstructured text content. Identifies organizations, people, instruments, and other financial entities within documents using natural lan
  name: Intelligent Tagging API
  slug: intelligent-tagging-api
- description: Web services API integrating financial market data, news, and analytics into websites, trading platforms, advisory portals, and mobile applications. Delivers pricing, news, fundamental data, consensus
  name: Refinitiv Knowledge Direct API
  slug: refinitiv-knowledge-direct-api
- description: Discovery Symbology API for concordance, navigation, and discovery of financial content. Enables mapping from external identifiers to LSEG PermIDs and navigating between a wide range of identifier typ
  name: Symbology API
  slug: symbology-api
- description: API enabling search across organizations, instruments, quotes, and economic indicators on the Refinitiv Data Platform. Part of the Search Light family of APIs for wealth management applications.
  name: Search API
  slug: search-api
- description: API built on the Refinitiv Data Platform providing streamlined access to real-time and historical sell-side research reports. Serves as the aggregate delivery system for providing buy-side institution
  name: Research API
  slug: research-api
- description: API providing access to financial news content for wealth management applications. Delivers real-time and historical news from Reuters and other sources through the Refinitiv Data Platform.
  name: News API for Wealth
  slug: news-api-for-wealth
- description: API providing access to Lipper fund data for wealth management applications. Delivers fund performance, classifications, ratings, and other mutual fund data through the Refinitiv Data Platform.
  name: Funds API for Wealth
  slug: funds-api-for-wealth
- description: API providing access to consensus estimates data for wealth management applications. Delivers analyst estimates, recommendations, and forecasts through the Refinitiv Data Platform.
  name: Estimates API for Wealth
  slug: estimates-api-for-wealth
- description: API providing access to institutional and fund ownership data for wealth management applications. Delivers ownership holdings, stakes, and shareholder information through the Refinitiv Data Platform.
  name: Ownership API for Wealth
  slug: ownership-api-for-wealth
- description: API providing access to regulatory filings data through the Refinitiv Data Platform. Delivers SEC filings, annual reports, and other regulatory documents for financial analysis and compliance workflow
  name: Filings API
  slug: filings-api
- description: Workflow-based REST/JSON API for screening entities against the World-Check risk intelligence database. Supports due diligence in the fight against financial crime, bribery, and corruption by enabling
  name: World-Check One API
  slug: world-check-one-api
- description: Cloud-native, stateless screening API purpose-built for real-time, low-latency screening of individuals and entities in modern payment workflows. Screens against World-Check risk intelligence data and
  name: World-Check Verify API
  slug: world-check-verify-api
- description: Web SDK for building custom applications using HTML5 and JavaScript within the Eikon App Studio environment. Provides access to Eikon JavaScript libraries, UI controls, and data APIs for creating embe
  name: App Studio Web SDK
  slug: app-studio-web-sdk
- description: COM APIs for integrating Refinitiv Eikon data into Microsoft Office applications. Provides access to real-time market data, news, fundamental data, and analytics through Visual Basic for Applications,
  name: Eikon COM APIs for Microsoft Office
  slug: eikon-com-apis-for-microsoft-office
- description: .NET APIs for building custom standalone applications that access Refinitiv Eikon data including real-time market data, news, fundamentals, and time series. Requires the Eikon application running with
  name: Eikon .NET APIs
  slug: eikon-net-apis
- description: OAuth 2.0 token management for API access
  name: Refinitiv Eikon Authentication API
  slug: refinitiv-eikon-authentication-api
- description: Environmental, Social, and Governance data and scores
  name: Refinitiv Eikon ESG API
  slug: refinitiv-eikon-esg-api
- description: On-demand and managed data extractions
  name: Refinitiv Eikon Extractions API
  slug: refinitiv-eikon-extractions-api
- description: Extracted file management and download
  name: Refinitiv Eikon Files API
  slug: refinitiv-eikon-files-api
- description: Historical price data including interday and intraday summaries
  name: Refinitiv Eikon Historical Pricing API
  slug: refinitiv-eikon-historical-pricing-api
- description: Management of instrument lists for extractions
  name: Refinitiv Eikon Instrument Lists API
  slug: refinitiv-eikon-instrument-lists-api
- description: Extraction job management and status monitoring
  name: Refinitiv Eikon Jobs API
  slug: refinitiv-eikon-jobs-api
- description: Financial news headlines and stories from Reuters and other sources
  name: Refinitiv Eikon News API
  slug: refinitiv-eikon-news-api
- description: Immediate tick data extraction requests
  name: Refinitiv Eikon On-Demand Extractions API
  slug: refinitiv-eikon-on-demand-extractions-api
- description: Configuration of extraction report templates
  name: Refinitiv Eikon Report Templates API
  slug: refinitiv-eikon-report-templates-api
- description: Scheduled extraction management
  name: Refinitiv Eikon Schedules API
  slug: refinitiv-eikon-schedules-api
- description: Search across organizations, instruments, quotes, and indicators
  name: Refinitiv Eikon Search API
  slug: refinitiv-eikon-search-api
- description: Snapshot and streaming price data for financial instruments
  name: Refinitiv Eikon Streaming Pricing API
  slug: refinitiv-eikon-streaming-pricing-api
- description: Instrument identifier concordance and navigation
  name: Refinitiv Eikon Symbology API
  slug: refinitiv-eikon-symbology-api
arazzos:
- description: Authenticate, run an on-demand DataScope Select extraction, list produced files, and download one.
  name: Refinitiv Eikon DataScope Extraction and Download
  slug: refinitiv-eikon-datascope-extraction-download-workflow
- description: Resolve an instrument by search, pull its full ESG scores, then drill into detailed ESG measures.
  name: Refinitiv Eikon Instrument ESG Profile
  slug: refinitiv-eikon-instrument-esg-profile-workflow
- description: Search news headlines for a query, then fetch the full story body for the most recent match.
  name: Refinitiv Eikon News Headline to Story
  slug: refinitiv-eikon-news-headline-to-story-workflow
- description: Search for an instrument by free text, then pull the latest pricing snapshot for the top match.
  name: Refinitiv Eikon Search to Pricing Snapshot
  slug: refinitiv-eikon-search-to-snapshot-workflow
- description: Resolve an external instrument identifier to a RIC, then pull its historical interday pricing summaries.
  name: Refinitiv Eikon Symbol to Time Series
  slug: refinitiv-eikon-symbol-to-timeseries-workflow
- description: Authenticate, submit a tick history extraction, check the job status, and download the result when complete.
  name: Refinitiv Eikon Tick History Extraction and Poll
  slug: refinitiv-eikon-tickhistory-extraction-poll-workflow
artifact_total: 127
asyncapis:
- description: Standards-based WebSocket API providing real-time streaming market data using JSON message formats following the Open Message Model (OMM). Connects to Refinitiv Real-Time Distribution Systems (RTDS) a
  name: LSEG (Refinitiv) Real-Time WebSocket API
  slug: refinitiv-eikon-asyncapi
collections:
- collection_type: postman
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication API
  slug: postman-refinitiv-eikon-authentication-api
- collection_type: postman
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication ESG API
  slug: postman-refinitiv-eikon-esg-api
- collection_type: postman
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Extractions API
  slug: postman-refinitiv-eikon-extractions-api
- collection_type: postman
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Files API
  slug: postman-refinitiv-eikon-files-api
- collection_type: postman
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Historical Pricing API
  slug: postman-refinitiv-eikon-historical-pricing-api
- collection_type: postman
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Instrument Lists API
  slug: postman-refinitiv-eikon-instrument-lists-api
- collection_type: postman
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Jobs API
  slug: postman-refinitiv-eikon-jobs-api
- collection_type: postman
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication News API
  slug: postman-refinitiv-eikon-news-api
- collection_type: postman
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication On-Demand Extractions API
  slug: postman-refinitiv-eikon-on-demand-extractions-api
- collection_type: postman
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Report Templates API
  slug: postman-refinitiv-eikon-report-templates-api
- collection_type: postman
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Schedules API
  slug: postman-refinitiv-eikon-schedules-api
- collection_type: postman
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Search API
  slug: postman-refinitiv-eikon-search-api
- collection_type: postman
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Streaming Pricing API
  slug: postman-refinitiv-eikon-streaming-pricing-api
- collection_type: postman
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Symbology API
  slug: postman-refinitiv-eikon-symbology-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication API
  slug: open-refinitiv-eikon-authentication-api
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs
  slug: open-refinitiv-eikon-data-platform
- collection_type: open
  name: Refinitiv Eikon LSEG DataScope Select REST API
  slug: open-refinitiv-eikon-datascope-select
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication ESG API
  slug: open-refinitiv-eikon-esg-api
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Extractions API
  slug: open-refinitiv-eikon-extractions-api
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Files API
  slug: open-refinitiv-eikon-files-api
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Historical Pricing API
  slug: open-refinitiv-eikon-historical-pricing-api
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Instrument Lists API
  slug: open-refinitiv-eikon-instrument-lists-api
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Jobs API
  slug: open-refinitiv-eikon-jobs-api
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication News API
  slug: open-refinitiv-eikon-news-api
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication On-Demand Extractions API
  slug: open-refinitiv-eikon-on-demand-extractions-api
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Report Templates API
  slug: open-refinitiv-eikon-report-templates-api
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Schedules API
  slug: open-refinitiv-eikon-schedules-api
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Search API
  slug: open-refinitiv-eikon-search-api
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Streaming Pricing API
  slug: open-refinitiv-eikon-streaming-pricing-api
- collection_type: open
  name: Refinitiv Eikon Refinitiv Data Platform APIs Authentication Symbology API
  slug: open-refinitiv-eikon-symbology-api
- collection_type: open
  name: Refinitiv Eikon LSEG Tick History REST API
  slug: open-refinitiv-eikon-tick-history
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/refinitiv-eikon/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/refinitiv-eikon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/refinitiv-eikon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/refinitiv-eikon-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/refinitiv-eikon-datascope-extraction-download-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/refinitiv-eikon-instrument-esg-profile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/refinitiv-eikon-news-headline-to-story-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/refinitiv-eikon-search-to-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/refinitiv-eikon-symbol-to-timeseries-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/refinitiv-eikon-tickhistory-extraction-poll-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/refinitiv-eikon
- group: start
  title: ''
  type: Portal
  url: https://developers.lseg.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lseg.com/en/api-catalog
- group: start
  title: ''
  type: Signup
  url: https://developers.lseg.com/en/register
- group: start
  title: ''
  type: Login
  url: https://developers.lseg.com/en/login
- group: company
  title: ''
  type: Blog
  url: https://medium.com/lseg-developer-community
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/lseg-developer-community
- group: operate
  title: ''
  type: Community
  url: https://community.developers.refinitiv.com/
- group: operate
  title: ''
  type: Support
  url: https://my.refinitiv.com/content/mytr/en/helpandsupport.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.refinitiv.com/en/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.refinitiv.com/en/policies/privacy-statement
- group: operate
  title: ''
  type: StatusPage
  url: https://status.refinitiv.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LSEG-API-Samples
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Refinitiv/Real-Time-SDK
- group: build
  title: ''
  type: Developer Tools
  url: https://apidocs.refinitiv.com/Apps/ApiDocs
- group: operate
  title: ''
  type: ChangeLog
  url: https://community.developers.refinitiv.com/discussions
- group: start
  title: ''
  type: Console
  url: https://my.refinitiv.com
- group: company
  title: ''
  type: Website
  url: https://www.lseg.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/refinitiv-eikon-data-platform-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/refinitiv-eikon-datascope-select-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/refinitiv-eikon-tick-history-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/refinitiv-eikon-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/refinitiv-eikon-instrument-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/refinitiv-eikon-esg-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/refinitiv-eikon-data-platform-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/refinitiv-eikon-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/refinitiv-eikon-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/refinitiv-eikon-vocabulary.yml
created: '2024-01-01'
description: Refinitiv Eikon provides financial professionals with access to real-time market data, news, analytics, and trading capabilities. The Eikon Data API allows programmatic access to financial data including prices, fundamentals, reference data, and time series. Eikon was withdrawn from the LSEG product line on June 30, 2025, and has been succeeded by LSEG Workspace.
examples:
- key_count: 2
  name: Refinitiv Eikon Get Esg Scores Example
  slug: refinitiv-eikon-get-esg-scores-example
- key_count: 2
  name: Refinitiv Eikon Get Interday Pricing Example
  slug: refinitiv-eikon-get-interday-pricing-example
finops:
- name: Refinitiv Eikon Finops
  service_category: Market Data
  slug: refinitiv-eikon-finops
image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
json_schemas:
- name: Error
  property_count: 1
  slug: refinitiv-eikon-error
- name: Refinitiv Eikon ESG Score
  property_count: 9
  slug: refinitiv-eikon-esg
- name: EsgMeasuresResponse
  property_count: 1
  slug: refinitiv-eikon-esgmeasuresresponse
- name: EsgScoresResponse
  property_count: 1
  slug: refinitiv-eikon-esgscoresresponse
- name: ExtractedFile
  property_count: 6
  slug: refinitiv-eikon-extractedfile
- name: ExtractionJob
  property_count: 4
  slug: refinitiv-eikon-extractionjob
- name: ExtractionRequest
  property_count: 1
  slug: refinitiv-eikon-extractionrequest
- name: ExtractionResponse
  property_count: 4
  slug: refinitiv-eikon-extractionresponse
- name: ExtractionWithNotesResponse
  property_count: 3
  slug: refinitiv-eikon-extractionwithnotesresponse
- name: HistoricalPricingResponse
  property_count: 1
  slug: refinitiv-eikon-historicalpricingresponse
- name: Refinitiv Eikon Financial Instrument
  property_count: 11
  slug: refinitiv-eikon-instrument
- name: InstrumentList
  property_count: 3
  slug: refinitiv-eikon-instrumentlist
- name: InstrumentSearchResult
  property_count: 5
  slug: refinitiv-eikon-instrumentsearchresult
- name: NewsHeadline
  property_count: 5
  slug: refinitiv-eikon-newsheadline
- name: NewsHeadlinesResponse
  property_count: 2
  slug: refinitiv-eikon-newsheadlinesresponse
- name: NewsStory
  property_count: 8
  slug: refinitiv-eikon-newsstory
- name: PricingDataPoint
  property_count: 8
  slug: refinitiv-eikon-pricingdatapoint
- name: PricingSnapshotResponse
  property_count: 1
  slug: refinitiv-eikon-pricingsnapshotresponse
- name: ReportTemplate
  property_count: 4
  slug: refinitiv-eikon-reporttemplate
- name: Schedule
  property_count: 5
  slug: refinitiv-eikon-schedule
- name: SearchRequest
  property_count: 7
  slug: refinitiv-eikon-searchrequest
- name: SearchResponse
  property_count: 2
  slug: refinitiv-eikon-searchresponse
- name: SymbologyLookupRequest
  property_count: 3
  slug: refinitiv-eikon-symbologylookuprequest
- name: SymbologyLookupResponse
  property_count: 1
  slug: refinitiv-eikon-symbologylookupresponse
- name: TickHistoryExtractionRequest
  property_count: 1
  slug: refinitiv-eikon-tickhistoryextractionrequest
- name: TickHistoryExtractionResponse
  property_count: 3
  slug: refinitiv-eikon-tickhistoryextractionresponse
- name: TokenResponse
  property_count: 5
  slug: refinitiv-eikon-tokenresponse
json_structures:
- name: Refinitiv Eikon Data Platform Structure
  property_count: 0
  slug: refinitiv-eikon-data-platform-structure
- name: Refinitiv Eikon Structure
  property_count: 0
  slug: refinitiv-eikon-structure
jsonld:
- class_count: 6
  name: Refinitiv Eikon Context
  property_count: 17
  slug: refinitiv-eikon-context
layout: provider
modified: '2026-05-29'
name: Refinitiv Eikon
nav: Providers
network: true
overview: 'Refinitiv Eikon publishes 15 APIs on the [APIs.io](https://apis.io/) network, including LSEG WebSocket API, Authentication API, ESG API, and 12 more. Tagged areas include Analytics, Financial Data, Financial News, Market Data, and Real-Time Data.


  The Refinitiv Eikon catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Refinitiv Eikon''s developer surface includes authentication, developer portal, getting-started guide, documentation, signup flow, engineering blog, support, and 32 more developer resources.'
plans:
- name: Refinitiv Eikon Plans Pricing
  plan_count: 1
  slug: refinitiv-eikon-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 1
  name: Refinitiv Eikon Rate Limits
  slug: refinitiv-eikon-rate-limits
rules:
- name: Refinitiv Eikon API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: refinitiv-eikon-asyncapi-spectral-rules
- name: Refinitiv Eikon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: refinitiv-eikon-jsonschema-spectral-rules
- name: Refinitiv Eikon API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 6
  slug: refinitiv-eikon-rules
score:
  band: strong
  composite: 57.9
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 75.6
    developer_ergonomics: 56.5
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/refinitiv-eikon/refs/heads/main/screenshots/refinitiv-eikon-2026-06-20T192745.png
security:
- kind: authentication
  name: Refinitiv Eikon Authentication
  slug: refinitiv-eikon-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Refinitiv Eikon Domain Security
  slug: refinitiv-eikon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: refinitiv-eikon
tags:
- Analytics
- Financial Data
- Financial News
- Market Data
- Real-Time Data
- Trading
website: https://www.lseg.com
---
