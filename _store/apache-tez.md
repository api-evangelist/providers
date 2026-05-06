---
aid: apache-tez
name: Apache Tez
description: Apache Tez is an application framework that allows for complex directed-acyclic-graph (DAG) based processing of data built on Apache Hadoop YARN. It is designed as a successor to MapReduce for executing Hive and Pig queries, providing a flexible API for creating DAG execution pipelines, in-memory data passing between tasks, and session reuse for reduced startup latency. Apache Tez is an Apache Software Foundation top-level project.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Big Data
  - DAG
  - Execution Engine
  - Hadoop
  - YARN
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-tez/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-tez:apache-tez-dag-api
    name: Apache Tez DAG API
    description: The Tez DAG API provides a Java programming model for defining and submitting directed-acyclic-graph (DAG) computation jobs to Apache YARN. It allows building DAGs composed of Vertex (processing units), Edge (data connections between vertices), and Processor implementations. The API supports data source/sink definitions, vertex grouping, fault tolerance configuration, and monitoring via the Tez UI and REST API.
    humanURL: https://tez.apache.org/developer-docs.html
    tags:
      - Java
      - DAG
      - YARN
      - Hadoop
    properties:
      - type: Documentation
        url: https://tez.apache.org/developer-docs.html
      - type: APIReference
        url: https://tez.apache.org/javadocs/
      - type: SDK
        url: https://search.maven.org/search?q=org.apache.tez
        title: Maven Java SDK
  - aid: apache-tez:apache-tez-ui-rest-api
    name: Apache Tez UI REST API
    description: The Tez UI and YARN Application History Server expose REST endpoints for monitoring Tez application history, DAG details, vertex and task statistics. The Tez Timeline Server integration provides historical data for DAGs, vertices, tasks, and task attempts with detailed resource usage and timing information.
    humanURL: https://tez.apache.org/tez-ui.html
    tags:
      - REST
      - Monitoring
      - YARN
      - History
    properties:
      - type: Documentation
        url: https://tez.apache.org/tez-ui.html
common:
  - type: GitHubRepository
    url: https://github.com/apache/tez
  - type: Documentation
    url: https://tez.apache.org/
  - type: Portal
    url: https://tez.apache.org/
  - type: ReleaseNotes
    url: https://github.com/apache/tez/releases
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: Features
    data:
      - name: DAG-Based Execution
        description: Flexible DAG computation model replacing MapReduce for complex multi-stage pipelines.
      - name: In-Memory Data Passing
        description: Direct in-memory data transfer between connected vertices eliminating HDFS I/O.
      - name: Session Reuse
        description: Tez sessions reuse container allocations across DAG submissions for reduced latency.
      - name: Dynamic Optimization
        description: Runtime DAG modification based on actual data statistics during execution.
      - name: YARN Integration
        description: Native YARN resource management with fine-grained resource requests per vertex.
  - type: UseCases
    data:
      - name: Apache Hive Query Execution
        description: Tez is the default execution engine for Apache Hive queries replacing MapReduce.
      - name: Apache Pig Script Execution
        description: Execute Apache Pig Latin scripts as optimized Tez DAGs.
      - name: Complex ETL Pipelines
        description: Multi-stage data transformation pipelines with in-memory data passing.
  - type: Integrations
    data:
      - name: Apache Hadoop YARN
        description: Native YARN resource manager integration for cluster resource allocation.
      - name: Apache Hive
        description: Default execution engine for Hive queries in HDP and CDH distributions.
      - name: Apache Pig
        description: Tez execution backend for Apache Pig script compilation and execution.
      - name: Apache HDFS
        description: Input/output storage for Tez job data via Hadoop Distributed File System.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
