---
aid: quandl
name: Quandl (Nasdaq Data Link)
description: Nasdaq Data Link (formerly Quandl) provides REST and streaming APIs for financial and economic data including time-series datasets, tabular datasets, and real-time market data feeds. Datasets cover stock prices, economic indicators, interest rates, commodities, equity fundamentals, options data, and alternative data sets.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/quandl/refs/heads/main/apis.yml
tags:
  - Finance
  - Market Data
  - Economic Data
  - Time Series
  - Streaming
created: '2026-03-18'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: quandl:nasdaq-data-link-timeseries-api
    name: Nasdaq Data Link REST API (Time-Series)
    description: Nasdaq Data Link REST API (formerly Quandl) provides access to financial and economic time-series datasets including stock prices, economic indicators, interest rates, and commodity data in JSON, XML, and CSV formats. Authenticated users receive up to 50,000 calls per day.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.data.nasdaq.com/
    baseURL: https://data.nasdaq.com/api/v3
    tags:
      - Finance
      - Economic Data
      - Time Series
      - Market Data
      - REST
    properties:
      - url: https://docs.data.nasdaq.com/
        type: Documentation
      - url: https://docs.data.nasdaq.com/
        type: Reference
      - url: https://docs.data.nasdaq.com/docs/getting-started
        type: GettingStarted
      - url: https://docs.data.nasdaq.com/docs/rate-limits
        type: RateLimits
      - url: https://docs.data.nasdaq.com/docs/python-installation
        type: SDKs
      - url: openapi/nasdaq-data-link-timeseries-openapi.yml
        type: OpenAPI
  - aid: quandl:nasdaq-data-link-tables-api
    name: Nasdaq Data Link Tables REST API
    description: Nasdaq Data Link Tables API provides access to tabular financial datasets including equity fundamentals, options data, and alternative data sets. Limited to 10,000 rows per call with pagination support up to 1,000,000 rows via the Python client.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.data.nasdaq.com/
    baseURL: https://data.nasdaq.com/api/v3
    tags:
      - Finance
      - Market Data
      - Tables
      - REST
    properties:
      - url: https://docs.data.nasdaq.com/
        type: Documentation
      - url: https://docs.data.nasdaq.com/docs/rate-limits-1
        type: RateLimits
  - aid: quandl:nasdaq-cloud-data-service-api
    name: Nasdaq Cloud Data Service (NCDS) Streaming API
    description: Nasdaq Cloud Data Service (NCDS) provides streaming and REST APIs for real-time and delayed market data delivery including equities, options, and fixed income from Nasdaq exchange feeds.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/Nasdaq/NasdaqCloudDataService-REST-API
    tags:
      - Finance
      - Market Data
      - Streaming
      - Real-time
      - REST
    properties:
      - url: https://github.com/Nasdaq/NasdaqCloudDataService-REST-API
        type: Documentation
      - url: https://github.com/Nasdaq/NasdaqCloudDataService-SDK-Python
        type: SDKs
      - url: https://github.com/Nasdaq/NasdaqCloudDataService-SDK-Java
        type: SDKs
common:
  - url: https://data.nasdaq.com/
    type: Portal
  - url: https://docs.data.nasdaq.com/
    type: Documentation
  - url: https://docs.data.nasdaq.com/docs/getting-started
    type: GettingStarted
  - url: https://docs.data.nasdaq.com/docs/rate-limits
    type: RateLimits
  - url: https://data.nasdaq.com/
    type: Website
  - url: https://docs.data.nasdaq.com/docs/contact-support
    type: Support
  - url: https://github.com/Nasdaq
    type: GitHubOrganization
  - url: https://github.com/quandl
    type: GitHubOrganization
  - url: https://github.com/Nasdaq/data-link-python
    type: SDKs
  - url: https://github.com/Nasdaq/NasdaqCloudDataService-SDK-Python
    type: SDKs
  - url: https://github.com/Nasdaq/NasdaqCloudDataService-SDK-Java
    type: SDKs
  - url: openapi/nasdaq-data-link-timeseries-openapi.yml
    type: OpenAPI
  - url: json-schema/nasdaq-data-link-dataset-schema.json
    type: JSONSchema
  - url: json-ld/nasdaq-data-link-context.jsonld
    type: JSONLDContext
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
