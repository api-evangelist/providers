---
aid: keen
name: Keen
description: Keen is an event analytics platform and API that enables developers to collect, store, analyze, and visualize custom event data. It provides a flexible RESTful API for streaming events, running multi-dimensional queries, and building embedded analytics dashboards for products and internal tools.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Custom Events
  - Data Collection
  - Embedded Analytics
  - Event Analytics
url: https://raw.githubusercontent.com/api-evangelist/keen/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: keen:event-collection-api
    name: Keen Event Collection API
    description: The Keen Event Collection API enables developers to send individual or batched events to Keen for storage and analysis. Each event is a JSON object that can contain any arbitrary properties, giving developers full flexibility in defining their data model. The API supports single event recording, multi-event uploads across collections, and inspection of existing collections and properties.
    humanURL: https://keen.io/docs/api/#record-a-single-event
    tags:
      - Analytics
      - Data Collection
      - Events
      - Ingestion
    properties:
      - type: Documentation
        url: https://keen.io/docs/api/#record-a-single-event
      - type: OpenAPI
        url: openapi/keen-event-collection-api-openapi.yml
  - aid: keen:query-api
    name: Keen Query API
    description: The Keen Query API provides a comprehensive set of analytical query types including count, sum, average, minimum, maximum, percentile, median, count unique, select unique, funnel, and multi-analysis. Queries support filters, time frames, intervals, group-by, and time zone parameters for flexible multi-dimensional analysis of event data.
    humanURL: https://keen.io/docs/api/#analyses
    tags:
      - Aggregation
      - Analytics
      - Queries
      - Reporting
    properties:
      - type: Documentation
        url: https://keen.io/docs/api/#analyses
      - type: OpenAPI
        url: openapi/keen-query-api-openapi.yml
  - aid: keen:cached-queries-api
    name: Keen Cached Queries API
    description: The Keen Cached Queries API allows developers to create, manage, and retrieve pre-defined queries that are automatically refreshed on a schedule. Cached queries improve performance for frequently accessed analytics by storing pre-computed results, making them ideal for powering dashboards and embedded analytics experiences.
    humanURL: https://keen.io/docs/api/#cached-queries
    tags:
      - Analytics
      - Caching
      - Performance
      - Queries
    properties:
      - type: Documentation
        url: https://keen.io/docs/api/#cached-queries
      - type: OpenAPI
        url: openapi/keen-cached-queries-api-openapi.yml
  - aid: keen:saved-queries-api
    name: Keen Saved Queries API
    description: The Keen Saved Queries API enables developers to create and manage reusable query definitions. Saved queries store query parameters as named resources that can be retrieved and executed later, enabling consistent analytics across applications and simplifying the management of complex query configurations.
    humanURL: https://keen.io/docs/api/#saved-queries
    tags:
      - Analytics
      - Queries
      - Saved Queries
    properties:
      - type: Documentation
        url: https://keen.io/docs/api/#saved-queries
      - type: OpenAPI
        url: openapi/keen-saved-queries-api-openapi.yml
  - aid: keen:data-extraction-api
    name: Keen Data Extraction API
    description: The Keen Data Extraction API enables developers to retrieve raw event data from event collections. It supports filtering, sorting, and pagination of event records and is useful for exporting data for external analysis, auditing, or feeding data into other systems and processing pipelines.
    humanURL: https://keen.io/docs/api/#extractions
    tags:
      - Analytics
      - Data
      - Events
      - Export
    properties:
      - type: Documentation
        url: https://keen.io/docs/api/#extractions
      - type: OpenAPI
        url: openapi/keen-data-extraction-api-openapi.yml
common:
  - type: Website
    url: https://keen.io
  - type: Documentation
    url: https://keen.io/docs
  - type: APIDocumentation
    url: https://keen.io/docs/api
  - type: GettingStarted
    url: https://keen.io/docs/getting-started
  - type: Blog
    url: https://keen.io/blog
  - type: Pricing
    url: https://keen.io/pricing
  - type: GitHub
    url: https://github.com/keen
  - type: Login
    url: https://keen.io/login
  - type: Signup
    url: https://keen.io/signup
  - type: Support
    url: https://keen.io/support
  - type: SDKs
    url: https://keen.io/docs/sdks
  - type: StatusPage
    url: https://status.keen.io
  - type: TermsOfService
    url: https://keen.io/terms-of-service
  - type: PrivacyPolicy
    url: https://keen.io/privacy-policy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
