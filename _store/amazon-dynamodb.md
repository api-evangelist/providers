---
aid: amazon-dynamodb
url: https://raw.githubusercontent.com/api-evangelist/amazon-dynamodb/refs/heads/main/apis.yml
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
  - type: Getting Started
    url: https://aws.amazon.com/dynamodb/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/dynamodb/faqs/
  - type: Service Level Agreement
    url: https://aws.amazon.com/dynamodb/sla/
  - type: User Guide
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/
  - type: API Reference
    url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/dynamodb/
  - type: Security
    url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/security.html
name: Amazon DynamoDB
tags:
- AWS
- Database
- Document Store
- Key-Value
- NoSQL
- Serverless
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability, allowing you to store and retrieve any amount of data and serve any level of request traffic using key-value and document data models.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

