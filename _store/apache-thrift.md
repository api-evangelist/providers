---
aid: apache-thrift
name: Apache Thrift
description: Apache Thrift is a software framework for scalable cross-language services development. It provides an interface definition language (IDL) and code generation engine for building RPC services that work efficiently across C++, Java, Python, PHP, Ruby, Erlang, Go, JavaScript, Node.js, Haskell, C#, Cocoa, Delphi, and many more languages. Originally developed at Facebook, Thrift is now an Apache Software Foundation top-level project used for high-performance internal microservices and APIs.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Code Generation
  - Cross-Language
  - IDL
  - RPC
  - Serialization
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-thrift/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-thrift:apache-thrift-idl
    name: Apache Thrift IDL
    description: The Thrift Interface Definition Language (IDL) is used to define data types and service interfaces in a language-neutral format. A .thrift file defines structs, enums, exceptions, typedefs, constants, and services with typed method signatures. The thrift compiler generates client and server code from .thrift files for over 20 target languages including Java, Python, C++, Go, JavaScript, PHP, Ruby, Erlang, and Haskell.
    humanURL: https://thrift.apache.org/docs/idl.html
    tags:
      - IDL
      - Code Generation
      - RPC
      - Cross-Language
    properties:
      - type: Documentation
        url: https://thrift.apache.org/docs/idl.html
      - type: Documentation
        url: https://thrift.apache.org/docs/types.html
      - type: JSONSchema
        url: json-schema/thrift-idl.yml
  - aid: apache-thrift:apache-thrift-server-api
    name: Apache Thrift Server API
    description: The Thrift Server API provides server implementations for hosting Thrift services including TSimpleServer (single-threaded), TThreadedServer, TThreadPoolServer, and TNonblockingServer (async I/O). Thrift supports multiple transport protocols (TBinaryProtocol, TCompactProtocol, TJSONProtocol) over various transports (TSocket, TFramedTransport, TFileTransport, TZlibTransport) enabling flexible deployment configurations.
    humanURL: https://thrift.apache.org/docs/concepts.html
    tags:
      - Server
      - RPC
      - Protocol
      - Transport
    properties:
      - type: Documentation
        url: https://thrift.apache.org/docs/concepts.html
common:
  - type: GitHubRepository
    url: https://github.com/apache/thrift
  - type: Documentation
    url: https://thrift.apache.org/docs/
  - type: Portal
    url: https://thrift.apache.org/
  - type: GettingStarted
    url: https://thrift.apache.org/tutorial/
  - type: ReleaseNotes
    url: https://github.com/apache/thrift/releases
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: SDK
    url: https://pypi.org/project/thrift/
    title: Python Package
  - type: SDK
    url: https://search.maven.org/search?q=org.apache.thrift
    title: Java Maven Package
  - type: Features
    data:
      - name: Cross-Language Code Generation
        description: Generate client and server stubs for 20+ programming languages from a single IDL file.
      - name: Binary Serialization
        description: Compact binary serialization (TCompactProtocol) for high-performance inter-service communication.
      - name: Multiple Transports
        description: TSocket, TFramedTransport, TFileTransport, TZlibTransport, and TMemoryBuffer transports.
      - name: Multiple Protocols
        description: TBinaryProtocol, TCompactProtocol, TJSONProtocol, and TSimpleJSONProtocol serialization formats.
      - name: Async Server Support
        description: Non-blocking async server (TNonblockingServer) for high-throughput service deployments.
      - name: Versioned Schema Evolution
        description: Optional and default fields enable backward-compatible schema evolution across service versions.
  - type: UseCases
    data:
      - name: Internal Microservices
        description: High-performance binary RPC between internal microservices in polyglot environments.
      - name: Cross-Language APIs
        description: Type-safe APIs that work identically across Java, Python, C++, and other languages.
      - name: Distributed Systems
        description: Service mesh and distributed system communication with efficient binary serialization.
  - type: Integrations
    data:
      - name: Apache Cassandra
        description: Cassandra uses Thrift (legacy) and CQL for client communication.
      - name: Apache HBase
        description: HBase Thrift gateway for non-Java clients to access HBase.
      - name: Apache Hadoop
        description: Hive Thrift server provides JDBC/ODBC access to Hive via Thrift protocol.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
