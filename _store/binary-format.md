---
aid: binary-format
name: Binary Format
description: Binary format refers to data encoding and serialization methods that use binary rather than text representations, including formats like Protocol Buffers, MessagePack, Avro, Thrift, CBOR, and others used in APIs and data storage systems for efficiency. Binary formats offer significant advantages over text-based formats in terms of size, parsing speed, and type safety.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Binary Format
  - Data Encoding
  - Protocol Buffers
  - Serialization
  - MessagePack
  - Apache Avro
  - Apache Thrift
  - CBOR
url: https://raw.githubusercontent.com/api-evangelist/binary-format/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
apis: []
common:
  - type: Reference
    url: https://protobuf.dev
  - type: Reference
    url: https://msgpack.org
  - type: Reference
    url: https://avro.apache.org
  - type: Reference
    url: https://thrift.apache.org
  - type: Reference
    url: https://cbor.io
  - type: Features
    data:
      - name: Protocol Buffers (protobuf)
        description: Google's language-neutral, platform-neutral extensible serialization format with schema-first design.
      - name: MessagePack
        description: Efficient binary serialization format that is JSON-compatible with smaller encoding size.
      - name: Apache Avro
        description: Row-oriented remote procedure call and data serialization framework developed in Apache Hadoop.
      - name: Apache Thrift
        description: Facebook-originated framework for scalable cross-language services development with binary transport.
      - name: CBOR (Concise Binary Object Representation)
        description: IETF RFC 8949 binary data format based on JSON data model with compact encoding.
      - name: FlatBuffers
        description: Google's cross-platform serialization library for memory-efficient access without parsing.
      - name: Cap'n Proto
        description: Ultra-fast data interchange format and RPC system with zero-copy reads.
      - name: Apache Arrow
        description: Cross-language columnar memory format for flat and hierarchical data.
  - type: UseCases
    data:
      - name: High-Performance API Communication
        description: Using binary serialization to reduce payload size and parsing overhead in API calls.
      - name: gRPC Service Definition
        description: Defining gRPC service contracts using Protocol Buffers IDL.
      - name: Event Streaming
        description: Encoding Kafka and event streaming messages using Avro with Schema Registry.
      - name: IoT Data Transmission
        description: Using compact binary formats like CBOR or MessagePack for bandwidth-constrained IoT devices.
      - name: Columnar Data Processing
        description: Using Apache Arrow for zero-copy analytics across language boundaries.
      - name: Microservice Communication
        description: Replacing JSON/XML with binary formats for internal microservice RPC efficiency.
  - type: Conformance
    data:
      - name: RFC 8949 - CBOR
        description: IETF standard for Concise Binary Object Representation.
        url: https://datatracker.ietf.org/doc/html/rfc8949
      - name: Protocol Buffers Language Guide
        description: Google's specification for Protocol Buffers schema definition language.
        url: https://protobuf.dev/programming-guides/proto3/
      - name: Apache Avro Specification
        description: Apache Software Foundation specification for the Avro serialization format.
        url: https://avro.apache.org/docs/current/specification/
  - type: Implementations
    data:
      - name: protoc
        description: Protocol Buffers compiler generating code from .proto schema files.
        url: https://grpc.io/docs/protoc-installation/
      - name: avro-tools
        description: Apache Avro command-line tools for schema management and data conversion.
        url: https://avro.apache.org
      - name: msgpack-python
        description: Python library for MessagePack serialization and deserialization.
        url: https://pypi.org/project/msgpack/
      - name: thrift compiler
        description: Apache Thrift IDL compiler for generating language-specific service stubs.
        url: https://thrift.apache.org
  - type: Vocabulary
    data:
      - term: Schema
        definition: Formal definition of data structure used by binary format encoders/decoders.
      - term: Serialization
        definition: Converting in-memory data structures into binary byte sequences for transmission or storage.
      - term: Deserialization
        definition: Reconstructing in-memory data structures from binary byte sequences.
      - term: IDL
        definition: Interface Definition Language used to define data schemas and service interfaces.
      - term: Wire Format
        definition: The binary encoding used when data is transmitted over a network.
      - term: Schema Evolution
        definition: Ability to add, remove, or modify schema fields while maintaining backward/forward compatibility.
      - term: Varint
        definition: Variable-length integer encoding used by Protocol Buffers for compact integer storage.
      - term: Encoding
        definition: Process of converting data to binary representation according to a format specification.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
