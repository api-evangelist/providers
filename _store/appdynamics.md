---
aid: appdynamics
url: https://raw.githubusercontent.com/api-evangelist/appdynamics/refs/heads/main/apis.yml
apis:
- aid: appdynamics:controller-rest-api
  name: AppDynamics Controller REST API
  tags:
  - Application Performance Monitoring
  - Metrics
  - Monitoring
  - Observability
  - Snapshots
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.appdynamics.com/appd/23.x/latest/en/extend-appdynamics/appdynamics-apis/using-the-controller-apis
  properties:
  - url: https://docs.appdynamics.com/appd/23.x/latest/en/extend-appdynamics/appdynamics-apis/using-the-controller-apis
    type: Documentation
  - url: openapi/appdynamics-controller-rest-api-openapi.yml
    type: OpenAPI
  description: The AppDynamics Controller REST API provides programmatic access to the AppDynamics Controller for retrieving application performance data, managing configurations, and automating monitoring workflows. The API uses standard HTTP methods and returns data in XML or JSON format, with the base URI pattern of /controller/rest/. Developers can use it to query application metrics, retrieve transaction snapshots, manage business transactions, and access topology information for monitored applications.
- aid: appdynamics:metric-and-snapshot-api
  name: AppDynamics Metric and Snapshot API
  tags:
  - Metrics
  - Monitoring
  - Performance Data
  - Snapshots
  - Time Series
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.appdynamics.com/appd/23.x/latest/en/extend-appdynamics/appdynamics-apis/metric-and-snapshot-api
  properties:
  - url: https://docs.appdynamics.com/appd/23.x/latest/en/extend-appdynamics/appdynamics-apis/metric-and-snapshot-api
    type: Documentation
  - url: openapi/appdynamics-metric-and-snapshot-api-openapi.yml
    type: OpenAPI
  description: The AppDynamics Metric and Snapshot API allows developers to retrieve metric data and transaction snapshots from monitored applications. It supports configurable time ranges, data aggregation through rollup parameters, and access to various metric types including response times, error rates, and call volumes. Developers can retrieve request snapshots for detailed transaction analysis and configure metric retention periods to control how long performance data is stored.
- aid: appdynamics:alert-and-respond-api
  name: AppDynamics Alert and Respond API
  tags:
  - Alerts
  - Health Rules
  - Incident Response
  - Monitoring
  - Notifications
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.appdynamics.com/appd/23.x/latest/en/extend-appdynamics/appdynamics-apis
  properties:
  - url: https://docs.appdynamics.com/appd/23.x/latest/en/extend-appdynamics/appdynamics-apis
    type: Documentation
  - url: openapi/appdynamics-alert-and-respond-api-openapi.yml
    type: OpenAPI
  description: The AppDynamics Alert and Respond API enables programmatic management of health rules, policies, and actions within the AppDynamics Controller. Developers can create, update, and delete health rules that define performance thresholds, configure alerting policies that determine how violations are handled, and set up automated response actions. This API is essential for automating incident response workflows and integrating AppDynamics alerting with external notification and ticketing systems.
- aid: appdynamics:configuration-api
  name: AppDynamics Configuration API
  tags:
  - Administration
  - Configuration
  - Export
  - Import
  - Management
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.appdynamics.com/appd/23.x/latest/en/extend-appdynamics/appdynamics-apis
  properties:
  - url: https://docs.appdynamics.com/appd/23.x/latest/en/extend-appdynamics/appdynamics-apis
    type: Documentation
  - url: openapi/appdynamics-configuration-api-openapi.yml
    type: OpenAPI
  description: The AppDynamics Configuration API provides endpoints for managing Controller configuration settings programmatically. It includes Configuration Import and Export capabilities that allow administrators to back up, restore, and migrate application configurations between Controller instances. Developers can automate the provisioning and management of application monitoring configurations, business transaction detection rules, and other Controller settings through this API.
- aid: appdynamics:analytics-events-api
  name: AppDynamics Analytics Events API
  tags:
  - Analytics
  - Business Intelligence
  - Custom Data
  - Events
  - Observability
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.appdynamics.com/appd/23.x/latest/en/extend-appdynamics/appdynamics-apis
  properties:
  - url: https://docs.appdynamics.com/appd/23.x/latest/en/extend-appdynamics/appdynamics-apis
    type: Documentation
  - url: openapi/appdynamics-analytics-events-api-openapi.yml
    type: OpenAPI
  description: The AppDynamics Analytics Events API allows developers to send custom analytics events from external data sources to the AppDynamics Events Service. This API supports creating custom event schemas, publishing event data, and querying stored events using the AppDynamics Analytics Query Language (ADQL). It enables organizations to correlate application performance data with custom business metrics and external data sources for deeper operational and business intelligence insights.
- aid: appdynamics:database-agent-api
  name: AppDynamics Database Agent API
  tags:
  - Collectors
  - Database
  - Database Performance
  - Monitoring
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.appdynamics.com/appd/23.x/latest/en/extend-appdynamics/appdynamics-apis
  properties:
  - url: https://docs.appdynamics.com/appd/23.x/latest/en/extend-appdynamics/appdynamics-apis
    type: Documentation
  - url: openapi/appdynamics-database-agent-api-openapi.yml
    type: OpenAPI
  description: The AppDynamics Database Agent API provides HTTP endpoints for managing Database Monitoring database Collectors. Developers can programmatically create, retrieve, update, and delete database collectors that monitor the performance and availability of database instances. This API enables automation of database monitoring setup and management, making it possible to scale database visibility across large environments without manual configuration through the Controller UI.
- aid: appdynamics:machine-agent-api
  name: AppDynamics Machine Agent API
  tags:
  - Custom Metrics
  - Infrastructure
  - Metrics
  - Server Monitoring
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.appdynamics.com/appd/23.x/latest/en/extend-appdynamics/appdynamics-apis
  properties:
  - url: https://docs.appdynamics.com/appd/23.x/latest/en/extend-appdynamics/appdynamics-apis
    type: Documentation
  - url: openapi/appdynamics-machine-agent-api-openapi.yml
    type: OpenAPI
  description: The AppDynamics Machine Agent API provides HTTP endpoints available at the machine agent for uploading custom metrics to the AppDynamics Controller. Developers can use this API to report custom infrastructure metrics, hardware metrics, and other machine-level data points that are not captured by the default agent instrumentation. This enables organizations to extend their monitoring coverage to include custom system-level metrics and integrate data from third-party monitoring tools.
- aid: appdynamics:cloud-observability-api
  name: Cisco Cloud Observability API
  tags:
  - AWS
  - Azure
  - Cloud
  - Connections
  - GCP
  - Observability
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.cisco.com/docs/appdynamics/
  properties:
  - url: https://developer.cisco.com/docs/appdynamics/
    type: Documentation
  - url: openapi/appdynamics-cloud-observability-api-openapi.yml
    type: OpenAPI
  description: The Cisco Cloud Observability API is the next-generation cloud-native platform for AppDynamics, available through the Cisco DevNet developer portal. It provides REST APIs for managing cloud connections, configuring health rules, running analytics queries, and managing application principals. The API supports connections to Amazon Web Services, Microsoft Azure, and Google Cloud Platform, enabling automated cloud monitoring setup and management at scale through OpenAPI-documented endpoints.
- aid: appdynamics:authentication-api
  name: AppDynamics OAuth Authentication API
  tags:
  - Access Tokens
  - Authentication
  - OAuth
  - Security
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developer.cisco.com/docs/appdynamics/authentication/
  properties:
  - url: https://developer.cisco.com/docs/appdynamics/authentication/
    type: Documentation
  - url: openapi/appdynamics-authentication-api-openapi.yml
    type: OpenAPI
  description: The AppDynamics OAuth Authentication API enables developers to generate short-lived access tokens using the OAuth 2.0 Client Credentials Grant flow. API clients can request access tokens to authenticate against AppDynamics APIs securely without using long-lived credentials. This API is used in conjunction with the Cisco Observability Platform to manage API client credentials and control access to the various AppDynamics platform services and endpoints.
name: Appdynamics
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Gain operational intelligence by collecting, indexing, and visualizing data using a powerful on-premises engine for actionable insights.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

