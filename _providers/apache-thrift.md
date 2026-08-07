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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: The Thrift Interface Definition Language (IDL) is used to define data types and service interfaces in a language-neutral format. A .thrift file defines structs, enums, exceptions, typedefs, constants,
  name: Apache Thrift IDL
  slug: apache-thrift-idl
- description: The Thrift Server API provides server implementations for hosting Thrift services including TSimpleServer (single-threaded), TThreadedServer, TThreadPoolServer, and TNonblockingServer (async I/O). Thr
  name: Apache Thrift Server API
  slug: apache-thrift-server-api
artifact_total: 20
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-thrift-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-thrift-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/thrift
- group: docs
  title: ''
  type: Documentation
  url: https://thrift.apache.org/docs/
- group: start
  title: ''
  type: Portal
  url: https://thrift.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://thrift.apache.org/tutorial/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/thrift/releases
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: build
  title: Python Package
  type: SDKs
  url: https://pypi.org/project/thrift/
- group: build
  title: Java Maven Package
  type: SDKs
  url: https://search.maven.org/search?q=org.apache.thrift
created: '2026-03-16'
description: Apache Thrift is a software framework for scalable cross-language services development. It provides an interface definition language (IDL) and code generation engine for building RPC services that work efficiently across C++, Java, Python, PHP, Ruby, Erlang, Go, JavaScript, Node.js, Haskell, C#, Cocoa, Delphi, and many more languages. Originally developed at Facebook, Thrift is now an Apache Software Foundation top-level project used for high-performance internal microservices and APIs.
features:
- description: Generate client and server stubs for 20+ programming languages from a single IDL file.
  name: Cross-Language Code Generation
- description: Compact binary serialization (TCompactProtocol) for high-performance inter-service communication.
  name: Binary Serialization
- description: TSocket, TFramedTransport, TFileTransport, TZlibTransport, and TMemoryBuffer transports.
  name: Multiple Transports
- description: TBinaryProtocol, TCompactProtocol, TJSONProtocol, and TSimpleJSONProtocol serialization formats.
  name: Multiple Protocols
- description: Non-blocking async server (TNonblockingServer) for high-throughput service deployments.
  name: Async Server Support
- description: Optional and default fields enable backward-compatible schema evolution across service versions.
  name: Versioned Schema Evolution
finops:
- name: Apache Thrift Finops
  service_category: API
  slug: apache-thrift-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-thrift.png
integrations:
- description: Cassandra uses Thrift (legacy) and CQL for client communication.
  name: Apache Cassandra
- description: HBase Thrift gateway for non-Java clients to access HBase.
  name: Apache HBase
- description: Hive Thrift server provides JDBC/ODBC access to Hive via Thrift protocol.
  name: Apache Hadoop
layout: provider
modified: '2026-04-19'
name: Apache Thrift
nav: Providers
network: true
overview: 'Apache Thrift publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Code Generation, Cross-Language, IDL, RPC, and Serialization.


  The Apache Thrift catalog on APIs.io includes 1 Spectral governance ruleset.


  Apache Thrift''s developer surface includes documentation, developer portal, getting-started guide, release notes, and 6 more developer resources.'
plans:
- name: Apache Thrift Plans Pricing
  plan_count: 3
  slug: apache-thrift-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 5
  name: Apache Thrift Rate Limits
  slug: apache-thrift-rate-limits
rules:
- name: Apache Thrift API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: apache-thrift-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 9.7
    developer_ergonomics: 34.8
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 47.4
  previous_composite: 38.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-thrift/refs/heads/main/screenshots/apache-thrift-2026-06-20T172152.png
security:
- kind: domain-security
  name: Apache Thrift Domain Security
  slug: apache-thrift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Thrift Vulnerability Disclosure
  slug: apache-thrift-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-thrift
tags:
- Code Generation
- Cross-Language
- IDL
- RPC
- Serialization
- Open Source
use_cases:
- description: High-performance binary RPC between internal microservices in polyglot environments.
  name: Internal Microservices
- description: Type-safe APIs that work identically across Java, Python, C++, and other languages.
  name: Cross-Language APIs
- description: Service mesh and distributed system communication with efficient binary serialization.
  name: Distributed Systems
website: https://thrift.apache.org/
---
