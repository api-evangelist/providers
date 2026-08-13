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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 120
  human_in_the_loop: 0
  name: Data World Agentic Access
  operation_count: 187
  slug: data-world-agentic-access
  summary_line: 187 operations · 120 acting
api_count: 37
apis:
- description: Create, retrieve, update, delete, and download datasets. Manage dataset metadata, links, contributors, and access permissions.
  name: data.world Datasets API
  slug: dataworld-datasets-api
- description: Create, retrieve, update, and delete projects. Link datasets to projects, manage contributors and access controls.
  name: data.world Projects API
  slug: dataworld-projects-api
- description: Execute SQL queries against datasets and projects, describe columns, manage saved queries, and retrieve results in multiple formats.
  name: data.world SQL Query API
  slug: dataworld-sql-query-api
- description: Execute SPARQL queries via GET or POST against datasets. Supports multiple output formats for semantic data querying.
  name: data.world SPARQL Query API
  slug: dataworld-sparql-query-api
- description: Create, search, update, and delete catalog resources by IRI. Manage tables, columns, relationships, collections, business glossaries, and data quality badges.
  name: data.world Metadata Management API
  slug: dataworld-metadata-management-api
- description: Subscribe to dataset, project, and account events to automatically respond to activity on data.world.
  name: data.world Webhooks API
  slug: dataworld-webhooks-api
- description: Ask natural language questions against structured data and receive answers. Enables AI-powered data exploration within the catalog.
  name: data.world Answer API
  slug: dataworld-answer-api
- description: Manage relationships between catalog resources
  name: data.world catalog relationships API
  slug: data-world-catalog-relationships-api
- description: The catalog resources API from data.world — 7 operation(s) for catalog resources.
  name: data.world catalog resources API
  slug: data-world-catalog-resources-api
- description: The connections API from data.world — 3 operation(s) for connections.
  name: data.world connections API
  slug: data-world-connections-api
- description: Manage data quality of metadata resources
  name: data.world data quality API
  slug: data-world-data-quality-api
- description: The datasets API from data.world — 5 operation(s) for datasets.
  name: data.world datasets API
  slug: data-world-datasets-api
- description: The DOIs API from data.world — 2 operation(s) for dois.
  name: data.world DOIs API
  slug: data-world-dois-api
- description: This API is in active development. Its definition may change frequently and without notice.
  name: data.world experimental API
  slug: data-world-experimental-api
- description: The files API from data.world — 7 operation(s) for files.
  name: data.world files API
  slug: data-world-files-api
- description: The insights API from data.world — 3 operation(s) for insights.
  name: data.world insights API
  slug: data-world-insights-api
- description: The instance admin API from data.world — 3 operation(s) for instance admin.
  name: data.world instance admin API
  slug: data-world-instance-admin-api
- description: The legacy catalog - analysis API from data.world — 3 operation(s) for legacy catalog - analysis.
  name: data.world legacy catalog - analysis API
  slug: data-world-legacy-catalog-analysis-api
- description: The legacy catalog - collections API from data.world — 2 operation(s) for legacy catalog - collections.
  name: data.world legacy catalog - collections API
  slug: data-world-legacy-catalog-collections-api
- description: The legacy catalog - data API from data.world — 8 operation(s) for legacy catalog - data.
  name: data.world legacy catalog - data API
  slug: data-world-legacy-catalog-data-api
- description: The legacy catalog - glossary API from data.world — 3 operation(s) for legacy catalog - glossary.
  name: data.world legacy catalog - glossary API
  slug: data-world-legacy-catalog-glossary-api
- description: The legacy catalog - properties API from data.world — 1 operation(s) for legacy catalog - properties.
  name: data.world legacy catalog - properties API
  slug: data-world-legacy-catalog-properties-api
- description: The legacy catalog - relationships API from data.world — 4 operation(s) for legacy catalog - relationships.
  name: data.world legacy catalog - relationships API
  slug: data-world-legacy-catalog-relationships-api
- description: The organizations API from data.world — 2 operation(s) for organizations.
  name: data.world organizations API
  slug: data-world-organizations-api
- description: The projects API from data.world — 4 operation(s) for projects.
  name: data.world projects API
  slug: data-world-projects-api
- description: The queries API from data.world — 14 operation(s) for queries.
  name: data.world queries API
  slug: data-world-queries-api
- description: Manage authorization requests
  name: data.world requests - authorization API
  slug: data-world-requests-authorization-api
- description: Manage resource requests
  name: data.world requests - resource API
  slug: data-world-requests-resource-api
- description: The search API from data.world — 2 operation(s) for search.
  name: data.world search API
  slug: data-world-search-api
- description: The serviceaccount API from data.world — 3 operation(s) for serviceaccount.
  name: data.world serviceaccount API
  slug: data-world-serviceaccount-api
- description: The streams API from data.world — 3 operation(s) for streams.
  name: data.world streams API
  slug: data-world-streams-api
- description: The tables API from data.world — 1 operation(s) for tables.
  name: data.world tables API
  slug: data-world-tables-api
- description: The telemetry API from data.world — 1 operation(s) for telemetry.
  name: data.world telemetry API
  slug: data-world-telemetry-api
- description: The topics and comments - resource API from data.world — 7 operation(s) for topics and comments - resource.
  name: data.world topics and comments - resource API
  slug: data-world-topics-and-comments-resource-api
- description: The user API from data.world — 8 operation(s) for user.
  name: data.world user API
  slug: data-world-user-api
- description: The users API from data.world — 1 operation(s) for users.
  name: data.world users API
  slug: data-world-users-api
- description: The webhooks API from data.world — 4 operation(s) for webhooks.
  name: data.world webhooks API
  slug: data-world-webhooks-api
artifact_total: 49
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/data-world-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/data-world-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-world-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/data-world-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.data.world/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.data.world/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.data.world/docs/api-getting-started
- group: build
  title: ''
  type: SDKs
  url: https://developer.data.world/docs/data-world-for-developers
- group: build
  title: ''
  type: PythonSDK
  url: https://developer.data.world/docs/data-world-for-developers
- group: build
  title: ''
  type: RSDK
  url: https://developer.data.world/docs/data-world-for-developers
- group: build
  title: ''
  type: GoSDK
  url: https://developer.data.world/docs/data-world-for-developers
- group: other
  title: ''
  type: JDBC
  url: https://developer.data.world/docs/data-world-for-developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://whatsnew.data.world/
- group: operate
  title: ''
  type: Status
  url: https://status.data.world
- group: operate
  title: ''
  type: Support
  url: https://dataworld.atlassian.net/servicedesk/customer/portals
- group: company
  title: ''
  type: Blog
  url: https://data.world/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://data.world/legal/terms/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/data-world/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/data-world/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/data-world/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Collaborative data catalog platform with REST APIs for accessing public and private datasets, running SQL and SPARQL queries, managing metadata, and integrating data across projects and organizations. Provides enterprise data governance, lineage, and business glossary capabilities.
examples:
- key_count: 3
  name: Api Examples
  slug: api-examples
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-world.png
json_schemas:
- name: data.world API Schemas
  property_count: 0
  slug: schemas
jsonld:
- class_count: 0
  name: Api Context
  property_count: 17
  slug: api
- class_count: 0
  name: context Context
  property_count: 17
  slug: context
layout: provider
modified: '2026-06-13'
name: data.world
nav: Providers
network: true
overview: 'data.world publishes 30 APIs on the [APIs.io](https://apis.io/) network, including catalog relationships API, catalog resources API, connections API, and 27 more. Tagged areas include Data Catalog, Data Governance, Metadata Management, SPARQL, and SQL.


  The data.world catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  data.world''s developer surface includes authentication, developer portal, documentation, changelog, status page, support, engineering blog, and 13 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 47
rate_limits:
- limit_count: 3
  name: Rate Limits
  slug: rate-limits
rules:
- name: data.world API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: data-world-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.6
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 58.9
    developer_ergonomics: 41.3
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 47.4
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 30
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 48.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-world/refs/heads/main/screenshots/data-world-2026-06-20T175628.png
security:
- kind: authentication
  name: Data World Authentication
  slug: data-world-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Data World Domain Security
  slug: data-world-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Data World Trust Center
  slug: data-world-trust-center
  summary_line: SOC 2, ISO 27001
slug: data-world
tags:
- Data Catalog
- Data Governance
- Metadata Management
- SPARQL
- SQL
- Open Data
- Collaboration
website: https://developer.data.world/
---
