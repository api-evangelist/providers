---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Microsoft Sql Server Agentic Access
  operation_count: 12
  slug: microsoft-sql-server-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 3
apis:
- description: .NET API for managing and administering SQL Server programmatically.
  name: SQL Server Management Objects (SMO) API
  slug: sql-server-management-objects-smo-api
- description: API for managing SSIS packages, projects, and execution in the SSIS Catalog.
  name: SQL Server Integration Services (SSIS) Catalog API
  slug: sql-server-integration-services-ssis-catalog-api
- description: Open source configuration-based engine that creates REST and GraphQL APIs for SQL Server, Azure SQL, Azure Cosmos DB, PostgreSQL, and MySQL databases.
  name: Data API Builder
  slug: data-api-builder
- description: REST API for managing Azure Analysis Services resources and performing asynchronous data refreshes of tabular models.
  name: Azure Analysis Services REST API
  slug: azure-analysis-services-rest-api
- description: ADO.NET data provider for .NET Framework and .NET Core used for connecting to SQL Server, executing commands, and retrieving results.
  name: Microsoft SqlClient Data Provider (ADO.NET)
  slug: microsoft-sqlclient-data-provider-ado-net
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
  slug: node-js-driver-for-sql-server-tedious
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Azure SQL Databases API from Microsoft SQL Server — 3 operation(s) for azure sql databases.
  name: Microsoft SQL Server Azure SQL Databases API
  slug: microsoft-sql-server-azure-sql-databases-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Azure SQL Servers API from Microsoft SQL Server — 1 operation(s) for azure sql servers.
  name: Microsoft SQL Server Azure SQL Servers API
  slug: microsoft-sql-server-azure-sql-servers-api
- baseURL: https://your-server.database.windows.net
  baseurl_source: declared
  description: The Data API Builder API from Microsoft SQL Server — 2 operation(s) for data api builder.
  name: Microsoft SQL Server Data API Builder API
  slug: microsoft-sql-server-data-api-builder-api
- description: .NET API for programmatically managing SQL Server instances and databases.
  name: SQL Server Management Objects (SMO)
  slug: sql-server-management-objects-smo
- description: ODBC driver API for connecting applications to SQL Server.
  name: ODBC Driver for SQL Server
  slug: odbc-driver-for-sql-server
- description: JDBC driver for connecting Java applications to SQL Server.
  name: JDBC Driver for SQL Server
  slug: jdbc-driver-for-sql-server
- description: APIs for managing and querying SQL Server Analysis Services.
  name: SQL Server Analysis Services (SSAS) API
  slug: sql-server-analysis-services-ssas-api
- description: Native T-SQL stored procedure sp_invoke_external_rest_endpoint for calling external HTTPS REST endpoints directly from SQL Server 2025 and Azure SQL.
  name: SQL Server External REST Endpoint Invocation
  slug: sql-server-external-rest-endpoint-invocation
- description: Open-source tool that generates REST and GraphQL endpoints for SQL Server and Azure SQL databases from configuration, without writing custom API code.
  name: Data API Builder for SQL Server
  slug: data-api-builder-for-sql-server
- description: The official .NET data provider for Microsoft SQL Server and Azure SQL databases, providing ADO.NET access to SQL Server.
  name: ADO.NET Provider for SQL Server (Microsoft.Data.SqlClient)
  slug: ado-net-provider-for-sql-server-microsoft-data-sqlclient
- description: Stand-alone OLE DB data access API for connecting applications to SQL Server.
  name: OLE DB Driver for SQL Server
  slug: ole-db-driver-for-sql-server
- description: Programmable object model for building, managing, and executing ETL data integration packages in SQL Server.
  name: SQL Server Integration Services (SSIS) API
  slug: sql-server-integration-services-ssis-api
- description: Node.js driver (tedious/mssql) for connecting JavaScript and TypeScript applications to SQL Server and Azure SQL Database.
  name: Node.js Driver for SQL Server
  slug: node-js-driver-for-sql-server
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
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Databases API from Microsoft SQL Server — 11 operation(s) for databases.
  name: Microsoft SQL Server Databases API
  slug: microsoft-sql-server-databases-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ManagedInstances API from Microsoft SQL Server — 12 operation(s) for managedinstances.
  name: Microsoft SQL Server Managed Instances API
  slug: microsoft-sql-server-managedinstances-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Servers API from Microsoft SQL Server — 6 operation(s) for servers.
  name: Microsoft SQL Server Servers API
  slug: microsoft-sql-server-servers-api
artifact_total: 51
collections:
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
- group: design
  href: https://artifacts.apis.io/microsoft-sql-server/rules/microsoft-sql-server-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-sql-server-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-sql-server/json-ld/microsoft-sql-server-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-sql-server-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-sql-server/vocabulary/microsoft-sql-server-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-sql-server-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-sql-server/data-model/microsoft-sql-server-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-sql-server-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/sql/database-engine/deprecated-database-engine-features-in-sql-server-2025
- group: design
  href: https://artifacts.apis.io/microsoft-sql-server/errors/microsoft-sql-server-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-sql-server-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-sql-server/mcp/microsoft-sql-server-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-sql-server-mcp.yml
- group: other
  href: https://artifacts.apis.io/microsoft-sql-server/hosts/microsoft-sql-server-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-sql-server-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-sql-server/integrations/microsoft-sql-server-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-sql-server-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-sql-server/vendors/microsoft-sql-server-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-sql-server-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: commercial
  href: https://artifacts.apis.io/microsoft-sql-server/plans/microsoft-sql-server-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-sql-server-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-sql-server/rate-limits/microsoft-sql-server-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-sql-server-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-sql-server/finops/microsoft-sql-server-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-sql-server-finops.yml
- group: other
  href: https://artifacts.apis.io/microsoft-sql-server/capabilities/microsoft-sql-server-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-sql-server-capability-edges.yml
- group: build
  href: https://artifacts.apis.io/microsoft-sql-server/packages/microsoft-sql-server-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-sql-server-packages.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-sql-server/well-known/microsoft-sql-server-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-sql-server-well-known.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-sql-server/well-known/microsoft-sql-server-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-sql-server-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-sql-server/llms/microsoft-sql-server-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-sql-server-llms.txt
- group: design
  href: https://artifacts.apis.io/microsoft-sql-server/conformance/microsoft-sql-server-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-sql-server-conformance.yml
- group: design
  href: https://artifacts.apis.io/microsoft-sql-server/lifecycle/microsoft-sql-server-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-sql-server-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/microsoft-sql-server/cli/microsoft-sql-server-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-sql-server-cli.yml
- group: design
  href: https://artifacts.apis.io/microsoft-sql-server/conventions/microsoft-sql-server-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-sql-server-conventions.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-sql-server/security/microsoft-sql-server-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-sql-server-trust-center.yml
- group: other
  title: ''
  type: Download
  url: https://www.microsoft.com/en-us/sql-server/sql-server-downloads
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
- group: auth
  title: ''
  type: Certification
  url: https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/sql
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
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
  url: https://github.com/Azure/data-api-builder/blob/main/LICENSE.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-sql-server/agentic-access/microsoft-sql-server-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-sql-server-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-sql-server/security/microsoft-sql-server-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-sql-server-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-sql-server/security/microsoft-sql-server-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-sql-server-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-sql-server/authentication/microsoft-sql-server-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-sql-server-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-sql-server/scopes/microsoft-sql-server-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-sql-server-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/msft-sql-server
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
  url: https://support.microsoft.com/en-us/contactus
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/sql/sql-server/
- group: company
  title: ''
  type: Blog
  url: https://cloudblogs.microsoft.com/sqlserver/
- group: operate
  title: ''
  type: Community
  url: https://techcommunity.microsoft.com/t5/sql-server/ct-p/SQLServer
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
created: '2024'
description: Microsoft SQL Server is Microsoft's relational database management system for enterprise data management, analytics and business intelligence. Its programmable surfaces span client drivers (ADO.NET, JDBC, ODBC, OLE DB, Python, Node.js), SMO, SSIS and SSAS management APIs, Data API Builder with its SQL MCP Server, and the Azure SQL Database and Managed Instance REST APIs on Azure Resource Manager.
finops:
- has_sources: true
  method: derived
  name: Microsoft Sql Server Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-sql-server-finops
  template: true
graphqls:
- description: Open source configuration-based engine that creates REST and GraphQL APIs for SQL Server, Azure SQL, Azure Cosmos DB, PostgreSQL, and MySQL databases.
  name: Microsoft SQL Server GraphQL API
  slug: microsoft-sql-server-graphql
image: https://www.microsoft.com/sql-server/logo.png
json_schemas:
- name: DatabaseListResult
  property_count: 2
  slug: microsoft-sql-server-database-list-result
- name: Database
  property_count: 6
  slug: microsoft-sql-server-database
jsonld:
- class_count: 2
  name: Microsoft Sql Server Context
  property_count: 8
  slug: microsoft-sql-server-context
layout: provider
mcp_servers:
- description: 'Microsoft''s SQL MCP Server, part of the open-source Data API builder (DAB) runtime, exposes SQL Server / Azure SQL entities to MCP clients. It is self-hosted by the customer; Microsoft runs no hosted '
  name: SQL MCP Server (Data API builder)
  slug: sql-mcp-server-data-api-builder
modified: '2026-05-19'
name: Microsoft SQL Server
nav: Providers
network: true
overview: 'Microsoft SQL Server publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including Azure SQL Databases API, Azure SQL Servers API, Data API Builder API, and 29 more. Tagged areas include Cloud, Data Management, Database, Enterprise, and Relational Database.


  The Microsoft SQL Server catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft SQL Server''s developer surface includes getting-started guide, CLI, developer portal, authentication, pricing, support, documentation, and 53 more developer resources.'
plans:
- name: Microsoft Sql Server Plans Pricing
  plan_count: 0
  slug: microsoft-sql-server-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Microsoft Sql Server Rate Limits
  slug: microsoft-sql-server-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Microsoft SQL Server API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: microsoft-sql-server-rules
scopes:
- name: Microsoft Sql Server Scopes
  scope_count: 1
  slug: microsoft-sql-server-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: exemplar
  composite: 66.7
  coverage:
    artifact_dirs: 33
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.3
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 54.6
    developer_ergonomics: 78.6
    discoverability: 70.0
    operational_transparency: 60.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 61.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/microsoft-sql-server/microsoft-sql-server-2026-06-20T185537.png
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
- kind: trust-center
  name: Microsoft Sql Server Trust Center
  slug: microsoft-sql-server-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA / HITRUST, FedRAMP, GDPR, CSA STAR
slug: microsoft-sql-server
tags:
- Cloud
- Data Management
- Database
- Enterprise
- Relational Database
- SQL
website: https://www.microsoft.com/
---
