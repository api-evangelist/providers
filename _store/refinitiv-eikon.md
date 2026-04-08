---
aid: refinitiv-eikon
url: https://raw.githubusercontent.com/api-evangelist/refinitiv-eikon/refs/heads/main/apis.yml
apis:
- name: Eikon Data API
  description: Python and R library that allows programmatic access to Refinitiv Eikon data. Provides access to instrument pricing, fundamentals, estimates, time series, news, and symbology. Requires the Eikon or LSEG Workspace desktop application to be running for data access.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/products/eikon-icon.png
  humanURL: https://developers.lseg.com/en/api-catalog/eikon/eikon-data-api
  baseURL: https://api.refinitiv.com
  tags:
  - Financial Data
  - Market Data
  - Python
  - Time Series
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/eikon/eikon-data-api/documentation
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/eikon/eikon-data-api/quick-start
  - type: Tutorials
    url: https://developers.lseg.com/en/api-catalog/eikon/eikon-data-api/tutorials
  - type: Downloads
    url: https://developers.lseg.com/en/api-catalog/eikon/eikon-data-api/download
  - type: GitHubRepository
    url: https://github.com/LSEG-API-Samples/Tutorial.EikonAPI.Python.Streaming
- name: Refinitiv Data Platform APIs
  description: RESTful APIs providing access to Refinitiv's comprehensive financial data including pricing, ESG data, news, research, alternative data, and streaming services. The platform serves as the central hub for programmatic access to LSEG content.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis
  baseURL: https://api.refinitiv.com
  tags:
  - ESG
  - Market Data
  - News
  - REST API
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis/documentation
  - type: OpenAPI
    url: https://api.refinitiv.com/streaming-pricing/docs/swagger.yaml
  - type: Authentication
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis/tutorials#authorization-all
  - type: Developer Tools
    url: https://apidocs.refinitiv.com/Apps/ApiDocs
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis/quick-start
  - type: Tutorials
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis/tutorials
  - type: Downloads
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis/download
- name: LSEG Messenger Bot SDK
  description: SDK for building intelligent, compliant messaging bots within the LSEG Messenger platform. Enables sending, receiving, and replying to messages in one-to-one and group chat contexts with full OAuth 2.0 authentication and audit trail compliance.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/lseg-messenger-bot-sdk/lseg-messenger-bot-sdk
  baseURL: https://api.refinitiv.com
  tags:
  - Chatbot
  - Collaboration
  - Compliance
  - Messaging
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/lseg-messenger-bot-sdk/lseg-messenger-bot-sdk/documentation
- name: Messenger Side by Side API
  description: API allowing external applications to connect with and pass information into LSEG Messenger. Requires user interaction and enables integration of third-party applications alongside the messenger for collaborative workflows.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/messenger-api/messenger-side-by-side-api
  baseURL: https://api.refinitiv.com
  tags:
  - Collaboration
  - Integration
  - Messaging
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/messenger-api/messenger-side-by-side-api/documentation
- name: Refinitiv Data Library for Python
  description: Python library providing uniform, ease-of-use interfaces for accessing the breadth and depth of financial data and services on the LSEG Data Platform. Returns data as Pandas DataFrames and supports both streaming and non-streaming data services.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python
  baseURL: https://api.refinitiv.com
  tags:
  - Data Library
  - Financial Data
  - Python
  - SDK
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/documentation
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/quick-start/getting-started-with-python
  - type: GitHubRepository
    url: https://github.com/LSEG-API-Samples/Example.DataLibrary.Python
- name: Refinitiv Data Library for TypeScript
  description: TypeScript and JavaScript library providing ease-of-use interfaces for accessing financial data and services on the Refinitiv Data Platform. Supports both streaming and non-streaming data services for web and Node.js applications.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-typescript
  baseURL: https://api.refinitiv.com
  tags:
  - Data Library
  - JavaScript
  - SDK
  - TypeScript
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-typescript/documentation
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-typescript/quick-start
  - type: Tutorials
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-typescript/tutorials
- name: Refinitiv Data Library for .NET
  description: .NET library providing uniform interfaces for accessing the Refinitiv Data Platform. Supports streaming and non-streaming data services for C# and other .NET languages, rebranded as LSEG Data Library for .NET.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for--net
  baseURL: https://api.refinitiv.com
  tags:
  - .NET
  - C#
  - Data Library
  - SDK
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for--net/documentation
- name: Datastream Web Service API
  description: API providing access to Datastream content, the world's leading time series database, via SOAP/XML and REST/JSON protocols. Enables strategists, economists, and research communities to access comprehensive financial information with histories back to the 1900s, covering over 48 million financial instruments.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/eikon/datastream-web-service
  baseURL: https://product.datastream.com
  tags:
  - Financial Data
  - Historical Data
  - SOAP
  - Time Series
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/eikon/datastream-web-service/Documents
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/eikon/datastream-web-service/Quickstart
  - type: Tutorials
    url: https://developers.lseg.com/en/api-catalog/eikon/datastream-web-service/Tutorials
  - type: Downloads
    url: https://developers.lseg.com/en/api-catalog/eikon/datastream-web-service/download
  - type: GitHubRepository
    url: https://github.com/datastreamapi/DatastreamPy
- name: LSEG WebSocket API
  description: Standards-based WebSocket API for real-time pricing streaming using JSON message formats. Connects to Real-Time Distribution Systems and Real-Time Optimized cloud solutions for data consumption, contribution, and posting across Python, R, .NET, and other platforms.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/websocket-api
  baseURL: wss://api.refinitiv.com
  tags:
  - Market Data
  - Real-Time
  - Streaming
  - WebSocket
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/websocket-api/documentation
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/websocket-api/quick-start
  - type: Tutorials
    url: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/websocket-api/tutorials
  - type: GitHubRepository
    url: https://github.com/Refinitiv/websocket-api
- name: Real-Time Java SDK
  description: Java SDK encompassing the Enterprise Message API (EMA) and Enterprise Transport API (ETA) for building high-performance real-time data applications. Provides consumer, provider, and publisher features for real-time market data streaming.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/rt-sdk-java
  baseURL: https://api.refinitiv.com
  tags:
  - Java
  - Real-Time
  - SDK
  - Streaming
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/rt-sdk-java/documentation
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/rt-sdk-java/quick-start
  - type: GitHubRepository
    url: https://github.com/Refinitiv/Real-Time-SDK
- name: Real-Time C/C++ SDK
  description: C and C++ SDK providing the Enterprise Message API (EMA) and Enterprise Transport API (ETA) for ultra-low-latency, high-throughput real-time data applications. The ETA foundation enables the highest performance with minimal memory and CPU utilization.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/rt-sdk-cc
  baseURL: https://api.refinitiv.com
  tags:
  - C++
  - Low Latency
  - Real-Time
  - SDK
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/rt-sdk-cc/documentation
  - type: GitHubRepository
    url: https://github.com/Refinitiv/Real-Time-SDK
- name: Real-Time C# SDK
  description: C# SDK providing the Enterprise Transport API (ETA) for building high-performance real-time data applications on .NET. Supports consuming, providing, and publishing real-time content using the Open Message Model.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/rt-sdk-csharp
  baseURL: https://api.refinitiv.com
  tags:
  - .NET
  - C#
  - Real-Time
  - SDK
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/rt-sdk-csharp/documentation
  - type: GitHubRepository
    url: https://github.com/Refinitiv/Real-Time-SDK
- name: Eikon Side by Side Interoperability API
  description: Web API for integrating standalone desktop applications with Refinitiv Eikon to create dynamic custom workflows. Enables launching Eikon apps programmatically and exchanging context such as portfolios, trade tickets, and instrument identifiers between applications.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/eikon/side-by-side-integration
  baseURL: https://api.refinitiv.com
  tags:
  - Deprecated
  - Desktop Integration
  - Interoperability
  - Workflow
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/eikon/side-by-side-integration/documentation
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/eikon/side-by-side-integration/quick-start
  - type: Deprecation Notice
    url: https://developers.lseg.com/en/api-catalog/eikon/side-by-side-integration
- name: Workspace Web Side by Side API
  description: API enabling interoperability and context passing between LSEG Workspace Web and external web applications within the same browser instance. Supports authentication, metadata exchange, and navigation between Workspace and third-party web apps.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/eikon/workspace-web-side-by-side-api
  baseURL: https://api.refinitiv.com
  tags:
  - Desktop Integration
  - Interoperability
  - Web
  - Workspace
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/eikon/workspace-web-side-by-side-api/documentation
- name: Workspace SDK
  description: End-to-end financial application development kit for designing GUI applications, powering them with market data, and integrating workflow logic into LSEG Workspace. Provides UI components, data integration, and workflow capabilities for building web-based financial applications.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/workspace-sdk/workspace-sdk
  baseURL: https://api.refinitiv.com
  tags:
  - Application Development
  - SDK
  - UI Components
  - Workspace
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/workspace-sdk/workspace-sdk/documentation
- name: LSEG DataScope Select REST API
  description: REST API providing programmatic access to the DataScope Select platform for extracting global prices, corporate actions, reference data, historical data, cross-reference data, and entity data. Supports flexible extraction scheduling with increased instrument limits compared to the SOAP API.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/datascope-select/datascope-select-rest-api
  baseURL: https://selectapi.datascope.refinitiv.com/RestApi/v1
  tags:
  - Corporate Actions
  - Data Extraction
  - Reference Data
  - REST API
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/datascope-select/datascope-select-rest-api/documentation
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/datascope-select/datascope-select-rest-api/quick-start
  - type: Tutorials
    url: https://developers.lseg.com/en/api-catalog/datascope-select/datascope-select-rest-api/tutorials
- name: LSEG Tick History REST API
  description: REST API providing programmatic access to historical tick-level market data through the DataScope Select platform. Supports on-demand and scheduled extractions of tick data, intraday bars, and end-of-day data across global markets. Also available via Google BigQuery on GCP.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-tick-history/refinitiv-tick-history-rth-rest-api
  baseURL: https://selectapi.datascope.refinitiv.com/RestApi/v1
  tags:
  - Historical Data
  - Market Data
  - REST API
  - Tick Data
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/refinitiv-tick-history/refinitiv-tick-history-rth-rest-api/documentation
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/refinitiv-tick-history/refinitiv-tick-history-rth-rest-api/quick-start
  - type: Tutorials
    url: https://developers.lseg.com/en/api-catalog/refinitiv-tick-history/refinitiv-tick-history-rth-rest-api/tutorials
- name: PermID Entity Search API
  description: RESTful API for searching and discovering organizations, equity instruments, and equity quotes using PermID identifiers. Supports searching by name, ticker, RIC, LEI, and other standard identifiers across approximately 13 million organizations and 3 million equity quotes.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/open-perm-id/permid-entity-search
  baseURL: https://api-eit.refinitiv.com/permid/search
  tags:
  - Entity Search
  - Identifiers
  - Open Data
  - Symbology
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/open-perm-id/permid-entity-search/documentation
  - type: Tutorials
    url: https://developers.lseg.com/en/api-catalog/open-perm-id/permid-entity-search/tutorials
- name: PermID Record Matching API
  description: RESTful API for matching unstructured entity records to PermID identifiers. Enables concordance by mapping external entity data to LSEG permanent identifiers for organizations and instruments.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/open-perm-id/permid-record-matching-restful-api
  baseURL: https://api-eit.refinitiv.com/permid/match
  tags:
  - Concordance
  - Entity Matching
  - Identifiers
  - Open Data
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/open-perm-id/permid-record-matching-restful-api/documentation
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/open-perm-id/permid-record-matching-restful-api/quick-start
- name: Intelligent Tagging API
  description: RESTful API for extracting entities, topics, and metadata from unstructured text content. Identifies organizations, people, instruments, and other financial entities within documents using natural language processing.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/open-perm-id/intelligent-tagging-restful-api
  baseURL: https://api-eit.refinitiv.com/permid/calais
  tags:
  - Entity Extraction
  - NLP
  - Tagging
  - Text Analytics
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/open-perm-id/intelligent-tagging-restful-api/documentation
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/open-perm-id/intelligent-tagging-restful-api/quick-start
- name: Refinitiv Knowledge Direct API
  description: Web services API integrating financial market data, news, and analytics into websites, trading platforms, advisory portals, and mobile applications. Delivers pricing, news, fundamental data, consensus estimates, Lipper fund data, and StockReports through SOAP and XML protocols.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-knowledge-direct/refinitiv-knowledge-direct-api-rkd-api
  baseURL: https://api.rkd.refinitiv.com
  tags:
  - Market Data
  - Portals
  - SOAP
  - Wealth Management
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/refinitiv-knowledge-direct/refinitiv-knowledge-direct-api-rkd-api/documentation
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/refinitiv-knowledge-direct/refinitiv-knowledge-direct-api-rkd-api/quick-start
  - type: Tutorials
    url: https://developers.lseg.com/en/api-catalog/refinitiv-knowledge-direct/refinitiv-knowledge-direct-api-rkd-api/tutorials
  - type: Downloads
    url: https://developers.lseg.com/en/api-catalog/refinitiv-knowledge-direct/refinitiv-knowledge-direct-api-rkd-api/download
- name: Symbology API
  description: Discovery Symbology API for concordance, navigation, and discovery of financial content. Enables mapping from external identifiers to LSEG PermIDs and navigating between a wide range of identifier types. Available at no additional cost to Data Platform subscribers.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/symbology-API
  baseURL: https://api.refinitiv.com
  tags:
  - Concordance
  - Identifiers
  - Reference Data
  - Symbology
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/symbology-API/documentation
- name: Search API
  description: API enabling search across organizations, instruments, quotes, and economic indicators on the Refinitiv Data Platform. Part of the Search Light family of APIs for wealth management applications.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/search-API
  baseURL: https://api.refinitiv.com
  tags:
  - Discovery
  - Instruments
  - Search
  - Wealth Management
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/search-API/documentation
- name: Research API
  description: API built on the Refinitiv Data Platform providing streamlined access to real-time and historical sell-side research reports. Serves as the aggregate delivery system for providing buy-side institutions with entitled research content.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/research-API
  baseURL: https://api.refinitiv.com
  tags:
  - Buy-Side
  - Reports
  - Research
  - Sell-Side
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/research-API/documentation
- name: News API for Wealth
  description: API providing access to financial news content for wealth management applications. Delivers real-time and historical news from Reuters and other sources through the Refinitiv Data Platform.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/news-API
  baseURL: https://api.refinitiv.com
  tags:
  - Financial News
  - News
  - Wealth Management
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/news-API/documentation
- name: Funds API for Wealth
  description: API providing access to Lipper fund data for wealth management applications. Delivers fund performance, classifications, ratings, and other mutual fund data through the Refinitiv Data Platform.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/lipper-funds-API
  baseURL: https://api.refinitiv.com
  tags:
  - Funds
  - Lipper
  - Performance
  - Wealth Management
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/lipper-funds-API/documentation
- name: Estimates API for Wealth
  description: API providing access to consensus estimates data for wealth management applications. Delivers analyst estimates, recommendations, and forecasts through the Refinitiv Data Platform.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/estimates-API
  baseURL: https://api.refinitiv.com
  tags:
  - Consensus
  - Estimates
  - Forecasts
  - Wealth Management
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/estimates-API/documentation
- name: Ownership API for Wealth
  description: API providing access to institutional and fund ownership data for wealth management applications. Delivers ownership holdings, stakes, and shareholder information through the Refinitiv Data Platform.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/ownership-API
  baseURL: https://api.refinitiv.com
  tags:
  - Holdings
  - Ownership
  - Shareholders
  - Wealth Management
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/ownership-API/documentation
- name: Filings API
  description: API providing access to regulatory filings data through the Refinitiv Data Platform. Delivers SEC filings, annual reports, and other regulatory documents for financial analysis and compliance workflows.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/filings-API
  baseURL: https://api.refinitiv.com
  tags:
  - Compliance
  - Filings
  - Regulatory
  - SEC
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/filings-API/documentation
- name: World-Check One API
  description: Workflow-based REST/JSON API for screening entities against the World-Check risk intelligence database. Supports due diligence in the fight against financial crime, bribery, and corruption by enabling checks against sanctions, PEPs, and reputational risk data.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/world-check-one-api
  baseURL: https://rms-world-check-one-api.thomsonreuters.com
  tags:
  - AML
  - Compliance
  - Risk
  - Screening
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/world-check-one-api/documentation
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/world-check-one-api/quick-start
- name: World-Check Verify API
  description: Cloud-native, stateless screening API purpose-built for real-time, low-latency screening of individuals and entities in modern payment workflows. Screens against World-Check risk intelligence data and client proprietary lists via REST/JSON over HTTPS.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/world-check-verify
  baseURL: https://api.refinitiv.com
  tags:
  - Compliance
  - Payments
  - Real-Time
  - Screening
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/world-check-verify/documentation
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/world-check-verify/quick-start
- name: App Studio Web SDK
  description: Web SDK for building custom applications using HTML5 and JavaScript within the Eikon App Studio environment. Provides access to Eikon JavaScript libraries, UI controls, and data APIs for creating embedded financial applications.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/app-studio/app-studio-web-sdk
  baseURL: https://api.refinitiv.com
  tags:
  - App Development
  - Embedded Apps
  - HTML5
  - JavaScript
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/app-studio/app-studio-web-sdk/documentation
- name: Eikon COM APIs for Microsoft Office
  description: COM APIs for integrating Refinitiv Eikon data into Microsoft Office applications. Provides access to real-time market data, news, fundamental data, and analytics through Visual Basic for Applications, VB, C++, and other COM-compatible languages.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/eikon/com-apis-for-use-in-microsoft-office
  baseURL: https://api.refinitiv.com
  tags:
  - COM
  - Deprecated
  - Microsoft Office
  - VBA
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/eikon/com-apis-for-use-in-microsoft-office/documentation
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog/eikon/com-apis-for-use-in-microsoft-office/quick-start
  - type: Tutorials
    url: https://developers.lseg.com/en/api-catalog/eikon/com-apis-for-use-in-microsoft-office/tutorials
  - type: Downloads
    url: https://developers.lseg.com/en/api-catalog/eikon/com-apis-for-use-in-microsoft-office/download
  - type: Deprecation Notice
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-libraries
- name: Eikon .NET APIs
  description: .NET APIs for building custom standalone applications that access Refinitiv Eikon data including real-time market data, news, fundamentals, and time series. Requires the Eikon application running with a signed-in user. 32-bit edition only.
  image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
  humanURL: https://developers.lseg.com/en/api-catalog/eikon/-net-apis-for-use-in-custom-applications
  baseURL: https://api.refinitiv.com
  tags:
  - .NET
  - Custom Applications
  - Deprecated
  - Desktop
  properties:
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog/eikon/-net-apis-for-use-in-custom-applications/documentation
  - type: Deprecation Notice
    url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-libraries
name: Refinitiv Eikon
tags:
- Analytics
- Financial Data
- Financial News
- Market Data
- Real-Time Data
- Trading
type: Contract
image: https://www.refinitiv.com/content/dam/marketing/en_us/images/logos/refinitiv-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Refinitiv Eikon provides financial professionals with access to real-time market data, news, analytics, and trading capabilities. The Eikon Data API allows programmatic access to financial data including prices, fundamentals, reference data, and time series. Eikon was withdrawn from the LSEG product line on June 30, 2025, and has been succeeded by LSEG Workspace.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

