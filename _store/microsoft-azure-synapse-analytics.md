---
specificationVersion: '0.18'
name: Azure Synapse Analytics
description: Azure Synapse Analytics is an enterprise analytics service that accelerates time to insight across data warehouses and big data systems. It brings together the best of SQL technologies used in enterprise data warehousing, Spark technologies for big data, and Pipelines for data integration and ETL/ELT.
image: https://azure.microsoft.com/svghandler/synapse-analytics/
tags:
  - Analytics
  - Apache Spark
  - Big Data
  - Data Integration
  - Data Warehouse
  - ETL
  - SQL
created: '2024-01-01'
modified: '2026-04-28'
url: https://azure.microsoft.com/en-us/services/synapse-analytics/
apis:
  - name: Synapse Workspace API
    description: Manage Synapse workspaces including creation, configuration, and lifecycle management of analytics environments through Azure Resource Manager.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/
    baseURL: https://management.azure.com
    tags:
      - Management
      - Resource Manager
      - Workspace
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/workspace
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/resource-manager/Microsoft.Synapse/stable/2021-06-01/workspace.json
      - type: Swagger
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/resource-manager/Microsoft.Synapse/stable/2021-06-01/workspace.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-workspace-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-synapse-analytics-workspace-schema.json
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse SQL Pools API
    description: Manage dedicated SQL pools for enterprise data warehousing workloads including provisioning, scaling, pausing, and resuming compute resources.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/sqlpools
    baseURL: https://management.azure.com
    tags:
      - Data Warehouse
      - Resource Manager
      - SQL Pool
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/sqlpools
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/resource-manager/Microsoft.Synapse/stable/2021-06-01/sqlPool.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-sql-pools-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-synapse-analytics-sql-pool-schema.json
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Spark Pools API
    description: Manage Apache Spark pools for big data processing including pool creation, auto-scaling configuration, and Spark runtime version management.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/bigdatapool
    baseURL: https://management.azure.com
    tags:
      - Apache Spark
      - Big Data
      - Resource Manager
      - Spark
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/bigdatapool
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/resource-manager/Microsoft.Synapse/stable/2021-06-01/bigDataPool.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-spark-pools-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-synapse-analytics-spark-pool-schema.json
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Pipeline API
    description: Create and manage data integration pipelines for ETL/ELT workflows. Supports orchestrating data movement and transformation activities across diverse data stores.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/pipeline
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Data Integration
      - Data Plane
      - ETL
      - Pipeline
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/pipeline
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/artifacts.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-pipeline-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-synapse-analytics-pipeline-schema.json
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Spark Job API
    description: Submit and manage Apache Spark batch jobs and interactive sessions. Provides operations for monitoring job status, retrieving logs, and cancelling running applications.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/spark
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Batch Processing
      - Data Plane
      - Spark Jobs
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/spark
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2019-11-01-preview/sparkJob.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-spark-job-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-synapse-analytics-spark-batch-job-schema.json
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Monitoring API
    description: Monitor pipeline runs, Spark jobs, and SQL requests within a Synapse workspace. Provides visibility into execution status, performance metrics, and operational health.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/monitoring
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Data Plane
      - Monitoring
      - Observability
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/monitoring
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/monitoring.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-monitoring-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Link API
    description: Manage Azure Synapse Link for real-time analytics over operational data. Enables hybrid transactional and analytical processing without impacting operational workloads.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/azure/synapse-analytics/synapse-link/
    baseURL: https://management.azure.com
    tags:
      - HTAP
      - Real-Time Analytics
      - Synapse Link
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/synapse-analytics/synapse-link/
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-synapse-link-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Access Control API
    description: Manage role assignments, role definitions, and access control for Synapse workspace resources. Supports Synapse role-based access control for fine-grained permissions.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/role-assignments
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Access Control
      - Data Plane
      - RBAC
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/role-assignments
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/roleAssignments.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-access-control-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-synapse-analytics-role-assignment-schema.json
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Notebook API
    description: Create, update, list, and delete notebooks within a Synapse workspace. Notebooks support interactive data exploration using Python, Scala, SQL, and .NET languages.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/notebook
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Artifacts
      - Data Exploration
      - Data Plane
      - Notebook
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/notebook
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/artifacts.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-notebook-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-synapse-analytics-notebook-schema.json
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Dataset API
    description: Create and manage datasets that represent data structures within linked data stores. Datasets define the schema and location of data used in pipelines and data flows.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/dataset
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Artifacts
      - Data Management
      - Data Plane
      - Dataset
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/dataset
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/artifacts.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-dataset-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-synapse-analytics-dataset-schema.json
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Linked Service API
    description: Create and manage linked services that define connection information to external data sources. Linked services act as connection strings for integrating with databases, storage, and other services.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/linked-service
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Connectivity
      - Data Integration
      - Data Plane
      - Linked Service
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/linked-service
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/artifacts.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-linked-service-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-synapse-analytics-linked-service-schema.json
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Data Flow API
    description: Create and manage data flows for visual data transformation logic. Data flows enable code-free data transformation at scale within Synapse pipelines.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/data-flow
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Data Flow
      - Data Plane
      - Data Transformation
      - ETL
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/data-flow
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/artifacts.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-data-flow-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse SQL Script API
    description: Create, update, list, and delete SQL scripts within a Synapse workspace. SQL scripts can target both dedicated and serverless SQL pools for querying and data management.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/sql-script
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Artifacts
      - Data Plane
      - SQL
      - SQL Script
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/sql-script
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/artifacts.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-sql-script-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Trigger API
    description: Create and manage triggers that orchestrate pipeline execution. Supports schedule-based, tumbling window, and event-based triggers for automated workflow execution.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/trigger
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Automation
      - Data Plane
      - Scheduling
      - Trigger
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/trigger
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/artifacts.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-trigger-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-synapse-analytics-trigger-schema.json
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Spark Job Definition API
    description: Create and manage Spark job definitions as reusable templates for batch processing. Spark job definitions encapsulate configuration, code, and dependencies for repeatable execution.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/spark-job-definition
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Artifacts
      - Batch Processing
      - Data Plane
      - Spark Job Definition
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/spark-job-definition
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/artifacts.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-spark-job-definition-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Managed Private Endpoints API
    description: Create and manage managed private endpoints within a Synapse managed virtual network. Enables secure, private connectivity to Azure resources without exposing traffic to the public internet.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/managed-private-endpoints
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Data Plane
      - Networking
      - Private Endpoints
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/managed-private-endpoints
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/preview/2021-06-01-preview/managedPrivateEndpoints.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-managed-private-endpoints-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Integration Runtimes API
    description: Manage integration runtimes that provide the compute infrastructure for data integration activities. Supports Azure-hosted, self-hosted, and Azure-SSIS integration runtime types.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/integration-runtimes
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Compute
      - Data Integration
      - Data Plane
      - Integration Runtime
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/integration-runtimes
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/artifacts.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-integration-runtimes-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Library API
    description: Manage workspace libraries including JAR files, Python wheels, and other packages used by Spark pools. Supports uploading, listing, and deleting library resources.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/library
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Data Plane
      - Library
      - Package Management
      - Spark
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/library
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/artifacts.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-library-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Git Integration API
    description: Manage Git repository integration for Synapse workspaces. Enables source control for workspace artifacts including pipelines, notebooks, and data flows through Git-based version control.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/git-integration
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Data Plane
      - DevOps
      - Git Integration
      - Source Control
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/git-integration
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/gitintegration.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-git-integration-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Firewall Rules API
    description: Manage IP firewall rules for Synapse workspaces to control network access. Supports creating, updating, and deleting server-level IP firewall rules for workspace security.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/ip-firewall-rules
    baseURL: https://management.azure.com
    tags:
      - Firewall Rules
      - Network Security
      - Resource Manager
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/ip-firewall-rules
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/resource-manager/Microsoft.Synapse/stable/2021-06-01/firewallRule.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-firewall-rules-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-synapse-analytics-firewall-rule-schema.json
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Keys API
    description: Manage workspace encryption keys for data protection at rest. Supports customer-managed key configuration for dedicated SQL pools and workspace-level encryption.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/keys
    baseURL: https://management.azure.com
    tags:
      - Encryption Keys
      - Resource Manager
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/keys
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/resource-manager/Microsoft.Synapse/stable/2021-06-01/keys.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-keys-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Private Endpoint Connections API
    description: Manage private endpoint connections to Synapse workspaces. Enables approval and management of private link connections for secure access from virtual networks.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/private-endpoint-connections
    baseURL: https://management.azure.com
    tags:
      - Networking
      - Private Endpoint
      - Resource Manager
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/private-endpoint-connections
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/resource-manager/Microsoft.Synapse/stable/2021-06-01/privateEndpointConnections.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-private-endpoint-connections-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Private Link Hubs API
    description: Manage private link hubs that enable connecting to Synapse Studio through Azure Private Link. Provides centralized private connectivity for workspace management operations.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/private-link-hubs
    baseURL: https://management.azure.com
    tags:
      - Networking
      - Private Link Hub
      - Resource Manager
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/private-link-hubs
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/resource-manager/Microsoft.Synapse/stable/2021-06-01/privatelinkhub.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-private-link-hubs-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Kusto Pools API
    description: Manage Data Explorer (Kusto) pools within a Synapse workspace for real-time log and telemetry analytics. Supports creating pools, databases, and managing data connections.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/kusto-pools
    baseURL: https://management.azure.com
    tags:
      - Data Explorer
      - Kusto Pool
      - Real-Time Analytics
      - Resource Manager
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/kusto-pools
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/resource-manager/Microsoft.Synapse/preview/2021-06-01-preview/kustoPool.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-kusto-pools-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Azure AD Only Authentication API
    description: Manage Azure Active Directory only authentication settings for Synapse workspaces. Enables enforcing Azure AD authentication and disabling SQL authentication for enhanced security.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/azure-ad-only-authentications
    baseURL: https://management.azure.com
    tags:
      - Authentication
      - Azure Active Directory
      - Resource Manager
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/azure-ad-only-authentications
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/resource-manager/Microsoft.Synapse/stable/2021-06-01/azureADOnlyAuthentication.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-azure-ad-only-auth-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Spark Configuration API
    description: Create and manage reusable Spark configuration artifacts for Synapse Spark pools. Supports defining Spark properties, environment variables, and package requirements as shareable configurations.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/spark-configuration
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Configuration
      - Data Plane
      - Spark
      - Spark Configuration
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/spark-configuration
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/preview/2021-06-01-preview/sparkConfigurations.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-spark-configuration-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Data Flow Debug Session API
    description: Manage data flow debug sessions for interactive testing and debugging of data flow transformations. Enables previewing data and validating transformation logic before deployment.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/data-flow-debug-session
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Data Flow Debug
      - Data Plane
      - Data Transformation
      - Debugging
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/data-flow-debug-session
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/artifacts.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-data-flow-debug-session-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Credential API
    description: Manage credential artifacts used for authenticating with external data sources in Synapse workspaces. Supports creating and managing credentials referenced by linked services and datasets.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/credential
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Authentication
      - Credential
      - Data Plane
      - Security
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/credential
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/stable/2020-12-01/artifacts.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-credential-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse KQL Script API
    description: Create and manage KQL (Kusto Query Language) scripts for querying Data Explorer pools. Supports authoring and storing KQL queries as workspace artifacts.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/kql-script
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Data Explorer
      - Data Plane
      - KQL Script
      - Kusto
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/kql-script
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/preview/2021-11-01-preview/kqlScripts.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-kql-script-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
  - name: Synapse Link Connection API
    description: Manage Synapse Link connections for continuous data replication from operational databases. Supports configuring and monitoring real-time data synchronization from sources like Azure Cosmos DB and Azure SQL.
    image: https://azure.microsoft.com/svghandler/synapse-analytics/
    humanURL: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/link-connection
    baseURL: https://{workspaceName}.dev.azuresynapse.net
    tags:
      - Data Plane
      - Data Replication
      - Link Connection
      - Real-Time Analytics
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/link-connection
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/synapse/data-plane/Microsoft.Synapse/preview/2023-04-18-preview/linkConnections.json
      - type: OpenAPI
        url: openapi/azure-synapse-analytics-link-connection-openapi.yml
      - type: JSONLD
        url: json-ld/azure-synapse-analytics-context.jsonld
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/synapse-analytics/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/synapse-analytics/get-started
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/synapse-analytics/security/synapse-workspace-security-overview
  - type: Change Log
    url: https://learn.microsoft.com/en-us/azure/synapse-analytics/whats-new
  - type: Blog
    url: https://techcommunity.microsoft.com/category/azuredatabases/blog/azuresynapseanalyticsblog
  - type: Status
    url: https://status.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/synapse-analytics/
  - type: Best Practices
    url: https://learn.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-best-practices
  - type: Security
    url: https://learn.microsoft.com/en-us/azure/synapse-analytics/security/synapse-workspace-security-overview
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: SDKs
    url: https://learn.microsoft.com/en-us/azure/synapse-analytics/
  - type: SDK - Python
    url: https://pypi.org/project/azure-synapse-artifacts/
  - type: SDK - .NET
    url: https://www.nuget.org/packages/Azure.ResourceManager.Synapse/
  - type: SDK - Java
    url: https://learn.microsoft.com/en-us/java/api/overview/azure/analytics-synapse-artifacts-readme
  - type: SDK - JavaScript
    url: https://www.npmjs.com/package/@azure/synapse-artifacts
  - type: Community
    url: https://techcommunity.microsoft.com/category/azuredatabases/blog/azuresynapseanalyticsblog
  - type: Website
    url: https://azure.microsoft.com/en-us/products/synapse-analytics
  - type: Login
    url: https://portal.azure.com/
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com/
---
