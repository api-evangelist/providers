---
aid: data-format
name: Data Format
description: Data Format covers the syntactic conventions used to represent, exchange, and persist information. The landscape spans text formats (JSON, XML, YAML, CSV, TOML), binary formats (Protocol Buffers, Avro, Parquet, ORC, MessagePack, BSON, CBOR, Arrow), and schema languages and IDLs that govern how those formats are validated and evolved.
type: Topic
xType: topic
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Binary Formats
  - Data Format
  - Data Serialization
  - Interchange
  - Text Formats
created: '2025-01-01'
modified: '2026-04-30'
url: https://raw.githubusercontent.com/api-evangelist/data-format/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis: []
common:
  - url: https://www.json.org/
    name: JSON
    type: Reference
    description: JavaScript Object Notation, the dominant text-based interchange format.
  - url: https://www.w3.org/XML/
    name: XML
    type: Reference
    description: W3C Extensible Markup Language for hierarchical document data.
  - url: https://yaml.org/
    name: YAML
    type: Reference
    description: Human-readable serialization format used for configuration and data.
  - url: https://datatracker.ietf.org/doc/html/rfc4180
    name: CSV (RFC 4180)
    type: Reference
    description: Comma-separated values format defined by IETF RFC 4180.
  - url: https://toml.io/
    name: TOML
    type: Reference
    description: Tom's Obvious Minimal Language for configuration files.
  - url: https://protobuf.dev/
    name: Protocol Buffers
    type: Reference
    description: Google's binary serialization with strongly typed schemas.
  - url: https://avro.apache.org/
    name: Apache Avro
    type: Reference
    description: Schema-driven binary serialization used in big data pipelines.
  - url: https://parquet.apache.org/
    name: Apache Parquet
    type: Reference
    description: Columnar storage format optimized for analytical workloads.
  - url: https://orc.apache.org/
    name: Apache ORC
    type: Reference
    description: Optimized Row Columnar file format for Hadoop workloads.
  - url: https://arrow.apache.org/
    name: Apache Arrow
    type: Reference
    description: In-memory columnar format for zero-copy analytics.
  - url: https://msgpack.org/
    name: MessagePack
    type: Reference
    description: Compact binary serialization that aims to be JSON-compatible.
  - url: https://bsonspec.org/
    name: BSON
    type: Reference
    description: Binary JSON format used by MongoDB.
  - url: https://cbor.io/
    name: CBOR
    type: Reference
    description: Concise Binary Object Representation defined by RFC 8949.
  - url: https://json-schema.org/
    name: JSON Schema
    type: Reference
    description: Schema language for validating JSON documents.
  - url: https://www.w3.org/XML/Schema
    name: XML Schema
    type: Reference
    description: W3C XML Schema Definition language for XML validation.
  - url: vocabulary/data-format-vocabulary.yml
    name: Vocabulary
    type: Vocabulary
    description: Vocabulary of data format and serialization concepts.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
