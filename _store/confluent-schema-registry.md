---
aid: confluent-schema-registry
url: https://raw.githubusercontent.com/api-evangelist/confluent-schema-registry/refs/heads/main/apis.yml
apis:
- aid: confluent-schema-registry:schema-registry-rest-api
  name: Confluent Schema Registry REST API
  description: RESTful API for managing schemas, subjects, versions, and compatibility settings. Supports Avro, JSON Schema, and Protobuf schema types with configurable compatibility levels and schema references.
  humanURL: https://docs.confluent.io/platform/current/schema-registry/develop/api.html
  baseURL: http://localhost:8081
  tags:
  - Compatibility
  - REST API
  - Schema Registry
  - Schemas
  properties:
  - type: Documentation
    url: https://docs.confluent.io/platform/current/schema-registry/develop/api.html
  - type: OpenAPI
    url: openapi/schema-registry.yml
  - type: JSONSchema
    url: json-schema/schema-registry-schema.json
name: Confluent Schema Registry
tags:
- Apache Kafka
- Avro
- Data Governance
- JSON Schema
- Protobuf
- Schema Registry
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Confluent Schema Registry provides a serving layer for metadata, offering a RESTful interface for storing and retrieving Avro, JSON Schema, and Protobuf schemas, enabling schema evolution and compatibility management for Apache Kafka-based streaming data pipelines.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

