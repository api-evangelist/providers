---
aid: refinitiv
name: Refinitiv
description: Refinitiv, an LSEG (London Stock Exchange Group) business, provides financial market data, infrastructure, and analytics to businesses and financial professionals worldwide.
type: Index
image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
url: https://raw.githubusercontent.com/api-evangelist/refinitiv/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-03-16'
specificationVersion: '0.19'
apis:
  - name: Refinitiv Data Platform (RDP) API
    description: Cloud-enabled RESTful API providing access to streaming and non-streaming financial data, news, research, and analytics. It serves as the primary programmatic interface to the breadth of Refinitiv content on the LSEG Data Platform.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis
    baseURL: https://api.refinitiv.com
    tags:
      - Analytics
      - Financial Data
      - Market Data
      - Streaming
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis/quick-start
      - type: Tutorials
        url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis/tutorials
      - type: Downloads
        url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis/download
      - type: API Playground
        url: https://apidocs.refinitiv.com/Apps/ApiDocs
      - type: Pricing
        url: https://www.lseg.com/en/data-analytics/financial-data
      - type: OpenAPI
        url: openapi/refinitiv-data-platform-openapi.yml
  - name: Refinitiv Data Library for Python
    description: Python library providing uniform access to the breadth and depth of financial data and services available on the LSEG Data Platform. It offers ease-of-use interfaces for streaming and non-streaming data, and can be used from within LSEG Workspace, through the Data Platform, or deployed on-premise.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
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
        url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/quick-start
      - type: Tutorials
        url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python/tutorials
      - type: GitHub Repository
        url: https://github.com/LSEG-API-Samples/Example.DataLibrary.Python
  - name: Refinitiv Data Library for .NET
    description: .NET library providing uniform access to financial data and services available on the LSEG Data Platform. It supports streaming and non-streaming data retrieval and integrates with LSEG Workspace, the Data Platform, and on-premise deployed infrastructure.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for--net
    baseURL: https://api.refinitiv.com
    tags:
      - .NET
      - Data Library
      - Financial Data
      - SDK
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for--net/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for--net/quick-start
  - name: Refinitiv Data Platform Libraries
    description: Suite of ease-of-use libraries and interfaces for Python, TypeScript and JavaScript providing access to streaming and non-streaming data services on the LSEG Data Platform. These libraries have been superseded by the newer Refinitiv Data Libraries for new development.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-libraries
    baseURL: https://api.refinitiv.com
    tags:
      - Financial Data
      - JavaScript
      - Libraries
      - SDK
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-libraries/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-libraries/quick-start
      - type: Tutorials
        url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-libraries/tutorials
  - name: Eikon Data API
    description: Python library providing access to financial data, news, and symbology from within the Refinitiv Eikon or LSEG Workspace desktop application. It enables Eikon end users to access data programmatically from their desktop session.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/eikon/eikon-data-api
    baseURL: https://api.refinitiv.com
    tags:
      - Desktop
      - Eikon
      - Financial Data
      - Python
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/eikon/eikon-data-api/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/eikon/eikon-data-api/quick-start
      - type: Tutorials
        url: https://developers.lseg.com/en/api-catalog/eikon/eikon-data-api/tutorials
      - type: Downloads
        url: https://developers.lseg.com/en/api-catalog/eikon/eikon-data-api/download
  - name: Refinitiv Real-Time WebSocket API
    description: Low-latency streaming API for real-time market data using WebSocket connections. It supports the Open Message Model (OMM) and allows applications to connect directly to Refinitiv Real-Time distribution systems or the LSEG Data Platform for streaming data.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-real-time-opnsrc/refinitiv-websocket-api
    baseURL: wss://api.refinitiv.com
    tags:
      - Market Data
      - Real-Time
      - Streaming
      - WebSocket
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/refinitiv-real-time-opnsrc/refinitiv-websocket-api/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/refinitiv-real-time-opnsrc/refinitiv-websocket-api/quick-start
      - type: Tutorials
        url: https://developers.lseg.com/en/api-catalog/refinitiv-real-time-opnsrc/refinitiv-websocket-api/tutorials
      - type: Downloads
        url: https://developers.lseg.com/en/api-catalog/refinitiv-real-time-opnsrc/refinitiv-websocket-api/download
      - type: AsyncAPI
        url: asyncapi/refinitiv-real-time-websocket-asyncapi.yml
  - name: Refinitiv Real-Time SDK - Java
    description: Open source Java SDK for the Refinitiv Real-Time platform, containing the Enterprise Message API (EMA) for ease-of-use rapid development and the Enterprise Transport API (ETA) for low-level, high-performance access to real-time streaming market data.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
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
      - type: Tutorials
        url: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/rt-sdk-java/tutorials
      - type: Downloads
        url: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/rt-sdk-java/download
      - type: GitHub Repository
        url: https://github.com/Refinitiv/Real-Time-SDK
  - name: Refinitiv Real-Time SDK - C/C++
    description: Open source C/C++ SDK for the Refinitiv Real-Time platform, providing the Enterprise Message API (EMA) and Enterprise Transport API (ETA) for building high-performance, low-latency applications that consume and contribute real-time market data.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/rt-sdk-cc
    baseURL: https://api.refinitiv.com
    tags:
      - C++
      - Real-Time
      - SDK
      - Streaming
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/rt-sdk-cc/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/real-time-opnsrc/rt-sdk-cc/quick-start
      - type: GitHub Repository
        url: https://github.com/Refinitiv/Real-Time-SDK
  - name: Refinitiv News API
    description: Access to comprehensive news content from Refinitiv including real-time and historical news articles, Machine Readable News (MRN), and news analytics delivered through the Refinitiv Data Platform.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis
    baseURL: https://api.refinitiv.com
    tags:
      - Content
      - Media
      - News
      - Research
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis/documentation
      - type: Tutorials
        url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis/tutorials
  - name: Refinitiv ESG API
    description: Access to environmental, social, and governance (ESG) data, scores, and analytics for sustainable investing. The API provides ESG scores, carbon emissions data, green revenue metrics, and controversy tracking across thousands of companies.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis
    baseURL: https://api.refinitiv.com
    tags:
      - Analytics
      - Environmental
      - ESG
      - Sustainability
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-platform-apis/documentation
      - type: Pricing
        url: https://www.lseg.com/en/data-analytics/sustainable-finance/esg-scores
  - name: LSEG DataScope Select - REST API
    description: Internet-hosted REST API for programmatic access to global pricing, corporate actions, reference data, historical data, cross-reference, and entity data. It provides fully automated extraction workflows and batch processing capabilities for large-scale data retrieval.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/datascope-select/datascope-select-rest-api
    baseURL: https://selectapi.datascope.lseg.com/RestApi/v1
    tags:
      - Data Extraction
      - Historical Data
      - Pricing
      - Reference Data
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/datascope-select/datascope-select-rest-api/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/datascope-select/datascope-select-rest-api/quick-start
      - type: Tutorials
        url: https://developers.lseg.com/en/api-catalog/datascope-select/datascope-select-rest-api/tutorials
      - type: Downloads
        url: https://developers.lseg.com/en/api-catalog/datascope-select/datascope-select-rest-api/download
      - type: OpenAPI
        url: openapi/refinitiv-datascope-select-openapi.yml
  - name: LSEG DataScope Select - SOAP API
    description: SOAP-based web service API for DataScope Select, providing extraction functionality for global pricing, reference, and historical data. Clients are encouraged to migrate to the REST API for new development, as all future functionality will be designed around REST.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/datascope-select/datascope-select-soap-api
    baseURL: https://selectapi.datascope.lseg.com
    tags:
      - Data Extraction
      - Legacy
      - Reference Data
      - SOAP
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/datascope-select/datascope-select-soap-api/documentation
      - type: Downloads
        url: https://developers.lseg.com/en/api-catalog/datascope-select/datascope-select-soap-api/download
  - name: LSEG Tick History REST API
    description: REST API providing access to historical high-frequency timestamped tick data across all global asset classes dating back to 1996. It supports custom reporting and Venue by Day standard reporting for complete trading data extraction.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-tick-history/refinitiv-tick-history-rth-rest-api
    baseURL: https://selectapi.datascope.lseg.com/RestApi/v1
    tags:
      - High Frequency
      - Historical Data
      - Tick Data
      - Trading
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/refinitiv-tick-history/refinitiv-tick-history-rth-rest-api/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/refinitiv-tick-history/refinitiv-tick-history-rth-rest-api/quick-start
      - type: Tutorials
        url: https://developers.lseg.com/en/api-catalog/refinitiv-tick-history/refinitiv-tick-history-rth-rest-api/tutorials
      - type: Downloads
        url: https://developers.lseg.com/en/api-catalog/refinitiv-tick-history/refinitiv-tick-history-rth-rest-api/download
  - name: Datastream Web Service API
    description: API providing access to Datastream, the world's leading time series database with histories back to the 1900s and over 48 million individual instruments or indicators. Available via SOAP, REST (JSON/XML), and .NET library interfaces for Python, R, MATLAB, and EViews.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/eikon/datastream-web-service
    baseURL: https://product.datastream.com
    tags:
      - Datastream
      - Economic Data
      - Historical Data
      - Time Series
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/eikon/datastream-web-service/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/eikon/datastream-web-service/quick-start
      - type: Tutorials
        url: https://developers.lseg.com/en/api-catalog/eikon/datastream-web-service/tutorials
      - type: Downloads
        url: https://developers.lseg.com/en/api-catalog/eikon/datastream-web-service/download
  - name: World-Check One API
    description: RESTful API for integrating LSEG World-Check screening capabilities into existing workflows and internal systems. It enables automated customer and third-party screening for onboarding, KYC, and due diligence processes against the World-Check risk intelligence database.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/world-check-one-api
    baseURL: https://api.refinitiv.com
    tags:
      - Compliance
      - KYC
      - Risk Intelligence
      - Screening
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/world-check-one-api/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/world-check-one-api/quick-start
      - type: Downloads
        url: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/world-check-one-api/download
      - type: OpenAPI
        url: openapi/refinitiv-world-check-one-openapi.yml
  - name: Qual-ID API
    description: RESTful API for automating identity verification and document verification processes. It helps organizations comply with regulations and identify potential financial crime using trusted and vetted data sources with normalized data fields.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/qual-id-api
    baseURL: https://api.refinitiv.com/verification/v1
    tags:
      - Compliance
      - Document Verification
      - Identity Verification
      - KYC
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/qual-id-api/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/customer-and-third-party-screening/qual-id-api/quick-start
      - type: OpenAPI
        url: openapi/refinitiv-qual-id-openapi.yml
  - name: LSEG Due Diligence Portal API
    description: REST API enabling clients to place orders for LSEG Due Diligence Reports from within their own internal systems and onboarding platforms. It uses OAuth2 for security and follows the OpenAPI 3 standard for documentation.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/lseg-due-diligence/lseg-due-diligence-reports-api
    baseURL: https://api.refinitiv.com
    tags:
      - Compliance
      - Due Diligence
      - Risk
      - Screening
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/lseg-due-diligence/lseg-due-diligence-reports-api/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/lseg-due-diligence/lseg-due-diligence-reports-api/quick-start
  - name: Refinitiv Knowledge Direct API (RKD)
    description: API for wealth management that provides access to Refinitiv hosted content and capabilities. It integrates into advisor solutions, customer-facing investment portals, and online trading platforms through a suite of endpoints for pricing, news, referential data, and specialized services.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/refinitiv-knowledge-direct/refinitiv-knowledge-direct-api-rkd-api
    baseURL: https://api.rkd.refinitiv.com
    tags:
      - Financial Data
      - News
      - Pricing
      - Wealth Management
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/refinitiv-knowledge-direct/refinitiv-knowledge-direct-api-rkd-api/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/refinitiv-knowledge-direct/refinitiv-knowledge-direct-api-rkd-api/quick-start
      - type: API Playground
        url: https://support-portal.rkd.refinitiv.com/
  - name: PermID Entity Search API
    description: RESTful API enabling search of entities by name, ticker, or RIC to return PermIDs, or use PermIDs to retrieve entity information. PermID is an open and free entity identification scheme that provides a unique identifier for organizations, instruments, and quotes.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/open-perm-id/permid-entity-search
    baseURL: https://api-eit.refinitiv.com
    tags:
      - Entity Search
      - Open Data
      - PermID
      - Symbology
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/open-perm-id/permid-entity-search/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/open-perm-id/permid-entity-search/quick-start
      - type: Website
        url: https://permid.org/
      - type: OpenAPI
        url: openapi/refinitiv-permid-entity-search-openapi.yml
  - name: Intelligent Tagging RESTful API
    description: Natural language processing API that identifies and tags entities such as companies, people, deals, geographical locations, industries, and events within unstructured text. It maps recognized entities to Refinitiv PermIDs for unambiguous identification and linking across documents.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/open-perm-id/intelligent-tagging-restful-api
    baseURL: https://api-eit.refinitiv.com
    tags:
      - Entity Recognition
      - NLP
      - Tagging
      - Text Analytics
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/open-perm-id/intelligent-tagging-restful-api/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/open-perm-id/intelligent-tagging-restful-api/quick-start
  - name: Workspace SDK
    description: End-to-end financial application development kit that allows developers to design a GUI, power it with market data, and integrate logic into workflows. It enables creation of web-based financial applications that run side by side with LSEG Workspace.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/workspace-sdk/workspace-sdk
    baseURL: https://api.refinitiv.com
    tags:
      - Application Development
      - Desktop
      - SDK
      - Workspace
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/workspace-sdk/workspace-sdk/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/workspace-sdk/workspace-sdk/quick-start
      - type: Tutorials
        url: https://developers.lseg.com/en/api-catalog/workspace-sdk/workspace-sdk/tutorials
  - name: Workspace Web Side by Side API
    description: Interoperability API that connects client web applications to LSEG Workspace Web. It allows applications to authenticate, connect to a running Workspace instance in the same browser, and exchange metadata such as active RICs between applications.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/eikon/workspace-web-side-by-side-api
    baseURL: https://api.refinitiv.com
    tags:
      - Desktop
      - Interoperability
      - Web
      - Workspace
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/eikon/workspace-web-side-by-side-api/documentation
      - type: Getting Started
        url: https://developers.lseg.com/en/api-catalog/eikon/workspace-web-side-by-side-api/quick-start
  - name: FX Trading - Spot and Forwards Matching API
    description: FIX protocol-based API for electronic FX trading on LSEG Matching venues, supporting spot and forwards currency trading. It uses FIX 5.0 SP2 with a specific set of FIX messages, tags, and workflows for order submission and execution.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/fx-venues/fx-trading-spot-forwards-matching
    baseURL: https://api.refinitiv.com
    tags:
      - FIX Protocol
      - Forwards
      - FX Trading
      - Spot
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/fx-venues/fx-trading-spot-forwards-matching/documentation
  - name: FX Trading - NDF Matching API
    description: FIX protocol-based API for electronic trading of non-deliverable forwards (NDFs) on LSEG Matching venues. It provides connectivity for trading participants to submit and manage NDF orders.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/fx-venues/fx-trading-matching
    baseURL: https://api.refinitiv.com
    tags:
      - Derivatives
      - FIX Protocol
      - FX Trading
      - NDF
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/fx-venues/fx-trading-matching/documentation
  - name: FX Market Data - NDF Matching API
    description: Point-to-point market data service based on FIX SBE technology, allowing trading participants to receive real-time information for each instrument traded on Primary CLOBs for NDF Matching venues.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/fx-venues/fx-market-data
    baseURL: https://api.refinitiv.com
    tags:
      - FX Market Data
      - NDF
      - Real-Time
      - Trading
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/fx-venues/fx-market-data/documentation
  - name: FX Reference Data API
    description: Service providing reference data for LSEG FX venues, offering instrument and venue configuration data to support FX trading operations on the replatformed spot and forward Matching venues.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/fx-venues/FX-Reference-Data-API
    baseURL: https://api.refinitiv.com
    tags:
      - FX
      - Reference Data
      - Trading
      - Venue
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/fx-venues/FX-Reference-Data-API/documentation
  - name: FX Participant Insight Reporting API
    description: API providing reporting and analytics for FX trading participants on LSEG venues, enabling access to execution quality metrics and participant insight data.
    image: https://www.refinitiv.com/etc/designs/refinitiv/images/refinitiv-logo.svg
    humanURL: https://developers.lseg.com/en/api-catalog/fx-venues/fx-reporting
    baseURL: https://api.refinitiv.com
    tags:
      - Analytics
      - FX
      - Reporting
      - Trading
    properties:
      - type: Documentation
        url: https://developers.lseg.com/en/api-catalog/fx-venues/fx-reporting/documentation
common:
  - type: JSON-LD
    url: json-ld/refinitiv-context.jsonld
  - type: JSONSchema
    url: json-schema/refinitiv-instrument-schema.json
  - type: JSONSchema
    url: json-schema/refinitiv-esg-score-schema.json
  - type: JSONSchema
    url: json-schema/refinitiv-screening-case-schema.json
  - type: JSONSchema
    url: json-schema/refinitiv-news-article-schema.json
  - type: Portal
    url: https://developers.lseg.com/en
  - type: Getting Started
    url: https://developers.lseg.com/en/api-catalog
  - type: Documentation
    url: https://developers.lseg.com/en/api-catalog
  - type: Support
    url: https://developers.lseg.com/en/support
  - type: Blog
    url: https://developers.lseg.com/en/article-catalog
  - type: GitHub Organization
    url: https://github.com/LSEG-API-Samples
  - type: GitHub Organization
    url: https://github.com/Refinitiv-API-Samples
  - type: Terms of Service
    url: https://developers.lseg.com/en/terms-and-conditions
  - type: Contact
    url: https://developers.lseg.com/en/contact-us
  - type: Privacy Policy
    url: https://www.lseg.com/en/policies/privacy-statement
  - type: Community
    url: https://community.developers.refinitiv.com/
  - type: Website
    url: https://www.lseg.com/en
  - type: Login
    url: https://www.lseg.com/en/product-logins
  - type: Developer Tools
    url: https://developers.lseg.com/en/tools-catalog
  - type: Medium
    url: https://medium.com/lseg-developer-community
  - type: OpenAPI
    url: openapi/refinitiv-data-platform-openapi.yml
  - type: OpenAPI
    url: openapi/refinitiv-datascope-select-openapi.yml
  - type: OpenAPI
    url: openapi/refinitiv-permid-entity-search-openapi.yml
  - type: OpenAPI
    url: openapi/refinitiv-qual-id-openapi.yml
  - type: OpenAPI
    url: openapi/refinitiv-world-check-one-openapi.yml
  - type: AsyncAPI
    url: asyncapi/refinitiv-real-time-websocket-asyncapi.yml
  - type: JSONSchema
    url: json-schema/refinitiv-instrument-schema.json
  - type: JSONSchema
    url: json-schema/refinitiv-esg-score-schema.json
  - type: JSONSchema
    url: json-schema/refinitiv-news-article-schema.json
  - type: JSONSchema
    url: json-schema/refinitiv-screening-case-schema.json
  - type: JSONStructure
    url: json-structure/refinitiv-data-platform-structure.json
  - type: JSONLDContext
    url: json-ld/refinitiv-context.jsonld
  - type: SpectralRules
    url: rules/refinitiv-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/financial-market-data.yaml
  - type: NaftikoCapabilities
    url: capabilities/compliance-screening.yaml
  - type: Vocabulary
    url: vocabulary/refinitiv-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
