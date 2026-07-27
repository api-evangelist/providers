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
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Mysql Agentic Access
  operation_count: 7
  slug: microsoft-azure-mysql-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 10
apis:
- description: Create, list, retrieve, and delete databases hosted on a MySQL Flexible Server. Manage character sets and collations for each database within a server.
  name: Azure Database for MySQL Databases API
  slug: azure-database-for-mysql-databases-api
- description: Create and manage server-level firewall rules to grant access to a MySQL Flexible Server from specified client IP address ranges. Required for clients connecting from outside the Azure network.
  name: Azure Database for MySQL Firewall Rules API
  slug: azure-database-for-mysql-firewall-rules-api
- description: Manage server parameters (configurations) for a MySQL Flexible Server. Adjust MySQL engine variables such as character_set_server, time_zone, and innodb_buffer_pool_size to tune performance and behavi
  name: Azure Database for MySQL Configurations API
  slug: azure-database-for-mysql-configurations-api
- description: Manage read replicas for MySQL Flexible Server to scale out read-heavy workloads. Create replicas in the same or different region for performance and read distribution.
  name: Azure Database for MySQL Replicas API
  slug: azure-database-for-mysql-replicas-api
- description: List and manage automated backups for MySQL Flexible Servers, including on-demand backup creation, retention configuration, and point-in-time restore operations.
  name: Azure Database for MySQL Backups API
  slug: azure-database-for-mysql-backups-api
- description: Configure Azure Active Directory administrators for MySQL Flexible Server. Allows tenant users, groups, or service principals to be designated as MySQL administrators for AAD-based authentication.
  name: Azure Database for MySQL Administrators API
  slug: azure-database-for-mysql-administrators-api
- description: Check whether a proposed MySQL Flexible Server name is available within the Azure global namespace before creating a new server.
  name: Azure Database for MySQL Check Name Availability API
  slug: azure-database-for-mysql-check-name-availability-api
- description: List Azure Database for MySQL provider operations available in the subscription, including supported operation types and metadata.
  name: Azure Database for MySQL Operations API
  slug: azure-database-for-mysql-operations-api
- description: Operations operations
  name: Azure Database for MySQL Operations API
  slug: microsoft-azure-mysql-operations-api
- description: Servers operations
  name: Azure Database for MySQL Servers API
  slug: microsoft-azure-mysql-servers-api
artifact_total: 18
collections:
- collection_type: open
  name: Azure Database for MySQL REST API
  slug: open-microsoft-azure-mysql
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-mysql-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-mysql-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-mysql-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-mysql-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/mysql/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/mysql/flexible-server/quickstart-create-server-portal
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-csharp
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/mysql/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/options/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/tag/azure-database-for-mysql/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/mysql/flexible-server/whats-new
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/mysql
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure Database for MySQL is a fully managed relational database service based on the open-source MySQL community edition. Its REST APIs enable management of flexible servers, single servers, databases, firewall and network rules, configurations, replicas, and backups with built-in high availability and automated backups.
finops:
- name: Microsoft Azure Mysql Finops
  service_category: API
  slug: microsoft-azure-mysql-finops
image: https://azure.microsoft.com/svghandler/mysql/
layout: provider
modified: '2026-05-19'
name: Azure Database for MySQL
nav: Providers
network: true
overview: 'Azure Database for MySQL publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Servers API. Tagged areas include Database, Flexible Server, Managed Database, MySQL, and Open Source.


  Azure Database for MySQL''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, support, engineering blog, and 14 more developer resources.'
plans:
- name: Microsoft Azure Mysql Plans Pricing
  plan_count: 3
  slug: microsoft-azure-mysql-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Microsoft Azure Mysql Rate Limits
  slug: microsoft-azure-mysql-rate-limits
scopes:
- name: Microsoft Azure Mysql Scopes
  scope_count: 1
  slug: microsoft-azure-mysql-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 59.4
  delta: 3.2
  facets:
    commercial_clarity: 84.2
    contract_quality: 53.1
    developer_ergonomics: 52.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 56.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-mysql/refs/heads/main/screenshots/microsoft-azure-mysql-2026-06-20T185425.png
security:
- kind: authentication
  name: Microsoft Azure Mysql Authentication
  slug: microsoft-azure-mysql-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Mysql Domain Security
  slug: microsoft-azure-mysql-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-mysql
tags:
- Database
- Flexible Server
- Managed Database
- MySQL
- Open Source
- Relational Database
website: https://azure.microsoft.com/en-us/products/mysql
---
