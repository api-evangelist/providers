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
  name: Microsoft Azure Migrate Agentic Access
  operation_count: 7
  slug: microsoft-azure-migrate-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 9
apis:
- description: Create and manage assessments that evaluate on-premises servers and databases for Azure readiness, sizing, and cost. Returns Azure VM readiness, recommended SKUs, monthly cost estimates, and migration
  name: Azure Migrate Assessments API
  slug: azure-migrate-assessments-api
- description: Manage discovery sites and inventory of on-premises servers, databases, and applications. Provides agentless and agent-based discovery for VMware, Hyper-V, and physical servers as a basis for assessme
  name: Azure Migrate Discovery API
  slug: azure-migrate-discovery-api
- description: Replicate, test migrate, and migrate on-premises servers including VMware, Hyper-V, and physical machines to Azure. Manages replication jobs, fabrics, and protected items used for server migration.
  name: Azure Migrate Server Migration API
  slug: azure-migrate-server-migration-api
- description: Streamline the migration of on-premises databases to Azure data platforms with minimal downtime. Supports SQL Server, MySQL, PostgreSQL, MongoDB, and Oracle source databases moving to Azure SQL, Azure
  name: Azure Database Migration Service API
  slug: azure-database-migration-service-api
- description: Discover and assess on-premises ASP.NET and Java web apps running on IIS and Tomcat for migration to Azure App Service. Returns readiness findings, configuration issues, and recommended Azure App Serv
  name: Azure Migrate Web Apps Assessment API
  slug: azure-migrate-web-apps-assessment-api
- description: Order and manage Azure Data Box devices for offline data transfer of large datasets to Azure when network bandwidth is limited or unavailable. Supports Data Box, Data Box Disk, and Data Box Heavy offe
  name: Azure Migrate Data Box API
  slug: azure-migrate-data-box-api
- description: Replicate workloads running on physical and virtual machines from a primary site to a secondary location for disaster recovery and migration. Manages recovery vaults, replication policies, protected i
  name: Azure Site Recovery API
  slug: azure-site-recovery-api
- description: Operations operations
  name: Azure Migrate Operations API
  slug: microsoft-azure-migrate-operations-api
- description: Projects operations
  name: Azure Migrate Projects API
  slug: microsoft-azure-migrate-projects-api
artifact_total: 17
collections:
- collection_type: open
  name: Azure Migrate REST API
  slug: open-microsoft-azure-migrate
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-migrate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-migrate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-migrate-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-migrate-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/migrate/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/migrate/migrate-services-overview
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/developer/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/azure-migrate/
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
  url: https://azure.microsoft.com/en-us/blog/tag/azure-migrate/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/migrate/whats-new
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
  url: https://azure.microsoft.com/en-us/products/azure-migrate
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
description: Azure Migrate provides a unified platform for discovering, assessing, and migrating on-premises servers, infrastructure, applications, databases, and data to Azure. Its REST APIs enable programmatic management of migration projects, discovery, assessment, and replication workflows for VMs, databases, and web apps.
finops:
- name: Microsoft Azure Migrate Finops
  service_category: API
  slug: microsoft-azure-migrate-finops
image: https://azure.microsoft.com/svghandler/azure-migrate/
layout: provider
modified: '2026-05-19'
name: Azure Migrate
nav: Providers
network: true
overview: 'Azure Migrate publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Projects API. Tagged areas include Assessment, Cloud Migration, Database Migration, Discovery, and Migration.


  Azure Migrate''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, support, engineering blog, and 14 more developer resources.'
plans:
- name: Microsoft Azure Migrate Plans Pricing
  plan_count: 3
  slug: microsoft-azure-migrate-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 5
  name: Microsoft Azure Migrate Rate Limits
  slug: microsoft-azure-migrate-rate-limits
scopes:
- name: Microsoft Azure Migrate Scopes
  scope_count: 1
  slug: microsoft-azure-migrate-scopes
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
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-migrate/refs/heads/main/screenshots/microsoft-azure-migrate-2026-06-20T185423.png
security:
- kind: authentication
  name: Microsoft Azure Migrate Authentication
  slug: microsoft-azure-migrate-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Migrate Domain Security
  slug: microsoft-azure-migrate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-migrate
tags:
- Assessment
- Cloud Migration
- Database Migration
- Discovery
- Migration
- Replication
- Server Migration
website: https://azure.microsoft.com/en-us/products/azure-migrate
---
