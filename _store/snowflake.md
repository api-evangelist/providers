---
aid: snowflake
url: https://raw.githubusercontent.com/api-evangelist/snowflake/refs/heads/main/apis.yml
apis:
- aid: snowflake:snowflake-account-api
  name: Snowflake Account API
  tags: []
  properties:
  - url: openapi/account.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/account
    type: Documentation
  description: The Snowflake Account API is a REST API that you can use to access, update, and perform certain actions on Account resource in Snowflake.
- aid: snowflake:snowflake-alert-api
  name: Snowflake Alert API
  tags: []
  properties:
  - url: openapi/alert.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/alert
    type: Documentation
  description: The Snowflake Alert API is a REST API that you can use to access, update, and perform certain actions on Alert resource in a Snowflake database.
- aid: snowflake:snowflake-api-integration-api
  name: Snowflake API Integration API
  tags: []
  properties:
  - url: openapi/api-integration.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/api-integration
    type: Documentation
  description: The Snowflake API Integration API is a REST API that you can use to access, update, and perform certain actions on API Integration resource in a Snowflake database.
- aid: snowflake:snowflake-artifact-repository-api
  name: Snowflake Artifact Repository API
  tags: []
  properties:
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/artifact-repository
    type: Documentation
  description: The Snowflake Artifact Repository API is a REST API that you can use to access, update, and perform certain actions on Artifact Repository resources in a Snowflake database.
- aid: snowflake:snowflake-catalog-integration-api
  name: Snowflake Catalog Integration API
  tags: []
  properties:
  - url: openapi/catalog-integration.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/catalog-integration
    type: Documentation
  description: The Snowflake Catalog Integration API is a REST API that you can use to access, update, and perform certain actions on Catalog Integration resource in a Snowflake database.
- aid: snowflake:snowflake-compute-pools-api
  name: Snowflake Compute Pools API
  tags: []
  properties:
  - url: openapi/compute-pool.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/compute-pool
    type: Documentation
  description: The Snowflake Compute Pools API is a REST API that you can use to access, update, and perform common actions on Compute Pool resources.
- aid: snowflake:cortex-analyst-api
  name: Cortex Analyst API
  tags: []
  properties:
  - url: openapi/cortex-analyst.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst/rest-api
    type: Documentation
  description: The Snowflake Cortex Analyst API is a REST API that allows end user to chat with their data leveraging semantic models to generate SQL queries.
- aid: snowflake:cortex-embed-api
  name: Cortex Embed API
  tags: []
  properties:
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/cortex-embed
    type: Documentation
  description: The Snowflake Cortex Embed API is a REST API that performs LLM embedding for input text, similar to the Snowflake Cortex EMBED_TEXT functions.
- aid: snowflake:cortex-inference-api
  name: Cortex Inference API
  tags: []
  properties:
  - url: openapi/cortex-inference.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/cortex-inference
    type: Documentation
  description: OpenAPI 3.0 specification for the Cortex REST API.
- aid: snowflake:cortex-search-rest-api
  name: Cortex Search REST API
  tags: []
  properties:
  - url: openapi/cortex-search-service.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/cortex-search-service
    type: Documentation
  description: OpenAPI 3.0 specification for the Cortex Search REST API.
- aid: snowflake:snowflake-database-role-api
  name: Snowflake Database Role API
  tags: []
  properties:
  - url: openapi/database-role.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/database-role
    type: Documentation
  description: The Snowflake Database Role API is a REST API that you can use to access, update, and perform certain actions on Database Role resource in a Snowflake database.
- aid: snowflake:snowflake-database-api
  name: Snowflake Database API
  tags: []
  properties:
  - url: openapi/database.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/database
    type: Documentation
  - url: json-schema/snowflake-database-schema.json
    type: JSONSchema
  - url: json-ld/snowflake-context.jsonld
    type: JSON-LD Context
  description: The Snowflake Database API is a REST API that you can use to access, update, and perform certain actions on Database resource in Snowflake.
- aid: snowflake:snowflake-dynamic-table-api
  name: Snowflake Dynamic Table API
  tags: []
  properties:
  - url: openapi/dynamic-table.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/dynamic-table
    type: Documentation
  description: The Snowflake Dynamic Table API is a REST API that you can use to access, update, and perform certain actions on Dynamic Tables resource in a Snowflake database.
- aid: snowflake:snowflake-event-table-api
  name: Snowflake Event Table API
  tags: []
  properties:
  - url: openapi/event-table.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/event-table
    type: Documentation
  description: The Snowflake Event Table API is a REST API that you can use to access, update, and perform certain actions on Event Table resource in a Snowflake database.
- aid: snowflake:snowflake-external-volume-api
  name: Snowflake External Volume API
  tags: []
  properties:
  - url: openapi/external-volume.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/external-volume
    type: Documentation
  description: The Snowflake External Volume API is a REST API that you can use to access, update, and perform certain actions on External Volume resource in a Snowflake database.
- aid: snowflake:snowflake-function-api
  name: Snowflake Function API
  tags: []
  properties:
  - url: openapi/function.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/function
    type: Documentation
  description: The Snowflake Function API is a REST API that allows caller to create, execute and drop functions in a Snowflake database.
- aid: snowflake:snowflake-grant-api
  name: Snowflake Grant API
  tags: []
  properties:
  - url: openapi/grant.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/grant
    type: Documentation
  description: The Snowflake Grant API is a REST API that you can use to show or manage privileges that have been provided to users and roles in a Snowflake database.
- aid: snowflake:snowflake-iceberg-table-api
  name: Snowflake Iceberg Table API
  tags: []
  properties:
  - url: openapi/iceberg-table.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/iceberg-table
    type: Documentation
  description: The Snowflake Iceberg Table API is a REST API that you can use to access, update, and perform certain actions on Iceberg Table resource in a Snowflake database.
- aid: snowflake:snowflake-image-repository-api
  name: Snowflake Image Repository API
  tags: []
  properties:
  - url: openapi/image-repository.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/image-repository
    type: Documentation
  description: The Snowflake Image Repository API is a REST API that you can use to access, update, and perform common actions on Image Repository resource in Snowflake.
- aid: snowflake:snowflake-managed-account-api
  name: Snowflake Managed Account API
  tags: []
  properties:
  - url: openapi/managed-account.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/managed-account
    type: Documentation
  description: The Snowflake Managed Account API is a REST API that you can use to access, update, and perform certain actions on Managed Account resource in Snowflake.
- aid: snowflake:snowflake-network-policy-api
  name: Snowflake Network Policy API
  tags: []
  properties:
  - url: openapi/network-policy.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/network-policy
    type: Documentation
  description: The Snowflake Network Policy API is a REST API that you can use to access, update, and perform certain actions on Network Policy resource in a Snowflake database.
- aid: snowflake:snowflake-notebook-api
  name: Snowflake Notebook API
  tags: []
  properties:
  - url: openapi/notebook.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/notebook
    type: Documentation
  description: The Snowflake Notebook API is a REST API that you can use to access, update, and perform certain actions on Notebook resource in a Snowflake database.
- aid: snowflake:snowflake-notification-integration-api
  name: Snowflake Notification Integration API
  tags: []
  properties:
  - url: openapi/notification-integration.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/notification-integration
    type: Documentation
  description: The Snowflake Notification Integration API is a REST API that you can use to access, update, and perform certain actions on Notification Integration resource in a Snowflake database.
- aid: snowflake:snowflake-pipe-api
  name: Snowflake Pipe API
  tags: []
  properties:
  - url: openapi/pipe.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/pipe
    type: Documentation
  description: The Snowflake Pipe API is a REST API that you can use to access, update, and perform certain actions on Pipe resource in a Snowflake database.
- aid: snowflake:snowflake-procedure-api
  name: Snowflake Procedure API
  tags: []
  properties:
  - url: openapi/procedure.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/procedure
    type: Documentation
  description: The Snowflake Procedure API is a REST API that you can use to access, update, and perform certain actions on Procedure resource in a Snowflake database.
- aid: snowflake:snowflake-result-api
  name: Snowflake Result API
  tags: []
  properties:
  - url: openapi/result.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/result
    type: Documentation
  description: The Snowflake Result API is a REST API that you can use to check request status and fetch request response.
- aid: snowflake:snowflake-role-api
  name: Snowflake Role API
  tags: []
  properties:
  - url: openapi/role.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/role
    type: Documentation
  description: The Snowflake Role API is a REST API that you can use to access, update, and perform certain actions on Role resource in a Snowflake database.
- aid: snowflake:snowflake-schema-api
  name: Snowflake Schema API
  tags: []
  properties:
  - url: openapi/schema.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/schema
    type: Documentation
  description: The Snowflake Schema API is a REST API that you can use to access, update, and perform certain actions on a Snowflake schema.
- aid: snowflake:snowflake-services-api
  name: Snowflake Services API
  tags: []
  properties:
  - url: openapi/service.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/service
    type: Documentation
  description: The Snowflake Services API is a REST API that you can use to access, update, and perform certain actions on Services resource in a Snowflake database.
- aid: snowflake:snowflake-sql-api
  name: Snowflake SQL API
  tags: []
  properties:
  - url: openapi/sqlapi.yaml
    type: OpenAPI
  - url: openapi/snowflake-sql-rest-api.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/sql-api/index
    type: Documentation
  - url: json-ld/snowflake-context.jsonld
    type: JSON-LD Context
  description: The Snowflake SQL API is a REST API that you can use to access and update data in a Snowflake database.
- aid: snowflake:snowflake-stage-api
  name: Snowflake Stage API
  tags: []
  properties:
  - url: openapi/stage.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/stage
    type: Documentation
  description: The Snowflake Stage API is a REST API that you can use to access, update, and perform certain actions on stage resources in a Snowflake database.
- aid: snowflake:snowflake-stream-api
  name: Snowflake Stream API
  tags: []
  properties:
  - url: openapi/stream.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/stream
    type: Documentation
  description: The Snowflake Stream API is a REST API that you can use to access, update, and perform certain actions on Stream resource in a Snowflake database.
- aid: snowflake:snowflake-table-api
  name: Snowflake Table API
  tags: []
  properties:
  - url: openapi/table.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/table
    type: Documentation
  description: The Snowflake Table API is a REST API that you can use to access, update, and perform certain actions on Tables resource in a Snowflake database.
- aid: snowflake:snowflake-task-api
  name: Snowflake Task API
  tags: []
  properties:
  - url: openapi/task.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/task
    type: Documentation
  description: The Snowflake Task API is a REST API that you can use to access, update, and perform certain actions on task resources in a Snowflake database.
- aid: snowflake:snowflake-user-defined-function-api
  name: Snowflake User Defined Function API
  tags: []
  properties:
  - url: openapi/user-defined-function.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/user-defined-function
    type: Documentation
  description: The Snowflake User Defined Function API is a REST API that you can use to access, update, and perform certain actions on User Defined Function resource in a Snowflake database.
- aid: snowflake:snowflake-user-api
  name: Snowflake User API
  tags: []
  properties:
  - url: openapi/user.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/user
    type: Documentation
  description: The Snowflake User API is a REST API that you can use to access, update, and perform certain action on Users in a Snowflake database.
- aid: snowflake:snowflake-view-api
  name: Snowflake View API
  tags: []
  properties:
  - url: openapi/view.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/view
    type: Documentation
  description: The Snowflake View API is a REST API that you can use to access, update, and perform certain actions on View resource in a Snowflake database.
- aid: snowflake:snowflake-warehouse-api
  name: Snowflake Warehouse API
  tags: []
  properties:
  - url: openapi/warehouse.yaml
    type: OpenAPI
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/warehouse
    type: Documentation
  - url: json-schema/snowflake-warehouse-schema.json
    type: JSONSchema
  - url: json-ld/snowflake-context.jsonld
    type: JSON-LD Context
  description: The Snowflake Warehouse API is a REST API that you can use to access, customize and manage virtual warehouse in a Snowflake account.
- aid: snowflake:snowflake-network-rule-api
  name: Snowflake Network Rule API
  tags: []
  properties:
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/network-rule
    type: Documentation
  description: The Snowflake Network Rule API is a REST API that you can use to access, update, and perform certain actions on Network Rule resources in a Snowflake database.
- aid: snowflake:snowflake-password-policy-api
  name: Snowflake Password Policy API
  tags: []
  properties:
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/password-policy
    type: Documentation
  description: The Snowflake Password Policy API is a REST API that you can use to access, update, and perform certain actions on Password Policy resources in a Snowflake database.
- aid: snowflake:snowflake-secret-api
  name: Snowflake Secret API
  tags: []
  properties:
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/secret
    type: Documentation
  description: The Snowflake Secret API is a REST API that you can use to access, update, and perform certain actions on Secret resources in a Snowflake database.
- aid: snowflake:snowflake-sequence-api
  name: Snowflake Sequence API
  tags: []
  properties:
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/sequence
    type: Documentation
  description: The Snowflake Sequence API is a REST API that you can use to access, update, and perform certain actions on Sequence resources in a Snowflake database.
- aid: snowflake:snowflake-spark-connect-api
  name: Snowflake Spark Connect API
  tags: []
  properties:
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/spark-connect
    type: Documentation
  description: The Snowflake Spark Connect API is a REST API that enables execution of Spark workloads on Snowflake infrastructure through REST endpoints.
- aid: snowflake:snowflake-streamlit-api
  name: Snowflake Streamlit API
  tags: []
  properties:
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/streamlit
    type: Documentation
  description: The Snowflake Streamlit API is a REST API that you can use to access, update, and perform certain actions on Streamlit application resources in a Snowflake database.
- aid: snowflake:snowflake-tag-api
  name: Snowflake Tag API
  tags: []
  properties:
  - url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/reference/tag
    type: Documentation
  description: The Snowflake Tag API is a REST API that you can use to access, update, and perform certain actions on Tag resources in a Snowflake database.
- aid: snowflake:cortex-agents-api
  name: Cortex Agents API
  tags: []
  properties:
  - url: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-rest-api
    type: Documentation
  description: The Snowflake Cortex Agents API is a REST API that you can use to create, manage, and interact with Cortex Agent objects in a Snowflake account.
- aid: snowflake:snowpipe-rest-api
  name: Snowpipe REST API
  tags: []
  properties:
  - url: https://docs.snowflake.com/en/user-guide/data-load-snowpipe-rest-apis
    type: Documentation
  description: The Snowpipe REST API provides REST endpoints for defining the list of files to ingest and fetching reports of the load history for continuous data loading into Snowflake.
name: Snowflake
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- NoSQL
- SQL
- T1
type: Contract
image: https://www.snowflake.com/wp-content/themes/snowflake/assets/img/brand-guidelines/logo-sno-blue-example.svg
access: 3rd-Party
common:
- url: https://status.snowflake.com/?_ga=2.248111808.698576284.1754337355-1524607073.1754337355&_fsi=Nti5Apdj
  name: Snowflake Status
  type: Status
  description: 'null'
- url: https://docs.snowflake.com/en/release-notes/overview
  name: Releases | Snowflake Documentation
  type: ChangeLog
  description: 'null'
- url: https://docs.snowflake.com/en/guides
  name: Guides - Snowflake Documentation
  type: Guide
  description: 'null'
- url: https://docs.snowflake.com/en/user-guide-getting-started
  name: Getting Started - Snowflake Documentation
  type: GettingStarted
  description: 'null'
- url: https://docs.snowflake.com/en/tutorials
  name: Tutorials - Snowflake Documentation
  type: Tutorials
  description: 'null'
- url: https://www.snowflake.com/en/legal/snowflake-site-terms/?_ga=2.189374828.698576284.1754337355-1524607073.1754337355
  name: Snowflake Site Terms
  type: TermsOfService
  description: 'null'
- url: https://docs.snowflake.com/?_ga=2.248111808.698576284.1754337355-1524607073.1754337355
  name: Snowflake Documentation
  type: Documentation
  description: 'null'
- url: https://www.snowflake.com/en/legal/privacy/privacy-policy/
  name: Snowflake Privacy Notice
  type: PrivacyPolicy
  description: 'null'
- url: https://www.snowflake.com/en/engineering-blog/
  name: Engineering Blog
  type: Blog
  description: 'null'
- url: https://www.snowflake.com/en/legal/addenda/priority-support-services-description/
  name: Priority Support Services Description
  type: PremiumSupport
  description: 'null'
- url: https://www.snowflake.com/en/support/
  name: Snowflake Support - Snowflake
  type: Support
  description: 'null'
- url: https://www.snowflake.com/en/pricing-options/
  name: Pricing Options
  type: Plans
  description: 'null'
- url: https://www.snowflake.com/en/developers/
  name: Snowflake for Developers
  type: Portal
  description: 'null'
- url: https://www.snowflake.com/about/events/
  name: Snowflake Events | Upcoming Snowflake Events Around the World
  type: Events
  description: 'null'
- url: https://www.snowflake.com/en/blog/
  name: Inside the AI Data Cloud | Snowflake Blog
  type: Blog
  description: 'null'
- url: https://www.snowflake.com/en/
  name: Snowflake AI Data Cloud
  type: Website
  description: 'null'
- url: https://github.com/snowflakedb/snowflake-rest-api-specs
  name: OpenAPI
  type: OpenAPI
created: '2025-06-05'
modified: '2026-04-07'
position: Consuming
description: Snowflake is a cloud-based data platform that provides data warehousing, data lakes, data engineering, data science, and data application development capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

