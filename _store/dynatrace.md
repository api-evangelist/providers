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
        type: SDK
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
        type: APIReference
      - url: openapi/dynatrace-metrics-api-v2-openapi.yml
        type: OpenAPI
      - url: json-schema/metrics-api-v2-constraint-violation-schema.json
        type: JSONSchema
      - url: json-schema/metrics-api-v2-metric-data-schema.json
        type: JSONSchema
      - url: json-schema/metrics-api-v2-metric-default-aggregation-schema.json
        type: JSONSchema
      - url: json-schema/metrics-api-v2-metric-descriptor-collection-schema.json
        type: JSONSchema
      - url: json-schema/metrics-api-v2-metric-descriptor-schema.json
        type: JSONSchema
      - url: json-schema/metrics-api-v2-metric-dimension-definition-schema.json
        type: JSONSchema
      - url: json-schema/metrics-api-v2-metric-series-collection-schema.json
        type: JSONSchema
      - url: json-schema/metrics-api-v2-metric-series-schema.json
        type: JSONSchema
      - url: json-structure/metrics-api-v2-constraint-violation-structure.json
        type: JSONStructure
      - url: json-structure/metrics-api-v2-metric-data-structure.json
        type: JSONStructure
      - url: json-structure/metrics-api-v2-metric-default-aggregation-structure.json
        type: JSONStructure
      - url: json-structure/metrics-api-v2-metric-descriptor-collection-structure.json
        type: JSONStructure
      - url: json-structure/metrics-api-v2-metric-descriptor-structure.json
        type: JSONStructure
      - url: json-structure/metrics-api-v2-metric-dimension-definition-structure.json
        type: JSONStructure
      - url: json-structure/metrics-api-v2-metric-series-collection-structure.json
        type: JSONStructure
      - url: json-structure/metrics-api-v2-metric-series-structure.json
        type: JSONStructure
      - url: examples/metrics-api-v2-constraint-violation-example.json
        type: Example
      - url: examples/metrics-api-v2-metric-data-example.json
        type: Example
      - url: examples/metrics-api-v2-metric-default-aggregation-example.json
        type: Example
      - url: examples/metrics-api-v2-metric-descriptor-collection-example.json
        type: Example
      - url: examples/metrics-api-v2-metric-descriptor-example.json
        type: Example
      - url: examples/metrics-api-v2-metric-dimension-definition-example.json
        type: Example
      - url: examples/metrics-api-v2-metric-series-collection-example.json
        type: Example
      - url: examples/metrics-api-v2-metric-series-example.json
        type: Example
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
      - url: json-schema/log-monitoring-api-v2-constraint-violation-schema.json
        type: JSONSchema
      - url: json-schema/log-monitoring-api-v2-log-aggregate-group-schema.json
        type: JSONSchema
      - url: json-schema/log-monitoring-api-v2-log-aggregate-result-schema.json
        type: JSONSchema
      - url: json-schema/log-monitoring-api-v2-log-export-result-schema.json
        type: JSONSchema
      - url: json-schema/log-monitoring-api-v2-log-ingest-record-schema.json
        type: JSONSchema
      - url: json-schema/log-monitoring-api-v2-log-record-schema.json
        type: JSONSchema
      - url: json-schema/log-monitoring-api-v2-log-record-search-result-schema.json
        type: JSONSchema
      - url: json-structure/log-monitoring-api-v2-constraint-violation-structure.json
        type: JSONStructure
      - url: json-structure/log-monitoring-api-v2-log-aggregate-group-structure.json
        type: JSONStructure
      - url: json-structure/log-monitoring-api-v2-log-aggregate-result-structure.json
        type: JSONStructure
      - url: json-structure/log-monitoring-api-v2-log-export-result-structure.json
        type: JSONStructure
      - url: json-structure/log-monitoring-api-v2-log-ingest-record-structure.json
        type: JSONStructure
      - url: json-structure/log-monitoring-api-v2-log-record-search-result-structure.json
        type: JSONStructure
      - url: json-structure/log-monitoring-api-v2-log-record-structure.json
        type: JSONStructure
      - url: examples/log-monitoring-api-v2-constraint-violation-example.json
        type: Example
      - url: examples/log-monitoring-api-v2-log-aggregate-group-example.json
        type: Example
      - url: examples/log-monitoring-api-v2-log-aggregate-result-example.json
        type: Example
      - url: examples/log-monitoring-api-v2-log-export-result-example.json
        type: Example
      - url: examples/log-monitoring-api-v2-log-ingest-record-example.json
        type: Example
      - url: examples/log-monitoring-api-v2-log-record-example.json
        type: Example
      - url: examples/log-monitoring-api-v2-log-record-search-result-example.json
        type: Example
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
        type: APIReference
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
        type: APIReference
      - url: openapi/dynatrace-account-management-api-openapi.yml
        type: OpenAPI
      - url: https://docs.dynatrace.com/docs/dynatrace-api/account-management-api/environment-management-api
        type: GettingStarted
      - url: json-schema/account-management-api-environment-collection-schema.json
        type: JSONSchema
      - url: json-schema/account-management-api-environment-schema.json
        type: JSONSchema
      - url: json-schema/account-management-api-group-collection-schema.json
        type: JSONSchema
      - url: json-schema/account-management-api-group-create-request-schema.json
        type: JSONSchema
      - url: json-schema/account-management-api-group-schema.json
        type: JSONSchema
      - url: json-schema/account-management-api-permission-collection-schema.json
        type: JSONSchema
      - url: json-schema/account-management-api-permission-schema.json
        type: JSONSchema
      - url: json-schema/account-management-api-user-collection-schema.json
        type: JSONSchema
      - url: json-schema/account-management-api-user-create-request-schema.json
        type: JSONSchema
      - url: json-schema/account-management-api-user-schema.json
        type: JSONSchema
      - url: json-structure/account-management-api-environment-collection-structure.json
        type: JSONStructure
      - url: json-structure/account-management-api-environment-structure.json
        type: JSONStructure
      - url: json-structure/account-management-api-group-collection-structure.json
        type: JSONStructure
      - url: json-structure/account-management-api-group-create-request-structure.json
        type: JSONStructure
      - url: json-structure/account-management-api-group-structure.json
        type: JSONStructure
      - url: json-structure/account-management-api-permission-collection-structure.json
        type: JSONStructure
      - url: json-structure/account-management-api-permission-structure.json
        type: JSONStructure
      - url: json-structure/account-management-api-user-collection-structure.json
        type: JSONStructure
      - url: json-structure/account-management-api-user-create-request-structure.json
        type: JSONStructure
      - url: json-structure/account-management-api-user-structure.json
        type: JSONStructure
      - url: examples/account-management-api-environment-collection-example.json
        type: Example
      - url: examples/account-management-api-environment-example.json
        type: Example
      - url: examples/account-management-api-group-collection-example.json
        type: Example
      - url: examples/account-management-api-group-create-request-example.json
        type: Example
      - url: examples/account-management-api-group-example.json
        type: Example
      - url: examples/account-management-api-permission-collection-example.json
        type: Example
      - url: examples/account-management-api-permission-example.json
        type: Example
      - url: examples/account-management-api-user-collection-example.json
        type: Example
      - url: examples/account-management-api-user-create-request-example.json
        type: Example
      - url: examples/account-management-api-user-example.json
        type: Example
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
        type: APIReference
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
        type: APIReference
      - url: https://developer.dynatrace.com/develop/sdks/client-automation/
        type: SDK
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
        type: ReleaseNotes
      - url: openapi/dynatrace-events-api-v2-openapi.yml
        type: OpenAPI
      - url: json-schema/events-api-v2-constraint-violation-schema.json
        type: JSONSchema
      - url: json-schema/events-api-v2-entity-stub-schema.json
        type: JSONSchema
      - url: json-schema/events-api-v2-event-collection-schema.json
        type: JSONSchema
      - url: json-schema/events-api-v2-event-ingest-payload-schema.json
        type: JSONSchema
      - url: json-schema/events-api-v2-event-ingest-result-item-schema.json
        type: JSONSchema
      - url: json-schema/events-api-v2-event-ingest-result-schema.json
        type: JSONSchema
      - url: json-schema/events-api-v2-event-schema.json
        type: JSONSchema
      - url: json-structure/events-api-v2-constraint-violation-structure.json
        type: JSONStructure
      - url: json-structure/events-api-v2-entity-stub-structure.json
        type: JSONStructure
      - url: json-structure/events-api-v2-event-collection-structure.json
        type: JSONStructure
      - url: json-structure/events-api-v2-event-ingest-payload-structure.json
        type: JSONStructure
      - url: json-structure/events-api-v2-event-ingest-result-item-structure.json
        type: JSONStructure
      - url: json-structure/events-api-v2-event-ingest-result-structure.json
        type: JSONStructure
      - url: json-structure/events-api-v2-event-structure.json
        type: JSONStructure
      - url: examples/events-api-v2-constraint-violation-example.json
        type: Example
      - url: examples/events-api-v2-entity-stub-example.json
        type: Example
      - url: examples/events-api-v2-event-collection-example.json
        type: Example
      - url: examples/events-api-v2-event-example.json
        type: Example
      - url: examples/events-api-v2-event-ingest-payload-example.json
        type: Example
      - url: examples/events-api-v2-event-ingest-result-example.json
        type: Example
      - url: examples/events-api-v2-event-ingest-result-item-example.json
        type: Example
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
        type: ReleaseNotes
      - url: openapi/dynatrace-problems-api-v2-openapi.yml
        type: OpenAPI
      - url: asyncapi/dynatrace-problems-asyncapi.yml
        type: AsyncAPI
      - url: json-schema/problems-api-v2-alerting-profile-stub-schema.json
        type: JSONSchema
      - url: json-schema/problems-api-v2-comment-collection-schema.json
        type: JSONSchema
      - url: json-schema/problems-api-v2-comment-request-body-schema.json
        type: JSONSchema
      - url: json-schema/problems-api-v2-comment-schema.json
        type: JSONSchema
      - url: json-schema/problems-api-v2-constraint-violation-schema.json
        type: JSONSchema
      - url: json-schema/problems-api-v2-entity-stub-schema.json
        type: JSONSchema
      - url: json-schema/problems-api-v2-management-zone-schema.json
        type: JSONSchema
      - url: json-schema/problems-api-v2-problem-close-request-schema.json
        type: JSONSchema
      - url: json-schema/problems-api-v2-problem-close-result-schema.json
        type: JSONSchema
      - url: json-schema/problems-api-v2-problem-collection-schema.json
        type: JSONSchema
      - url: json-schema/problems-api-v2-problem-schema.json
        type: JSONSchema
      - url: json-structure/problems-api-v2-alerting-profile-stub-structure.json
        type: JSONStructure
      - url: json-structure/problems-api-v2-comment-collection-structure.json
        type: JSONStructure
      - url: json-structure/problems-api-v2-comment-request-body-structure.json
        type: JSONStructure
      - url: json-structure/problems-api-v2-comment-structure.json
        type: JSONStructure
      - url: json-structure/problems-api-v2-constraint-violation-structure.json
        type: JSONStructure
      - url: json-structure/problems-api-v2-entity-stub-structure.json
        type: JSONStructure
      - url: json-structure/problems-api-v2-management-zone-structure.json
        type: JSONStructure
      - url: json-structure/problems-api-v2-problem-close-request-structure.json
        type: JSONStructure
      - url: json-structure/problems-api-v2-problem-close-result-structure.json
        type: JSONStructure
      - url: json-structure/problems-api-v2-problem-collection-structure.json
        type: JSONStructure
      - url: json-structure/problems-api-v2-problem-structure.json
        type: JSONStructure
      - url: examples/problems-api-v2-alerting-profile-stub-example.json
        type: Example
      - url: examples/problems-api-v2-comment-collection-example.json
        type: Example
      - url: examples/problems-api-v2-comment-example.json
        type: Example
      - url: examples/problems-api-v2-comment-request-body-example.json
        type: Example
      - url: examples/problems-api-v2-constraint-violation-example.json
        type: Example
      - url: examples/problems-api-v2-entity-stub-example.json
        type: Example
      - url: examples/problems-api-v2-management-zone-example.json
        type: Example
      - url: examples/problems-api-v2-problem-close-request-example.json
        type: Example
      - url: examples/problems-api-v2-problem-close-result-example.json
        type: Example
      - url: examples/problems-api-v2-problem-collection-example.json
        type: Example
      - url: examples/problems-api-v2-problem-example.json
        type: Example
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
      - url: json-schema/entities-api-v2-constraint-violation-schema.json
        type: JSONSchema
      - url: json-schema/entities-api-v2-entity-collection-schema.json
        type: JSONSchema
      - url: json-schema/entities-api-v2-entity-lookup-request-schema.json
        type: JSONSchema
      - url: json-schema/entities-api-v2-entity-schema.json
        type: JSONSchema
      - url: json-schema/entities-api-v2-entity-tag-schema.json
        type: JSONSchema
      - url: json-schema/entities-api-v2-entity-type-collection-schema.json
        type: JSONSchema
      - url: json-schema/entities-api-v2-entity-type-property-schema.json
        type: JSONSchema
      - url: json-schema/entities-api-v2-entity-type-relationship-schema.json
        type: JSONSchema
      - url: json-schema/entities-api-v2-entity-type-schema.json
        type: JSONSchema
      - url: json-schema/entities-api-v2-management-zone-schema.json
        type: JSONSchema
      - url: json-structure/entities-api-v2-constraint-violation-structure.json
        type: JSONStructure
      - url: json-structure/entities-api-v2-entity-collection-structure.json
        type: JSONStructure
      - url: json-structure/entities-api-v2-entity-lookup-request-structure.json
        type: JSONStructure
      - url: json-structure/entities-api-v2-entity-structure.json
        type: JSONStructure
      - url: json-structure/entities-api-v2-entity-tag-structure.json
        type: JSONStructure
      - url: json-structure/entities-api-v2-entity-type-collection-structure.json
        type: JSONStructure
      - url: json-structure/entities-api-v2-entity-type-property-structure.json
        type: JSONStructure
      - url: json-structure/entities-api-v2-entity-type-relationship-structure.json
        type: JSONStructure
      - url: json-structure/entities-api-v2-entity-type-structure.json
        type: JSONStructure
      - url: json-structure/entities-api-v2-management-zone-structure.json
        type: JSONStructure
      - url: examples/entities-api-v2-constraint-violation-example.json
        type: Example
      - url: examples/entities-api-v2-entity-collection-example.json
        type: Example
      - url: examples/entities-api-v2-entity-example.json
        type: Example
      - url: examples/entities-api-v2-entity-lookup-request-example.json
        type: Example
      - url: examples/entities-api-v2-entity-tag-example.json
        type: Example
      - url: examples/entities-api-v2-entity-type-collection-example.json
        type: Example
      - url: examples/entities-api-v2-entity-type-example.json
        type: Example
      - url: examples/entities-api-v2-entity-type-property-example.json
        type: Example
      - url: examples/entities-api-v2-entity-type-relationship-example.json
        type: Example
      - url: examples/entities-api-v2-management-zone-example.json
        type: Example
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
        type: APIReference
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
        type: APIReference
      - url: https://developer.dynatrace.com/develop/sdks/client-query/
        type: SDK
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
        type: APIReference
      - url: https://docs.dynatrace.com/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens
        type: GettingStarted
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
        type: APIReference
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
        type: APIReference
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
        type: APIReference
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
        type: APIReference
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
        type: APIReference
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
        type: APIReference
      - url: https://docs.dynatrace.com/docs/dynatrace-api/environment-api/application-security/davis-security-advice
        type: APIReference
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
        type: APIReference
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
        type: APIReference
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
        type: SDK
      - url: https://developer.dynatrace.com/plan/platform-services/document-service/
        type: APIReference
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
        type: APIReference
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
        type: GettingStarted
      - url: https://docs.dynatrace.com/docs/discover-dynatrace/platform/davis-ai
        type: APIReference
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
        type: APIReference
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
        type: APIReference
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
modified: '2026-04-18'
position: Consumer
description: Dynatrace is a software intelligence platform that provides application performance monitoring, artificial intelligence for operations, cloud infrastructure monitoring, and digital experience management.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - url: https://www.dynatrace.com/support/help/dynatrace-api
    type: Portal
  - url: https://docs.dynatrace.com/docs/dynatrace-api
    type: Documentation
  - url: https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication
    type: Authentication
  - url: https://www.dynatrace.com/support/help/dynatrace-api/basics
    type: GettingStarted
  - url: https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-response-codes
    type: APIReference
  - url: https://docs.dynatrace.com/docs/whats-new/dynatrace-api
    type: ChangeLog
  - url: https://www.dynatrace.com/company/trust-center/terms/
    type: TermsOfService
  - url: https://www.dynatrace.com/company/trust-center/privacy/
    type: PrivacyPolicy
  - url: https://www.dynatrace.com/support/
    type: Support
  - url: https://www.dynatrace.com/pricing/
    type: Pricing
  - url: https://www.dynatrace.com/signup/
    type: SignUp
  - url: https://community.dynatrace.com/
    type: Support
  - url: https://community.dynatrace.com/t5/Developer-Blog/bg-p/dev_blog
    type: Blog
  - url: https://dynatrace.status.io/
    type: StatusPage
  - url: https://github.com/Dynatrace
    type: GitHubOrganization
  - url: https://developer.dynatrace.com/
    type: DeveloperPortal
  - url: https://stackoverflow.com/questions/tagged/dynatrace
    type: StackOverflow
  - url: https://www.youtube.com/c/dynatrace
    type: YouTube
  - url: json-schema/dynatrace-metric-series-schema.json
    type: JSONSchema
  - url: json-schema/dynatrace-problem-schema.json
    type: JSONSchema
  - url: json-ld/dynatrace-context.jsonld
    type: JSONLD
  - url: https://developer.dynatrace.com/develop/sdks/
    type: SDK
  - url: https://developer.dynatrace.com/develop/access-platform-apis-from-outside/
    type: Authentication
  - url: https://docs.dynatrace.com/docs/manage/identity-access-management
    type: Security
  - url: https://github.com/Dynatrace/dynatrace-api
    type: GitHubRepository
  - url: https://www.dynatrace.com/hub/
    type: Marketplace
  - url: https://docs.dynatrace.com/docs/discover-dynatrace/references/dynatrace-api/basics/deprecation-migration-guides
    type: ReleaseNotes
  - url: https://developer.dynatrace.com/plan/platform-services/
    type: Documentation
  - type: Features
    data:
      - name: Full-Stack Observability
        description: End-to-end monitoring of applications, infrastructure, and digital experiences with automatic discovery and AI-powered root cause analysis.
      - name: Davis AI Engine
        description: Deterministic AI engine that automatically detects anomalies, identifies root causes, and provides precise answers about performance issues without manual configuration.
      - name: Grail Data Lakehouse
        description: Unified data store that combines logs, metrics, traces, events, and business data in a single analytics platform with unlimited retention and DQL query language.
      - name: Software Intelligence
        description: Real-time topology mapping and dependency analysis across distributed systems with automatic baselining and smart alerting.
      - name: Cloud Automation
        description: Automated workflows, remediation, and orchestration capabilities that integrate with CI/CD pipelines and IT service management tools.
      - name: Application Security
        description: Runtime application security with vulnerability detection, attack protection, and security analytics built into the observability platform.
      - name: Digital Experience Monitoring
        description: Real user monitoring, session replay, and synthetic monitoring for web and mobile applications to optimize user experience.
      - name: OpenPipeline Data Ingestion
        description: Flexible data ingestion framework supporting any data source and format with configurable routing, processing, and enrichment pipelines.
      - name: Extensions Framework
        description: Extensible monitoring platform with 600+ out-of-the-box integrations and a framework for building custom data collection extensions.
      - name: Service Level Objectives
        description: Automated SLO tracking and evaluation with burn rate alerting and reliability scoring based on real monitoring data.
  - type: UseCases
    data:
      - name: Infrastructure Monitoring
        description: Monitor hosts, containers, and cloud infrastructure with automatic discovery, health metrics, and capacity planning across hybrid and multi-cloud environments.
      - name: Application Performance Management
        description: Trace distributed transactions end-to-end, identify bottlenecks, and optimize application performance with code-level visibility and AI-powered insights.
      - name: Log Analytics and Management
        description: Ingest, search, and analyze log data at scale using the Grail data lakehouse with DQL queries for troubleshooting and compliance.
      - name: Cloud Migration Monitoring
        description: Track application health and performance during cloud migration with automatic dependency mapping and impact analysis.
      - name: DevOps and SRE Automation
        description: Integrate observability into CI/CD pipelines with automated quality gates, deployment validation, and incident response workflows.
      - name: Business Analytics
        description: Correlate business events with technical performance data to measure revenue impact and optimize digital business outcomes.
      - name: Security Posture Management
        description: Detect runtime vulnerabilities, monitor attack attempts, and assess application security posture with integrated security analytics.
      - name: Synthetic Testing
        description: Proactively monitor application availability and performance with browser-based and HTTP synthetic tests from global locations.
  - type: Integrations
    data:
      - name: AWS CloudWatch
        description: Native integration with AWS services for monitoring EC2, Lambda, RDS, and other AWS resources with automatic tagging and topology mapping.
      - name: Azure Monitor
        description: Deep integration with Microsoft Azure for monitoring Azure App Services, AKS, Functions, and other Azure platform services.
      - name: Google Cloud Platform
        description: Integration with GCP services including GKE, Cloud Run, Cloud Functions, and BigQuery for comprehensive cloud monitoring.
      - name: Kubernetes
        description: Full-stack Kubernetes monitoring with automatic pod, node, and cluster discovery, resource utilization tracking, and workload health analysis.
      - name: ServiceNow
        description: Bidirectional integration with ServiceNow for automated incident creation, enrichment, and resolution based on Dynatrace problem detection.
      - name: PagerDuty
        description: Integration with PagerDuty for intelligent alert routing, incident management, and on-call notification based on Dynatrace AI-detected problems.
      - name: Slack
        description: Notification integration with Slack channels for real-time alerts on performance issues, deployments, and problem resolution updates.
      - name: Jira
        description: Integration with Atlassian Jira for automated issue creation and tracking based on detected performance problems and vulnerabilities.
      - name: Terraform
        description: Terraform provider for infrastructure-as-code management of Dynatrace monitoring configuration, dashboards, and alerting profiles.
      - name: Ansible
        description: Ansible collection for automated deployment and configuration of Dynatrace OneAgent and environment settings across infrastructure.
  - type: CLI
    url: https://github.com/Dynatrace/dynatrace-configuration-as-code
    title: Configuration as Code CLI
  - type: SDK
    url: https://github.com/Dynatrace/OneAgent-SDK-for-Java
    title: Java OneAgent SDK
  - type: SDK
    url: https://github.com/Dynatrace/OneAgent-SDK-for-Python
    title: Python OneAgent SDK
  - type: SDK
    url: https://github.com/Dynatrace/OneAgent-SDK-for-NodeJs
    title: Node.js OneAgent SDK
  - type: SDK
    url: https://github.com/Dynatrace/OneAgent-SDK-for-dotnet
    title: .NET OneAgent SDK
  - type: SDK
    url: https://github.com/Dynatrace/OneAgent-SDK-for-C
    title: C OneAgent SDK
  - type: SDK
    url: https://github.com/Dynatrace/swift-mobile-sdk
    title: Swift Mobile SDK
  - type: CodeExamples
    url: https://github.com/Dynatrace/Dynatrace-workflow-samples
    title: Workflow Samples
  - type: CodeExamples
    url: https://github.com/Dynatrace/snippets
    title: Code Snippets
  - type: CodeExamples
    url: https://github.com/Dynatrace/community-examples
    title: Community Examples
  - type: Tutorials
    url: https://github.com/Dynatrace/Dynatrace-Tutorial
    title: Tutorials
  - type: SpectralRules
    url: rules/dynatrace-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/dynatrace-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/identity-and-access.yaml
  - type: NaftikoCapability
    url: capabilities/log-analytics.yaml
  - type: NaftikoCapability
    url: capabilities/observability-monitoring.yaml
  - type: JSONLD
    url: json-ld/dynatrace-account-management-api-context.jsonld
  - type: JSONLD
    url: json-ld/dynatrace-dynatrace-metric-series-context.jsonld
  - type: JSONLD
    url: json-ld/dynatrace-dynatrace-problem-context.jsonld
  - type: JSONLD
    url: json-ld/dynatrace-entities-api-v2-context.jsonld
  - type: JSONLD
    url: json-ld/dynatrace-events-api-v2-context.jsonld
  - type: JSONLD
    url: json-ld/dynatrace-log-monitoring-api-v2-context.jsonld
  - type: JSONLD
    url: json-ld/dynatrace-metrics-api-v2-context.jsonld
  - type: JSONLD
    url: json-ld/dynatrace-problems-api-v2-context.jsonld
  - type: JSONLD
    url: json-ld/dynatrace-problems-entity-ref-context.jsonld
  - type: JSONLD
    url: json-ld/dynatrace-problems-impacted-entity-context.jsonld
  - type: JSONLD
    url: json-ld/dynatrace-problems-problem-details-context.jsonld
  - type: JSONLD
    url: json-ld/dynatrace-problems-problem-notification-payload-context.jsonld
  - type: JSONLD
    url: json-ld/dynatrace-problems-webhook-header-context.jsonld
  - type: JSONLD
    url: json-ld/dynatrace-problems-webhook-notification-config-context.jsonld
---
