---
aid: apache-flink
url: https://raw.githubusercontent.com/api-evangelist/apache-flink/refs/heads/main/apis.yml
apis:
- name: Apache Flink REST API
  description: The REST API provides programmatic access to monitor and control Flink jobs and clusters. It supports job submission, cluster management, and metrics retrieval.
  image: https://flink.apache.org/img/flink-header-logo.svg
  humanURL: https://flink.apache.org/
  baseURL: http://localhost:8081
  tags:
  - Big Data
  - Distributed Computing
  - Real-Time Processing
  - Streaming
  properties:
  - type: Documentation
    url: https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/rest_api/
  - type: OpenAPI
    url: https://nightlies.apache.org/flink/flink-docs-stable/api/openapi/
  - type: Swagger
    url: https://petstore.swagger.io/?url=https://nightlies.apache.org/flink/flink-docs-stable/api/openapi/
  contact:
  - FN: Apache Flink Community
    email: user@flink.apache.org
- name: Apache Flink Monitoring API
  description: Monitoring REST API for accessing job metrics, checkpoints, and cluster statistics.
  image: https://flink.apache.org/img/flink-header-logo.svg
  humanURL: https://flink.apache.org/
  baseURL: http://localhost:8081
  tags:
  - Metrics
  - Monitoring
  - Observability
  properties:
  - type: Documentation
    url: https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/monitoring/
  - type: Metrics
    url: https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/metrics/
name: Apache Flink
tags:
- Apache
- Batch Processing
- Big Data
- Real-Time Analytics
- Stateful Computing
- Stream Processing
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

