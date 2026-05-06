---
name: SAP HANA
description: APIs for SAP HANA, an in-memory, column-oriented, relational database management system developed and marketed by SAP SE.
image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
tags:
  - Analytics
  - Cloud
  - Database
  - Enterprise
  - In-Memory
created: '2024-01-01'
modified: '2026-04-18'
url: https://www.sap.com/products/technology-platform/hana.html
specificationVersion: '0.19'
type: Index
access: 3rd-Party
position: Consumer
apis:
  - name: SAP HANA Cloud REST API
    description: REST API for managing SAP HANA Cloud instances, monitoring, and administration.
    image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
    humanURL: https://help.sap.com/docs/HANA_CLOUD
    baseURL: https://api.cf.{region}.hana.ondemand.com
    tags:
      - Administration
      - Cloud
      - Database Management
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/HANA_CLOUD/9ae9104a46f74a6583ce5182e7fb20cb/
      - type: OpenAPI
        url: openapi/sap-hana-cloud-rest-api.yml
      - type: Authentication
        url: https://help.sap.com/docs/HANA_CLOUD/9ae9104a46f74a6583ce5182e7fb20cb/3670474a58c24ac2b082e76cbbd9dc19.html
      - type: Tutorials
        url: https://developers.sap.com/tutorials/hana-cloud-automation-rest..html
      - type: JSONSchema
        url: json-schema/sap-hana-database-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-service-instance-list-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-service-instance-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-instance-parameters-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-last-operation-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-create-service-instance-request-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-update-service-instance-request-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-inventory-instance-list-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-inventory-instance-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-alert-event-list-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-alert-event-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-alert-rule-list-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-alert-rule-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-update-alert-rules-request-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-metric-value-list-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-metric-series-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-metric-data-point-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-metering-value-list-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-metering-value-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-instance-mapping-list-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-instance-mapping-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-create-instance-mapping-request-schema.json
      - type: JSONSchema
        url: json-schema/sap-hana-cloud-rest-error-schema.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-service-instance-list-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-service-instance-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-instance-parameters-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-last-operation-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-create-service-instance-request-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-update-service-instance-request-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-inventory-instance-list-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-inventory-instance-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-alert-event-list-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-alert-event-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-alert-rule-list-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-alert-rule-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-update-alert-rules-request-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-metric-value-list-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-metric-series-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-metric-data-point-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-metering-value-list-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-metering-value-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-instance-mapping-list-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-instance-mapping-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-create-instance-mapping-request-structure.json
      - type: JSONStructure
        url: json-structure/sap-hana-cloud-rest-error-structure.json
      - type: Example
        url: examples/sap-hana-cloud-rest-service-instance-list-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-service-instance-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-instance-parameters-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-last-operation-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-create-service-instance-request-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-update-service-instance-request-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-inventory-instance-list-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-inventory-instance-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-alert-event-list-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-alert-event-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-alert-rule-list-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-alert-rule-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-update-alert-rules-request-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-metric-value-list-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-metric-series-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-metric-data-point-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-metering-value-list-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-metering-value-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-instance-mapping-list-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-instance-mapping-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-create-instance-mapping-request-example.json
      - type: Example
        url: examples/sap-hana-cloud-rest-error-example.json
      - type: JSONLD
        url: json-ld/sap-hana-cloud-rest-context.jsonld
  - name: SAP HANA SQL API
    description: SQL interface for querying and managing data in SAP HANA databases.
    image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
    humanURL: https://help.sap.com/docs/SAP_HANA_PLATFORM
    baseURL: jdbc:sap://{host}:{port}
    tags:
      - Database
      - Query
      - SQL
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/
  - name: SAP HANA XS Engine API
    description: Extended Application Services (XS) for building applications directly on SAP HANA.
    image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
    humanURL: https://help.sap.com/docs/SAP_HANA_PLATFORM
    baseURL: https://{host}:{port}
    tags:
      - Application Development
      - JavaScript
      - OData
      - XS
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_HANA_PLATFORM/4505d0bdaf4948449b7f7379d24d0f0d/
  - name: SAP HANA Cockpit API
    description: RESTful API for SAP HANA Cockpit administration and monitoring.
    image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
    humanURL: https://help.sap.com/docs/SAP_HANA_COCKPIT
    baseURL: https://{host}:{port}/sap/hana/
    tags:
      - Administration
      - Management
      - Monitoring
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_HANA_COCKPIT/afa922439b204e9caf22c78b6b69e4f2/
  - name: SAP HANA Smart Data Integration API
    description: APIs for data provisioning, replication, and integration.
    image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
    humanURL: https://help.sap.com/docs/SAP_HANA_SMART_DATA_INTEGRATION
    baseURL: https://{host}:{port}
    tags:
      - Data Integration
      - ETL
      - Replication
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_HANA_SMART_DATA_INTEGRATION/7952ef28a6914997abc01745fef1b607/
  - name: SAP HANA Cloud Alerts and Metrics REST API
    description: REST API for accessing triggered alerts, database metrics, and metering data for SAP HANA Cloud instances.
    image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
    humanURL: https://developers.sap.com/tutorials/hana-cloud-alerts-rest-api.html
    baseURL: https://api.cf.{region}.hana.ondemand.com
    tags:
      - Alerts
      - Metering
      - Metrics
      - Monitoring
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/r/64f7d2b06c6b40a9b3097860c5930641/Cloud/en-US/9f02513389e64490a0652955fedce2ad.html
      - type: Tutorials
        url: https://developers.sap.com/tutorials/hana-cloud-alerts-rest-api.html
  - name: SAP HANA Spatial Services API
    description: REST API providing geocoding, routing, and mapping services through a unified interface supporting multiple back-end service providers.
    image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
    humanURL: https://help.sap.com/docs/sap-hana-spatial-services
    baseURL: https://api.cf.{region}.hana.ondemand.com
    tags:
      - Geocoding
      - Location
      - Mapping
      - Routing
      - Spatial
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/sap-hana-spatial-services
      - type: Tutorials
        url: https://developers.sap.com/tutorials/hana-spatial-services-apis..html
  - name: SAP HANA Cloud Data Lake Files REST API
    description: REST API for managing, uploading, reading, deleting, and listing files in SAP HANA Cloud Data Lake file containers.
    image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
    humanURL: https://help.sap.com/docs/hana-cloud-data-lake
    baseURL: https://{host}:{port}
    tags:
      - Cloud Storage
      - Data Lake
      - File Storage
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/hana-cloud-data-lake
      - type: Tutorials
        url: https://developers.sap.com/tutorials/data-lake-file-containers-restapi..html
  - name: SAP HANA Deployment Infrastructure (HDI) API
    description: API for managing HDI containers used to deploy database artifacts in isolated schemas with dependency management and lifecycle support.
    image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
    humanURL: https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-deployment-infrastructure-hdi-reference/sap-hana-cloud-sap-hana-database-deployment-infrastructure-reference
    baseURL: https://{host}:{port}
    tags:
      - Containers
      - Deployment
      - DevOps
      - HDI
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-deployment-infrastructure-hdi-reference/sap-hana-cloud-sap-hana-database-deployment-infrastructure-reference
  - name: SAP HANA Predictive Analysis Library (PAL) API
    description: In-database machine learning and statistical algorithms library providing clustering, classification, regression, and time series analysis capabilities.
    image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
    humanURL: https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-predictive-analysis-library/sap-hana-cloud-sap-hana-database-predictive-analysis-library-pal
    baseURL: https://{host}:{port}
    tags:
      - AI
      - Machine Learning
      - Predictive Analytics
      - Statistics
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-predictive-analysis-library/sap-hana-cloud-sap-hana-database-predictive-analysis-library-pal
  - name: SAP HANA JSON Document Store API
    description: API for storing, querying, and managing semi-structured JSON documents within SAP HANA using a hybrid relational and document-oriented approach.
    image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
    humanURL: https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/5e783b7f5a9749bcbfffe167524aeccc.html
    baseURL: https://{host}:{port}
    tags:
      - Document Store
      - JSON
      - Multi-Model
      - NoSQL
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/5e783b7f5a9749bcbfffe167524aeccc.html
  - name: SAP HANA Graph Engine API
    description: Graph processing engine for network analysis with built-in algorithms for path finding, pattern matching, and knowledge graph capabilities using OpenCypher and SPARQL.
    image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
    humanURL: https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-knowledge-graph-guide/sap-hana-cloud-sap-hana-database-knowledge-graph-engine-guide
    baseURL: https://{host}:{port}
    tags:
      - Graph
      - Knowledge Graph
      - Multi-Model
      - Network Analysis
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-knowledge-graph-guide/sap-hana-cloud-sap-hana-database-knowledge-graph-engine-guide
  - name: SAP HANA REST Info API
    description: REST API for retrieving system information and metadata about SAP HANA Platform instances.
    image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
    humanURL: https://help.sap.com/docs/SAP_HANA_PLATFORM/b3d0daf2a98e49ada00bf31b7ca7a42e/0e5335b66a9e4c64993605fc24ccd6d1.html
    baseURL: https://{host}:{port}
    tags:
      - Metadata
      - REST
      - System Information
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_HANA_PLATFORM/b3d0daf2a98e49ada00bf31b7ca7a42e/0e5335b66a9e4c64993605fc24ccd6d1.html
common:
  - type: DeveloperPortal
    url: https://api.sap.com/
  - type: Support
    url: https://support.sap.com/
  - type: Pricing
    url: https://www.sap.com/products/technology-platform/hana/pricing.html
  - type: StatusPage
    url: https://www.sap.com/about/trust-center/cloud-service-status.html
  - type: TermsOfService
    url: https://www.sap.com/about/trust-center/agreements.html
  - type: GettingStarted
    url: https://www.sap.com/products/data-cloud/hana/get-started.html
  - type: Tutorials
    url: https://developers.sap.com/tutorial-navigator.html
  - type: GitHubRepository
    url: https://github.com/SAP-samples
  - type: PrivacyPolicy
    url: https://www.sap.com/about/legal/privacy.html
  - type: JSONLD
    url: json-ld/sap-hana-context.jsonld
  - type: SpectralRules
    url: rules/sap-hana-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/cloud-administration.yaml
  - type: Features
    data:
      - name: In-Memory Computing
        description: Process massive datasets in real-time using columnar in-memory storage for analytics and transactions.
      - name: Multi-Model Processing
        description: Support for relational, graph, spatial, JSON document, and time series data in a single database.
      - name: Cloud Native
        description: Fully managed cloud database service with elastic scaling, automated backups, and multi-region deployment.
      - name: Predictive Analytics
        description: Built-in machine learning algorithms through the Predictive Analysis Library for in-database analytics.
      - name: Data Lake Integration
        description: Seamlessly extend storage with SAP HANA Cloud Data Lake for cost-effective warm and cold data management.
      - name: Smart Data Integration
        description: Real-time and batch data replication from heterogeneous sources with built-in data quality.
  - type: UseCases
    data:
      - name: Real-Time Analytics
        description: Run complex analytical queries on live transactional data without ETL delays.
      - name: Application Development
        description: Build high-performance applications directly on the database using XS Engine and HDI containers.
      - name: IoT Data Processing
        description: Ingest and analyze high-volume sensor and device data with time series and spatial capabilities.
      - name: Enterprise Data Warehousing
        description: Consolidate enterprise data for reporting and business intelligence with columnar compression.
  - type: Integrations
    data:
      - name: SAP BTP
        description: Native integration with SAP Business Technology Platform for enterprise application development.
      - name: SAP S/4HANA
        description: Serve as the underlying database for SAP S/4HANA ERP suite.
      - name: SAP Analytics Cloud
        description: Direct live connections for real-time business intelligence dashboards and planning.
      - name: Microsoft Azure
        description: Deploy SAP HANA Cloud instances on Azure infrastructure with cross-cloud governance.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
