---
aid: apache-giraph
name: Apache Giraph
description: Apache Giraph is an iterative graph processing system built for high scalability on Apache Hadoop. It is modeled after Google's Pregel and provides a simple yet flexible Java API for graph algorithms at massive scale using the Bulk Synchronous Parallel (BSP) model. Note - Apache Giraph has been retired as of 2024.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Big Data
  - BSP
  - Graph Processing
  - Hadoop
  - Open Source
  - Retired
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-giraph/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-giraph:apache-giraph-job-api
    name: Apache Giraph Job Monitoring API
    description: Monitoring API for Apache Giraph graph processing jobs via the YARN ResourceManager REST API, providing job status, progress tracking, and cluster capacity metrics.
    humanURL: https://giraph.apache.org/quick_start.html
    baseURL: http://localhost:8088
    tags:
      - BSP
      - Graph
      - Hadoop
      - Job Management
      - YARN
    properties:
      - type: Documentation
        url: https://giraph.apache.org/quick_start.html
      - type: OpenAPI
        url: openapi/apache-giraph-job-openapi.yml
      - type: JSONSchema
        url: json-schema/giraph-job-application-info-schema.json
      - type: JSON-LD
        url: json-ld/apache-giraph-job-context.jsonld
  - aid: apache-giraph:apache-giraph-java-api
    name: Apache Giraph Java API
    description: Java API based on the Bulk Synchronous Parallel (BSP) model for implementing graph algorithms, with Vertex, Edge, and Master compute APIs for distributed graph processing on Hadoop.
    humanURL: https://giraph.apache.org/apidocs/
    tags:
      - BSP
      - Graph
      - Java
      - SDK
    properties:
      - type: Documentation
        url: https://giraph.apache.org/apidocs/
      - type: SDK
        url: https://search.maven.org/artifact/org.apache.giraph/giraph-core
        title: Java SDK (Maven Central)
common:
  - type: Documentation
    url: https://giraph.apache.org/
  - type: GettingStarted
    url: https://giraph.apache.org/quick_start.html
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/giraph
  - type: SpectralRules
    url: rules/apache-giraph-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-giraph-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/giraph-graph-processing.yaml
  - type: Features
    data:
      - name: Bulk Synchronous Parallel (BSP) Model
        description: Google Pregel-inspired BSP computation model where vertices communicate through supersteps.
      - name: Vertex-Centric Programming
        description: Write graph algorithms by defining per-vertex compute functions that exchange messages with neighbors.
      - name: Master Compute API
        description: Global coordination API for aggregating results and controlling algorithm termination across supersteps.
      - name: Aggregators
        description: Sharded aggregators for collecting global statistics across all vertices during computation.
      - name: Edge-Oriented Input
        description: Flexible input formats for loading graphs from HDFS, Hive, Gora, and Rexster sources.
      - name: Out-of-Core Computation
        description: Spill graph data to disk for processing graphs larger than available memory.
      - name: Hadoop Integration
        description: Runs as a MapReduce job on Apache Hadoop YARN for resource management and fault tolerance.
      - name: Fault Tolerance
        description: Checkpoint-based recovery for fault tolerance across superstep boundaries.
  - type: UseCases
    data:
      - name: Social Graph Analysis
        description: Analyze social network connections, communities, and influence at billions-of-vertices scale (as used at Facebook).
      - name: PageRank Computation
        description: Compute web page or entity rankings using iterative link analysis algorithms.
      - name: Shortest Path Computation
        description: Find shortest paths between vertices for network routing and recommendation problems.
      - name: Connected Components
        description: Identify clusters and connected components in large graphs for community detection.
      - name: Graph Machine Learning Features
        description: Generate graph-structural features for machine learning models at scale.
  - type: Integrations
    data:
      - name: Apache Hadoop
        description: Runs on Hadoop YARN as a MapReduce application for cluster resource management.
      - name: Apache Hive
        description: Hive I/O module for loading graph data from Hive tables.
      - name: Apache Gora
        description: Gora I/O module for loading graph data from various NoSQL data stores.
      - name: Rexster
        description: Rexster graph server I/O module for loading data from TinkerPop graph databases.
      - name: Apache HBase
        description: HBase integration for storing and loading vertex and edge data.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
