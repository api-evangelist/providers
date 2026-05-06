---
name: Amazon DynamoDB
description: Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability, allowing you to store and retrieve any amount of data and serve any level of request traffic using key-value and document data models.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/dynamodb/
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon DynamoDB API
    description: Core API for managing Amazon DynamoDB tables, items, indexes, and performing data plane operations including single-item actions, queries, scans, batch operations, and transactions.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/dynamodb/
    baseURL: https://dynamodb.amazonaws.com
    tags:
      - AWS
      - Database
      - Document Store
      - Key-Value
      - NoSQL
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/
      - type: OpenAPI
        url: openapi/amazon-dynamodb-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/dynamodb/2012-08-10/openapi.yaml
      - type: JSONSchema
        url: json-schema/amazon-dynamodb-table-schema.json
      - type: JSONLD
        url: json-ld/amazon-dynamodb-context.jsonld
      - type: Pricing
        url: https://aws.amazon.com/dynamodb/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/dynamodb/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/dynamodb/faqs/
      - type: TermsOfService
        url: https://aws.amazon.com/dynamodb/sla/
      - type: Documentation
        url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/
      - type: APIReference
        url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/
      - type: Documentation
        url: https://docs.aws.amazon.com/cli/latest/reference/dynamodb/
      - type: Security
        url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security.html
      - type: JSONStructure
        url: json-structure/amazon-dynamodb-table-structure.json
      - type: Example
        url: examples/amazon-dynamodb-table-example.json
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/dynamodb/
  - type: Documentation
    url: https://docs.aws.amazon.com/dynamodb/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/database/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/dynamodbv2/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-dynamodb
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Security
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security.html
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Features
    data:
      - name: Serverless Architecture
        description: Fully managed, no server provisioning, patching, or capacity management required.
      - name: Single-Digit Millisecond Performance
        description: Consistent performance at any scale with single-digit millisecond response times.
      - name: Global Tables
        description: Multi-Region, active-active replication with up to 99.999% availability and zero RPO.
      - name: Automatic Scaling
        description: On-demand mode automatically adapts to application throughput without capacity planning.
      - name: Transactions
        description: ACID transactions across multiple items and tables with conditional operations.
      - name: Streams
        description: DynamoDB Streams captures a time-ordered sequence of changes to items for event-driven architectures.
      - name: Point-in-Time Recovery
        description: Enables continuous backups with point-in-time recovery to any second over the last 35 days.
      - name: TTL
        description: Time to Live automatically deletes expired items to reduce storage costs.
  - type: UseCases
    data:
      - name: Financial Services
        description: Fraud detection, digital onboarding, and regulatory compliance workloads requiring consistent low latency.
      - name: Gaming Applications
        description: Player profiles, leaderboards, session state, and game data with high-throughput requirements.
      - name: E-Commerce
        description: Shopping carts, inventory tracking, order management, and customer data platforms.
      - name: IoT Data Storage
        description: High-volume telemetry data ingestion and time-series storage from IoT devices.
      - name: Content Management
        description: Metadata storage and content indexing for media streaming and publishing platforms.
  - type: Integrations
    data:
      - name: AWS Lambda
        description: Event-driven processing of DynamoDB Streams with Lambda functions for real-time workflows.
      - name: Amazon CloudWatch
        description: Monitor DynamoDB table metrics, set alarms, and view consumption and performance data.
      - name: AWS IAM
        description: Fine-grained access control for tables, items, and attributes using IAM policies.
      - name: Amazon Kinesis Data Streams
        description: Export DynamoDB changes to Kinesis for real-time analytics and archiving.
      - name: AWS Glue
        description: Export DynamoDB data to S3 for analysis with Athena, Redshift Spectrum, or SageMaker.
  - type: SpectralRules
    url: rules/amazon-dynamodb-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-dynamodb-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/dynamodb-management.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AWS
  - Database
  - Document Store
  - Key-Value
  - NoSQL
  - Serverless
---
