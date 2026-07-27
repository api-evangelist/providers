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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 32
  human_in_the_loop: 1
  name: Tidb Agentic Access
  operation_count: 74
  slug: tidb-agentic-access
  summary_line: 74 operations · 32 acting · 1 human-in-the-loop
api_count: 23
apis:
- description: Operations for creating, listing, updating, and deleting TiDB Cloud API keys.
  name: tidb API Keys API
  slug: tidb-api-keys-api
- description: Operations for retrieving organization-level console audit logs.
  name: tidb Audit Logs API
  slug: tidb-audit-logs-api
- description: Operations for retrieving monthly billing summaries, cost details, and usage trends.
  name: tidb Billing API
  slug: tidb-billing-api
- description: Operations for translating natural language questions into SQL and executing them against TiDB Cloud clusters.
  name: tidb Chat2Data API
  slug: tidb-chat2data-api
- description: Operations for creating, listing, updating, and deleting TiDB Cloud Dedicated clusters.
  name: tidb Clusters API
  slug: tidb-clusters-api
- description: Operations for managing API keys scoped to a specific Data App.
  name: tidb Data App API Keys API
  slug: tidb-data-app-api-keys-api
- description: Operations for creating, listing, updating, and deleting Data Apps.
  name: tidb Data Apps API
  slug: tidb-data-apps-api
- description: Operations for linking and managing TiDB Cloud clusters as data sources within a Data App.
  name: tidb Data Sources API
  slug: tidb-data-sources-api
- description: Operations for generating and managing AI summaries of database schemas used as context for SQL generation.
  name: tidb Data Summaries API
  slug: tidb-data-summaries-api
- description: Endpoints for managing and inspecting DDL jobs, including ownership and history.
  name: tidb DDL API
  slug: tidb-ddl-api
- description: Operations for deploying and managing versions of a Data App.
  name: tidb Deployments API
  slug: tidb-deployments-api
- description: Endpoints for downloading debug information and managing server diagnostics.
  name: tidb Diagnostics API
  slug: tidb-diagnostics-api
- description: Operations for creating, listing, updating, testing, and deleting custom SQL-backed API endpoints.
  name: tidb Endpoints API
  slug: tidb-endpoints-api
- description: Operations for creating and managing data import tasks into TiDB Cloud clusters.
  name: tidb Imports API
  slug: tidb-imports-api
- description: Operations for managing third-party integrations with TiDB Cloud clusters.
  name: tidb Integrations API
  slug: tidb-integrations-api
- description: Endpoints for retrieving multi-version concurrency control (MVCC) key details for debugging.
  name: tidb MVCC API
  slug: tidb-mvcc-api
- description: Operations for listing available cloud regions and node specifications.
  name: tidb Regions API
  slug: tidb-regions-api
- description: Endpoints for retrieving database and table schema information from the TiDB information schema.
  name: tidb Schema API
  slug: tidb-schema-api
- description: Operations for creating and managing multi-round conversational chat sessions.
  name: tidb Sessions API
  slug: tidb-sessions-api
- description: Endpoints for retrieving and modifying TiDB server runtime settings.
  name: tidb Settings API
  slug: tidb-settings-api
- description: Operations for refining and improving previously generated SQL queries.
  name: tidb SQL Refinement API
  slug: tidb-sql-refinement-api
- description: Endpoints for exporting optimizer statistics used for query planning.
  name: tidb Statistics API
  slug: tidb-statistics-api
- description: Endpoints for retrieving the operational status of the TiDB server instance.
  name: tidb Status API
  slug: tidb-status-api
artifact_total: 41
collections:
- collection_type: open
  name: TiDB Cloud API
  slug: open-tidb-cloud-api
- collection_type: open
  name: TiDB Cloud Chat2Query API
  slug: open-tidb-cloud-chat2query
- collection_type: open
  name: TiDB Cloud Data Service API
  slug: open-tidb-cloud-data-service
- collection_type: open
  name: TiDB HTTP API
  slug: open-tidb-http-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tidb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tidb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tidb-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pingcap
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tidb-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tidb-cluster-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tidb-data-service-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/tidb-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tidb-vocabulary.yml
description: TiDB is an open-source distributed SQL database that supports Hybrid Transactional and Analytical Processing workloads, with horizontal scalability, strong consistency, and high availability.
examples:
- key_count: 2
  name: Tidb Cloud Api List Clusters Example
  slug: tidb-cloud-api-list-clusters-example
- key_count: 2
  name: Tidb Cloud Chat2Query Example
  slug: tidb-cloud-chat2query-example
- key_count: 2
  name: Tidb Http Api Get Status Example
  slug: tidb-http-api-get-status-example
finops:
- name: Tidb Finops
  service_category: Database
  slug: tidb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tidb.png
json_schemas:
- name: TiDB Cloud Cluster
  property_count: 14
  slug: tidb-cluster
- name: TiDB Cloud Data Service
  property_count: 6
  slug: tidb-data-service
json_structures:
- name: Tidb Cluster Structure
  property_count: 0
  slug: tidb-cluster-structure
jsonld:
- class_count: 0
  name: Tidb Context
  property_count: 16
  slug: tidb-context
layout: provider
modified: '2026-05-19'
name: tidb
nav: Providers
network: true
overview: 'tidb publishes 23 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Audit Logs API, Billing API, and 20 more.


  The tidb catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tidb''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: Tidb Plans Pricing
  plan_count: 6
  slug: tidb-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Tidb Rate Limits
  slug: tidb-rate-limits
rules:
- name: tidb API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: tidb-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.3
  delta: 4.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 75.6
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 31.6
  previous_composite: 45.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/screenshots/tidb-2026-06-20T195336.png
security:
- kind: authentication
  name: Tidb Authentication
  slug: tidb-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tidb Domain Security
  slug: tidb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tidb
---
