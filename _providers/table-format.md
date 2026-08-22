---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Table Format Agentic Access
  operation_count: 18
  slug: table-format-agentic-access
  summary_line: 18 operations · 11 acting
api_count: 8
apis:
- description: Delta Lake is an open-source storage framework developed by Databricks that adds reliability, performance, and ACID compliance to data lakes. It uses a transaction log (delta log) to record all change
  name: Delta Lake
  slug: delta-lake
- description: Apache Hudi (Hadoop Upserts Deletes and Incrementals) is an open-source data lakehouse platform optimized for upserts, deletes, and incremental data processing. It supports Copy-on-Write (COW) and Mer
  name: Apache Hudi
  slug: apache-hudi
- description: Transaction commits and metadata updates
  name: Table Format Commits API
  slug: table-format-commits-api
- description: Catalog configuration and discovery
  name: Table Format Configuration API
  slug: table-format-configuration-api
- description: Namespace (database/schema) management
  name: Table Format Namespaces API
  slug: table-format-namespaces-api
- description: OAuth2 token management
  name: Table Format OAuth2 API
  slug: table-format-oauth2-api
- description: Table creation, listing, loading, and management
  name: Table Format Tables API
  slug: table-format-tables-api
- description: View lifecycle management
  name: Table Format Views API
  slug: table-format-views-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Iceberg REST Catalog API
  slug: open-apache-iceberg-rest-catalog
- collection_type: open
  name: Apache Iceberg REST Catalog Commits API
  slug: open-table-format-commits-api
- collection_type: open
  name: Apache Iceberg REST Catalog Commits Configuration API
  slug: open-table-format-configuration-api
- collection_type: open
  name: Apache Iceberg REST Catalog Commits Namespaces API
  slug: open-table-format-namespaces-api
- collection_type: open
  name: Apache Iceberg REST Catalog Commits OAuth2 API
  slug: open-table-format-oauth2-api
- collection_type: open
  name: Apache Iceberg REST Catalog Commits Tables API
  slug: open-table-format-tables-api
- collection_type: open
  name: Apache Iceberg REST Catalog Commits Views API
  slug: open-table-format-views-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/table-format-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/table-format-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/table-format-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/table-format-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/table-format-scopes.yml
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Apache_Iceberg
- group: other
  title: ''
  type: Apache Iceberg
  url: https://iceberg.apache.org/
- group: other
  title: ''
  type: Delta Lake
  url: https://delta.io/
- group: other
  title: ''
  type: Apache Hudi
  url: https://hudi.apache.org/
- group: other
  title: ''
  type: Unity Catalog
  url: https://www.unitycatalog.io/
- group: build
  title: ''
  type: Apache Iceberg GitHub
  url: https://github.com/apache/iceberg
- group: build
  title: ''
  type: Delta Lake GitHub
  url: https://github.com/delta-io/delta
- group: build
  title: ''
  type: Apache Hudi GitHub
  url: https://github.com/apache/hudi
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/table-format/refs/heads/main/vocabulary/table-format-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://iceberg.apache.org/feed_rss_updated.xml
created: '2025'
description: Open Table Format is a category of open standards for organizing and managing data in data lakehouses. The three dominant formats are Apache Iceberg (the emerging industry standard with snapshot-based metadata and broad engine support), Delta Lake (Databricks-originated, transaction-log-based), and Apache Hudi (upsert-optimized with Copy-on-Write and Merge-on-Read modes). These formats bring ACID transactions, schema evolution, time travel, and efficient query planning to data lake storage. Apache Iceberg defines a REST Catalog API (OpenAPI spec) that enables standardized catalog operations across implementations like Polaris, Nessie, AWS Glue, and Google BigLake.
examples:
- key_count: 2
  name: Apache Iceberg Create Table Example
  slug: apache-iceberg-create-table-example
- key_count: 2
  name: Apache Iceberg List Namespaces Example
  slug: apache-iceberg-list-namespaces-example
finops:
- name: Table Format Finops
  service_category: API
  slug: table-format-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/table-format.png
json_schemas:
- name: Apache Iceberg Table Metadata
  property_count: 11
  slug: table-format-iceberg-table
json_structures:
- name: Table Format Iceberg Table Structure
  property_count: 0
  slug: table-format-iceberg-table-structure
jsonld:
- class_count: 26
  name: Table Format Context
  property_count: 0
  slug: table-format-context
layout: provider
modified: '2026-05-19'
name: Table Format
nav: Providers
network: true
overview: 'Table Format publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Commits API, Configuration API, Namespaces API, and 3 more. Tagged areas include Data Lakehouse, Open Table Format, Apache Iceberg, Delta Lake, and Apache Hudi.


  The Table Format catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Table Format''s developer surface includes authentication, engineering blog, and 13 more developer resources.'
plans:
- name: Table Format Plans Pricing
  plan_count: 3
  slug: table-format-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Table Format Rate Limits
  slug: table-format-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Table Format API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: table-format-jsonschema-spectral-rules
scopes:
- name: Table Format Scopes
  scope_count: 1
  slug: table-format-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 31.5
  delta: -5.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 60.0
    developer_ergonomics: 14.3
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/table-format/refs/heads/main/screenshots/table-format-2026-06-20T194843.png
security:
- kind: authentication
  name: Table Format Authentication
  slug: table-format-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Table Format Domain Security
  slug: table-format-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Table Format Vulnerability Disclosure
  slug: table-format-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: table-format
tags:
- Data Lakehouse
- Open Table Format
- Apache Iceberg
- Delta Lake
- Apache Hudi
- Data Lake
- ACID Transactions
- Schema Evolution
- Time Travel
---
