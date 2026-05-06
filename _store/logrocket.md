---
aid: logrocket
name: LogRocket
url: https://raw.githubusercontent.com/api-evangelist/logrocket/refs/heads/main/apis.yml
created: '2026-03-20'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Error Monitoring
  - Frontend Monitoring
  - Observability
  - Session Replay
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: JSON-LD
    url: json-ld/logrocket-context.jsonld
  - type: JSONSchema
    url: json-schema/logrocket-session-schema.json
  - type: JSONSchema
    url: json-schema/logrocket-data-export-schema.json
apis:
  - aid: logrocket:rest-api
    name: LogRocket REST API
    tags:
      - Analytics
      - Error Monitoring
      - Observability
      - Session Replay
      - User Identification
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.logrocket.com
    humanURL: https://docs.logrocket.com/reference
    properties:
      - url: https://docs.logrocket.com/reference
        type: Documentation
      - url: openapi/logrocket-rest-api-openapi.yml
        type: OpenAPI
    description: The LogRocket REST API provides programmatic access to LogRocket session replay and monitoring data. It enables developers to manage user identification by sending demographic and engagement data via PUT requests to contextualize user behavior. The API also supports retrieving session highlights and exported session data. All endpoints require an API access key available from the LogRocket dashboard under Settings.
  - aid: logrocket:graphql-api
    name: LogRocket GraphQL API
    tags:
      - Analytics
      - GraphQL
      - Observability
      - Querying
      - Session Replay
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.logrocket.com
    humanURL: https://docs.logrocket.com/reference/graphql-1
    properties:
      - url: https://docs.logrocket.com/reference/graphql-1
        type: Documentation
      - url: openapi/logrocket-graphql-api-openapi.yml
        type: OpenAPI
    description: The LogRocket GraphQL API allows developers to query session replay and analytics data using GraphQL. It provides a flexible query interface for retrieving session information, user activity, error details, and performance metrics. Developers can use this API to build custom dashboards, integrate session data into internal tools, and perform advanced filtering and aggregation of LogRocket monitoring data.
  - aid: logrocket:javascript-sdk
    name: LogRocket JavaScript SDK
    tags:
      - Browser
      - Frontend Monitoring
      - JavaScript
      - SDK
      - Session Replay
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://docs.logrocket.com/reference/getting-started-with-sdks
    properties:
      - url: https://docs.logrocket.com/reference/getting-started-with-sdks
        type: Documentation
    description: The LogRocket JavaScript SDK enables session replay and error monitoring for web applications. Once initialized with LogRocket.init(), it automatically records user sessions including DOM changes, network requests, console logs, and JavaScript errors. The SDK provides methods for user identification, session URL retrieval, and custom event tracking. It can be installed via npm or script tag and integrates with popular frameworks like React, Angular, and Vue.
  - aid: logrocket:react-native-sdk
    name: LogRocket React Native SDK
    tags:
      - Mobile
      - Mobile Monitoring
      - React Native
      - SDK
      - Session Replay
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://docs.logrocket.com/reference/configure-reactnative-sdk
    properties:
      - url: https://docs.logrocket.com/reference/configure-reactnative-sdk
        type: Documentation
    description: The LogRocket React Native SDK brings session replay and error monitoring to React Native mobile applications. It captures wireframes of UI elements, network requests, and application errors to help developers reproduce and diagnose issues on mobile devices. The SDK provides initialization, user identification, and session URL access methods similar to the browser SDK, adapted for the React Native environment.
  - aid: logrocket:data-export-api
    name: LogRocket Data Export API
    tags:
      - Analytics
      - Data Export
      - ETL
      - Session Data
      - Storage
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.logrocket.com
    humanURL: https://docs.logrocket.com/docs/data-export
    properties:
      - url: https://docs.logrocket.com/docs/data-export
        type: Documentation
    description: The LogRocket Data Export API enables automated export of session data into file storage buckets for external analysis. When a session completes, LogRocket creates a JSON Lines file containing the session data which can be retrieved programmatically. This API is useful for teams that need to integrate LogRocket session data into their data warehouses, build custom analytics pipelines, or perform long-term retention and analysis of user behavior data.
  - aid: logrocket:user-identification-api
    name: LogRocket User Identification API
    tags:
      - Analytics
      - Identification
      - User Data
      - User Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.logrocket.com
    humanURL: https://docs.logrocket.com/docs/user-identification-api
    properties:
      - url: https://docs.logrocket.com/docs/user-identification-api
        type: Documentation
    description: The LogRocket User Identification API allows developers to send user demographic, financial, and engagement data from any backend system to LogRocket. Using PUT requests to the organizations and apps endpoint, developers can attach user attributes such as subscription type, revenue data, and product interest to session recordings. This enables teams to contextualize user behavior, filter sessions by user attributes, and break down business metrics within the LogRocket dashboard.
  - aid: logrocket:session-highlights-api
    name: LogRocket Galileo Highlights API
    tags:
      - AI
      - Highlights
      - Observability
      - Session Replay
      - Summarization
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.logrocket.com
    humanURL: https://docs.logrocket.com/docs/session-highlights-api
    properties:
      - url: https://docs.logrocket.com/docs/session-highlights-api
        type: Documentation
      - url: asyncapi/logrocket-highlights-webhook-asyncapi.yml
        type: AsyncAPI
    description: The LogRocket Galileo Highlights API provides programmatic access to AI-generated session summaries and highlights. Galileo AI watches user sessions and automatically identifies and aggregates problematic interactions, errors, and notable user behaviors. Developers can use this API to retrieve session highlights via POST requests, enabling integration of AI-powered session insights into custom workflows, alerting systems, and internal dashboards.
description: LogRocket is a frontend application monitoring solution that lets developers replay problems as if they happened in their own browser, combining session replay, error tracking, and product analytics.
---
