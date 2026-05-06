---
aid: kotlin
name: Kotlin
description: Kotlin is a modern, concise, and safe programming language for the JVM, Android, and multiplatform development. It is developed by JetBrains and provides full interoperability with Java. Kotlin's standard library and ecosystem offer rich APIs for building applications across all platforms.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Android
  - JVM
  - Kotlin
  - Multiplatform
  - Programming Language
url: https://raw.githubusercontent.com/api-evangelist/kotlin/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kotlin:stdlib
    name: Kotlin Standard Library API
    description: Core Kotlin standard library with collections, I/O, and utility functions.
    humanURL: https://kotlinlang.org/api/latest/jvm/stdlib/
    tags:
      - Collections
      - Core
      - Stdlib
    properties:
      - type: Documentation
        url: https://kotlinlang.org/api/latest/jvm/stdlib/
      - type: Reference
        url: https://kotlinlang.org/api/latest/jvm/stdlib/alltypes/
  - aid: kotlin:coroutines
    name: Kotlin Coroutines API
    description: Library support for Kotlin coroutines with async/await patterns.
    humanURL: https://kotlinlang.org/api/kotlinx.coroutines/
    tags:
      - Async
      - Concurrency
      - Coroutines
    properties:
      - type: Documentation
        url: https://kotlinlang.org/docs/coroutines-overview.html
      - type: Reference
        url: https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/
common:
  - type: Website
    url: https://kotlinlang.org/
  - type: Documentation
    url: https://kotlinlang.org/docs/home.html
  - type: Blog
    url: https://blog.jetbrains.com/kotlin/
  - type: GitHub Organization
    url: https://github.com/JetBrains/kotlin
  - type: Community
    url: https://kotlinlang.org/community/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
