---
name: Amazon DynamoDB
description: A fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
tags:
  - AWS
  - Cloud
  - Database
  - Document Store
  - Key-Value
  - Managed Service
  - NoSQL
  - Serverless
created: '2024'
modified: '2026-04-18'
url: https://aws.amazon.com/dynamodb/
specificationVersion: '0.18'
apis:
  - name: Amazon DynamoDB API
    description: RESTful API for interacting with DynamoDB tables and items.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/dynamodb/
    baseURL: https://dynamodb.{region}.amazonaws.com
    tags:
      - Database
      - Items
      - Managed Service
      - NoSQL
      - Queries
      - Tables
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/dynamodb/
      - type: OpenAPI
        url: openapi/dynamodb-openapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/Welcome.html
      - type: GettingStarted
        url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html
      - type: SDK
        url: https://aws.amazon.com/tools/
      - type: Pricing
        url: https://aws.amazon.com/dynamodb/pricing/
      - type: Console
        url: https://console.aws.amazon.com/dynamodb/
      - type: BestPractices
        url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html
      - type: FAQ
        url: https://aws.amazon.com/dynamodb/faqs/
      - type: StatusPage
        url: https://status.aws.amazon.com/
      - type: Security
        url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security.html
      - type: Features
        url: https://aws.amazon.com/dynamodb/features/
      - type: JSONSchema
        url: json-schema/dynamodb-item-schema.json
      - type: JSONLD
        url: json-ld/dynamodb-context.jsonld
    contact:
      - type: Support
        url: https://aws.amazon.com/premiumsupport/
  - name: Amazon DynamoDB Streams API
    description: API for capturing and processing change data from DynamoDB tables in near real-time, providing time-ordered sequences of item-level modifications.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html
    baseURL: https://streams.dynamodb.{region}.amazonaws.com
    tags:
      - Change Data Capture
      - Event-Driven
      - Real-Time
      - Streams
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html
      - type: AsyncAPI
        url: asyncapi/dynamodb-streams-asyncapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Operations_Amazon_DynamoDB_Streams.html
  - name: Amazon DynamoDB Accelerator (DAX) API
    description: API for managing DynamoDB Accelerator (DAX) clusters, an in-memory caching service that delivers microsecond response times for DynamoDB read workloads.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/dynamodbaccelerator/
    baseURL: https://dax.{region}.amazonaws.com
    tags:
      - Accelerator
      - Caching
      - In-Memory
      - Performance
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/dax/2017-04-19/openapi.yaml
      - type: APIReference
        url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Types_Amazon_DynamoDB_Accelerator__DAX_.html
common:
  - type: Blog
    url: https://aws.amazon.com/blogs/database/category/database/amazon-dynamodb/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Resources
    url: https://aws.amazon.com/dynamodb/resources/
  - type: SpectralRules
    url: rules/dynamodb-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/dynamodb-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/database-management.yaml
  - type: Features
    data:
      - name: Single-Digit Millisecond Performance
        description: Consistent low-latency reads and writes at any scale with SSD-backed storage.
      - name: Global Tables
        description: Multi-region, multi-active replication for globally distributed applications.
      - name: On-Demand Capacity
        description: Automatically scale throughput capacity based on workload without capacity planning.
      - name: DynamoDB Streams
        description: Capture item-level changes for real-time processing, replication, and event-driven architectures.
      - name: Point-in-Time Recovery
        description: Continuous backups with restore to any second within the last 35 days.
      - name: Transactions
        description: ACID transactions across multiple items and tables for complex business logic.
      - name: PartiQL Support
        description: Execute SQL-compatible queries against DynamoDB tables using PartiQL language.
  - type: UseCases
    data:
      - name: Serverless Application Backend
        description: Use as the data layer for serverless architectures with Lambda and API Gateway.
      - name: Gaming Leaderboards
        description: Store and query player data, session state, and leaderboards with consistent low latency.
      - name: IoT Data Storage
        description: Ingest and query high-volume time-series data from IoT devices at scale.
      - name: E-Commerce Shopping Cart
        description: Store shopping cart and session data with high availability and automatic scaling.
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Trigger Lambda functions from DynamoDB Streams for event-driven processing.
      - name: Amazon S3
        description: Export table data to S3 or import from S3 for analytics and data migration.
      - name: Amazon Kinesis
        description: Stream DynamoDB changes to Kinesis for real-time analytics pipelines.
      - name: AWS CloudFormation
        description: Provision and manage DynamoDB tables as infrastructure as code.
      - name: Amazon CloudWatch
        description: Monitor table metrics, set alarms, and track performance with CloudWatch integration.
maintainers:
  - name: Amazon Web Services
    email: aws-dynamodb@amazon.com
    url: https://aws.amazon.com
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
