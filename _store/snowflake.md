---
aid: snowflake
name: Snowflake
description: Snowflake is a cloud-based data platform that provides data warehousing, data lakes, data engineering, data science, and data application development capabilities.
image: https://www.snowflake.com/wp-content/themes/snowflake/assets/img/brand-guidelines/logo-sno-blue-example.svg
url: https://raw.githubusercontent.com/api-evangelist/snowflake/refs/heads/main/apis.yml
created: '2025-06-05'
modified: '2026-05-04'
specificationVersion: '0.19'
type: Contract
access: 3rd-Party
position: Consuming
apis:
  - aid: snowflake:snowflake-account-api
    name: Snowflake Account API
    description: The Snowflake Account API is a REST API that you can use to access, update, and perform certain actions on Account resource in Snowflake.
    tags:
      - Accounts
      - Administration
    properties:
      - type: OpenAPI
        url: openapi/account.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/account
      - type: JSONLD
        url: json-ld/account-context.jsonld
  - aid: snowflake:snowflake-alert-api
    name: Snowflake Alert API
    description: The Snowflake Alert API is a REST API that you can use to access, update, and perform certain actions on Alert resource in a Snowflake database.
    tags:
      - Alerts
      - Monitoring
    properties:
      - type: OpenAPI
        url: openapi/alert.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/alert
      - type: JSONLD
        url: json-ld/alert-context.jsonld
  - aid: snowflake:snowflake-api-integration-api
    name: Snowflake API Integration API
    description: The Snowflake API Integration API is a REST API that you can use to access, update, and perform certain actions on API Integration resource in a Snowflake database.
    tags:
      - API Integrations
      - Integrations
    properties:
      - type: OpenAPI
        url: openapi/api-integration.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/api-integration
      - type: JSONLD
        url: json-ld/api-integration-context.jsonld
  - aid: snowflake:snowflake-artifact-repository-api
    name: Snowflake Artifact Repository API
    description: The Snowflake Artifact Repository API is a REST API that you can use to access, update, and perform certain actions on Artifact Repository resources in a Snowflake database.
    tags:
      - Artifacts
      - Repositories
    properties:
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/artifact-repository
  - aid: snowflake:snowflake-catalog-integration-api
    name: Snowflake Catalog Integration API
    description: The Snowflake Catalog Integration API is a REST API that you can use to access, update, and perform certain actions on Catalog Integration resource in a Snowflake database.
    tags:
      - Catalog
      - Integrations
    properties:
      - type: OpenAPI
        url: openapi/catalog-integration.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/catalog-integration
      - type: JSONLD
        url: json-ld/catalog-integration-context.jsonld
  - aid: snowflake:snowflake-compute-pools-api
    name: Snowflake Compute Pools API
    description: The Snowflake Compute Pools API is a REST API that you can use to access, update, and perform common actions on Compute Pool resources.
    tags:
      - Compute
      - Infrastructure
    properties:
      - type: OpenAPI
        url: openapi/compute-pool.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/compute-pool
      - type: JSONLD
        url: json-ld/compute-pool-context.jsonld
  - aid: snowflake:cortex-analyst-api
    name: Cortex Analyst API
    description: The Snowflake Cortex Analyst API is a REST API that allows end user to chat with their data leveraging semantic models to generate SQL queries.
    tags:
      - AI
      - Analytics
      - Cortex
      - Natural Language
    properties:
      - type: OpenAPI
        url: openapi/cortex-analyst.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/rest-api
      - type: JSONLD
        url: json-ld/cortex-analyst-context.jsonld
  - aid: snowflake:cortex-embed-api
    name: Cortex Embed API
    description: The Snowflake Cortex Embed API is a REST API that performs LLM embedding for input text, similar to the Snowflake Cortex EMBED_TEXT functions.
    tags:
      - AI
      - Cortex
      - Embeddings
    properties:
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/cortex-embed
  - aid: snowflake:cortex-inference-api
    name: Cortex Inference API
    description: OpenAPI 3.0 specification for the Cortex REST API.
    tags:
      - AI
      - Cortex
      - Inference
      - LLM
    properties:
      - type: OpenAPI
        url: openapi/cortex-inference.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/cortex-inference
      - type: JSONLD
        url: json-ld/cortex-inference-context.jsonld
  - aid: snowflake:cortex-search-rest-api
    name: Cortex Search REST API
    description: OpenAPI 3.0 specification for the Cortex Search REST API.
    tags:
      - AI
      - Cortex
      - Search
    properties:
      - type: OpenAPI
        url: openapi/cortex-search-service.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/cortex-search-service
      - type: JSONLD
        url: json-ld/cortex-search-service-context.jsonld
  - aid: snowflake:snowflake-database-role-api
    name: Snowflake Database Role API
    description: The Snowflake Database Role API is a REST API that you can use to access, update, and perform certain actions on Database Role resource in a Snowflake database.
    tags:
      - Access Control
      - Database Roles
      - Security
    properties:
      - type: OpenAPI
        url: openapi/database-role.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/database-role
      - type: JSONLD
        url: json-ld/database-role-context.jsonld
  - aid: snowflake:snowflake-database-api
    name: Snowflake Database API
    description: The Snowflake Database API is a REST API that you can use to access, update, and perform certain actions on Database resource in Snowflake.
    tags:
      - Databases
      - Data Management
    properties:
      - type: OpenAPI
        url: openapi/database.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/database
      - type: JSONSchema
        url: json-schema/snowflake-database-schema.json
      - type: JSONLD
        url: json-ld/database-context.jsonld
  - aid: snowflake:snowflake-dynamic-table-api
    name: Snowflake Dynamic Table API
    description: The Snowflake Dynamic Table API is a REST API that you can use to access, update, and perform certain actions on Dynamic Tables resource in a Snowflake database.
    tags:
      - Data Pipelines
      - Dynamic Tables
      - Tables
    properties:
      - type: OpenAPI
        url: openapi/dynamic-table.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/dynamic-table
      - type: JSONLD
        url: json-ld/dynamic-table-context.jsonld
  - aid: snowflake:snowflake-event-table-api
    name: Snowflake Event Table API
    description: The Snowflake Event Table API is a REST API that you can use to access, update, and perform certain actions on Event Table resource in a Snowflake database.
    tags:
      - Events
      - Logging
      - Tables
    properties:
      - type: OpenAPI
        url: openapi/event-table.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/event-table
      - type: JSONLD
        url: json-ld/event-table-context.jsonld
  - aid: snowflake:snowflake-external-volume-api
    name: Snowflake External Volume API
    description: The Snowflake External Volume API is a REST API that you can use to access, update, and perform certain actions on External Volume resource in a Snowflake database.
    tags:
      - External Volumes
      - Storage
    properties:
      - type: OpenAPI
        url: openapi/external-volume.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/external-volume
      - type: JSONLD
        url: json-ld/external-volume-context.jsonld
  - aid: snowflake:snowflake-function-api
    name: Snowflake Function API
    description: The Snowflake Function API is a REST API that allows caller to create, execute and drop functions in a Snowflake database.
    tags:
      - Functions
      - Programmability
    properties:
      - type: OpenAPI
        url: openapi/function.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/function
      - type: JSONLD
        url: json-ld/function-context.jsonld
  - aid: snowflake:snowflake-grant-api
    name: Snowflake Grant API
    description: The Snowflake Grant API is a REST API that you can use to show or manage privileges that have been provided to users and roles in a Snowflake database.
    tags:
      - Access Control
      - Grants
      - Security
    properties:
      - type: OpenAPI
        url: openapi/grant.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/grant
      - type: JSONLD
        url: json-ld/grant-context.jsonld
  - aid: snowflake:snowflake-iceberg-table-api
    name: Snowflake Iceberg Table API
    description: The Snowflake Iceberg Table API is a REST API that you can use to access, update, and perform certain actions on Iceberg Table resource in a Snowflake database.
    tags:
      - Data Lakes
      - Iceberg
      - Tables
    properties:
      - type: OpenAPI
        url: openapi/iceberg-table.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/iceberg-table
      - type: JSONLD
        url: json-ld/iceberg-table-context.jsonld
  - aid: snowflake:snowflake-image-repository-api
    name: Snowflake Image Repository API
    description: The Snowflake Image Repository API is a REST API that you can use to access, update, and perform common actions on Image Repository resource in Snowflake.
    tags:
      - Containers
      - Image Repository
    properties:
      - type: OpenAPI
        url: openapi/image-repository.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/image-repository
      - type: JSONLD
        url: json-ld/image-repository-context.jsonld
  - aid: snowflake:snowflake-managed-account-api
    name: Snowflake Managed Account API
    description: The Snowflake Managed Account API is a REST API that you can use to access, update, and perform certain actions on Managed Account resource in Snowflake.
    tags:
      - Accounts
      - Administration
    properties:
      - type: OpenAPI
        url: openapi/managed-account.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/managed-account
      - type: JSONLD
        url: json-ld/managed-account-context.jsonld
  - aid: snowflake:snowflake-network-policy-api
    name: Snowflake Network Policy API
    description: The Snowflake Network Policy API is a REST API that you can use to access, update, and perform certain actions on Network Policy resource in a Snowflake database.
    tags:
      - Network
      - Security
    properties:
      - type: OpenAPI
        url: openapi/network-policy.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/network-policy
      - type: JSONLD
        url: json-ld/network-policy-context.jsonld
  - aid: snowflake:snowflake-notebook-api
    name: Snowflake Notebook API
    description: The Snowflake Notebook API is a REST API that you can use to access, update, and perform certain actions on Notebook resource in a Snowflake database.
    tags:
      - Data Science
      - Notebooks
    properties:
      - type: OpenAPI
        url: openapi/notebook.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/notebook
      - type: JSONLD
        url: json-ld/notebook-context.jsonld
  - aid: snowflake:snowflake-notification-integration-api
    name: Snowflake Notification Integration API
    description: The Snowflake Notification Integration API is a REST API that you can use to access, update, and perform certain actions on Notification Integration resource in a Snowflake database.
    tags:
      - Integrations
      - Notifications
    properties:
      - type: OpenAPI
        url: openapi/notification-integration.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/notification-integration
      - type: JSONLD
        url: json-ld/notification-integration-context.jsonld
  - aid: snowflake:snowflake-pipe-api
    name: Snowflake Pipe API
    description: The Snowflake Pipe API is a REST API that you can use to access, update, and perform certain actions on Pipe resource in a Snowflake database.
    tags:
      - Data Ingestion
      - Pipes
    properties:
      - type: OpenAPI
        url: openapi/pipe.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/pipe
      - type: JSONLD
        url: json-ld/pipe-context.jsonld
  - aid: snowflake:snowflake-procedure-api
    name: Snowflake Procedure API
    description: The Snowflake Procedure API is a REST API that you can use to access, update, and perform certain actions on Procedure resource in a Snowflake database.
    tags:
      - Procedures
      - Programmability
    properties:
      - type: OpenAPI
        url: openapi/procedure.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/procedure
      - type: JSONLD
        url: json-ld/procedure-context.jsonld
  - aid: snowflake:snowflake-result-api
    name: Snowflake Result API
    description: The Snowflake Result API is a REST API that you can use to check request status and fetch request response.
    tags:
      - Query Results
      - SQL
    properties:
      - type: OpenAPI
        url: openapi/result.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/result
  - aid: snowflake:snowflake-role-api
    name: Snowflake Role API
    description: The Snowflake Role API is a REST API that you can use to access, update, and perform certain actions on Role resource in a Snowflake database.
    tags:
      - Access Control
      - Roles
      - Security
    properties:
      - type: OpenAPI
        url: openapi/role.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/role
      - type: JSONLD
        url: json-ld/role-context.jsonld
  - aid: snowflake:snowflake-schema-api
    name: Snowflake Schema API
    description: The Snowflake Schema API is a REST API that you can use to access, update, and perform certain actions on a Snowflake schema.
    tags:
      - Data Management
      - Schemas
    properties:
      - type: OpenAPI
        url: openapi/schema.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/schema
      - type: JSONLD
        url: json-ld/schema-context.jsonld
  - aid: snowflake:snowflake-services-api
    name: Snowflake Services API
    description: The Snowflake Services API is a REST API that you can use to access, update, and perform certain actions on Services resource in a Snowflake database.
    tags:
      - Containers
      - Services
    properties:
      - type: OpenAPI
        url: openapi/service.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/service
      - type: JSONLD
        url: json-ld/service-context.jsonld
  - aid: snowflake:snowflake-sql-api
    name: Snowflake SQL API
    description: The Snowflake SQL API is a REST API that you can use to access and update data in a Snowflake database.
    tags:
      - Query
      - SQL
    properties:
      - type: OpenAPI
        url: openapi/sqlapi.yaml
      - type: OpenAPI
        url: openapi/snowflake-sql-rest-api.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/sql-api/index
      - type: JSONLD
        url: json-ld/sqlapi-context.jsonld
      - type: JSONLD
        url: json-ld/snowflake-sql-rest-context.jsonld
  - aid: snowflake:snowflake-stage-api
    name: Snowflake Stage API
    description: The Snowflake Stage API is a REST API that you can use to access, update, and perform certain actions on stage resources in a Snowflake database.
    tags:
      - Data Loading
      - Stages
      - Storage
    properties:
      - type: OpenAPI
        url: openapi/stage.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/stage
      - type: JSONLD
        url: json-ld/stage-context.jsonld
  - aid: snowflake:snowflake-stream-api
    name: Snowflake Stream API
    description: The Snowflake Stream API is a REST API that you can use to access, update, and perform certain actions on Stream resource in a Snowflake database.
    tags:
      - Change Data Capture
      - Streams
    properties:
      - type: OpenAPI
        url: openapi/stream.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/stream
      - type: JSONLD
        url: json-ld/stream-context.jsonld
  - aid: snowflake:snowflake-table-api
    name: Snowflake Table API
    description: The Snowflake Table API is a REST API that you can use to access, update, and perform certain actions on Tables resource in a Snowflake database.
    tags:
      - Data Management
      - Tables
    properties:
      - type: OpenAPI
        url: openapi/table.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/table
      - type: JSONLD
        url: json-ld/table-context.jsonld
  - aid: snowflake:snowflake-task-api
    name: Snowflake Task API
    description: The Snowflake Task API is a REST API that you can use to access, update, and perform certain actions on task resources in a Snowflake database.
    tags:
      - Scheduling
      - Tasks
    properties:
      - type: OpenAPI
        url: openapi/task.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/task
      - type: JSONLD
        url: json-ld/task-context.jsonld
  - aid: snowflake:snowflake-user-defined-function-api
    name: Snowflake User Defined Function API
    description: The Snowflake User Defined Function API is a REST API that you can use to access, update, and perform certain actions on User Defined Function resource in a Snowflake database.
    tags:
      - Functions
      - Programmability
      - UDF
    properties:
      - type: OpenAPI
        url: openapi/user-defined-function.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/user-defined-function
      - type: JSONLD
        url: json-ld/user-defined-function-context.jsonld
  - aid: snowflake:snowflake-user-api
    name: Snowflake User API
    description: The Snowflake User API is a REST API that you can use to access, update, and perform certain action on Users in a Snowflake database.
    tags:
      - Security
      - Users
    properties:
      - type: OpenAPI
        url: openapi/user.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/user
      - type: JSONLD
        url: json-ld/user-context.jsonld
  - aid: snowflake:snowflake-view-api
    name: Snowflake View API
    description: The Snowflake View API is a REST API that you can use to access, update, and perform certain actions on View resource in a Snowflake database.
    tags:
      - Data Management
      - Views
    properties:
      - type: OpenAPI
        url: openapi/view.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/view
      - type: JSONLD
        url: json-ld/view-context.jsonld
  - aid: snowflake:snowflake-warehouse-api
    name: Snowflake Warehouse API
    description: The Snowflake Warehouse API is a REST API that you can use to access, customize and manage virtual warehouse in a Snowflake account.
    tags:
      - Compute
      - Warehouses
    properties:
      - type: OpenAPI
        url: openapi/warehouse.yaml
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/warehouse
      - type: JSONSchema
        url: json-schema/snowflake-warehouse-schema.json
      - type: JSONLD
        url: json-ld/warehouse-context.jsonld
  - aid: snowflake:snowflake-network-rule-api
    name: Snowflake Network Rule API
    description: The Snowflake Network Rule API is a REST API that you can use to access, update, and perform certain actions on Network Rule resources in a Snowflake database.
    tags:
      - Network
      - Security
    properties:
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/network-rule
  - aid: snowflake:snowflake-password-policy-api
    name: Snowflake Password Policy API
    description: The Snowflake Password Policy API is a REST API that you can use to access, update, and perform certain actions on Password Policy resources in a Snowflake database.
    tags:
      - Password Policy
      - Security
    properties:
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/password-policy
  - aid: snowflake:snowflake-secret-api
    name: Snowflake Secret API
    description: The Snowflake Secret API is a REST API that you can use to access, update, and perform certain actions on Secret resources in a Snowflake database.
    tags:
      - Secrets
      - Security
    properties:
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/secret
  - aid: snowflake:snowflake-sequence-api
    name: Snowflake Sequence API
    description: The Snowflake Sequence API is a REST API that you can use to access, update, and perform certain actions on Sequence resources in a Snowflake database.
    tags:
      - Data Management
      - Sequences
    properties:
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/sequence
  - aid: snowflake:snowflake-spark-connect-api
    name: Snowflake Spark Connect API
    description: The Snowflake Spark Connect API is a REST API that enables execution of Spark workloads on Snowflake infrastructure through REST endpoints.
    tags:
      - Data Engineering
      - Spark
    properties:
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/spark-connect
  - aid: snowflake:snowflake-streamlit-api
    name: Snowflake Streamlit API
    description: The Snowflake Streamlit API is a REST API that you can use to access, update, and perform certain actions on Streamlit application resources in a Snowflake database.
    tags:
      - Applications
      - Streamlit
    properties:
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/streamlit
  - aid: snowflake:snowflake-tag-api
    name: Snowflake Tag API
    description: The Snowflake Tag API is a REST API that you can use to access, update, and perform certain actions on Tag resources in a Snowflake database.
    tags:
      - Data Governance
      - Tags
    properties:
      - type: Documentation
        url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/tag
  - aid: snowflake:cortex-agents-api
    name: Cortex Agents API
    description: The Snowflake Cortex Agents API is a REST API that you can use to create, manage, and interact with Cortex Agent objects in a Snowflake account.
    tags:
      - Agents
      - AI
      - Cortex
    properties:
      - type: Documentation
        url: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-rest-api
  - aid: snowflake:snowpipe-rest-api
    name: Snowpipe REST API
    description: The Snowpipe REST API provides REST endpoints for defining the list of files to ingest and fetching reports of the load history for continuous data loading into Snowflake.
    tags:
      - Data Ingestion
      - Snowpipe
    properties:
      - type: Documentation
        url: https://docs.snowflake.com/en/user-guide/data-load-snowpipe-rest-apis
common:
  - type: StatusPage
    url: https://status.snowflake.com/
  - type: ChangeLog
    url: https://docs.snowflake.com/en/release-notes/overview
  - type: GettingStarted
    url: https://docs.snowflake.com/en/user-guide-getting-started
  - type: Tutorials
    url: https://docs.snowflake.com/en/tutorials
  - type: TermsOfService
    url: https://www.snowflake.com/en/legal/snowflake-site-terms/
  - type: Documentation
    url: https://docs.snowflake.com/
  - type: PrivacyPolicy
    url: https://www.snowflake.com/en/legal/privacy/privacy-policy/
  - type: Blog
    url: https://www.snowflake.com/en/engineering-blog/
  - type: Support
    url: https://www.snowflake.com/en/support/
  - type: Plans
    url: https://www.snowflake.com/en/pricing-options/
  - type: Portal
    url: https://www.snowflake.com/en/developers/
  - type: Events
    url: https://www.snowflake.com/about/events/
  - type: SignUp
    url: https://signup.snowflake.com/
  - type: GitHubOrganization
    url: https://github.com/snowflakedb
  - type: Quickstart
    url: https://quickstarts.snowflake.com/
  - type: Documentation
    url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/snowflake-rest-api
    title: REST APIs Overview
  - type: GettingStarted
    url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/getting-started
    title: REST API Getting Started
  - type: Documentation
    url: https://docs.snowflake.com/en/developer-guide/snowpark/index
    title: Snowpark API
  - type: SDK
    url: https://docs.snowflake.com/en/developer-guide/python-connector/python-connector
    title: Python Connector
  - type: OpenAPI
    url: https://github.com/snowflakedb/snowflake-rest-api-specs
  - type: Authentication
    url: https://docs.snowflake.com/en/user-guide/admin-security.html
  - type: JSONSchema
    url: json-schema/snowflake-warehouse-schema.json
    title: Snowflake Warehouse JSON Schema
  - type: JSONSchema
    url: json-schema/snowflake-database-schema.json
    title: Snowflake Database JSON Schema
  - type: JSONLD
    url: json-ld/snowflake-context.jsonld
    title: Snowflake JSON-LD Context
  - type: OpenAPI
    url: openapi/snowflake-sql-rest-api.yaml
    title: Snowflake SQL REST API OpenAPI 3.1.0
  - type: NaftikoCapability
    url: capabilities/data-management.yaml
    title: Data Management
  - type: NaftikoCapability
    url: capabilities/data-engineering.yaml
    title: Data Engineering
  - type: NaftikoCapability
    url: capabilities/cortex-ai.yaml
    title: Cortex AI
  - type: NaftikoCapability
    url: capabilities/security-and-access.yaml
    title: Security and Access
  - type: NaftikoCapability
    url: capabilities/compute-and-services.yaml
    title: Compute and Services
  - type: NaftikoCapability
    url: capabilities/integrations-and-connectors.yaml
    title: Integrations and Connectors
  - type: Features
    data:
      - 'Standard: $2.00/credit (US on-demand baseline)'
      - 'Enterprise: $3.00/credit (1.5x) with multi-cluster, Time Travel 90d'
      - 'Business Critical: $4.00/credit (2x) with CMK, PrivateLink, HIPAA'
      - 'VPS: dedicated metadata for highest isolation'
      - 'Storage: $23/TB-month on-demand'
      - 'Multi-cloud: AWS, GCP, Azure (regions priced 20-50% higher outside US)'
      - Warehouse sizes XS-6XL (1-512 credits/hour)
      - SQL API for REST-based queries
      - Snowpipe streaming for low-latency ingest (per-channel limits)
      - Default 60 concurrent queries per user, 8 per warehouse
      - Snowpark for Python/Scala/Java in-DB execution
      - Cortex AI/ML built-in functions
      - Native Apps framework
      - Data Marketplace for data sharing
      - Streamlit hosted apps
      - Time Travel and Fail-safe
    sources:
      - https://www.snowflake.com/en/pricing-options/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Data Engineering
        description: Build and orchestrate data pipelines using tasks, streams, pipes, and dynamic tables for ETL/ELT workflows.
      - name: Data Science and ML
        description: Develop and deploy machine learning models using Snowpark, notebooks, and Cortex AI capabilities.
      - name: Data Analytics
        description: Run complex analytical queries across massive datasets with automatic scaling and concurrency.
      - name: AI-Powered Analytics
        description: Use Cortex Analyst to ask questions about data in natural language and receive SQL-backed answers.
      - name: Data Application Development
        description: Build data-intensive applications using Snowflake APIs, Snowpark, and Streamlit.
      - name: Data Governance
        description: Manage access control, data classification, and compliance using roles, grants, tags, and network policies.
  - type: Integrations
    data:
      - name: Apache Spark
        description: Execute Spark workloads on Snowflake infrastructure through the Spark Connect API.
      - name: Apache Iceberg
        description: Create and manage Iceberg tables with support for AWS Glue, Delta, and REST catalog integrations.
      - name: Cloud Storage
        description: Connect to external cloud storage on AWS S3, Azure Blob, and Google Cloud Storage via external volumes and stages.
      - name: Notification Services
        description: Integrate with AWS SNS, Azure Event Grid, and GCP Pub/Sub for event-driven data pipelines.
      - name: Git Repositories
        description: Connect to Git repositories for version-controlled code and configuration management.
tags:
  - Data Lakes
  - Data Sharing
  - Data Warehousing
  - Database
  - SQL
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
  - name: Snowflake Inc.
    email: support@snowflake.com
    url: https://www.snowflake.com
---
