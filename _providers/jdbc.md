---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jdbc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.oracle.com/en/java/javase/21/docs/api/java.sql/module-summary.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/java/javase/21/docs/api/java.sql/java/sql/package-summary.html
- group: build
  title: ''
  type: EnterpriseExtension
  url: https://docs.oracle.com/en/java/javase/21/docs/api/java.sql/javax/sql/package-summary.html
created: '2025-01-01'
description: JDBC (Java Database Connectivity) is a Java API that defines how a client may access a database. It provides methods for querying and updating data in a database and is oriented towards relational databases. JDBC is part of the Java Standard Edition platform via the java.sql module (with enterprise extensions in javax.sql), and every JDBC driver implements the Driver interface to enable database connectivity in Java applications.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jdbc.png
layout: provider
modified: '2026-04-28'
name: JDBC
nav: Providers
network: true
overview: 'JDBC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Java, JDBC, SQL, and Standard.


  JDBC''s developer surface includes documentation and 3 more developer resources.'
random_paper: 46
score:
  band: minimal
  composite: 8.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jdbc/refs/heads/main/screenshots/jdbc-2026-06-20T183713.png
security:
- kind: domain-security
  name: Jdbc Domain Security
  slug: jdbc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jdbc
tags:
- Database
- Java
- JDBC
- SQL
- Standard
- java.sql
website: https://docs.oracle.com/en/java/javase/21/docs/api/java.sql/module-summary.html
---
