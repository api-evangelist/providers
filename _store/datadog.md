---
aid: datadog
url: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/apis.yml
apis:
  - aid: datadog:datadog-api
    name: Datadog API
    tags:
      - Monitoring
      - Observability
    humanURL: https://docs.datadoghq.com/api/latest/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: openapi/datadog-api-openapi.yml
        type: OpenAPI
      - url: https://docs.datadoghq.com/api/latest/
        type: Documentation
      - url: https://docs.datadoghq.com/api/latest/authentication/
        type: Authentication
    description: The Datadog API is an HTTP REST API. The API uses resource-oriented URLs to call the API, uses status codes to indicate the success or failure of requests, returns JSON from all requests, and uses standard HTTP response codes. Use the Datadog API to access the Datadog platform programmatically.
  - aid: datadog:datadog-metrics-api
    name: Datadog Metrics API
    tags:
      - Metrics
      - Monitoring
      - Timeseries
    humanURL: https://docs.datadoghq.com/api/latest/metrics/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: openapi/datadog-metrics-openapi.yml
        type: OpenAPI
      - url: json-schema/datadog-metric-schema.json
        type: JSONSchema
      - url: https://docs.datadoghq.com/api/latest/metrics/
        type: Documentation
      - url: https://docs.datadoghq.com/metrics/
        type: Reference
    description: The Metrics API allows you to post metrics data to be graphed on Datadog dashboards, query metrics from any time period as timeseries or scalar values, and modify tag configurations for metrics. It also supports viewing tags and volumes for metrics.
  - aid: datadog:datadog-logs-api
    name: Datadog Logs API
    tags:
      - Log Management
      - Logs
      - Search
    humanURL: https://docs.datadoghq.com/api/latest/logs/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: openapi/datadog-logs-openapi.yml
        type: OpenAPI
      - url: json-schema/datadog-log-event-schema.json
        type: JSONSchema
      - url: https://docs.datadoghq.com/api/latest/logs/
        type: Documentation
      - url: https://docs.datadoghq.com/logs/
        type: Reference
    description: The Logs API allows you to search and send log events to the Datadog platform over HTTP. It supports querying and aggregating log data from the Log Management product.
  - aid: datadog:datadog-events-api
    name: Datadog Events API
    tags:
      - Event Management
      - Events
    humanURL: https://docs.datadoghq.com/api/latest/events/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: openapi/datadog-events-openapi.yml
        type: OpenAPI
      - url: json-schema/datadog-event-schema.json
        type: JSONSchema
      - url: https://docs.datadoghq.com/api/latest/events/
        type: Documentation
      - url: https://docs.datadoghq.com/service_management/events/
        type: Reference
    description: The Event Management API allows you to programmatically post events to the Events Explorer and fetch events from the Events Explorer. Events represent notable changes or activity within your monitored infrastructure.
  - aid: datadog:datadog-monitors-api
    name: Datadog Monitors API
    tags:
      - Alerting
      - Monitors
      - Notifications
    humanURL: https://docs.datadoghq.com/api/latest/monitors/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: openapi/datadog-monitors-openapi.yml
        type: OpenAPI
      - url: json-schema/datadog-monitor-schema.json
        type: JSONSchema
      - url: https://docs.datadoghq.com/api/latest/monitors/
        type: Documentation
      - url: https://docs.datadoghq.com/monitors/
        type: Reference
    description: The Monitors API allows you to create, update, delete, and mute monitors that watch a metric or check and notify your team when a defined threshold has been exceeded.
  - aid: datadog:datadog-dashboards-api
    name: Datadog Dashboards API
    tags:
      - Dashboards
      - Visualizations
    humanURL: https://docs.datadoghq.com/api/latest/dashboards/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/dashboards/
        type: Documentation
      - url: https://docs.datadoghq.com/dashboards/
        type: Reference
    description: The Dashboards API allows you to create, update, delete, and retrieve dashboards and dashboard lists. It also supports organizing, finding, and sharing dashboards with your team and organization.
  - aid: datadog:datadog-incidents-api
    name: Datadog Incidents API
    tags:
      - Incident Management
      - Incidents
    humanURL: https://docs.datadoghq.com/api/latest/incidents/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: openapi/datadog-incidents-openapi.yml
        type: OpenAPI
      - url: https://docs.datadoghq.com/api/latest/incidents/
        type: Documentation
      - url: https://docs.datadoghq.com/service_management/incident_management/
        type: Reference
    description: The Incidents API allows you to manage incident response, as well as associated attachments, metadata, and todos. It also supports creating, updating, deleting, and retrieving services associated with incidents.
  - aid: datadog:datadog-synthetics-api
    name: Datadog Synthetics API
    tags:
      - Synthetics
      - Testing
      - Uptime
    humanURL: https://docs.datadoghq.com/api/latest/synthetics/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/synthetics/
        type: Documentation
      - url: https://docs.datadoghq.com/synthetics/
        type: Reference
    description: The Synthetics API allows you to manage API tests and browser tests programmatically. Datadog Synthetics uses simulated user requests and browser rendering to help ensure uptime, identify regional issues, and track application performance.
  - aid: datadog:datadog-service-level-objectives-api
    name: Datadog Service Level Objectives API
    tags:
      - Reliability
      - Service Level Objectives
      - SLOs
    humanURL: https://docs.datadoghq.com/api/latest/service-level-objectives/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/service-level-objectives/
        type: Documentation
      - url: https://docs.datadoghq.com/monitors/service_level_objectives/
        type: Reference
    description: The Service Level Objectives API provides a framework for defining clear targets around application performance. SLOs help teams provide a consistent customer experience, balance feature development with platform stability, and improve communication with internal and external users.
  - aid: datadog:datadog-security-monitoring-api
    name: Datadog Security Monitoring API
    tags:
      - Security
      - Security Monitoring
      - SIEM
    humanURL: https://docs.datadoghq.com/api/latest/security-monitoring/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/security-monitoring/
        type: Documentation
      - url: https://docs.datadoghq.com/security/
        type: Reference
    description: The Security Monitoring API allows you to create and manage security rules, signals, and filters. It provides programmatic access to Datadog Cloud SIEM capabilities for threat detection and security signal management.
  - aid: datadog:datadog-service-definition-api
    name: Datadog Service Definition API
    tags:
      - Service Catalog
    humanURL: https://docs.datadoghq.com/api/latest/service-definition/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/service-definition/
        type: Documentation
      - url: https://docs.datadoghq.com/tracing/service_catalog/
        type: Reference
    description: The Service Definition API allows you to create, update, retrieve, and delete service definitions in the Datadog Service Catalog. It supports the v2.2 schema and earlier; for v3.0 schema use the Software Catalog endpoints.
  - aid: datadog:datadog-software-catalog-api
    name: Datadog Software Catalog API
    tags:
      - Software Catalog
    humanURL: https://docs.datadoghq.com/api/latest/software-catalog/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/software-catalog/
        type: Documentation
      - url: https://docs.datadoghq.com/service_catalog/
        type: Reference
    description: The Software Catalog API allows you to create, update, retrieve, and delete Software Catalog entities using the v3.0 schema. It provides a unified catalog for tracking ownership, reliability, and performance of all software components.
  - aid: datadog:datadog-users-api
    name: Datadog Users API
    tags:
      - Account Management
      - Users
    humanURL: https://docs.datadoghq.com/api/latest/users/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/users/
        type: Documentation
      - url: https://docs.datadoghq.com/account_management/users/
        type: Reference
    description: The Users API allows you to create, edit, and disable users within your Datadog organization. It supports role assignment and user management for access control purposes.
  - aid: datadog:datadog-roles-api
    name: Datadog Roles API
    tags:
      - Access Control
      - RBAC
      - Roles
    humanURL: https://docs.datadoghq.com/api/latest/roles/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/roles/
        type: Documentation
      - url: https://docs.datadoghq.com/account_management/rbac/
        type: Reference
    description: The Roles API is used to create and manage Datadog roles, the global permissions they grant, and which users belong to them. Roles provide role-based access control for Datadog resources and features.
  - aid: datadog:datadog-key-management-api
    name: Datadog Key Management API
    tags:
      - API Keys
      - Application Keys
      - Authentication
    humanURL: https://docs.datadoghq.com/api/latest/key-management/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/key-management/
        type: Documentation
      - url: https://docs.datadoghq.com/account_management/api-app-keys/
        type: Reference
    description: The Key Management API allows you to manage your Datadog API and application keys. It provides endpoints to create, list, update, and delete both API keys and application keys for your organization.
  - aid: datadog:datadog-organizations-api
    name: Datadog Organizations API
    tags:
      - Account Management
      - Organizations
    humanURL: https://docs.datadoghq.com/api/latest/organizations/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/organizations/
        type: Documentation
      - url: https://docs.datadoghq.com/account_management/multi_organization/
        type: Reference
    description: The Organizations API allows you to create, edit, and manage your Datadog organizations. It supports multi-org account configurations where a parent organization manages one or more child organizations.
  - aid: datadog:datadog-downtimes-api
    name: Datadog Downtimes API
    tags:
      - Alerting
      - Downtimes
      - Monitors
    humanURL: https://docs.datadoghq.com/api/latest/downtimes/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/downtimes/
        type: Documentation
      - url: https://docs.datadoghq.com/monitors/notify/downtimes/
        type: Reference
    description: The Downtimes API gives you greater control over monitor notifications by allowing you to globally exclude scopes from alerting. Downtime settings can be scheduled with start and end times to prevent alerting for specified Datadog tags.
  - aid: datadog:datadog-rum-api
    name: Datadog RUM API
    tags:
      - Real User Monitoring
      - RUM
      - Session Replay
    humanURL: https://docs.datadoghq.com/api/latest/rum/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/rum/
        type: Documentation
      - url: https://docs.datadoghq.com/real_user_monitoring/
        type: Reference
    description: The RUM API allows you to manage Real User Monitoring applications and search or aggregate RUM events over HTTP. It provides access to session data, user interactions, and frontend performance metrics.
  - aid: datadog:datadog-apm-retention-filters-api
    name: Datadog APM Retention Filters API
    tags:
      - APM
      - Retention
      - Tracing
    humanURL: https://docs.datadoghq.com/api/latest/apm-retention-filters/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/apm-retention-filters/
        type: Documentation
      - url: https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention/
        type: Reference
    description: The APM Retention Filters API allows you to manage configuration of APM retention filters for your organization. Retention filters control which traces are indexed and retained for analysis and require Admin rights to interact with.
  - aid: datadog:datadog-usage-metering-api
    name: Datadog Usage Metering API
    tags:
      - Billing
      - Metering
      - Usage
    humanURL: https://docs.datadoghq.com/api/latest/usage-metering/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/usage-metering/
        type: Documentation
      - url: https://docs.datadoghq.com/account_management/billing/usage_details/
        type: Reference
    description: The Usage Metering API allows you to get hourly, daily, and monthly usage across multiple facets of Datadog. It is available to all Pro and Enterprise customers, with usage data delayed by up to 72 hours.
  - aid: datadog:datadog-spans-api
    name: Datadog Spans API
    tags:
      - APM
      - Spans
      - Tracing
    humanURL: https://docs.datadoghq.com/api/latest/spans/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/spans/
        type: Documentation
      - url: https://docs.datadoghq.com/tracing/
        type: Reference
    description: The Spans API allows you to search and aggregate spans from your Datadog platform over HTTP. It supports querying distributed tracing data collected by Datadog APM.
  - aid: datadog:datadog-processes-api
    name: Datadog Processes API
    tags:
      - Infrastructure
      - Processes
    humanURL: https://docs.datadoghq.com/api/latest/processes/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/processes/
        type: Documentation
      - url: https://docs.datadoghq.com/infrastructure/process/
        type: Reference
    description: The Processes API allows you to query processes data for your organization. It provides access to live process information collected from hosts running the Datadog Agent.
  - aid: datadog:datadog-teams-api
    name: Datadog Teams API
    tags:
      - Account Management
      - Teams
    humanURL: https://docs.datadoghq.com/api/latest/teams/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/teams/
        type: Documentation
      - url: https://docs.datadoghq.com/account_management/teams/
        type: Reference
    description: The Teams API allows you to view and manage teams within Datadog. Teams can be associated with incidents, dashboards, and other resources to organize ownership and collaboration within your organization.
  - aid: datadog:datadog-workflow-automation-api
    name: Datadog Workflow Automation API
    tags:
      - Automation
      - Workflows
    humanURL: https://docs.datadoghq.com/api/latest/workflow-automation/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/workflow-automation/
        type: Documentation
      - url: https://docs.datadoghq.com/service_management/workflows/
        type: Reference
    description: The Workflow Automation API allows you to automate end-to-end processes by connecting Datadog with the rest of your tech stack. It supports over 1,000 out-of-the-box actions including integrations with AWS, JIRA, ServiceNow, GitHub, and OpenAI.
  - aid: datadog:datadog-case-management-api
    name: Datadog Case Management API
    tags:
      - Case Management
      - Cases
    humanURL: https://docs.datadoghq.com/api/latest/case-management/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/case-management/
        type: Documentation
      - url: https://docs.datadoghq.com/service_management/case_management/
        type: Reference
    description: The Case Management API allows you to view and manage cases and projects within Datadog Case Management. Cases can be created from monitors, security signals, and other alert sources to track investigation and remediation work.
  - aid: datadog:datadog-observability-pipelines-api
    name: Datadog Observability Pipelines API
    tags:
      - Logs
      - Observability Pipelines
    humanURL: https://docs.datadoghq.com/api/latest/observability-pipelines/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/observability-pipelines/
        type: Documentation
      - url: https://docs.datadoghq.com/observability_pipelines/
        type: Reference
    description: The Observability Pipelines API allows you to collect and process logs within your own infrastructure and route them to downstream integrations. It provides programmatic management of pipeline configurations.
  - aid: datadog:datadog-sensitive-data-scanner-api
    name: Datadog Sensitive Data Scanner API
    tags:
      - Data Privacy
      - Security
      - Sensitive Data
    humanURL: https://docs.datadoghq.com/api/latest/sensitive-data-scanner/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/sensitive-data-scanner/
        type: Documentation
      - url: https://docs.datadoghq.com/sensitive_data_scanner/
        type: Reference
    description: The Sensitive Data Scanner API allows you to create, update, delete, and retrieve sensitive data scanner groups and rules. It enables automated detection and redaction of sensitive data within logs, APM events, and RUM events.
  - aid: datadog:datadog-aws-integration-api
    name: Datadog AWS Integration API
    tags:
      - AWS
      - Cloud
      - Integrations
    humanURL: https://docs.datadoghq.com/api/latest/aws-integration/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/aws-integration/
        type: Documentation
      - url: https://docs.datadoghq.com/integrations/amazon_web_services/
        type: Reference
    description: The AWS Integration API allows you to configure your Datadog-AWS integration directly through the Datadog API. It supports managing AWS accounts, metrics collection, and log forwarding configuration.
  - aid: datadog:datadog-gcp-integration-api
    name: Datadog GCP Integration API
    tags:
      - Cloud
      - GCP
      - Google Cloud
      - Integrations
    humanURL: https://docs.datadoghq.com/api/latest/gcp-integration/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/gcp-integration/
        type: Documentation
      - url: https://docs.datadoghq.com/integrations/google_cloud_platform/
        type: Reference
    description: The GCP Integration API allows you to configure your Datadog-Google Cloud Platform integration directly through the Datadog API. It supports managing GCP projects, service accounts, and metrics collection settings.
  - aid: datadog:datadog-ci-visibility-pipelines-api
    name: Datadog CI Visibility Pipelines API
    tags:
      - CI
      - CI/CD
      - Pipelines
    humanURL: https://docs.datadoghq.com/api/latest/ci-visibility-pipelines/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/ci-visibility-pipelines/
        type: Documentation
      - url: https://docs.datadoghq.com/continuous_integration/pipelines/
        type: Reference
    description: The CI Visibility Pipelines API allows you to search or aggregate CI Visibility pipeline events and send them to your Datadog site over HTTP. It provides insight into the performance and reliability of CI/CD pipelines.
  - aid: datadog:datadog-network-device-monitoring-api
    name: Datadog Network Device Monitoring API
    tags:
      - Infrastructure
      - Network
      - Network Device Monitoring
    humanURL: https://docs.datadoghq.com/api/latest/network-device-monitoring/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/network-device-monitoring/
        type: Documentation
      - url: https://docs.datadoghq.com/network_monitoring/
        type: Reference
    description: The Network Device Monitoring API allows you to fetch devices and interfaces and their attributes. It provides programmatic access to network topology and performance data collected from network devices.
  - aid: datadog:datadog-on-call-api
    name: Datadog On-Call API
    tags:
      - Incident Management
      - On-Call
      - Paging
    humanURL: https://docs.datadoghq.com/api/latest/on-call/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/on-call/
        type: Documentation
      - url: https://docs.datadoghq.com/service_management/on-call/
        type: Reference
    description: The On-Call API allows you to configure and manage Datadog On-Call schedules, escalation policies, and teams. It also supports triggering and managing on-call pages directly through the Datadog API.
  - aid: datadog:datadog-dora-metrics-api
    name: Datadog DORA Metrics API
    tags:
      - CI/CD
      - DevOps
      - DORA Metrics
    humanURL: https://docs.datadoghq.com/api/latest/dora-metrics/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/dora-metrics/
        type: Documentation
      - url: https://docs.datadoghq.com/dora_metrics/
        type: Reference
    description: The DORA Metrics API allows you to search and send events for DORA Metrics to measure and improve software delivery performance. It tracks deployment frequency, lead time for changes, change failure rate, and time to restore service.
  - aid: datadog:datadog-cloud-cost-management-api
    name: Datadog Cloud Cost Management API
    tags:
      - Cloud
      - Cloud Cost Management
      - FinOps
    humanURL: https://docs.datadoghq.com/api/latest/cloud-cost-management/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/cloud-cost-management/
        type: Documentation
      - url: https://docs.datadoghq.com/cloud_cost_management/
        type: Reference
    description: The Cloud Cost Management API allows you to set up, edit, and delete Cloud Cost Management accounts for AWS and Azure. Cost data can be queried using the Metrics endpoint with the cloud_cost data source.
  - aid: datadog:datadog-hosts-api
    name: Datadog Hosts API
    tags:
      - Hosts
      - Infrastructure
    humanURL: https://docs.datadoghq.com/api/latest/hosts/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/hosts/
        type: Documentation
      - url: https://docs.datadoghq.com/infrastructure/
        type: Reference
    description: The Hosts API allows you to search for hosts by name, alias, or tag and retrieve host totals. Hosts live within the past 3 hours are included by default, with a retention of 7 days.
  - aid: datadog:datadog-tags-api
    name: Datadog Tags API
    tags:
      - Infrastructure
    humanURL: https://docs.datadoghq.com/api/latest/tags/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/tags/
        type: Documentation
      - url: https://docs.datadoghq.com/getting_started/tagging/
        type: Reference
    description: The Tags API allows you to assign tags to hosts, returning a mapping of tags to hosts for your entire infrastructure. Tags can be used to filter and group resources across Datadog.
  - aid: datadog:datadog-containers-api
    name: Datadog Containers API
    tags:
      - Containers
      - Infrastructure
    humanURL: https://docs.datadoghq.com/api/latest/containers/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/containers/
        type: Documentation
      - url: https://docs.datadoghq.com/infrastructure/containers/
        type: Reference
    description: The Containers API allows you to get all containers for your organization. It provides programmatic access to container data collected from hosts running the Datadog Agent.
  - aid: datadog:datadog-container-images-api
    name: Datadog Container Images API
    tags:
      - Container Images
      - Containers
      - Infrastructure
    humanURL: https://docs.datadoghq.com/api/latest/container-images/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/container-images/
        type: Documentation
      - url: https://docs.datadoghq.com/infrastructure/containers/container_images/
        type: Reference
    description: The Container Images API allows you to get all container images for your organization. It provides visibility into the container images running across your infrastructure.
  - aid: datadog:datadog-notebooks-api
    name: Datadog Notebooks API
    tags:
      - Collaboration
      - Notebooks
    humanURL: https://docs.datadoghq.com/api/latest/notebooks/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/notebooks/
        type: Documentation
      - url: https://docs.datadoghq.com/notebooks/
        type: Reference
    description: The Notebooks API allows you to interact with Datadog Notebooks programmatically. Notebooks combine graphs and text in a linear, cell-based layout for exploring and sharing stories with your data.
  - aid: datadog:datadog-dashboard-lists-api
    name: Datadog Dashboard Lists API
    tags:
      - Dashboard Lists
      - Dashboards
    humanURL: https://docs.datadoghq.com/api/latest/dashboard-lists/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/dashboard-lists/
        type: Documentation
      - url: https://docs.datadoghq.com/dashboards/
        type: Reference
    description: The Dashboard Lists API allows you to interact with dashboard lists through the API to organize, find, and share all of your dashboards with your team and organization.
  - aid: datadog:datadog-logs-pipelines-api
    name: Datadog Logs Pipelines API
    tags:
      - Log Processing
      - Logs
      - Pipelines
    humanURL: https://docs.datadoghq.com/api/latest/logs-pipelines/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/logs-pipelines/
        type: Documentation
      - url: https://docs.datadoghq.com/logs/log_configuration/pipelines/
        type: Reference
    description: The Logs Pipelines API allows you to manage pipelines and processors that operate on incoming logs, parsing and transforming them into structured attributes for easier querying.
  - aid: datadog:datadog-logs-indexes-api
    name: Datadog Logs Indexes API
    tags:
      - Indexes
      - Log Management
      - Logs
    humanURL: https://docs.datadoghq.com/api/latest/logs-indexes/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/logs-indexes/
        type: Documentation
      - url: https://docs.datadoghq.com/logs/log_configuration/indexes/
        type: Reference
    description: The Logs Indexes API allows you to manage configuration of log indexes for your organization. Log indexes define how logs are filtered, aggregated, and stored for retention and querying.
  - aid: datadog:datadog-logs-metrics-api
    name: Datadog Logs Metrics API
    tags:
      - Log-Based Metrics
      - Logs
      - Metrics
    humanURL: https://docs.datadoghq.com/api/latest/logs-metrics/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/logs-metrics/
        type: Documentation
      - url: https://docs.datadoghq.com/logs/log_configuration/logs_to_metrics/
        type: Reference
    description: The Logs Metrics API allows you to manage configuration of log-based metrics for your organization. It provides the ability to generate metrics from log data for cost-effective long-term analysis.
  - aid: datadog:datadog-logs-archives-api
    name: Datadog Logs Archives API
    tags:
      - Archives
      - Logs
      - Storage
    humanURL: https://docs.datadoghq.com/api/latest/logs-archives/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/logs-archives/
        type: Documentation
      - url: https://docs.datadoghq.com/logs/log_configuration/archives/
        type: Reference
    description: The Logs Archives API allows you to manage logs archives that forward all ingested logs to cloud storage systems. It supports configuration of archive destinations and rehydration settings.
  - aid: datadog:datadog-logs-custom-destinations-api
    name: Datadog Logs Custom Destinations API
    tags:
      - Custom Destinations
      - Log Forwarding
      - Logs
    humanURL: https://docs.datadoghq.com/api/latest/logs-custom-destinations/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/logs-custom-destinations/
        type: Documentation
    description: The Logs Custom Destinations API allows you to manage custom destinations that forward all ingested logs to external destinations such as Elasticsearch, Microsoft Sentinel, and HTTP endpoints.
  - aid: datadog:datadog-logs-restriction-queries-api
    name: Datadog Logs Restriction Queries API
    tags:
      - Access Control
      - Logs
      - RBAC
    humanURL: https://docs.datadoghq.com/api/latest/logs-restriction-queries/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/logs-restriction-queries/
        type: Documentation
    description: The Logs Restriction Queries API allows you to manage restriction queries that control which logs the logs_read_data permission grants read access to, enabling fine-grained log access control by role.
  - aid: datadog:datadog-spans-metrics-api
    name: Datadog Spans Metrics API
    tags:
      - APM
      - Metrics
      - Spans
    humanURL: https://docs.datadoghq.com/api/latest/spans-metrics/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/spans-metrics/
        type: Documentation
    description: The Spans Metrics API allows you to manage configuration of span-based metrics for your organization. It provides the ability to generate metrics from spans for cost-effective long-term analysis of APM data.
  - aid: datadog:datadog-service-checks-api
    name: Datadog Service Checks API
    tags:
      - Monitoring
      - Service Checks
    humanURL: https://docs.datadoghq.com/api/latest/service-checks/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/service-checks/
        type: Documentation
    description: The Service Checks API allows you to submit a list of service checks to Datadog. Service checks can be submitted up to 10 minutes in the past and are used to monitor the status of services.
  - aid: datadog:datadog-snapshots-api
    name: Datadog Snapshots API
    tags:
      - Graphs
      - Snapshots
      - Visualizations
    humanURL: https://docs.datadoghq.com/api/latest/snapshots/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/snapshots/
        type: Documentation
    description: The Snapshots API allows you to take graph snapshots. Snapshots are PNG images generated by rendering a specified widget and capturing it once the data is available.
  - aid: datadog:datadog-ip-ranges-api
    name: Datadog IP Ranges API
    tags:
      - Infrastructure
      - IP Ranges
      - Network
    humanURL: https://docs.datadoghq.com/api/latest/ip-ranges/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/ip-ranges/
        type: Documentation
    description: The IP Ranges API provides a list of IP prefixes belonging to Datadog. It returns available prefix information for Agent, API, and APM endpoints along with IPv4 and IPv6 prefixes.
  - aid: datadog:datadog-ip-allowlist-api
    name: Datadog IP Allowlist API
    tags:
      - Access Control
      - IP Allowlist
      - Security
    humanURL: https://docs.datadoghq.com/api/latest/ip-allowlist/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/ip-allowlist/
        type: Documentation
    description: The IP Allowlist API is used to manage the IP addresses that can access the Datadog API and web UI. It allows you to configure IP address restrictions for your organization.
  - aid: datadog:datadog-audit-api
    name: Datadog Audit API
    tags:
      - Audit
      - Audit Logs
      - Compliance
    humanURL: https://docs.datadoghq.com/api/latest/audit/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/audit/
        type: Documentation
      - url: https://docs.datadoghq.com/account_management/audit_trail/
        type: Reference
    description: The Audit API allows you to search your Audit Logs events over HTTP. It returns Audit Logs events that match an audit search query, providing visibility into actions taken within your organization.
  - aid: datadog:datadog-apm-api
    name: Datadog APM API
    tags:
      - APM
      - Application Performance
      - Tracing
    humanURL: https://docs.datadoghq.com/api/latest/apm/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/apm/
        type: Documentation
      - url: https://docs.datadoghq.com/tracing/
        type: Reference
    description: The APM API provides endpoints for working with Application Performance Monitoring services and tracing data. It supports querying service-level metrics and trace data collected by Datadog APM.
  - aid: datadog:datadog-webhooks-integration-api
    name: Datadog Webhooks Integration API
    tags:
      - Integrations
      - Notifications
      - Webhooks
    humanURL: https://docs.datadoghq.com/api/latest/webhooks-integration/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/webhooks-integration/
        type: Documentation
      - url: https://docs.datadoghq.com/integrations/webhooks/
        type: Reference
    description: The Webhooks Integration API allows you to configure the Datadog-Webhooks integration directly through the Datadog API. It supports creating, updating, and deleting webhook endpoints and custom variables.
  - aid: datadog:datadog-slo-corrections-api
    name: Datadog SLO Corrections API
    tags:
      - Reliability
      - SLO Corrections
      - SLOs
    humanURL: https://docs.datadoghq.com/api/latest/service-level-objective-corrections/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/service-level-objective-corrections/
        type: Documentation
    description: The SLO Corrections API allows you to create, update, and delete corrections for Service Level Objectives. SLO corrections adjust SLO status calculations to account for planned maintenance or known issues.
  - aid: datadog:datadog-aws-logs-integration-api
    name: Datadog AWS Logs Integration API
    tags:
      - AWS
      - Integrations
      - Logs
    humanURL: https://docs.datadoghq.com/api/latest/aws-logs-integration/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/aws-logs-integration/
        type: Documentation
      - url: https://docs.datadoghq.com/integrations/amazon_web_services/#log-collection
        type: Reference
    description: The AWS Logs Integration API allows you to configure log collection from AWS services and manage your Datadog-AWS Logs integration. It supports listing and managing AWS log collection configurations.
  - aid: datadog:datadog-azure-integration-api
    name: Datadog Azure Integration API
    tags:
      - Azure
      - Cloud
      - Integrations
    humanURL: https://docs.datadoghq.com/api/latest/azure-integration/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/azure-integration/
        type: Documentation
      - url: https://docs.datadoghq.com/integrations/azure/
        type: Reference
    description: The Azure Integration API allows you to configure your Datadog-Azure integration directly through the Datadog API. It supports managing Azure tenants, host filters, and metrics collection settings.
  - aid: datadog:datadog-slack-integration-api
    name: Datadog Slack Integration API
    tags:
      - Integrations
      - Notifications
      - Slack
    humanURL: https://docs.datadoghq.com/api/latest/slack-integration/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/slack-integration/
        type: Documentation
      - url: https://docs.datadoghq.com/integrations/slack/
        type: Reference
    description: The Slack Integration API allows you to configure your Datadog-Slack integration directly through the Datadog API. It supports managing Slack channels for monitor notifications and alerts.
  - aid: datadog:datadog-pagerduty-integration-api
    name: Datadog PagerDuty Integration API
    tags:
      - Incident Management
      - Integrations
      - PagerDuty
    humanURL: https://docs.datadoghq.com/api/latest/pagerduty-integration/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/pagerduty-integration/
        type: Documentation
      - url: https://docs.datadoghq.com/integrations/pagerduty/
        type: Reference
    description: The PagerDuty Integration API allows you to configure your Datadog-PagerDuty integration directly through the Datadog API. It supports managing PagerDuty services and scheduling configurations.
  - aid: datadog:datadog-opsgenie-integration-api
    name: Datadog Opsgenie Integration API
    tags:
      - Incident Management
      - Integrations
      - Opsgenie
    humanURL: https://docs.datadoghq.com/api/latest/opsgenie-integration/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/opsgenie-integration/
        type: Documentation
    description: The Opsgenie Integration API allows you to configure your Datadog-Opsgenie integration directly through the Datadog API. It supports managing Opsgenie services and alert routing.
  - aid: datadog:datadog-cloudflare-integration-api
    name: Datadog Cloudflare Integration API
    tags:
      - CDN
      - Cloudflare
      - Integrations
    humanURL: https://docs.datadoghq.com/api/latest/cloudflare-integration/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/cloudflare-integration/
        type: Documentation
      - url: https://docs.datadoghq.com/integrations/cloudflare/
        type: Reference
    description: The Cloudflare Integration API allows you to manage your Datadog-Cloudflare integration directly through the Datadog API. It supports listing and managing Cloudflare accounts and their associated resources.
  - aid: datadog:datadog-fastly-integration-api
    name: Datadog Fastly Integration API
    tags:
      - CDN
      - Fastly
      - Integrations
    humanURL: https://docs.datadoghq.com/api/latest/fastly-integration/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/fastly-integration/
        type: Documentation
    description: The Fastly Integration API allows you to manage your Datadog-Fastly integration accounts and services directly through the Datadog API. It supports listing and managing Fastly accounts.
  - aid: datadog:datadog-confluent-cloud-api
    name: Datadog Confluent Cloud API
    tags:
      - Confluent Cloud
      - Integrations
      - Kafka
    humanURL: https://docs.datadoghq.com/api/latest/confluent-cloud/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/confluent-cloud/
        type: Documentation
    description: The Confluent Cloud API allows you to manage your Datadog-Confluent Cloud integration accounts and account resources directly through the Datadog API. It supports monitoring Kafka clusters and related services.
  - aid: datadog:datadog-okta-integration-api
    name: Datadog Okta Integration API
    tags:
      - Identity
      - Integrations
      - Okta
    humanURL: https://docs.datadoghq.com/api/latest/okta-integration/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/okta-integration/
        type: Documentation
      - url: https://docs.datadoghq.com/integrations/okta/
        type: Reference
    description: The Okta Integration API allows you to configure your Datadog-Okta integration directly through the Datadog API. It supports listing and managing Okta accounts and their configurations.
  - aid: datadog:datadog-microsoft-teams-integration-api
    name: Datadog Microsoft Teams Integration API
    tags:
      - Integrations
      - Microsoft Teams
      - Notifications
    humanURL: https://docs.datadoghq.com/api/latest/microsoft-teams-integration/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/microsoft-teams-integration/
        type: Documentation
      - url: https://docs.datadoghq.com/integrations/microsoft-teams/
        type: Reference
    description: The Microsoft Teams Integration API allows you to configure your Datadog-Microsoft Teams integration directly through the Datadog API. It supports managing Teams channels for notifications and alerts.
  - aid: datadog:datadog-jira-integration-api
    name: Datadog Jira Integration API
    tags:
      - Integrations
      - Issue Tracking
      - Jira
    humanURL: https://docs.datadoghq.com/api/latest/jira-integration/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/jira-integration/
        type: Documentation
      - url: https://docs.datadoghq.com/integrations/jira/
        type: Reference
    description: The Jira Integration API allows you to configure your Datadog-Jira integration directly through the Datadog API. It supports managing Jira issue templates and project configurations.
  - aid: datadog:datadog-error-tracking-api
    name: Datadog Error Tracking API
    tags:
      - Debugging
      - Error Tracking
    humanURL: https://docs.datadoghq.com/api/latest/error-tracking/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/error-tracking/
        type: Documentation
      - url: https://docs.datadoghq.com/error_tracking/
        type: Reference
    description: The Error Tracking API allows you to search issues within your organization programmatically. It returns a list of issues that match a given search query using event search syntax.
  - aid: datadog:datadog-application-security-api
    name: Datadog Application Security API
    tags:
      - Application Security
      - AppSec
      - Security
    humanURL: https://docs.datadoghq.com/api/latest/application-security/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/application-security/
        type: Documentation
      - url: https://docs.datadoghq.com/security/application_security/
        type: Reference
    description: The Application Security API provides protection against application-level attacks that aim to exploit code-level vulnerabilities such as SSRF, SQL injection, Log4Shell, and XSS.
  - aid: datadog:datadog-csm-threats-api
    name: Datadog CSM Threats API
    tags:
      - Cloud Security
      - CSM
      - Threats
    humanURL: https://docs.datadoghq.com/api/latest/csm-threats/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/csm-threats/
        type: Documentation
      - url: https://docs.datadoghq.com/security/cloud_security_management/
        type: Reference
    description: The CSM Threats API provides endpoints for managing Cloud Security Management Workload Protection agent rules. It monitors file, network, and process activity to detect real-time threats to your infrastructure.
  - aid: datadog:datadog-csm-agents-api
    name: Datadog CSM Agents API
    tags:
      - Agents
      - Cloud Security
      - CSM
    humanURL: https://docs.datadoghq.com/api/latest/csm-agents/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/csm-agents/
        type: Documentation
    description: The CSM Agents API allows you to get the list of all Cloud Security Management agents running on your hosts and containers. It provides visibility into agent coverage across your infrastructure.
  - aid: datadog:datadog-service-scorecards-api
    name: Datadog Service Scorecards API
    tags:
      - Best Practices
      - Scorecards
      - Service Catalog
    humanURL: https://docs.datadoghq.com/api/latest/service-scorecards/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/service-scorecards/
        type: Documentation
      - url: https://docs.datadoghq.com/internal_developer_portal/scorecards/
        type: Reference
    description: The Service Scorecards API allows you to create and manage scorecard rules and outcomes. Scorecards help formalize your organization's best practices and track service compliance against defined criteria.
  - aid: datadog:datadog-service-dependencies-api
    name: Datadog Service Dependencies API
    tags:
      - APM
      - Dependencies
    humanURL: https://docs.datadoghq.com/api/latest/service-dependencies/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/service-dependencies/
        type: Documentation
    description: The Service Dependencies API allows you to get a list of services from APM and their dependencies. Services are filtered by environment and primary tag to map your service topology.
  - aid: datadog:datadog-powerpack-api
    name: Datadog Powerpack API
    tags:
      - Dashboards
      - Powerpacks
      - Widgets
    humanURL: https://docs.datadoghq.com/api/latest/powerpack/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/powerpack/
        type: Documentation
      - url: https://docs.datadoghq.com/dashboards/widgets/powerpack/
        type: Reference
    description: The Powerpack API allows you to create, update, delete, and retrieve Powerpacks. Powerpacks are templated groups of dashboard widgets that scale graphing expertise as reusable building blocks.
  - aid: datadog:datadog-embeddable-graphs-api
    name: Datadog Embeddable Graphs API
    tags:
      - Embeds
      - Graphs
      - Visualizations
    humanURL: https://docs.datadoghq.com/api/latest/embeddable-graphs/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/embeddable-graphs/
        type: Documentation
    description: The Embeddable Graphs API allows you to create and manage embeddable graph snapshots that can be shared outside of Datadog. It supports creating, revoking, and listing embeddable graphs.
  - aid: datadog:datadog-rum-metrics-api
    name: Datadog RUM Metrics API
    tags:
      - Metrics
      - Real User Monitoring
      - RUM
    humanURL: https://docs.datadoghq.com/api/latest/rum-metrics/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/rum-metrics/
        type: Documentation
      - url: https://docs.datadoghq.com/real_user_monitoring/
        type: Reference
    description: The RUM Metrics API allows you to manage configuration of RUM-based metrics for your organization. It provides the ability to generate metrics from Real User Monitoring data.
  - aid: datadog:datadog-domain-allowlist-api
    name: Datadog Domain Allowlist API
    tags:
      - Access Control
      - Domain Allowlist
      - Security
    humanURL: https://docs.datadoghq.com/api/latest/domain-allowlist/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/domain-allowlist/
        type: Documentation
    description: The Domain Allowlist API allows you to manage the email domain allowlist for your organization. It supports getting and updating the list of allowed email domains.
  - aid: datadog:datadog-restriction-policies-api
    name: Datadog Restriction Policies API
    tags:
      - Access Control
      - RBAC
      - Restriction Policies
    humanURL: https://docs.datadoghq.com/api/latest/restriction-policies/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/restriction-policies/
        type: Documentation
    description: The Restriction Policies API allows you to manage restriction policies associated with Datadog resources including dashboards, notebooks, security rules, SLOs, workflows, and more.
  - aid: datadog:datadog-authn-mappings-api
    name: Datadog AuthN Mappings API
    tags:
      - Authentication
      - Identity
      - Mappings
    humanURL: https://docs.datadoghq.com/api/latest/authn-mappings/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/authn-mappings/
        type: Documentation
      - url: https://docs.datadoghq.com/account_management/authn_mapping/
        type: Reference
    description: The AuthN Mappings API is used to automatically map groups of users to roles in Datadog using attributes sent from Identity Providers. It enables federated authentication to role mapping.
  - aid: datadog:datadog-integrations-api
    name: Datadog Integrations API
    tags:
      - Integrations
    humanURL: https://docs.datadoghq.com/api/latest/integrations/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/integrations/
        type: Documentation
      - url: https://docs.datadoghq.com/integrations/
        type: Reference
    description: The Integrations API allows you to manage Datadog integrations programmatically. It provides endpoints for configuring and managing third-party service integrations within your organization.
  - aid: datadog:datadog-ci-visibility-tests-api
    name: Datadog CI Visibility Tests API
    tags:
      - CI
      - CI/CD
      - Tests
    humanURL: https://docs.datadoghq.com/api/latest/ci-visibility-tests/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/ci-visibility-tests/
        type: Documentation
      - url: https://docs.datadoghq.com/continuous_integration/tests/
        type: Reference
    description: The CI Visibility Tests API allows you to search or aggregate CI Visibility test events over HTTP. It provides insight into the performance and reliability of your test suites.
  - aid: datadog:datadog-agentless-scanning-api
    name: Datadog Agentless Scanning API
    tags:
      - Agentless Scanning
      - Cloud Security
      - Vulnerabilities
    humanURL: https://docs.datadoghq.com/api/latest/agentless-scanning/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/agentless-scanning/
        type: Documentation
      - url: https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning/
        type: Reference
    description: The Agentless Scanning API provides visibility into risks and vulnerabilities within your hosts, running containers, and serverless functions without requiring teams to install Agents.
  - aid: datadog:datadog-static-analysis-api
    name: Datadog Static Analysis API
    tags:
      - Code Quality
      - Security
      - Static Analysis
    humanURL: https://docs.datadoghq.com/api/latest/static-analysis/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/static-analysis/
        type: Documentation
    description: The Static Analysis API provides access to static analysis and dependency scanning results. It supports querying code analysis data for your organization.
  - aid: datadog:datadog-entity-risk-scores-api
    name: Datadog Entity Risk Scores API
    tags:
      - Cloud Security
      - Risk Scores
      - Security
    humanURL: https://docs.datadoghq.com/api/latest/entity-risk-scores/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/entity-risk-scores/
        type: Documentation
    description: The Entity Risk Scores API provides security risk assessments for entities like cloud resources, identities, or services based on detected signals, misconfigurations, and identity risks.
  - aid: datadog:datadog-api-management-api
    name: Datadog API Management API
    tags:
      - API Catalog
      - API Management
    humanURL: https://docs.datadoghq.com/api/latest/api-management/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/api-management/
        type: Documentation
      - url: https://docs.datadoghq.com/api_catalog/
        type: Reference
    description: The API Management API allows you to create and manage APIs from OpenAPI specifications. It supports the Datadog API Catalog for tracking API performance, security, and ownership.
  - aid: datadog:datadog-cloud-workload-security-api
    name: Datadog Cloud Workload Security API
    tags:
      - Cloud Workload Security
      - Runtime Protection
      - Security
    humanURL: https://docs.datadoghq.com/api/latest/cloud-workload-security/
    baseURL: https://api.datadoghq.com
    image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
    properties:
      - url: https://docs.datadoghq.com/api/latest/cloud-workload-security/
        type: Documentation
      - url: https://docs.datadoghq.com/security/cloud_security_management/
        type: Reference
    description: The Cloud Workload Security API provides endpoints for managing workload protection rules and agent configurations. It monitors file, network, and process activity to detect real-time threats.
name: Datadog
tags:
  - Analytics
  - Dashboards
  - Monitoring
  - Platform
  - T1
  - Visualizations
image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
common:
  - type: Website
    url: https://www.datadoghq.com/
  - type: Portal
    url: https://docs.datadoghq.com/api/
  - type: Documentation
    url: https://docs.datadoghq.com/
  - type: Authentication
    url: https://docs.datadoghq.com/api/latest/authentication/
  - type: GitHubOrganization
    url: https://github.com/DataDog
  - type: Blog
    url: https://www.datadoghq.com/blog/
  - type: Support
    url: https://www.datadoghq.com/support/
  - type: StatusPage
    url: https://status.datadoghq.com/
  - type: Pricing
    url: https://www.datadoghq.com/pricing/
  - type: Login
    url: https://app.datadoghq.com/
  - type: SignUp
    url: https://www.datadoghq.com/free-datadog-trial/
  - url: json-ld/datadog-context.jsonld
    name: Datadog JSON-LD Context
    type: JSON-LD
    description: JSON-LD context file mapping Datadog entities (Metric, Monitor, LogEvent, Event, Dashboard, Incident) to schema.org, dcterms, and xsd vocabularies
  - url: json-schema/datadog-metric-schema.json
    name: Datadog Metric Schema
    type: JSONSchema
    description: JSON Schema for the Datadog metric series model including data points, tags, host, and resource information
  - url: json-schema/datadog-monitor-schema.json
    name: Datadog Monitor Schema
    type: JSONSchema
    description: JSON Schema for the Datadog monitor model including query, thresholds, notification options, state, and creator
  - url: json-schema/datadog-log-event-schema.json
    name: Datadog Log Event Schema
    type: JSONSchema
    description: JSON Schema for the Datadog log event model including content, attributes, HTTP context, user context, and error attributes
  - url: json-schema/datadog-event-schema.json
    name: Datadog Event Schema
    type: JSONSchema
    description: JSON Schema for the Datadog event model including title, text, timestamp, priority, host, tags, and alert type
  - url: https://www.datadoghq.com/product/
    name: Infrastructure & Application Monitoring as a Service | Datadog
    type: Products
    description: 'null'
  - url: https://www.datadoghq.com/customers/
    name: Customers | Datadog
    type: Customers
    description: 'null'
  - url: https://www.datadoghq.com/pricing/
    name: Pricing | Datadog
    type: Pricing
    description: 'null'
  - url: https://docs.datadoghq.com/integrations/
    name: Integrations
    type: Integrations
    description: 'null'
  - url: https://www.datadoghq.com/about/leadership/
    name: Leadership | Datadog
    type: About
    description: 'null'
  - url: https://www.datadoghq.com/blog/
    name: The Monitor | Datadog Official Blog
    type: Blog
    description: 'null'
  - url: https://app.datadoghq.com/account/login
    name: 'Datadog: Log In'
    type: Login
    description: 'null'
  - url: https://app.datadoghq.com/account/login
    name: 'Datadog: Log In'
    type: Login
    description: 'null'
  - url: https://app.datadoghq.com/account/login
    name: 'Datadog: Log In'
    type: Login
    description: 'null'
  - url: https://us5.datadoghq.com/signup
    name: Datadog
    type: SignUp
    description: 'null'
  - url: https://www.datadoghq.com/support/
    name: Support | Datadog
    type: Support
    description: 'null'
  - url: https://www.datadoghq.com/certification/overview/
    name: Certification | Datadog
    type: Certifications
    description: 'null'
  - url: https://www.datadoghq.com/privacy/
    name: Privacy at Datadog | Datadog
    type: PrivacyPolicy
    description: 'null'
  - url: https://www.datadoghq.com/security/
    name: Security | Datadog
    type: Security
    description: 'null'
  - url: https://trust.datadoghq.com/
    name: Datadog Trust Center | Powered by SafeBase
    type: Trust
    description: 'null'
  - url: https://www.datadoghq.com/partner/network/
    name: Datadog Partner Network Program | Datadog
    type: Partners
    description: 'null'
  - url: https://docs.datadoghq.com/
    name: Datadog Documentation
    type: Documentation
    description: 'null'
  - url: https://docs.datadoghq.com/api/latest/
    name: Datadog API Reference
    type: Portal
    description: 'null'
  - url: https://docs.datadoghq.com/getting_started/
    name: Getting Started with Datadog
    type: GettingStarted
    description: 'null'
  - url: https://docs.datadoghq.com/api/latest/authentication/
    name: Authentication | Datadog API Reference
    type: Authentication
    description: 'null'
  - url: https://status.datadoghq.com/
    name: Datadog Status
    type: StatusPage
    description: 'null'
  - url: https://github.com/DataDog
    name: Datadog GitHub Organization
    type: GitHub Organization
    description: 'null'
  - url: https://docs.datadoghq.com/api/latest/rate-limits/
    name: Rate Limits | Datadog API Reference
    type: RateLimits
    description: 'null'
  - url: https://docs.datadoghq.com/developers/
    name: Developers | Datadog
    type: Developer Portal
    description: 'null'
  - url: https://docs.datadoghq.com/developers/libraries/
    name: Libraries | Datadog
    type: SDKs
    description: 'null'
  - url: https://www.datadoghq.com/legal/terms/
    name: Terms of Service | Datadog
    type: TermsOfService
    description: 'null'
  - url: https://docs.datadoghq.com/agent/
    name: Datadog Agent Documentation
    type: Agent
    description: 'null'
  - url: https://community.datadoghq.com/
    name: Datadog Community
    type: Community
    description: 'null'
  - url: https://docs.datadoghq.com/api/latest/scopes/
    name: Authorization Scopes | Datadog API Reference
    type: Authorization Scopes
    description: 'null'
  - url: https://docs.datadoghq.com/api/latest/using-the-api/
    name: Using the API | Datadog API Reference
    type: Using the API
    description: 'null'
  - url: https://learn.datadoghq.com/
    name: Datadog Learning Center
    type: Learning Center
    description: 'null'
  - url: https://www.datadoghq.com/events-webinars/
    name: Events & Webinars | Datadog
    type: Events
    description: 'null'
  - url: https://www.datadoghq.com/marketplacepartners/
    name: Datadog Marketplace for Technology Partners
    type: Marketplace
    description: 'null'
  - url: https://www.postman.com/datadog/datadog-s-public-workspace/overview
    name: Datadog Public Workspace | Postman API Network
    type: PostmanWorkspace
    description: 'null'
  - url: https://docs.datadoghq.com/getting_started/api/
    name: Using Postman with Datadog APIs
    type: GettingStarted
    description: 'null'
  - url: https://www.datadoghq.com/learn/
    name: Datadog Learning Resources
    type: Learning Resources
    description: 'null'
  - type: Features
    data:
      - Infrastructure Monitoring with 1,000+ integrations and 15-month metric retention
      - APM (Application Performance Monitoring) with end-to-end distributed traces
      - APM Pro with Data Streams Monitoring for queue/pipeline observability
      - APM Enterprise with Continuous Profiler
      - Log Management with $0.10/GB ingest and tiered indexing/Flex storage
      - Real User Monitoring (RUM) for browser and mobile
      - Synthetic Monitoring with API and browser tests
      - Network Performance Monitoring
      - Database Monitoring
      - Cloud Security Posture Management (CSPM)
      - Cloud Workload Security
      - Cloud SIEM
      - Sensitive Data Scanner
      - Watchdog ML-based anomaly detection (Enterprise)
      - Governance Console for org-wide policy
      - Per-endpoint REST API rate limits with X-RateLimit-* headers
      - Cost Management and Usage Metering for FinOps
    sources:
      - https://www.datadoghq.com/pricing/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Full-Stack Observability
        description: Correlate metrics, traces, and logs across the entire application stack.
      - name: Container Monitoring
        description: Monitor Kubernetes, Docker, and container orchestration platforms.
      - name: Cloud Infrastructure Monitoring
        description: Monitor AWS, Azure, GCP, and hybrid cloud environments.
      - name: Application Performance Management
        description: Identify and resolve application bottlenecks with distributed tracing.
      - name: Log Analytics
        description: Centralize and analyze logs for troubleshooting and compliance.
      - name: Incident Management
        description: Automate incident detection, response, and resolution workflows.
      - name: DevOps Automation
        description: Integrate monitoring into CI/CD pipelines with API-driven workflows.
      - name: Security Posture Management
        description: Monitor cloud security misconfigurations and compliance violations.
  - type: Integrations
    data:
      - name: AWS
        description: Native integration with 80+ AWS services for metrics, logs, and traces.
      - name: Kubernetes
        description: Container orchestration monitoring with cluster, pod, and node visibility.
      - name: Terraform
        description: Infrastructure-as-code management of Datadog monitors, dashboards, and alerts.
      - name: Slack
        description: Alert notifications and incident management within Slack channels.
      - name: PagerDuty
        description: Incident escalation and on-call management integration.
      - name: Jira
        description: Create Jira tickets from Datadog alerts and incidents.
  - type: Solutions
    data:
      - name: Datadog Infrastructure
        description: Infrastructure monitoring with 800+ integrations for servers, containers, and cloud.
      - name: Datadog APM
        description: Application performance monitoring with distributed tracing and profiling.
      - name: Datadog Logs
        description: Log management with indexing, archiving, and analytics.
      - name: Datadog Security
        description: Cloud security posture management and threat detection.
created: 2024/04/14
modified: '2026-05-04'
description: Datadog is a monitoring and analytics platform that helps organizations gain insight into their infrastructure, applications, and services. It allows users to collect, visualize, and analyze real-time data from a variety of sources, including servers, databases, and cloud services. Datadog's platform enables companies to track performance metrics, troubleshoot issues, and optimize their systems for peak efficiency.
maintainers:
  - FN: Kin Lane
    url: http://apievangelist.com
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
