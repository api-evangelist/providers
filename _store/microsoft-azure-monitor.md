---
name: Azure Monitor
description: Azure Monitor helps you maximize the availability and performance of your applications and services. It delivers a comprehensive solution for collecting, analyzing, and acting on telemetry from your cloud and on-premises environments.
image: https://azure.microsoft.com/svghandler/monitor/
tags:
  - Application Insights
  - Cloud
  - Logs
  - Metrics
  - Monitoring
  - Observability
created: '2024'
modified: '2026-04-28'
url: https://azure.microsoft.com/en-us/services/monitor/
specificationVersion: '0.18'
apis:
  - name: Azure Monitor Metrics API
    description: Provides access to Azure Monitor platform metric definitions and values for Azure resources, including performance counters, custom metrics, and time-series data.
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/metrics-supported
    baseURL: https://management.azure.com
    tags:
      - Metrics
      - Performance
      - Resource Monitoring
      - Time Series
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/monitor/metrics
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/monitor/resource-manager/Microsoft.Insights/stable/2023-10-01/metrics_API.json
      - type: OpenAPI
        url: openapi/azure-monitor-metrics-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-monitor-metric-schema.json
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/rest-api-walkthrough
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/rest-api-walkthrough
  - name: Azure Monitor Metric Definitions API
    description: Retrieves the list of available metric definitions for a given Azure resource, including metric names, units, aggregation types, and dimensions.
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/rest/api/monitor/metric-definitions
    baseURL: https://management.azure.com
    tags:
      - Definitions
      - Metadata
      - Metrics
      - Resource Monitoring
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/monitor/metric-definitions
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/monitor/resource-manager/Microsoft.Insights/stable/2023-10-01/metricDefinitions_API.json
      - type: OpenAPI
        url: openapi/azure-monitor-metric-definitions-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-monitor-metric-definition-schema.json
  - name: Azure Monitor Metrics Batch API
    description: A high-volume API designed for retrieving metric values across multiple Azure resources in a single request. All resources in a batch must be in the same subscription and region.
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/rest/api/monitor/metrics-batch
    baseURL: https://management.azure.com
    tags:
      - Batch
      - High Volume
      - Metrics
      - Performance
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/monitor/metrics-batch
      - type: OpenAPI
        url: openapi/azure-monitor-metrics-batch-openapi.yml
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/metrics/migrate-to-batch-api
  - name: Azure Monitor Logs API
    description: Query and retrieve log data from Azure Monitor Logs and Application Insights using the Kusto Query Language (KQL).
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/api/overview
    baseURL: https://api.loganalytics.io
    tags:
      - Analytics
      - KQL
      - Logs
      - Query
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/loganalytics/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/operationalinsights/data-plane/Microsoft.OperationalInsights/stable/2022-10-27/OperationalInsights.json
      - type: OpenAPI
        url: openapi/azure-monitor-logs-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-monitor-log-query-schema.json
      - type: Query Language
        url: https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/api/overview
  - name: Azure Monitor Logs Ingestion API
    description: Sends custom log data to a Log Analytics workspace using a REST API call or client libraries. Supports sending data to both supported Azure tables and custom tables via data collection rules and endpoints.
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/logs-ingestion-api-overview
    baseURL: https://management.azure.com
    tags:
      - Custom Logs
      - Data Collection
      - Ingestion
      - Logs
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/logs-ingestion-api-overview
      - type: OpenAPI
        url: openapi/azure-monitor-logs-ingestion-openapi.yml
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/tutorial-logs-ingestion-api
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/tutorial-logs-ingestion-code
  - name: Azure Monitor Alerts API
    description: Create, update, and manage alert rules and action groups for monitoring Azure resources. Supports metric alerts, log search alerts, and activity log alerts.
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview
    baseURL: https://management.azure.com
    tags:
      - Action Groups
      - Alerts
      - Monitoring
      - Notifications
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/monitor/alertrules
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/monitor/resource-manager/Microsoft.Insights/stable/2016-03-01/alertRules_API.json
      - type: OpenAPI
        url: openapi/azure-monitor-alerts-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-monitor-alert-rule-schema.json
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview
  - name: Azure Monitor Scheduled Query Rules API
    description: Create and manage log search alert rules that automatically evaluate log queries at regular intervals and fire alerts when conditions are met.
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/rest/api/monitor/scheduledqueryrule-2021-08-01/scheduled-query-rules
    baseURL: https://management.azure.com
    tags:
      - Alerts
      - Automation
      - Log Search
      - Scheduled Query
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/monitor/scheduledqueryrule-2021-08-01/scheduled-query-rules
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/monitor/resource-manager/Microsoft.Insights/stable/2021-08-01/scheduledQueryRule_API.json
      - type: OpenAPI
        url: openapi/azure-monitor-scheduled-query-rules-openapi.yml
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-log-api-switch
  - name: Azure Monitor Action Groups API
    description: Create and manage action groups that define notification and automation actions triggered by Azure Monitor alerts, including email, SMS, webhooks, and Azure Functions.
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups
    baseURL: https://management.azure.com
    tags:
      - Action Groups
      - Automation
      - Notifications
      - Webhooks
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/monitor/action-groups
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/monitor/resource-manager/Microsoft.Insights/stable/2022-06-01/actionGroups_API.json
      - type: OpenAPI
        url: openapi/azure-monitor-action-groups-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-monitor-action-group-schema.json
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/action-groups
  - name: Azure Monitor Autoscale API
    description: Configure autoscale settings for Azure resources based on metric thresholds, schedules, or predictive rules to automatically adjust resource capacity.
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-overview
    baseURL: https://management.azure.com
    tags:
      - Autoscale
      - Capacity Management
      - Performance
      - Scaling
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/monitor/autoscale-settings
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/monitor/resource-manager/Microsoft.Insights/stable/2022-10-01/autoscale_API.json
      - type: OpenAPI
        url: openapi/azure-monitor-autoscale-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-monitor-autoscale-setting-schema.json
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-best-practices
  - name: Azure Application Insights API
    description: Access Application Insights telemetry data including requests, dependencies, exceptions, traces, and custom events for application performance monitoring.
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview
    baseURL: https://api.applicationinsights.io
    tags:
      - APM
      - Application Performance
      - Telemetry
      - Tracing
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/application-insights/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/applicationinsights/data-plane/Microsoft.Insights/stable/v1/AppInsights.json
      - type: OpenAPI
        url: openapi/azure-monitor-application-insights-openapi.yml
      - type: SDKs
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/app/api-custom-events-metrics
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable
  - name: Azure Monitor Diagnostic Settings API
    description: Configure diagnostic settings to route platform logs and metrics from Azure resources to destinations such as Log Analytics workspaces, Storage Accounts, and Event Hubs.
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings
    baseURL: https://management.azure.com
    tags:
      - Configuration
      - Diagnostics
      - Logs
      - Routing
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/monitor/diagnostic-settings
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/monitor/resource-manager/Microsoft.Insights/stable/2021-05-01-preview/diagnosticsSettings_API.json
      - type: OpenAPI
        url: openapi/azure-monitor-diagnostic-settings-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-monitor-diagnostic-setting-schema.json
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings
  - name: Azure Monitor Activity Log API
    description: Access Azure Activity Log events for subscription-level operations including resource creation, updates, deletions, and administrative actions.
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log
    baseURL: https://management.azure.com
    tags:
      - Activity Log
      - Audit
      - Compliance
      - Events
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/monitor/activity-logs
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/monitor/resource-manager/Microsoft.Insights/stable/2015-04-01/activityLogs_API.json
      - type: OpenAPI
        url: openapi/azure-monitor-activity-log-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-monitor-activity-log-event-schema.json
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log-schema
  - name: Azure Monitor Data Collection Rules API
    description: Create and manage data collection rules that define how data is collected, transformed, and routed to destinations within Azure Monitor.
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview
    baseURL: https://management.azure.com
    tags:
      - Configuration
      - Data Collection
      - Ingestion
      - Rules
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/monitor/data-collection-rules
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/monitor/resource-manager/Microsoft.Insights/stable/2023-03-11/dataCollectionRules_API.json
      - type: OpenAPI
        url: openapi/azure-monitor-data-collection-rules-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-monitor-data-collection-rule-schema.json
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-create-edit
  - name: Azure Monitor Data Collection Endpoints API
    description: Create and manage data collection endpoints that provide unique ingestion and configuration endpoints for data collection in Azure Monitor.
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-endpoint-overview
    baseURL: https://management.azure.com
    tags:
      - Configuration
      - Data Collection
      - Endpoints
      - Ingestion
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/monitor/data-collection-endpoints
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/monitor/resource-manager/Microsoft.Insights/stable/2023-03-11/dataCollectionEndpoints_API.json
      - type: OpenAPI
        url: openapi/azure-monitor-data-collection-endpoints-openapi.yml
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-endpoint-overview
  - name: Azure Monitor Private Link Scopes API
    description: Create and manage Azure Monitor Private Link Scopes to connect Azure Monitor resources to private endpoints, enabling secure network access to monitoring data.
    image: https://azure.microsoft.com/svghandler/monitor/
    humanURL: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/private-link-security
    baseURL: https://management.azure.com
    tags:
      - Configuration
      - Networking
      - Private Link
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/monitor/private-link-scopes
      - type: OpenAPI
        url: openapi/azure-monitor-private-link-scopes-openapi.yml
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/private-link-configure
      - type: Reference
        url: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/private-link-design
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/azure-monitor/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/azure-monitor/overview
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/api/access-api
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/topics/monitor/
  - type: Change Log
    url: https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/whats-new
  - type: SDKs
    url: https://learn.microsoft.com/en-us/azure/azure-monitor/app/platforms
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/monitor/
  - type: Status
    url: https://status.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/options/
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://azure.microsoft.com/en-us/explore/trusted-cloud/privacy
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: Community
    url: https://techcommunity.microsoft.com/t5/azure-monitor/bd-p/AzureMonitor
  - type: Website
    url: https://azure.microsoft.com/en-us/products/monitor
  - type: Login
    url: https://portal.azure.com
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free
  - type: JSON-LD
    url: json-ld/azure-monitor-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
