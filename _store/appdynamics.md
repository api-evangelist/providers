---
aid: appdynamics
url: https://raw.githubusercontent.com/api-evangelist/appdynamics/refs/heads/main/apis.yml
modified: '2026-04-19'
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
common:
  - type: JSON-LD
    url: json-ld/appdynamics-context.jsonld
  - type: JSONSchema
    url: json-schema/appdynamics-application-model-schema.json
  - type: JSONSchema
    url: json-schema/appdynamics-health-rule-schema.json
  - type: JSONSchema
    url: json-schema/appdynamics-database-collector-schema.json
  - type: JSONSchema
    url: json-schema/appdynamics-analytics-event-schema.json
  - type: Documentation
    url: https://docs.appdynamics.com/appd/24.x/24.3/en/extend-cisco-appdynamics/cisco-appdynamics-apis
  - type: DeveloperPortal
    url: https://developer.cisco.com/site/appdynamics/
  - type: GettingStarted
    url: https://developer.cisco.com/docs/appdynamics/
  - type: GitHubOrganization
    url: https://github.com/Appdynamics
  - type: Pricing
    url: https://www.appdynamics.com/pricing/
  - type: Support
    url: https://www.cisco.com/c/en/us/support/index.html
  - type: JSONStructure
    url: json-structure/appdynamics-application-model-structure.json
  - type: JSONStructure
    url: json-structure/appdynamics-health-rule-structure.json
  - type: JSONStructure
    url: json-structure/appdynamics-database-collector-structure.json
  - type: JSONStructure
    url: json-structure/appdynamics-analytics-event-structure.json
  - type: Example
    url: examples/appdynamics-application-model-example.json
  - type: Example
    url: examples/appdynamics-health-rule-example.json
  - type: Example
    url: examples/appdynamics-database-collector-example.json
  - type: Example
    url: examples/appdynamics-analytics-event-example.json
  - type: Features
    data:
      - name: Application Performance Monitoring
        description: Full-stack APM with code-level visibility into Java, .NET, Node.js, PHP, Python, Go, and Ruby applications.
      - name: Business Transaction Monitoring
        description: End-to-end transaction tracing correlating application performance with business outcomes.
      - name: AI-Powered Anomaly Detection
        description: Automatic baselining and AI-driven anomaly detection to identify performance degradation.
      - name: Infrastructure Monitoring
        description: Server, container, and Kubernetes infrastructure monitoring via Machine Agent.
      - name: Database Monitoring
        description: Database performance monitoring for PostgreSQL, MySQL, MongoDB, Oracle, and more.
      - name: Analytics Events API
        description: Custom analytics events ingestion for correlating business data with application performance.
      - name: Cloud Observability
        description: Next-generation Cisco Cloud Observability platform with OpenTelemetry support and cloud provider connections.
      - name: Health Rules and Alerting
        description: Configurable health rules and automated alerting with policy-based response actions.
      - name: Configuration Management API
        description: Import/export configuration for backup, restore, and migration between Controller instances.
      - name: OAuth 2.0 Authentication
        description: Short-lived OAuth 2.0 access tokens for secure API authentication via Cisco platform.
  - type: UseCases
    data:
      - name: Application Performance Optimization
        description: Identify and resolve performance bottlenecks at the code level before they impact end users.
      - name: DevOps Integration
        description: Integrate performance monitoring into CI/CD pipelines using the Controller REST API.
      - name: Cloud Migration Monitoring
        description: Monitor application performance during and after cloud migration using Cloud Observability.
      - name: Business Impact Analysis
        description: Correlate application performance data with business metrics using the Analytics Events API.
      - name: Automated Incident Response
        description: Automate incident response workflows by integrating AppDynamics alerting with ticketing systems.
  - type: Integrations
    data:
      - name: Cisco Full-Stack Observability
        description: Integration with Cisco FSO platform and Thousand Eyes for end-to-end observability.
      - name: OpenTelemetry
        description: Support for OpenTelemetry metrics ingestion via Cisco Cloud Observability common ingestion pipeline.
      - name: Splunk
        description: Integration with Splunk for log correlation and SIEM.
      - name: ServiceNow
        description: ITSM integration for automated incident and change management.
      - name: PagerDuty
        description: Alerting integration for automated on-call notification and incident management.
      - name: AWS
        description: Amazon Web Services cloud connection for infrastructure and application monitoring.
      - name: Azure
        description: Microsoft Azure cloud connection for cloud-native observability.
      - name: GCP
        description: Google Cloud Platform connection for multi-cloud observability.
description: AppDynamics, now part of Cisco, is an application performance monitoring (APM) and observability platform that provides full-stack visibility into application, business, and infrastructure performance. The platform offers REST APIs for controller management, metrics, alerts, analytics events, database monitoring, and the next-generation Cisco Cloud Observability platform.
name: AppDynamics
tags:
  - APM
  - Application Performance Monitoring
  - Cisco
  - Cloud Observability
  - DevOps
  - Monitoring
  - Observability
  - OpenTelemetry
specificationVersion: '0.19'
---
