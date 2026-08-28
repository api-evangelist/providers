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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: Retrofit is a type-safe HTTP client for the JVM that turns annotated Java/Kotlin interfaces into HTTP API calls. Supports all HTTP methods via annotations. Built on OkHttp with support for synchronous
  name: Retrofit
  slug: retrofit-core
- description: Pluggable serialization converters for Retrofit supporting Gson, Moshi, Jackson, Kotlinx Serialization, JAXB, Protocol Buffers (Wire), SimpleXML, and Scalars.
  name: Retrofit Converters
  slug: retrofit-converters
- description: Pluggable call adapters that allow Retrofit interfaces to return RxJava Observables (v1, v2, v3), Java 8 CompletableFuture, Guava ListenableFuture, and Scala Future types.
  name: Retrofit Call Adapters
  slug: retrofit-adapters
- description: Provides behavior-simulating implementations of Retrofit interfaces for local testing without requiring a network connection.
  name: Retrofit Mock
  slug: retrofit-mock
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://square.github.io/retrofit/
- group: docs
  title: ''
  type: Documentation
  url: https://square.github.io/retrofit/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/square/retrofit
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/square
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/square/retrofit/blob/trunk/CHANGELOG.md
- group: operate
  title: ''
  type: Issues
  url: https://github.com/square/retrofit/issues
- group: other
  title: ''
  type: Maven
  url: https://search.maven.org/artifact/com.squareup.retrofit2/retrofit
- group: commercial
  title: ''
  type: License
  url: https://github.com/square/retrofit/blob/trunk/LICENSE.txt
- group: other
  title: ''
  type: JavaDoc
  url: https://square.github.io/retrofit/2.x/retrofit/
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/retrofit/refs/heads/main/vocabulary/retrofit-vocabulary.yml
created: '2026-03-27'
description: Retrofit is a type-safe HTTP client for Android and the JVM (Java and Kotlin) built by Square, turning HTTP API interfaces into callable Java objects with annotation-based configuration and pluggable serialization. Retrofit is built on top of OkHttp and supports synchronous/asynchronous execution, JSON/XML/Protobuf converters, RxJava adapters, and Kotlin coroutines. Current stable version is 3.0.0.
finops:
- name: Retrofit Finops
  service_category: API
  slug: retrofit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/retrofit.png
json_schemas:
- name: Retrofit Library
  property_count: 10
  slug: retrofit-library
json_structures:
- name: Retrofit Library Structure
  property_count: 0
  slug: retrofit-library-structure
jsonld:
- class_count: 11
  name: Retrofit Context
  property_count: 4
  slug: retrofit-context
layout: provider
modified: '2026-05-02'
name: Retrofit
nav: Providers
network: true
overview: 'Retrofit publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Android, HTTP Client, Java, Kotlin, and Library.


  The Retrofit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Retrofit''s developer surface includes documentation, GitHub presence, changelog, and 7 more developer resources.'
plans:
- name: Retrofit Plans Pricing
  plan_count: 3
  slug: retrofit-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Retrofit Rate Limits
  slug: retrofit-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Retrofit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: retrofit-jsonschema-spectral-rules
score:
  band: emerging
  composite: 18.0
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 18.7
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 18.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/retrofit/refs/heads/main/screenshots/retrofit-2026-06-20T193038.png
slug: retrofit
tags:
- Android
- HTTP Client
- Java
- Kotlin
- Library
- Mobile
- Open-Source
- SDK
- Square
website: https://square.github.io/retrofit/
---
