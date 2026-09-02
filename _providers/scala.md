---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-01'
api_count: 11
apis:
- description: The Scala Standard Library provides core data structures, collections, concurrent primitives, and runtime utilities for Scala programs on the JVM, JavaScript (Scala.js), and Native (Scala Native) runt
  name: Scala Standard Library API
  slug: scala-lang
- description: Akka is a toolkit for building highly concurrent, distributed, and fault-tolerant applications on the JVM using the Actor model. Includes Akka Actors, Akka HTTP, Akka Streams, and Akka Cluster.
  name: Akka API
  slug: akka
- description: Akka HTTP provides a full server- and client-side HTTP stack built on Akka Streams. Offers high-throughput, non-blocking HTTP handling with a powerful Scala DSL for routing and marshalling.
  name: Akka HTTP API
  slug: akka-http
- description: Play is a reactive web framework for Scala (and Java) built on Akka and Akka Streams. Provides MVC routing, template engine, WS client, and reactive database integrations for building web applications
  name: Play Framework API
  slug: play-framework
- description: ZIO is a type-safe, composable library for asynchronous and concurrent programming in Scala. Provides a purely functional effect system with structured concurrency, resource management, and a rich eco
  name: ZIO API
  slug: zio
- description: 'Cats is a lightweight, modular library for functional programming in Scala. It provides type class abstractions (Functor, Monad, Applicative, etc.) and their instances for standard library types. The '
  name: Cats API
  slug: cats
- description: http4s is a typeful, functional, streaming HTTP library for Scala built on cats-effect and fs2. Provides server and client abstractions with backends for Blaze, Ember, Jetty, and Tomcat. Second most p
  name: http4s API
  slug: http4s
- description: Slick is Functional Relational Mapping (FRM) for Scala — a type-safe, composable database access library that lets you work with stored data almost as if you were using Scala collections. Supports Pos
  name: Slick API
  slug: slick
- description: Circe is the most widely used JSON library for Scala, built on top of Cats. Provides encoding, decoding, traversal, and transformation of JSON values with automatic derivation support for case classes
  name: Circe API
  slug: circe
- description: Apache Spark is the dominant big data processing framework in the Scala ecosystem. Its API enables large-scale data processing, SQL analytics, streaming, and machine learning across distributed cluste
  name: Apache Spark API
  slug: apache-spark
- description: sbt (Simple Build Tool) is the dominant build tool in the Scala ecosystem (90% adoption). Its Server API enables IDE integration via the Build Server Protocol (BSP). sbt 2.0 release candidates show up
  name: sbt Build Tool
  slug: sbt
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scala-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scala-lang.org/
- group: company
  title: ''
  type: Blog
  url: https://www.scala-lang.org/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scala-lang.org/
- group: operate
  title: ''
  type: Forums
  url: https://users.scala-lang.org/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/scala
- group: company
  title: ''
  type: Newsletter
  url: https://scalatimes.com/
- group: other
  title: ''
  type: Social
  url: https://twitter.com/scala_lang
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/scala
- group: docs
  title: ''
  type: JSONSchema
  url: https://github.com/api-evangelist/scala/blob/main/json-schema/scala-library-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://github.com/api-evangelist/scala/blob/main/json-structure/scala-library-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://github.com/api-evangelist/scala/blob/main/json-ld/scala-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://github.com/api-evangelist/scala/blob/main/vocabulary/scala-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: https://github.com/api-evangelist/scala/blob/main/examples/scala-zio-http-example.json
- group: build
  title: ''
  type: Examples
  url: https://github.com/api-evangelist/scala/blob/main/examples/scala-cats-effect-http4s-example.json
created: '2024-01-15'
description: A topic collection covering the Scala programming language ecosystem, including its standard library, key frameworks, and widely-used libraries. Scala is a strongly-typed, JVM-based language that blends object-oriented and functional programming, widely used in big data engineering, distributed systems, fintech, and backend development. The ecosystem includes the Akka actor framework, Play web framework, ZIO effect system, Cats typeclass library, http4s, Slick, sbt build tool, and Spark. Scala 3.8 is the current major version (January 2026).
examples:
- key_count: 1
  name: Scala Cats Effect Http4S Example
  slug: scala-cats-effect-http4s-example
- key_count: 1
  name: Scala Zio Http Example
  slug: scala-zio-http-example
finops:
- name: Scala Finops
  service_category: API
  slug: scala-finops
image: https://www.scala-lang.org/resources/img/scala-logo.png
json_schemas:
- name: Scala Library
  property_count: 15
  slug: scala-library
json_structures:
- name: Scala Library Structure
  property_count: 0
  slug: scala-library-structure
jsonld:
- class_count: 34
  name: Scala Context
  property_count: 1
  slug: scala-context
layout: provider
modified: '2026-05-02'
name: Scala
nav: Providers
network: true
overview: 'Scala publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Big Data, Distributed Systems, Functional Programming, JVM, and Programming Language.


  The Scala catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Scala''s developer surface includes engineering blog, documentation, GitHub presence, code examples, and 11 more developer resources.'
plans:
- name: Scala Plans Pricing
  plan_count: 3
  slug: scala-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Scala Rate Limits
  slug: scala-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Scala API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: scala-jsonschema-spectral-rules
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 17.3
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 13.2
  previous_composite: 23.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scala/refs/heads/main/screenshots/scala-2026-06-20T193449.png
security:
- kind: domain-security
  name: Scala Domain Security
  slug: scala-domain-security
  summary_line: TLSv1.3 · DMARC
slug: scala
tags:
- Big Data
- Distributed Systems
- Functional Programming
- JVM
- Programming Language
- Scala
- Scala 3
- Type Safety
website: https://www.scala-lang.org/
---
