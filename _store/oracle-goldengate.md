---
aid: oracle-goldengate
url: https://raw.githubusercontent.com/api-evangelist/oracle-goldengate/refs/heads/main/apis.yml
apis:
- name: Oracle GoldenGate REST API
  description: RESTful API for managing Oracle GoldenGate Microservices Architecture, including deployment configuration, process management, and monitoring.
  image: https://www.oracle.com/a/ocom/img/cb71-oracle-goldengate.jpg
  humanUrl: https://docs.oracle.com/en/middleware/goldengate/core/
  baseUrl: https://<goldengate-host>:<port>/services/v2
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
  - type: Documentation (26ai)
    url: https://docs.oracle.com/en/database/goldengate/core/26/oggra/index.html
  - type: Authentication (26ai)
    url: https://docs.oracle.com/en/database/goldengate/core/26/oggra/authenticate.html
  - type: Getting Started
    url: https://docs.oracle.com/en/database/goldengate/core/26/
  - type: Tutorials
    url: https://docs.oracle.com/en/database/goldengate/core/26/tutorials.html
  - type: Change Log
    url: https://docs.oracle.com/en/database/goldengate/core/26/release-notes/
  contact:
  - type: Support
    url: https://support.oracle.com
- name: Oracle GoldenGate for Big Data REST API
  description: API for managing Oracle GoldenGate for Big Data deployments, allowing integration with Hadoop, Kafka, and other big data targets.
  image: https://www.oracle.com/a/ocom/img/cb71-oracle-goldengate.jpg
  humanUrl: https://docs.oracle.com/en/middleware/goldengate/big-data/
  baseUrl: https://<goldengate-host>:<port>/services/v2
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
  - type: Getting Started
    url: https://docs.oracle.com/en/middleware/goldengate/big-data/21.3/gadbd/getting-started.html
  contact:
  - type: Support
    url: https://support.oracle.com
- name: Oracle GoldenGate Veridata REST API
  description: API for Oracle GoldenGate Veridata to verify and compare data between source and target systems.
  image: https://www.oracle.com/a/ocom/img/cb71-oracle-goldengate.jpg
  humanUrl: https://docs.oracle.com/en/middleware/goldengate/veridata/
  baseUrl: https://<veridata-host>:<port>/veridata/v1
  tags:
  - Comparison
  - Data Quality
  - Data Validation
  - Data Verification
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/middleware/goldengate/veridata/12.2.1.4/gvdug/index.html
  - type: API Reference
    url: https://docs.oracle.com/en/middleware/goldengate/veridata/12.2.1.4/gvdra/index.html
  - type: OpenAPI
    url: openapi/oracle-goldengate-veridata-rest-api-openapi.yml
  - type: Documentation (26c)
    url: https://docs.oracle.com/en/database/goldengate/veridata/26/
  - type: Change Log
    url: https://docs.oracle.com/en/database/goldengate/veridata/26/gvdrn/index.html
  contact:
  - type: Support
    url: https://support.oracle.com
- name: Oracle GoldenGate Cloud Service API
  description: Oracle Cloud Infrastructure API for managing GoldenGate deployments in OCI.
  image: https://www.oracle.com/a/ocom/img/cb71-oracle-goldengate.jpg
  humanUrl: https://docs.oracle.com/en-us/iaas/goldengate/
  baseUrl: https://goldengate.{region}.oci.oraclecloud.com
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
  - type: Getting Started
    url: https://docs.oracle.com/en/cloud/paas/goldengate-service/index.html
  - type: Authentication
    url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm
  - type: Tutorials
    url: https://docs.oracle.com/en/cloud/paas/goldengate-service/tutorials.html
  - type: Change Log
    url: https://docs.oracle.com/en-us/iaas/releasenotes/services/goldengate/
  - type: Terraform
    url: https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/golden_gate_deployment
  - type: Python SDK
    url: https://docs.oracle.com/en-us/iaas/tools/python/latest/api/golden_gate.html
  - type: Using REST API
    url: https://docs.oracle.com/en-us/iaas/goldengate/doc/using-rest-api.html
  contact:
  - type: Support
    url: https://support.oracle.com
- name: Oracle GoldenGate Stream Analytics REST API
  description: REST API for managing Oracle GoldenGate Stream Analytics pipelines, enabling real-time event stream processing, monitoring, and dashboard creation.
  image: https://www.oracle.com/a/ocom/img/cb71-oracle-goldengate.jpg
  humanUrl: https://docs.oracle.com/en/database/goldengate/stream-analytics/index.html
  baseUrl: https://<ggsa-host>:<port>/osa
  tags:
  - Dashboards
  - Event Processing
  - Real-Time Analytics
  - Spark
  - Stream Analytics
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/database/goldengate/stream-analytics/26/
  - type: API Reference
    url: https://docs.oracle.com/en/middleware/fusion-middleware/osa/19.1/ggsa-rest-api/quick-start.html
  - type: OpenAPI
    url: openapi/oracle-goldengate-stream-analytics-rest-api-openapi.yml
  - type: Getting Started
    url: https://docs.oracle.com/en/database/goldengate/stream-analytics/26/
  - type: Change Log
    url: https://docs.oracle.com/en/database/goldengate/stream-analytics/26/release-notes/release-notes-goldengate-stream-analytics.pdf
  contact:
  - type: Support
    url: https://support.oracle.com
- name: Oracle GoldenGate Data Streams REST API
  description: REST API for distributing and managing Oracle GoldenGate data streams, enabling real-time data distribution to downstream consumers.
  image: https://www.oracle.com/a/ocom/img/cb71-oracle-goldengate.jpg
  humanUrl: https://docs.oracle.com/en/database/goldengate/core/26/coredoc/distribute-datastream-rest-api.html
  baseUrl: https://<goldengate-host>:<port>/services/v2
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
  - type: Getting Started
    url: https://docs.oracle.com/en/database/goldengate/core/26/
  contact:
  - type: Support
    url: https://support.oracle.com
name: Oracle GoldenGate
tags:
- CDC
- Data Integration
- Data Synchronization
- Database
- Enterprise
- Real-Time Replication
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Oracle GoldenGate enables real-time data integration and replication in heterogeneous IT environments. These APIs provide programmatic access to manage and monitor GoldenGate deployments, processes, and configurations.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

