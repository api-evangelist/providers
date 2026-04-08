---
aid: sap-hana
url: https://raw.githubusercontent.com/api-evangelist/sap-hana/refs/heads/main/apis.yml
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
  - type: OpenAPI
    url: https://api.sap.com/api/hana_cloud_admin/overview
  - type: JSONSchema
    url: json-schema/sap-hana-database-schema.json
  - type: JSONLD
    url: json-ld/sap-hana-context.jsonld
  - type: Authentication
    url: https://help.sap.com/docs/HANA_CLOUD/9ae9104a46f74a6583ce5182e7fb20cb/3670474a58c24ac2b082e76cbbd9dc19.html
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPHanaCloud/rest
  - type: Tutorials
    url: https://developers.sap.com/tutorials/hana-cloud-automation-rest..html
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
  - type: SQL Reference
    url: https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/20a61f5075191014b3c5a0b9b37e5ce1.html
  - type: JDBC Driver
    url: https://help.sap.com/docs/SAP_HANA_CLIENT/f1b440ded6144a54ada97ff95dac7adf/
  - type: ODBC Driver
    url: https://developers.sap.com/tutorials/hana-clients-odbc..html
  - type: JDBC Connection Guide
    url: https://help.sap.com/docs/SAP_HANA_CLIENT/f1b440ded6144a54ada97ff95dac7adf/ff15928cf5594d78b841fbbe649f04b4.html
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
  - type: JavaScript API
    url: https://help.sap.com/docs/SAP_HANA_PLATFORM/4505d0bdaf4948449b7f7379d24d0f0d/2a2d5865bc97443fbc4436c85d5d694b.html
  - type: OData Services
    url: https://help.sap.com/docs/SAP_HANA_PLATFORM/4505d0bdaf4948449b7f7379d24d0f0d/5b5c3a8b67924c43a92e35e38c55daa5.html
  - type: XS Advanced Developer Guide
    url: https://help.sap.com/docs/SAP_HANA_PLATFORM/d89d4595fae647eabc14002c0340a999/1639bb4a23814bc4945f46ca3af1a781.html
  - type: XS Classic JavaScript Reference
    url: https://help.sap.com/doc/3de842783af24336b6305a3c0223a369/2.0.03/en-US/$.html
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
  - type: REST API
    url: https://help.sap.com/docs/SAP_HANA_COCKPIT/afa922439b204e9caf22c78b6b69e4f2/461114e1a8ab4bb085fef7c83f797e52.html
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
  - type: Adapters
    url: https://help.sap.com/docs/SAP_HANA_SMART_DATA_INTEGRATION/7952ef28a6914997abc01745fef1b607/935315b2d6ae4970836a93bb06e93799.html
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
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPHanaCloud/rest
  - type: Alert Management Guide
    url: https://developers.sap.com/group.hana-cloud-alerts-metrics.html
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
  - type: SAP Business Accelerator Hub
    url: https://api.sap.com/package/SAPHANASpatialServices/overview
  - type: Tutorials
    url: https://developers.sap.com/tutorials/hana-spatial-services-apis..html
  - type: SAP Discovery Center
    url: https://discovery-center.cloud.sap/serviceCatalog/sap-hana-spatial-services
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
  - type: REST API Reference
    url: https://help.sap.com/doc/9d084a41830f46d6904fd4c23cd4bbfa/QRC_3_2021/en-US/html/index.html
  - type: Tutorials
    url: https://developers.sap.com/tutorials/data-lake-file-containers-restapi..html
  - type: Node.js Tutorial
    url: https://developers.sap.com/tutorials/data-lake-file-containers-restapi-node..html
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
  - type: HDI Container Setup Guide
    url: https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-deployment-infrastructure-hdi-reference/set-up-sap-hdi-container-with-hdi-api
  - type: HDI Containers
    url: https://help.sap.com/docs/SAP_HANA_PLATFORM/4505d0bdaf4948449b7f7379d24d0f0d/e28abca91a004683845805efc2bf967c.html
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
  - type: PAL Reference
    url: https://help.sap.com/doc/86fb8d26952748debc8d08db756e6c1f/2.0.07/en-US/SAP_HANA_Predictive_Analysis_Library_PAL_en.pdf
  - type: Python Client API
    url: https://help.sap.com/doc/1d0ebfe5e8dd44d09606814d83308d4b/2.0.07/en-US/hana_ml.html
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
  - type: Introduction
    url: https://help.sap.com/docs/SAP_HANA_PLATFORM/3e48dd3ad36e41efbdf534a89fdf278f/b4518419653e44daad99c285039b29c5.html
  - type: Tutorials
    url: https://developers.sap.com/tutorials/hana-dbx-multi-model..html
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
  - type: Knowledge Graph Guide
    url: https://help.sap.com/docs/hana-cloud-database/sap-hana-cloud-sap-hana-database-knowledge-graph-guide/sap-hana-knowledge-graph-inside-sap-hana-cloud-database
  - type: Tutorials
    url: https://developers.sap.com/group.hana-aa-graph-overview.html
  - type: Graph Samples
    url: https://github.com/SAP-samples/hana-graph-examples
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
  - type: REST API Reference
    url: https://help.sap.com/doc/f32a797a5ec94d8ba4d7ed240d95bfae/2.0.04/en-US/index.html
  - type: Info API
    url: https://help.sap.com/docs/SAP_HANA_PLATFORM/b3d0daf2a98e49ada00bf31b7ca7a42e/d6b92411a7604cb59f90ded3169c2071.html
name: SAP HANA
tags:
- Analytics
- Cloud
- Database
- Enterprise
- In-Memory
type: Contract
image: https://www.sap.com/content/dam/application/shared/logos/sap-logo-svg.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for SAP HANA, an in-memory, column-oriented, relational database management system developed and marketed by SAP SE.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

