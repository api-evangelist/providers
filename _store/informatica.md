---
aid: informatica
name: Informatica
segments:
  - iPaaS
description: Collection of APIs for Informatica Intelligent Cloud Services (IICS) and Intelligent Data Management Cloud (IDMC), providing programmatic access to data integration, data governance, data quality, master data management, B2B gateway, and platform administration capabilities.
type: Index
position: Consumer
access: 3rd-Party
image: https://companieslogo.com/img/orig/INFA-3e1d4e5a.png
tags:
  - Address Verification
  - B2B Gateway
  - Cloud Services
  - Data Governance
  - Data Integration
  - Data Profiling
  - Data Quality
  - Enterprise Software
  - ETL
  - IDMC
  - IICS
  - Master Data Management
  - Reference Data Management
created: '2025-01-08'
modified: '2026-04-18'
url: https://raw.githubusercontent.com/api-evangelist/informatica/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: informatica:informatica
    name: Informatica Platform REST API
    description: The Informatica Intelligent Cloud Services Platform REST API provides access to platform-level resources including login and authentication, roles and privileges, user and user group management, organizations, connections, schedules, runtime environments, Secure Agent services, object permissions, export and import, source control, projects and folders, licenses, metering data, and security logs. Supports version 2 (JSON and XML) and version 3 (JSON) resource formats.
    humanURL: https://docs.informatica.com/integration-cloud/cloud-platform/current-version/rest-api-reference/informatica-intelligent-cloud-services-rest-api.html
    tags:
      - Authentication
      - Platform
      - Roles
      - Users
    properties:
      - type: Documentation
        url: https://docs.informatica.com/integration-cloud/cloud-platform/current-version/rest-api-reference/informatica-intelligent-cloud-services-rest-api.html
      - type: Documentation
        url: https://docs.informatica.com/integration-cloud/b2b-gateway/current-version/rest-api-reference/platform-rest-api-version-3-resources.html
        title: Platform REST API v3
      - type: Documentation
        url: https://docs.informatica.com/integration-cloud/b2b-gateway/current-version/rest-api-reference/platform-rest-api-version-3-resources/roles.html
        title: Roles API
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/informatica/refs/heads/main/openapi/informatica-platform-rest-api-openapi.yml
      - type: OpenAPI
        url: openapi/informatica-platform-rest-api-openapi.yml
      - type: JSONSchema
        url: json-schema/informatica-connection-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-login-request-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-login-response-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-connection-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-connection-create-request-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-connection-update-request-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-mapping-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-mapping-parameter-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-mapping-in-out-parameter-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-mapping-task-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-mapping-task-create-request-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-mapping-task-update-request-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-job-start-request-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-job-start-response-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-job-stop-request-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-activity-log-entry-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-schedule-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-schedule-create-request-schema.json
      - type: JSONSchema
        url: json-schema/informatica-platform-rest-error-response-schema.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-login-request-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-login-response-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-connection-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-connection-create-request-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-connection-update-request-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-mapping-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-mapping-parameter-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-mapping-in-out-parameter-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-mapping-task-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-mapping-task-create-request-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-mapping-task-update-request-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-job-start-request-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-job-start-response-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-job-stop-request-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-activity-log-entry-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-schedule-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-schedule-create-request-structure.json
      - type: JSONStructure
        url: json-structure/informatica-platform-rest-error-response-structure.json
      - type: Example
        url: examples/informatica-platform-rest-login-request-example.json
      - type: Example
        url: examples/informatica-platform-rest-login-response-example.json
      - type: Example
        url: examples/informatica-platform-rest-connection-example.json
      - type: Example
        url: examples/informatica-platform-rest-connection-create-request-example.json
      - type: Example
        url: examples/informatica-platform-rest-connection-update-request-example.json
      - type: Example
        url: examples/informatica-platform-rest-mapping-example.json
      - type: Example
        url: examples/informatica-platform-rest-mapping-parameter-example.json
      - type: Example
        url: examples/informatica-platform-rest-mapping-in-out-parameter-example.json
      - type: Example
        url: examples/informatica-platform-rest-mapping-task-example.json
      - type: Example
        url: examples/informatica-platform-rest-mapping-task-create-request-example.json
      - type: Example
        url: examples/informatica-platform-rest-mapping-task-update-request-example.json
      - type: Example
        url: examples/informatica-platform-rest-job-start-request-example.json
      - type: Example
        url: examples/informatica-platform-rest-job-start-response-example.json
      - type: Example
        url: examples/informatica-platform-rest-job-stop-request-example.json
      - type: Example
        url: examples/informatica-platform-rest-activity-log-entry-example.json
      - type: Example
        url: examples/informatica-platform-rest-schedule-example.json
      - type: Example
        url: examples/informatica-platform-rest-schedule-create-request-example.json
      - type: Example
        url: examples/informatica-platform-rest-error-response-example.json
      - type: JSONLD
        url: json-ld/informatica-context.jsonld
      - type: JSONLD
        url: json-ld/informatica-platform-rest-context.jsonld
  - aid: informatica:data-integration-rest-api
    name: Informatica Data Integration REST API
    description: The Data Integration REST API provides programmatic access to manage data integration assets and operations, including connections, mappings, mapping tasks, dynamic mapping tasks, taskflows, code tasks, connectors, data preview, fields, file listeners, file transfer, and hierarchical mappers. Uses version 2 resources with JSON or XML format.
    humanURL: https://docs.informatica.com/integration-cloud/data-integration/current-version/rest-api-reference/data-integration-rest-api.html
    tags:
      - Connections
      - Data Integration
      - ETL
      - Mappings
    properties:
      - type: Documentation
        url: https://docs.informatica.com/integration-cloud/data-integration/current-version/rest-api-reference/data-integration-rest-api.html
      - type: APIReference
        url: https://docs.informatica.com/integration-cloud/data-integration/current-version/rest-api-reference/rest-api-resource-quick-references/data-integration-resource-quick-reference.html
  - aid: informatica:cloud-data-governance-and-catalog-api
    name: Informatica Cloud Data Governance and Catalog API
    description: The Cloud Data Governance and Catalog API enables programmatic creation and management of assets, searching for assets, and viewing asset details within Informatica Data Governance and Catalog. Calls can be made using a REST client, the cURL tool, or a suitable programming interface.
    humanURL: https://docs.informatica.com/data-quality-cloud/cloud-data-governance-and-catalog/current-version.html
    tags:
      - Data Catalog
      - Data Governance
    properties:
      - type: Documentation
        url: https://docs.informatica.com/data-quality-cloud/cloud-data-governance-and-catalog/current-version.html
  - aid: informatica:cloud-data-profiling-rest-api
    name: Informatica Cloud Data Profiling REST API
    description: The Cloud Data Profiling REST API allows interaction with the Data Profiling Service through API calls to create, delete, update, and run queries and profiles within your organization. Supports platform REST API version 2 and version 3 resources and service-specific resources.
    humanURL: https://docs.informatica.com/data-governance-and-quality-cloud/cloud-data-profiling/current-version/data-profiling/data-profiling/data-profiling-rest-api.html
    tags:
      - Data Profiling
      - Data Quality
    properties:
      - type: Documentation
        url: https://docs.informatica.com/data-governance-and-quality-cloud/cloud-data-profiling/current-version/data-profiling/data-profiling/data-profiling-rest-api.html
      - type: GettingStarted
        url: https://docs.informatica.com/data-governance-and-quality-cloud/cloud-data-profiling/h2l/1547-getting-started-with-cloud-data-profiling-rest-api/getting-started-with-cloud-data-profiling-rest-api/overview.html
  - aid: informatica:cloud-address-verification-api
    name: Informatica Cloud Address Verification API
    description: The Cloud Address Verification API is a REST API-based solution for verifying and validating postal addresses in real time. You can integrate the Address Verification service API endpoints into your application using a REST client, the cURL tool, or any suitable programming interface.
    humanURL: https://docs.informatica.com/data-governance-and-quality-cloud/data-quality/current-version/cloud-address-verification-api/introduction.html
    tags:
      - Address Verification
      - Data Quality
    properties:
      - type: Documentation
        url: https://docs.informatica.com/data-governance-and-quality-cloud/data-quality/current-version/cloud-address-verification-api/introduction.html
  - aid: informatica:b2b-gateway-rest-api
    name: Informatica B2B Gateway REST API
    description: The B2B Gateway REST APIs enable running inbound and outbound partner flows, querying the status of events, and getting control numbers for outbound EDI X12 and EDIFACT messages through programmatic API calls.
    humanURL: https://docs.informatica.com/ipaas/b2b-gateway/current-version/rest-api-reference/informatica-intelligent-cloud-services-rest-api.html
    tags:
      - B2B
      - EDI
      - Gateway
    properties:
      - type: Documentation
        url: https://docs.informatica.com/ipaas/b2b-gateway/current-version/rest-api-reference/informatica-intelligent-cloud-services-rest-api.html
  - aid: informatica:reference-360-rest-api
    name: Informatica Reference 360 REST API
    description: The Reference 360 REST API enables programmatic management of reference data, including exporting and importing reference data sets, managing code values and value mappings, retrieving asset details, managing code lists, crosswalks, hierarchies, and audit trails. Supports multiple API versions for model import and export operations.
    humanURL: https://docs.informatica.com/master-data-management-cloud/reference-360/current-version/reference-360/reference-360-rest-api.html
    tags:
      - Master Data Management
      - Reference Data
    properties:
      - type: Documentation
        url: https://docs.informatica.com/master-data-management-cloud/reference-360/current-version/reference-360/reference-360-rest-api.html
common:
  - type: Portal
    url: https://developer.informatica.com/
  - type: Documentation
    url: https://docs.informatica.com/
  - type: KnowledgeCenter
    url: https://knowledge.informatica.com/
  - type: Support
    url: https://www.informatica.com/support.html
  - type: Support
    url: https://network.informatica.com/
    title: Community
  - type: Login
    url: https://dm-us.informaticacloud.com/identity-service/home
  - type: SpectralRules
    url: rules/informatica-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/informatica-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/platform-rest-api.yaml
    title: Platform REST API Shared Definition
  - type: NaftikoCapability
    url: capabilities/data-integration.yaml
    title: Data Integration Workflow
  - type: Features
    data:
      - name: Data Integration
        description: Connect, transform, and move data across cloud and on-premises environments using visual mapping interfaces.
      - name: Data Governance
        description: Discover, catalog, and govern data assets with automated classification and lineage tracking.
      - name: Data Quality
        description: Profile, cleanse, standardize, and validate data to ensure accuracy and consistency.
      - name: Master Data Management
        description: Create and manage golden records for critical business entities across the enterprise.
      - name: Address Verification
        description: Validate and standardize postal addresses globally in real time.
      - name: B2B Gateway
        description: Exchange EDI documents with trading partners using X12, EDIFACT, and other B2B protocols.
      - name: Reference Data Management
        description: Manage code lists, crosswalks, and hierarchies for standardized reference data across systems.
      - name: API and Application Integration
        description: Build and manage API-led integrations connecting SaaS, cloud, and on-premises applications.
  - type: UseCases
    data:
      - name: Cloud Data Warehouse Loading
        description: Extract data from multiple sources and load into cloud data warehouses like Snowflake, Redshift, or BigQuery.
      - name: Real-Time Data Synchronization
        description: Synchronize data across CRM, ERP, and marketing platforms in real time using change data capture.
      - name: Data Migration
        description: Migrate data between legacy systems and modern cloud platforms with automated mapping and transformation.
      - name: Regulatory Compliance
        description: Ensure data quality and governance standards to meet GDPR, CCPA, and industry-specific regulations.
      - name: Customer 360
        description: Create unified customer profiles by integrating and matching data from multiple source systems.
  - type: Integrations
    data:
      - name: Salesforce
        description: Native connectors for bidirectional data integration with Salesforce CRM and platform.
      - name: SAP
        description: Pre-built connectors for SAP ERP, S/4HANA, and SAP BW data integration.
      - name: Snowflake
        description: Optimized connectors for loading, transforming, and managing data in Snowflake.
      - name: Amazon Web Services
        description: Native connectors for S3, Redshift, DynamoDB, and other AWS data services.
      - name: Microsoft Azure
        description: Connectors for Azure SQL, Blob Storage, Synapse Analytics, and other Azure services.
      - name: Google Cloud Platform
        description: Connectors for BigQuery, Cloud Storage, and other GCP data services.
      - name: Workday
        description: Pre-built connectors for Workday HCM and financial data integration.
      - name: ServiceNow
        description: Connectors for ServiceNow ITSM and platform data integration.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
