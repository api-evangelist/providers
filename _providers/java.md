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
  scored_at: '2026-09-02'
api_count: 9
apis:
- description: Core Java SE API including fundamental classes and utilities for building Java applications, including the java.lang, java.util, java.io, and other foundational packages.
  name: Java Core API
  slug: java-core-api
- description: Interfaces and classes for storing and manipulating groups of objects including List, Set, Map, and Queue implementations.
  name: Java Collections Framework
  slug: java-collections-framework
- description: Input and output through data streams, serialization and the file system using the java.io package.
  name: Java I/O API
  slug: java-io-api
- description: Non-blocking I/O operations for buffers, channels, selectors, and asynchronous file system access.
  name: Java NIO API
  slug: java-nio-api
- description: APIs for networking applications including HTTP, sockets, and URLs.
  name: Java Networking API
  slug: java-networking-api
- description: Utilities for concurrent programming including executors, thread pools, locks, atomic variables, and concurrent collections.
  name: Java Concurrency API
  slug: java-concurrency-api
- description: API for connecting to relational databases and executing SQL queries from Java applications.
  name: Java Database Connectivity (JDBC)
  slug: jdbc-api
- description: Examine and modify the runtime behavior of applications by inspecting classes, methods, fields, and annotations.
  name: Java Reflection API
  slug: java-reflection-api
- description: Functional-style operations on streams of elements including map, filter, reduce, and collect operations.
  name: Java Stream API
  slug: java-stream-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/java-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.java.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/java/javase/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.java/learn/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openjdk
- group: commercial
  title: ''
  type: License
  url: https://www.oracle.com/downloads/licenses/javase-license1.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: operate
  title: ''
  type: Support
  url: https://www.oracle.com/java/technologies/javase/support-roadmap.html
created: '2024-01-01'
description: Java is a high-level, class-based, object-oriented programming language developed by Sun Microsystems and now stewarded by Oracle. The Java Standard Edition (SE) platform provides a comprehensive set of APIs and class libraries for building cross-platform applications. Key APIs include Collections, Concurrency, I/O, NIO, Networking, JDBC, Reflection, and Streams. Java is the foundation for the Jakarta EE enterprise platform and is supported by an extensive ecosystem of open source projects, frameworks, and runtimes.
finops:
- name: Java Finops
  service_category: API
  slug: java-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/java.png
layout: provider
modified: '2026-04-28'
name: Java
nav: Providers
network: true
overview: 'Java publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise, Java, JVM, Object-Oriented, and Oracle.


  Java''s developer surface includes documentation, getting-started guide, support, and 5 more developer resources.'
plans:
- name: Java Plans Pricing
  plan_count: 3
  slug: java-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Java Rate Limits
  slug: java-rate-limits
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 17.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/java/refs/heads/main/screenshots/java-2026-06-20T183701.png
security:
- kind: domain-security
  name: Java Domain Security
  slug: java-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: java
tags:
- Enterprise
- Java
- JVM
- Object-Oriented
- Oracle
- Programming Language
website: https://www.java.com/
---
