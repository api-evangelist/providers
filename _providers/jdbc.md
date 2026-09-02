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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
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
random_paper: 4
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
