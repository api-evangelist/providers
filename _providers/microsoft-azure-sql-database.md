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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Microsoft Azure Sql Database Agentic Access
  operation_count: 15
  slug: microsoft-azure-sql-database-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 5
apis:
- description: The Databases API from Azure SQL Database — 2 operation(s) for databases.
  name: Azure SQL Database Databases API
  slug: microsoft-azure-sql-database-databases-api
- description: The ElasticPools API from Azure SQL Database — 1 operation(s) for elasticpools.
  name: Azure SQL Database ElasticPools API
  slug: microsoft-azure-sql-database-elasticpools-api
- description: The FailoverGroups API from Azure SQL Database — 1 operation(s) for failovergroups.
  name: Azure SQL Database FailoverGroups API
  slug: microsoft-azure-sql-database-failovergroups-api
- description: The FirewallRules API from Azure SQL Database — 2 operation(s) for firewallrules.
  name: Azure SQL Database FirewallRules API
  slug: microsoft-azure-sql-database-firewallrules-api
- description: The Servers API from Azure SQL Database — 3 operation(s) for servers.
  name: Azure SQL Database Servers API
  slug: microsoft-azure-sql-database-servers-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure SQL Database REST Databases API
  slug: open-microsoft-azure-sql-database-databases-api
- collection_type: open
  name: Azure SQL Database REST Databases ElasticPools API
  slug: open-microsoft-azure-sql-database-elasticpools-api
- collection_type: open
  name: Azure SQL Database REST Databases FailoverGroups API
  slug: open-microsoft-azure-sql-database-failovergroups-api
- collection_type: open
  name: Azure SQL Database REST Databases FirewallRules API
  slug: open-microsoft-azure-sql-database-firewallrules-api
- collection_type: open
  name: Azure SQL Database REST Databases Servers API
  slug: open-microsoft-azure-sql-database-servers-api
- collection_type: open
  name: Azure SQL Database REST API
  slug: open-microsoft-azure-sql-database
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-sql-database-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-sql-database-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-sql-database-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/azure-sql-database/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-sql/database/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/azure-sql/database/single-database-create-quickstart
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/product/azure-sql-database/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-sql-database
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure SQL Database is a fully managed relational database service built on the SQL Server engine with built-in intelligence, high availability, and elastic scaling.
finops:
- name: Microsoft Azure Sql Database Finops
  service_category: API
  slug: microsoft-azure-sql-database-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-sql-database.png
layout: provider
modified: '2026-05-19'
name: Azure SQL Database
nav: Providers
network: true
overview: 'Azure SQL Database publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Databases API, ElasticPools API, FailoverGroups API, and 2 more. Tagged areas include Database, SQL, and Relational Database.


  Azure SQL Database''s developer surface includes authentication, developer portal, pricing, documentation, getting-started guide, support, engineering blog, and 8 more developer resources.'
plans:
- name: Microsoft Azure Sql Database Plans Pricing
  plan_count: 3
  slug: microsoft-azure-sql-database-plans-pricing
random_paper: 143
rate_limits:
- limit_count: 5
  name: Microsoft Azure Sql Database Rate Limits
  slug: microsoft-azure-sql-database-rate-limits
score:
  band: thin
  composite: 41.7
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 52.2
    developer_ergonomics: 45.7
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-sql-database/refs/heads/main/screenshots/microsoft-azure-sql-database-2026-06-20T185438.png
security:
- kind: authentication
  name: Microsoft Azure Sql Database Authentication
  slug: microsoft-azure-sql-database-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Azure Sql Database Domain Security
  slug: microsoft-azure-sql-database-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-sql-database
tags:
- Database
- SQL
- Relational Database
website: https://portal.azure.com/
---
