---
aid: retrofit
name: Retrofit
description: Retrofit is a type-safe HTTP client for Android and the JVM (Java and Kotlin) built by Square, turning HTTP API interfaces into callable Java objects with annotation-based configuration and pluggable serialization. Retrofit is built on top of OkHttp and supports synchronous/asynchronous execution, JSON/XML/Protobuf converters, RxJava adapters, and Kotlin coroutines. Current stable version is 3.0.0.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Android
  - HTTP Client
  - Java
  - Kotlin
  - Library
  - Mobile
  - Open Source
  - SDK
  - Square
url: https://raw.githubusercontent.com/api-evangelist/retrofit/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: retrofit:retrofit-core
    name: Retrofit
    description: Retrofit is a type-safe HTTP client for the JVM that turns annotated Java/Kotlin interfaces into HTTP API calls. Supports all HTTP methods via annotations. Built on OkHttp with support for synchronous Call, RxJava, Java 8 CompletableFuture, and Kotlin coroutines.
    humanURL: https://square.github.io/retrofit/
    tags:
      - Android
      - HTTP Client
      - Java
      - Kotlin
      - Open Source
    properties:
      - type: Documentation
        url: https://square.github.io/retrofit/
      - type: GitHub
        url: https://github.com/square/retrofit
      - type: Changelog
        url: https://github.com/square/retrofit/blob/trunk/CHANGELOG.md
      - type: JavaDoc
        url: https://square.github.io/retrofit/2.x/retrofit/
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/retrofit/refs/heads/main/json-schema/retrofit-library-schema.json
  - aid: retrofit:retrofit-converters
    name: Retrofit Converters
    description: Pluggable serialization converters for Retrofit supporting Gson, Moshi, Jackson, Kotlinx Serialization, JAXB, Protocol Buffers (Wire), SimpleXML, and Scalars.
    humanURL: https://square.github.io/retrofit/#converters
    tags:
      - Converters
      - Gson
      - Jackson
      - Moshi
      - Protobuf
      - Serialization
    properties:
      - type: Documentation
        url: https://square.github.io/retrofit/#converters
      - type: GitHub
        url: https://github.com/square/retrofit/tree/trunk/retrofit-converters
  - aid: retrofit:retrofit-adapters
    name: Retrofit Call Adapters
    description: Pluggable call adapters that allow Retrofit interfaces to return RxJava Observables (v1, v2, v3), Java 8 CompletableFuture, Guava ListenableFuture, and Scala Future types.
    humanURL: https://square.github.io/retrofit/#call-adapters
    tags:
      - Adapters
      - Async
      - Java 8
      - RxJava
      - Scala
    properties:
      - type: Documentation
        url: https://square.github.io/retrofit/#call-adapters
      - type: GitHub
        url: https://github.com/square/retrofit/tree/trunk/retrofit-adapters
  - aid: retrofit:retrofit-mock
    name: Retrofit Mock
    description: Provides behavior-simulating implementations of Retrofit interfaces for local testing without requiring a network connection.
    humanURL: https://github.com/square/retrofit/tree/trunk/retrofit-mock
    tags:
      - Mock
      - Testing
    properties:
      - type: GitHub
        url: https://github.com/square/retrofit/tree/trunk/retrofit-mock
common:
  - type: Website
    url: https://square.github.io/retrofit/
  - type: Documentation
    url: https://square.github.io/retrofit/
  - type: GitHub
    url: https://github.com/square/retrofit
  - type: GitHubOrganization
    url: https://github.com/square
  - type: Changelog
    url: https://github.com/square/retrofit/blob/trunk/CHANGELOG.md
  - type: Issues
    url: https://github.com/square/retrofit/issues
  - type: Maven
    url: https://search.maven.org/artifact/com.squareup.retrofit2/retrofit
  - type: License
    url: https://github.com/square/retrofit/blob/trunk/LICENSE.txt
  - type: JavaDoc
    url: https://square.github.io/retrofit/2.x/retrofit/
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/retrofit/refs/heads/main/vocabulary/retrofit-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
