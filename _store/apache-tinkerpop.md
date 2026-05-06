---
aid: apache-tinkerpop
name: Apache TinkerPop
description: Apache TinkerPop is a graph computing framework for both graph databases (OLTP) and graph analytic systems (OLAP). It provides the Gremlin graph traversal language which works with any TinkerPop-enabled graph system. TinkerPop abstracts the underlying graph database, allowing applications to work with Neo4j, Amazon Neptune, Azure Cosmos DB, JanusGraph, Amazon DynamoDB, and other graph databases using a single consistent API. It is maintained by the Apache Software Foundation.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Graph Computing
  - Graph Database
  - Gremlin
  - OLAP
  - OLTP
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-tinkerpop/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-tinkerpop:apache-tinkerpop-gremlin-server-api
    name: Apache TinkerPop Gremlin Server API
    description: The Gremlin Server provides WebSocket and HTTP endpoints for submitting Gremlin traversals to a remote graph database. The HTTP API accepts POST requests with Gremlin traversal strings or bytecode at /gremlin endpoint. The WebSocket API supports binary (GraphBinary) and text (GraphSON) serialization formats. Gremlin Server also exposes REST-like endpoints for graph management operations.
    humanURL: https://tinkerpop.apache.org/docs/current/reference/#gremlin-server
    tags:
      - WebSocket
      - HTTP
      - Gremlin
      - Graph Database
    properties:
      - type: Documentation
        url: https://tinkerpop.apache.org/docs/current/reference/#gremlin-server
  - aid: apache-tinkerpop:apache-tinkerpop-gremlin-api
    name: Apache TinkerPop Gremlin Traversal API
    description: The Gremlin graph traversal language and API provide a functional, data-flow-based language for expressing complex graph queries and mutations. Gremlin steps include vertex/edge traversals (V, E, out, in, both, outE, inE), filtering (has, where, filter), transformation (map, flatMap, select, project), aggregation (groupCount, group, count, sum), and mutation steps (addV, addE, property, drop). Available as Java, Python, JavaScript, Go, .NET, and other language SDKs.
    humanURL: https://tinkerpop.apache.org/docs/current/reference/
    tags:
      - Gremlin
      - Graph Traversal
      - Graph Database
      - Java
      - Python
    properties:
      - type: Documentation
        url: https://tinkerpop.apache.org/docs/current/reference/
      - type: SDK
        url: https://pypi.org/project/gremlinpython/
        title: Python Gremlin SDK
      - type: SDK
        url: https://search.maven.org/search?q=org.apache.tinkerpop
        title: Java Maven SDK
      - type: SDK
        url: https://www.npmjs.com/package/gremlin
        title: JavaScript/Node.js SDK
common:
  - type: GitHubRepository
    url: https://github.com/apache/tinkerpop
  - type: Documentation
    url: https://tinkerpop.apache.org/docs/current/reference/
  - type: Portal
    url: https://tinkerpop.apache.org/
  - type: GettingStarted
    url: https://tinkerpop.apache.org/docs/current/tutorials/getting-started/
  - type: ReleaseNotes
    url: https://github.com/apache/tinkerpop/releases
  - type: Support
    url: https://groups.google.com/g/gremlin-users
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: Features
    data:
      - name: Graph Database Abstraction
        description: Single API working across Neo4j, JanusGraph, Amazon Neptune, Azure Cosmos DB, and 20+ graph systems.
      - name: Gremlin Language
        description: Expressive functional graph traversal language for both queries and mutations.
      - name: OLAP Graph Processing
        description: Bulk/analytical graph processing via SparkGraphComputer for large-scale graph algorithms.
      - name: GraphBinary Serialization
        description: Compact binary serialization format for efficient Gremlin traversal encoding.
      - name: GraphSON Format
        description: JSON-based graph serialization format for human-readable graph data exchange.
      - name: Gremlin Server
        description: Standalone server hosting Gremlin traversal execution over WebSocket or HTTP.
      - name: Multi-Language SDKs
        description: Official Gremlin SDKs for Java, Python, JavaScript, Go, and .NET.
  - type: UseCases
    data:
      - name: Knowledge Graphs
        description: Build and query knowledge graphs for entity relationship modeling.
      - name: Social Network Analysis
        description: Traverse and analyze social graph relationships and influence patterns.
      - name: Fraud Detection
        description: Detect fraud rings and suspicious patterns via graph relationship traversal.
      - name: Recommendation Engines
        description: Graph-based collaborative filtering and content recommendation.
      - name: Identity and Access Management
        description: Model and query complex permission hierarchies and role relationships.
  - type: Integrations
    data:
      - name: Amazon Neptune
        description: AWS managed graph database with full TinkerPop and Gremlin compatibility.
      - name: Azure Cosmos DB
        description: Azure Cosmos DB Gremlin API for TinkerPop-compatible graph storage.
      - name: JanusGraph
        description: Distributed graph database with TinkerPop/Gremlin interface and Cassandra/HBase backend.
      - name: Neo4j
        description: Neo4j TinkerPop plugin for Gremlin traversal on Neo4j graph data.
      - name: Apache Spark
        description: SparkGraphComputer for OLAP graph analytics on Spark clusters.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
