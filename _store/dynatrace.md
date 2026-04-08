---
aid: dynatrace
url: https://raw.githubusercontent.com/api-evangelist/dynatrace/refs/heads/main/apis.yml
apis:
- aid: dynatrace:dynatrace-environment-api
  name: Dynatrace Environment API
  tags:
  - Analytics
  - Automation
  - Intelligence
  - Monitoring
  - Observability
  humanURL: https://docs.dynatrace.com/docs/dynatrace-api/environment-api
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api
    type: Documentation
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication
    type: Authentication
  - url: https://developer.dynatrace.com/develop/sdks/client-classic-environment-v2/
    type: Client Libraries
  description: The Dynatrace Environment API provides access to monitoring data and configuration settings for a specific Dynatrace environment. It includes endpoints for metrics, problems, events, logs, entities, settings, and synthetic monitoring, and is the primary API for interacting with observability data within a Dynatrace environment.
- aid: dynatrace:dynatrace-metrics-api-v2
  name: Dynatrace Metrics API v2
  tags:
  - Metrics
  - Monitoring
  - Observability
  - Time Series
  humanURL: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2
    type: Documentation
  - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2/best-practices
    type: Reference
  - url: openapi/dynatrace-metrics-api-v2-openapi.yml
    type: OpenAPI
  description: The Dynatrace Metrics API v2 allows you to query, ingest, and manage time-series metric data within a Dynatrace environment. It supports retrieving metric descriptors, querying data points with flexible selectors, and ingesting custom metrics from external sources.
- aid: dynatrace:dynatrace-log-monitoring-api-v2
  name: Dynatrace Log Monitoring API v2
  tags:
  - Log Management
  - Logs
  - Monitoring
  - Observability
  humanURL: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/log-monitoring-v2
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/log-monitoring-v2
    type: Documentation
  - url: openapi/dynatrace-log-monitoring-api-v2-openapi.yml
    type: OpenAPI
  description: The Dynatrace Log Monitoring API v2 enables ingestion, search, and export of log records within a Dynatrace environment. It allows you to stream log data to the Grail data lakehouse and retrieve logs programmatically for analysis and integration purposes.
- aid: dynatrace:dynatrace-synthetic-api-v2
  name: Dynatrace Synthetic API v2
  tags:
  - Digital Experience
  - Observability
  - Synthetic Monitoring
  - Testing
  humanURL: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/synthetic-v2
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/synthetic-v2
    type: Documentation
  - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-monitor-execution
    type: Reference
  description: The Dynatrace Synthetic API v2 provides programmatic access to synthetic monitoring resources including browser monitors, HTTP monitors, and clickpaths. It allows you to create, update, delete, and retrieve synthetic monitors and their execution results.
- aid: dynatrace:dynatrace-configuration-api
  name: Dynatrace Configuration API
  tags:
  - Configuration
  - Management
  - Monitoring
  - Observability
  humanURL: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/configuration-api
  baseURL: https://mySampleEnv.live.dynatrace.com/api/config/v1
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/configuration-api
    type: Documentation
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication
    type: Authentication
  description: The Dynatrace Configuration API provides access to environment-level configuration settings including alerting profiles, anomaly detection rules, application detection rules, and data privacy settings. It supports GET, POST, PUT, and DELETE operations for managing Dynatrace environment configuration programmatically.
- aid: dynatrace:dynatrace-account-management-api
  name: Dynatrace Account Management API
  tags:
  - Access Management
  - Account Management
  - Administration
  - Identity
  humanURL: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/account-management-api
  baseURL: https://api.dynatrace.com/iam/v1
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/account-management-api
    type: Documentation
  - url: https://docs.dynatrace.com/docs/dynatrace-api/basics/dynatrace-api-authentication/account-api-authentication
    type: Authentication
  - url: https://docs.dynatrace.com/docs/dynatrace-api/account-management-api/user-management-api
    type: Reference
  - url: openapi/dynatrace-account-management-api-openapi.yml
    type: OpenAPI
  - url: https://docs.dynatrace.com/docs/dynatrace-api/account-management-api/environment-management-api
    type: Getting Started
  description: The Dynatrace Account Management API allows you to manage your Dynatrace account including users, groups, permissions, environments, and service users. It uses OAuth 2.0 authentication and enables programmatic management of identity and access controls across a Dynatrace account.
- aid: dynatrace:dynatrace-openpipeline-api
  name: Dynatrace OpenPipeline API
  tags:
  - Data Ingestion
  - Data Pipelines
  - Observability
  - Platform
  humanURL: https://docs.dynatrace.com/docs/discover-dynatrace/platform/openpipeline/reference/openpipeline-api
  baseURL: https://mySampleEnv.live.dynatrace.com/platform
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/platform/openpipeline/reference/openpipeline-api
    type: Documentation
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/platform/openpipeline
    type: Reference
  description: The Dynatrace OpenPipeline API enables configuration of data ingestion pipelines that handle observability, security, and business data from any source or format. It provides endpoints for managing pipeline configurations, ingest sources, routing rules, and processing stages that feed data into the Grail data lakehouse.
- aid: dynatrace:dynatrace-automation-api
  name: Dynatrace Automation API
  tags:
  - Automation
  - Orchestration
  - Platform
  - Workflows
  humanURL: https://docs.dynatrace.com/docs/analyze-explore-automate/workflows
  baseURL: https://mySampleEnv.live.dynatrace.com/platform
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/analyze-explore-automate/workflows
    type: Documentation
  - url: https://developer.dynatrace.com/develop/workflows/
    type: Reference
  - url: https://developer.dynatrace.com/develop/sdks/client-automation/
    type: Client Libraries
  description: The Dynatrace Automation API provides access to the Workflows automation engine, allowing you to create, manage, and execute automated workflows within Dynatrace. It supports orchestrating remediation actions, alert responses, and multi-step automation tasks through the REST API.
- aid: dynatrace:dynatrace-events-api-v2
  name: Dynatrace Events API v2
  tags:
  - Alerting
  - Events
  - Monitoring
  - Observability
  humanURL: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/events-v2
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/events-v2
    type: Documentation
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/basics/deprecation-migration-guides/events-v1-to-v2
    type: Migration Guide
  - url: openapi/dynatrace-events-api-v2-openapi.yml
    type: OpenAPI
  description: The Dynatrace Events API v2 enables you to push custom events into Dynatrace and retrieve event data from your monitored environment. It supports creating deployment events, custom annotations, and information events targeting multiple entities in a single POST request, and events sent via v2 are subject to DDU licensing.
- aid: dynatrace:dynatrace-problems-api-v2
  name: Dynatrace Problems API v2
  tags:
  - Alerting
  - Monitoring
  - Observability
  - Problems
  humanURL: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/problems-v2
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/problems-v2
    type: Documentation
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/basics/deprecation-migration-guides/problems-v1-to-v2
    type: Migration Guide
  - url: openapi/dynatrace-problems-api-v2-openapi.yml
    type: OpenAPI
  - url: asyncapi/dynatrace-problems-asyncapi.yml
    type: AsyncAPI
  description: The Dynatrace Problems API v2 allows you to query and manage detected problems within a Dynatrace environment. It provides endpoints for listing open and closed problems, retrieving problem details including root cause analysis, and closing problems programmatically. It improves on v1 by supporting entity selectors for multi-entity targeting.
- aid: dynatrace:dynatrace-entities-api-v2
  name: Dynatrace Entities API v2
  tags:
  - Entities
  - Monitoring
  - Observability
  - Topology
  humanURL: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/entity-v2
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/entity-v2
    type: Documentation
  - url: openapi/dynatrace-entities-api-v2-openapi.yml
    type: OpenAPI
  description: The Dynatrace Entities API v2 enables querying of monitored entities such as services, hosts, processes, and applications within a Dynatrace environment. It supports filtering entities by type, tags, and management zones, and returns entity relationships and properties for topology analysis and dependency mapping.
- aid: dynatrace:dynatrace-settings-api-v2
  name: Dynatrace Settings API 2.0
  tags:
  - Configuration
  - Management
  - Observability
  - Settings
  humanURL: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/settings-v2
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/settings-v2
    type: Documentation
  description: The Dynatrace Settings API 2.0 is the modern, schema-driven configuration API for managing Dynatrace environment settings objects. It replaces portions of the Configuration API v1 and provides a unified approach to reading and writing anomaly detection, alerting, and platform settings through versioned schema definitions.
- aid: dynatrace:dynatrace-extensions-api-v2
  name: Dynatrace Extensions API 2.0
  tags:
  - Extensions
  - Integrations
  - Monitoring
  - Observability
  humanURL: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/extensions-v2
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/extensions-v2
    type: Documentation
  - url: https://docs.dynatrace.com/docs/ingest-from/extensions/manage-extensions
    type: Reference
  description: The Dynatrace Extensions API 2.0 provides endpoints for managing monitoring extensions including uploading, activating, configuring, and removing extensions within a Dynatrace environment. It supports the Extensions 2.0 framework used for custom data collection and integration with third-party systems and technologies.
- aid: dynatrace:dynatrace-grail-dql-api
  name: Dynatrace DQL/Grail Query API
  tags:
  - Analytics
  - DQL
  - Grail
  - Observability
  - Query
  humanURL: https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/api
  baseURL: https://mySampleEnv.live.dynatrace.com/platform
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language/api
    type: Documentation
  - url: https://docs.dynatrace.com/docs/platform/grail/dynatrace-query-language
    type: Reference
  - url: https://developer.dynatrace.com/develop/sdks/client-query/
    type: Client Libraries
  description: The Dynatrace DQL/Grail Query API enables execution of DQL (Dynatrace Query Language) queries against the Grail data lakehouse via REST. Queries execute asynchronously using a POST to initiate and GET to poll for results, providing programmatic access to unified observability, security, and business data stored in Grail for custom analytics and automated workflows.
- aid: dynatrace:dynatrace-access-tokens-api-v2
  name: Dynatrace Access Tokens API v2
  tags:
  - Access Management
  - Authentication
  - Security
  - Tokens
  humanURL: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/tokens-v2
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/tokens-v2
    type: Documentation
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/tokens-v2/api-tokens
    type: Reference
  - url: https://docs.dynatrace.com/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens
    type: Getting Started
  description: The Dynatrace Access Tokens API v2 allows you to create, list, update, and delete API access tokens and ActiveGate tokens within a Dynatrace environment. It provides fine-grained scope management for controlling access to specific product functionality, and supports both environment-level API tokens and ActiveGate connection tokens.
- aid: dynatrace:dynatrace-slo-api
  name: Dynatrace Service-Level Objectives API
  tags:
  - Observability
  - Reliability
  - Service Level Objectives
  - SLO
  humanURL: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/service-level-objectives
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/service-level-objectives
    type: Documentation
  - url: https://docs.dynatrace.com/docs/deliver/service-level-objectives
    type: Reference
  description: The Dynatrace Service-Level Objectives API is a management API for creating, editing, listing, deleting, and evaluating SLOs and SLO templates within a Dynatrace environment. It enables programmatic definition of reliability targets and automated evaluation of service-level compliance based on Dynatrace monitoring data.
- aid: dynatrace:dynatrace-releases-api
  name: Dynatrace Releases API
  tags:
  - Deployment
  - Observability
  - Releases
  - Version Management
  humanURL: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/releaseapi
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/releaseapi
    type: Documentation
  description: The Dynatrace Releases API provides an overview of releases deployed in your monitored environment. It allows you to retrieve information about software releases, deployment versions, and release stages, enabling automated tracking of deployment activity and version management across monitored entities.
- aid: dynatrace:dynatrace-network-zones-api
  name: Dynatrace Network Zones API
  tags:
  - Infrastructure
  - Monitoring
  - Network Zones
  - Networking
  humanURL: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/network-zones
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/network-zones
    type: Documentation
  - url: https://docs.dynatrace.com/docs/manage/network-zones/network-zones-basic-info
    type: Reference
  description: The Dynatrace Network Zones API enables you to manage network zones within a Dynatrace environment. It provides endpoints for listing all network zones, retrieving zone details including OneAgent counts, creating and updating zone configurations, deleting zones, and getting global network zone configuration settings.
- aid: dynatrace:dynatrace-deployment-api
  name: Dynatrace Deployment API
  tags:
  - ActiveGate
  - Deployment
  - Installation
  - OneAgent
  humanURL: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/deployment
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/deployment
    type: Documentation
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/deployment/oneagent
    type: Reference
  description: The Dynatrace Deployment API provides endpoints for downloading OneAgent and ActiveGate installers, listing available installer versions, and retrieving ActiveGate endpoint information. It enables automated deployment and upgrade of monitoring agents across your infrastructure using the InstallerDownload token scope.
- aid: dynatrace:dynatrace-audit-logs-api
  name: Dynatrace Audit Logs API
  tags:
  - Audit Logs
  - Compliance
  - Governance
  - Security
  humanURL: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/audit-logs
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/audit-logs
    type: Documentation
  - url: https://docs.dynatrace.com/docs/manage/data-privacy-and-security/configuration/audit-logs-api
    type: Reference
  description: The Dynatrace Audit Logs API provides access to audit-related events within a Dynatrace environment including logins, logouts, configuration changes, and API token modifications. Audit logs are retained for 30 days and support filtering by event type, user, and time range for security monitoring and compliance purposes.
- aid: dynatrace:dynatrace-business-events-api-v2
  name: Dynatrace Business Events API v2
  tags:
  - Business Analytics
  - Business Events
  - Business Intelligence
  - Observability
  humanURL: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/business-analytics-v2
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/business-analytics-v2
    type: Documentation
  - url: https://docs.dynatrace.com/docs/observe/business-observability/bo-api-ingest
    type: Reference
  description: The Dynatrace Business Events API v2 enables ingestion of business event data in JSON format into Dynatrace via the bizevents/ingest endpoint. It supports business-grade reporting and analytics through the Grail data lakehouse with lossless data prioritization, deep data capture from in-flight payloads, and powerful ad-hoc queries for business observability use cases.
- aid: dynatrace:dynatrace-application-security-api
  name: Dynatrace Application Security API
  tags:
  - Application Security
  - Runtime Protection
  - Security
  - Vulnerabilities
  humanURL: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/application-security/vulnerabilities
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/application-security/vulnerabilities
    type: Documentation
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/application-security/attacks
    type: Reference
  - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/application-security/davis-security-advice
    type: Reference
  description: The Dynatrace Application Security API provides endpoints for querying vulnerabilities, vulnerability details, remediation items, vulnerable functions, and security attacks within a Dynatrace environment. It includes the Vulnerabilities API, Attacks API, and Davis Security Advisor API for comprehensive runtime application security analysis and threat detection.
- aid: dynatrace:dynatrace-custom-tags-api
  name: Dynatrace Custom Tags API
  tags:
  - Entities
  - Metadata
  - Monitoring
  humanURL: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/custom-tags
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/custom-tags
    type: Documentation
  description: The Dynatrace Custom Tags API allows you to manage custom tags on monitored entities within a Dynatrace environment. It provides endpoints for reading, adding, and removing tags from entities such as hosts, services, processes, and applications, enabling automated organization and categorization of monitored resources.
- aid: dynatrace:dynatrace-activegate-api
  name: Dynatrace ActiveGate API
  tags:
  - ActiveGate
  - Deployment
  - Infrastructure
  - Monitoring
  humanURL: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/activegates
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/activegates
    type: Documentation
  - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/tokens-v2/activegate-tokens
    type: Reference
  description: The Dynatrace ActiveGate API enables you to view and manage ActiveGate configurations within a Dynatrace environment. It provides endpoints for listing ActiveGates, retrieving ActiveGate details, managing auto-update configurations, and monitoring auto-update job status for Environment ActiveGates.
- aid: dynatrace:dynatrace-credential-vault-api
  name: Dynatrace Credential Vault API
  tags:
  - Credentials
  - Secrets
  - Security
  - Synthetic Monitoring
  humanURL: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/credential-vault
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/credential-vault
    type: Documentation
  - url: https://docs.dynatrace.com/docs/manage/credential-vault
    type: Reference
  description: The Dynatrace Credential Vault API enables management of credentials used for synthetic browser and HTTP monitors within a Dynatrace environment. It supports creating, listing, updating, and deleting credential sets of type certificate, public certificate, token, and username/password for use in synthetic monitoring configurations.
- aid: dynatrace:dynatrace-document-api
  name: Dynatrace Document API
  tags:
  - Dashboards
  - Documents
  - Notebooks
  - Platform
  humanURL: https://docs.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/document-api
  baseURL: https://mySampleEnv.live.dynatrace.com/platform/document/v1
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/document-api
    type: Documentation
  - url: https://developer.dynatrace.com/develop/sdks/client-document/
    type: Client Libraries
  - url: https://developer.dynatrace.com/plan/platform-services/document-service/
    type: Reference
  description: The Dynatrace Document API provides a platform service for creating, managing, and sharing documents such as dashboards, notebooks, and launchpads within Dynatrace. It persists content-agnostic documents with metadata and supports querying by document type, enabling programmatic management of analytical and visualization assets.
- aid: dynatrace:dynatrace-grail-bucket-management-api
  name: Dynatrace Grail Bucket Management API
  tags:
  - Data Management
  - Grail
  - Platform
  - Storage
  humanURL: https://developer.dynatrace.com/develop/sdks/client-bucket-management/
  baseURL: https://mySampleEnv.live.dynatrace.com/platform
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://developer.dynatrace.com/develop/sdks/client-bucket-management/
    type: Documentation
  - url: https://docs.dynatrace.com/docs/platform/grail/organize-data
    type: Reference
  description: The Dynatrace Grail Bucket Management API provides a public API for managing storage buckets within the Grail data lakehouse. It supports creating, updating, deleting, and truncating buckets for organizing logs, events, and business events data with configurable retention periods between 1 and 3657 days.
- aid: dynatrace:dynatrace-davis-ai-api
  name: Dynatrace Davis AI API
  tags:
  - Causal Analysis
  - Davis AI
  - Machine Learning
  - Platform
  - Predictive Analytics
  humanURL: https://developer.dynatrace.com/develop/sdks/client-davis-analyzers/
  baseURL: https://mySampleEnv.live.dynatrace.com/platform
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://developer.dynatrace.com/develop/sdks/client-davis-analyzers/
    type: Documentation
  - url: https://developer.dynatrace.com/develop/forecast-with-davis-ai/
    type: Getting Started
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/platform/davis-ai
    type: Reference
  description: The Dynatrace Davis AI API provides access to the Davis predictive and causal AI platform service for customized AI/ML analysis. It delivers time series forecasting, anomaly detection model training, and automated monitoring of metric behavior changes, enabling application creators to build intelligent automation and analytics within Dynatrace Apps.
- aid: dynatrace:dynatrace-hub-api
  name: Dynatrace Hub API
  tags:
  - Apps
  - Catalog
  - Extensions
  - Hub
  - Platform
  humanURL: https://developer.dynatrace.com/develop/sdks/client-hub/
  baseURL: https://mySampleEnv.live.dynatrace.com/platform
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://developer.dynatrace.com/develop/sdks/client-hub/
    type: Documentation
  - url: https://docs.dynatrace.com/docs/manage/hub
    type: Reference
  description: The Dynatrace Hub API provides programmatic access to the Dynatrace Hub catalog content including apps, extensions, and technologies in the context of the current environment. It supports listing and retrieving details for apps, extensions, technologies, and Hub categories for building custom catalog integrations and discovery experiences.
- aid: dynatrace:dynatrace-oneagent-on-host-api
  name: Dynatrace OneAgent on a Host API
  tags:
  - Deployment
  - Host Monitoring
  - Infrastructure
  - OneAgent
  humanURL: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/oneagent-on-host
  baseURL: https://mySampleEnv.live.dynatrace.com/api/v2
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/environment-api/oneagent-on-host
    type: Documentation
  description: The Dynatrace OneAgent on a Host API enables you to check the configuration and status of OneAgent instances deployed on your hosts. It provides endpoints for listing hosts with OneAgent details, retrieving agent version information, and monitoring agent health and connectivity within a Dynatrace environment.
- aid: dynatrace:dynatrace-platform-management-api
  name: Dynatrace Platform Management API
  tags:
  - Administration
  - Environment Management
  - Platform
  - Settings
  humanURL: https://developer.dynatrace.com/develop/sdks/client-platform-management-service/
  baseURL: https://mySampleEnv.live.dynatrace.com/platform
  image: https://www.dynatrace.com/logo.png
  properties:
  - url: https://developer.dynatrace.com/develop/sdks/client-platform-management-service/
    type: Documentation
  - url: https://developer.dynatrace.com/plan/platform-services/platform-management-service/
    type: Reference
  description: The Dynatrace Platform Management API provides basic read-only information about the currently logged-in environment including environment settings, license information, and permissions. It is a core platform service used for querying environment metadata and configuration context within Dynatrace Apps and automation workflows.
name: Dynatrace
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
type: Index
image: https://www.dynatrace.com/logo.png
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-07'
position: Consumer
description: Dynatrace is a software intelligence platform that provides application performance monitoring, artificial intelligence for operations, cloud infrastructure monitoring, and digital experience management.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

