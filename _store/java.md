---
aid: java
name: Java
description: Java is a high-level, class-based, object-oriented programming language developed by Sun Microsystems and now stewarded by Oracle. The Java Standard Edition (SE) platform provides a comprehensive set of APIs and class libraries for building cross-platform applications. Key APIs include Collections, Concurrency, I/O, NIO, Networking, JDBC, Reflection, and Streams. Java is the foundation for the Jakarta EE enterprise platform and is supported by an extensive ecosystem of open source projects, frameworks, and runtimes.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Enterprise
  - Java
  - JVM
  - Object-Oriented
  - Oracle
  - Programming Language
url: https://raw.githubusercontent.com/api-evangelist/java/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: java:java-core-api
    name: Java Core API
    description: Core Java SE API including fundamental classes and utilities for building Java applications, including the java.lang, java.util, java.io, and other foundational packages.
    humanURL: https://docs.oracle.com/en/java/javase/
    tags:
      - Core
      - Java
      - Standard Library
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/module-summary.html
      - type: Specification
        url: https://docs.oracle.com/javase/specs/
  - aid: java:java-collections-framework
    name: Java Collections Framework
    description: Interfaces and classes for storing and manipulating groups of objects including List, Set, Map, and Queue implementations.
    humanURL: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/package-summary.html
    tags:
      - Collections
      - Data Structures
      - Utilities
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/package-summary.html
      - type: Tutorial
        url: https://docs.oracle.com/javase/tutorial/collections/
  - aid: java:java-io-api
    name: Java I/O API
    description: Input and output through data streams, serialization and the file system using the java.io package.
    humanURL: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/package-summary.html
    tags:
      - Files
      - I/O
      - Streams
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/package-summary.html
  - aid: java:java-nio-api
    name: Java NIO API
    description: Non-blocking I/O operations for buffers, channels, selectors, and asynchronous file system access.
    humanURL: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/package-summary.html
    tags:
      - Async I/O
      - Buffers
      - NIO
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/package-summary.html
  - aid: java:java-networking-api
    name: Java Networking API
    description: APIs for networking applications including HTTP, sockets, and URLs.
    humanURL: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/package-summary.html
    tags:
      - HTTP
      - Networking
      - Sockets
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/package-summary.html
      - type: Documentation
        url: https://docs.oracle.com/en/java/javase/21/docs/api/java.net.http/java/net/http/package-summary.html
  - aid: java:java-concurrency-api
    name: Java Concurrency API
    description: Utilities for concurrent programming including executors, thread pools, locks, atomic variables, and concurrent collections.
    humanURL: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/package-summary.html
    tags:
      - Concurrency
      - Multithreading
      - Parallel
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/package-summary.html
  - aid: java:jdbc-api
    name: Java Database Connectivity (JDBC)
    description: API for connecting to relational databases and executing SQL queries from Java applications.
    humanURL: https://docs.oracle.com/en/java/javase/21/docs/api/java.sql/java/sql/package-summary.html
    tags:
      - Database
      - JDBC
      - SQL
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/java/javase/21/docs/api/java.sql/module-summary.html
      - type: Specification
        url: https://jcp.org/en/jsr/detail?id=221
  - aid: java:java-reflection-api
    name: Java Reflection API
    description: Examine and modify the runtime behavior of applications by inspecting classes, methods, fields, and annotations.
    humanURL: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/package-summary.html
    tags:
      - Introspection
      - Metadata
      - Reflection
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/reflect/package-summary.html
  - aid: java:java-stream-api
    name: Java Stream API
    description: Functional-style operations on streams of elements including map, filter, reduce, and collect operations.
    humanURL: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/package-summary.html
    tags:
      - Functional
      - Lambda
      - Streams
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/package-summary.html
      - type: Tutorial
        url: https://docs.oracle.com/javase/tutorial/collections/streams/
common:
  - type: Website
    url: https://www.java.com/
  - type: Documentation
    url: https://docs.oracle.com/en/java/javase/
  - type: Getting Started
    url: https://dev.java/learn/
  - type: GitHub Organization
    url: https://github.com/openjdk
  - type: License
    url: https://www.oracle.com/downloads/licenses/javase-license1.html
  - type: Terms of Service
    url: https://www.oracle.com/legal/terms.html
  - type: Support
    url: https://www.oracle.com/java/technologies/javase/support-roadmap.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
