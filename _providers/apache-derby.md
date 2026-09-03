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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Derby provides a standard JDBC API for database operations in both embedded (org.apache.derby.jdbc.EmbeddedDriver) and client/server (org.apache.derby.jdbc.ClientDriver) modes, supporting full SQL, st
  name: Apache Derby
  slug: apache-derby
artifact_total: 29
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/derby/blob/trunk/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-derby-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-derby-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://db.apache.org/derby/
- group: docs
  title: ''
  type: Documentation
  url: https://db.apache.org/derby/manuals/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://db.apache.org/derby/quick_start.html
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/derby
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/apache-derby
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/apache-derby/refs/heads/main/vocabulary/apache-derby-vocabulary.yaml
created: '2026-03-16'
description: Apache Derby is an open-source relational database implemented entirely in Java, formerly governed by the Apache Software Foundation (retired October 2025). It provides a small-footprint (~3.5MB) database engine with full SQL support, JDBC compliance, ACID transactions, stored procedures, and triggers. Derby operates in both embedded mode (bundled inside Java applications) and client/server mode via the Derby Network Server.
examples:
- key_count: 10
  name: Apache Derby Connection Config Example
  slug: apache-derby-connection-config-example
- key_count: 4
  name: Apache Derby Table Info Example
  slug: apache-derby-table-info-example
features:
- description: Derby can be embedded directly in Java applications as a library, providing a zero-administration database with no separate server process required.
  name: Embedded Mode
- description: Derby Network Server supports multiple concurrent JDBC clients connecting over TCP/IP using the Derby Network Client driver.
  name: Client/Server Mode
- description: Supports ANSI SQL-92 with extensions including subqueries, joins, constraints, triggers, views, stored procedures, and user-defined functions.
  name: Full SQL Support
- description: Full ACID transaction support with row-level locking, MVCC-style isolation levels, and savepoints.
  name: ACID Transactions
- description: The base Derby engine and embedded JDBC driver is approximately 3.5MB, making it suitable for desktop and embedded applications.
  name: Small Footprint
- description: Supports Java-based stored procedures and functions callable directly from SQL using standard JDBC interfaces.
  name: Java Stored Procedures
finops:
- name: Apache Derby Finops
  service_category: API
  slug: apache-derby-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-derby.png
integrations:
- description: Derby provides JDBC 4.0/4.1/4.2 compliant embedded and network client drivers.
  name: JDBC
- description: Commonly used with Spring DataSource and JPA/Hibernate for test database configuration.
  name: Spring Framework
- description: Derby has a Hibernate dialect (DerbyDialect) for ORM integration.
  name: Hibernate / JPA
- description: Derby artifacts are available on Maven Central under org.apache.derby group ID.
  name: Apache Maven
- description: Eclipse IDE includes Derby as a built-in SQL explorer and development database.
  name: Eclipse IDE
json_schemas:
- name: ConnectionConfig
  property_count: 10
  slug: apache-derby-connection-config
- name: TableInfo
  property_count: 5
  slug: apache-derby-table-info
json_structures:
- name: Apache Derby Connection Config Structure
  property_count: 10
  slug: apache-derby-connection-config-structure
- name: Apache Derby Table Info Structure
  property_count: 5
  slug: apache-derby-table-info-structure
jsonld:
- class_count: 2
  name: Apache Derby Context
  property_count: 15
  slug: apache-derby-context
layout: provider
modified: '2026-04-19'
name: Apache Derby
nav: Providers
network: true
overview: 'Apache Derby publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Apache, Database, Embedded, Java, and JDBC.


  The Apache Derby catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apache Derby''s developer surface includes developer portal, documentation, getting-started guide, Stack Overflow tag, and 7 more developer resources.'
plans:
- name: Apache Derby Plans Pricing
  plan_count: 3
  slug: apache-derby-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Apache Derby Rate Limits
  slug: apache-derby-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Derby API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-derby-jsonschema-spectral-rules
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 30.7
    developer_ergonomics: 47.6
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 28.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-derby/refs/heads/main/screenshots/apache-derby-2026-06-20T172052.png
security:
- kind: domain-security
  name: Apache Derby Domain Security
  slug: apache-derby-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Derby Vulnerability Disclosure
  slug: apache-derby-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-derby
tags:
- Apache
- Database
- Embedded
- Java
- JDBC
- Open-Source
- Relational
- SQL
use_cases:
- description: Embed Derby in desktop Java applications, IDEs, or tools that need a local SQL database without a separate server.
  name: Embedded Application Database
- description: Use Derby as an in-memory or on-disk test database for Java application integration tests with JDBC.
  name: Unit and Integration Testing
- description: Use Derby as a development database when production uses a heavier RDBMS, without installing MySQL or PostgreSQL.
  name: Lightweight Development Database
- description: Use Derby as a staging database for ETL processes in Java-based data pipelines.
  name: Data Migration and ETL
website: https://db.apache.org/derby/
---
