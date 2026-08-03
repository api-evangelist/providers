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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Azure Synapse Agentic Access
  operation_count: 6
  slug: azure-synapse-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 3
apis:
- description: Manage Apache Spark pools
  name: Azure Synapse Analytics Spark Pools API
  slug: azure-synapse-spark-pools-api
- description: Manage dedicated SQL pools
  name: Azure Synapse Analytics SQL Pools API
  slug: azure-synapse-sql-pools-api
- description: Manage Synapse Analytics workspaces
  name: Azure Synapse Analytics Workspaces API
  slug: azure-synapse-workspaces-api
artifact_total: 34
collections:
- collection_type: postman
  name: Azure Synapse Analytics Spark Pools API
  slug: postman-azure-synapse-spark-pools-api
- collection_type: postman
  name: Azure Synapse Analytics Spark Pools SQL Pools API
  slug: postman-azure-synapse-sql-pools-api
- collection_type: postman
  name: Azure Synapse Analytics Spark Pools Workspaces API
  slug: postman-azure-synapse-workspaces-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-synapse-analytics/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-synapse-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-synapse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-synapse-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-synapse-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.microsoft.com/en-us/azure/synapse-analytics/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.microsoft.com/en-us/azure/synapse-analytics/get-started
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/azure-synapse-analytics-blog/bg-p/AzureSynapseAnalyticsBlog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure/azure-synapse-analytics
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/azure-synapse/refs/heads/main/rules/azure-synapse-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/azure-synapse/refs/heads/main/vocabulary/azure-synapse-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/azure-synapse/refs/heads/main/json-ld/azure-synapse-context.jsonld
created: '2024-01-01'
description: Azure Synapse Analytics is an enterprise analytics service that accelerates time to insight across data warehouses and big data systems. It brings together SQL technologies, Spark technologies, Data Explorer, and integrated pipelines for data integration and ETL/ELT.
examples:
- key_count: 4
  name: Azure Synapse Big Data Pool Example
  slug: azure-synapse-big-data-pool-example
- key_count: 2
  name: Azure Synapse Big Data Pool Resource Info List Result Example
  slug: azure-synapse-big-data-pool-resource-info-list-result-example
- key_count: 6
  name: Azure Synapse Sql Pool Example
  slug: azure-synapse-sql-pool-example
- key_count: 2
  name: Azure Synapse Sql Pool Info List Result Example
  slug: azure-synapse-sql-pool-info-list-result-example
- key_count: 6
  name: Azure Synapse Workspace Example
  slug: azure-synapse-workspace-example
- key_count: 2
  name: Azure Synapse Workspace Info List Result Example
  slug: azure-synapse-workspace-info-list-result-example
finops:
- name: Azure Synapse Finops
  service_category: API
  slug: azure-synapse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-synapse.png
json_schemas:
- name: BigDataPoolResourceInfoListResult
  property_count: 2
  slug: azure-synapse-big-data-pool-resource-info-list-result
- name: BigDataPool
  property_count: 4
  slug: azure-synapse-big-data-pool
- name: SqlPoolInfoListResult
  property_count: 2
  slug: azure-synapse-sql-pool-info-list-result
- name: SqlPool
  property_count: 6
  slug: azure-synapse-sql-pool
- name: WorkspaceInfoListResult
  property_count: 2
  slug: azure-synapse-workspace-info-list-result
- name: Workspace
  property_count: 6
  slug: azure-synapse-workspace
json_structures:
- name: Azure Synapse Big Data Pool Resource Info List Result Structure
  property_count: 2
  slug: azure-synapse-big-data-pool-resource-info-list-result-structure
- name: Azure Synapse Big Data Pool Structure
  property_count: 4
  slug: azure-synapse-big-data-pool-structure
- name: Azure Synapse Sql Pool Info List Result Structure
  property_count: 2
  slug: azure-synapse-sql-pool-info-list-result-structure
- name: Azure Synapse Sql Pool Structure
  property_count: 6
  slug: azure-synapse-sql-pool-structure
- name: Azure Synapse Workspace Info List Result Structure
  property_count: 2
  slug: azure-synapse-workspace-info-list-result-structure
- name: Azure Synapse Workspace Structure
  property_count: 6
  slug: azure-synapse-workspace-structure
jsonld:
- class_count: 7
  name: Azure Synapse Context
  property_count: 8
  slug: azure-synapse-context
layout: provider
modified: '2026-05-19'
name: Azure Synapse Analytics
nav: Providers
network: true
overview: 'Azure Synapse Analytics publishes 3 APIs on the [APIs.io](https://apis.io/) network: Spark Pools API, SQL Pools API, and Workspaces API. Tagged areas include Analytics, Apache Spark, Big Data, Data Warehouse, and ETL.


  The Azure Synapse Analytics catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Azure Synapse Analytics'' developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, and 11 more developer resources.'
plans:
- name: Azure Synapse Plans Pricing
  plan_count: 3
  slug: azure-synapse-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Azure Synapse Rate Limits
  slug: azure-synapse-rate-limits
rules:
- name: Azure Synapse Analytics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-synapse-jsonschema-spectral-rules
- name: Azure Synapse Analytics API Rules
  rule_count: 21
  severity_counts:
    error: 5
    hint: 0
    info: 5
    warn: 11
  slug: azure-synapse-spectral-rules
scopes:
- name: Azure Synapse Scopes
  scope_count: 1
  slug: azure-synapse-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 49.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 20.5
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-synapse/refs/heads/main/screenshots/azure-synapse-2026-06-20T172913.png
security:
- kind: authentication
  name: Azure Synapse Authentication
  slug: azure-synapse-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Azure Synapse Domain Security
  slug: azure-synapse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azure-synapse
tags:
- Analytics
- Apache Spark
- Big Data
- Data Warehouse
- ETL
- SQL
website: https://portal.azure.com
---
