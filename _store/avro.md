---
aid: avro
name: Apache Avro
description: Apache Avro is a data serialization system that provides rich data structures, a compact binary format, and container files for storing persistent data. Avro uses JSON for defining data types and protocols, and serializes data in a compact binary format.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Big Data
  - Binary Format
  - Data Serialization
  - Schema Evolution
url: https://raw.githubusercontent.com/api-evangelist/avro/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: avro:avro-schema
    name: Apache Avro Schema Format
    description: JSON Schema for validating Apache Avro schema definitions. Covers all Avro types including primitive types (null, boolean, int, long, float, double, bytes, string), complex types (records, enums, arrays, maps, unions, fixed), logical types, and schema evolution features like aliases and default values.
    humanURL: https://avro.apache.org/docs/current/specification/
    tags:
      - Data Serialization
      - JSON
      - Schema
      - Schema Evolution
    properties:
      - type: Documentation
        url: https://avro.apache.org/docs/current/specification/
      - type: JSONSchema
        url: json-schema/avro-schema.yml
common:
  - type: Website
    url: https://avro.apache.org/
  - type: Documentation
    url: https://avro.apache.org/docs/
  - type: GitHub Organization
    url: https://github.com/apache/avro
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/avro/refs/heads/main/rules/avro-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/avro/refs/heads/main/vocabulary/avro-vocabulary.yaml
  - type: Features
    data:
      - name: Schema-First Design
        description: Avro requires schemas to be defined in JSON before serialization, enabling strong typing and schema validation.
      - name: Schema Evolution
        description: Avro supports backward, forward, and full schema compatibility through aliases, defaults, and type promotions.
      - name: Compact Binary Format
        description: Avro serializes data in a compact binary format without field names, reducing payload size significantly.
      - name: Rich Type System
        description: Supports primitive types, complex types (records, enums, arrays, maps, unions, fixed), and logical types (date, time, decimal, UUID).
      - name: Language Agnostic
        description: Official implementations in Java, Python, C, C++, C#, PHP, Ruby, and Rust with broad ecosystem support.
      - name: Container Files
        description: Avro Object Container Files (OCF) embed the schema with the data for self-describing data files.
      - name: RPC Support
        description: Avro defines an RPC protocol mechanism using schemas for both request and response messages.
      - name: Kafka Native Format
        description: Apache Kafka ecosystem uses Avro as a primary serialization format with the Confluent Schema Registry.
  - type: UseCases
    data:
      - name: Event Streaming
        description: Serialize Kafka events with Avro schemas stored in a Schema Registry for high-throughput data pipelines.
      - name: Data Lake Storage
        description: Store large datasets in Avro container files in Hadoop-compatible storage with embedded schema metadata.
      - name: Schema Registry Integration
        description: Use Confluent Schema Registry to manage schema versions and enforce compatibility across producers and consumers.
      - name: Inter-Service Messaging
        description: Define message contracts between microservices using Avro schemas for type-safe data exchange.
      - name: Batch Data Processing
        description: Process large volumes of structured data with Apache Spark, Hive, or Flink using Avro as the interchange format.
  - type: Integrations
    data:
      - name: Apache Kafka
        description: Native serialization format for Kafka messages via the Confluent Schema Registry and Kafka clients.
      - name: Apache Spark
        description: Spark SQL and DataFrames support reading and writing Avro files natively.
      - name: Apache Hive
        description: Hive tables can be backed by Avro container files with schema stored in the Hive Metastore.
      - name: Confluent Schema Registry
        description: Centralized schema management service for validating and evolving Avro schemas in Kafka ecosystems.
      - name: Apache Flink
        description: Flink supports Avro for serialization and deserialization of streaming data.
      - name: Apache Hadoop
        description: Avro is a native storage format supported by the Hadoop ecosystem for distributed processing.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
