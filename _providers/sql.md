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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Open Database Connectivity (ODBC) is a standard C-language API for accessing database management systems. ODBC allows applications to connect to any ODBC-compliant database using a unified programming
  name: ODBC API
  slug: odbc-api
- description: Java Database Connectivity (JDBC) is the standard Java API for connecting Java applications to relational databases. JDBC provides a uniform interface for executing SQL queries, managing transactions,
  name: JDBC API
  slug: jdbc-api
artifact_total: 11
common:
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sql-query-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sql-result-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sql-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sql-vocabulary.yml
- group: other
  title: ''
  type: ISO Standard
  url: https://www.iso.org/standard/76583.html
- group: other
  title: ''
  type: ANSI Standard
  url: https://www.ansi.org/
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/SQL
- group: learn
  title: ''
  type: W3Schools Tutorial
  url: https://www.w3schools.com/sql/
- group: docs
  title: ''
  type: MDN Web Docs
  url: https://developer.mozilla.org/en-US/docs/Learn/Server-side/SQL
created: '2026-05-02'
description: SQL (Structured Query Language) is the ANSI/ISO standard language for managing and querying relational databases. SQL defines the interface for creating, reading, updating, and deleting data in relational database management systems (RDBMS). Database connectivity standards including ODBC (Open Database Connectivity) and JDBC (Java Database Connectivity) expose SQL capabilities as programmatic APIs, enabling applications to connect to and interact with SQL-compliant databases. Major implementations include MySQL, PostgreSQL, Microsoft SQL Server, Oracle, SQLite, and many others.
examples:
- key_count: 4
  name: Sql Select Query Example
  slug: sql-select-query-example
finops:
- name: Sql Finops
  service_category: API
  slug: sql-finops
image: https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png
json_schemas:
- name: SQL Query
  property_count: 6
  slug: sql-query
- name: SQL Query Result
  property_count: 8
  slug: sql-result
json_structures:
- name: Sql Query Structure
  property_count: 0
  slug: sql-query-structure
jsonld:
- class_count: 17
  name: Sql Context
  property_count: 6
  slug: sql-context
layout: provider
modified: '2026-05-02'
name: SQL
nav: Providers
network: true
overview: 'SQL publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ANSI Standard, Data Management, Database, ISO Standard, and Query Language.


  The SQL catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Sql Plans Pricing
  plan_count: 3
  slug: sql-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Sql Rate Limits
  slug: sql-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SQL API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sql-jsonschema-spectral-rules
score:
  band: emerging
  composite: 15.2
  delta: -5.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 11.3
    developer_ergonomics: 0.0
    discoverability: 51.9
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 20.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sql/refs/heads/main/screenshots/sql-2026-06-20T194425.png
slug: sql
tags:
- ANSI Standard
- Data Management
- Database
- ISO Standard
- Query Language
- Relational Database
- SQL
website: https://www.iso.org/standard/76583.html
---
