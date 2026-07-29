---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Oracle Database 19C Agentic Access
  operation_count: 12
  slug: oracle-database-19c-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 9
apis:
- description: Document-oriented NoSQL-style API for storing, retrieving, and querying JSON documents in Oracle Database.
  name: Oracle Database SODA (Simple Oracle Document Access)
  slug: oracle-database-soda-simple-oracle-document-access
- description: Browser-based interface for Oracle Database providing SQL worksheet, data modeler, and database administration capabilities.
  name: Oracle SQL Developer Web
  slug: oracle-sql-developer-web
- description: MongoDB-compatible API allowing MongoDB applications to connect to Oracle Database.
  name: Oracle Database API for MongoDB
  slug: oracle-database-api-for-mongodb
- description: RESTful API for managing JSON document collections with CRUD operations.
  name: Oracle Database JSON Collections API
  slug: oracle-database-json-collections-api
- description: REST APIs for Oracle Machine Learning AutoML capabilities including model building and deployment.
  name: Oracle Database REST API for AutoML
  slug: oracle-database-rest-api-for-automl
- description: AutoREST-enabled tables and views
  name: Oracle Database 19c AutoREST API
  slug: oracle-database-19c-autorest-api
- description: Schema and metadata catalog
  name: Oracle Database 19c Metadata API
  slug: oracle-database-19c-metadata-api
- description: Simple Oracle Document Access REST API
  name: Oracle Database 19c SODA API
  slug: oracle-database-19c-soda-api
- description: Ad-hoc SQL execution
  name: Oracle Database 19c SQL API
  slug: oracle-database-19c-sql-api
artifact_total: 26
collections:
- collection_type: open
  name: Oracle Database 19c - Oracle REST Data Services (ORDS) API
  slug: open-oracle-database-19c-ords
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-database-19c-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-database-19c-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-database-19c-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/oracle-database-19c-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: other
  title: ''
  type: Licensing
  url: https://www.oracle.com/database/technologies/database19c-license.html
- group: auth
  title: ''
  type: Security Alerts
  url: https://www.oracle.com/security-alerts/
- group: start
  title: ''
  type: Support Portal
  url: https://support.oracle.com
- group: operate
  title: ''
  type: Community Forums
  url: https://community.oracle.com/tech/developers/categories/oracle-database
- group: other
  title: ''
  type: Downloads
  url: https://www.oracle.com/database/technologies/oracle-database-software-downloads.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/database/technologies/database-pricing.html
created: '2024-01-15'
description: Oracle Database 19c is a multi-model database management system that provides a comprehensive platform for enterprise data management, analytics, and application development.
finops:
- name: Oracle Database 19C Finops
  service_category: Database
  slug: oracle-database-19c-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-database-19c.png
json_schemas:
- name: AutoRestResultSet
  property_count: 6
  slug: oracle-database-19c-autorestresultset
- name: MetadataCatalog
  property_count: 1
  slug: oracle-database-19c-metadatacatalog
- name: SODA Collection
  property_count: 9
  slug: oracle-database-19c-soda-collection
- name: SODA Document
  property_count: 7
  slug: oracle-database-19c-soda-document
- name: SodaListing
  property_count: 5
  slug: oracle-database-19c-sodalisting
- name: SqlResponse
  property_count: 1
  slug: oracle-database-19c-sqlresponse
json_structures:
- name: Oracle Database 19C Structure
  property_count: 0
  slug: oracle-database-19c-structure
jsonld:
- class_count: 11
  name: Oracle Database 19C Context
  property_count: 14
  slug: oracle-database-19c-context
layout: provider
modified: '2026-05-19'
name: Oracle Database 19c
nav: Providers
network: true
overview: 'Oracle Database 19c publishes 4 APIs on the [APIs.io](https://apis.io/) network, including AutoREST API, Metadata API, SODA API, and 1 more. Tagged areas include Database, Enterprise, Json, Machine-Learning, and Nosql.


  The Oracle Database 19c catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Oracle Database 19c''s developer surface includes authentication, pricing, and 9 more developer resources.'
plans:
- name: Oracle Database 19C Plans Pricing
  plan_count: 5
  slug: oracle-database-19c-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Oracle Database 19C Rate Limits
  slug: oracle-database-19c-rate-limits
rules:
- name: Oracle Database 19c API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: oracle-database-19c-jsonschema-spectral-rules
scopes:
- name: Oracle Database 19C Scopes
  scope_count: 0
  slug: oracle-database-19c-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.2
  delta: -4.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Oracle Database 19C Authentication
  slug: oracle-database-19c-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Oracle Database 19C Domain Security
  slug: oracle-database-19c-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-database-19c
tags:
- Database
- Enterprise
- Json
- Machine-Learning
- Nosql
- Oracle
- Rest
- Sql
---
