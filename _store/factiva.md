---
name: Factiva
description: Factiva is a business information and research tool from Dow Jones that provides access to global news, company information, and market data from thousands of sources.
image: https://www.dowjones.com/wp-content/uploads/sites/9/2021/03/factiva-logo.png
url: https://www.dowjones.com/professional/factiva/
created: '2024'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Business Intelligence
  - Content Aggregation
  - Market Data
  - Media Monitoring
  - News
  - Research
apis:
  - name: Factiva Snapshots API
    description: Provides programmatic access to create, retrieve, and manage news snapshots based on search queries and filters. Supports analytics explain jobs and time series operations for volume estimation and trend analysis over Factiva content.
    image: https://www.dowjones.com/wp-content/uploads/sites/9/2021/03/factiva-logo.png
    humanURL: https://developer.dowjones.com/site/global/apis/factiva_snapshots/index.gsp
    baseURL: https://api.dowjones.com/factiva/snapshots/v1
    tags:
      - Analytics
      - News
      - Search
      - Snapshots
    properties:
      - type: Documentation
        url: https://developer.dowjones.com/site/global/apis/factiva_snapshots/index.gsp
      - type: Authentication
        url: https://developer.dowjones.com/site/global/apis/authentication/index.gsp
      - type: Pricing
        url: https://www.dowjones.com/professional/factiva/pricing/
      - type: Postman Collection
        url: https://www.postman.com/dj-cse/dow-jones-apis/documentation/l9tpql6/factiva-apis
      - type: Client Libraries
        url: https://github.com/dowjones/factiva-news-python
    contact:
      - FN: Dow Jones Developer Support
        email: api.support@dowjones.com
        url: https://developer.dowjones.com/support
  - name: Factiva Streams API
    description: Real-time streaming API that delivers continuous feeds of news content matching specified criteria and filters. Supports creating and managing stream subscriptions with listener methods for pushing content to downstream systems in high-availability setups.
    image: https://www.dowjones.com/wp-content/uploads/sites/9/2021/03/factiva-logo.png
    humanURL: https://developer.dowjones.com/site/global/apis/factiva_streams/index.gsp
    baseURL: https://api.dowjones.com/factiva/streams/v1
    tags:
      - News Feed
      - Real-Time
      - Streaming
    properties:
      - type: Documentation
        url: https://developer.dowjones.com/site/global/apis/factiva_streams/index.gsp
      - type: Authentication
        url: https://developer.dowjones.com/site/global/apis/authentication/index.gsp
      - type: Pricing
        url: https://www.dowjones.com/professional/factiva/pricing/
      - type: Postman Collection
        url: https://www.postman.com/dj-cse/dow-jones-apis/documentation/l9tpql6/factiva-apis
      - type: Client Libraries
        url: https://github.com/dowjones/factiva-news-python
    contact:
      - FN: Dow Jones Developer Support
        email: api.support@dowjones.com
        url: https://developer.dowjones.com/support
  - name: Factiva Extractions API
    description: Enables large-scale extraction of historical news articles and content based on complex queries and date ranges. After job validation, a Snapshot ID is provided along with a list of files to download for offline analysis.
    image: https://www.dowjones.com/wp-content/uploads/sites/9/2021/03/factiva-logo.png
    humanURL: https://developer.dowjones.com/site/global/apis/factiva_extractions/index.gsp
    baseURL: https://api.dowjones.com/factiva/extractions/v1
    tags:
      - Bulk Data
      - Extractions
      - Historical Data
    properties:
      - type: Documentation
        url: https://developer.dowjones.com/site/global/apis/factiva_extractions/index.gsp
      - type: Authentication
        url: https://developer.dowjones.com/site/global/apis/authentication/index.gsp
      - type: Pricing
        url: https://www.dowjones.com/professional/factiva/pricing/
      - type: Postman Collection
        url: https://www.postman.com/dj-cse/dow-jones-apis/documentation/l9tpql6/factiva-apis
      - type: Client Libraries
        url: https://github.com/dowjones/factiva-news-python
    contact:
      - FN: Dow Jones Developer Support
        email: api.support@dowjones.com
        url: https://developer.dowjones.com/support
  - name: Factiva Analytics API
    description: Provides access to aggregated analytics, trends, and insights derived from Factiva's news and content database. Supports volume estimation, explain jobs, and time series analysis for understanding news coverage patterns.
    image: https://www.dowjones.com/wp-content/uploads/sites/9/2021/03/factiva-logo.png
    humanURL: https://developer.dowjones.com/site/global/apis/factiva_analytics/index.gsp
    baseURL: https://api.dowjones.com/factiva/analytics/v1
    tags:
      - Analytics
      - Insights
      - Trends
    properties:
      - type: Documentation
        url: https://developer.dowjones.com/site/global/apis/factiva_analytics/index.gsp
      - type: Authentication
        url: https://developer.dowjones.com/site/global/apis/authentication/index.gsp
      - type: Pricing
        url: https://www.dowjones.com/professional/factiva/pricing/
      - type: Postman Collection
        url: https://www.postman.com/dj-cse/dow-jones-apis/documentation/l9tpql6/factiva-apis
      - type: Client Libraries
        url: https://github.com/dowjones/factiva-analytics-python
    contact:
      - FN: Dow Jones Developer Support
        email: api.support@dowjones.com
        url: https://developer.dowjones.com/support
  - name: Factiva DJID Taxonomy API
    description: Explores the taxonomy of the Factiva databases using Dow Jones Intelligent Identifiers (DJID). Provides access to approximately 350,000 taxonomy codes covering industries, regions, news subjects, companies, and organizations used to classify Factiva content.
    image: https://www.dowjones.com/wp-content/uploads/sites/9/2021/03/factiva-logo.png
    humanURL: https://dowjones.developerprogram.org/site/docs/factiva_apis/factiva_djid_taxonomy_api/index.gsp
    baseURL: https://api.dowjones.com
    tags:
      - Classification
      - Metadata
      - Reference Data
      - Taxonomy
    properties:
      - type: Documentation
        url: https://dowjones.developerprogram.org/site/docs/factiva_apis/factiva_djid_taxonomy_api/index.gsp
      - type: Authentication
        url: https://developer.dowjones.com/site/global/apis/authentication/index.gsp
      - type: Postman Collection
        url: https://www.postman.com/dj-cse/dow-jones-apis/documentation/l9tpql6/factiva-apis
      - type: Client Libraries
        url: https://github.com/dowjones/factiva-analytics-python
    contact:
      - FN: Dow Jones Developer Support
        email: api.support@dowjones.com
        url: https://developer.dowjones.com/support
  - name: Factiva Code API
    description: Enables retrieval of codes necessary to search for companies, currencies, exchanges, locations, industries, instruments, and news subjects within Factiva. Each data item is identified by a unique Factiva Code and supports lookups by Dow Jones Ticker, CUSIP, DUNS, and ISIN identifiers.
    image: https://www.dowjones.com/wp-content/uploads/sites/9/2021/03/factiva-logo.png
    humanURL: https://dowjones.developerprogram.org/site/docs/factiva_apis/factiva_code_api/index.gsp
    baseURL: https://api.dowjones.com
    tags:
      - Codes
      - Companies
      - Identifiers
      - Reference Data
    properties:
      - type: Documentation
        url: https://dowjones.developerprogram.org/site/docs/factiva_apis/factiva_code_api/index.gsp
      - type: Authentication
        url: https://developer.dowjones.com/site/global/apis/authentication/index.gsp
      - type: Postman Collection
        url: https://www.postman.com/dj-cse/dow-jones-apis/documentation/l9tpql6/factiva-apis
    contact:
      - FN: Dow Jones Developer Support
        email: api.support@dowjones.com
        url: https://developer.dowjones.com/support
  - name: Factiva Retrieval API
    description: Provides retrieval functionality that returns licensed news articles as part of trusted data sources in a retrieval-augmented generation (RAG) stack. Designed for enterprise customers building chatbots, research tools, and other AI applications using copyright-compliant Factiva content.
    image: https://www.dowjones.com/wp-content/uploads/sites/9/2021/03/factiva-logo.png
    humanURL: https://www.postman.com/dj-cse/factiva-developer/collection/7qbhcvz/factiva-retrieval-api
    baseURL: https://api.dowjones.com
    tags:
      - AI
      - Content
      - RAG
      - Retrieval
    properties:
      - type: Documentation
        url: https://www.postman.com/dj-cse/factiva-developer/collection/7qbhcvz/factiva-retrieval-api
      - type: Authentication
        url: https://developer.dowjones.com/site/global/apis/authentication/index.gsp
      - type: GitHub Repository
        url: https://github.com/dowjones/factiva-retrievalapi-demo
    contact:
      - FN: Dow Jones Developer Support
        email: api.support@dowjones.com
        url: https://developer.dowjones.com/support
  - name: Factiva Market Data API
    description: Retrieves real-time quotes, delayed quotes, and time series market data for US, Canadian, and global companies. Supports lookups by Dow Jones Ticker, Factiva Code, CUSIP, DUNS, or ISIN to retrieve market fundamentals such as revenue, earnings, assets, liabilities, and growth.
    image: https://www.dowjones.com/wp-content/uploads/sites/9/2021/03/factiva-logo.png
    humanURL: https://developer.dowjones.com
    baseURL: https://api.dowjones.com
    tags:
      - Financials
      - Market Data
      - Quotes
      - Time Series
    properties:
      - type: Documentation
        url: https://developer.dowjones.com
      - type: Authentication
        url: https://developer.dowjones.com/site/global/apis/authentication/index.gsp
    contact:
      - FN: Dow Jones Developer Support
        email: api.support@dowjones.com
        url: https://developer.dowjones.com/support
common:
  - type: Portal
    url: https://developer.dowjones.com
  - type: Sign Up
    url: https://developer.dowjones.com/site/global/register/index.gsp
  - type: Getting Started
    url: https://www.postman.com/dj-cse/dow-jones-apis/collection/l9tpql6/factiva-apis
  - type: Authentication
    url: https://developer.dowjones.com/site/global/apis/authentication/index.gsp
  - type: Documentation
    url: https://www.postman.com/dj-cse/dow-jones-apis/documentation/l9tpql6/factiva-apis
  - type: Postman Collection
    url: https://www.postman.com/dj-cse/dow-jones-apis/documentation/l9tpql6/factiva-apis
  - type: Terms of Service
    url: https://www.dowjones.com/terms-of-use/
  - type: Privacy Policy
    url: https://www.dowjones.com/privacy-policy/
  - type: Status
    url: https://status.dowjones.com
  - type: Support
    url: https://developer.dowjones.com/support
  - type: Website
    url: https://www.dowjones.com/professional/factiva/
  - type: Blog
    url: https://medium.com/dowjones
  - type: GitHub Organization
    url: https://github.com/dowjones
  - type: GitHub Repository
    url: https://github.com/dowjones/developer-platform
  - type: SDKs
    url: https://github.com/dowjones/factiva-news-python
  - type: LinkedIn
    url: https://www.linkedin.com/company/dow-jones
  - type: X
    url: https://twitter.com/DowJones
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
