---
aid: servicenow
url: https://raw.githubusercontent.com/api-evangelist/servicenow/refs/heads/main/apis.yml
apis:
- aid: servicenow:servicenow-table-api
  name: ServiceNow Table API
  tags:
  - CRUD
  - Data
  - ITSM
  - Records
  - Tables
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_TableAPI.html
  baseURL: https://{instance}.service-now.com/api/now/table
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_TableAPI.html
    type: Documentation
  - url: https://www.servicenow.com/docs/bundle/xanadu-api-reference/page/integrate/inbound-rest/concept/c_TableAPI.html
    type: Reference
  - url: openapi/servicenow-table-api-openapi.yml
    type: OpenAPI
  description: The ServiceNow Table API provides endpoints to perform create, read, update, and delete (CRUD) operations on records within any ServiceNow table. It is the primary REST interface for interacting with ServiceNow platform data such as incidents, problems, changes, and custom tables.
- aid: servicenow:servicenow-aggregate-api
  name: ServiceNow Aggregate API
  tags:
  - Aggregation
  - Analytics
  - Reporting
  - Statistics
  - Tables
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_AggregateAPI.html
  baseURL: https://{instance}.service-now.com/api/now/stats
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_AggregateAPI.html
    type: Documentation
  - url: openapi/servicenow-aggregate-api-openapi.yml
    type: OpenAPI
  description: The ServiceNow Aggregate API provides endpoints to compute aggregate statistics (count, average, min, max, sum) against records in any ServiceNow table. It supports grouping and filtering results, making it useful for reporting and dashboard data retrieval.
- aid: servicenow:servicenow-attachment-api
  name: ServiceNow Attachment API
  tags:
  - Attachments
  - Files
  - Records
  - Upload
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_AttachmentAPI.html
  baseURL: https://{instance}.service-now.com/api/now/attachment
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_AttachmentAPI.html
    type: Documentation
  - url: openapi/servicenow-attachment-api-openapi.yml
    type: OpenAPI
  description: The ServiceNow Attachment API enables uploading, retrieving, and deleting file attachments associated with records in ServiceNow tables. It supports uploading files via multipart/form-data or binary streams and allows up to 1024 MB file size by default.
- aid: servicenow:servicenow-import-set-api
  name: ServiceNow Import Set API
  tags:
  - Data Loading
  - ETL
  - Import
  - Integration
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_ImportSetAPI.html
  baseURL: https://{instance}.service-now.com/api/now/import
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_ImportSetAPI.html
    type: Documentation
  - url: openapi/servicenow-import-set-api-openapi.yml
    type: OpenAPI
  description: The ServiceNow Import Set API allows external systems to push data into ServiceNow import set tables, which can then be synchronously or asynchronously transformed and loaded into target tables. It is commonly used for integrating external data sources with ServiceNow using transform maps.
- aid: servicenow:servicenow-batch-api
  name: ServiceNow Batch API
  tags:
  - Batch
  - Integration
  - Performance
  - REST
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/batch-api.html
  baseURL: https://{instance}.service-now.com/api/now/v1/batch
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/batch-api.html
    type: Documentation
  description: The ServiceNow Batch API enables sending multiple REST API requests in a single HTTP call, reducing network overhead and improving integration performance. Each request in the batch is executed independently, and the API returns a stream of corresponding responses.
- aid: servicenow:servicenow-change-management-api
  name: ServiceNow Change Management API
  tags:
  - Change Management
  - IT Operations
  - ITSM
  - Workflows
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/change-management-api.html
  baseURL: https://{instance}.service-now.com/api/sn_chg_rest/v1/change
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/change-management-api.html
    type: Documentation
  - url: https://www.servicenow.com/docs/bundle/xanadu-api-reference/page/integrate/inbound-rest/concept/change-management-api.html
    type: Reference
  - url: openapi/servicenow-change-management-api-openapi.yml
    type: OpenAPI
  description: The ServiceNow Change Management API provides REST endpoints for creating, retrieving, updating, and managing change requests and their associated tasks and approvals. It supports the full change lifecycle including normal, standard, and emergency change types.
- aid: servicenow:servicenow-knowledge-management-api
  name: ServiceNow Knowledge Management API
  tags:
  - Articles
  - Knowledge Base
  - Knowledge Management
  - Self-Service
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/knowledge-api.html
  baseURL: https://{instance}.service-now.com/api/sn_km_api/knowledge
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/knowledge-api.html
    type: Documentation
  - url: https://www.servicenow.com/docs/bundle/xanadu-api-reference/page/integrate/inbound-rest/concept/knowledge-api.html
    type: Reference
  description: The ServiceNow Knowledge Management REST API provides endpoints for searching and retrieving knowledge articles, including most-viewed and featured articles. It supports public and authenticated access to knowledge bases and requires the Knowledge API (sn_km_api) plugin to be activated.
- aid: servicenow:servicenow-service-catalog-api
  name: ServiceNow Service Catalog API
  tags:
  - ITSM
  - Requests
  - Self-Service
  - Service Catalog
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_ServiceCatalogAPI.html
  baseURL: https://{instance}.service-now.com/api/sn_sc/servicecatalog
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_ServiceCatalogAPI.html
    type: Documentation
  - url: https://www.servicenow.com/docs/bundle/xanadu-api-reference/page/integrate/inbound-rest/concept/c_ServiceCatalogAPI.html
    type: Reference
  - url: openapi/servicenow-service-catalog-api-openapi.yml
    type: OpenAPI
  description: The ServiceNow Service Catalog API provides REST endpoints for browsing catalog categories and items, retrieving catalog item details and variables, and submitting catalog requests. It enables external applications and portals to integrate with ServiceNow's self-service request capabilities.
- aid: servicenow:servicenow-cmdb-instance-api
  name: ServiceNow CMDB Instance API
  tags:
  - Assets
  - CMDB
  - Configuration Management
  - IT Operations
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/cmdb-instance-api.html
  baseURL: https://{instance}.service-now.com/api/now/cmdb/instance
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/cmdb-instance-api.html
    type: Documentation
  - url: https://www.servicenow.com/docs/bundle/xanadu-api-reference/page/integrate/inbound-rest/concept/cmdb-instance-api.html
    type: Reference
  - url: openapi/servicenow-cmdb-instance-api-openapi.yml
    type: OpenAPI
  description: The ServiceNow CMDB Instance API provides REST endpoints for retrieving configuration item (CI) records from the Configuration Management Database by class name and sys_id. It is used to query and access infrastructure and application CI data stored in ServiceNow's CMDB.
- aid: servicenow:servicenow-identification-reconciliation-api
  name: ServiceNow Identification and Reconciliation API
  tags:
  - CMDB
  - Configuration Management
  - Discovery
  - Reconciliation
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_IdentifyReconcileAPI.html
  baseURL: https://{instance}.service-now.com/api/now/identifyreconcile
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_IdentifyReconcileAPI.html
    type: Documentation
  - url: https://www.servicenow.com/docs/bundle/xanadu-api-reference/page/integrate/inbound-rest/concept/c_IdentifyReconcileAPI.html
    type: Reference
  description: The ServiceNow Identification and Reconciliation API provides a REST endpoint for creating or updating configuration items (CIs) in the CMDB using the platform's identification and reconciliation engine. It ensures that CI data from external discovery sources is correctly identified, deduplicated, and reconciled against existing CMDB records.
- aid: servicenow:servicenow-performance-analytics-api
  name: ServiceNow Performance Analytics API
  tags:
  - Analytics
  - Dashboards
  - Performance
  - Reporting
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_PerformanceAnalyticsAPI.html
  baseURL: https://{instance}.service-now.com/api/now/pa
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_PerformanceAnalyticsAPI.html
    type: Documentation
  description: The ServiceNow Performance Analytics API provides REST endpoints for retrieving performance analytics data including scores, breakdowns, and widget data. It enables integration with external dashboards and reporting tools to access historical and real-time KPI data collected by the Now Platform.
- aid: servicenow:servicenow-contact-api
  name: ServiceNow Contact API
  tags:
  - Contacts
  - CSM
  - Customer Service
  - Records
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/r/xanadu/api-reference/rest-apis/contact-api.html
  baseURL: https://{instance}.service-now.com/api/now/contact
  properties:
  - url: https://www.servicenow.com/docs/r/xanadu/api-reference/rest-apis/contact-api.html
    type: Documentation
  - url: openapi/contact-api-openapi.yaml
    type: OpenAPI
  description: The ServiceNow Contact API provides endpoints for retrieving and updating Customer Service Management (CSM) contact records. It also supports generating new social media profile records when creating a contact, and requires the Customer Service plugin (com.sn_customerservice).
- aid: servicenow:servicenow-trouble-ticket-api
  name: ServiceNow Trouble Ticket Open API
  tags:
  - Customer Service
  - Incidents
  - TM Forum
  - Trouble Tickets
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html
  baseURL: https://{instance}.service-now.com/api/now/troubleticket
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html
    type: Documentation
  - url: openapi/trouble-ticket-openapi.yaml
    type: OpenAPI
  description: The ServiceNow Trouble Ticket Open API provides endpoints to create, update, and retrieve data from Case, Incident, and Service Problem Case tables. It is a ServiceNow implementation of the TM Forum Trouble Ticket Management API REST specification for managing ticket information between external ticketing systems and the ServiceNow AI Platform.
- aid: servicenow:servicenow-scripted-rest-apis
  name: ServiceNow Scripted REST APIs
  tags:
  - Custom APIs
  - Integration
  - Platform
  - Scripting
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/custom-web-services/concept/c_CustomWebServices.html
  baseURL: https://{instance}.service-now.com/api/{namespace}/{api_id}
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/custom-web-services/concept/c_CustomWebServices.html
    type: Documentation
  description: ServiceNow Scripted REST APIs allow developers to create custom REST API endpoints on the Now Platform using server-side JavaScript. They support custom request processing logic, authentication, and response handling, enabling organizations to expose business-specific functionality as web services to external consumers.
- aid: servicenow:servicenow-graphql-api
  name: ServiceNow GraphQL API
  tags:
  - Custom APIs
  - GraphQL
  - Integration
  - Platform
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://docs.servicenow.com/bundle/tokyo-application-development/page/integrate/graphql/concept/scripted-graph-ql.html
  baseURL: https://{instance}.service-now.com/api/now/graphql
  properties:
  - url: https://docs.servicenow.com/bundle/tokyo-application-development/page/integrate/graphql/concept/scripted-graph-ql.html
    type: Documentation
  - url: https://www.servicenow.com/community/developer-articles/getting-started-graphql-api-framework/ta-p/2312207
    type: Getting Started
  description: The ServiceNow GraphQL API framework allows developers to create custom GraphQL API schemas on the Now Platform for querying record data from components or external systems. It supports defining resolvers with server-side scripts and enables flexible, client-driven queries as an alternative to REST-based integration.
- aid: servicenow:servicenow-application-service-api
  name: ServiceNow Application Service API
  tags:
  - Application Services
  - CMDB
  - IT Operations
  - Service Mapping
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/application-service-api.html
  baseURL: https://{instance}.service-now.com/api/now/cmdb/app_service
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/application-service-api.html
    type: Documentation
  description: The ServiceNow Application Service API provides REST endpoints to create, modify, and update application services in the CMDB. It requires users to have the app_service_admin role and enables programmatic management of business application service mappings and their associated configuration items.
- aid: servicenow:servicenow-case-api
  name: ServiceNow Case API
  tags:
  - Cases
  - CSM
  - Customer Service
  - Support
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/case-api.html
  baseURL: https://{instance}.service-now.com/api/sn_customerservice/case
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/case-api.html
    type: Documentation
  description: The ServiceNow Case API provides REST endpoints for creating, retrieving, and updating Customer Service Management (CSM) case records. It supports the full case lifecycle including case creation, assignment, escalation, and resolution within the CSM application.
- aid: servicenow:servicenow-account-api
  name: ServiceNow Account API
  tags:
  - Accounts
  - CSM
  - Customer Service
  - Records
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/account-api.html
  baseURL: https://{instance}.service-now.com/api/now/account
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/account-api.html
    type: Documentation
  description: The ServiceNow Account API provides REST endpoints for retrieving and managing customer account records within Customer Service Management (CSM). It enables external systems to query and update account information used for B2B customer relationship tracking.
- aid: servicenow:servicenow-consumer-api
  name: ServiceNow Consumer API
  tags:
  - Consumers
  - CSM
  - Customer Service
  - Self-Service
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html
  baseURL: https://{instance}.service-now.com/api/now/consumer
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html
    type: Documentation
  description: The ServiceNow Consumer API provides REST endpoints for retrieving and updating CSM consumer records. It supports managing individual consumer profiles and can generate new social media profile records when creating a consumer entry within the Customer Service Management application.
- aid: servicenow:servicenow-csm-attachment-api
  name: ServiceNow CSM Attachment API
  tags:
  - Attachments
  - CSM
  - Customer Service
  - Files
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/attachment_csm-api.html
  baseURL: https://{instance}.service-now.com/api/sn_customerservice/attachment
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/attachment_csm-api.html
    type: Documentation
  description: The ServiceNow CSM Attachment API provides REST endpoints for uploading and managing file attachments on Customer Service Management records such as cases and interactions. It extends the base Attachment API with CSM-specific functionality and access controls.
- aid: servicenow:servicenow-email-api
  name: ServiceNow Email API
  tags:
  - Email
  - Messaging
  - Notifications
  - Platform
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/email-api.html
  baseURL: https://{instance}.service-now.com/api/now/email
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/email-api.html
    type: Documentation
  description: The ServiceNow Email API provides REST endpoints for sending email messages from the Now Platform. It allows external systems and integrations to trigger email notifications and communications through ServiceNow's email infrastructure.
- aid: servicenow:servicenow-cicd-api
  name: ServiceNow CI/CD API
  tags:
  - Automation
  - CI/CD
  - Deployment
  - DevOps
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/cicd-api.html
  baseURL: https://{instance}.service-now.com/api/sn_cicd
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/cicd-api.html
    type: Documentation
  description: The ServiceNow CI/CD API provides REST endpoints for integrating ServiceNow application development with continuous integration and continuous delivery pipelines. It supports operations such as applying changes, running ATF test suites, activating plugins, and managing application installations from external CI/CD tools.
- aid: servicenow:servicenow-cicd-update-set-api
  name: ServiceNow CI/CD Update Set API
  tags:
  - CI/CD
  - Deployment
  - DevOps
  - Update Sets
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/cicd-update-set-api.html
  baseURL: https://{instance}.service-now.com/api/sn_cicd/update_set
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/cicd-update-set-api.html
    type: Documentation
  description: The ServiceNow CI/CD Update Set API provides REST methods to create, retrieve, preview, commit, and back out update sets. It enables automated deployment workflows by allowing CI/CD pipelines to manage update set transfers between ServiceNow instances.
- aid: servicenow:servicenow-devops-api
  name: ServiceNow DevOps API
  tags:
  - Change Velocity
  - CI/CD
  - DevOps
  - Pipelines
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/devops-api.html
  baseURL: https://{instance}.service-now.com/api/sn_devops
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/devops-api.html
    type: Documentation
  description: The ServiceNow DevOps API provides REST endpoints for integrating external DevOps toolchains with ServiceNow's DevOps Change Velocity product. It enables automated change request creation, artifact and package tracking, and pipeline orchestration from tools such as Jenkins, Azure DevOps, and GitLab.
- aid: servicenow:servicenow-devops-config-api
  name: ServiceNow DevOps Config API
  tags:
  - Automation
  - Change Management
  - Configuration
  - DevOps
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/devops-config-api.html
  baseURL: https://{instance}.service-now.com/api/sn_devops_config
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/devops-config-api.html
    type: Documentation
  description: The ServiceNow DevOps Config API provides REST endpoints for managing DevOps configuration data and policies. It supports configuration validation and compliance checks as part of the DevOps change acceleration workflow.
- aid: servicenow:servicenow-cmdb-meta-api
  name: ServiceNow CMDB Meta API
  tags:
  - CMDB
  - Configuration Management
  - Metadata
  - Schema
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/cmdb-meta-api.html
  baseURL: https://{instance}.service-now.com/api/now/cmdb/meta
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/cmdb-meta-api.html
    type: Documentation
  description: The ServiceNow CMDB Meta API provides REST endpoints for retrieving metadata about CMDB classes, including their attributes, relationships, and hierarchy. It enables developers to programmatically discover the CMDB data model and schema for building integrations and reporting tools.
- aid: servicenow:servicenow-cmdb-data-ingestion-api
  name: ServiceNow CMDB Data Ingestion API
  tags:
  - CMDB
  - Configuration Management
  - Data Ingestion
  - Integration
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/cmdb-ingest-api.html
  baseURL: https://{instance}.service-now.com/api/now/cmdb/ingest
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/cmdb-ingest-api.html
    type: Documentation
  description: The ServiceNow CMDB Data Ingestion API provides REST endpoints for bulk ingesting configuration item data into the CMDB from external data sources. It supports high-volume CI data loading with built-in identification and reconciliation processing.
- aid: servicenow:servicenow-metricbase-time-series-api
  name: ServiceNow MetricBase Time Series API
  tags:
  - ITOM
  - Metrics
  - Monitoring
  - Time Series
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/Clotho-Time-Series-API.html
  baseURL: https://{instance}.service-now.com/api/now/clotho
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/Clotho-Time-Series-API.html
    type: Documentation
  description: The ServiceNow MetricBase Time Series API (formerly Clotho) provides REST endpoints for storing, retrieving, and transforming time series metric data on the Now Platform. It is used by IT Operations Management to ingest and query monitoring data such as CPU usage, memory utilization, and custom metrics.
- aid: servicenow:servicenow-interaction-management-api
  name: ServiceNow Interaction Management API
  tags:
  - Agent Workspace
  - Customer Service
  - Interactions
  - Omnichannel
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/interaction-management-api.html
  baseURL: https://{instance}.service-now.com/api/interaction
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/interaction-management-api.html
    type: Documentation
  description: The ServiceNow Interaction Management API provides REST endpoints for creating and managing customer interactions across multiple channels. It supports omnichannel routing and enables external contact center systems to create and update interaction records in ServiceNow Agent Workspace.
- aid: servicenow:servicenow-voice-interaction-resource-api
  name: ServiceNow Voice Interaction Resource API
  tags:
  - Contact Center
  - Interactions
  - Telephony
  - Voice
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/voice-interaction-resource-api.html
  baseURL: https://{instance}.service-now.com/api/now/voice
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/voice-interaction-resource-api.html
    type: Documentation
  description: The ServiceNow Voice Interaction Resource API provides REST endpoints for integrating telephony and voice systems with ServiceNow. It enables Contact Center as a Service (CCaaS) providers to manage voice interactions and route calls to agents within Agent Workspace.
- aid: servicenow:servicenow-user-role-inheritance-api
  name: ServiceNow User Role Inheritance API
  tags:
  - Access Control
  - Roles
  - Security
  - Users
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/user-role-inheritance-api.html
  baseURL: https://{instance}.service-now.com/api/now/user_role_inheritance
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/user-role-inheritance-api.html
    type: Documentation
  description: The ServiceNow User Role Inheritance API provides REST endpoints for querying the role inheritance hierarchy for users and groups. It enables external systems to determine effective roles and permissions assigned through direct assignment or group membership inheritance.
- aid: servicenow:servicenow-hr-api
  name: ServiceNow HR API
  tags:
  - Employee Services
  - HR Service Delivery
  - HRSD
  - Human Resources
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/hr-core-api.html
  baseURL: https://{instance}.service-now.com/api/sn_hr_core
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/hr-core-api.html
    type: Documentation
  description: The ServiceNow HR API provides REST endpoints for managing Human Resources Service Delivery (HRSD) data including employee cases, lifecycle events, and HR service requests. It enables integration with external HR systems such as Workday and SuccessFactors for employee data synchronization.
- aid: servicenow:servicenow-event-management-topic-api
  name: ServiceNow Event Management Topic Open API
  tags:
  - Alerts
  - Event Management
  - ITOM
  - Monitoring
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/event_management_topic-api.html
  baseURL: https://{instance}.service-now.com/api/em/topic
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/event_management_topic-api.html
    type: Documentation
  - url: asyncapi/servicenow-events-asyncapi.yml
    type: AsyncAPI
  description: The ServiceNow Event Management Topic Open API provides REST endpoints for managing event topics and subscriptions within IT Operations Management. It enables external monitoring tools to publish events and subscribe to event notifications using a topic-based messaging pattern.
- aid: servicenow:servicenow-predictive-intelligence-api
  name: ServiceNow Predictive Intelligence API
  tags:
  - AI
  - Classification
  - Machine Learning
  - Predictions
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/agent-intelligence-api.html
  baseURL: https://{instance}.service-now.com/api/now/agent_intelligence
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/agent-intelligence-api.html
    type: Documentation
  description: The ServiceNow Predictive Intelligence API provides REST endpoints for accessing machine learning prediction models on the Now Platform. It supports classification, similarity matching, and regression predictions to automate categorization, assignment, and prioritization of records such as incidents and cases.
- aid: servicenow:servicenow-awa-agent-api
  name: ServiceNow AWA Agent API
  tags:
  - Agent Workspace
  - Queues
  - Routing
  - Workforce Management
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/agent-api.html
  baseURL: https://{instance}.service-now.com/api/now/awa/agent
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/agent-api.html
    type: Documentation
  description: The ServiceNow AWA Agent API provides REST endpoints for managing agent availability, presence, and capacity within Advanced Work Assignment (AWA). It enables external systems to query and update agent status for work routing and workforce management purposes.
- aid: servicenow:servicenow-awa-offer-work-api
  name: ServiceNow AWA Offer Work API
  tags:
  - Agent Workspace
  - Queues
  - Routing
  - Work Assignment
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/awa-offer-work-api.html
  baseURL: https://{instance}.service-now.com/api/now/awa/offerwork
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/awa-offer-work-api.html
    type: Documentation
  description: The ServiceNow AWA Offer Work API provides REST endpoints to assign or transfer work items to agents through the Advanced Work Assignment engine. It enables programmatic distribution of tasks, cases, and interactions to available agents based on capacity and skills.
- aid: servicenow:servicenow-virtual-agent-bot-integration-api
  name: ServiceNow Virtual Agent Bot Integration API
  tags:
  - Chatbot
  - Conversational AI
  - Self-Service
  - Virtual Agent
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/bot-api.html
  baseURL: https://{instance}.service-now.com/api/sn_va_as_service
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/bot-api.html
    type: Documentation
  description: The ServiceNow Virtual Agent Bot Integration API provides REST endpoints for integrating external messaging platforms and chatbot frameworks with ServiceNow Virtual Agent. It enables sending and receiving conversational messages to automate employee and customer self-service through AI-powered virtual agents.
- aid: servicenow:servicenow-openframe-api
  name: ServiceNow Openframe API
  tags:
  - CCaaS
  - Contact Center
  - Integration
  - Telephony
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/openframe-api.html
  baseURL: https://{instance}.service-now.com/api/now/openframe
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/openframe-api.html
    type: Documentation
  description: The ServiceNow Openframe API provides REST endpoints that enable Contact Center as a Service (CCaaS) providers to create and update interaction records without using the Operation Handler. It supports third-party telephony integration with ServiceNow Agent Workspace through an open framework.
- aid: servicenow:servicenow-ai-assets-api
  name: ServiceNow AI Assets API
  tags:
  - AI Governance
  - Artificial Intelligence
  - Machine Learning
  - Platform
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/ai-assets-api.html
  baseURL: https://{instance}.service-now.com/api/now/ai/assets
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/ai-assets-api.html
    type: Documentation
  description: The ServiceNow AI Assets API provides REST endpoints to retrieve, update, and create AI assets such as systems, data sets, prompts, and models. It supports AI governance and inventory management by enabling programmatic tracking of AI components deployed across the organization.
- aid: servicenow:servicenow-lead-api
  name: ServiceNow Lead API
  tags:
  - CRM
  - Leads
  - Marketing
  - Sales
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html
  baseURL: https://{instance}.service-now.com/api/sn_lead
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html
    type: Documentation
  description: The ServiceNow Lead API provides REST endpoints to create, update, and retrieve marketing leads and their associated lead line items. It enables integration with external marketing automation and CRM systems to manage the lead lifecycle within ServiceNow.
- aid: servicenow:servicenow-sales-agreement-api
  name: ServiceNow Sales Agreement API
  tags:
  - Agreements
  - Contracts
  - CRM
  - Sales
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html
  baseURL: https://{instance}.service-now.com/api/sn_sales_agreement
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html
    type: Documentation
  description: The ServiceNow Sales Agreement API provides REST methods for creating new sales agreements and retrieving existing sales agreements by sys_id. It supports contract management workflows within ServiceNow's sales operations capabilities.
- aid: servicenow:servicenow-agent-client-collector-api
  name: ServiceNow Agent Client Collector API
  tags:
  - Agents
  - Discovery
  - ITOM
  - Monitoring
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/agnt_clnt_cll-api.html
  baseURL: https://{instance}.service-now.com/api/now/acc
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/agnt_clnt_cll-api.html
    type: Documentation
  description: The ServiceNow Agent Client Collector (ACC) API provides REST endpoints for managing agent client collectors used in IT Operations Management. It enables programmatic interaction with ACC agents for discovery, monitoring, and data collection from infrastructure components.
- aid: servicenow:servicenow-agent-mapping-api
  name: ServiceNow Agent Mapping API
  tags:
  - Agent Workspace
  - Integration
  - Mapping
  - Routing
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/agent-mapping-api.html
  baseURL: https://{instance}.service-now.com/api/now/agent_mapping
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/agent-mapping-api.html
    type: Documentation
  description: The ServiceNow Agent Mapping API provides REST endpoints for managing agent mapping configurations. It enables external systems to create and manage mappings between external agent identifiers and ServiceNow agent records for routing and assignment purposes.
- aid: servicenow:servicenow-automation-center-api
  name: ServiceNow Automation Center API
  tags:
  - Automation
  - Orchestration
  - Platform
  - Workflows
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/auto-api.html
  baseURL: https://{instance}.service-now.com/api/sn_automation_center
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/auto-api.html
    type: Documentation
  description: The ServiceNow Automation Center API provides REST endpoints for managing and executing automation workflows on the Now Platform. It supports programmatic control of automation tasks, enabling external systems to trigger, monitor, and manage automated processes.
- aid: servicenow:servicenow-ap-invoice-api
  name: ServiceNow AP Invoice API
  tags:
  - Accounts Payable
  - Finance
  - Invoices
  - Procurement
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/ap-invoice-api.html
  baseURL: https://{instance}.service-now.com/api/now/ap/invoice
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/ap-invoice-api.html
    type: Documentation
  description: The ServiceNow AP Invoice API provides REST endpoints for managing accounts payable invoice records on the Now Platform. It enables external financial systems to create, retrieve, and update invoice data for procurement and payment processing workflows.
- aid: servicenow:servicenow-csm-order-api
  name: ServiceNow CSM Order API
  tags:
  - Commerce
  - CSM
  - Customer Service
  - Orders
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/order_csm-api.html
  baseURL: https://{instance}.service-now.com/api/sn_customerservice/order
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/order_csm-api.html
    type: Documentation
  description: The ServiceNow CSM Order API provides REST endpoints for managing order records within Customer Service Management. It enables external systems to create, retrieve, and update customer orders and associated order line items.
- aid: servicenow:servicenow-ci-lifecycle-management-api
  name: ServiceNow CI Lifecycle Management API
  tags:
  - CMDB
  - Configuration Management
  - IT Operations
  - Lifecycle
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/ci-lifecycle-management-api.html
  baseURL: https://{instance}.service-now.com/api/now/cmdb/ci_lifecycle
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/ci-lifecycle-management-api.html
    type: Documentation
  description: The ServiceNow CI Lifecycle Management API provides REST endpoints for managing the lifecycle states of configuration items (CIs) in the CMDB. It enables programmatic tracking and transition of CI states from procurement through deployment, operation, and retirement.
- aid: servicenow:servicenow-alarm-management-open-api
  name: ServiceNow Alarm Management Open API
  tags:
  - Alerts
  - Event Management
  - ITOM
  - Monitoring
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/alarm-open-api.html
  baseURL: https://{instance}.service-now.com/api/now/alarm
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/alarm-open-api.html
    type: Documentation
  description: The ServiceNow Alarm Management Open API provides REST endpoints for managing alarm records within IT Operations Management. It supports creating, retrieving, and updating alarm data from external monitoring systems, enabling centralized alarm management on the Now Platform.
- aid: servicenow:servicenow-sam-software-usage-api
  name: ServiceNow SAM Software Usage Data Integration API
  tags:
  - ITAM
  - Licensing
  - Software Asset Management
  - Usage Tracking
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/sam_soft_us_int-api.html
  baseURL: https://{instance}.service-now.com/api/sam/software_usage
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/sam_soft_us_int-api.html
    type: Documentation
  description: The ServiceNow SAM Software Usage Data Integration API provides REST endpoints for importing software usage and metering data into Software Asset Management. It enables third-party software usage tracking tools to feed consumption data into ServiceNow for license compliance and optimization.
- aid: servicenow:servicenow-product-catalog-open-api
  name: ServiceNow Product Catalog Open API
  tags:
  - Commerce
  - Product Catalog
  - Telecommunications
  - TMF
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/product-catalog-open-api.html
  baseURL: https://{instance}.service-now.com/api/sn_ind_tmt_orm/catalogManagement/v4
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/product-catalog-open-api.html
    type: Documentation
  description: The ServiceNow Product Catalog Open API provides REST endpoints for managing product catalog data based on the TM Forum TMF620 specification. It enables querying and managing product specifications, offerings, and categories for telecommunications and order management workflows.
- aid: servicenow:servicenow-service-catalog-open-api
  name: ServiceNow Service Catalog Open API
  tags:
  - Commerce
  - Service Catalog
  - Telecommunications
  - TMF
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/service-catalog-open-api.html
  baseURL: https://{instance}.service-now.com/api/sn_ind_tmt_orm/serviceCatalogManagement/v4
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/service-catalog-open-api.html
    type: Documentation
  description: The ServiceNow Service Catalog Open API provides REST endpoints for managing service catalog data based on the TM Forum TMF633 specification. It supports querying and managing service specifications and service candidates for telecommunications service management.
- aid: servicenow:servicenow-product-order-open-api
  name: ServiceNow Product Order Open API
  tags:
  - Commerce
  - Product Ordering
  - Telecommunications
  - TMF
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/tmf622_product_ordering-api.html
  baseURL: https://{instance}.service-now.com/api/sn_ind_tmt_orm/productOrderingManagement/v4
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/tmf622_product_ordering-api.html
    type: Documentation
  description: The ServiceNow Product Order Open API provides REST endpoints for managing product orders based on the TM Forum TMF622 specification. It enables creating, retrieving, and updating product orders for telecommunications order management workflows.
- aid: servicenow:servicenow-service-order-open-api
  name: ServiceNow Service Order Open API
  tags:
  - Commerce
  - Service Ordering
  - Telecommunications
  - TMF
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/service-order-open-api.html
  baseURL: https://{instance}.service-now.com/api/sn_ind_tmt_orm/serviceOrderingManagement/v4
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/service-order-open-api.html
    type: Documentation
  description: The ServiceNow Service Order Open API provides REST endpoints for managing service orders based on the TM Forum TMF641 specification. It enables creating, retrieving, and updating service orders for telecommunications service ordering workflows.
- aid: servicenow:servicenow-resource-inventory-open-api
  name: ServiceNow Resource Inventory Open API
  tags:
  - Inventory
  - Resources
  - Telecommunications
  - TMF
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/resource-inventory-api.html
  baseURL: https://{instance}.service-now.com/api/sn_ind_tmt_orm/resourceInventoryManagement/v4
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/resource-inventory-api.html
    type: Documentation
  description: The ServiceNow Resource Inventory Open API provides REST endpoints for managing resource inventory data based on TM Forum specifications. It supports querying and managing physical and logical resource records for telecommunications network inventory management.
- aid: servicenow:servicenow-product-inventory-open-api
  name: ServiceNow Product Inventory Open API
  tags:
  - Inventory
  - Products
  - Telecommunications
  - TMF
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/product-inventory-open-api.html
  baseURL: https://{instance}.service-now.com/api/sn_ind_tmt_orm/productInventoryManagement/v4
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/product-inventory-open-api.html
    type: Documentation
  description: The ServiceNow Product Inventory Open API provides REST endpoints for managing product inventory data based on TM Forum specifications. It supports querying and managing product instances and their lifecycle states for telecommunications product inventory management.
- aid: servicenow:servicenow-service-test-management-open-api
  name: ServiceNow Service Test Management Open API
  tags:
  - Quality
  - Service Testing
  - Telecommunications
  - TMF
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/service-test-management-api.html
  baseURL: https://{instance}.service-now.com/api/sn_ind_tmt_orm/serviceTestManagement/v4
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/service-test-management-api.html
    type: Documentation
  description: The ServiceNow Service Test Management Open API provides REST endpoints for managing service test records based on TM Forum specifications. It supports creating and managing service test definitions and results for telecommunications service quality assurance.
- aid: servicenow:servicenow-project-portfolio-management-api
  name: ServiceNow Project Portfolio Management API
  tags:
  - Governance
  - PPM
  - Project Management
  - Strategic Portfolio Management
  image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
  humanURL: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/ppm-api.html
  baseURL: https://{instance}.service-now.com/api/now/ppm
  properties:
  - url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/ppm-api.html
    type: Documentation
  description: The ServiceNow Project Portfolio Management API provides REST endpoints for managing projects, demands, and resource plans within Strategic Portfolio Management (SPM). It enables external systems to create, retrieve, and update project portfolio data for governance and planning purposes.
name: ServiceNow
tags:
- Automation
- Cloud Services
- Digital Workflows
- Enterprise Platform
- IT Service Management
- ITSM
- Processes
- T1
- Workflow Automation
- Workflows
type: Contract
image: https://www.servicenow.com/content/dam/servicenow-assets/images/meganav/servicenow-logo.svg
access: 3rd-Party
common:
- url: https://www.servicenow.com/
  name: Website
  type: Website
  description: 'null'
- url: https://www.servicenow.com/community/developer-blog/bg-p/developer-blog
  name: Developer blog - ServiceNow Community
  type: Blog
  description: 'null'
- url: https://www.servicenow.com/community/events/ct-p/TopLevel_Events
  name: Events - ServiceNow Community
  type: Events
  description: 'null'
- url: https://www.servicenow.com/community/developer-forum/bd-p/developer-forum
  name: Developer forum - ServiceNow Community
  type: Forums
  description: 'null'
- url: https://www.servicenow.com/docs/
  name: Product Documentation | ServiceNow
  type: Documentation
  description: 'null'
- url: https://www.servicenow.com/terms-of-use.html
  name: Website terms of use - ServiceNow
  type: TermsOfService
  description: 'null'
- url: https://www.servicenow.com/privacy-statement.html
  name: Website and Events Privacy Statement - ServiceNow
  type: PrivacyPolicy
  description: 'null'
created: '2025-01-08'
modified: '2026-04-07'
position: Consuming
description: ServiceNow provides cloud-based platform services that automate enterprise IT operations.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

