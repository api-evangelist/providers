---
aid: statsig
url: https://raw.githubusercontent.com/api-evangelist/statsig/refs/heads/main/apis.yml
apis:
- aid: statsig:http-api
  name: Statsig HTTP API
  tags:
  - A/B Testing
  - Analytics
  - Dynamic Configuration
  - Experimentation
  - Feature Flags
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.statsig.com
  humanURL: https://docs.statsig.com/http-api/
  properties:
  - url: https://docs.statsig.com/http-api/
    type: Documentation
  - url: openapi/statsig-http-api-openapi.yml
    type: OpenAPI
  description: The Statsig HTTP API allows developers to evaluate feature gates, dynamic configs, and experiments for users via server-side HTTP requests. It provides endpoints for checking gate values, fetching configuration data, and logging custom events. All requests use the POST method with JSON request bodies and require authentication via the statsig-api-key header.
- aid: statsig:console-api
  name: Statsig Console API
  tags:
  - Administration
  - Automation
  - Configuration Management
  - Experimentation
  - Feature Flags
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://statsigapi.net/console/v1
  humanURL: https://docs.statsig.com/console-api/
  properties:
  - url: https://docs.statsig.com/console-api/
    type: Documentation
  - url: openapi/statsig-console-api-openapi.yml
    type: OpenAPI
  description: The Statsig Console API enables developers to programmatically manage their Statsig project configuration. It supports full CRUD operations on feature gates, dynamic configs, experiments, segments, layers, and other entities. The API requires a Console API Key and uses versioned endpoints with the STATSIG-API-VERSION header.
- aid: statsig:client-sdk-api
  name: Statsig Client SDK API
  tags:
  - Client Side
  - Feature Flags
  - Mobile
  - SDKs
  - Web
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.statsig.com
  humanURL: https://docs.statsig.com/client/introduction
  properties:
  - url: https://docs.statsig.com/client/introduction
    type: Documentation
  - url: openapi/statsig-client-sdk-api-openapi.yml
    type: OpenAPI
  description: The Statsig Client SDK API provides endpoints that power Statsig's client-side SDKs for JavaScript, React, React Native, iOS, Android, Unity, and other platforms. Client SDKs use Client-SDK Keys that are safe to embed in mobile apps and front-end web applications. They access the initialize endpoint to retrieve all evaluated gates, configs, and experiments for a given user, and the log_event endpoint for sending analytics events.
- aid: statsig:server-sdk-api
  name: Statsig Server SDK API
  tags:
  - Backend
  - Evaluation
  - Feature Flags
  - SDKs
  - Server Side
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.statsig.com
  humanURL: https://docs.statsig.com/server/introduction
  properties:
  - url: https://docs.statsig.com/server/introduction
    type: Documentation
  - url: openapi/statsig-server-sdk-api-openapi.yml
    type: OpenAPI
  description: The Statsig Server SDK API provides endpoints that power Statsig's server-side SDKs for Node.js, Python, Java, Ruby, Go, .NET, and other backend languages. Server SDKs use Server Secret Keys and access the download_config_specs endpoint to retrieve the full project configuration for local evaluation. This enables sub-millisecond feature gate checks without per-request network calls.
- aid: statsig:events-api
  name: Statsig Events API
  tags:
  - Analytics
  - Data Ingestion
  - Events
  - Logging
  - Metrics
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://events.statsigapi.net
  humanURL: https://docs.statsig.com/http-api/
  properties:
  - url: https://docs.statsig.com/http-api/
    type: Documentation
  - url: openapi/statsig-events-api-openapi.yml
    type: OpenAPI
  - url: asyncapi/statsig-webhooks-asyncapi.yml
    type: AsyncAPI
  description: The Statsig Events API handles the ingestion of event data from both client and server SDKs. It receives exposure events, custom events, and diagnostic data at the events.statsigapi.net endpoint. This data powers Statsig's experimentation analysis, product analytics, and metric computations. The Events API is optimized for high-throughput data ingestion, processing over a trillion events daily with high reliability and low latency, enabling real-time experiment monitoring and metric updates.
name: Statsig
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Statsig is a feature management and experimentation platform that helps product teams ship features safely with feature flags, run A/B tests, and measure the impact of every feature on key metrics.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

