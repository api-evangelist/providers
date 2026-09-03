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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Microsoft Sql Server Agentic Access
  operation_count: 12
  slug: microsoft-sql-server-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 14
apis:
- description: .NET API for managing and administering SQL Server programmatically.
  name: SQL Server Management Objects (SMO) API
  slug: sql-server-management-objects-smo-api
- description: API for managing SSIS packages, projects, and execution in the SSIS Catalog.
  name: SQL Server Integration Services (SSIS) Catalog API
  slug: sql-server-integration-services-ssis-catalog-api
- description: REST API for creating, configuring, and managing Azure SQL Managed Instances including databases, operations, and scheduling.
  name: Azure SQL Managed Instance REST API
  slug: azure-sql-managed-instance-rest-api
- description: Open source configuration-based engine that creates REST and GraphQL APIs for SQL Server, Azure SQL, Azure Cosmos DB, PostgreSQL, and MySQL databases.
  name: Data API Builder
  slug: data-api-builder
- description: REST API for managing Azure Analysis Services resources and performing asynchronous data refreshes of tabular models.
  name: Azure Analysis Services REST API
  slug: azure-analysis-services-rest-api
- description: ADO.NET data provider for .NET Framework and .NET Core used for connecting to SQL Server, executing commands, and retrieving results.
  name: Microsoft SqlClient Data Provider (ADO.NET)
  slug: microsoft-sqlclient-data-provider-adonet
- description: Type 4 JDBC driver providing database connectivity to SQL Server through standard JDBC application program interfaces on the Java platform.
  name: Microsoft JDBC Driver for SQL Server
  slug: microsoft-jdbc-driver-for-sql-server
- description: ODBC driver providing native-code API connectivity to SQL Server and Azure SQL Database for applications on Windows, Linux, and macOS.
  name: Microsoft ODBC Driver for SQL Server
  slug: microsoft-odbc-driver-for-sql-server
- description: Stand-alone OLE DB data access API for low-level COM components requiring high-performance access to SQL Server.
  name: Microsoft OLE DB Driver for SQL Server
  slug: microsoft-ole-db-driver-for-sql-server
- description: Python driver using Direct Database Connectivity for direct connections to SQL Server without requiring an external driver manager, compliant with Python DB-API 2.0.
  name: Microsoft Python Driver for SQL Server (mssql-python)
  slug: microsoft-python-driver-for-sql-server-mssql-python
- description: Open-source JavaScript implementation of the TDS protocol for connecting to SQL Server from Node.js on Windows, Linux, or macOS.
  name: Node.js Driver for SQL Server (tedious)
  slug: nodejs-driver-for-sql-server-tedious
- baseURL: https://your-server.database.windows.net
  baseurl_source: declared
  description: The Azure SQL Databases API from Microsoft SQL Server — 3 operation(s) for azure sql databases.
  name: Microsoft SQL Server Azure SQL Databases API
  slug: microsoft-sql-server-azure-sql-databases-api
- baseURL: https://your-server.database.windows.net
  baseurl_source: declared
  description: The Azure SQL Servers API from Microsoft SQL Server — 1 operation(s) for azure sql servers.
  name: Microsoft SQL Server Azure SQL Servers API
  slug: microsoft-sql-server-azure-sql-servers-api
- baseURL: https://your-server.database.windows.net
  baseurl_source: declared
  description: The Data API Builder API from Microsoft SQL Server — 2 operation(s) for data api builder.
  name: Microsoft SQL Server Data API Builder API
  slug: microsoft-sql-server-data-api-builder-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft SQL Server - Azure SQL & Data API Builder HTTP APIs Azure SQL Databases API
  slug: open-microsoft-sql-server-azure-sql-databases-api
- collection_type: open
  name: Microsoft SQL Server - Azure SQL & Data API Builder HTTP APIs Azure SQL Databases Azure SQL Servers API
  slug: open-microsoft-sql-server-azure-sql-servers-api
- collection_type: open
  name: Microsoft SQL Server - Azure SQL & HTTP APIs Azure SQL Databases Data API Builder API
  slug: open-microsoft-sql-server-data-api-builder-api
- collection_type: open
  name: Microsoft SQL Server - Azure SQL & Data API Builder HTTP APIs
  slug: open-microsoft-sql-server
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Azure/data-api-builder/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Azure/data-api-builder/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Azure/data-api-builder/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Azure/data-api-builder/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Azure/data-api-builder/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Azure/data-api-builder/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-sql-server-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-sql-server-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-sql-server-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-sql-server-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-sql-server-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/msft-sql-server
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.microsoft.com/sql/sql-server/sql-server-get-started
- group: other
  title: ''
  type: Downloads
  url: https://www.microsoft.com/sql-server/sql-server-downloads
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/sql-server/sql-server-2022-pricing
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/sql
- group: company
  title: ''
  type: Blog
  url: https://cloudblogs.microsoft.com/sqlserver/
- group: operate
  title: ''
  type: Community
  url: https://techcommunity.microsoft.com/t5/sql-server/ct-p/SQLServer
- group: learn
  title: ''
  type: Training
  url: https://docs.microsoft.com/learn/sql-server/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.microsoft.com/sql/sql-server/sql-server-version-information
- group: other
  title: ''
  type: Driver History
  url: https://learn.microsoft.com/en-us/sql/connect/connect-history
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/sql-server-samples
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2025
- group: operate
  title: ''
  type: Forums
  url: https://learn.microsoft.com/en-us/answers/tags/191/sql-server
- group: other
  title: ''
  type: Feedback
  url: https://feedback.azure.com/d365community/forum/04fe6ee0-3b25-ec11-b6e6-000d3a4f0da0
- group: learn
  title: ''
  type: Videos
  url: https://learn.microsoft.com/en-us/shows/data-exposed/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/microsoft/clarity-mcp-server
created: '2024'
description: A relational database management system developed by Microsoft for enterprise-scale data management and business intelligence solutions.
finops:
- name: Microsoft Sql Server Finops
  service_category: API
  slug: microsoft-sql-server-finops
graphqls:
- description: Open source configuration-based engine that creates REST and GraphQL APIs for SQL Server, Azure SQL, Azure Cosmos DB, PostgreSQL, and MySQL databases.
  name: Microsoft SQL Server GraphQL API
  slug: microsoft-sql-server-graphql
image: https://www.microsoft.com/sql-server/logo.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Microsoft SQL Server
nav: Providers
network: true
overview: 'Microsoft SQL Server publishes 3 APIs on the [APIs.io](https://apis.io/) network: Azure SQL Databases API, Azure SQL Servers API, and Data API Builder API. Tagged areas include Cloud, Data Management, Database, Enterprise, and Relational Database.


  Microsoft SQL Server''s developer surface includes authentication, getting-started guide, pricing, support, engineering blog, training material, release notes, and 20 more developer resources.'
plans:
- name: Microsoft Sql Server Plans Pricing
  plan_count: 3
  slug: microsoft-sql-server-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Microsoft Sql Server Rate Limits
  slug: microsoft-sql-server-rate-limits
scopes:
- name: Microsoft Sql Server Scopes
  scope_count: 1
  slug: microsoft-sql-server-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 51.9
    developer_ergonomics: 61.9
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-sql-server/refs/heads/main/screenshots/microsoft-sql-server-2026-06-20T185537.png
security:
- kind: authentication
  name: Microsoft Sql Server Authentication
  slug: microsoft-sql-server-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Sql Server Domain Security
  slug: microsoft-sql-server-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Sql Server Vulnerability Disclosure
  slug: microsoft-sql-server-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-sql-server
tags:
- Cloud
- Data Management
- Database
- Enterprise
- Relational Database
- SQL
website: https://www.microsoft.com/sql-server
---
