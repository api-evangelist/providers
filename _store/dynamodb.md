---
aid: dynamodb
url: https://raw.githubusercontent.com/api-evangelist/dynamodb/refs/heads/main/apis.yml
apis:
- name: Amazon DynamoDB API
  description: RESTful API for interacting with DynamoDB tables and items.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://aws.amazon.com/dynamodb/
  baseUrl: https://dynamodb.{region}.amazonaws.com
  tags:
  - Database
  - Items
  - Managed Service
  - Nosql
  - Queries
  - Tables
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/dynamodb/
  - type: OpenAPI
    url: openapi/dynamodb-openapi.yml
  - type: OpenAPI (Third-Party)
    url: https://api.apis.guru/v2/specs/amazonaws.com/dynamodb/2012-08-10/openapi.yaml
  - type: JSON Schema
    url: json-schema/dynamodb-item-schema.json
  - type: JSON-LD Context
    url: json-ld/dynamodb-context.jsonld
  - type: API Reference
    url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/Welcome.html
  - type: Getting Started
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html
  - type: SDKs
    url: https://aws.amazon.com/tools/
  - type: Pricing
    url: https://aws.amazon.com/dynamodb/pricing/
  - type: Service Level Agreement
    url: https://aws.amazon.com/dynamodb/sla/
  - type: Console
    url: https://console.aws.amazon.com/dynamodb/
  - type: Best Practices
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html
  - type: FAQ
    url: https://aws.amazon.com/dynamodb/faqs/
  - type: Status
    url: https://status.aws.amazon.com/
  - type: API Operations
    url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Operations_Amazon_DynamoDB.html
  - type: Developer Guide
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html
  - type: Low-Level API
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.LowLevelAPI.html
  - type: PartiQL Reference
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.html
  - type: Global Tables
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html
  - type: Backup and Restore
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Backup-and-Restore.html
  - type: Point-in-Time Recovery
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Point-in-time-recovery.html
  - type: Export to S3
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataExport.HowItWorks.html
  - type: Import from S3
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/S3DataImport.HowItWorks.html
  - type: Security
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security.html
  - type: Contributor Insights
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/contributorinsights.html
  - type: Features
    url: https://aws.amazon.com/dynamodb/features/
  - type: Document History
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DocumentHistory.html
  - type: Postman Collection
    url: https://www.postman.com/api-evangelist/amazon-web-services-aws/documentation/tuuvg4g/amazon-dynamodb
- name: Amazon DynamoDB Streams API
  description: API for capturing and processing change data from DynamoDB tables in near real-time, providing time-ordered sequences of item-level modifications.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html
  baseUrl: https://streams.dynamodb.{region}.amazonaws.com
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
  - type: OpenAPI (Third-Party)
    url: https://api.apis.guru/v2/specs/amazonaws.com/streams.dynamodb/2012-08-10/openapi.yaml
  - type: API Reference
    url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Operations_Amazon_DynamoDB_Streams.html
  - type: Low-Level Walkthrough
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.LowLevel.Walkthrough.html
- name: Amazon DynamoDB Accelerator (DAX) API
  description: API for managing DynamoDB Accelerator (DAX) clusters, an in-memory caching service that delivers microsecond response times for DynamoDB read workloads.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanUrl: https://aws.amazon.com/dynamodbaccelerator/
  baseUrl: https://dax.{region}.amazonaws.com
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
  - type: API Reference
    url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Types_Amazon_DynamoDB_Accelerator__DAX_.html
  - type: How It Works
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.concepts.html
  - type: Client Development
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.client.html
  - type: Cluster Management
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html
name: Amazon DynamoDB
tags:
- Aws
- Cloud
- Database
- Document Store
- Key-Value
- Managed Service
- Nosql
- Serverless
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

