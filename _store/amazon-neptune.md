---
name: Amazon Neptune
description: Amazon Neptune is a fast, reliable, fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets. It supports property graph and RDF models, with multiple query languages including Gremlin, SPARQL, and openCypher.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
tags:
  - AWS
  - Database
  - Graph Database
  - Gremlin
  - Neptune
  - Property Graph
  - RDF
  - SPARQL
created: '2024'
modified: '2026-04-19'
specificationVersion: '0.18'
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
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
common:
  - type: Portal
    url: https://aws.amazon.com/neptune/
  - type: Documentation
    url: https://docs.aws.amazon.com/neptune/
  - type: Getting Started
    url: https://aws.amazon.com/neptune/getting-started/
  - type: Authentication
    url: https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html
  - type: Blog
    url: https://aws.amazon.com/blogs/database/category/database/amazon-neptune/
  - type: Change Log
    url: https://docs.aws.amazon.com/neptune/latest/userguide/doc-history.html
  - type: Release Notes
    url: https://docs.aws.amazon.com/neptune/latest/userguide/engine-releases.html
  - type: Status
    url: https://health.aws.amazon.com/
  - type: Support
    url: https://repost.aws/tags/TAxVAEdWg1SrS0lClUSX-m_Q
  - type: Terms of Service
    url: https://aws.amazon.com/service-terms/
  - type: Privacy Policy
    url: https://aws.amazon.com/privacy/
  - type: GitHub Organization
    url: https://github.com/aws
  - type: Community
    url: https://repost.aws/
  - type: Website
    url: https://aws.amazon.com/neptune/
  - type: Login
    url: https://console.aws.amazon.com/neptune/
  - type: Sign Up
    url: https://portal.aws.amazon.com/billing/signup
  - type: FAQs
    url: https://aws.amazon.com/neptune/faqs/
  - type: Features
    url: https://aws.amazon.com/neptune/features/
  - type: Security
    url: https://docs.aws.amazon.com/neptune/latest/userguide/security.html
  - type: Service Level Agreement
    url: https://aws.amazon.com/neptune/sla/
  - type: Console
    url: https://console.aws.amazon.com/neptune/
  - type: GitHub Samples
    url: https://github.com/aws-samples/amazon-neptune-samples
  - type: SDKs
    url: https://docs.aws.amazon.com/neptune/latest/userguide/using-neptune-apis.html
  - type: Tools
    url: https://github.com/awslabs/amazon-neptune-tools
  - type: Pricing
    url: https://aws.amazon.com/neptune/pricing/
  - type: JSON-LD
    url: json-ld/amazon-neptune-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-neptune-db-cluster-schema.json
    title: DB Cluster Schema
  - type: JSONSchema
    url: json-schema/amazon-neptune-db-instance-schema.json
    title: DB Instance Schema
  - type: JSONSchema
    url: json-schema/amazon-neptune-graph-element-schema.json
    title: Graph Element Schema
  - type: JSONSchema
    url: json-schema/amazon-neptune-loader-job-schema.json
    title: Loader Job Schema
  - type: JSONSchema
    url: json-schema/amazon-neptune-stream-record-schema.json
    title: Stream Record Schema
  - type: JSONSchema
    url: json-schema/amazon-neptune-analytics-graph-schema.json
    title: Analytics Graph Schema
  - type: JSONSchema
    url: json-schema/amazon-neptune-ml-job-schema.json
    title: ML Job Schema
  - type: Features
    data:
      - name: Serverless Graph Database
        description: Automatically scales compute and memory resources based on workload demands without requiring capacity planning.
      - name: Multiple Query Language Support
        description: Supports Apache TinkerPop Gremlin, openCypher, and SPARQL 1.1 query languages for property graph and RDF models.
      - name: High Availability
        description: Multi-AZ deployment with up to 15 read replicas, automated failover, and continuous backups with point-in-time recovery up to 35 days.
      - name: Global Database
        description: Multi-region replication with sub-second latency across up to five secondary clusters for global applications.
      - name: Neptune Analytics
        description: Memory-optimized graph analytics engine for analyzing tens of billions of relationships within seconds with vector search capabilities.
      - name: GraphRAG Support
        description: Fully managed GraphRAG with Amazon Bedrock Knowledge Bases for AI-enhanced graph retrieval augmented generation.
      - name: Machine Learning on Graphs
        description: Native graph neural network support via Neptune ML powered by Amazon SageMaker for link prediction and node classification.
      - name: ACID Transactions
        description: Full ACID transaction support ensuring data consistency and integrity across graph operations.
      - name: AWS Security Integration
        description: VPC network isolation, IAM resource permissions, AWS KMS encryption, TLS in-transit encryption, and CloudWatch audit logging.
      - name: Auto-Expanding Storage
        description: Storage automatically grows up to 128 TiB with self-healing architecture spanning three availability zones.
  - type: UseCases
    data:
      - name: Knowledge Graphs and GraphRAG
        description: Build knowledge graphs to enhance AI accuracy, comprehensiveness, and explainability using GraphRAG with Amazon Bedrock.
      - name: Fraud Detection
        description: Model transaction and account relationship networks to detect fraudulent patterns in near real-time using graph traversals.
      - name: Customer 360
        description: Build unified customer profile graphs linking purchases, preferences, and interactions for personalization and marketing.
      - name: Cybersecurity and Threat Detection
        description: Model IT infrastructure as a connected graph to detect attack paths, anomalies, and proactive threats.
      - name: Recommendation Engines
        description: Power product and content recommendation engines by traversing user-item relationship graphs.
      - name: Social Networks
        description: Model and query highly connected social graph data for applications requiring relationship traversal at scale.
      - name: Network and IT Operations
        description: Map network topology, dependencies, and configuration relationships for operations and impact analysis.
      - name: Supply Chain Management
        description: Model complex supply chain relationships and dependencies for optimization and risk analysis.
  - type: Integrations
    data:
      - name: Amazon Bedrock
        description: Integration with Bedrock Knowledge Bases for fully managed GraphRAG and AI-enhanced knowledge graph applications.
      - name: Amazon SageMaker
        description: Neptune ML uses SageMaker for training graph neural network models on Neptune graph data.
      - name: Amazon S3
        description: Bulk data loading from S3 using the Neptune Loader API with CSV and RDF serialization format support.
      - name: AWS IAM
        description: Fine-grained resource-level access control and role-based permissions via AWS Identity and Access Management.
      - name: Amazon CloudWatch
        description: Metrics, logs, and audit logging for monitoring Neptune cluster performance and compliance.
      - name: AWS KMS
        description: Encryption at rest using AWS Key Management Service for customer-managed key support.
      - name: Amazon VPC
        description: Network isolation using Amazon Virtual Private Cloud with security group and firewall controls.
      - name: Apache TinkerPop
        description: Gremlin graph traversal language and TinkerPop ecosystem integration for property graph querying.
      - name: Strands AI Agents SDK
        description: Integration with Strands AI Agents SDK and popular agentic memory tools for AI agent applications.
  - type: SpectralRules
    url: rules/amazon-neptune-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-neptune-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/neptune-graph-management.yaml
  - type: NaftikoCapability
    url: capabilities/neptune-analytics-ml.yaml
  - type: JSON-LD
    url: json-ld/amazon-neptune-analytics-context.jsonld
    title: Analytics Context
  - type: JSON-LD
    url: json-ld/amazon-neptune-data-context.jsonld
    title: Data Context
  - type: JSON-LD
    url: json-ld/amazon-neptune-gremlin-context.jsonld
    title: Gremlin Context
  - type: JSON-LD
    url: json-ld/amazon-neptune-loader-context.jsonld
    title: Loader Context
  - type: JSON-LD
    url: json-ld/amazon-neptune-management-context.jsonld
    title: Management Context
  - type: JSON-LD
    url: json-ld/amazon-neptune-ml-context.jsonld
    title: Ml Context
  - type: JSON-LD
    url: json-ld/amazon-neptune-opencypher-context.jsonld
    title: Opencypher Context
  - type: JSON-LD
    url: json-ld/amazon-neptune-sparql-context.jsonld
    title: Sparql Context
  - type: JSON-LD
    url: json-ld/amazon-neptune-streams-context.jsonld
    title: Streams Context
---
