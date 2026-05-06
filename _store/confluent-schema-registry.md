---
aid: confluent-schema-registry
name: Confluent Schema Registry
description: Confluent Schema Registry is the open-source serving layer for schema metadata used in Apache Kafka data pipelines. It exposes a RESTful interface for storing and retrieving Avro, JSON Schema, and Protobuf schemas, manages schema evolution through configurable compatibility rules (BACKWARD, FORWARD, FULL, and transitive variants), supports schema references and contexts, and integrates with Kafka producers and consumers via shipped serializers and deserializers. Schema Registry is distributed under the Confluent Community License and is a core component of both Confluent Platform and Confluent Cloud.
type: Index
position: Provider
access: Open Source
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/confluent-schema-registry/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
x-type: opensource
tags:
  - Apache Kafka
  - Avro
  - Compatibility
  - Confluent
  - Data Governance
  - Data Streaming
  - JSON Schema
  - Open Source
  - Protobuf
  - REST
  - Schema Evolution
  - Schema Registry
apis:
  - aid: confluent-schema-registry:schema-registry-rest-api
    name: Confluent Schema Registry REST API
    description: The Confluent Schema Registry REST API provides programmatic management of schemas, subjects, schema versions, schema references, compatibility modes, and operating mode. Producers and consumers use it to register and look up Avro, JSON Schema, and Protobuf schemas, while platform teams use it to enforce schema evolution policies through subject- and cluster-level compatibility settings. The API uses the application/vnd.schemaregistry.v1+json content type and supports authentication via HTTP Basic, mTLS, or OAuth depending on deployment.
    humanURL: https://docs.confluent.io/platform/current/schema-registry/develop/api.html
    baseURL: http://localhost:8081
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Compatibility
      - REST
      - Schemas
      - Subjects
    properties:
      - type: Documentation
        url: https://docs.confluent.io/platform/current/schema-registry/develop/api.html
      - type: OpenAPI
        url: openapi/schema-registry.yml
      - type: JSONSchema
        url: json-schema/schema-registry-schema.json
      - type: JSON-LD
        url: json-ld/confluent-schema-registry-context.jsonld
      - type: Spectral
        url: rules/confluent-schema-registry-rules.yml
      - type: Naftiko Capabilities
        url: capabilities/confluent-schema-registry-capabilities.yml
      - type: GitHub
        url: https://github.com/confluentinc/schema-registry
    x-features:
      - Avro Schema Support
      - JSON Schema Support
      - Protobuf Schema Support
      - Schema Versioning
      - Compatibility Levels (BACKWARD, FORWARD, FULL)
      - Transitive Compatibility
      - Schema References
      - Schema Contexts
      - Schema Normalization
      - Soft and Hard Delete
      - Subject-Level and Global Configuration
      - Operating Modes (READWRITE, READONLY, IMPORT)
      - Schema Linking via Exporters
      - HTTP Basic, mTLS, and OAuth Auth
    x-use-cases:
      - Register schemas for Kafka producers and consumers
      - Evolve schemas safely with compatibility checks
      - Reference shared schemas across subjects
      - Migrate schemas between clusters with Schema Linking
      - Govern data contracts in streaming pipelines
common:
  - type: Website
    url: https://www.confluent.io/
  - type: Documentation
    url: https://docs.confluent.io/platform/current/schema-registry/
  - type: Getting Started
    url: https://docs.confluent.io/platform/current/schema-registry/develop/using.html
  - type: API Reference
    url: https://docs.confluent.io/platform/current/schema-registry/develop/api.html
  - type: GitHub
    url: https://github.com/confluentinc/schema-registry
  - type: License
    url: https://www.confluent.io/confluent-community-license/
  - type: Blog
    url: https://www.confluent.io/blog/
  - type: Pricing
    url: https://www.confluent.io/pricing/
  - type: JSON-LD
    url: json-ld/confluent-schema-registry-context.jsonld
  - type: Spectral
    url: rules/confluent-schema-registry-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/confluent-schema-registry-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
