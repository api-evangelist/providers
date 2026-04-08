---
aid: amazon-neptune
url: https://raw.githubusercontent.com/api-evangelist/amazon-neptune/refs/heads/main/apis.yml
apis:
- name: Amazon Neptune Management API
  description: Amazon Neptune Management API for creating, managing, and deleting Neptune DB clusters, instances, parameter groups, snapshots, and related infrastructure resources.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://aws.amazon.com/neptune/
  baseUrl: https://rds.{region}.amazonaws.com
  tags:
  - AWS
  - Cluster Management
  - Database Management
  - Graph Database
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/neptune/latest/userguide/intro.html
  - type: OpenAPI
    url: openapi/amazon-neptune-management-openapi.yml
  - type: API Reference
    url: https://docs.aws.amazon.com/neptune/latest/userguide/api.html
  - type: Pricing
    url: https://aws.amazon.com/neptune/pricing/
  - type: Getting Started
    url: https://docs.aws.amazon.com/neptune/latest/userguide/get-started.html
  - type: SDKs
    url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune.html
- name: Amazon Neptune Data API
  description: Amazon Neptune Data API provides SDK support for more than 40 data operations including data loading, query execution, data inquiry, and machine learning. It supports Gremlin and openCypher query languages.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://docs.aws.amazon.com/neptune/latest/userguide/data-api.html
  baseUrl: https://neptune-db.{region}.amazonaws.com
  tags:
  - Data API
  - Data Operations
  - Graph Query
  - SDK
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/neptune/latest/userguide/data-api.html
  - type: OpenAPI
    url: openapi/amazon-neptune-data-openapi.yml
  - type: API Reference
    url: https://docs.aws.amazon.com/neptune/latest/data-api/Welcome.html
  - type: SDKs
    url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata.html
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/neptunedata/
  - type: JavaScript SDK
    url: https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/neptunedata/
  - type: Go SDK
    url: https://docs.aws.amazon.com/sdk-for-go/api/service/neptunedata/
- name: Neptune Gremlin API
  description: Apache TinkerPop Gremlin graph traversal language API for querying property graphs in Neptune. It supports both WebSocket and HTTP REST endpoints for submitting Gremlin traversals.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin.html
  baseUrl: wss://{cluster-endpoint}:8182/gremlin
  tags:
  - Graph Traversal
  - Gremlin
  - Property Graph
  - Query Language
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin.html
  - type: OpenAPI
    url: openapi/amazon-neptune-gremlin-openapi.yml
  - type: Reference
    url: https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-api-reference.html
  - type: Gremlin Reference
    url: https://tinkerpop.apache.org/docs/current/reference/
  - type: Best Practices
    url: https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-gremlin.html
  - type: REST Endpoint
    url: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-rest.html
- name: Neptune SPARQL API
  description: W3C SPARQL 1.1 query language API for querying RDF graphs in Neptune. It provides an HTTP REST endpoint compatible with the SPARQL 1.1 protocol specification.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html
  baseUrl: https://{cluster-endpoint}:8182/sparql
  tags:
  - Query Language
  - RDF
  - Semantic Web
  - SPARQL
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql.html
  - type: OpenAPI
    url: openapi/amazon-neptune-sparql-openapi.yml
  - type: SPARQL Reference
    url: https://www.w3.org/TR/sparql11-query/
  - type: Best Practices
    url: https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-sparql.html
  - type: REST Endpoint
    url: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql-http-rest.html
- name: Neptune openCypher API
  description: openCypher graph query language API for querying property graphs with Cypher syntax in Neptune. It provides an HTTP endpoint for executing openCypher queries against property graph data.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html
  baseUrl: https://{cluster-endpoint}:8182/openCypher
  tags:
  - Cypher
  - openCypher
  - Property Graph
  - Query Language
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html
  - type: OpenAPI
    url: openapi/amazon-neptune-opencypher-openapi.yml
  - type: openCypher Reference
    url: https://opencypher.org/
  - type: Best Practices
    url: https://docs.aws.amazon.com/neptune/latest/userguide/best-practices-opencypher.html
- name: Neptune Streams API
  description: Neptune Streams generates a complete sequence of change-log entries that record every change made to graph data as it happens, enabling real-time capture of graph mutations via a REST API.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://docs.aws.amazon.com/neptune/latest/userguide/streams.html
  baseUrl: https://{cluster-endpoint}:8182
  tags:
  - Change Data Capture
  - Event Log
  - Real-Time
  - Streams
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/neptune/latest/userguide/streams.html
  - type: OpenAPI
    url: openapi/amazon-neptune-streams-openapi.yml
  - type: API Reference
    url: https://docs.aws.amazon.com/neptune/latest/userguide/streams-using-api-call.html
  - type: Response Format
    url: https://docs.aws.amazon.com/neptune/latest/userguide/streams-using-api-reponse.html
  - type: Data API Reference
    url: https://docs.aws.amazon.com/neptune/latest/userguide/data-api-dp-streams.html
- name: Neptune Loader API
  description: Neptune bulk loader API for ingesting large volumes of data from Amazon S3 into a Neptune DB instance. It supports CSV formats for property graphs and multiple RDF serialization formats.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html
  baseUrl: https://{cluster-endpoint}:8182/loader
  tags:
  - Bulk Import
  - Data Ingestion
  - Data Loading
  - ETL
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html
  - type: OpenAPI
    url: openapi/amazon-neptune-loader-openapi.yml
  - type: API Reference
    url: https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference.html
  - type: Loader Command
    url: https://docs.aws.amazon.com/neptune/latest/userguide/load-api-reference-load.html
  - type: Data Formats
    url: https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format.html
  - type: Data API Reference
    url: https://docs.aws.amazon.com/neptune/latest/userguide/data-api-dp-loader.html
- name: Neptune ML API
  description: Neptune ML enables machine learning on graph data using graph neural networks. It provides APIs for data processing, model training, and inference endpoint management powered by Amazon SageMaker.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://aws.amazon.com/neptune/machine-learning/
  baseUrl: https://{cluster-endpoint}:8182/ml
  tags:
  - Graph Neural Network
  - Machine Learning
  - Predictions
  - SageMaker
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning.html
  - type: OpenAPI
    url: openapi/amazon-neptune-ml-openapi.yml
  - type: API Reference
    url: https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-api-reference.html
  - type: Model Training
    url: https://docs.aws.amazon.com/neptune/latest/userguide/data-api-dp-ml-training.html
  - type: Getting Started
    url: https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-overview.html
- name: Neptune Analytics API
  description: Neptune Analytics is a memory-optimized graph database engine for analytics, providing optimized graph analytic algorithms, low-latency queries, and vector search capabilities within graph traversals.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html
  baseUrl: https://neptune-graph.{region}.amazonaws.com
  tags:
  - Analytics
  - Graph Analytics
  - In-Memory
  - Vector Search
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html
  - type: OpenAPI
    url: openapi/amazon-neptune-analytics-openapi.yml
  - type: API Reference
    url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/Welcome.html
  - type: SDKs
    url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph.html
  - type: Getting Started
    url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-accessing.html
name: Amazon Neptune
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Neptune is a fast, reliable, fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets. It supports property graph and RDF models, with multiple query languages including Gremlin, SPARQL, and openCypher.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

