---
aid: oracle-goldengate
name: Oracle GoldenGate
description: Oracle GoldenGate enables real-time data integration and replication in heterogeneous IT environments. These APIs provide programmatic access to manage and monitor GoldenGate deployments, processes, and configurations.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/oracle-goldengate/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.19'
apis:
  - name: Oracle GoldenGate REST API
    description: RESTful API for managing Oracle GoldenGate Microservices Architecture, including deployment configuration, process management, and monitoring.
    image: https://www.oracle.com/a/ocom/img/cb71-oracle-goldengate.jpg
    humanURL: https://docs.oracle.com/en/middleware/goldengate/core/
    baseURL: https://<goldengate-host>:<port>/services/v2
    tags:
      - CDC
      - Data Replication
      - ETL
      - Microservices
      - Real-Time Data Integration
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/middleware/goldengate/core/21.3/oggra/index.html
      - type: OpenAPI
        url: openapi/oracle-goldengate-rest-api-openapi.yml
      - type: Authentication
        url: https://docs.oracle.com/en/middleware/goldengate/core/21.3/oggra/authentication.html
      - type: Documentation
        url: https://docs.oracle.com/en/database/goldengate/core/26/oggra/index.html
      - type: Authentication
        url: https://docs.oracle.com/en/database/goldengate/core/26/oggra/authenticate.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/database/goldengate/core/26/
      - type: Tutorials
        url: https://docs.oracle.com/en/database/goldengate/core/26/tutorials.html
      - type: ChangeLog
        url: https://docs.oracle.com/en/database/goldengate/core/26/release-notes/
    contact:
      - type: Support
        url: https://support.oracle.com
  - name: Oracle GoldenGate for Big Data REST API
    description: API for managing Oracle GoldenGate for Big Data deployments, allowing integration with Hadoop, Kafka, and other big data targets.
    image: https://www.oracle.com/a/ocom/img/cb71-oracle-goldengate.jpg
    humanURL: https://docs.oracle.com/en/middleware/goldengate/big-data/
    baseURL: https://<goldengate-host>:<port>/services/v2
    tags:
      - Big Data
      - Hadoop
      - Kafka
      - NoSQL
      - Streaming
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/middleware/goldengate/big-data/21.3/gadbd/index.html
      - type: OpenAPI
        url: openapi/oracle-goldengate-big-data-rest-api-openapi.yml
      - type: GettingStarted
        url: https://docs.oracle.com/en/middleware/goldengate/big-data/21.3/gadbd/getting-started.html
    contact:
      - type: Support
        url: https://support.oracle.com
  - name: Oracle GoldenGate Veridata REST API
    description: API for Oracle GoldenGate Veridata to verify and compare data between source and target systems.
    image: https://www.oracle.com/a/ocom/img/cb71-oracle-goldengate.jpg
    humanURL: https://docs.oracle.com/en/middleware/goldengate/veridata/
    baseURL: https://<veridata-host>:<port>/veridata/v1
    tags:
      - Comparison
      - Data Quality
      - Data Validation
      - Data Verification
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/middleware/goldengate/veridata/12.2.1.4/gvdug/index.html
      - type: APIReference
        url: https://docs.oracle.com/en/middleware/goldengate/veridata/12.2.1.4/gvdra/index.html
      - type: OpenAPI
        url: openapi/oracle-goldengate-veridata-rest-api-openapi.yml
      - type: Documentation
        url: https://docs.oracle.com/en/database/goldengate/veridata/26/
      - type: ChangeLog
        url: https://docs.oracle.com/en/database/goldengate/veridata/26/gvdrn/index.html
    contact:
      - type: Support
        url: https://support.oracle.com
  - name: Oracle GoldenGate Cloud Service API
    description: Oracle Cloud Infrastructure API for managing GoldenGate deployments in OCI.
    image: https://www.oracle.com/a/ocom/img/cb71-oracle-goldengate.jpg
    humanURL: https://docs.oracle.com/en-us/iaas/goldengate/
    baseURL: https://goldengate.{region}.oci.oraclecloud.com
    tags:
      - Cloud
      - Cloud Integration
      - Database Migration
      - OCI
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/api/#/en/goldengate/latest/
      - type: OpenAPI
        url: openapi/oracle-goldengate-cloud-service-api-openapi.yml
      - type: SDK
        url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm
      - type: CLI
        url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/paas/goldengate-service/index.html
      - type: Authentication
        url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm
      - type: Tutorials
        url: https://docs.oracle.com/en/cloud/paas/goldengate-service/tutorials.html
      - type: ChangeLog
        url: https://docs.oracle.com/en-us/iaas/releasenotes/services/goldengate/
      - type: SDK
        url: https://docs.oracle.com/en-us/iaas/tools/python/latest/api/golden_gate.html
      - type: APIReference
        url: https://docs.oracle.com/en-us/iaas/goldengate/doc/using-rest-api.html
    contact:
      - type: Support
        url: https://support.oracle.com
  - name: Oracle GoldenGate Stream Analytics REST API
    description: REST API for managing Oracle GoldenGate Stream Analytics pipelines, enabling real-time event stream processing, monitoring, and dashboard creation.
    image: https://www.oracle.com/a/ocom/img/cb71-oracle-goldengate.jpg
    humanURL: https://docs.oracle.com/en/database/goldengate/stream-analytics/index.html
    baseURL: https://<ggsa-host>:<port>/osa
    tags:
      - Dashboards
      - Event Processing
      - Real-Time Analytics
      - Spark
      - Stream Analytics
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/goldengate/stream-analytics/26/
      - type: APIReference
        url: https://docs.oracle.com/en/middleware/fusion-middleware/osa/19.1/ggsa-rest-api/quick-start.html
      - type: OpenAPI
        url: openapi/oracle-goldengate-stream-analytics-rest-api-openapi.yml
      - type: GettingStarted
        url: https://docs.oracle.com/en/database/goldengate/stream-analytics/26/
      - type: ChangeLog
        url: https://docs.oracle.com/en/database/goldengate/stream-analytics/26/release-notes/release-notes-goldengate-stream-analytics.pdf
    contact:
      - type: Support
        url: https://support.oracle.com
  - name: Oracle GoldenGate Data Streams REST API
    description: REST API for distributing and managing Oracle GoldenGate data streams, enabling real-time data distribution to downstream consumers.
    image: https://www.oracle.com/a/ocom/img/cb71-oracle-goldengate.jpg
    humanURL: https://docs.oracle.com/en/database/goldengate/core/26/coredoc/distribute-datastream-rest-api.html
    baseURL: https://<goldengate-host>:<port>/services/v2
    tags:
      - Data Distribution
      - Data Streams
      - Real-Time
      - Streaming
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/goldengate/core/26/coredoc/distribute-datastream-rest-api.html
      - type: OpenAPI
        url: openapi/oracle-goldengate-data-streams-rest-api-openapi.yml
      - type: GettingStarted
        url: https://docs.oracle.com/en/database/goldengate/core/26/
    contact:
      - type: Support
        url: https://support.oracle.com
common:
  - type: Portal
    url: https://www.oracle.com/integration/goldengate/
  - type: Blog
    url: https://blogs.oracle.com/dataintegration/
  - type: Pricing
    url: https://www.oracle.com/integration/goldengate/pricing/
  - type: GettingStarted
    url: https://docs.oracle.com/en/middleware/goldengate/core/21.3/index.html
  - type: TermsOfService
    url: https://www.oracle.com/legal/terms.html
  - type: PrivacyPolicy
    url: https://www.oracle.com/legal/privacy/
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/paas/goldengate-service/docs.html
  - type: SignUp
    url: https://www.oracle.com/cloud/free/
  - type: Login
    url: https://cloud.oracle.com/
  - type: StatusPage
    url: https://ocistatus.oraclecloud.com/
  - type: Support
    url: https://support.oracle.com
  - type: KnowledgeCenter
    url: https://www.oracle.com/integration/goldengate/knowledge-hub/
  - type: GitHubOrganization
    url: https://github.com/oracle
  - type: GitHubRepository
    url: https://github.com/oracle/docker-images/tree/main/OracleGoldenGate
  - type: Features
    url: https://www.oracle.com/integration/goldengate/features/
    data:
      - Real-time data replication across heterogeneous databases
      - Change data capture (CDC) with minimal impact on source systems
      - Zero-downtime migration and database upgrades
      - Multi-cloud and hybrid cloud data integration
      - Bidirectional replication for active-active architectures
      - Stream analytics for real-time event processing
      - Data verification and repair with Veridata
      - Big data target support including Kafka, HDFS, and MongoDB
  - type: UseCases
    url: https://www.oracle.com/integration/goldengate/
    data:
      - Real-time data warehouse loading and synchronization
      - Database migration with zero downtime
      - Active-active database replication for high availability
      - Streaming data to big data platforms (Kafka, Hadoop, Elasticsearch)
      - Cloud migration from on-premises Oracle databases to OCI
      - Data verification and compliance auditing
      - Real-time analytics pipeline construction
  - type: Integrations
    url: https://www.oracle.com/integration/goldengate/
    data:
      - Oracle Database
      - MySQL
      - PostgreSQL
      - SQL Server
      - MongoDB
      - Apache Kafka
      - Apache Hadoop / HDFS
      - Elasticsearch
      - Google BigQuery
      - Amazon Kinesis
      - Snowflake
      - Oracle Cloud Infrastructure
  - type: Training
    url: https://education.oracle.com/data-integration/goldengate/product_148
  - type: Tutorials
    url: https://docs.oracle.com/en/cloud/paas/goldengate-service/tutorials.html
  - type: ReleaseNotes
    url: https://docs.oracle.com/en/database/goldengate/core/26/release-notes/
  - type: JSONSchema
    url: json-schema/oracle-goldengate-deployment-schema.json
  - type: JSONLD
    url: json-ld/oracle-goldengate-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - CDC
  - Data Integration
  - Data Synchronization
  - Database
  - Enterprise
  - Real-Time Replication
---
