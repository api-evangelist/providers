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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-07-28'
api_count: 21
apis:
- description: Native database engine APIs for connecting and executing queries against SQL Server.
  name: SQL Server Database Engine API
  slug: sql-server-database-engine-api
- description: REST API for managing SQL Server resources in Azure.
  name: SQL Server REST API
  slug: sql-server-rest-api
- description: .NET API for programmatically managing SQL Server instances and databases.
  name: SQL Server Management Objects (SMO)
  slug: sql-server-management-objects-smo
- description: REST API for managing and accessing SQL Server Reporting Services.
  name: SQL Server Reporting Services (SSRS) API
  slug: sql-server-reporting-services-ssrs-api
- description: ODBC driver API for connecting applications to SQL Server.
  name: ODBC Driver for SQL Server
  slug: odbc-driver-for-sql-server
- description: JDBC driver for connecting Java applications to SQL Server.
  name: JDBC Driver for SQL Server
  slug: jdbc-driver-for-sql-server
- description: APIs for managing and querying SQL Server Analysis Services.
  name: SQL Server Analysis Services (SSAS) API
  slug: sql-server-analysis-services-ssas-api
- description: REST API for managing Azure SQL Database resources.
  name: Azure SQL Database REST API
  slug: azure-sql-database-rest-api
- description: REST API for creating, configuring, and managing Azure SQL Managed Instances.
  name: Azure SQL Managed Instance REST API
  slug: azure-sql-managed-instance-rest-api
- description: Native T-SQL stored procedure sp_invoke_external_rest_endpoint for calling external HTTPS REST endpoints directly from SQL Server 2025 and Azure SQL.
  name: SQL Server External REST Endpoint Invocation
  slug: sql-server-external-rest-endpoint-invocation
- description: Open-source tool that generates REST and GraphQL endpoints for SQL Server and Azure SQL databases from configuration, without writing custom API code.
  name: Data API Builder for SQL Server
  slug: data-api-builder-for-sql-server
- description: The official .NET data provider for Microsoft SQL Server and Azure SQL databases, providing ADO.NET access to SQL Server.
  name: ADO.NET Provider for SQL Server (Microsoft.Data.SqlClient)
  slug: adonet-provider-for-sql-server-microsoftdatasqlclient
- description: Stand-alone OLE DB data access API for connecting applications to SQL Server.
  name: OLE DB Driver for SQL Server
  slug: ole-db-driver-for-sql-server
- description: Programmable object model for building, managing, and executing ETL data integration packages in SQL Server.
  name: SQL Server Integration Services (SSIS) API
  slug: sql-server-integration-services-ssis-api
- description: Node.js driver (tedious/mssql) for connecting JavaScript and TypeScript applications to SQL Server and Azure SQL Database.
  name: Node.js Driver for SQL Server
  slug: nodejs-driver-for-sql-server
- description: Python drivers for connecting to SQL Server including the first-party mssql-python driver, pyodbc, and pymssql.
  name: Python Drivers for SQL Server
  slug: python-drivers-for-sql-server
- description: Microsoft Go driver (go-mssqldb) for connecting Go applications to SQL Server and Azure SQL Database using the TDS protocol.
  name: Go Driver for SQL Server
  slug: go-driver-for-sql-server
- description: Microsoft Drivers for PHP for SQL Server providing SQLSRV and PDO_SQLSRV extensions for connecting PHP applications to SQL Server.
  name: PHP Drivers for SQL Server
  slug: php-drivers-for-sql-server
- description: Ruby driver (TinyTDS) for connecting Ruby applications to SQL Server using FreeTDS DB-Library bindings.
  name: Ruby Driver for SQL Server
  slug: ruby-driver-for-sql-server
- description: Entity Framework Core database provider enabling .NET object-relational mapping with SQL Server and Azure SQL databases.
  name: Entity Framework Core SQL Server Provider
  slug: entity-framework-core-sql-server-provider
- description: PowerShell cmdlets for managing SQL Server instances, databases, and resources from the command line.
  name: SQL Server PowerShell Module
  slug: sql-server-powershell-module
artifact_total: 43
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sql-server-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/sql-server-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sql-server-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sql-server-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sql-server-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sql-server-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/sql-server-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sql-server-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sql-server-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/sql-server-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sql-server-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sql-server-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sql-server-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sql-server-trust-center.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/msft-sql-server
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.microsoft.com/en-us/sql/sql-server/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/sql-server/sql-server-2022-pricing
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/sql
- group: other
  title: ''
  type: Download
  url: https://www.microsoft.com/en-us/sql-server/sql-server-downloads
- group: company
  title: ''
  type: Blog
  url: https://cloudblogs.microsoft.com/sqlserver/
- group: operate
  title: ''
  type: Community
  url: https://techcommunity.microsoft.com/t5/sql-server/ct-p/SQLServer
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.microsoft.com/en-us/status/
- group: other
  title: ''
  type: Drivers
  url: https://learn.microsoft.com/en-us/sql/connect/sql-connection-libraries
- group: learn
  title: ''
  type: Learning
  url: https://learn.microsoft.com/en-us/sql/sql-server/educational-sql-resources
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/modules/introduction-to-sql-server-2022/
- group: auth
  title: ''
  type: Certification
  url: https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/sql
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/sql/sql-server/what-s-new-in-sql-server-2022
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
created: '2024'
description: A collection of APIs and interfaces for interacting with Microsoft SQL Server.
features:
- description: Full-featured relational database engine with comprehensive T-SQL support for queries, stored procedures, and functions.
  name: T-SQL Query Engine
- description: High availability and disaster recovery with automatic failover for mission-critical databases.
  name: Always On Availability Groups
- description: Memory-optimized tables and natively compiled stored procedures for high-throughput transaction processing.
  name: In-Memory OLTP
- description: Query external data sources including Hadoop, Azure Blob Storage, and Oracle using T-SQL.
  name: PolyBase
- description: Enterprise reporting platform for creating, managing, and delivering paginated reports.
  name: SQL Server Reporting Services
- description: ETL platform for building data integration and transformation packages.
  name: SQL Server Integration Services
- description: Generate REST and GraphQL endpoints from database tables and views without custom code.
  name: Data API Builder
- description: Call external HTTPS REST APIs directly from T-SQL using sp_invoke_external_rest_endpoint.
  name: External REST Endpoint Invocation
finops:
- name: Sql Server Finops
  service_category: API
  slug: sql-server-finops
graphqls:
- description: Open-source tool that generates REST and GraphQL endpoints for SQL Server and Azure SQL databases from configuration, without writing custom API code.
  name: Microsoft SQL Server APIs GraphQL API
  slug: sql-server-graphql
image: /assets/icons/sql-server.png
layout: provider
mcp_servers:
- description: ''
  name: sql-server-mcp.yml
  slug: sql-server-mcpyml
modified: '2026-06-20'
name: Microsoft SQL Server APIs
nav: Providers
network: true
overview: 'Microsoft SQL Server APIs publishes 2 APIs on the [APIs.io](https://apis.io/) network: SQL Server REST API and Azure SQL Database REST API. Tagged areas include Azure SQL, Cloud Database, Data Management, Database, and Microsoft.


  Microsoft SQL Server APIs'' developer surface includes changelog, CLI, authentication, getting-started guide, pricing, support, engineering blog, and 24 more developer resources.'
plans:
- name: Sql Server Plans Pricing
  plan_count: 3
  slug: sql-server-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Sql Server Rate Limits
  slug: sql-server-rate-limits
score:
  band: developing
  composite: 51.0
  delta: -0.4
  facets:
    commercial_clarity: 78.9
    contract_quality: 32.3
    developer_ergonomics: 52.2
    discoverability: 81.5
    governance: 3.1
    operational_transparency: 63.2
  previous_composite: 51.4
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sql-server/refs/heads/main/screenshots/sql-server-2026-06-20T194427.png
security:
- kind: authentication
  name: Sql Server Authentication
  slug: sql-server-authentication
  summary_line: sql-login/windows-integrated/oauth2/mutualTLS · 0 schemes
- kind: domain-security
  name: Sql Server Domain Security
  slug: sql-server-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sql Server Vulnerability Disclosure
  slug: sql-server-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Sql Server Trust Center
  slug: sql-server-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA / HITRUST, FedRAMP, GDPR, CSA STAR
slug: sql-server
tags:
- Azure SQL
- Cloud Database
- Data Management
- Database
- Microsoft
- Relational Database
- SQL
use_cases:
- description: Store and manage enterprise data with ACID compliance, security, and high availability.
  name: Enterprise Data Management
- description: Build BI solutions with reporting services, analysis services, and data integration.
  name: Business Intelligence
- description: Migrate on-premises SQL Server databases to Azure SQL Database or Managed Instance.
  name: Cloud Database Migration
- description: Use SQL Server as the data tier for web, mobile, and enterprise applications.
  name: Application Backend
- description: Build data warehouses with columnstore indexes, partitioning, and ETL pipelines.
  name: Data Warehousing
website: https://portal.azure.com
---
