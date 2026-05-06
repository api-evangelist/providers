---
aid: flink
name: Apache Flink
description: Apache Flink is an open-source framework and distributed processing engine for stateful computations over unbounded and bounded data streams. It is designed to run in all common cluster environments and to perform computations at in-memory speed and at any scale. Flink exposes a REST API on the JobManager Dispatcher that allows external systems to query cluster status, submit and manage jobs, trigger savepoints and checkpoints, upload and run JARs, and inspect metrics, accumulators, and exception histories. The same REST endpoints power the Flink Web UI.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/flink/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Big Data
  - Distributed Computing
  - Real-Time Analytics
  - Stream Processing
  - Workflows
apis:
  - aid: flink:rest-api
    name: Apache Flink REST API
    description: The Flink REST API is exposed by the JobManager Dispatcher and provides monitoring and management capabilities for a Flink cluster. It covers cluster configuration, JobManager environment and metrics, job lifecycle (submit, list, cancel, stop), checkpoint and savepoint management, JAR upload and execution, dataset operations, and TaskManager inspection. The same REST API powers the Flink Web UI and is the primary programmatic interface for operating a Flink cluster.
    humanURL: https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/rest_api/
    baseURL: http://localhost:8081
    tags:
      - Stream Processing
      - Job Management
      - Cluster Management
      - Checkpoints
      - Monitoring
    properties:
      - url: https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/rest_api/
        type: Documentation
      - url: https://flink.apache.org/
        type: Website
      - url: https://github.com/apache/flink
        type: GitHubRepository
      - url: openapi/flink-rest-api-openapi-original.yml
        type: OpenAPI
common:
  - type: Website
    url: https://flink.apache.org/
  - type: Documentation
    url: https://nightlies.apache.org/flink/flink-docs-stable/
  - type: RESTAPIDocumentation
    url: https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/rest_api/
  - type: GitHubRepository
    url: https://github.com/apache/flink
  - type: Blog
    url: https://flink.apache.org/posts/
  - type: Community
    url: https://flink.apache.org/community/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
