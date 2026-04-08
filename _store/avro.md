---
aid: avro
url: https://raw.githubusercontent.com/api-evangelist/avro/refs/heads/main/apis.yml
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
name: Apache Avro
tags:
- Apache
- Big Data
- Binary Format
- Data Serialization
- Schema Evolution
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Apache Avro is a data serialization system that provides rich data structures, a compact binary format, and container files for storing persistent data. Avro uses JSON for defining data types and protocols, and serializes data in a compact binary format.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

