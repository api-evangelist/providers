---
aid: scala
name: Scala
description: A topic collection covering the Scala programming language ecosystem, including its standard library, key frameworks, and widely-used libraries. Scala is a strongly-typed, JVM-based language that blends object-oriented and functional programming, widely used in big data engineering, distributed systems, fintech, and backend development. The ecosystem includes the Akka actor framework, Play web framework, ZIO effect system, Cats typeclass library, http4s, Slick, sbt build tool, and Spark. Scala 3.8 is the current major version (January 2026).
image: https://www.scala-lang.org/resources/img/scala-logo.png
tags:
  - Big Data
  - Distributed Systems
  - Functional Programming
  - JVM
  - Programming Language
  - Scala
  - Scala 3
  - Type Safety
type: Index
created: '2024-01-15'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: scala:scala-lang
    name: Scala Standard Library API
    description: The Scala Standard Library provides core data structures, collections, concurrent primitives, and runtime utilities for Scala programs on the JVM, JavaScript (Scala.js), and Native (Scala Native) runtimes. Scala 3.8 shipped in January 2026 with a JDK 17 baseline.
    tags:
      - Core
      - JVM
      - Programming Language
      - Scala
      - Standard Library
    humanURL: https://www.scala-lang.org/api/current/
    properties:
      - type: Documentation
        url: https://www.scala-lang.org/api/current/
      - type: Website
        url: https://www.scala-lang.org/
      - type: GitHub
        url: https://github.com/scala/scala
  - aid: scala:akka
    name: Akka API
    description: Akka is a toolkit for building highly concurrent, distributed, and fault-tolerant applications on the JVM using the Actor model. Includes Akka Actors, Akka HTTP, Akka Streams, and Akka Cluster.
    tags:
      - Actors
      - Concurrent
      - Distributed Systems
      - HTTP
      - Reactive
      - Scala
    humanURL: https://doc.akka.io/
    properties:
      - type: Documentation
        url: https://doc.akka.io/docs/akka/current/
      - type: API Documentation
        url: https://doc.akka.io/api/akka/current/akka/
      - type: GitHub
        url: https://github.com/akka/akka
  - aid: scala:akka-http
    name: Akka HTTP API
    description: Akka HTTP provides a full server- and client-side HTTP stack built on Akka Streams. Offers high-throughput, non-blocking HTTP handling with a powerful Scala DSL for routing and marshalling.
    tags:
      - Akka
      - Client
      - HTTP
      - Reactive
      - Scala
      - Server
    humanURL: https://doc.akka.io/docs/akka-http/current/
    properties:
      - type: Documentation
        url: https://doc.akka.io/docs/akka-http/current/
      - type: API Documentation
        url: https://doc.akka.io/api/akka-http/current/akka/http/
      - type: GitHub
        url: https://github.com/akka/akka-http
  - aid: scala:play-framework
    name: Play Framework API
    description: Play is a reactive web framework for Scala (and Java) built on Akka and Akka Streams. Provides MVC routing, template engine, WS client, and reactive database integrations for building web applications and REST APIs.
    tags:
      - MVC
      - Reactive
      - REST
      - Scala
      - Web Framework
    humanURL: https://www.playframework.com/
    properties:
      - type: Documentation
        url: https://www.playframework.com/documentation/latest/Home
      - type: API Documentation
        url: https://www.playframework.com/documentation/latest/api/scala/
      - type: GitHub
        url: https://github.com/playframework/playframework
  - aid: scala:zio
    name: ZIO API
    description: ZIO is a type-safe, composable library for asynchronous and concurrent programming in Scala. Provides a purely functional effect system with structured concurrency, resource management, and a rich ecosystem of ZIO-based libraries (ZIO HTTP, ZIO Kafka, ZIO Quill, ZIO Schema).
    tags:
      - Async
      - Concurrent
      - Effect System
      - Functional Programming
      - Scala
      - Type Safe
    humanURL: https://zio.dev/
    properties:
      - type: Documentation
        url: https://zio.dev/overview/
      - type: API Documentation
        url: https://javadoc.io/doc/dev.zio/zio_3/latest/
      - type: GitHub
        url: https://github.com/zio/zio
  - aid: scala:cats
    name: Cats API
    description: Cats is a lightweight, modular library for functional programming in Scala. It provides type class abstractions (Functor, Monad, Applicative, etc.) and their instances for standard library types. The most widely used functional programming library in the Scala ecosystem (56% adoption).
    tags:
      - Category Theory
      - Functional Programming
      - Scala
      - Type Classes
    humanURL: https://typelevel.org/cats/
    properties:
      - type: Documentation
        url: https://typelevel.org/cats/
      - type: API Documentation
        url: https://typelevel.org/cats/api/
      - type: GitHub
        url: https://github.com/typelevel/cats
  - aid: scala:http4s
    name: http4s API
    description: http4s is a typeful, functional, streaming HTTP library for Scala built on cats-effect and fs2. Provides server and client abstractions with backends for Blaze, Ember, Jetty, and Tomcat. Second most popular HTTP library in the Scala ecosystem (45% adoption).
    tags:
      - Cats Effect
      - Functional Programming
      - HTTP
      - Scala
      - Streaming
    humanURL: https://http4s.org/
    properties:
      - type: Documentation
        url: https://http4s.org/v1/docs/
      - type: GitHub
        url: https://github.com/http4s/http4s
  - aid: scala:slick
    name: Slick API
    description: Slick is Functional Relational Mapping (FRM) for Scala — a type-safe, composable database access library that lets you work with stored data almost as if you were using Scala collections. Supports PostgreSQL, MySQL, H2, SQLite, and more.
    tags:
      - Database
      - Functional
      - ORM
      - Scala
      - SQL
    humanURL: https://scala-slick.org/
    properties:
      - type: Documentation
        url: https://scala-slick.org/doc/stable/
      - type: API Documentation
        url: https://scala-slick.org/doc/stable/api/
      - type: GitHub
        url: https://github.com/slick/slick
  - aid: scala:circe
    name: Circe API
    description: Circe is the most widely used JSON library for Scala, built on top of Cats. Provides encoding, decoding, traversal, and transformation of JSON values with automatic derivation support for case classes and sealed traits.
    tags:
      - Cats
      - Functional Programming
      - JSON
      - Parsing
      - Scala
      - Serialization
    humanURL: https://circe.github.io/circe/
    properties:
      - type: Documentation
        url: https://circe.github.io/circe/
      - type: API Documentation
        url: https://circe.github.io/circe/api/
      - type: GitHub
        url: https://github.com/circe/circe
  - aid: scala:apache-spark
    name: Apache Spark API
    description: Apache Spark is the dominant big data processing framework in the Scala ecosystem. Its API enables large-scale data processing, SQL analytics, streaming, and machine learning across distributed clusters.
    tags:
      - Big Data
      - Data Engineering
      - Distributed Systems
      - Machine Learning
      - Scala
      - Spark
    humanURL: https://spark.apache.org/docs/latest/api/scala/
    properties:
      - type: Documentation
        url: https://spark.apache.org/docs/latest/api/scala/
      - type: REST API
        url: https://spark.apache.org/docs/latest/monitoring.html#rest-api
      - type: GitHub
        url: https://github.com/apache/spark
  - aid: scala:sbt
    name: sbt Build Tool
    description: sbt (Simple Build Tool) is the dominant build tool in the Scala ecosystem (90% adoption). Its Server API enables IDE integration via the Build Server Protocol (BSP). sbt 2.0 release candidates show up to 41% faster startup.
    tags:
      - Build Tool
      - Developer Tools
      - Scala
    humanURL: https://www.scala-sbt.org/
    properties:
      - type: Documentation
        url: https://www.scala-sbt.org/1.x/docs/
      - type: GitHub
        url: https://github.com/sbt/sbt
common:
  - type: Website
    url: https://www.scala-lang.org/
    name: Scala Language Website
  - type: Blog
    url: https://www.scala-lang.org/blog/
    name: Scala Official Blog
  - type: Documentation
    url: https://docs.scala-lang.org/
    name: Scala Documentation
  - type: Forum
    url: https://users.scala-lang.org/
    name: Scala Users Forum
  - type: GitHub
    url: https://github.com/scala
    name: Scala GitHub Organization
  - type: Newsletter
    url: https://scalatimes.com/
    name: Scala Times Newsletter
  - type: Social
    url: https://twitter.com/scala_lang
    name: Scala Twitter
  - type: Community
    url: https://discord.gg/scala
    name: Scala Discord
  - type: JSONSchema
    url: https://github.com/api-evangelist/scala/blob/main/json-schema/scala-library-schema.json
    name: Scala Library JSON Schema
  - type: JSONStructure
    url: https://github.com/api-evangelist/scala/blob/main/json-structure/scala-library-structure.json
    name: Scala Library JSON Structure
  - type: JSONLDContext
    url: https://github.com/api-evangelist/scala/blob/main/json-ld/scala-context.jsonld
    name: Scala JSON-LD Context
  - type: Vocabulary
    url: https://github.com/api-evangelist/scala/blob/main/vocabulary/scala-vocabulary.yml
    name: Scala Vocabulary
  - type: Examples
    url: https://github.com/api-evangelist/scala/blob/main/examples/scala-zio-http-example.json
    name: ZIO HTTP Server Example
  - type: Examples
    url: https://github.com/api-evangelist/scala/blob/main/examples/scala-cats-effect-http4s-example.json
    name: http4s REST API with cats-effect Example
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
