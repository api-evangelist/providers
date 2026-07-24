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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Google Bigquery Agentic Access
  operation_count: 30
  slug: google-bigquery-agentic-access
  summary_line: 30 operations · 17 acting
api_count: 11
apis:
- description: The BigQuery Connection API enables developers to create and manage connections between BigQuery and external data sources such as Cloud SQL, Cloud Spanner, and other databases. These connections allo
  name: BigQuery Connection API
  slug: bigquery-connection
- description: 'The BigQuery Migration API provides tools for migrating data warehouse workloads to BigQuery from other platforms. It supports assessment and planning of migration tasks, translation of SQL dialects, '
  name: BigQuery Migration API
  slug: bigquery-migration
- description: The BigQuery Reservation API allows developers to manage slot reservations and capacity commitments for BigQuery compute resources. It provides programmatic control over how compute capacity is alloca
  name: BigQuery Reservation API
  slug: bigquery-reservation
- description: 'The BigQuery Storage API provides high-throughput read and write access to BigQuery managed storage. It enables developers to read data from BigQuery tables using an efficient streaming protocol that '
  name: BigQuery Storage API
  slug: bigquery-storage
- description: Operations for managing BigQuery datasets
  name: Google BigQuery Datasets API
  slug: google-bigquery-datasets-api
- description: Operations for managing query and load jobs
  name: Google BigQuery Jobs API
  slug: google-bigquery-jobs-api
- description: Operations for managing BigQuery ML models
  name: Google BigQuery Models API
  slug: google-bigquery-models-api
- description: Operations for listing projects and service accounts
  name: Google BigQuery Projects API
  slug: google-bigquery-projects-api
- description: Operations for managing routines (functions and procedures)
  name: Google BigQuery Routines API
  slug: google-bigquery-routines-api
- description: Operations for reading and inserting table rows
  name: Google BigQuery Tabledata API
  slug: google-bigquery-tabledata-api
- description: Operations for managing tables within datasets
  name: Google BigQuery Tables API
  slug: google-bigquery-tables-api
artifact_total: 49
collections:
- collection_type: open
  name: Google BigQuery API
  slug: open-bigquery-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-bigquery-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-bigquery-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-bigquery-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-bigquery-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-bigquery-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/bigquery/docs/quickstarts
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/bigquery/pricing
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/bigquery/docs/authentication
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/bigquery
- group: build
  title: ''
  type: CLI
  url: https://cloud.google.com/bigquery/docs/reference/bq-cli-reference
- group: build
  title: ''
  type: SDKs
  url: https://cloud.google.com/bigquery/docs/reference/libraries
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/bigquery/docs/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-bigquery-context.jsonld
created: '2026-03-13'
description: Google BigQuery is a fully managed, serverless data warehouse that enables scalable analysis over petabytes of data using SQL.
finops:
- name: Google Bigquery Finops
  service_category: Data Warehouse / Analytics
  slug: google-bigquery-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-bigquery.png
json_schemas:
- name: Dataset
  property_count: 9
  slug: google-bigquery-dataset
- name: DatasetList
  property_count: 3
  slug: google-bigquery-datasetlist
- name: DatasetReference
  property_count: 2
  slug: google-bigquery-datasetreference
- name: ErrorProto
  property_count: 3
  slug: google-bigquery-errorproto
- name: Job
  property_count: 6
  slug: google-bigquery-job
- name: JobCancelResponse
  property_count: 2
  slug: google-bigquery-jobcancelresponse
- name: JobConfiguration
  property_count: 5
  slug: google-bigquery-jobconfiguration
- name: JobList
  property_count: 3
  slug: google-bigquery-joblist
- name: JobReference
  property_count: 3
  slug: google-bigquery-jobreference
- name: JobStatus
  property_count: 3
  slug: google-bigquery-jobstatus
- name: Model
  property_count: 6
  slug: google-bigquery-model
- name: ModelList
  property_count: 2
  slug: google-bigquery-modellist
- name: ProjectList
  property_count: 4
  slug: google-bigquery-projectlist
- name: Google BigQuery Query Request
  property_count: 9
  slug: google-bigquery-query
- name: QueryRequest
  property_count: 6
  slug: google-bigquery-queryrequest
- name: QueryResponse
  property_count: 8
  slug: google-bigquery-queryresponse
- name: Routine
  property_count: 6
  slug: google-bigquery-routine
- name: RoutineList
  property_count: 2
  slug: google-bigquery-routinelist
- name: Google BigQuery Table
  property_count: 14
  slug: google-bigquery-table
- name: TableDataInsertAllRequest
  property_count: 4
  slug: google-bigquery-tabledatainsertallrequest
- name: TableDataInsertAllResponse
  property_count: 2
  slug: google-bigquery-tabledatainsertallresponse
- name: TableDataList
  property_count: 4
  slug: google-bigquery-tabledatalist
- name: TableFieldSchema
  property_count: 5
  slug: google-bigquery-tablefieldschema
- name: TableList
  property_count: 4
  slug: google-bigquery-tablelist
- name: TableReference
  property_count: 3
  slug: google-bigquery-tablereference
- name: TableSchema
  property_count: 1
  slug: google-bigquery-tableschema
json_structures:
- name: Google Bigquery Structure
  property_count: 0
  slug: google-bigquery-structure
jsonld:
- class_count: 0
  name: Google Bigquery Context
  property_count: 5
  slug: google-bigquery-context
layout: provider
modified: '2026-05-19'
name: Google BigQuery
nav: Providers
network: true
overview: 'Google BigQuery publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Jobs API, Models API, and 4 more. Tagged areas include Analytics, Big Data, Cloud, Data Warehouse, and Serverless.


  The Google BigQuery catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google BigQuery''s developer surface includes authentication, getting-started guide, pricing, developer console, CLI, support, and 9 more developer resources.'
plans:
- name: Google Bigquery Plans Pricing
  plan_count: 6
  slug: google-bigquery-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 15
  name: Google Bigquery Rate Limits
  slug: google-bigquery-rate-limits
rules:
- name: Google BigQuery API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-bigquery-jsonschema-spectral-rules
scopes:
- name: Google Bigquery Scopes
  scope_count: 2
  slug: google-bigquery-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 56.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.6
    developer_ergonomics: 45.7
    discoverability: 55.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 56.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-bigquery/refs/heads/main/screenshots/google-bigquery-2026-06-20T182029.png
security:
- kind: authentication
  name: Google Bigquery Authentication
  slug: google-bigquery-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Bigquery Domain Security
  slug: google-bigquery-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Bigquery Vulnerability Disclosure
  slug: google-bigquery-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-bigquery
tags:
- Analytics
- Big Data
- Cloud
- Data Warehouse
- Serverless
- SQL
---
