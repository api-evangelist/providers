---
aid: honeycomb
url: https://raw.githubusercontent.com/api-evangelist/honeycomb/refs/heads/main/apis.yml
apis:
- aid: honeycomb:api
  name: Honeycomb API
  tags:
  - Debugging
  - Monitoring
  - Observability
  - Telemetry
  - Tracing
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.honeycomb.io
  humanURL: https://api-docs.honeycomb.io/api
  properties:
  - url: https://api-docs.honeycomb.io/api
    type: Documentation
  - url: openapi/honeycomb-api-openapi.yml
    type: OpenAPI
  description: The Honeycomb API is a REST API that provides programmatic access to the Honeycomb observability platform. It enables developers to send events, manage datasets and columns, create and run queries, configure SLOs and burn alerts, set up triggers and recipients, manage boards and markers, and administer environments and API keys.
- aid: honeycomb:events-api
  name: Honeycomb Events API
  tags:
  - Events
  - Ingestion
  - Observability
  - Telemetry
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.honeycomb.io
  humanURL: https://api-docs.honeycomb.io/api/events
  properties:
  - url: https://api-docs.honeycomb.io/api/events
    type: Documentation
  - url: openapi/honeycomb-events-api-openapi.yml
    type: OpenAPI
  description: The Honeycomb Events API is the lowest-level interface for sending event data to Honeycomb. It supports both single event creation and batch event submission, allowing developers to send structured telemetry data directly to Honeycomb datasets. While Honeycomb recommends using OpenTelemetry or Beeline SDKs for most instrumentation use cases, the Events API provides direct control for custom integrations and specialized data pipelines.
- aid: honeycomb:queries-api
  name: Honeycomb Queries API
  tags:
  - Analytics
  - Data Analysis
  - Observability
  - Queries
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.honeycomb.io
  humanURL: https://api-docs.honeycomb.io/api/queries
  properties:
  - url: https://api-docs.honeycomb.io/api/queries
    type: Documentation
  - url: openapi/honeycomb-queries-api-openapi.yml
    type: OpenAPI
  description: The Honeycomb Queries API allows developers to programmatically create and manage query specifications within Honeycomb. Queries are used to identify and reference queries across other parts of the API, including boards, triggers, and query annotations. Developers can run queries asynchronously by creating a Query Result that references a Query ID, then polling the query result endpoint until the data is ready. The Query Data API complements this by providing access to query results.
- aid: honeycomb:slos-api
  name: Honeycomb SLOs API
  tags:
  - Observability
  - Reliability
  - Service Level Objectives
  - SLOs
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.honeycomb.io
  humanURL: https://api-docs.honeycomb.io/api/slos
  properties:
  - url: https://api-docs.honeycomb.io/api/slos
    type: Documentation
  - url: openapi/honeycomb-slos-api-openapi.yml
    type: OpenAPI
  description: The Honeycomb SLOs API enables developers to define and monitor Service Level Objectives programmatically. It supports creating, listing, updating, and deleting SLO objects for an organization. Combined with the Burn Alerts API for notifications and the Reporting API for historical SLO performance analysis, it provides a complete interface for managing reliability targets and tracking error budgets over time.
- aid: honeycomb:datasets-api
  name: Honeycomb Datasets API
  tags:
  - Data Management
  - Datasets
  - Observability
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.honeycomb.io
  humanURL: https://api-docs.honeycomb.io/api/datasets
  properties:
  - url: https://api-docs.honeycomb.io/api/datasets
    type: Documentation
  - url: openapi/honeycomb-datasets-api-openapi.yml
    type: OpenAPI
  description: The Honeycomb Datasets API provides management capabilities for datasets, which represent collections of related events from the same source. It allows developers to list, create, and update datasets programmatically. The related Columns API enables management of fields within datasets, including listing, creating, updating, and deleting columns that define the structure of event data stored in Honeycomb.
- aid: honeycomb:boards-api
  name: Honeycomb Boards API
  tags:
  - Dashboards
  - Observability
  - Visualization
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.honeycomb.io
  humanURL: https://api-docs.honeycomb.io/api/boards
  properties:
  - url: https://api-docs.honeycomb.io/api/boards
    type: Documentation
  - url: openapi/honeycomb-boards-api-openapi.yml
    type: OpenAPI
  description: The Honeycomb Boards API allows developers to programmatically create and manage boards, which are collections of queries displayed together as a dashboard-like view. Boards provide a way to organize and share related queries for monitoring and debugging workflows. The API supports listing, creating, updating, and deleting boards, making it possible to automate the setup of observability dashboards across environments.
- aid: honeycomb:markers-api
  name: Honeycomb Markers API
  tags:
  - Annotations
  - Deployments
  - Markers
  - Observability
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.honeycomb.io
  humanURL: https://api-docs.honeycomb.io/api/marker-settings
  properties:
  - url: https://api-docs.honeycomb.io/api/marker-settings
    type: Documentation
  - url: openapi/honeycomb-markers-api-openapi.yml
    type: OpenAPI
  description: The Honeycomb Markers API enables developers to create and manage markers that indicate points in time on graphs where notable events occurred, such as deploys, configuration changes, or outages. Marker Settings allow grouping similar markers together with consistent visual styling. The API supports listing, creating, updating, and deleting both markers and marker settings, making it straightforward to integrate deployment pipelines and incident workflows with Honeycomb visualizations.
- aid: honeycomb:triggers-api
  name: Honeycomb Triggers API
  tags:
  - Alerts
  - Monitoring
  - Notifications
  - Observability
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.honeycomb.io
  humanURL: https://api-docs.honeycomb.io/api/triggers
  properties:
  - url: https://api-docs.honeycomb.io/api/triggers
    type: Documentation
  - url: openapi/honeycomb-triggers-api-openapi.yml
    type: OpenAPI
  description: The Honeycomb Triggers API allows developers to programmatically configure alerting rules that fire when query results meet specified conditions. Triggers work in conjunction with the Recipients API, which manages notification destinations including PagerDuty, Email, Webhook, Microsoft Teams, and Slack. The API supports listing, creating, updating, and deleting triggers, enabling automated setup of alerting workflows for production observability.
- aid: honeycomb:environments-api
  name: Honeycomb Environments API
  tags:
  - Administration
  - Environments
  - Observability
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.honeycomb.io
  humanURL: https://api-docs.honeycomb.io/api/environments
  properties:
  - url: https://api-docs.honeycomb.io/api/environments
    type: Documentation
  - url: openapi/honeycomb-environments-api-openapi.yml
    type: OpenAPI
  description: The Honeycomb Environments API provides administrative capabilities for managing environments within a Honeycomb team. Environments allow organizations to separate telemetry data across different stages such as development, staging, and production. The API supports listing, creating, updating, and deleting environments, along with the Auth API for validating API keys and determining their associated team and environment permissions.
name: Honeycomb
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Build integrations and automate workflows with the Honeycomb API. Programmatically manage datasets, queries, triggers, SLOs, environments, API keys, and more.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

