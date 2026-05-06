---
name: Schema Evolution
description: Schema Evolution is the practice of managing changes to data schemas over time while preserving compatibility between producers and consumers. It covers backward compatibility, forward compatibility, full compatibility, breaking change detection, schema migration strategies, and versioning patterns for REST APIs, event streaming (Kafka/Avro), GraphQL, database schemas, and Protocol Buffers. Effective schema evolution is critical for maintaining API contracts and enabling independent deployment of distributed system components.
url: https://github.com/api-evangelist/schema-evolution
x-type: topic
tags:
  - Schema Evolution
  - Backward Compatibility
  - Forward Compatibility
  - API Versioning
  - Breaking Changes
  - Schema Registry
  - Data Migration
  - Kafka
created: '2026-05-02'
modified: '2026-05-02'
apis:
  - name: Confluent Schema Registry API
    description: The Confluent Schema Registry provides a serving layer for your metadata. It provides a RESTful interface for storing and retrieving your Avro, JSON Schema, and Protobuf schemas. It stores a versioned history of all schemas based on a specified subject name strategy, provides multiple compatibility settings and allows evolution of schemas according to the configured compatibility setting. It is used by Kafka producers and consumers to enforce schema compatibility when reading and writing Kafka messages.
    humanURL: https://docs.confluent.io/platform/current/schema-registry/develop/api.html
    baseURL: https://your-schema-registry-host/
    tags:
      - Schema Registry
      - Confluent
      - Kafka
      - Avro
      - Compatibility
    properties:
      - type: Documentation
        url: https://docs.confluent.io/platform/current/schema-registry/develop/api.html
      - type: Reference
        url: https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html
  - name: AWS Glue Schema Registry API
    description: AWS Glue Schema Registry is a feature that enables you to centrally discover, control, and evolve data stream schemas. The AWS Glue Schema Registry API supports creating, deleting, listing, updating, and fetching schemas, and it supports compatibility checking for Avro and JSON Schema formats.
    humanURL: https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html
    baseURL: https://glue.us-east-1.amazonaws.com
    tags:
      - AWS
      - Schema Registry
      - Cloud
      - Avro
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html
  - name: Apicurio Schema Registry API
    description: Apicurio Registry is a datastore for standard event schemas and API designs. Apicurio Registry enables you to add, update, and remove artifacts from the registry using a REST API interface. It supports Apache Avro, JSON Schema, Protobuf, GraphQL SDL, and more, with configurable compatibility rules including backward, forward, and full compatibility.
    humanURL: https://www.apicur.io/registry/
    baseURL: https://registry.example.com/apis/registry/v2
    tags:
      - Schema Registry
      - Open Source
      - Avro
      - Compatibility
    properties:
      - type: Documentation
        url: https://www.apicur.io/registry/
      - type: GitHub Repository
        url: https://github.com/Apicurio/apicurio-registry
common:
  - type: Website
    url: https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html
  - type: JSONSchema
    url: json-schema/schema-evolution-change-schema.json
  - type: JSONStructure
    url: json-structure/schema-evolution-compatibility-structure.json
  - type: JSONLDContext
    url: json-ld/schema-evolution-context.jsonld
  - type: Vocabulary
    url: vocabulary/schema-evolution-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
